#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { execFile } from "child_process";
import fs from "fs/promises";
import path from "path";
import util from "util";

const execFileAsync = util.promisify(execFile);

const KDEV = process.env.KDEV || "/home/rocha/kryonix/kryonix-dev";
const SCRIPT_PATH = path.join(KDEV, "scripts", "kryonix-test-profile.sh");
const VAULT_PATH = path.join(KDEV, "repos", "kryonix-vault");

const VALID_PROFILES = [
  "smoke",
  "installer-critical",
  "nix-fast",
  "nix-full",
  "python",
  "rust",
  "vault",
];

const REPORT_ROOT = path.join(VAULT_PATH, "99-Logs", "test-runs");

async function assertReportPathAllowed(reportPath) {
  const resolvedRoot = await fs.realpath(REPORT_ROOT);
  const resolvedPath = await fs.realpath(reportPath);

  if (
    resolvedPath !== resolvedRoot &&
    !resolvedPath.startsWith(resolvedRoot + path.sep)
  ) {
    throw new Error("Invalid path. Only reports under vault/99-Logs/test-runs are allowed.");
  }

  if (!resolvedPath.endsWith(".md")) {
    throw new Error("Invalid report file. Only markdown reports are allowed.");
  }

  return resolvedPath;
}

function sanitizeSummary(summary) {
  if (typeof summary !== "string") {
    throw new Error("summary must be a string");
  }

  if (summary.length > 4000) {
    throw new Error("summary too large; max 4000 chars");
  }

  return summary
    .replace(/api[_-]?key[=: ]+\S+/gi, "api_key=<REDACTED>")
    .replace(/token[=: ]+\S+/gi, "token=<REDACTED>")
    .replace(/secret[=: ]+\S+/gi, "secret=<REDACTED>")
    .replace(/password[=: ]+\S+/gi, "password=<REDACTED>")
    .replace(/authorization:\s*bearer\s+\S+/gi, "authorization: bearer <REDACTED>");
}

const server = new Server(
  {
    name: "kryonix-test-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "list_test_profiles",
        description: "List all allowed deterministic test profiles",
        inputSchema: {
          type: "object",
          properties: {},
          required: [],
        },
      },
      {
        name: "run_test_profile",
        description: "Run a specific test profile deterministically",
        inputSchema: {
          type: "object",
          properties: {
            profile: {
              type: "string",
              description: "The name of the profile to run",
            },
          },
          required: ["profile"],
        },
      },
      {
        name: "get_last_test_report",
        description: "Fetch the contents of a specific test report file by path. Fetches up to the first 200 lines to avoid sending large logs to the model.",
        inputSchema: {
          type: "object",
          properties: {
            report_path: {
              type: "string",
              description: "Absolute path to the markdown report file returned by run_test_profile.",
            },
          },
          required: ["report_path"],
        },
      },
      {
        name: "get_last_failures",
        description: "Parses a given report file and extracts only the failed sections.",
        inputSchema: {
          type: "object",
          properties: {
            report_path: {
              type: "string",
              description: "Absolute path to the markdown report file returned by run_test_profile.",
            },
          },
          required: ["report_path"],
        },
      },
      {
        name: "write_test_summary_to_vault",
        description: "Write a high-level manual summary or addendum to a test report in the vault.",
        inputSchema: {
          type: "object",
          properties: {
            summary: {
              type: "string",
              description: "The text summary to append.",
            },
            report_path: {
              type: "string",
              description: "The report path to append the summary to.",
            }
          },
          required: ["summary", "report_path"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    switch (request.params.name) {
      case "list_test_profiles": {
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify({ profiles: VALID_PROFILES }),
            },
          ],
        };
      }
      case "run_test_profile": {
        const { profile } = request.params.arguments;
        if (!VALID_PROFILES.includes(profile)) {
          throw new Error(`Invalid profile: ${profile}. Allowed: ${VALID_PROFILES.join(", ")}`);
        }

        try {
          const { stdout } = await execFileAsync(SCRIPT_PATH, [profile], { shell: false });
          
          // Parse the JSON output from the script
          const lines = stdout.trim().split("\n");
          let jsonResult = null;
          
          for (let i = lines.length - 1; i >= 0; i--) {
            try {
              jsonResult = JSON.parse(lines[i]);
              break;
            } catch (e) {
              // Ignore non-json lines
            }
          }
          
          if (!jsonResult) {
             return {
               content: [
                 {
                   type: "text",
                   text: JSON.stringify({
                     profile,
                     status: "ERROR",
                     error: "Failed to parse script output",
                   }),
                 },
               ],
             };
          }
          
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify(jsonResult),
              },
            ],
          };
        } catch (error) {
          // Process exited with non-zero (test failure). The JSON should still be in stdout.
          if (error.stdout) {
            const lines = error.stdout.trim().split("\n");
            let jsonResult = null;
            
            for (let i = lines.length - 1; i >= 0; i--) {
              try {
                jsonResult = JSON.parse(lines[i]);
                break;
              } catch (e) {}
            }
            
            if (jsonResult) {
              return {
                content: [
                  {
                    type: "text",
                    text: JSON.stringify(jsonResult),
                  },
                ],
              };
            }
          }
          
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify({
                  profile,
                  status: "ERROR",
                  error: error.message,
                }),
              },
            ],
          };
        }
      }
      case "get_last_test_report": {
        const { report_path } = request.params.arguments;
        const safePath = await assertReportPathAllowed(report_path);
        
        const content = await fs.readFile(safePath, "utf-8");
        const lines = content.split('\n');
        
        let out = content;
        if (lines.length > 200) {
           out = lines.slice(0, 200).join('\n') + "\n\n...[TRUNCATED. File too long to avoid sending full log to model]...";
        }
        
        return {
          content: [{ type: "text", text: out }],
        };
      }
      case "get_last_failures": {
        const { report_path } = request.params.arguments;
        const safePath = await assertReportPathAllowed(report_path);
        
        const content = await fs.readFile(safePath, "utf-8");
        
        // Very basic extraction of failed blocks
        // The script outputs:
        // ## <name>
        // ```txt
        // <output>
        // ```
        // - <name>: FAIL
        
        const failures = [];
        const blocks = content.split("## ");
        
        for (const block of blocks) {
           if (!block.trim()) continue;
           if (block.includes(": FAIL")) {
              failures.push("## " + block.trim());
           }
        }
        
        if (failures.length === 0) {
           return {
             content: [{ type: "text", text: JSON.stringify({ status: "No failures found in report" }) }]
           };
        }
        
        const failureStr = failures.join("\n\n");
        const lines = failureStr.split('\n');
        let out = failureStr;
        if (lines.length > 200) {
           out = lines.slice(0, 200).join('\n') + "\n\n...[TRUNCATED]...";
        }
        
        return {
          content: [{ type: "text", text: out }],
        };
      }
      case "write_test_summary_to_vault": {
        const { summary, report_path } = request.params.arguments;
        const safePath = await assertReportPathAllowed(report_path);
        
        const safeSummary = sanitizeSummary(summary);
        const toAppend = `\n\n## Agent Summary\n\n${safeSummary}\n`;
        await fs.appendFile(safePath, toAppend, "utf-8");
        
        return {
          content: [{ type: "text", text: "Successfully appended summary to report." }],
        };
      }
      default:
        throw new Error("Unknown tool");
    }
  } catch (error) {
    return {
      isError: true,
      content: [{ type: "text", text: error.message }],
    };
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Kryonix Test MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});
