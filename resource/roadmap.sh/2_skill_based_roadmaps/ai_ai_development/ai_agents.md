# AI Agents

## Metadata
- Type: Skill
- Domain: Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ai-agents
- Related Roles:
  - AI Engineer
  - AI and Data Scientist
  - Data Analyst
  - MLOps Engineer

---

## 1. Beginner

### 1.1 Basic Backend Development
- **Basic Backend Development**
  - Before you start learning how to build AI agents, we would recommend you to have a basic knowledge of Backend development. This includes, programming language knowledge, interacting with database and basics of APIs at minimum.

### 1.2 Git and Terminal Usage
- **Git and Terminal Usage**
  - Git and the terminal are key tools for AI agents and developers. Git lets you track changes in code, work with branches, and collaborate safely with others.

### 1.3 Streamed vs Unstreamed Responses
- **Streamed vs Unstreamed Responses**
  - An unstreamed response waits until the model finishes generating the entire output before returning anything to the caller. A streamed response sends tokens back as they are generated, so the caller can start displaying or processing output immediately.

### 1.4 REST API Knowledge
- **REST API Knowledge**
  - REST APIs serve as a standardized way for different software systems to communicate with each other over the internet using HTTP requests. They allow an application to send data or request specific actions from a web server by using common methods like GET, POST, PUT, and DELETE.

### 1.5 Reasoning vs Standard Models
- **Reasoning vs Standard Models**
  - Standard models generate a response directly from a prompt, while reasoning models are trained or prompted to work through intermediate steps before producing a final answer. This extra reasoning process tends to improve performance on complex tasks like math or multi-step planning, but it usually costs more tokens and takes longer to respond.

### 1.6 Fine-tuning vs Prompt Engineering
- **Fine-tuning vs Prompt Engineering**
  - Fine-tuning and prompt engineering are two ways to get better outputs from a language model. Fine-tuning means training an existing model further with your own examples so it adapts to specific tasks.

### 1.7 Transformer Models and LLMs
- **Tokenization**
  - Tokenization is the process of breaking text into smaller units called tokens, which can be whole words, parts of words, or individual characters depending on the tokenizer. A language model does not read raw text, it reads a sequence of token IDs mapped from these units.
- **Context Windows**
  - The context window is the maximum number of tokens a model can process in a single request, including both the input and the generated output. Anything beyond this limit gets truncated or causes an error, so long conversations or documents need to be managed carefully.
- **Token Based Pricing**
  - Token-based pricing is how many language-model services charge for use. A token is a small chunk of text, roughly four characters or part of a word.
- **Top-p**
  - Top-p, also called nucleus sampling, is a setting that guides how an LLM picks its next word. The model lists many possible words and sorts them by probability.

### 1.8 Embeddings and Vector Search
- **Embeddings and Vector Search**
  - Embeddings turn words, pictures, or other data into lists of numbers called vectors. Each vector keeps the meaning of the original item.

### 1.9 Open Weight Models
- **Open Weight Models**
  - Open weight models are language models whose trained parameters are published for anyone to download, run, and fine-tune, examples include Llama and Mistral. Because the weights are available, developers can self host these models, modify them, and avoid relying on a third party API.

### 1.10 Understand the Basics of RAG
- **Understand the Basics of RAG**
  - Retrieval Augmented Generation (RAG) is a technique where relevant documents or data are fetched from an external source and added to a model's prompt before it generates a response. This lets the model answer questions using information it was not originally trained on, such as private documents or recent data.

---

## 2. Intermediate

### 2.1 Closed Weight Models
- **Temperature**
  - Temperature is a setting that changes how random or predictable an AI model’s text output is. The value usually goes from 0 to 1, sometimes higher.
- **Frequency Penalty**
  - Frequency penalty reduces the likelihood of the model repeating tokens it has already used, with the penalty growing the more often a token appears. This discourages repetitive phrases and loops in longer generations.

### 2.2 Pricing of Common Models
- **Pricing of Common Models**
  - Different LLM providers charge different rates per million input and output tokens, and prices vary widely between model sizes and capability tiers. Comparing pricing across common models like GPT, Claude, and Gemini helps in picking a model that fits both the task's quality requirements and the project's budget.

### 2.3 Agent Loop
- **Presence Penalty**
  - Presence penalty is a setting you can adjust when you ask a large language model to write. It pushes the model to choose words it has not used yet.
- **Stopping Criteria**
  - Stopping criteria tell the language model when to stop writing more text. Without them, the model could keep adding words forever, waste time, or spill past the point we care about.
- **Perception / User Input**
  - Perception, also called user input, is the first step in an agent loop. The agent listens and gathers data from the outside world.
- **Reason and Plan**
  - Reason and Plan is the moment when an AI agent thinks before it acts. The agent starts with a goal and the facts it already knows.
- **Acting / Tool Invocation**
  - Acting, also called tool invocation, is the step where the AI chooses a tool and runs it to get real-world data or to change something. The agent looks at its current goal and the plan it just made.
- **Observation & Reflection**
  - Observation and reflection form the thinking pause in an AI agent’s loop. First, the agent looks at the world around it, gathers fresh data, and sees what has changed.
- **Personal assistant**
  - A personal assistant AI agent is a smart program that helps one person manage daily tasks. It can check a calendar, set reminders, and send alerts so you never miss a meeting.
- **Max Length**
  - Max Length sets the maximum number of tokens a language model can generate in one reply. Tokens are pieces of text—roughly 100 tokens equals a short paragraph.

### 2.4 What is Prompt Engineering
- **What are AI Agents?**
  - An AI agent is a computer program or robot that can sense its surroundings, think about what it senses, and then act to reach a goal. It gathers data through cameras, microphones, or software inputs, decides what the data means using rules or learned patterns, and picks the best action to move closer to its goal.
- **What are Tools?**
  - Tools are extra skills or resources that an AI agent can call on to finish a job. A tool can be anything from a web search API to a calculator, a database, or a language-translation engine.
- **Be specific in what you want**
  - When you ask an AI to do something, clear and exact words help it give the answer you want. State the goal, the format, and any limits up front.
- **Provide additional context**
  - Provide additional context means giving the AI enough background facts, constraints, and goals so it can reply in the way you need. Start by naming the topic and the purpose of the answer.
- **Use relevant technical terms**
  - Using relevant technical terms means including precise vocabulary from the domain of the task instead of describing things in vague, general language. A model trained on technical text responds better to prompts phrased the way experts in that field would phrase them.

### 2.5 Tree-of-Thought
- **Code generation**
  - Code-generation agents take a plain language request, understand the goal, and then write or edit source code to meet it. They can build small apps, add features, fix bugs, refactor old code, write tests, or translate code from one language to another.
- **Data analysis**
  - AI agents can automate data analysis by pulling information from files, databases, or live streams. They clean the data by spotting missing values, outliers, and making smart corrections.

### 2.6 Chain of Thought (CoT)
- **Web Scraping / Crawling**
  - Web scraping and crawling let an AI agent collect data from many web pages without human help. The agent sends a request to a page, reads the HTML, and pulls out parts you ask for, such as prices, news headlines, or product details.
- **NPC / Game AI**
  - Game studios use AI agents to control non-player characters (NPCs). The agent observes the game state and decides actions like moving, speaking, or fighting.

### 2.7 Tool Definition
- **Use Examples in your Prompt**
  - A clear way to guide an AI is to place one or two short samples inside your prompt. Show a small input and the exact output you expect.
- **Iterate and Test your Prompts**
  - After you write a first prompt, treat it as a draft, not the final version. Run it with the AI, check the output, and note what is missing, wrong, or confusing.
- **Web Search**
  - Web search lets an AI agent pull fresh facts, news, and examples from the internet while it is working. The agent turns a user request into search words, sends them to a search engine, and reads the list of results.
- **Code Execution / REPL**
  - A code execution or REPL tool lets an agent run code and see the actual result, rather than only generating code as text. This is useful for tasks like calculations, data processing, or verifying that generated code works before presenting it.
- **Database Queries**
  - Database queries let an AI agent fetch, add, change, or remove data stored in a database. The agent sends a request written in a query language, most often SQL.

### 2.8 Model Context Protocol (MCP)
- **MCP Hosts**
  - MCP Hosts are computers or services that run the Model Context Protocol. They handle incoming calls, load the MCP manifest, check requests, and pass data between users, tools, and language models.

### 2.9 Creating MCP Servers
- **Specify Length, format etc**
  - When you give a task to an AI, make clear how long the answer should be and what shape it must take. Say “Write 120 words” or “Give the steps as a numbered list.” If you need a table, state the column names and order.
- **Local Desktop**
  - A Local Desktop deployment means running the MCP server directly on your own computer instead of a remote cloud or server. You install the MCP software, needed runtimes, and model files onto your desktop or laptop.
- **Remote / Cloud**
  - Remote or cloud deployment places the MCP server on a cloud provider instead of a local machine. You package the server as a container or virtual machine, choose a service like AWS, Azure, or GCP, and give it compute, storage, and a public HTTPS address.

### 2.10 What is Agent Memory?
- **API Requests**
  - API requests let an AI agent ask another service for data or for an action. The agent builds a short message that follows the service’s rules, sends it over the internet, and waits for a reply.
- **Email / Slack / SMS**
  - Email, Slack, and SMS are message channels an AI agent can use to act on tasks and share updates. The agent writes and sends emails to give detailed reports or collect files.
- **File System Access**
  - File system access lets an AI agent read, create, change, or delete files and folders on a computer or server. With this power, the agent can open a text file to pull data, write a new report, save logs, or tidy up old files without human help.
- **MCP Client**
  - The MCP Client is the part of an AI agent that talks to the language model API. It collects messages, files, and tool signals, packs them using the Model Context Protocol, and sends them to the model.

### 2.11 Short Term  Memory
- **Short Term  Memory**
  - Short-term memory refers to the immediate, transient information that an AI agent holds during a specific task or conversation. It is typically implemented by including recent interaction history, active goals, and relevant context directly within the model's prompt window.

### 2.12 Episodic vs Semantic Memory
- **RAG and Vector Databases**
  - Using RAG with a vector database means storing pieces of information as embeddings and retrieving the most relevant ones by similarity search when the agent needs context. This combination lets an agent access a large body of knowledge without keeping it all in the prompt, since only the relevant retrieved pieces get added to context.
- **User Profile Storage**
  - User profile storage is the part of an AI agent’s memory that holds stable facts about each user, such as name, age group, language, past choices, and long-term goals. The agent saves this data in a file or small database so it can load it each time the same user returns.
- **MCP Servers**
  - An MCP server exposes a set of tools, data, or capabilities to any compatible client using the Model Context Protocol. It might, for example, provide access to a file system, a database, or a third party API.

### 2.13 Long Term Memory
- **Long Term Memory**
  - Long term memory in an AI agent stores important information for future use, like a digital notebook. It saves facts, past events, user preferences, and learned skills so the agent can make smarter and more consistent decisions over time.

### 2.14 RAG Agent
- **Summarization / Compression**
  - Summarization or compression reduces the size of stored or in context information by condensing it into a shorter form that keeps the key details. This is used when conversation history or retrieved data grows too large to fit within a context window.
- **Forgetting / Aging Strategies**
  - Forgetting or aging strategies decide what stored information an agent should discard or deprioritize over time, since keeping everything indefinitely is neither practical nor useful. Common approaches include removing information after a set time, lowering its priority if it is not accessed, or replacing outdated details with newer ones.

---

## 3. Advanced

### 3.1 ReAct (Reason + Act)
- **ReAct (Reason + Act)**
  - ReAct is an agent architecture that interleaves reasoning steps with actions, having the model think through what to do, take an action, observe the result, and reason again before the next action. This tight loop between thought and action lets the agent adjust its plan based on real feedback rather than committing to a full plan upfront.

### 3.2 Planner Executor
- **Planner Executor**
  - A planner executor architecture splits an agent into two roles: a planner that breaks a goal down into a sequence of steps, and an executor that carries out each step and reports back the result. This separation lets the planner focus on high level strategy while the executor handles the details of each individual action.

### 3.3 DAG Agents
- **Metrics to Track**
  - To judge how well an AI agent works, you need clear numbers. Track accuracy, precision, recall, and F1 score to measure correctness.
- **Unit Testing for Individual Tools**
  - Unit testing checks that each tool an AI agent uses works as expected when it stands alone. You write small tests that feed the tool clear input and then compare its output to a known correct answer.
- **Integration Testing for Flows**
  - Integration testing for flows checks that an agent behaves correctly across a full multi step task, not just that individual tools work on their own. It verifies that the agent chooses the right tools in the right order and handles the combined behavior of reasoning, acting, and observing correctly.
- **Human in the Loop Evaluation**
  - Human-in-the-loop evaluation checks an AI agent by letting real people judge its output and behavior. Instead of trusting only automated scores, testers invite users, domain experts, or crowd workers to watch tasks, label answers, flag errors, and rate clarity, fairness, or safety.
- **LangSmith**
  - LangSmith is a platform for debugging, testing, and monitoring LLM applications, including agents, by tracing each step of a run and logging inputs, outputs, and intermediate reasoning. It also supports building evaluation datasets and running automated tests against them to measure quality over time, alongside dashboards for tracking cost and latency in production.
- **Ragas**
  - Ragas is an evaluation framework focused specifically on retrieval augmented generation pipelines, measuring things like the relevance of retrieved documents and the faithfulness of generated answers to that retrieved content. It provides a standard set of metrics tailored to RAG systems rather than general purpose LLM evaluation.
- **DeepEval**
  - DeepEval is an open-source tool that helps you test and score the answers your AI agent gives. You write small test cases that show an input and the reply you hope to get, or a rule the reply must follow.
- **Self-critique Agents**
  - Self-critique agents are a type of AI agent designed to evaluate and improve their own performance. They work by generating outputs, then analyzing those outputs to identify weaknesses or errors.
- **Multi-Agents**
  - Multi-agent systems involve multiple autonomous agents that interact with each other to achieve individual or collective goals. These agents can collaborate, compete, or coordinate their actions within a shared environment.

### 3.4 Manual (from scratch)
- **Manual (from scratch)**
  - Building an AI agent from scratch means writing every part of the system yourself, without ready-made libraries. You define how the agent senses inputs, stores memory, makes decisions, and learns over time.

### 3.5 LLM Native "Function Calling"
- **OpenAI Functions Calling**
  - OpenAI's function calling lets a model choose from a set of functions defined in the API request and return a structured call with the function name and arguments as JSON. The calling application executes the function and sends the result back for the model to use in its next response.
- **Gemini Function Calling**
  - Gemini function calling is Google's implementation of native tool calling, letting a Gemini model select from provided function definitions and return a structured call with arguments. The application runs the corresponding function and returns the output to continue the interaction.
- **OpenAI Assistant API**
  - The OpenAI Assistants API is a higher level interface for building agents that manages conversation threads, tool calls, and file based context on OpenAI's servers, rather than requiring the developer to track state manually. It handles things like persisting conversation history and running tools like code execution or file search.
- **LangChain**
  - LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). It provides tools and abstractions to connect LLMs to various data sources, create chains of calls to LLMs or other utilities, and build agents that can interact with their environment.
- **LlamaIndex**
  - LlamaIndex is a framework focused on connecting language models to external data, providing tools for ingesting, indexing, and querying documents for retrieval augmented generation. It handles tasks like chunking documents, generating embeddings, and building indexes that support efficient retrieval.
- **Haystack**
  - Haystack is an open source framework for building search and question answering pipelines, including retrieval augmented generation and agent based applications. It provides modular components for document retrieval, ranking, and generation that can be combined into custom pipelines.
- **AutoGen**
  - AutoGen is a framework from Microsoft for building applications with multiple agents that communicate with each other to solve tasks. It defines agents with specific roles and lets them exchange messages, delegate subtasks, and collaborate toward a shared goal.
- **CrewAI**
  - CrewAI is an open-source Python framework for creating teams of AI agents, called a crew. Each agent is assigned a name, role, and set of tools, and the system manages planning, communication, and execution between them.
- **Structured logging & tracing**
  - Structured logging and tracing record an agent's execution in a consistent, machine readable format, capturing details like which tool was called, what arguments were used, and how long each step took. Unlike plain text logs, structured data can be filtered, searched, and analyzed programmatically.
- **LangGraph**
  - LangGraph is a Python library designed to help developers create robust and stateful conversational AI applications, often referred to as AI Agents. It allows you to structure complex agent workflows by defining states (data held throughout the conversation) and edges (transitions between states based on agent decisions or external events), creating a graph-like representation of the agent's reasoning process.

### 3.6 Prompt Injection / Jailbreaks
- **Smol Depot**
  - Smol Depot is an open-source kit that lets you bundle all the parts of a small AI agent in one place. You keep prompts, settings, and code files together in a single folder, then point the Depot tool at that folder to spin the agent up.
- **Anthropic Tool Use**
  - Anthropic tool use is Claude's implementation of native function calling, where the model can choose to call a defined tool with structured arguments as part of its response. The calling application executes the tool and returns the result, which Claude can use to continue reasoning or produce a final answer.
- **LangSmith**
  - LangSmith is a web tool that helps you see and fix what your AI agents are doing. It records each call that the agent makes to a language model, the input it used, and the answer it got back.
- **Helicone**
  - Helicone is an open-source tool that helps you watch and understand how your AI agents talk to large language models. You send your model calls through Helicone’s proxy, and it records each request and response without changing the result.
- **LangFuse**
  - Langfuse is an open source observability and analytics platform for LLM applications, providing tracing, evaluation, and prompt management features. It captures detailed traces of agent runs, including nested tool calls, and lets teams analyze performance and quality over time.
- **openllmetry**
  - OpenLLMetry is an open source observability standard that extends OpenTelemetry, a widely used tracing framework, to cover LLM specific data like prompts, completions, and token usage. It lets teams instrument their LLM applications using familiar observability tooling rather than a separate, proprietary system.
- **Agno**
  - Agno is a Python framework designed to streamline the process of building AI agents. It offers tools and abstractions that simplify tasks such as agent planning, tool use, and memory management, making it easier to create sophisticated and functional AI agents without managing low-level implementation details.

### 3.7 Tool sandboxing / Permissioning
- **Tool sandboxing / Permissioning**
  - Tool sandboxing keeps the AI agent inside a safe zone where it can only run approved actions and cannot touch the wider system. Permissioning sets clear rules that say which files, networks, or commands the agent may use.

### 3.8 Data Privacy + PII Redaction
- **Data Privacy + PII Redaction**
  - AI agents often process text, images, and logs that include personal data like names, phone numbers, or addresses. Leaks can cause fraud, stalking, or other harm, so laws like GDPR and CCPA require strict protections.

### 3.9 Bias & Toxicity Guardrails
- **Bias & Toxicity Guardrails**
  - Bias and toxicity guardrails are checks put in place to detect and block outputs that are discriminatory, offensive, or otherwise harmful before they reach a user. These can be implemented through classifier models, keyword filters, or the underlying model's own safety training.

### 3.10 Safety + Red Team Testing
- **Safety + Red Team Testing**
  - Safety + Red Team Testing is the practice of checking an AI agent for harmful or risky behavior before and after release. Safety work sets rules, guardrails, and alarms so the agent follows laws, keeps data private, and treats people fairly.

---

## 4. Optional / Specialized Topics

- Acting / Tool Invocation
- Observation & Reflection
- Personal assistant
- Max Length
- Use relevant technical terms
- Database Queries
- LangSmith
- Ragas
- DeepEval
- Self-critique Agents
- Multi-Agents
- LlamaIndex
- Haystack
- AutoGen
- CrewAI
- Structured logging & tracing
- LangGraph
- LangFuse
- openllmetry
- Agno

---

## 5. References

- [AI Agents Roadmap](https://roadmap.sh/ai-agents)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer
- AI and Data Scientist
- Data Analyst
- MLOps Engineer

### Related Skills
- Prompt Engineering
- Claude Code
- Vibe Coding