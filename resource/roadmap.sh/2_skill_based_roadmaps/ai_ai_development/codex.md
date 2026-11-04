# Codex

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/codex
- Related Roles:
  - Software Engineer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **What is a Coding Agent?**
  - A coding agent is an AI system that can write, test and debug code on its own to complete a task. Unlike autocomplete, it can read many files, run shell commands, see the results and decide what to do next.
- **What is Agentic Loop?**
  - An agentic loop is the cycle an agent repeats until a task is done. The model reasons over the current context, calls a tool such as reading a file or running a command, observes the result and decides on the next step.

### 1.2 Setting Up
- **CLI**
  - The Codex CLI is a coding agent that runs locally in your terminal. You start it with codex inside a project, describe a task, and Codex inspects the code, edits files and runs your tools.
- **Subscription Plans**
  - Codex is included with ChatGPT Free, Go, Plus, Pro, Business, Edu and Enterprise plans. Higher plans give more usage and add cloud features such as automatic code review and Slack.
- **API usage**
  - You can sign in to Codex with an OpenAI API key instead of a ChatGPT account. API usage is billed at standard API rates and follows the models available to your key.
- **Desktop**
  - The ChatGPT desktop app is a graphical home for Codex on macOS, Windows and Linux. It lets you run several projects in parallel, keeps every chat visible and supports scheduled tasks, worktrees, browser use and computer use.

### 1.3 Ways to use Codex
- **Ctrl+C**
  - Ctrl+C interrupts what Codex is doing in the terminal UI. Use it to stop a turn that is going in the wrong direction.
- **Ctrl+L**
  - Ctrl+L clears and redraws the terminal screen without starting a new conversation. Your chat and context stay as they are, so it only cleans up the display.
- **Editor Extensions**
  - The Codex IDE extension works beside your code in the editor. It can use your open files, selected code and recent chats as context, and you review its edits in place.
- **Mobile**
  - The ChatGPT mobile app lets you start and follow Codex tasks from your phone. You can run a task in Codex Cloud or control a project on your own computer after pairing it with a QR code.
- **Web**
  - Codex on the web runs in your browser at chatgpt.com. You sign in with your ChatGPT account, choose where Codex should work and send a task.
- **Codex cloud**
  - Codex Cloud runs coding tasks on remote infrastructure instead of your machine. You create an environment with your repositories, setup scripts, internet access rules and secrets, then send a task to it.

### 1.4 Using Codex
- **Slash Commands (/)**
  - Typing / in the composer opens the list of built-in slash commands. They control the session from inside the terminal UI: choosing a model, changing permissions, planning, reviewing, managing context and more.
- **TAB**
  - Pressing Tab while Codex is running queues a follow-up prompt, slash command or ! command to run after the current turn.
- **Esc + Esc**
  - Pressing Esc twice on an empty composer lets you edit your previous message. Pressing it again goes further back through earlier messages.
- **Integrations**
  - Codex connects to the tools where your team already works. On GitHub it can review pull requests automatically and respond to @codex mentions, and it can also start tasks from issues.
- **Ctrl+O**
  - Ctrl+O copies the latest completed Codex output to your clipboard. It is the keyboard shortcut for /copy.
- **Ctrl+R**
  - Ctrl+R opens a search through your prompt history. You type part of an earlier prompt and Codex shows matches you can reuse.
- **Ctrl+G**
  - Ctrl+G opens the current prompt in your external editor, as set by the $VISUAL or $EDITOR environment variable. This is useful for writing long, multi-line prompts with your usual editing tools.
- **Your First Task**
  - A good first task is small and easy to check, such as asking Codex to explain the project or fix a failing test. Open a project folder, run codex, and give a clear prompt with the goal and how to verify it.

### 1.5 Codex Models
- **Astra**
  - GPT-6 Astra (gpt-6-astra) is the most capable model available in Codex. It is built for complex work across code, apps and research that needs sustained reasoning and judgment.
- **Sol**
  - GPT-6.1 Sol (gpt-6.1-sol) is built for repeated, long-running work across code, apps and documents. The docs describe its performance as close to Astra at a lower cost.
- **Terra**
  - GPT-6.1 Terra (gpt-6.1-terra) is a fast, efficient model for clear writing, visual understanding and computer use. It suits tasks where Codex works from screenshots or acts across your browser and apps.
- **codex**
  - codex starts the interactive terminal UI in the current directory. You can pass an optional starting prompt, for example codex "explain this project", and attach images with --image.
- **resume**
  - codex resume continues a previous interactive session. Run it alone to pick from your saved sessions, add --last for the most recent one, or pass a session ID.
- **Luna**
  - GPT-6 Luna (gpt-6-luna) is the most cost-efficient model, meant for focused, high-volume tasks such as summarization, extraction and narrow coding jobs. It has by far the largest usage allowance.

---

## 2. Intermediate

### 2.1 Basic Workflows
- **Explore Codebases**
  - Codex can read a repository and explain how it is organized before you change anything. Ask it for an overview, to trace where a feature is implemented, or to list the files involved in a bug.
- **login**
  - codex login signs you in. It supports ChatGPT OAuth, device auth for remote or headless machines with --device-auth, an API key piped in with --with-api-key, and an access token with --with-access-token.
- **exec**
  - codex exec runs Codex non-interactively, so you can use it in scripts and CI. Progress goes to stderr and the final message goes to stdout, which makes it easy to pipe.
- **review**
  - codex review runs a non-interactive code review. You can point it at uncommitted changes with --uncommitted, at a branch diff with --base, or at a single commit with --commit, and you can add custom review instructions.
- **doctor**
  - codex doctor generates a diagnostic report about your setup. It checks the installation, configuration, authentication, runtime and Git health.
- **Fix Bugs & Refactoring**
  - For bug fixes, give Codex the error message, the steps to reproduce it and the expected behavior. It can find the cause, apply a fix and run the tests to confirm.
- **Review Diffs**
  - Reviewing the diff is how you stay in control of what Codex changed. Use /diff to see all edits, including new files, and /review to have a separate reviewer check them.
- **Write Effective Prompts**
  - An effective prompt states the goal, gives the context, names the constraints and says how to check the result. For code, that means reproduction steps, the files that matter, boundaries such as what not to change, and a test or command that proves it works.
- **mcp**
  - codex mcp manages MCP servers from the command line. The subcommands add, get, list, login, logout and remove cover the whole lifecycle, including OAuth sign-in for remote servers.
- **update**
  - codex update checks for a newer Codex CLI version and applies it when your install supports self-update. If you installed with npm or Homebrew, you can also update through that package manager.
- **apply**
  - codex apply applies the latest diff from a Codex Cloud task to your local working tree. You pass the task ID, and the command is also available as codex a.
- **Plan, Edit & Test**
  - For anything beyond a small change, ask Codex to plan first with /plan, then let it edit, then have it run the tests. Planning surfaces misunderstandings before they become code.
- **logout**
  - codex logout removes the stored credentials from your machine. Use it on shared computers or when you want to switch accounts.

### 2.2 Sessions
- **--ask-for-approval**
  - --ask-for-approval (or -a) sets when Codex pauses for your approval before running a command. The values are on-request, where Codex works inside the sandbox and asks before going beyond it, and never, where it does not ask.
- **Resuming**
  - Resuming reopens a saved session with its context. Use codex resume to pick one, codex resume --last for the most recent, or /resume inside the terminal UI.
- **Forking**
  - Forking copies a session into a new chat and keeps the original transcript unchanged. Use codex fork or /fork to try another approach without losing the first one.
- **Archive & Delete**
  - Archiving hides a saved session from the picker without deleting it, and you can restore it with codex unarchive. Deleting removes the session permanently, including its descendants.
- **--help**
  - --help prints the commands and options available in your installed version. It is the most reliable reference, because the list of flags and slash commands changes between releases.
- **--model**
  - --model (or -m) overrides the configured model for one run, for example codex -m gpt-6.1-sol. The same setting can be made permanent with model in config.toml.
- **--cd**
  - --cd (or -C) sets the working directory Codex uses before it starts. It lets you launch Codex on a project without first changing folders in your shell.
- **--image**
  - --image (or -i) attaches one or more images to the first prompt. Separate several paths with commas or repeat the flag.
- **--sandbox**
  - --sandbox (or -s) selects the sandbox policy for commands that Codex runs. The options are read-only, workspace-write and danger-full-access.
- **--search**
  - --search turns on live web search for the run. By default, local Codex sessions use a cached search index, which lowers the risk of prompt injection from web pages.
- **Manage Context**
  - The context window is the amount of information the model can consider at once. Long sessions fill it, and quality can drop as old details crowd out new ones.

### 2.3 Permissions & Approvals
- **/model**
  - /model chooses the active model and, when the model supports it, the reasoning effort. Use it to move to a stronger model for a hard task or a cheaper one for simple work.
- **/permissions**
  - /permissions changes what Codex can do without asking, in the middle of a session. You can switch between profiles such as Ask for approval, Approve for me and Full access.
- **Sandbox Modes**
  - The sandbox is an enforced boundary around the commands Codex runs. read-only lets Codex inspect files but not change them, workspace-write allows edits inside the workspace and routine local commands, and danger-full-access removes the limits on files and network.
- **Approval Policies**
  - The approval policy controls when Codex stops to ask you. The supported values are on-request, where Codex works inside the sandbox and asks before going beyond it, and never, where it does not ask.
- **Git Checkpoints**
  - A Git checkpoint is a commit or stash you make before and after a Codex task. The docs recommend creating them so you can revert if the changes go wrong.
- **--add-dir**
  - --add-dir grants write access to an extra directory alongside the main workspace. You can repeat it for several paths.
- **--worktree**
  - --worktree starts Codex in a new managed Git worktree. The changes stay isolated from your current checkout, so you can run a task without touching unfinished work.
- **--profile**
  - --profile (or -p) loads a named profile on top of your base configuration. The profile is a profile-name.config.toml file in your Codex home directory.
- **--yolo**
  - --yolo is the short form of --dangerously-bypass-approvals-and-sandbox. It runs every command without approvals and without a sandbox, so Codex can change anything your user account can.

### 2.4 Project Instructions
- **/approve**
  - /approve retries one recent action that automatic review denied. When Approve for me is on, a reviewer agent can reject a request.
- **/init**
  - /init generates an AGENTS.md scaffold in the current directory. The file gives Codex persistent instructions for the project, such as build and test commands and coding conventions.
- **/review**
  - /review asks Codex to review your working tree. A dedicated reviewer reads the selected diff, such as uncommitted changes or a branch against its base, and reports prioritized findings without editing files.
- **/plan**
  - /plan switches Codex to plan mode, optionally with a prompt. Codex proposes an approach before it changes anything, so you can correct the direction first.
- **/diff**
  - /diff shows the Git diff of the working tree, including files Git does not track yet. Use it to check what Codex changed before you commit or run tests.
- **/status**
  - /status shows the current session configuration and token usage. It confirms the active model, approval policy, writable roots and how much context remains.
- **Initialize a Project**
  - Initializing a project means creating its first AGENTS.md. Run /init in the project directory and Codex generates a scaffold you can edit.
- **Project Conventions**
  - Project conventions are the rules Codex should follow when it works in your repository. Typical entries are how to run tests and linters, naming and formatting rules, folders that should not be edited, and what a good pull request looks like.
- **AGENTS.md**
  - AGENTS.md is a markdown file with persistent instructions for Codex. A global file lives in your Codex home folder, and project files live from the repository root down to your working directory.

### 2.5 Models & Usage
- **/compact**
  - /compact summarizes the visible chat to free up context. Codex keeps the key points and drops the detail, so a long session can continue without hitting the context limit.
- **/new**
  - /new starts a new chat inside the same CLI session. The context is reset, but you stay in the same terminal and repository.
- **/fork**
  - /fork copies the current chat into a new one. The original transcript stays untouched, so you can try a different approach and still go back.
- **/resume**
  - /resume opens your saved chats and resumes the one you pick. Use it to continue earlier work without leaving the terminal UI.
- **Choosing Models**
  - Choose a model by the kind of task. Use Astra for the hardest reasoning, Sol for long-running work at a lower cost, Terra for visual and computer-use tasks, and Luna for narrow, high-volume jobs.
- **Reasoning Efforts**
  - Reasoning effort controls how much reasoning budget the model uses before answering. Higher effort helps with planning and hard debugging, and lower effort reduces latency and cost.
- **Fast Mode**
  - Fast mode is a service tier that returns results sooner at a higher credit cost. You toggle it with /fast when the current model offers it.
- **Usage Limits**
  - Included usage is measured in estimated messages per five-hour window for each model, and the numbers differ between Astra, Sol, Terra and Luna. Pro currently has no five-hour limit, and cloud tasks can use more allowance than local messages.
- **/mention**
  - /mention attaches a file or folder to the chat. Codex then looks at exactly what you point to instead of searching for it.
- **/fast**
  - /fast toggles the Fast service tier for models that offer one. Fast mode returns results sooner but uses more credits, so it fits work you are waiting on.

### 2.6 Customization
- **/mcp**
  - /mcp lists the MCP tools configured for the session, and adding verbose shows server details. Use it to check which external tools Codex can call.
- **/skills**
  - /skills lets you browse and select a local skill. Choosing one adds it to your prompt so Codex follows its instructions.
- **/goal**
  - /goal sets, edits, pauses, resumes, shows or clears a task goal. The goal text works as both the first prompt and the completion criteria, so Codex keeps working until the outcome is reached.
- **/subagents**
  - /subagents switches the active subagent thread. When Codex spawns subagents, each one works in its own thread, and this command lets you inspect or continue one from the main session.
- **Skills**
  - A skill is a folder with a SKILL.md file that teaches Codex a repeatable workflow. The file needs a name and a description, and it can include scripts, references and assets.
- **config.toml**
  - config.toml is Codex's main settings file, found at ~/.codex/config.toml. A trusted project can add its own .codex/config.toml for project-specific settings.
- **Plugins**
  - A plugin is an installable bundle of capabilities. It can include skills, MCP server connections, hooks and browser extensions, and it is distributed through a marketplace shared by ChatGPT and Codex.
- **/copy**
  - /copy copies the latest completed Codex output to your clipboard. Use it to take a finished answer or plan without selecting text manually.
- **/recap**
  - /recap generates a summary of the current conversation without compacting it. Your context stays intact, and you get a short catch-up on what has happened.
- **MCP**
  - The Model Context Protocol connects Codex to external tools and data. Each server has a [mcpservers.<name>] table in config.toml, and it is either a local STDIO process or a remote streamable HTTP server with OAuth or a bearer token.

### 2.7 Scaling Codex
- **Git Worktrees**
  - A Git worktree is a second checkout of the same repository, so each task gets its own files and branch. Codex can create one for you: start with codex --worktree, use /worktree in a session, or run a scheduled task in a background worktree.
- **/plugins**
  - /plugins lists installed and discoverable plugins. From there you can inspect a plugin's tools, install one from a configured marketplace, or turn it on or off.
- **/hooks**
  - /hooks shows and manages lifecycle hooks. Hooks that you did not manage yourself must be reviewed and trusted here before they run, and a changed hook needs a new review.
- **Subagents**
  - Subagents are specialized agents that Codex spawns to work in parallel and report back. They keep noisy output such as logs and exploration notes out of the main thread.
- **Parallel Sessions**
  - You can run several Codex chats at the same time, each with its own context. Parallel chats should not edit the same files, so give each one a separate worktree or a separate part of the code.
- **/import**
  - /import brings a Claude Code or Cursor setup into Codex. It can import supported configuration, projects and chats into Codex configuration and local files.
- **/memories**
  - /memories configures how Codex uses and generates memory. You can turn memory injection or memory generation on or off without leaving the terminal UI.

---

## 3. Advanced

### 3.1 Code Review
- **Code Review**
  - Codex can review code at several points. /review and codex review check local changes, such as uncommitted work, a branch against its base or a single commit, and report findings without editing files.

### 3.2 CI/CD
- **Non-Interactive Mode**
  - Non-interactive mode runs Codex without the terminal UI through codex exec. You pass a prompt as an argument or through stdin, and Codex runs the task and prints the final message.
- **GitHub Actions**
  - The openai/codex-action@v1 action installs the Codex CLI and runs codex exec inside a GitHub workflow. You give it a prompt or a prompt file, a sandbox setting and your API key from a repository secret, and it returns the final message as an output.

### 3.3 Images & Web Search
- **Images & Web Search**
  - Codex accepts images and can search the web. Add screenshots, designs or diagrams with --image, by pasting into the composer, or by dragging a file in.

### 3.4 Hooks
- **Hooks**
  - Hooks run your own scripts at points in Codex's lifecycle. Events include SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, SubagentStart, SubagentStop and Stop.

### 3.5 Custom Agents
- **Custom Agents**
  - Custom agents are subagents you define yourself in a standalone TOML file. Put them in ~/.codex/agents/ for personal use or .codex/agents/ for a project.

---

## 4. Optional / Specialized Topics

- Web
- Codex cloud
- Ctrl+O
- Ctrl+R
- Ctrl+G
- Your First Task
- resume
- Luna
- doctor
- Fix Bugs & Refactoring
- Review Diffs
- Write Effective Prompts
- mcp
- update
- apply
- Plan, Edit & Test
- logout
- --help
- --model
- --cd
- --image
- --sandbox
- --search
- Manage Context
- Git Checkpoints

---

## 5. References

- [Codex Roadmap](https://roadmap.sh/codex)

---

## 6. Related Roles / Topics

### Related Roles
- Software Engineer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Claude Code
- Vibe Coding
- AI Agents