# Frontend Developer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/frontend
- Related Roles:
  - Fullstack Developer
  - DevOps Engineer
  - Software Architect

---

## 1. Beginner

### 1.1 Internet
- **How does the internet work?**
  - The internet is a global network connecting computers and devices for information sharing. Enables browsing, email, streaming, and communication through interconnected systems.
- **What is HTTP?**
  - HTTP (Hypertext Transfer Protocol) enables browser-server communication through requests and responses. Stateless protocol using methods like GET and POST.
- **What is Domain Name?**
  - Domain names are human-friendly web addresses (e.g., google.com) substituting numerical IP addresses. Comprise second-level ("google") and top-level (".com") domains.
- **What is hosting?**
  - Web hosting stores website files on servers, making sites accessible online. Types include shared (multiple sites per server) and dedicated (exclusive server) hosting.
- **DNS and how it works?**
  - DNS (Domain Name System) translates human-readable domain names into IP addresses through a global, decentralized server network. Enables easy internet navigation by converting names like www.example.com to numeric addresses browsers can connect to.
- **Browsers and how they work?**
  - Web browsers request and display websites by interpreting HTML, CSS, and JavaScript. Use rendering engines (Blink, Gecko) for display and JavaScript engines (V8) for code execution.

### 1.2 HTML
- **HTML**
  - HTML (Hypertext Markup Language) is the standard for creating web pages, structuring content with elements and attributes. Browsers interpret HTML tags to render pages.

### 1.3 CSS
- **CSS**
  - CSS (Cascading Style Sheets) styles HTML documents, controlling layout, colors, and fonts. Separates design from content using selectors to target elements.

### 1.4 JavaScript
- **JavaScript**
  - JavaScript is a versatile programming language that makes websites interactive. Runs in browsers, servers (Node.js), and desktop applications.

### 1.5 Version Control
- **Git**
  - Git is a distributed version control system tracking code changes and enabling collaborative development. Features branching, merging, and complete project history.

### 1.6 VCS Hosting
- **GitHub**
  - GitHub is the leading Git repository hosting platform for open-source and private projects. Owned by Microsoft since 2018, it's essential for modern software development, project showcasing, and open-source contributions.
- **GitLab**
  - GitLab is a comprehensive DevOps platform offering integrated development tools including Git hosting, CI/CD, issue tracking, and deployment. Available as cloud service or self-hosted solution.
- **Vue.js**
  - Vue.js is a JavaScript framework for building website interfaces. It's easy to start with and can be added to projects bit by bit.
- **React**
  - React is a JavaScript tool from Facebook for building UIs, especially for single-page apps. It lets you create reusable UI parts that update when data changes.

### 1.7 Package Managers
- **yarn**
  - Yarn is Facebook's JavaScript package manager offering fast, reliable, secure alternative to npm. Features lockfile consistency, parallel installations, offline mode, and checksum verification.
- **pnpm**
  - pnpm (performant npm) is a fast, disk-efficient JavaScript package manager using global storage with symlinks. Saves disk space, ensures strict package.json compliance, supports monorepos, and provides better security through dependency isolation.
- **npm**
  - npm (Node Package Manager) is the primary JavaScript package manager for finding, sharing, and managing code dependencies. Uses package.json to track project requirements and enables consistent builds across environments.
- **Bun**
  - Bun is a JavaScript runtime, bundler, transpiler, and package manager, all-in-one. It's designed to be a faster, more efficient alternative to Node.js and npm, aiming to improve performance and developer experience through its speed and comprehensive toolset.

### 1.8 CSS Frameworks
- **Tailwind**
  - Tailwind CSS is a utility-first CSS framework providing small, composable classes for rapid custom design development. Features mobile-first approach, automatic unused style removal (purging), and flexible customization.

### 1.9 Learn a Framework
- **Angular**
  - Angular is Google's TypeScript framework for building single-page applications (SPAs). Features reusable components, two-way data binding, dependency injection, and robust template system.
- **Svelte**
  - Svelte is a JavaScript tool for building UIs. Unlike others, Svelte does its main work during build time, not in the browser.
- **Solid JS**
  - SolidJS is a JavaScript tool for building website interfaces that is known for being very fast and efficient. It updates only the parts of the page that change, which makes it perform well.

### 1.10 Learn the Basics
- **How LLMs work**
  - LLMs, or Large Language Models, are advanced AI models trained on vast datasets to understand and generate human-like text. They can perform a wide range of natural language processing tasks, such as text generation, translation, summarization, and question answering.
- **AI vs Traditional Coding**
  - Traditional software development relies on developers explicitly writing code to instruct computers on how to perform tasks. This involves defining every step and logic manually.
- **Applications**
  - AI is increasingly being used to automate tasks, improve user interfaces, and enhance the overall development process in frontend. It can help with code generation, intelligent suggestions, automated testing, and creating personalized user experiences through features like dynamic content and adaptive layouts.

### 1.11 AI Assisted Coding
- **Claude Code**
  - Claude Code is a family of large language models designed for code generation and understanding. It excels at tasks like code completion, bug finding, documentation, and even translating code between different programming languages.
- **Copilot**
  - GitHub Copilot is an AI-powered code-completion tool that helps developers write code faster and with fewer errors. It uses a combination of machine learning algorithms and access to GitHub's vast repository of open-source code to provide context-aware suggestions for coding tasks.
- **Cursor**
  - Cursor is an AI-powered code editor designed to enhance developer productivity. It leverages large language models to offer features like code completion, generation, and refactoring suggestions.
- **Antigravity**
  - Antigravity is an AI-powered code completion tool designed to enhance developer productivity. Created by Google, it learns from your coding style and project context to provide intelligent suggestions, autocompletions, and code generation snippets directly within your integrated development environment (IDE).

---

## 2. Intermediate

### 2.1 Prompting Techniques
- **Prompting Techniques**
  - Prompt engineering is the process of crafting effective inputs (prompts) to guide AI models to generate desired outputs. It involves strategically designing prompts to optimize the model’s performance by providing clear instructions, context, and examples.

### 2.2 Agents
- **Code Reviews**
  - AI-powered code reviews leverage machine learning models to analyze source code and identify potential issues, such as bugs, security vulnerabilities, code style violations, and performance bottlenecks. These tools can automate parts of the code review process, freeing up developers to focus on more complex problems and improving the overall quality and maintainability of the codebase.

### 2.3 MCP
- **MCP**
  - Model Context Protocol (MCP) is a rulebook that tells an AI agent how to pack background information before it sends a prompt to a language model. It lists what pieces go into the prompt—things like the system role, the user’s request, past memory, tool calls, or code snippets—and fixes their order.

### 2.4 Skills
- **Skills**
  - AI coding assistants can leverage "skills" – pre-defined functions or tools exposed to the AI that allow it to perform specific actions. Instead of relying solely on their internal knowledge and large language models, these assistants can call upon these skills (like running tests, deploying code, or querying databases) when needed.

### 2.5 Implementing AI
- **Gemini**
  - Gemini is a family of multimodal large language models (LLMs) developed by Google. These models are designed to handle and understand different types of data, including text, code, images, audio, and video.
- **OpenAI**
  - OpenAI provides a suite of artificial intelligence models and tools accessible through an API. These models can perform tasks like generating text, translating languages, writing different kinds of creative content, and answering your questions in an informative way.
- **Anthropic**
  - Anthropic is an AI safety and research company focused on developing reliable, interpretable, and steerable AI systems. They create AI models, like Claude, that are designed to be helpful, harmless, and honest, prioritizing safety through techniques like Constitutional AI, where the AI is guided by a set of principles during its training and operation.

### 2.6 Linters & Formatters
- **Prettier**
  - Prettier automatically formats code for consistency across JavaScript, TypeScript, CSS, and other languages. Enforces opinionated style rules, eliminating style debates and saving time.
- **ESLint**
  - ESLint is a JavaScript linter checking code for problems, maintains consistent style, and finds errors. Highly configurable with custom or preset rules.
- **Biome**
  - Biome is a high-performance tool for web projects, designed to format and lint code. It aims to replace a suite of existing tools like Prettier, ESLint, and others, offering a unified solution for code quality and consistency.
- **Docs Generation**
  - AI-powered documentation generation leverages machine learning models to automatically create and maintain software documentation. These tools can analyze code, comments, and other project artifacts to produce API references, tutorials, and other types of documentation, reducing the manual effort required and ensuring accuracy and consistency.
- **Refactoring**
  - Refactoring, in the context of software development, is the process of restructuring existing computer code—changing its internal structure—without changing its external behavior. AI tools can assist in this process by analyzing code for potential improvements in readability, performance, and maintainability.

### 2.7 Module Bundlers
- **Parcel**
  - Parcel is a zero-configuration web app bundler handling JavaScript, CSS, HTML automatically. Features dependency resolution, code transformation, optimization, live reloading, code splitting, and tree-shaking by default.
- **Rollup**
  - Rollup is a JavaScript bundler creating efficient bundles from ES modules. Excels at tree-shaking to remove unused code and supports multiple output formats.
- **esbuild**
  - esbuild is an extremely fast JavaScript bundler and minifier written in Go. Handles modern JavaScript, TypeScript, and JSX with near-instant bundling.
- **Vite**
  - Vite is a modern build tool using native ES modules for instant server starts and fast Hot Module Replacement. Supports Vue, React, Svelte with Rollup for production builds.
- **SWC**
  - SWC (Speedy Web Compiler) is a Rust-based JavaScript/TypeScript compiler and bundler, much faster than Babel. Supports modern JavaScript features, JSX, and TypeScript compilation.
- **Rolldown**
  - Rolldown is a fast JavaScript bundler written in Rust, designed to be a drop-in replacement for Rollup. It takes your JavaScript and related assets (like CSS and images) and packages them into optimized bundles that can be efficiently loaded in a web browser.

### 2.8 Auth Strategies
- **Auth Strategies**
  - Authentication strategies verify a user's identity to grant access. Common methods include Basic Auth (username/password), Session-based (server remembers login), Token-based (like JWT, a secure digital key), OAuth (for third-party access like "Login with Google"), and SSO (Single Sign-On, one login for many apps).

### 2.9 Testing
- **Vitest**
  - Vitest is a fast JavaScript/TypeScript testing framework optimized for Vite with Jest-compatible API. Features live test updates, snapshot testing, mocking, code coverage, parallel execution, and watch mode.
- **Jest**
  - Jest is Facebook's JavaScript testing framework for unit testing with auto mocking, code coverage, and snapshot testing. Works with React, Angular, Vue.
- **Playwright**
  - Playwright is Microsoft's cross-browser automation testing framework supporting Chromium, Firefox, WebKit across platforms. Works with JavaScript, TypeScript, Python, .NET.
- **Cypress**
  - Cypress is a JavaScript end-to-end testing framework running tests directly in browsers. Built on Mocha with excellent asynchronous testing support.

### 2.10 Web Security
- **CORS**
  - CORS (Cross-Origin Resource Sharing) controls web page access to resources from different domains through HTTP headers. Servers specify allowed origins while browsers send preflight requests for permission.
- **HTTPS**
  - HTTPS (Hypertext Transfer Protocol Secure) is HTTP's encrypted version, securing data transmission between browsers and websites. Essential for protecting sensitive information like banking and email.
- **CSP**
  - Content Security Policy (CSP) prevents XSS and clickjacking attacks by specifying trusted content sources through HTTP headers. Website creators define safe sources for scripts, styles, images, and other resources.
- **OWASP Risks**
  - OWASP (Open Web Application Security Project) identifies top web application security risks including injection attacks, broken authentication, data exposure, and vulnerable dependencies. Provides guidance on secure coding practices, regular security testing, and comprehensive protection strategies for web applications.

### 2.11 Web APIs
- **Web APIs**
  - Web APIs are interfaces provided by web browsers that allow JavaScript code to interact with the browser environment and the wider web. These APIs provide access to functionalities like manipulating the Document Object Model (DOM), handling user input, making network requests, managing browser history, and accessing device hardware like the camera or microphone.

### 2.12 React
- **Next.js**
  - Next.js is a React framework supporting server-side rendering and static site generation. Features automatic code splitting, file-based routing, CSS support, API routes, and optimized performance.
- **Tanstack Start**
  - Tanstack Start is a full-stack framework built on React that simplifies the process of creating web applications with server-side rendering (SSR). It provides tools and conventions for routing, data fetching, and deployment, allowing developers to focus on building features rather than configuring infrastructure.

### 2.13 Vue.js
- **Angular**
  - Angular is a popular tool from Google for building websites and web apps. It uses TypeScript (a type of JavaScript) to create large, efficient single-page applications (SPAs), where content loads in one go without needing to reload the whole page.
- **Nuxt.js**
  - Nuxt.js is a Vue.js framework providing structure, automatic routing, and server-side rendering. Supports static site generation, code splitting, and data fetching.
- **GitHub Pages**
  - GitHub Pages is a free static site hosting service that takes HTML, CSS, and JavaScript files directly from a GitHub repository and publishes them as a website. It's ideal for hosting project documentation, portfolios, blogs, and other static websites.
- **Netlify**
  - Netlify is a web development platform that simplifies building, deploying, and hosting websites and web applications. It automates the process of deploying static sites and single-page applications by directly connecting to your Git repository.

### 2.14 SSR
- **SSR**
  - Server-side rendering (SSR) generates complete HTML on the server before sending to browsers. Improves initial load times, SEO, and performance on slow devices.

### 2.15 SvelteKit
- **Svelte**
  - Svelte is a compile-time JavaScript framework building UIs with minimal runtime overhead. Compiles components to optimized vanilla JavaScript without virtual DOM.
- **Astro**
  - Astro is a static site generator supporting multiple frameworks (React, Vue, Svelte) with partial hydration. Renders components to static HTML, sending JavaScript only when needed.

---

## 3. Advanced

### 3.1 Type Checkers
- **react-router**
  - React Router enables client-side routing in React applications, creating single-page apps with multiple views. Handles URL management, provides route definition components, and supports lazy loading and route guards.

### 3.2 SSG
- **Vuepress**
  - VuePress is a Vue.js-powered static site generator optimized for documentation. Creates fast, SEO-friendly sites with Vue-based theming, syntax highlighting, and Markdown support with Vue components.
- **Astro**
  - Astro is a static site generator supporting multiple frameworks (React, Vue, Svelte) with partial hydration. Renders components to static HTML, sending JavaScript only when needed.
- **Next.js**
  - Next.js is a React framework supporting server-side rendering and static site generation. Features automatic code splitting, file-based routing, CSS support, API routes, and optimized performance.

### 3.3 Deployment
- **Vercel**
  - Vercel is a platform designed for deploying and hosting web applications, particularly those built with modern frontend frameworks and static site generators. It provides features like automatic deployments from Git repositories, serverless functions, and a global content delivery network (CDN) to ensure fast and reliable performance.
- **Cloudflare**
  - Cloudflare is a service that sits between your website and its visitors, acting as a reverse proxy. It provides a range of features including a content delivery network (CDN) to speed up website loading times by caching content closer to users, DDoS protection to safeguard against malicious attacks, and SSL/TLS encryption to secure data transmission.
- **Railway**
  - Railway is a cloud platform that simplifies deploying web applications and services. It allows developers to deploy directly from their Git repositories, automatically handling infrastructure concerns like server provisioning, networking, and scaling.
- **Render**
  - Render is a unified cloud platform that simplifies the process of deploying and hosting web applications, static websites, and backend services. It automates infrastructure management, allowing developers to focus on writing code rather than configuring servers.

### 3.4 Design Systems
- **Design Systems**
  - A design system is a structured collection of reusable components, guidelines, standards, and best practices that ensure consistency across an application's visual design and user experience. It typically includes typography, colors, spacing, icons, UI components, interaction patterns, and documentation on how to use everything correctly.

### 3.5 Performance
- **Lighthouse**
  - Lighthouse is an open-source, automated tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication.
- **DevTools Usage**
  - DevTools are a set of web developer tools built directly into web browsers. They allow you to inspect and debug HTML, CSS, and JavaScript, monitor network activity, analyze performance bottlenecks, and more.
- **Service Workers**
  - Service Workers are JavaScript files that act as proxy servers between web browsers and web servers. They can intercept network requests, cache resources, and deliver push notifications, even when the user is offline.
- **Streamed Responses**
  - Streamed responses involve sending data from a server to a client in chunks, rather than waiting for the entire response to be ready before sending anything. This allows the browser to start processing and rendering content sooner, improving perceived performance and user experience, especially for large datasets or long-running processes.
- **Cache-Control**
  - Cache-Control is an HTTP header used to specify caching directives in HTTP requests and responses. These directives control how browsers and other intermediaries (like CDNs) should cache content.

### 3.6 Web Components
- **Custom Elements**
  - Custom Elements enable creating your own HTML tags as part of Web Components. Build reusable webpage components with custom behavior instead of nested standard HTML.
- **HTML Templates**
  - The <template> HTML element holds hidden content for later use by JavaScript. Acts as a reusable blueprint for creating dynamic page elements.
- **Shadow DOM**
  - Shadow DOM creates private, encapsulated DOM trees inside elements, isolating HTML, CSS, and JavaScript from the main page. Prevents style and script conflicts, enabling cleaner, reusable components.

### 3.7 GraphQL
- **Apollo**
  - Apollo GraphQL is a comprehensive platform for GraphQL applications. Apollo Client handles caching, data fetching, and state management.

### 3.8 Accessibility
- **Nuxt.js**
  - Nuxt.js is a Vue.js framework providing structure, automatic routing, and server-side rendering. Supports static site generation, code splitting, and data fetching.
- **Eleventy**
  - Eleventy (11ty) is a flexible static site generator supporting multiple template languages (HTML, Markdown, JavaScript). Creates pages from data sources, adds no client-side JavaScript for fast loading.

### 3.9 PWAs
- **PWAs**
  - Progressive Web Apps (PWAs) are web applications behaving like native apps using HTML, CSS, JavaScript. Feature offline functionality, push notifications, home screen installation, and service workers for caching.

### 3.10 Mobile Apps
- **React Native**
  - React Native enables building native mobile apps for iOS and Android using JavaScript and React. Compiles to native components for authentic look and performance.
- **Flutter**
  - Flutter is Google's cross-platform framework building apps for iOS, Android, web, desktop from single Dart codebase. Features rich widget library, hot reload, and custom rendering engine for consistent UI.
- **Ionic**
  - Ionic is an open-source mobile toolkit that allows developers to build high-quality cross-platform applications for iOS, Android, and the web using a single codebase. It leverages web technologies like HTML, CSS, and JavaScript, and integrates seamlessly with popular frameworks such as Angular, React, and Vue.

### 3.11 Desktop Apps
- **Relay Modern**
  - Relay is Facebook's JavaScript library for data-heavy React applications using GraphQL. Co-locates data requirements with components, enabling efficient fetching and updates.
- **Electron**
  - Electron builds cross-platform desktop apps using web technologies (HTML, CSS, JavaScript) with Chromium and Node.js. Provides native OS access and powers apps like VS Code.
- **Tauri**
  - Tauri builds small, secure desktop apps using web technologies with Rust backend. Uses system webview instead of bundled browser, resulting in smaller apps.
- **Flutter**
  - Flutter is Google's cross-platform framework building apps for iOS, Android, web, desktop from single Dart codebase. Features rich widget library, hot reload, and custom rendering engine for consistent UI.

---

## 4. Optional / Specialized Topics

- GitLab
- yarn
- pnpm
- Angular
- Vue.js
- Svelte
- Solid JS
- Parcel
- Rollup
- Jest
- Cypress
- Custom Elements
- HTML Templates
- Shadow DOM
- react-router
- Relay Modern
- Vuepress
- Nuxt.js
- Eleventy
- Next.js
- Flutter
- Ionic
- SWC
- Astro
- Bun

---

## 5. References

- [Frontend Developer Roadmap](https://roadmap.sh/frontend)

---

## 6. Related Roles / Topics

### Related Roles
- Fullstack Developer
- DevOps Engineer
- Software Architect

### Related Skills
- JavaScript
- Node.js
- React
- Angular
- Vue.js
- Design System