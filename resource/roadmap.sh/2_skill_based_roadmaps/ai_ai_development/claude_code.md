# Claude Code

## Metadata
- Type: Skill
- Domain: Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/claude-code
- Related Roles:
  - AI Engineer

---

## 1. Beginner

### 1.1 Introduction
- **What is Vibe Coding?**
  - Vibe coding is a modern software development approach in which developers use AI agents and large language models (LLMs) to generate, build, and iterate on applications via natural language prompts, rather than writing code manually. Coined by Andrej Karpathy, this method focuses on the "vibe" or overall intent of the application, often involving rapid prototyping and minimal manual code review, making software development more accessible and faster.
- **What is a Coding Agent?**
  - A coding agent is an AI-powered software entity designed to autonomously write, test, and debug code to solve specific programming tasks or complete software development projects. It uses various AI techniques, like large language models and reinforcement learning, to understand requirements, generate code snippets, identify errors, and iterate on its solutions to achieve the desired outcome.
- **CLI**
  - Claude Code CLI is a command-line tool that acts as an agentic AI coding partner by interacting directly with your local files and terminal. To set it up, you first need an active Claude subscription or an Anthropic Console account.
- **Desktop**
  - Claude Code desktop is a software application that allows an AI assistant to interact directly with your local files and development tools through a graphical interface. It functions as an agentic coding partner that can read your codebase, edit files, and execute terminal commands to help build features or fix bugs in real time.
- **Setting up Claude**
  - To set up Claude Code, you first install the CLI tool through your terminal using a single command tailored to your operating system. For macOS, Linux, or WSL, you run curl -fsSL https://claude.ai/install.sh | bash, while Windows users can use PowerShell to run irm https://claude.ai/install.ps1 | iex.
- **What is Agentic Loop?**
  - An agentic loop is a computational pattern where an agent continuously interacts with its environment through a cycle of perception, planning, and action. The agent observes its surroundings, decides on a course of action based on its goals and current state, executes that action, and then observes the results to inform its next decision.
- **Mobile**
  - Claude Code does not have a separate mobile app. The Claude app for iOS and Android is a client that reaches Claude Code sessions in the Code tab.
- **Web**
  - Claude Code on the web runs sessions on cloud infrastructure instead of your machine. You start one at claude.ai/code, from the Code tab in the Claude app, from the Desktop app, or from the terminal with claude --cloud.

### 1.2 Ways to use Claude
- **Subscription**
  - Subscription options for Claude Code allow users to authenticate and access its features. Individuals with a Claude Pro or Claude Max subscription can link their account for free Claude Code usage.
- **API usage**
  - Claude Console authentication uses a pay-as-you-go model where the tool connects directly to the Anthropic API using a personal API key rather than a flat-rate monthly subscription. To set this up, you must first create an account at the Claude Console, generate a secret API key, and ensure you have a balance of credits in your account.
- **CLAUDE.md**
  - CLAUDE.md is a configuration file placed in a project's root directory that provides the AI assistant with specific rules, project context, and custom instructions for that particular codebase. It acts as a set of persistent guidelines that the AI reads at the start of every session to ensure its code suggestions align with your project's coding standards, tech stack, and architectural patterns.
- **Skills**
  - Claude Code skills are modular packages of instructions, scripts, and assets that teach the AI assistant how to perform specific, repeatable workflows. Each skill is stored in a dedicated folder containing a mandatory SKILL.md file, which uses YAML frontmatter to define its name and a description that the AI uses to automatically discover and load the skill when relevant.
- **Tools**
  - Tools are specialized functions that allow the AI assistant to perform actions on your computer rather than just generating text. These functions are categorized into client-side tools that interact with your local environment, such as Bash for running terminal commands, Read and Edit for file manipulation, and Glob or Grep for searching codebases, and server-side tools like WebSearch for fetching real-time information from the internet.
- **Context**
  - A context window is the total amount of information a model can hold in its active memory at one time, including your conversation history, the files it has read, and the results of any terminal commands it has executed. It functions like a temporary workspace where every word and symbol (counted as tokens) fills up a limited capacity.
- **Modes**
  - Modes set the level of autonomy Claude Code has in a session. Manual mode asks before edits and shell commands, Accept Edits mode approves file changes and common filesystem commands automatically, and Plan mode keeps Claude read-only while it outlines a strategy.
- **Models**
  - Claude Code is powered by three distinct models—Opus, Sonnet, and Haiku— each optimized for a specific role within the development lifecycle. Claude Opus is the "deep thinker" and primary architect, used for complex reasoning, high-level system design, and surgical bug fixes in large codebases.
- **Editor Extensions**
  - IDE extensions allow you to use Claude Code directly within popular development environments like Visual Studio Code and the JetBrains family (including IntelliJ IDEA, PyCharm, and WebStorm). These extensions provide a graphical sidebar and inline diff viewers, enabling you to review proposed code changes side-by-side with your existing files.
- **MCP**
  - The Model Context Protocol (MCP) is an open-source standard that enables a Claude Code to connect securely to a vast ecosystem of external tools, databases, and third-party services. By acting like a "universal connector" for AI, MCP allows you to extend the Claude Code's core capabilities beyond simple file editing, giving it the power to interact with APIs like GitHub to manage pull requests, query live databases such as PostgreSQL or Snowflake, and much more.
- **Plugins**
  - Claude Code plugins are shareable packages that bundle multiple customizations, including slash commands, specialized agents, skills, hooks, and Model Context Protocol (MCP) servers, into a single installable unit. They serve as a standardized way to distribute complex AI workflows across different projects or within an engineering team, ensuring that every developer has access to the same tools and coding standards.
- **Remote Control**
  - Remote Control connects claude.ai/code or the Claude mobile app to a Claude Code session running on your own machine. Claude keeps running locally, so your filesystem, MCP servers and project configuration stay available while you drive the session from a phone, tablet or another browser.
- **Teleport & Handoff**
  - Teleport and handoff move work between surfaces. claude --teleport pulls a cloud session into your terminal, checking out its branch and loading the conversation, and /teleport (or /tp) does the same from inside a session.
- **Dispatch**
  - Dispatch is a persistent conversation with Claude in Cowork that you message from your phone. You describe a task, and Dispatch decides how to handle it.
- **Channels**
  - Channels are MCP server plugins that push messages, alerts and webhooks into a Claude Code session that is already running. They support platforms like Telegram, Discord and iMessage, so Claude can react to events while you are away from the terminal.
- **Slack**
  - Slack integrations let you hand coding tasks to Claude from a team conversation. Mentioning @Claude in a channel with a bug report or request starts a Claude Code cloud session, posts progress in the thread, and returns a summary with buttons to view the session or create a pull request.
- **Chrome**
  - The Chrome integration connects Claude Code to your browser through the Claude in Chrome extension. Claude can open tabs, click, type, read console errors and the page structure, so it can test a web app, debug a failing page or fill in forms without leaving your session.

### 1.3 Using Claude Code
- **Common Usecases**
  - Claude Code can be used for a wide range of professional software development tasks, from legacy system modernization and large-scale refactoring to rapid prototyping for startups. Organizations use it to navigate and modernize massive codebases containing millions of lines of code, while data science teams employ it to convert exploratory research from notebooks into production-ready data pipelines.
- **Opus**
  - Claude Opus is the most advanced and capable large language model in the Claude family, designed specifically for high-level reasoning and complex problem-solving. It functions as a "deep thinking" engine that can handle vast amounts of information and follow intricate instructions with a high degree of accuracy and nuance.
- **Sonnet**
  - Claude Sonnet is a high-performance large language model that strikes an ideal balance between advanced reasoning intelligence and rapid processing speed. It serves as the versatile "workhorse" of the Claude family, capable of handling complex programming tasks, such as multi-file refactoring and autonomous debugging, while operating significantly faster and more cost-effectively than the top-tier Opus model.
- **Haiku**
  - Claude Haiku is the fastest and most cost-effective model in the Claude family, specifically engineered for high-speed, high-volume tasks that require near-instant responsiveness. It provides a compact but powerful solution for real-time applications like customer service chatbots, rapid data extraction, and moderating large content streams where low latency is critical.
- **Ctrl+C**
  - Ctrl+C is a keyboard shortcut that immediately sends an interrupt signal to the Claude Code terminal to stop its current activity. It is primarily used to halt a long-running process, such as an accidental infinite loop in your code, a search that is taking too long, or a lengthy model response that you realized was going in the wrong direction.
- **Esc**
  - The Esc key is a navigation shortcut used to exit current menus, cancel active inputs, or clear the command line. If you are in the middle of typing a long prompt and want to start over, pressing Esc will wipe the input field clean, and if you have a dropdown menu or a multi-select list open—such as when choosing files to add to context—it will close that menu without making a selection.
- **Ctrl+R**
  - Ctrl+R is a terminal shortcut that opens the command history search, allowing you to quickly find and reuse previous prompts or terminal commands you have typed during your session. Instead of manually retyping complex instructions or scrolling back through hundreds of lines of output, you can press Ctrl+R and start typing a few letters to filter your recent activity until the correct entry is highlighted.
- **Esc + Esc**
  - Double-tapping the Esc key in Claude Code activates the Rewind feature, which serves as a temporal navigation system for both your conversation history and your code state. When triggered, it opens an interactive menu that allows you to jump back to any previous prompt in the session, effectively acting as a "undo" button for AI-driven development.
- **Plan**
  - Plan Mode is a strictly read-only permission state that allows Claude to analyze your codebase, research dependencies, and draft a step-by-step implementation strategy without the risk of modifying any files or executing state-changing commands.
- **Hooks**
  - Hooks are automated triggers that execute specific scripts or commands at key points in the AI's workflow, such as before or after the assistant performs a task. These hooks allow developers to enforce project standards and ensure system reliability without manual intervention, much like Git hooks but designed for an AI-driven development cycle.
- **Subagents**
  - Subagents are specialized AI assistants that function as independent "team members" to handle focused tasks on behalf of the main agent. Each subagent operates within its own isolated context window, meaning it starts with a clean slate and does not clutter your primary conversation with large amounts of intermediate research or technical logs.
- **Ctrl+O**
  - Ctrl+O toggles the transcript viewer, a detailed view of everything that happened in the session. It shows tool usage and execution, with a timestamp and the model used on each assistant message.
- **Ctrl+B**
  - Ctrl+B moves running Bash commands and agents to the background. The session stays free for your next prompt while the work continues, which helps with long builds, dev servers or test runs.
- **Ctrl+G**
  - Ctrl+G opens your current prompt in your default text editor, so you can write or edit a long prompt in a full editor instead of the input line. Ctrl+X Ctrl+E does the same and is the readline-native binding.
- **Auto**
  - Auto mode lets Claude Code run without per-action permission prompts by having a separate classifier model review each action before it runs. The classifier blocks actions that go beyond your request, target unrecognized infrastructure, or appear driven by hostile content Claude read, and explicit ask rules still force a prompt.
- **Fable**
  - Claude Fable is the most capable model family in Claude Code, built for demanding reasoning and long-running agentic work such as root-cause investigations and architecture decisions. Fable 5.1 (claude-fable-5-1) is the current version, and you select it with /model fable because it is not the default on any plan.

### 1.4 Claude Workflow
- **Shift+Tab**
  - Shift+Tab is a navigation shortcut that allows you to cycle through different permission modes to control how much autonomy the AI assistant has over your computer. These modes act as a security dial, ranging from Default Mode, where the assistant must ask for your approval before making any file edits or running terminal commands, to Auto-Accept Mode, which grants it the power to modify files automatically while still prompting for shell commands.
- **Slash Commands (/)**
  - Slash commands are the steering wheel of Claude Code. They allow you to execute meta-actions, manage your session, and configure the environment without needing to write a natural language request.
- **Permission Modes**
  - Permission modes control how much Claude Code can do without asking you first. Manual (default) only runs reads without approval, acceptEdits also allows file edits and common filesystem commands, and plan restricts Claude to research and planning.
- **Manage Sessions**
  - Claude Code manages sessions through a persistent, local architecture where every interaction is stored in a unique session file, allowing you to resume work using terminal flags like claude --continue (for the most recent thread) or claude --resume (to open an interactive picker of past conversations). While each new session initializes with a fresh context window to optimize token usage and avoid irrelevance, Claude automatically snapshots affected files before any modification, enabling you to use the /rewind command to revert both code and conversation history to a previous "checkpoint."

### 1.5 Usage Best Practices
- **claude**
  - The claude command is the primary entry point used to launch the Claude Code interface from your terminal. When you type this command within a project directory, it initializes the agentic environment, indexes your local files, and establishes a secure connection to the AI model so you can begin issuing natural language instructions.
- **claude -r**
  - The claude -r command (short for --resume) allows you to restart a specific past conversation by providing its unique Session ID. Unlike the -c flag, which automatically opens the very last session you had, -r gives you the precision to jump back to any session from your history, ensuring you can continue a specific line of work without losing context or previous tool outputs.
- **Resume**
  - To resume a conversation in Claude Code, you can use the terminal command claude --continue (or -c) to instantly pick up the most recent session in your current directory, or claude --resume (or -r) to open an interactive session picker. This picker allows you to browse past conversations and select one using your arrow keys and the Enter key.
- **Rewind**
  - To rewind a conversation in Claude Code, you can use the /rewind slash command or the Esc + Esc keyboard shortcut to open the interactive checkpoint menu. This feature leverages the tool's automatic snapshotting, which creates a restore point for every user prompt and file modification throughout your session.

### 1.6 CLAUDE.md
- **claude "query"**
  - The claude "query" command allows you to start the Claude Code interactive REPL (Read-Eval-Print Loop) with an initial instruction already provided. By passing a string as an argument directly after the claude command, the assistant will immediately begin processing that request—such as "explain this project" or "fix the lint errors"—the moment the interface loads.
- **claude -p**
  - The claude -p command (short for --print) activates Print Mode, which runs Claude Code as a non-interactive, single-use utility rather than a continuous chat session. When you use this flag, you provide a prompt directly in the command line; Claude then executes its agentic loop—researching, editing files, or running commands as needed—and exits immediately once the task is complete.
- **claude -c**
  - The claude -c command (short for --continue) is a CLI flag used to instantly reopen the most recent conversation session in your current directory. Instead of starting a fresh chat with a clean context, this command restores the previous conversation history, allowing you to pick up exactly where you left off without having to re-explain your project’s state or repeat previous instructions.
- **--add-dir**
  - The claude --add-dir command is a startup flag that allows you to include extra folders in your working session before the interface even opens. By providing one or more directory paths when you launch the tool (for example, claude --add-dir ../library --add-dir ./docs), you grant the assistant permission to read and modify files in those external locations alongside your current project.
- **How to Structure**
  - To write an effective CLAUDE.md, you should treat it as a concise, persistent "source of truth" that provides Claude with the project-specific context it cannot infer from the code alone. The file should be kept short and human-readable, focusing on non-obvious information like unique bash commands for building and testing, repository-specific code styles, and architectural decisions.
- **Locations**
  - Claude Code manages instructions through a hierarchical memory system that layers context based on the directory structure of your project. At the start of every session, Claude recursively searches from your current working directory up to the root, automatically loading global preferences from ~/.claude/CLAUDE.md and shared team standards from the project root's CLAUDE.md.
- **--cloud**
  - claude --cloud "task" starts a new cloud session for the repository in your current directory, and the task runs on Anthropic infrastructure while you keep working locally. The cloud VM clones your GitHub remote at your current branch, so push local commits first.

---

## 2. Intermediate

### 2.1 Skills
- **Creating Skills**
  - To create a custom skill in Claude Code, you must establish a new folder within the .claude/skills/ directory containing a SKILL.md file that defines the skill's identity and logic. This file begins with a YAML frontmatter block containing a unique name and a detailed description, which Claude uses as a trigger to "know" when to activate the skill, and can include an optional disable-model-invocation: true flag if you want the skill to run as a manual, deterministic workflow rather than an autonomous one.
- **Skill Best Practices**
  - When configuring Claude Code skills, the primary best practice is to optimize for discoverability and context efficiency by using precise YAML frontmatter and "lazy loading." Your skill's description should act as a clear semantic trigger, using specific keywords that help Claude identify exactly when to activate the expert instructions without bloating the context window of every conversation. Structure the SKILL.md with a narrow, modular focus rather than creating a "Swiss Army Knife" skill; if a workflow has non-negotiable side effects, use disable-model-invocation: true to ensure it only runs when manually triggered via a slash command.
- **--teleport**
  - claude --teleport pulls a cloud session into your local terminal. Claude Code checks that you are in a checkout of the same repository, fetches and checks out the session's branch, and loads the full conversation history.
- **--bare**
  - --bare is a minimal startup mode for scripted calls with -p. It skips auto-discovery of hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory and CLAUDE.md, so a run starts faster and behaves the same on every machine.
- **--permission-mode**
  - --permission-mode starts a session in a specific permission mode. It accepts default (also written manual), acceptEdits, plan, auto, dontAsk and bypassPermissions.

### 2.2 Hooks
- **/help**
  - The /help command is an interactive directory that provides a comprehensive list of all available slash commands, keyboard shortcuts, and system features. When you type it, Claude Code displays a searchable guide that explains how to use tools such as context management, file mentions, and permission modes.
- **/clear**
  - The /clear command is a utility tool that removes all previous messages, tool outputs, and file contents from the active conversation history. It wipes the current context, allowing you to start a fresh dialogue with the AI without exiting the application or losing your current working directory settings.
- **/exit**
  - The /exit command is a built-in utility used to safely terminate your current Claude Code session and return you to your standard terminal prompt. Unlike force-quitting the application, using this command ensures that the system performs a clean shutdown, which includes saving your conversation history and updating any local session metadata so that you can resume your work later using the claude -c flag.
- **/usage**
  - The /usage command is a specialized diagnostic tool designed specifically for users on Claude Pro or Claude Max subscription plans. Since these plans have unified limits, the command provides a real-time status report of your remaining capacity instead of monetary costs.
- **/goal**
  - The /cost command is a financial monitoring tool that provides a real-time snapshot of the monetary expenses and token usage for your active session. While the /usage command focuses on how much of your context window is occupied, /cost translates that activity into USD amounts, showing you exactly how much your current conversation has cost based on your API pricing tier.
- **/export**
  - The /export command is a data utility that allows you to save your entire current conversation history into a single file on your local machine. This command generates a Markdown-formatted document containing all your prompts, the AI's responses, and the results of any code changes or terminal commands executed during the session.
- **Hook Inputs & Outputs**
  - Hooks communicate via a standardized JSON interface: Inputs are passed to the hook via stdin, and Outputs are returned via stdout to influence the agent's next move. The input payload typically includes a context object containing session metadata and event-specific data, such as the tool name and its arguments (e.g., the exact code being written or command being run).
- **Hook Types**
  - In Claude Code, you can configure three distinct handler types for your hooks—Command, Prompt, and Agent—depending on whether you need a script, an AI "judgement call," or a specialized researcher to validate actions. Command hooks (type: "command") are deterministic shell scripts that execute standard commands (like npm run lint) and use exit codes to either approve the action or block it with an error message.
- **Hook Events & Matchers**
  - In Claude Code, Hook Events represent the specific lifecycle moments when custom logic can be triggered, while Matchers act as the regex-based filters that determine which specific actions within those moments should fire the hook.

### 2.3 Manage Context
- **Understand Claude Pricing**
  - Claude Code offers a flexible, dual-path pricing model designed to accommodate both individual power users and high-scale enterprise teams. You can access the tool through a fixed-rate subscription (such as the Pro or Max plans), which provides a generous recurring allocation of messages shared across the web interface and the terminal, making costs predictable for daily development.
- **/status**
  - The /status command is an interactive dashboard that provides a comprehensive overview of your current session's health and system configuration. Unlike the /statusline command, which places a permanent information bar at the bottom of your terminal, /status opens a temporary, tabbed interface that displays detailed metrics such as your Claude Code version, the specific AI model in use, active account details, and real-time usage limits.
- **/rewind**
  - The /rewind command restores a session to an earlier point. You can rewind the conversation, the code changes, or both, and you can also summarize the conversation from a selected message instead of discarding it.
- **/doctor**
  - The /doctor command is a diagnostic utility used to troubleshoot and verify the health of your Claude Code installation and its environment. When executed, it runs a series of automated checks to ensure that your authentication tokens are valid, your network connection to the Anthropic servers is stable, and all required system dependencies—like Git and Node.js—are correctly configured.
- **/plan**
  - Plan Mode is a read-only environment that allows the AI to research, analyze, and outline a multi-step strategy for a task without making any actual changes to your files or executing state-altering commands. When you enter this mode—either by typing /plan or pressing Shift+Tab—the assistant focuses on gathering context and identifying dependencies to create a detailed implementation document.
- **Use /compact and /clear**
  - Regularly using /compact and /clear is the most effective way to prevent "context rot" and manage spiraling API costs while working with Claude Code. Because Claude re-processes your entire conversation history with every new message, a session that has accumulated thousands of lines of terminal output and file diffs will eventually become expensive, slow, and prone to "forgetting" early instructions.
- **/schedule**
  - /schedule creates and manages cloud scheduled tasks, formerly called routines, from inside a session. Claude asks about the schedule, repositories and prompt, then saves the task to your account.
- **/desktop**
  - /desktop continues your current terminal session in the Claude Code Desktop app, where you can review diffs visually. The handoff needs a claude.ai subscription and works on macOS and x64 Windows.

### 2.4 Model Configuration
- **Be mindful of extensions**
  - Carefully managing extensions, such as MCP servers, skills, and subagents, is vital because every active integration consumes a portion of Claude’s finite context window, and excessive "context pollution" can lead to degraded reasoning or higher operational costs.
- **Thinking modes & Effort**
  - Using thinking modes and adjusting effort levels in Claude Code is essential for balancing deep reasoning with operational efficiency. Furthermore, you can fine-tune Claude's cognitive energy using the effort parameter (available through the /model command).
- **Use subagents and hooks**
  - Subagents and Hooks are powerful architectural tools that manage the context window by practicing "selective attention," ensuring the main conversation stays lean while specialized tasks remain high-precision. Subagents act as isolated "expert bubbles" that run in their own independent context windows with restricted toolsets, while Hooks provide a deterministic way to inject or prune context at key lifecycle moments.
- **/remote-control**
  - /remote-control makes the current session available through Remote Control, so you can continue it from claude.ai/code or the Claude mobile app. Claude keeps running on your machine, so your filesystem, MCP servers and project configuration stay available.
- **/ultrareview**
  - ultrareview is an alias of /code-review ultra. It starts an ultrareview, a deep review that runs as a cloud session on Anthropic's infrastructure.
- **/code-review**
  - /code-review is a bundled skill that reviews your current diff, a pull request, a branch or a path for bugs. It runs in your own session on any plan, and an optional level from low to max sets how thorough the review is.

### 2.5 Customize Status Line
- **Prompt Caching**
  - Prompt caching in Claude Code is a performance-optimizing feature that stores the frequently used "prefixes" of your conversations—such as your entire codebase state, system instructions, and tool definitions—so they don't have to be reprocessed from scratch with every new message. In an agentic environment where Claude often re-reads your files multiple times to maintain context, caching acts as a "checkpoint" system: while the initial write to the cache carries a slight premium, every subsequent interaction that reuses that prefix receives a 90% discount on input tokens and up to an 85% reduction in latency.
- **/context**
  - The /context command is a diagnostic tool that provides a technical breakdown of how the model's context window is currently allocated, using a colored grid. While commands like /usage show you the "how much," /context shows you the "what." It lists every file, conversation turn, and tool result currently being held in the AI's active memory, allowing you to see exactly which resources are consuming tokens.
- **/compact**
  - The /compact command is a context management tool designed to optimize your session's memory when the context window begins to fill up. Instead of completely wiping your history like /clear, /compact instructs Claude to generate a concise summary of the key decisions, code changes, and project state established so far.
- **/memory**
  - The /memory command is a knowledge management tool used to create and manage persistent information that survives across different Claude Code sessions. Unlike the /compact command, which only optimizes the current conversation's temporary window, /memory interacts with permanent storage—primarily your project's CLAUDE.md file and a hidden auto-memory directory.
- **/init**
  - The /init command is the initialization utility used to set up Claude Code for a specific project directory. When you run this command, it creates a CLAUDE.md file in your current folder.

### 2.6 Output Styles
- **/config**
  - The /config command is the central management tool for customizing your Claude Code experience and fine-tuning how the assistant interacts with your system. Running this command opens an interactive menu—or allows for direct terminal arguments—to modify global and project-specific settings such as default models, theme preferences, and permission levels.
- **/permissions**
  - The /permissions command is a security management interface that allows you to view and adjust the rules governing what Claude can and cannot do on your machine. By default, Claude Code operates with a "human-in-the-loop" philosophy, meaning it asks for your approval before performing any action that could affect your system—such as modifying a file or running a terminal command.
- **Artifacts**
  - Artifacts turn Claude Code's work into live web pages hosted on claude.ai. When terminal text is the wrong medium, such as an annotated pull request, a dashboard or a set of design options, Claude writes an HTML or Markdown page and publishes it to a private URL.

### 2.7 Connecting Tools with MCP
- **/model**
  - The /model command is a switcher utility that allows you to change which large language model (LLM) is powering your current session without restarting the application. This is particularly useful for cost-performance optimization; you can use a high-intelligence model like Claude Sonnet for complex architectural planning and then switch to a faster, cheaper model like Claude Haiku for repetitive tasks like writing boilerplate code or unit tests.
- **/agents**
  - The /agents command points you to subagent management. On current versions it prints a reminder to ask Claude to create or manage subagents, or to edit the files in .claude/agents/ or ~/.claude/agents/ yourself.
- **/mcp**
  - The /mcp command is the integration hub for the Model Context Protocol, an open standard that connects Claude Code to external data sources and third-party tools. While you use the terminal command claude mcp add to install a new server, the /mcp slash command is used inside the session to manage those connections, authorize permissions, and view the specific capabilities (tools) available to the AI.
- **/hooks**
  - The /hooks command opens an interactive management menu for configuring automated workflows that trigger at specific points in the Claude Code lifecycle. While features like CLAUDE.md provide "soft" instructions, hooks offer deterministic control, ensuring that specific shell commands or AI evaluations run every single time a certain event occurs—such as formatting code after an edit or sending a notification when Claude needs your attention.
- **Skills for MCP**
  - Skills act as structured, reusable knowledge packages that dramatically improve how Claude interacts with MCP (Model Context Protocol) servers by giving it precise, context-aware instructions for specific tools and workflows. Rather than relying on Claude to infer how to use a given MCP server from scratch each time, skills provide curated guidance that helps Claude make smarter, more reliable decisions when invoking tools, chaining calls, and interpreting results.
- **Channels**
  - Channels are MCP server plugins that push messages, alerts and webhooks into a Claude Code session that is already running. They support platforms like Telegram, Discord and iMessage, so Claude can react to events while you are away from the terminal.
- **Tunnels**
  - MCP Tunnels let you connect Claude to MCP servers running inside your private network without opening inbound firewall ports or exposing services to the public internet. Traffic flows over an outbound-only encrypted connection, meaning your internal tools and data sources stay fully private while still being accessible to Claude.

### 2.8 Plugins
- **SessionStart**
  - The SessionStart hook is an initialization lifecycle event that triggers at the very beginning of a Claude Code interaction. Unlike other hooks that react to specific user prompts or file edits, SessionStart is designed to bootstrap your environment and inject high-priority context before the first prompt is even processed.
- **SessionEnd**
  - The SessionEnd hook is a teardown lifecycle event that triggers when you exit Claude Code or terminate a session. While SessionStart is for preparation, SessionEnd is your dedicated window for cleanup, archiving, and final reporting.
- **Code Intelligence**
  - Code Intelligence plugins extend the CLI's native search capabilities by integrating with the Language Server Protocol (LSP), granting Claude the same "IDE-level" awareness found in modern editors.

---

## 3. Advanced

### 3.1 Scheduling Jobs
- **PreToolUse**
  - The PreToolUse hook is a validation gate that executes immediately after Claude decides to use a tool (like writing a file or running a shell command) but before that tool actually runs. It is primarily used for security, policy enforcement, and input sanitization, acting as a final check to ensure the AI's proposed action is safe and correct.
- **PostToolUse**
  - The PostToolUse hook is a reactive lifecycle event that triggers immediately after a tool (like Bash, Write, Edit, or a custom MCP tool) completes its execution. While the PreToolUse hook acts as a guard to block actions, the PostToolUse hook is designed for automation, cleanup, and quality control—ensuring that every action Claude takes adheres to your project's standards.
- **UserPromptSubmit**
  - The UserPromptSubmit hook is an interception mechanism that fires the moment you press Enter on a prompt, but before the text is actually sent to the Claude model. It is the most powerful tool for prompt engineering automation, allowing you to programmatically rewrite, validate, or enhance your instructions on the fly.
- **Stop**
  - The Stop hook is a final-stage lifecycle event that triggers when Claude Code believes it has finished its entire response and is about to return control to the user. Unlike PostToolUse, which fires after every single file edit or command, the Stop hook only runs once at the very end of the interaction "turn."
- **Loops**
  - /loop reruns a prompt on a repeating interval inside an open session, which is useful for polling a deployment or watching a pull request. With an interval and a prompt it runs on a fixed schedule, with only a prompt Claude chooses the interval each time, and with neither it runs a built-in maintenance prompt or your own loop.md file.
- **Cloud Scheduled tasks**
  - Cloud scheduled tasks, formerly called routines, are saved Claude Code configurations that run on Anthropic-managed cloud infrastructure, so they work when your laptop is closed. A task holds a prompt, one or more repositories and a set of connectors.
- **Desktop Scheduled tasks**
  - Desktop scheduled tasks run recurring Claude Code work on your own machine through the Desktop app. They do not need an open session, but the computer has to be on.
- **SubagentStop**
  - SubagentStop is a hook event that fires when a subagent finishes responding. The matcher filters by agent type, and a hook with no matcher runs for every subagent.
- **PermissionRequest**
  - PermissionRequest is a hook event that fires when Claude Code is about to ask you for permission to use a tool. Unlike PreToolUse, which runs before every tool call, it only runs when a prompt would appear.

### 3.2 Scaling Claude
- **Git Worktrees**
  - Using Git worktrees with Claude Code is a powerful scaling technique that allows you to run multiple independent AI sessions in parallel without the overhead of context switching or the risk of file-edit collisions. This workflow is highly efficient for "fanning out" tasks: you can supervise several separate worktrees simultaneously, leveraging prompt caching across them for shared codebase context, and simply delete the worktree folder once the branch is merged to keep your environment clean.
- **Subagents**
  - Subagents are specialized AI assistants that function as independent "team members" to handle focused tasks on behalf of the main agent. Each subagent operates within its own isolated context window, meaning it starts with a clean slate and does not clutter your primary conversation with large amounts of intermediate research or technical logs.

### 3.3 CI/CD
- **Headless mode**
  - Headless mode runs Claude Code without the interactive interface by passing the -p (or --print) flag with a prompt. It is the CLI form of the Agent SDK and is meant for scripts and CI/CD pipelines.
- **Agent Team**
  - Agent Teams are an experimental multi-agent orchestration feature in Claude Code that allows you to coordinate multiple AI instances working in parallel on a single project. Agent Teams function as a collaborative network where a designated Team Lead manages a shared task list and delegates work to Teammates who can message each other directly to share findings or debate solutions.
- **Agent View**
  - Agent view is a single screen for managing many Claude Code sessions at once. You open it with claude agents, and it shows what each session is doing and which ones need your input.
- **Agent SDK**
  - The Agent SDK gives you the same tools, agent loop and context management that power Claude Code, as a library for Python and TypeScript. You use it to embed an agent in your own application, with built-in tools for reading files, running commands and searching the web.
- **GitHub Actions**
  - Claude Code GitHub Actions runs Claude Code inside your repository's workflows through the claude-code-action action. Mention @claude in an issue or pull request comment and Claude analyzes code, implements changes and pushes commits.
- **GitLab**
  - Claude Code GitLab CI/CD runs Claude Code in GitLab pipeline jobs. You add a job to .gitlab-ci.yml that installs the CLI and runs claude -p, with your API key stored as a masked CI/CD variable.

### 3.4 Code Review
- **Claude Code Security**
  - Claude Code Security is a new feature built into Claude Code that scans your codebase for security vulnerabilities and suggests fixes for your team to review. Every finding goes through a verification process before it reaches you, with severity ratings so you know what to fix first.
- **Dynamic Workflows**
  - A dynamic workflow is a JavaScript script that orchestrates many subagents at once. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.
- **Ultrareview**
  - Ultrareview is a deep code review that runs as a cloud session on Anthropic's infrastructure. You start it with /code-review ultra (/ultrareview is an alias when available), on your branch or on a GitHub pull request number.
- **Code Review on PRs**
  - Code Review on pull requests is a managed service that reviews every pull request in your GitHub repositories without a workflow file. Several agents read the diff with the surrounding code, a verification step removes false positives, and the review posts inline comments ranked by severity, a summary and a check run.

### 3.5 Security Best Practices
- **Sandboxing**
  - The sandboxed Bash tool wraps the shell commands Claude runs, and the processes they start, in an operating-system boundary. By default, commands can write only to the working directory, a temp directory and directories you add, while most reads stay allowed except denied paths like credential files.

---

## 4. Optional / Specialized Topics

- Setting up Claude
- What is Agentic Loop?
- Mobile
- Web
- Tools
- Context
- Modes
- Models
- Editor Extensions
- MCP
- Plugins
- Remote Control
- Teleport & Handoff
- Dispatch
- Channels
- Slack
- Chrome
- Ctrl+C
- Esc
- Ctrl+R
- Esc + Esc
- Plan
- Hooks
- Subagents
- Ctrl+O

---

## 5. References

- [Claude Code Roadmap](https://roadmap.sh/claude-code)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer

### Related Skills
- AI Agents
- Prompt Engineering
- Vibe Coding