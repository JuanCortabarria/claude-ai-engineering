# Claude AI Engineering

My 3-month study journey to become an AI Engineer, focused on building with Claude: the Claude API, the Model Context Protocol (MCP) and Claude Code.

This repo holds my notes and exercises from each course. Bigger projects live in their own repositories (linked below as they ship).

## Roadmap

| Phase | Weeks | Focus | Status |
| --- | --- | --- | --- |
| Month 1 | 1–3 | Building with the Claude API | ⏳ In progress |
| Month 1 | 4 | Introduction to MCP + MCP: Advanced Topics | 🔜 Pending |
| Month 2 | 5 | Claude Code 101 + Claude Code in Action | 🔜 Pending |
| Month 2 | 6–8 | Main project: RAG system + agent using my MCP server | 🔜 Pending |
| Month 3 | 9–10 | Production: evals, prompt caching, error handling, logging | 🔜 Pending |
| Month 3 | 11 | LLM fundamentals: tokens, embeddings, context windows, transformers | 🔜 Pending |
| Month 3 | 12 | Portfolio: READMEs, badges, write-up | 🔜 Pending |

## Courses

| # | Course | Duration | Badge |
| --- | --- | --- | --- |
| 1 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | ~9 h | ⬜ |
| 2 | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | ~1 h | ⬜ |
| 2 | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | ~1.5 h | ⬜ |
| 3 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | ~1.5 h | ⬜ |
| 3 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | ~1 h | ⬜ |

All courses are free on [Claude Academy](https://academy.claude.com/courses).

## Repository structure

```
claude-ai-engineering/
├── README.md
├── .gitignore
├── 01-claude-api/      # Building with the Claude API: notes + exercises
├── 02-mcp/             # MCP intro + advanced: servers and clients
├── 03-claude-code/     # Claude Code 101 + Claude Code in Action
└── notes/              # General notes, concepts and learnings
```

## Projects

| Project | Description | Repo |
| --- | --- | --- |
| Tool-use assistant | Assistant with tool use and structured outputs (end of course 1) | _coming soon_ |
| MCP server | Custom MCP server connecting Claude to an external API/DB | _coming soon_ |
| RAG + agent | Main project: RAG system with an agent using my MCP server | _coming soon_ |

## Setup

Requirements: Python 3.10+, an Anthropic API key ([Claude Console](https://console.anthropic.com)).

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
```

Create a `.env` file in the project root (it is git-ignored, never commit it):

```
ANTHROPIC_API_KEY=your-key-here
```

## Stack

Python · Claude API · MCP · Claude Code · Git

## Author

**Juan Cortabarria** · [GitHub](https://github.com/JuanCortabarria)
