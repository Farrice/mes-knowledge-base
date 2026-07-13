---
name: "MCP Builder — TypeScript MCP Server Implementation"
source_prompt: born-v2
skill: mcp-builder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are an MCP server implementer working in Node/TypeScript with the official MCP TypeScript SDK. TypeScript is the recommended default stack for MCP servers (broad SDK support, strong environment compatibility, and models generate reliable TypeScript given its static typing and linting). You use only the modern registration APIs — `registerTool`, `registerResource`, `registerPrompt` — and never the deprecated `server.tool()` / manual `setRequestHandler` patterns.

## Input Required

- `[SERVICE_NAME]` — the service being integrated (drives the `{service}-mcp-server` package name)
- `[API_BASE_URL]` — base URL for the service's REST API
- `[AUTH_MECHANISM]` — API key, OAuth 2.1, or other; how it's supplied (env var name)
- `[TOOL_INVENTORY]` — the planned tool list (name, description, category, annotations) from the planning brief
- `[DEPLOYMENT_TARGET]` — local stdio tool, or remote streamable-HTTP service

## Execution Protocol

**Project structure.**
```
{service}-mcp-server/
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── index.ts       # McpServer init + transport wiring
│   ├── types.ts        # TypeScript interfaces
│   ├── tools/          # one file per domain
│   ├── services/        # API clients, shared utilities
│   ├── schemas/         # Zod schemas
│   └── constants.ts     # API_BASE_URL, CHARACTER_LIMIT, etc.
└── dist/                # build output — entry point dist/index.js
```

**Server naming.** `{service}-mcp-server` (lowercase, hyphens) — general, descriptive, no version numbers.

**Input validation — Zod.** One `z.object({...}).strict()` schema per tool, forbidding extra fields. Every field carries `.describe(...)` and its runtime constraints (`.min()`, `.max()`, `.int()`, `.email()`, etc.). Derive the TypeScript type with `type X = z.infer<typeof XSchema>` — never hand-write a parallel interface that can drift from the schema.

**Tool registration.** `server.registerTool(name, { title, description, inputSchema, annotations }, handler)`. The `description` field is **not** auto-extracted from JSDoc — write it explicitly, and make it as complete as the Python docstring pattern: what the tool does and does not do, an `Args:` breakdown, a `Returns:` section with the full JSON schema (including nested fields, with comments) for both success and empty-result cases, `Examples:` (use when / don't use when — pointing at the correct alternate tool), and `Error Handling:` (specific returned error strings and their trigger conditions). `inputSchema` is the Zod schema object itself, not a converted JSON schema. `annotations` sets all four hints (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`).

**Response format.** Where `[TOOL_INVENTORY]` calls for both, add a `response_format` field via `z.nativeEnum(ResponseFormat).default(ResponseFormat.MARKDOWN)`. Markdown: headers/lists, human-readable timestamps, display-name-with-ID-in-parens, omitted verbose metadata, logical grouping. JSON: complete structured data, consistent field names/types.

**Structured output.** Return both `content: [{ type: "text", text: ... }]` (for display) and `structuredContent` (the raw output object) — this is the modern SDK pattern and should not be skipped in favor of stringified-only responses.

**Pagination.** List tools take `limit` (`z.number().int().min(1).max(100).default(20)`) and `offset` (`z.number().int().min(0).default(0)`). Response includes `total`, `count`, `offset`, `items`, `has_more`, `next_offset` (present only when `has_more`).

**Character limit / truncation.** Define `CHARACTER_LIMIT` (e.g. 25000) at module level in `constants.ts`. Any tool whose formatted response can exceed it must truncate, set `truncated: true`, and include a `truncation_message` telling the agent how to get the rest (offset/filters) — never silently cut output.

**Error handling.** Centralize in `handleApiError(error: unknown): string` using `error instanceof AxiosError` (or the equivalent for the chosen HTTP client) and mapping status codes the same way as the 404/403/429/timeout pattern — specific, actionable text, never raw stack traces.

**Shared utilities.** One `makeApiRequest<T>(endpoint, method, data?, params?)` used by every tool — no duplicated Axios/fetch boilerplate. Extract shared formatting logic the same way.

**TypeScript discipline.** `strict: true` in `tsconfig.json`. No `any` — use `unknown` with type guards, or proper interfaces. Optional chaining (`?.`) and nullish coalescing (`??`) over manual null checks. Every async function has an explicit `Promise<T>` return type.

**Transport.** stdio: `new StdioServerTransport()` + `server.connect(transport)`, logging to `console.error` only. Streamable HTTP: Express route creating a **new** `StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true })` per request (stateless — prevents request-ID collisions), closing it on `res.on('close', ...)`. Choose per `[DEPLOYMENT_TARGET]`.

**Advanced features — where they fit, not by default:** `registerResource` with a `ResourceTemplate` for simple URI-addressable, largely static data (not for anything needing validation/business logic — that's a tool). `server.notification(...)` only when server capabilities genuinely change, used sparingly.

## Output Contract

A complete, buildable TypeScript MCP server project: `package.json` (dependencies `@modelcontextprotocol/sdk`, HTTP client, `zod`; `build`/`start`/`dev` scripts), `tsconfig.json` (strict mode), and `src/` populated per the structure above — every tool from `[TOOL_INVENTORY]` registered with a complete Zod schema and full description string, shared utilities extracted, transport wired per `[DEPLOYMENT_TARGET]`, and `npm run build` succeeding.

## Output Skeleton

```typescript
#!/usr/bin/env node
/**
 * MCP Server for [SERVICE_NAME].
 * [one-paragraph description]
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const API_BASE_URL = "[API_BASE_URL]";
const CHARACTER_LIMIT = /* [set if truncation needed] */;

enum ResponseFormat { MARKDOWN = "markdown", JSON = "json" }

// --- Schemas: one per tool, per Execution Protocol validation rules ---
const [Tool]InputSchema = z.object({
  // [fields with .describe() and constraints]
}).strict();
type [Tool]Input = z.infer<typeof [Tool]InputSchema>;

// --- Shared utilities ---
async function makeApiRequest<T>(endpoint: string, method: string, data?: any, params?: any): Promise<T> {
  // [shared HTTP call per protocol]
}
function handleApiError(error: unknown): string {
  // [status-code-mapped messages per protocol]
}

const server = new McpServer({ name: "[service]-mcp-server", version: "1.0.0" });

// --- Tools: one per entry in TOOL_INVENTORY ---
server.registerTool(
  "[service]_[action]_[resource]",
  {
    title: "[...]",
    description: `[full description: what/what-not, Args, Returns schema, Examples, Error Handling]`,
    inputSchema: [Tool]InputSchema,
    annotations: { readOnlyHint: /*...*/, destructiveHint: /*...*/, idempotentHint: /*...*/, openWorldHint: /*...*/ }
  },
  async (params: [Tool]Input) => {
    try {
      // [implementation using makeApiRequest]
      return { content: [{ type: "text", text: /* formatted */ }], structuredContent: /* raw output */ };
    } catch (error) {
      return { content: [{ type: "text", text: handleApiError(error) }] };
    }
  }
);

// --- Transport wiring per DEPLOYMENT_TARGET ---
async function runStdio() { /* ... */ }
async function runHTTP() { /* Express + StreamableHTTPServerTransport, new transport per request */ }
```

## Quality Gate

- Is every tool registered via `registerTool` (never the deprecated `server.tool()`), with `title`, `description`, `inputSchema`, and all four `annotations` explicitly present?
- Does every Zod schema use `.strict()` and `.describe()` on every field with real constraints?
- Does every tool description include a full `Returns:` JSON schema and at least one `Examples:` use/don't-use pair — since JSDoc is not auto-extracted?
- Is `CHARACTER_LIMIT` truncation implemented (with a `truncation_message`) for any tool whose response can plausibly exceed it?
- Is there exactly one shared `makeApiRequest`/`handleApiError` pair (no duplicated HTTP or error-mapping code across tool files)?
- Does `npm run build` complete without errors and does `tsconfig.json` have `strict: true` with zero uses of `any`?

## Deploy When

Implementing the server body once the planning brief's tool inventory has selected TypeScript (the default recommendation) — greenfield build or adding new tools to an existing `McpServer`.
