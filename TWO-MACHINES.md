# Two machines, two Claudes (Mac = lead, PC = worker)

"Worker" is just a name: the Claude session running on the PC. You talk to the Mac Claude (the lead). It sends text messages to the PC Claude, the PC does the heavy work, and replies.

## Setup (once, about 10 minutes)
1. **Both machines:** same claude.ai account (`/login`), Claude Code up to date (`claude update`). Mac needs v2.1.225+, Windows v2.1.234+. Check with `claude --version`.
2. **Same code on both:** clone the same GitHub repo on the Mac and the PC. Messages carry text only, never files, so git is how code moves: whoever finishes pushes a branch, the other pulls.
3. **PC stays awake:** Windows sleep = Never, keep the terminal open.

## Every time
**PC**, in the project folder:
    claude --remote-control --name pc

**Mac**, in the project folder:
    claude --remote-control --name mac

(Use the same permission mode on both; do not run one in bypass mode and the other not, or messages get held for approval.)

## Check it works (2 minutes)
On the Mac, say: `List my sessions.` You should see `pc` marked Remote Control.
Then: `Ask @pc to run git log -1 and tell me what it says.` The answer should come back.

## How to use it
- "Tell @pc to run the full test suite and report back."
- "Have @pc build the API in a worktree on branch api and push when green; I will do the UI here."
- "Tell me when @pc finishes what it is working on."  (same-machine only; across machines just ask it to message you when done)
- Anything the PC needs approved shows up as a prompt on the PC (or in claude.ai/code). A message can never approve it for you, so pre-allow the commands the PC needs or use auto mode on the PC.

## Limits to remember
- Plain text only, no files or history. Use git to share code.
- If the PC shows `offline`, messages arrive when it reconnects.
- Each session spends your Max allowance. Remote Control and messaging need a claude.ai login, not an API key.
- Untested between your two machines until you run the 2-minute check above.

Simpler fallback: run only the PC session and drive it from the Mac browser at claude.ai/code (`claude remote-control` on the PC).
