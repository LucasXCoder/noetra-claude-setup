---
# ============================================================================
# NOETRA DESIGN SYSTEM — source of truth for ALL Noetra UI
# Dashboards · landing pages · agent surfaces · tools. Original system.
# Aesthetic: Apple-grade polish · cinematic depth · 3D · glassmorphism ·
#            physics-based motion · premium dark · awwwards-tier.
# Format: YAML tokens (machine) on top, Markdown rules (human/agent) below.
# ============================================================================
name: Noetra
mode: dark-first        # light is a derived theme, dark is canonical
philosophy: >
  Depth over decoration. Every surface sits in real space — light falls, glass
  refracts, things move with weight. Restraint at rest, alive on interaction.
  Never templated, never flat-by-default, never "AI beige."

color:
  # --- base voids (cool near-black, not pure #000) ---
  void:        "#06070B"   # app background, deepest layer
  bg:          "#0A0B11"   # default surface
  raise1:      "#10121A"   # cards / elevated panels
  raise2:      "#171A25"   # popovers / modals
  hairline:    "#23273440" # 1px borders (alpha)
  # --- text ---
  fg:          "#EEF0F6"   # primary text
  fg_muted:    "#A4A9B8"   # secondary text
  fg_faint:    "#5C6273"   # tertiary / disabled
  # --- signature accents ---
  iris:        "#6D5DF6"   # PRIMARY — electric indigo (brand, CTAs, focus)
  iris_bright: "#8B7CFF"   # hover / glow core
  aurora:      "#38E1FF"   # SECONDARY — cyan, highlights, data, links
  plasma:      "#FF6B5C"   # WARM signal — alerts, energy, destructive (Odysseus-red lineage)
  mint:        "#54E8B0"   # success / positive
  amber:       "#FFC24B"   # warning
  # --- gradients (cinematic mesh/aurora) ---
  grad_brand:  "linear-gradient(135deg,#6D5DF6 0%,#38E1FF 100%)"
  grad_plasma: "linear-gradient(135deg,#FF6B5C 0%,#FFC24B 100%)"
  grad_mesh:   "radial-gradient(60% 80% at 20% 10%,#6D5DF633,transparent), radial-gradient(50% 60% at 90% 20%,#38E1FF22,transparent), radial-gradient(80% 90% at 50% 110%,#FF6B5C1A,transparent)"

glass:                     # the house material — use everywhere surfaces float
  fill:        "rgba(255,255,255,0.04)"
  fill_strong: "rgba(255,255,255,0.07)"
  border:      "rgba(255,255,255,0.10)"
  highlight:   "inset 0 1px 0 0 rgba(255,255,255,0.14)"   # top inner light edge
  blur:        "18px"
  saturate:    "140%"
  recipe: "background:var(--glass-fill); backdrop-filter:blur(18px) saturate(140%); border:1px solid var(--glass-border); box-shadow:var(--glass-highlight), var(--elev-2);"

elevation:                 # cinematic shadows — soft, layered, colored ambient
  e0: "none"
  e1: "0 1px 2px rgba(0,0,0,.4)"
  e2: "0 8px 24px -8px rgba(0,0,0,.55)"
  e3: "0 20px 60px -16px rgba(0,0,0,.65)"
  e4: "0 40px 120px -24px rgba(0,0,0,.7)"
  glow_iris:   "0 0 0 1px #6D5DF655, 0 8px 40px -6px #6D5DF666"
  glow_aurora: "0 0 32px -4px #38E1FF66"

radius:
  xs: "6px"
  sm: "10px"
  md: "16px"   # default for cards/inputs
  lg: "24px"
  xl: "32px"
  pill: "999px"

space:                     # 4px base, 8px rhythm
  base: "4px"
  scale: [0, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192]

typography:
  display: "'Geist', 'SF Pro Display', 'Inter', system-ui, sans-serif"   # hero / numbers
  sans:    "'Inter', 'SF Pro Text', system-ui, sans-serif"               # body / UI
  mono:    "'Geist Mono', 'JetBrains Mono', ui-monospace, monospace"      # code / data / labels
  # fluid scale (clamp: min, vw, max)
  scale:
    hero:  "clamp(2.75rem, 6vw, 5.5rem)"   # weight 600, letter-spacing -0.03em, line 1.02
    h1:    "clamp(2rem, 3.5vw, 3rem)"       # -0.025em
    h2:    "clamp(1.5rem, 2.2vw, 2rem)"
    h3:    "1.25rem"
    body:  "1rem"        # line-height 1.6
    small: "0.875rem"
    label: "0.6875rem"   # uppercase, letter-spacing 0.12em, weight 600 (mono)
  weights: {regular: 400, medium: 500, semibold: 600}

motion:                    # physics-first. spring > linear easing.
  ease_out:    "cubic-bezier(0.16, 1, 0.3, 1)"     # default UI ease (expo-out feel)
  ease_inout:  "cubic-bezier(0.65, 0, 0.35, 1)"
  ease_spring: "cubic-bezier(0.34, 1.56, 0.64, 1)" # subtle overshoot (use sparingly)
  spring_soft:  {stiffness: 210, damping: 26, mass: 1}    # cards, layout
  spring_snappy:{stiffness: 420, damping: 30, mass: 0.8}  # buttons, toggles
  spring_loose: {stiffness: 120, damping: 18, mass: 1.1}  # large/hero, parallax
  duration: {instant: "80ms", fast: "160ms", base: "240ms", slow: "420ms", cinematic: "720ms"}
  rule: "Animate transform + opacity only. Never animate layout/width/top. Honor prefers-reduced-motion."

depth_3d:                  # 3D & spatial guidance
  stack: "react-three-fiber + drei (R3F) for scenes; Spline for art-directed hero objects; CSS 3D transforms for lightweight cards."
  layers: ["bg mesh gradient", "far parallax (z -200)", "content plane (z 0)", "floating glass (z +40)", "cursor/pointer light (z +80)"]
  parallax: "Pointer + scroll drive subtle translateZ/rotateX (max ±6deg tilt, ±20px shift). Spring-damped, never 1:1."
  perf: "Lazy-load/Suspense 3D. Cap DPR at 2. Pause raf when offscreen/tab-hidden. <16ms frames. Fallback static poster if WebGL unavailable or reduced-motion."

stack_default:             # what to build with unless the repo says otherwise
  web: "React + TypeScript + Vite, Tailwind tokens mapped to these vars, motion/react (Framer Motion), R3F for 3D, GSAP for scroll timelines."
  tokens: "Expose every color/space/radius as CSS custom properties (--noetra-*). Tailwind theme extends from them — single source of truth."

a11y:
  contrast: "Body text ≥ 4.5:1 on its surface. Never rely on glow alone for state."
  focus: "Visible focus ring = 2px iris + 2px offset (glow_iris on interactive)."
  motion: "All motion gated behind prefers-reduced-motion: reduce → cross-fade only, no parallax/3D auto-spin."
  targets: "Min 40×40px hit area."
---

# Noetra Design System — Rules

This file governs **all** Noetra UI. Read it before any frontend work. Pair it with the
installed skills: **impeccable** + **taste-skill** (anti-slop direction), **design-motion-principles**
(motion), **ui-ux-pro-max** / **soft-skill** (polish), **liquid-glass-design** (glass material).

## 1. Core principles
1. **Depth is the brand.** Nothing is flat-by-default. Every surface has a light source (top),
   a shadow below, and — when floating — glass. Build in layers (see `depth_3d.layers`).
2. **Restraint at rest, alive on interaction.** Calm, dark, spacious when idle. Motion, glow,
   and parallax wake up on hover/scroll/pointer — never auto-distracting.
3. **One accent does the work.** `iris` (electric indigo) is the brand. `aurora` (cyan) for
   highlights/data/links. `plasma` for energy/destructive. Don't rainbow.
4. **Cinematic, not noisy.** Mesh gradients + soft colored shadows create mood; keep type and
   layout impeccably clean over that mood.
5. **Premium = precision.** Optical alignment, consistent radii, true vertical rhythm (8px),
   hairline borders, no default browser anything.

## 2. Color usage
- App background: `void`; surfaces step up `bg → raise1 → raise2` by elevation.
- Behind heroes/sections, layer `grad_mesh` at low opacity for depth (never on text containers).
- Text: `fg` / `fg_muted` / `fg_faint` only. Accent text reserved for links + emphasis.
- Borders are **hairline** (`hairline`) or glass border — never solid gray 1px boxes.
- `plasma` is the only "warm" — alerts, destructive, urgency. `mint`/`amber` for status only.

## 3. The glass material (house signature)
Use `glass.recipe` for floating panels, nav bars, cards-on-media, modals, tooltips, command
palettes. Always include the **top inner highlight** (`glass.highlight`) — it's what makes glass
read as glass. Glass needs something behind it (gradient/media/3D) to refract; never glass on flat bg.

## 4. Typography
- `display` for hero numerals + headlines (tight tracking, `-0.03em`, weight 600).
- `sans` for everything UI/body (line-height 1.6 body, 1.2 headings).
- `mono` for labels/eyebrows (uppercase, `label` size, `0.12em` tracking), data, code.
- Fluid `clamp()` scale — never fixed px for headings. Max line length ~68ch.

## 5. Motion (physics-first)
- Default transition: `transform`/`opacity` over `duration.base` with `ease_out`.
- Use **springs** (`motion.spring_*`) for anything interactive or entering — weight beats linear.
- Stagger lists/cards 40–70ms. Page/section reveals on scroll: fade-up 16–24px + `spring_loose`.
- `ease_spring` overshoot only on small confirmations (toggle, like, add). Never on large blocks.
- **Always** honor `prefers-reduced-motion` (see `a11y.motion`). 60fps or it doesn't ship.

## 6. 3D & spatial depth
- Hero: an R3F or Spline floating object (glass/metal/iridescent), pointer-parallaxed, spring-damped.
- Cards: subtle 3D tilt on hover (max ±6°) with a moving specular highlight + lift (`elevation.e3`).
- Background: animated mesh gradient or low-poly field, very slow, blurred, behind glass.
- Respect `depth_3d.perf` — lazy-load, cap DPR, pause offscreen, static fallback always.

## 7. Components (defaults)
- **Button (primary):** `grad_brand` fill OR solid `iris`, radius `md`, `glow_iris` on hover,
  `spring_snappy` press (scale .97). Text `fg`/white, weight 500.
- **Button (ghost):** transparent, `hairline` border → glass fill + `iris` border on hover.
- **Card:** `raise1` or glass, radius `lg`, `elevation.e2`→`e3` on hover, inner highlight.
- **Input:** `raise1`, hairline border, radius `md`; focus → iris ring + faint `glow_iris`.
- **Nav:** sticky glass bar, blur, hairline bottom; shrinks + intensifies blur on scroll.
- **Modal/overlay:** scrim `rgba(6,7,11,.6)` + blur; panel = glass `raise2`, radius `xl`, `e4`,
  enter via `spring_soft` scale .96→1 + fade.
- **Bento grid:** primary landing/dashboard layout — varied tile sizes, glass tiles over mesh.

## 8. Hard don'ts (anti-slop)
- ❌ Pure black `#000` / pure white surfaces · ❌ flat gray cards with hard 1px borders
- ❌ default Tailwind blue/indigo-500 look · ❌ generic drop shadows (`0 4px 6px`) — use `elevation.*`
- ❌ linear/instant transitions on interactive elements · ❌ centered-everything hero with one CTA
- ❌ emoji as primary icons (use a real icon set) · ❌ glow as the only state signal
- ❌ rainbow accents · ❌ auto-playing distracting motion · ❌ animating layout properties

## 9. Provenance
Original system. Token discipline (CSS custom properties, accent-driven states, dark base) carried
from the Odysseus design language; `plasma` nods to Odysseus's `--red`. Everything else is Noetra's own.
