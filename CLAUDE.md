# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
npm install

# Development build (watch mode) — use this during development
npm run watch              # Runs all watch tasks: esbuild + tsc for extension, web worker, simulation

# Type-check only (no output)
npm run typecheck

# Production build
npm run build              # minified, no source maps
npm run compile            # dev build (not suitable for checking errors — use typecheck or watch)

# Lint
npm run lint               # ESLint with zero warnings allowed
npm run lint-staged        # Lint staged files only

# Tests
npm run test:unit          # Vitest unit tests (*.spec.ts, *.spec.tsx)
npm run test:extension     # VS Code integration tests (runs in the extension host)
npm run simulate           # Simulation tests (reaches out to Copilot APIs — expensive, LLM-based)

# Run a single unit test file
npx vitest run src/path/to/file.spec.ts

# Format
npm run prettier
npm run tsfmt              # TypeScript formatting check/apply
```

> **ALWAYS** monitor the `watch:tsc-extension` task output for compilation errors. **Never** use `npm run compile` as a correctness check — it succeeds even with type errors. Fix all TS errors before considering work done.

## Architecture Overview

This is the **GitHub Copilot Chat** VS Code extension — a TypeScript/TSX extension that provides conversational AI, inline editing, agent mode, and code completions within VS Code.

### Source Directory Layout

```
src/
  util/          # Pure utilities. No VS Code runtime access. Can be used by tests outside VS Code.
  platform/      # Platform services (search, telemetry, parsing, embeddings, git, openai, ...).
                 # May import from util. Cannot import from extension/.
  extension/     # All feature implementations. Can import from util and platform.
  shared-fetch-utils/  # Shared HTTP fetch utilities
test/            # Simulation tests, e2e tests, scenario tests (.stest.ts files)
```

**Rule**: `util` ← `platform` ← `extension`. Never import upward.

### Runtime Layers

Every source file must live in a folder named after its supported runtime layer. ESLint enforces this:

| Layer | Allowed APIs |
|---|---|
| `common` | TypeScript builtins only (no VS Code runtime, no Node.js) |
| `vscode` | VS Code APIs + common |
| `node` | Node.js APIs + common |
| `vscode-node` | VS Code APIs + Node.js APIs (desktop only) |
| `worker` | Web Worker APIs + common |
| `vscode-worker` | VS Code APIs + Web Worker APIs (serverless web) |

**Prefer `common` and `vscode` layers** so features work in both desktop and serverless web. Node.js-specific code goes in `node` / `vscode-node`.

### Extension Entry Points

- `src/extension/extension/vscode/extension.ts` — Base activation (both runtimes)
- `src/extension/extension/vscode-node/extension.ts` — Node.js activation
- `src/extension/extension/vscode-worker/extension.ts` — Web worker activation

Contributions and services are registered in these three pairs of files (one per runtime):
- `contributions.ts` / `services.ts` in `extension/vscode/`, `extension/vscode-node/`, `extension/vscode-worker/`

### Service System

The codebase uses VS Code-style dependency injection via `IInstantiationService`. Prefer `I*Service` interfaces over raw APIs:

- Use `IFileSystemService` not `fs` or `vscode.workspace.fs`
- Use `ILogService` not `console.log`
- This enables unit testing without VS Code, simulation test support, and cross-platform (Node vs web) abstractions.

### Key Feature Locations

| Area | Path |
|---|---|
| Chat participants / agent mode | `src/extension/conversation/` |
| Inline chat (`Ctrl+I`) | `src/extension/inlineChat/` |
| Inline edits / NES | `src/extension/inlineEdits/` |
| Agent agentic loop | `src/extension/intents/node/toolCallingLoop.ts` |
| Agent prompt (main) | `src/extension/prompts/node/agent/agentPrompt.tsx` |
| Agent system prompt | `src/extension/prompts/node/agent/agentInstructions.tsx` |
| Tool implementations | `src/extension/tools/node/` |
| Tool names (model-facing) | `src/extension/tools/common/toolNames.ts` |
| Language model endpoints | `src/extension/endpoint/` |
| Context resolution | `src/extension/context/` |
| Workspace semantic search | `src/extension/workspaceSemanticSearch/` |
| Workspace chunk search | `src/extension/workspaceChunkSearch/` |
| MCP integration | `src/extension/mcp/` |
| Authentication | `src/extension/authentication/` |
| BYOK (bring your own key) | `src/extension/byok/` |
| Telemetry | `src/extension/telemetry/` |
| Platform: OpenAI protocol | `src/platform/openai/` |
| Platform: Embeddings | `src/platform/embeddings/` |
| Platform: Code parsing | `src/platform/parser/` |

### Claude Code Integration

Located at `src/extension/chatSessions/claude/`. This integrates the `@anthropic-ai/claude-agent-sdk` to run Claude Code sessions inside VS Code Chat. Key files:

- `node/claudeCodeAgent.ts` — `ClaudeAgentManager` (routes requests) + `ClaudeCodeSession` (single conversation)
- `node/claudeCodeSdkService.ts` — Thin DI wrapper around the SDK
- `node/sessionParser/claudeCodeSessionService.ts` — Loads/resumes persisted sessions from `~/.claude/projects/`
- `common/claudeTools.ts` — Tool name enum and input type definitions
- `node/hooks/claudeHookRegistry.ts` — Registry for SDK lifecycle hooks
- `vscode-node/slashCommands/claudeSlashCommandRegistry.ts` — Registry for `/commands`
- `common/claudeMcpServerRegistry.ts` — Registry for MCP server contributors

Upgrading `@anthropic-ai/claude-agent-sdk`: follow the process in `.claude/agents/anthropic-sdk-upgrader.md`.

### Prompt Engineering (TSX)

Prompts are built using `@vscode/prompt-tsx` with a custom JSX factory:
- JSX factory: `vscpp` (not `React.createElement`)
- Fragment factory: `vscppf`
- Prompt components live under `src/extension/prompts/`

### Adding a New Tool

1. Add entry under `contributes.languageModelTools` in `package.json` (description, schema)
2. Add to `ToolName` enum in `src/extension/tools/common/toolNames.ts`
3. Implement in `src/extension/tools/node/` (implement `vscode.LanguageModelTool` or `ICopilotTool`)
4. Register: `ToolRegistry.registerTool(YourTool)` and import in `allTools.ts`
5. Read `docs/tools.md` before adding any tool — it covers confirmations, UI patterns, and best practices

## Coding Conventions

- **Indentation**: Tabs (enforced by ESLint)
- **Quotes**: Double quotes for user-visible/localizable strings, single quotes for internal strings
- **Arrow functions**: Prefer `x => x` over `(x) => x` — only wrap params when necessary
- **Curly braces**: Always use them for loops/conditionals; opening brace on same line
- **Types**: Avoid `any`. Use `readonly` wherever possible. Use proper interfaces instead of casts.
- **Exports**: Only export what needs to be shared across components
- **URIs**: Always use `vscode.Uri` (or the internal `URI` type) instead of string file paths

All source files require the Microsoft copyright header. ESLint enforces this.

## Testing Conventions

- **Unit tests** (`*.spec.ts` / `*.spec.tsx`): Vitest, live next to source in `/test/` subdirectories. Run with `npm run test:unit`.
- **Integration tests** (`*.test.ts` in `test/` root): Run inside VS Code extension host with `npm run test:extension`.
- **Simulation tests** (`*.stest.ts`): LLM-based end-to-end tests. Expensive; results snapshotted in `test/simulation/baseline.json`. Run with `npm run simulate`.

The VS Code `vscode` module is shimmed for unit tests via `src/util/common/test/shims/vscodeTypesShim.ts`.

## VS Code Proposed APIs

The extension uses many proposed VS Code APIs declared in `src/extension/vscode.proposed.*.d.ts` files. When adopting a breaking API change, update the version in `package.json`'s `enabledApiProposals` (e.g., `lmTools@2`) and update `engines.vscode` for additive changes.

## Debugging

Run the `Launch Copilot Extension - Watch Mode` debug configuration in VS Code (or `Launch Copilot Extension` if the watch mode version fails).

To inspect model requests: run the command **"Show Chat Debug View"** in VS Code. This shows each request's prompt, tools, and response. Always check the rendered prompt when changing prompt code.
