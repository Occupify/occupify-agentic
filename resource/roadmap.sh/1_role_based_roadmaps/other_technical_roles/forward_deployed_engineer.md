# Forward Deployed Engineer

## Metadata
- Type: Role
- Domain: Solutions Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/forward-deployed-engineer
- Related Roles:
  - Fullstack Developer
  - DevOps Engineer
  - AI Engineer
  - Backend Developer
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **Roles & Responsabilities**
  - The FDE job has three phases: audit, evals, and deployment. In the audit phase, you embed with different teams inside the customer's organization, map their workflows, identify bottlenecks, and decide where AI can create real value and where it cannot.
- **From X to FDE**
  - Three backgrounds tend to transition well into the FDE role: software engineers, consultants, and product managers. Software engineers already have the technical foundation but often need to develop the ability to communicate AI tradeoffs to non-technical stakeholders and build a portfolio that shows they can own a full deployment, not just write code.
- **FDE Tiers**
  - Not all FDE roles are the same. The job market has split into three distinct tiers with different skill requirements.
- **Delta**
  - The Delta is the original term Palantir used for what is now called an FDE. It refers to the gap between what a software product does out of the box and what a specific customer actually needs.
- **Last-Mile Integration**
  - Last-mile integration refers to the final set of connections between a product and the specific systems, data sources, and workflows of a customer environment. It is called last-mile because it is often the shortest but hardest part of a deployment: the product works in general, but making it work with this particular customer's setup requires custom engineering.
- **Day 2 Operations**
  - Day 2 Operations refers to everything that happens after a system goes live. Day 1 is the launch.
- **UAT**
  - User Acceptance Testing (UAT) is the process by which a customer's own team validates that a system works correctly before it goes into production. It typically involves preparing test scripts, defining acceptance criteria, and supporting the customer during testing.

### 1.2 Learn a Language
- **Productized Consulting**
  - Productized consulting refers to a model where a consulting engagement delivers not just advice or a custom solution but a repeatable, packaged system that can be redeployed with other customers. It means building in a way that abstracts customer-specific details so the core architecture can be reused across similar engagements.
- **Embedded Engineering**
  - Embedded engineering describes the physical and organizational model of an FDE engagement: the engineer is embedded inside the customer's team, not working remotely or at arm's length. This means joining the customer's Slack, attending their standups, working in their codebase, and being present in the environment where the problems actually live.
- **Python**
  - Python is a general-purpose programming language known for its readable syntax and broad ecosystem. It is widely used in web development, data engineering, scripting, automation, and AI/ML workloads.
- **Java / Scala**
  - Java is a statically typed, object-oriented language that runs on the Java Virtual Machine (JVM) and is widely used in enterprise systems, backend services, and Android development. Scala is also a JVM language that blends object-oriented and functional programming styles, commonly used in data processing with Apache Spark.
- **JavaScript / TypeScript**
  - JavaScript is the programming language of the web, running natively in browsers and on servers via Node.js. TypeScript is a superset of JavaScript that adds static type annotations, catching errors at compile time and improving code maintainability at scale.
- **Go**
  - Go is a statically typed, compiled language developed by Google, designed for simplicity and performance. It is commonly used for building backend services, command-line tools, and cloud infrastructure components.

### 1.3 DSA & System Design
- **Rust**
  - Rust is a systems programming language that focuses on safety, speed, and concurrency. It manages memory through a unique ownership model with strict compiler checks, which allows developers to prevent common bugs like null pointer dereferences and buffer overflows without needing a garbage collector.
- **C++**
  - C++ is a high-performance, statically typed language that gives developers fine-grained control over memory and system resources. It is used in systems programming, game engines, embedded software, and performance-critical applications.

### 1.4 Git & GitHub
- **Git & GitHub**
  - Git is a distributed version control system that tracks changes to code over time and allows multiple people to collaborate on the same codebase without overwriting each other's work. GitHub builds on top of Git with features like pull requests, code review, issue tracking, and CI/CD integrations.

### 1.5 Linux Skills
- **Linux Skills**
  - Linux is an open-source operating system used widely in servers, cloud environments, and developer workstations. Most production software runs on Linux, so being comfortable navigating a Linux system, managing processes, reading logs, and configuring services is a practical necessity for anyone building and deploying in real customer environments.

### 1.6 Frontend Skills
- **React**
  - React is a JavaScript library for building user interfaces using a component-based model. Each component manages its own state and rendering logic, and components are composed to build complete interfaces.
- **JavaScript**
  - JavaScript is the scripting language that runs in web browsers, giving web pages dynamic behavior. It handles user interactions, DOM manipulation, and API requests.
- **CSS**
  - CSS, or Cascading Style Sheets, controls the visual appearance of HTML elements on a web page. It handles layout, colors, typography, spacing, animations, and responsive design.
- **HTML**
  - HTML, or HyperText Markup Language, is the standard language for structuring content on the web. It defines the elements of a page such as headings, paragraphs, links, forms, and images.

---

## 2. Intermediate

### 2.1 Backend Skills
- **PostgreSQL**
  - PostgreSQL is a powerful, open-source relational database system that supports advanced features like JSONB storage, full-text search, window functions, and custom data types. It goes well beyond what basic SQL databases offer and is a widely used default in both startups and large organizations.
- **NoSQL DBs**
  - NoSQL databases store data in formats other than traditional relational tables, such as documents, key-value pairs, graphs, or wide columns. Examples include MongoDB, Redis, Cassandra, and DynamoDB.
- **Node.js**
  - Node.js is a JavaScript runtime built on Chrome's V8 engine that lets developers run JavaScript on the server side. It uses a non-blocking, event-driven architecture that makes it efficient for I/O-heavy workloads like APIs, real-time applications, and data streaming.
- **APIs Design**
  - API design is the process of defining how services communicate with each other through well-structured interfaces. Good API design involves choosing the right protocol (REST, GraphQL, gRPC), defining clear resource models, handling errors consistently, and versioning carefully.
- **GraphQL**
  - GraphQL is a query language and runtime for APIs that lets clients request exactly the fields they need, rather than consuming fixed endpoints with predefined shapes. This reduces over-fetching, makes APIs more flexible, and is especially useful in frontend-heavy applications with complex or variable data requirements.
- **SQL**
  - SQL, or Structured Query Language, is the standard language for interacting with relational databases. It is used to create, read, update, and delete records, and to define the structure of tables and their relationships.

### 2.2 Data Engineering Skills
- **Data Modeling**
  - Data modeling is the process of deciding how data should be structured and stored so it can be queried efficiently and understood by the people who use it. Common patterns include the star schema, where a central fact table is surrounded by dimension tables; the one big table (OBT) approach favored in some analytics workloads; and the medallion architecture used in data lakehouses, where data flows through bronze (raw), silver (cleaned), and gold (aggregated) layers.
- **Data Pipelines**
  - A data pipeline is a series of steps that move and transform data from one place to another, usually from source systems into a warehouse or processing layer. Pipelines can be batch-based (running on a schedule) or streaming (processing data as it arrives).
- **Spark**
  - Apache Spark is a distributed computing framework for processing large datasets in parallel across a cluster. It supports batch processing, streaming, SQL queries, and machine learning through a unified API.
- **Airflow**
  - Apache Airflow is an open-source workflow orchestration platform for scheduling and monitoring data pipelines. Pipelines are defined as Directed Acyclic Graphs (DAGs) in Python, where each node represents a task.
- **Data Warehouses**
  - A data warehouse is a system optimized for analytical queries across large volumes of structured data. The major platforms in enterprise environments are Snowflake, Google BigQuery, and Amazon Redshift.

### 2.3 AI Engineering Skills
- **LLM Fundamentals**
  - Large language models (LLMs) are machine learning models trained on large amounts of text data that can generate, summarize, classify, and reason about language. They work by predicting the most likely next tokens given a context window of input.
- **Prompt Engineering**
  - Prompt engineering is the practice of crafting inputs to language models in a way that produces more accurate, useful, or reliable outputs. Techniques include zero-shot and few-shot prompting, chain-of-thought reasoning, role assignment, and structured output formatting.
- **RAGs**
  - Retrieval-Augmented Generation (RAG) is a pattern where relevant documents or data are fetched from a knowledge source and injected into a model's context before generating a response. This gives the model access to specific or up-to-date information without requiring fine-tuning.
- **Vector DBs**
  - Vector databases store high-dimensional vector embeddings and support efficient similarity search, usually using approximate nearest neighbor algorithms. They are a core component of RAG systems and semantic search applications, where the goal is to find content semantically similar to a query rather than matching keywords.
- **Choosing Model Providers**
  - Different LLM providers offer models with different tradeoffs in capability, cost, latency, context length, and licensing terms. Common providers include OpenAI, Anthropic, Google, Meta (open weights), and Mistral.
- **Context Engineering**
  - Context engineering is the practice of strategically curating, structuring, and refining the information provided to a Large Language Model to ensure accurate and relevant outputs. It involves techniques like prompt crafting, Retrieval-Augmented Generation (RAG), and managing conversation memory to provide the model with the necessary background knowledge for specific tasks.

### 2.4 AI Agents
- **Agent Architectures**
  - Agent architectures define how an AI agent is structured: how it reasons, selects tools, manages memory, and decides when to stop. Common patterns include ReAct (reason + act), plan-and-execute, and tree-of-thought.
- **Tools & Functions**
  - Tools and functions are the mechanisms through which AI agents interact with the outside world. A tool might query a database, call an external API, run a code interpreter, or search the web.
- **Memory & State**
  - Memory in AI agents refers to how information is stored and retrieved across steps in a conversation or task. Short-term memory lives in the context window, while long-term memory requires external storage like a database or vector store.
- **MCP**
  - The Model Context Protocol (MCP) is an open standard for connecting AI models to external tools and data sources through a unified interface. Instead of building custom integrations for every tool, developers implement MCP servers that expose tools and resources in a standardized way.
- **Multi-Agents**
  - Multi-agent systems involve multiple AI agents working together, where each agent has a specific role or capability and they coordinate to complete a larger task. One agent might plan the work while others execute specific subtasks, and a final agent synthesizes the results.
- **Prompt Management**
  - Prompt management is the systematic process of creating, versioning, testing, and refining the text inputs used to guide large language models toward desired outputs. It involves maintaining a structured library of effective prompt templates, tracking how specific changes in phrasing impact model performance, and integrating these prompts into the application development lifecycle.

### 2.5 Vibe Coding
- **Claude Code**
  - Claude Code is an AI coding assistant built on Anthropic's Claude model. It can write, edit, explain, and debug code across a wide range of languages and frameworks, and is designed to handle complex multi-file tasks and refactoring alongside code generation.
- **Codex**
  - Codex is OpenAI's code-focused model, trained on large amounts of public code. It can generate code from natural language descriptions, complete functions, and help with documentation.
- **Cursor**
  - Cursor is an AI-powered code editor built on top of VS Code that integrates LLMs directly into the coding experience. It supports chat-based code editing, multi-file edits, codebase-aware completions, and agent-style workflows where the model can make changes across an entire project.
- **OpenCode**
  - OpenCode is an open-source AI coding agent that runs in the terminal. It works with many model providers, including Anthropic, OpenAI, Google and locally hosted models, so you are not tied to a single vendor.

### 2.6 Integration Engineering
- **Gemini**
  - Gemini is Google DeepMind's family of multimodal AI models, capable of processing and generating text, code, images, and more. It is available via Google AI Studio and Vertex AI in different sizes with varying tradeoffs in speed and capability.
- **Working with Legacy Systems**
  - Legacy systems are the established, often undocumented infrastructure that most large organizations run their core operations on. They may be on-prem databases with no API, ERP systems that took years and millions of dollars to migrate to, or internal tools written a decade ago that no one fully understands anymore.
- **OpenClaw**
  - OpenClaw is an AI-assisted development tool designed to automate the integration and interaction between complex software systems and large language models. It functions by providing a structured framework for developers to execute code generation, refactoring, and debugging tasks directly within their existing environment, effectively lowering the barrier for rapid prototyping.

### 2.7 Cloud Platforms
- **AWS**
  - Amazon Web Services (AWS) is the largest cloud platform by market share, offering hundreds of services including compute (EC2, Lambda), storage (S3), databases (RDS, DynamoDB), networking, and AI/ML tooling. It has a deep ecosystem of third-party integrations and is the most widely used cloud platform across startups and enterprises.
- **GCP**
  - Google Cloud Platform (GCP) is Google's cloud offering, known for strong data and analytics services like BigQuery and AI/ML infrastructure like Vertex AI. It is often the preferred choice for data-intensive workloads and organizations already using Google Workspace.
- **Azure**
  - Microsoft Azure is Microsoft's cloud platform with particularly strong adoption in enterprise environments, especially those using Active Directory, Office 365, and .NET. It offers compute, storage, networking, databases, DevOps tooling, and AI services including Azure OpenAI Service.
- **Terraform**
  - Terraform is an open-source infrastructure-as-code tool by HashiCorp that lets engineers define cloud resources in configuration files and provision or update them automatically. It works across multiple cloud providers and is the standard tool for managing infrastructure in a repeatable, version-controlled way.

### 2.8 Containers
- **Docker**
  - Docker is the leading platform for building, shipping, and running containers. A Dockerfile defines the steps to build a container image, and Docker provides tools to run those images locally or push them to a registry for deployment.
- **Kubernetes**
  - Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. It handles scheduling containers across a cluster, managing service discovery, load balancing, rolling updates, and self-healing by restarting failed containers.

---

## 3. Advanced

### 3.1 DevOps Skills
- **DevOps Skills**
  - DevOps is the practice of automating and streamlining how software is built, tested, and deployed. A forward-deployed engineer who knows DevOps can own the full deployment lifecycle, from spinning up infrastructure to shipping a containerized agent into a client's cloud environment, without depending on another team to get there.

### 3.2 Observability
- **Inference Optimization**
  - Inference optimization refers to techniques for making model predictions faster and cheaper without significantly reducing quality. Common approaches include quantization (reducing numerical precision), distillation (training a smaller model to mimic a larger one), caching repeated requests, and batching.
- **Building Eval Pipelines**
  - Evaluation pipelines are automated systems for measuring the quality of an AI model or application over a set of test cases. A good eval does not just check whether the final answer is correct.
- **Debugging Agent Logic**
  - Debugging AI agent logic involves tracing through the sequence of reasoning steps, tool calls, and decisions an agent made to find where it went wrong. This is harder than debugging traditional code because agent behavior is non-deterministic and depends on model outputs.

### 3.3 Security
- **DevSecOps**
  - DevSecOps integrates security practices directly into the DevOps pipeline rather than treating security as a final gate before release. This includes automated security scanning in CI/CD, dependency vulnerability checks, secrets management, and security review as part of the development process.
- **API Security**
  - API security covers the practices and controls needed to protect APIs from unauthorized access and abuse. This includes authentication, authorization, rate limiting, input validation, and protection against common attacks like injection and replay attacks.
- **Authentication**
  - Authentication is the process of verifying the identity of a user or system. Common mechanisms include username/password, API keys, OAuth 2.0 tokens, and JWTs.
- **AI Governance**
  - AI governance refers to the policies, processes, and controls that ensure AI systems behave safely, fairly, and in compliance with regulations and organizational standards. This includes defining acceptable use, managing model risk, ensuring transparency in AI decision-making, and monitoring for bias or harmful outputs.
- **Data Privacy & Compliance**
  - Data privacy and compliance involves handling personal or sensitive data according to applicable laws and organizational policies. Relevant regulations include GDPR, CCPA, HIPAA, and others depending on the industry and geography.

### 3.4 MLOps
- **MLOps**
  - MLOps applies DevOps principles to machine learning systems, covering the processes and tooling needed to reliably build, deploy, monitor, and update ML models in production. This includes versioning data and models, automating training pipelines, serving inference at scale, and detecting model degradation over time.

### 3.5 Discovery & Scoping
- **Requirements Gathering**
  - Project requirements come from observation as much as from conversation. You watch how teams actually work, not just how they describe their work, because those two things are often different.
- **Scoping & Sequencing**
  - Technical scoping involves breaking a project into discrete tasks, estimating their complexity, and identifying dependencies. Sequencing means ordering those tasks logically, starting with the highest-risk or most uncertain parts.
- **Scope, Speed, Quality**
  - Every project involves tradeoffs between scope (how much is built), speed (how fast it is delivered), and quality (how well it holds up over time). Reducing scope can speed things up without sacrificing quality.

### 3.6 Business Acumen
- **Enterprise Workflow**
  - Enterprise workflows are the processes and systems through which large organizations operate, including approvals, handoffs, integrations with existing tools, and compliance requirements. Building for enterprise environments requires understanding these workflows and designing solutions that fit within them.
- **ROI & AI Impact**
  - Understanding return on investment (ROI) for AI projects means being able to quantify how an AI system creates value, whether through cost savings, productivity improvements, revenue growth, or risk reduction. It also means being honest about what AI can realistically deliver.
- **Stakeholder Management**
  - Stakeholder management in FDE work is less about keeping people happy and more about making sure the right people know what is happening before it becomes a problem. This means identifying who the skeptics are early, giving them the evidence they need to trust the system (usually evals), managing expectations before a demo rather than after it goes wrong, and escalating blockers fast rather than letting them quietly slow the engagement.
- **Product Feedback Loop**
  - A product feedback loop is the cycle of shipping something, collecting feedback from users or stakeholders, and using that input to improve future iterations. This usually means working closely with the customer to observe how the delivered product is actually being used, identifying gaps between expectation and reality, and feeding those observations back into the build process while still on the engagement.
- **Time-to-Value**
  - Time-to-value is the elapsed time between the start of an engagement and the moment the customer has something they can actually use. Compressing it means shipping a working feature early rather than designing the perfect system, prioritizing the work that demonstrates the most value first, and sequencing deliverables so that trust builds incrementally.

### 3.7 Communication
- **Technical Writing**
  - Technical writing is the practice of producing clear, accurate, and useful documentation for software systems. This includes API docs, architecture decision records, runbooks, onboarding guides, and design documents.
- **Executive Reporting**
  - Executive reporting is the practice of communicating the status of a technical engagement to non-technical decision makers in a format they can act on. A good executive update leads with value delivered, not tasks completed.

---

## 4. Optional / Specialized Topics

- Last-Mile Integration
- Day 2 Operations
- UAT
- JavaScript / TypeScript
- Go
- GraphQL
- SQL
- Data Warehouses
- Choosing Model Providers
- Context Engineering
- Multi-Agents
- Prompt Management
- Data Privacy & Compliance
- Time-to-Value

---

## 5. References

- [Forward Deployed Engineer Roadmap](https://roadmap.sh/forward-deployed-engineer)

---

## 6. Related Roles / Topics

### Related Roles
- Fullstack Developer
- DevOps Engineer
- AI Engineer
- Backend Developer
- Frontend Developer

### Related Skills
- Python
- AI Agents
- Linux