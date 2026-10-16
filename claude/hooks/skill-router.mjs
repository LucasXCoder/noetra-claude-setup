#!/usr/bin/env node
// UserPromptSubmit: no-LLM router for skills hidden from the listing (skillOverrides "name-only").
// Matches the prompt against each hidden skill's name + description and, on a confident match,
// tells Claude which skill to load. Costs nothing on prompts that match nothing. Always exits 0.
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';

const CLAUDE = join(process.env.USERPROFILE || homedir(), '.claude');
const MIN_SCORE = 3;  // a rare skill-name word scores 3, a description word 1
const MAX_SHOWN = 3;
const STOP = new Set(('a an the and or of to for in on with is are be use used using when this that it as at by from your you any '
  + 'not if do does how what which can will should skill code new add make build create need want help get set run file files '
  + 'project them they their into out up all also more than only about using based work works one').split(' '));

// Name words too generic to prove relevance on their own.
const GENERIC = new Set('testing patterns design builder audit check review optimizer optimization advisor enforcement foundations onboarding existing projects'.split(' '));
const words = (t) => (t.toLowerCase().match(/[a-z][a-z0-9-]{2,}/g) || []).filter((w) => !STOP.has(w));

function description(skill) {
  const p = join(CLAUDE, 'skills', skill, 'SKILL.md');
  if (!existsSync(p)) return null;
  const fm = readFileSync(p, 'utf8').match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) return null;
  const m = fm[1].match(/^description:\s*(?:[>|][-+]?\s*\r?\n)?((?:[ \t]+.*\r?\n?)+|.*)/m);
  return m ? m[1].replace(/\s+/g, ' ').replace(/^["']|["']$/g, '').trim() : '';
}

function main() {
  const input = JSON.parse(readFileSync(0, 'utf8') || '{}');
  const prompt = String(input.prompt || '');
  if (prompt.length < 12) return;
  const settings = JSON.parse(readFileSync(join(CLAUDE, 'settings.json'), 'utf8'));
  const hidden = Object.entries(settings.skillOverrides || {}).filter(([, v]) => v === 'name-only').map(([k]) => k);
  if (!hidden.length) return;

  const stem = (w) => w.replace(/(ing|ers|er|ed|es|s)$/, '');
  const near = (a, b) => a === b || (a.length >= 4 && b.length >= 4 && (a.startsWith(b) || b.startsWith(a)));
  const promptStems = [...new Set(words(prompt).map(stem))];
  const inPrompt = (w) => promptStems.some((p) => near(p, stem(w)));
  const docs = hidden.map((name) => ({ name, desc: description(name.replace(/^ckm:/, '')) ?? description(name) ?? '' }));
  // A word that names many skills ("testing", "design") is weak evidence; rare name words are strong.
  const nameDf = new Map();
  for (const d of docs) for (const w of new Set(words(d.name.replace(/[-:]/g, ' ')))) nameDf.set(w, (nameDf.get(w) || 0) + 1);
  const descDf = new Map();
  for (const d of docs) for (const w of new Set(words(d.desc))) descDf.set(w, (descDf.get(w) || 0) + 1);

  const hits = [];
  for (const d of docs) {
    let score = 0;
    let strong = false;
    const matched = [];
    for (const w of new Set(words(d.name.replace(/[-:]/g, ' ')))) {
      if (inPrompt(w)) { const rare = nameDf.get(w) <= 2 && !GENERIC.has(w); score += rare ? 3 : 1; strong ||= rare; matched.push(w); }
    }
    for (const w of new Set(words(d.desc))) {
      if ((descDf.get(w) || 0) <= 4 && inPrompt(w) && !matched.includes(w)) { score += 1; matched.push(w); }
    }
    if (score >= MIN_SCORE && (strong || score >= MIN_SCORE + 2)) hits.push({ ...d, score, matched });
  }
  if (!hits.length) return;
  hits.sort((a, b) => b.score - a.score);
  const lines = hits.slice(0, MAX_SHOWN).map((h) => `- ${h.name}: ${h.desc.slice(0, 160)}`);
  const additionalContext = 'Skills that look relevant to this request but are hidden from the skill list '
    + '(load one with the Skill tool if it fits; ignore if not):\n' + lines.join('\n');
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'UserPromptSubmit', additionalContext } }));
}

try { main(); } catch { /* never block a prompt */ }
process.exit(0);
