# OpenClaw

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/openclaw
- Related Roles:
  - AI Engineer

---

## 1. Beginner

### 1.1 Introduction
- **OpenClaw vs Claude Code**
  - Claude Code is Anthropic's official CLI tool for AI-assisted coding, tightly integrated with Claude models and designed for developer workflows. OpenClaw is a community-built alternative that runs independently, supports a wide range of AI providers beyond Anthropic, and extends beyond coding to general agent automation across messaging platforms.
- **Use cases**
  - Open Claw can be used for a wide range of tasks: you can connect it to your messaging apps to have it read and respond to messages on your behalf, set up scheduled jobs using cron and heartbeats to run recurring tasks like daily summaries or file cleanups without any human input, process incoming data from webhooks by extracting and acting on information automatically, manage and update files and documentation in your workspace, chain multiple actions together in a single agent loop to complete multi-step workflows from start to finish, and even run several specialized agents in parallel with routing rules and shared memory so each one handles a different domain while staying coordinated with the others.
- **Context Window**
  - The context window is the amount of conversation history, instructions, and tool results the AI model can see at once when generating a response. Open Claw manages this carefully through a context engine and compaction system so long-running agents don't exceed the model's limits.
- **Gateway**
  - The Gateway is the single always-on process that handles routing, the control plane, and all channel connections. It runs on a single multiplexed port that serves the WebSocket control and RPC interface, HTTP APIs, the Control UI, and hooks.
- **Agents**
  - An agent in Open Claw is a fully isolated unit with its own workspace folder containing its personality and configuration files, its own state directory that holds auth profiles and the model registry, and its own session store that keeps the full conversation history separate from every other agent. Because auth profiles are scoped per-agent, credentials for one agent are never automatically shared with another, which means you can run a personal agent on your WhatsApp number and a work agent on a separate account on the same Gateway without any risk of their sessions, memories, or API keys crossing over.
- **Agent Loop**
  - When Open Claw receives a message, it runs a full agent loop rather than returning a single response. The loop validates the message, resolves the model, assembles the system prompt from skills and context files, and then sends everything to the model for inference.

### 1.2 How OpenClaw Works
- **How OpenClaw Works**
  - Open Claw runs a single long-lived Gateway that owns all messaging surfaces and exposes a typed WebSocket API for control-plane clients like the macOS app, CLI, and web UI. When a message arrives, the Gateway routes it to the appropriate agent, which then runs through a full loop of context assembly, model inference, and tool execution before streaming a reply back.

### 1.3 Setting up OpenClaw
- **Setting up OpenClaw**
  - Setting up Open Claw involves installing the package via npm, running the onboarding wizard to connect your AI model provider and first communication channel, and optionally installing the Gateway as a background daemon so it starts automatically.

### 1.4 Local Machine
- **Why and Why not?**
  - A local machine is the right choice if you are just getting started, experimenting with Open Claw, or running it as a personal assistant for yourself only. It requires no ongoing costs, no remote infrastructure to manage, and lets you get up and running in minutes.
- **Security Best Practices**
  - Use a local machine setup only for single-user personal use. Bind the Gateway to localhost so it is never exposed to the internet, set a strong randomly generated auth token, and store all API keys in environment variables rather than config files.

### 1.5 VPS/Cloud
- **Why and Why not?**
  - A VPS or cloud server is the right choice if you need your agent to be always online, reachable from anywhere, and capable of receiving webhooks from external services. It is the most common production setup and works well for personal assistants, team automation, and any workflow that requires continuous availability.
- **Security Best Practices**
  - When running Open Claw locally, bind the Gateway to localhost only so it is never exposed directly to the internet, set a strong, randomly generated auth token, and never hardcode API keys in config files — use environment variables instead. Run the process as a non-root user, keep your sender allowlist minimal, and enable device pairing so unknown devices cannot connect.

### 1.6 Dedicated Hardware
- **Memory System**
  - The memory system allows Open Claw agents to remember information across conversations. Instead of starting fresh every time, agents can store and retrieve facts, past interactions, or user preferences from structured memory files in the workspace.
- **Channels**
  - Channels are the messaging platforms through which users interact with Open Claw, and each one connects to the single Gateway process that routes incoming messages to the right agent and sends replies back. Every channel runs simultaneously on the same Gateway, so you can be connected to Telegram, WhatsApp, Discord, and Slack all at once without running separate processes.
- **Skills**
  - OpenClaw uses AgentSkills-compatible skill folders to teach the agent how to use tools. A skill is a markdown file injected into the system prompt that gives the agent context, constraints, and step-by-step guidance for using tools effectively.
- **Proactive Core**
  - The proactive core is what allows Open Claw agents to act on their own initiative rather than just responding to messages. Using heartbeats, cron jobs, and standing orders, the agent can run tasks on a schedule or trigger automatically based on conditions you define.
- **Raspberry Pi**
  - A Raspberry Pi is a small, low-cost single-board computer that can run Open Claw 24/7 with minimal power consumption. It is a popular self-hosting choice for hobbyists who want a home server.
- **Mac Mini**
  - A Mac Mini is a compact desktop computer that works well as a home server for Open Claw. It is more powerful than a Raspberry Pi and runs macOS, which may simplify setup for Mac users.
- **Why and Why not?**
  - Running Open Claw on dedicated hardware like a Raspberry Pi or Mac Mini gives you full control and no ongoing cloud fees, but the hardware itself is a constraint. Low-powered devices like a Raspberry Pi may struggle with memory-intensive tasks or multiple simultaneous agent sessions, and any hardware failure means your agent goes offline until you physically fix or replace the device.

---

## 2. Intermediate

### 2.1 Installation
- **Docker**
  - Docker lets you run Open Claw inside a container, an isolated environment that keeps it separate from the rest of your system. This makes installation cleaner, reduces conflicts with other software, and makes it easier to remove or update later.
- **Pick a Provider**
  - Open Claw runs on any VPS or cloud server that supports Node.js, so you are not locked into a specific provider. The official docs include setup guides for several popular options, including DigitalOcean, Render, Hetzner, Fly.io, Google Cloud Platform, Azure, and exe.dev, each with different trade-offs around pricing, location, and ease of setup

### 2.2 Onboarding
- **Auth & Model Providers**
  - This section covers how to connect Open Claw to AI model providers like Anthropic, OpenAI, Gemini, or Ollama by entering your API credentials. The model provider is what powers the agent's intelligence.
- **Adding First Channel**
  - After setting up your model provider, the next step is connecting a communication channel, in other words, the platform where you will actually talk to your agent. Telegram is recommended as the fastest channel to get started with.
- **Workspace Settings**
  - Workspace settings define the environment your agent operates in, including its identity, behavioral guidelines, and what it knows about you. These are stored in a set of markdown configuration files in your project directory.
- **Anthropic**
  - Anthropic is the company behind the Claude family of models. Connecting Open Claw to Anthropic lets you use Claude as your agent's underlying model, which is well-suited for reasoning, writing, and tool use.
- **OpenAI**
  - OpenAI provides access to models like GPT-4o. Open Claw can use these models as the AI brain behind your agent by configuring your OpenAI API key in the model provider settings.
- **Gemini**
  - Gemini is Google's family of AI models. Open Claw supports Gemini as an alternative model provider, giving you access to Google's AI infrastructure for powering your agents.
- **Ollama**
  - Ollama is a tool that lets you run open-source AI models locally on your own hardware, making it a natural fit for Open Claw setups where privacy, cost, or offline availability are a priority. It shines most in dedicated hardware setups like a Mac Mini or a capable home server, where you have enough RAM and processing power to run a model comfortably.
- **Gateway Settings**
  - Gateway settings control how the Open Claw server behaves, including the port it listens on, authentication tokens, and which interfaces it binds to. These settings are critical for both functionality and security.
- **MEMORY.md**
  - MEMORY.md is a persistent file where the agent stores important facts it has learned over time. It is regularly updated so the agent can recall relevant information in future conversations.
- **AGENTS.md**
  - AGENTS.md describes the agents available in your workspace, their roles, and how they relate to each other. It is used when running multiple agents to clarify who does what.
- **SOUL.md**
  - SOUL.md is the file where you define the agent's personality, tone, and core behavioral guidelines. Think of it as the agent's character sheet.
- **USER.md**
  - USER.md contains information about you: your preferences, context, and anything you want the agent to know about you by default. The agent reads this to personalize its responses.

### 2.3 Hooks
- **iMessage**
  - iMessage is Apple's built-in messaging system. The recommended way to connect it to Open Claw is via BlueBubbles, a macOS server that provides a full-featured REST API for iMessage integration.
- **Telegram**
  - Telegram is a messaging app that supports bots via a straightforward API. It is one of the easiest channels to connect to Open Claw and is recommended as the first channel for new users.
- **Slack**
  - Slack is a team communication platform. Open Claw connects to it via the Bolt SDK as a workspace app, making it useful for team-based automation and internal tooling.
- **WhatsApp**
  - WhatsApp is the most popular channel in Open Claw. It connects via the Baileys library and requires a QR code pairing step to link your account to the Gateway.
- **Discord**
  - Discord is a chat platform popular in gaming and developer communities. Open Claw connects to it via the Discord Bot API and Gateway, supporting servers, channels, and DMs.
- **Signal**
  - Signal is an end-to-end encrypted messaging app. Open Claw connects to it via signal-cli, making it a strong option for users who prioritize privacy in their communications with the agent.
- **Hook Structure**
  - Each hook is a directory containing a HOOK.md file with metadata and a handler.ts file with the logic to run. The metadata defines which events to listen for and what requirements the hook needs to be eligible.

### 2.4 Webhooks
- **Event Types**
  - Open Claw hooks support a range of event types, including command events like /new and /reset, session events like compaction, agent bootstrap events, gateway startup events, and message received and sent events.

### 2.5 Usage Best Practices
- **doctor --deep**
  - openclaw doctor --deep is an extended version of openclaw doctor that performs a more thorough diagnostic check, scanning system services for extra gateway installs and deeper configuration issues that the standard check might miss. You can add the --yes flag to automatically accept any prompts without manual input, which is useful for running the command in a headless or
- **doctor**
  - The openclaw doctor command checks your Open Claw installation for common configuration problems and misconfigurations. It is the first thing to run when something is not working as expected.
- **Adding Daemon**
  - A daemon is a background process that runs continuously without needing a terminal window open. Configuring Open Claw as a daemon ensures it starts automatically and keeps running even after you log out or restart your machine.
- **Other Workspace Files**
  - Open Claw recognizes several other special markdown files that are automatically injected into the agent's context at startup. BOOT.md contains instructions that the agent runs once when the Gateway starts.
- **memory/YYYY-MM-DD.md**
  - These are dated memory log files that store a record of what happened on a specific day. They give the agent a chronological history that it can reference when needed, and are created automatically by the session-memory hook.
- **onboard**
  - openclaw onboard walks you through the initial setup process interactively, helping you connect your model provider and first channel step by step.

### 2.6 Heartbeats
- **Securing Webhooks**
  - The Webhooks plugin ensures that each route is protected by shared-secret authentication, rate limiting, request size guards, and in-flight request limiting. Use a strong unique secret per route, store it as a SecretRef rather than inline plaintext, and bind each route to the narrowest session that fits the workflow.
- **Interval & Active Hours**
  - You can configure how often heartbeats fire and restrict them to certain hours of the day, so your agent only runs automated tasks during times you define as active.

### 2.7 Automating Tasks
- **gateway**
  - openclaw gateway is the main command for interacting with the gateway process. It is the entry point for all gateway-related operations from the command line.
- **security audit**
  - openclaw security audit scans your Open Claw setup for potential security vulnerabilities such as exposed ports, weak tokens, or insecure configurations. You can also run openclaw security audit --deep for a live Gateway probe, or openclaw security audit --fix to automatically tighten safe defaults.

### 2.8 Cron Jobs
- **Installing from ClawHub**
  - ClawHub is a community repository of pre-built skills. You can browse and install skills from ClawHub directly, saving time compared to building them from scratch.
- **Creating Skills**
  - You can write your own skills by creating a SKILL.md file with instructions and placing it in your workspace's skills/ folder. This lets you teach the agent new behaviors tailored to your specific needs.
- **Managing & Disabling Jobs**
  - You can list, pause, and delete cron jobs from the command line, giving you control over which scheduled tasks are active at any given time.
- **HEARTBEAT.md**
  - HEARTBEAT.md is a workspace configuration file where you define what the agent should do during each heartbeat cycle — essentially a set of instructions for proactive, time-based behavior.

---

## 3. Advanced

### 3.1 Sessions
- **channels list**
  - openclaw channels list displays all the communication channels currently connected to your Open Claw gateway, along with their status.
- **gateway start | stop | restart**
  - openclaw gateway start, openclaw gateway stop, and openclaw gateway restart control the lifecycle of the Open Claw gateway process, starting it up, shutting it down, or restarting it after a configuration change.

### 3.2 Skills
- **channels login**
  - openclaw channels login initiates the authentication flow for a specific channel, allowing Open Claw to connect to it on your behalf.
- **channels add --channel**
  - openclaw channels add --channel adds a new communication channel to your Open Claw setup, specifying which platform to connect.
- **Security Risks**
  - Installing third-party skills carries risk since a skill can define instructions or tool access that could be misused. It is important to review skills from external sources before installing them.
- **channels remove --channel**
  - openclaw channels remove --channel disconnects and removes a channel from your Open Claw configuration.

### 3.3 Plugins
- **channels status --probe**
  - openclaw channels status --probe actively checks the connection status of your channels by probing them, rather than just reporting cached status.
- **Creating Plugins**
  - You can build your own plugins to add custom functionality to Open Claw, such as integrating a new service or adding a new type of tool the agent can call.
- **Installing Plugins**
  - Plugins are installed via openclaw plugins install followed by the package name or path. Once installed, they become available to all agents in your workspace.
- **Security Risks**
  - Plugins run at a deeper level than skills and can have significant access to your system. Open Claw installs plugin dependencies with --ignore-scripts to reduce risk, but you should still only install plugins from trusted sources.

### 3.4 MCP
- **models list | set | status**
  - openclaw models list, openclaw models set, and openclaw models status let you view the AI models available in your setup, switch between them, and check which one is currently active.
- **models auth add**
  - openclaw models auth add is the interactive auth helper. It can launch a provider auth flow (OAuth/API key) or guide you into manual token paste, depending on the provider you choose.

### 3.5 Multi-Agents
- **models auth setup-token**
  - openclaw models auth setup-token stores the authentication token for a model provider, allowing Open Claw to make authenticated API calls on your behalf. It is part of the broader models auth command group, which also includes add, login, and paste-token.
- **cron list**
  - openclaw cron list shows all the scheduled tasks currently registered in Open Claw along with their schedules and status.
- **cron add**
  - openclaw cron add registers a new scheduled task, letting you define what the agent should do and when it should trigger automatically.
- **/status**
  - /status asks the agent to report its current state, including active tasks, connected channels, and any pending operations. It also shows provider usage and quota for the current model provider when usage tracking is enabled.
- **/new**
  - /new starts a fresh conversation with the agent, clearing the current context so you are beginning from a clean slate. It also triggers the session-memory hook to save the previous session before resetting.
- **/model**
  - /model is a directive that lets you switch the AI model the agent is currently using. You can pass a number from the model picker, a full provider/model string, or use /model list to see available options.
- **/context**
  - /context explains what context the agent is currently working with. You can use /context list for a summary, /context detail for a breakdown of per-file, per-tool, per-skill, and system prompt sizes, or /context json for machine-readable output.
- **/compact**
  - /compact is a text-only command that compresses or summarizes the current conversation context to free up space in the context window without losing essential information. You can optionally pass instructions to guide how the compaction is done.
- **memory index --all**
  - openclaw memory index rebuilds the search index for all memory files, ensuring the agent can efficiently retrieve relevant information from its stored memories.
- **memory search "<query>"**
  - openclaw memory search "query" lets you search through the agent's stored memories using a keyword or phrase, useful for checking what the agent has remembered about past conversations or preferences.
- **/help**
  - /help displays a list of available slash commands and a brief description of what each one does. It also works as an inline shortcut, meaning it can be embedded in a normal message and will be stripped before the model sees the rest of the text.
- **/reset**
  - /reset resets the agent's current state, clearing any ongoing task or context and returning it to its idle state. Like /new, it triggers the session-memory hook before resetting.
- **/stop**
  - /stop interrupts the agent if it is currently in the middle of a task or loop, bringing it to a halt immediately. It targets the active chat session directly so it can abort the current run.
- **Routing Rules**
  - Routing rules determine which agent handles which incoming messages. Open Claw uses a deterministic, most-specific-wins system: peer matches beat channel-wide rules, which beat the fallback default agent.
- **backup create**
  - openclaw backup create generates a snapshot of your Open Claw configuration and memory files so you can restore your setup if something goes wrong.
- **/usage**
  - /usage controls the per-response usage footer appended to normal replies. It takes off, tokens, full, or cost as arguments.
- **/think**
  - /think is a directive that sets the agent's thinking level before responding. It takes off, minimal, low, medium, high, or xhigh as arguments.
- **/fast**
  - /fast is a directive that toggles fast mode for the current session. It takes on, off, or status as arguments.
- **/reasoning**
  - /reasoning is a directive that enables or disables extended reasoning mode. It takes on, off, or stream as arguments.
- **/allowlist**
  - /allowlist lists, adds, or removes entries from the sender allowlist that controls who can interact with the agent. Add and remove operations require commands.config: true to be set in your configuration.
- **/config**
  - /config reads and writes your on-disk openclaw.json configuration file directly from chat. It is disabled by default and requires commands.config: true in your config to enable.
- **/mcp**
  - /mcp manages OpenClaw-managed MCP server definitions from chat. It is disabled by default and requires commands.mcp: true to enable.
- **/plugins**
  - /plugins lets you inspect discovered plugins and toggle their enablement from chat. It is disabled by default and requires commands.plugins: true to enable.

---

## 4. Optional / Specialized Topics

- Agents
- Agent Loop
- Raspberry Pi
- Mac Mini
- Why and Why not?
- OpenAI
- Gemini
- Ollama
- Gateway Settings
- MEMORY.md
- AGENTS.md
- SOUL.md
- USER.md
- Discord
- Signal
- Hook Structure
- memory/YYYY-MM-DD.md
- onboard
- /new
- /model
- /context
- /compact
- memory index --all
- memory search "<query>"
- /help

---

## 5. References

- [OpenClaw Roadmap](https://roadmap.sh/openclaw)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer

### Related Skills
- Vibe Coding
- Claude Code
- AI Agents