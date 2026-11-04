# AI Product Builder

## Metadata
- Type: Skill
- Domain: Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ai-product-builder
- Related Roles:
  - DevOps Engineer
  - Fullstack Developer
  - Forward Deployed Engineer

---

## 1. Beginner

### 1.1 AI Product Creation Cycle
- **App Anatomy**
  - Every app has the same basic parts: a front end that users interact with, a back end that processes logic, a database that stores data, and an API that connects them. Understanding this structure helps you review what the AI generates and ask better questions when something does not work as expected.

### 1.2 Definition & Scope
- **Tech Stack & Constraints**
  - Define the technologies you want to use before generating anything. AI generation tools produce better output when given clear constraints rather than being left to choose freely.
- **Problem Definition**
  - Start by writing one or two sentences describing the problem your app solves and who it solves it for. If you cannot explain the problem clearly, the generated output will be unfocused.
- **Feature Scoping**
  - List only the features that are strictly necessary for the first version of the product. Every feature you add increases the complexity of the generated code and the time needed to test and refine it.

---

## 2. Intermediate

### 2.1 1. Prototyping
- **Choose a Prototype Tool**
  - Developers are increasingly moving away from traditional design tools like Figma and Miro toward AI prototyping tools that generate a working version of the app directly from a text description. Tools like Lovable, Replit, and Bolt let you go from idea to something clickable in minutes, which makes it easier to validate a concept before committing to a full generation cycle.
- **Feedback & Validation**
  - Before generating the full product, share the prototype with your team and some potential users. You are looking for obvious gaps or misunderstandings in the design.
- **Lovable**
  - Lovable generates a working front-end application from a text description. It is one of the fastest ways to move from an idea to a clickable prototype.
- **Replit**
  - Replit is a browser-based coding environment that also supports AI-assisted app generation. It is useful when you want to prototype and immediately run the code in the same place.
- **v0**
  - v0 is Vercel's UI generation tool. You describe a component or screen, and it produces React code ready to use in your project.
- **Claude Design**
  - Understand fundamental concepts, architectures, and implementation practices of Claude Design.

### 2.2 2. Generation
- **Bolt**
  - Bolt generates full-stack applications from a prompt and produces clean, readable code. It is faster than writing from scratch and gives you more control over the output than most no-code tools.
- **Hope**
  - Hope is an agentic architect that transforms human prompts into composable, production-ready software. By automating complex engineering, it bridges the gap between rapid prototyping and professional standards, enabling teams to build scalable, enterprise-grade systems in hours.

### 2.3 3. Refinement
- **Cursor**
  - Cursor lets you select any part of the codebase and ask questions or request changes directly in the editor. It is the most practical tool for navigating AI-generated code you did not write yourself.
- **Codex**
  - Codex is best for translating a clearly defined requirement into working code. Describe the specific behavior you want; it generates the implementation.
- **Claude Code**
  - Claude Code works in the terminal and is best used when you need to understand a piece of generated code before modifying it. Give it a specific problem; ask it to explain a function, trace a bug, or rewrite a block of logic.
- **Copilot**
  - Copilot works inline as you type and is best used when you know what you want to write but want to move faster. It predicts the next line or block based on the surrounding code.
- **Gemini CLI**
  - Gemini CLI is Google's command-line AI tool for developers. It integrates with your existing terminal workflow and can assist with code generation, explanation, and refactoring.
- **Targeted Change**
  - A targeted change is a small, localized fix: a bug in a component, a layout adjustment, a logic tweak. Use AI-assisted coding tools like Cursor, Claude Code, or Copilot to make these changes directly in the code without touching the broader architecture.
- **New Feature / Structural Change**
  - When a change affects the architecture of the app, such as adding a new service, reworking the data model, or introducing a new user flow, go back through the generation tool rather than patching the code manually. This keeps the codebase consistent and reduces technical debt.

---

## 3. Advanced

### 3.1 4. Collaboration
- **Cloudflare**
  - Cloudflare offers serverless deployment for front-end apps and lightweight back-end functions through Cloudflare Workers and Pages. It has a generous free tier and deploys to a global edge network, which means fast load times for users anywhere in the world.
- **HTML / CSS / JavaScript**
  - These are the three foundational technologies of every web app. HTML defines the structure of a page, CSS controls how it looks, and JavaScript makes it interactive.
- **React**
  - React is the most widely used library for building web interfaces. Most AI-generated front ends use React by default.
- **Browsers / DevTools**
  - Browser developer tools let you inspect HTML, debug JavaScript, monitor network requests, and measure performance directly in the browser. They are the first place to look when something in the front end is not working as expected.
- **Node.js**
  - Node.js is the runtime that allows JavaScript to run on a server. Most AI-generated back ends use Node.js.
- **User Testing**
  - User testing means putting the app in front of real people and watching how they use it. You are not looking for opinions; you are looking for moments where they hesitate, get confused, or do something unexpected.
- **Unit Testing**
  - A unit test checks that a single function or component behaves as expected in isolation. AI-generated codebases sometimes include unit tests automatically; if they do not, write them for the parts of the code that handle critical business logic.
- **Integration Testing**
  - Integration tests check that different parts of the app work correctly together; for example, that a form submission reaches the database and returns the right response. They catch problems that unit tests miss because they test the connections between components, not the components themselves.
- **E2E Testing**
  - End-to-end tests simulate a real user moving through the app from start to finish. They verify that the full system works as expected in an environment that resembles production.

### 3.2 5. Deployment
- **AWS**
  - AWS is the largest cloud provider in the world. It offers infrastructure for computing, storage, databases, networking, and dozens of other services.
- **Azure**
  - Azure is Microsoft's cloud platform. It is a strong choice for teams already using Microsoft tools or working in enterprise environments.
- **GCP**
  - Google Cloud Platform is Google's cloud infrastructure service. It is particularly strong for data processing, machine learning workloads, and applications that need to integrate with other Google services.
- **Vercel**
  - Vercel is a platform designed for deploying and hosting web applications, particularly those built with modern frontend frameworks and static site generators. It provides features like automatic deployments from Git repositories, serverless functions, and a global content delivery network (CDN) to ensure fast and reliable performance.
- **Render**
  - Render is a cloud platform that supports web services, background workers, cron jobs, and static sites. It is straightforward to configure and deploy directly from a GitHub repository.
- **Railway**
  - Railway is a deployment platform designed for speed and simplicity. It detects the type of project automatically and configures the deployment environment accordingly.
- **DigitalOcean**
  - DigitalOcean is a cloud provider focused on simplicity and developer experience. Its App Platform lets you deploy a full-stack application from a GitHub repository with minimal configuration.
- **MongoDB / Atlas**
  - MongoDB is a document-based database that stores data in a flexible, JSON-like format. Atlas is MongoDB's managed cloud service, which handles backups, scaling, and monitoring automatically.
- **PostgreSQL / MySQL**
  - PostgreSQL and MySQL are relational databases that store data in structured tables with defined relationships. They are the most widely used databases for web applications and are well supported by every major cloud provider.
- **Supabase**
  - Supabase is an open-source alternative to Firebase built on top of PostgreSQL. It provides a managed database, built-in authentication, real-time subscriptions, and an auto-generated API.
- **GitHub**
  - GitHub is the most widely used platform for hosting and managing code. It tracks every change to the codebase, makes it easy to collaborate with others, and integrates with most CI/CD tools.
- **GitLab**
  - GitLab is an alternative to GitHub that combines version control with built-in CI/CD pipelines and project management tools. It is a good option if you want everything in one platform or if your organization already uses it.
- **Bit Cloud**
  - Bit Cloud is how humans and AI agents build software autonomously. It enables them to build and maintain software as independent, decoupled building blocks—each owned separately, yet composable into larger systems—so everyone can work in parallel without friction.
- **Azure DevOps**
  - Azure DevOps is Microsoft's platform for managing code, pipelines, and project tasks. It integrates tightly with Azure infrastructure and is a common choice in enterprise environments.

---

## 4. Optional / Specialized Topics

- v0
- Claude Design
- Gemini CLI
- Targeted Change
- New Feature / Structural Change
- Node.js
- User Testing
- Unit Testing
- Integration Testing
- E2E Testing
- Render
- Railway
- DigitalOcean
- MongoDB / Atlas
- PostgreSQL / MySQL
- Supabase
- GitHub
- GitLab
- Bit Cloud
- Azure DevOps

---

## 5. References

- [AI Product Builder Roadmap](https://roadmap.sh/ai-product-builder)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Fullstack Developer
- Forward Deployed Engineer

### Related Skills
- Claude Code
- Vibe Coding
- OpenClaw