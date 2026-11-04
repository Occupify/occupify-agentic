# Next.js

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/nextjs
- Related Roles:
  - Frontend Developer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Introduction
- **JavaScript Basics**
  - JavaScript is a programming language that adds interactivity to websites. It allows you to create dynamic content, control multimedia, animate images, and much more.
- **Why React**
  - React is a JavaScript library designed for building user interfaces in a declarative and component-based way. It simplifies the process of creating dynamic and interactive web applications by allowing developers to break down complex UIs into smaller, reusable pieces.
- **Why Frontend Frameworks**
  - Building modern web applications often involves managing complex user interfaces, handling data efficiently, and ensuring a smooth user experience. Frontend frameworks like React, Angular, and Next.js provide a structured approach to these challenges.
- **SPA vs SSR**
  - Single-Page Applications (SPAs) load a single HTML page and dynamically update the content using JavaScript, providing a fluid user experience without full page reloads. Server-Side Rendering (SSR), on the other hand, generates the HTML on the server for each request, sending a fully rendered page to the client.

### 1.2 React Frameworks
- **Next.js**
  - Next.js is a React framework that provides extra features and optimizations on top of React for building web applications. It simplifies development by offering solutions for routing, data fetching, and server-side rendering out of the box.
- **Why Next.js**
  - Next.js is a React framework that provides extra features and optimizations beyond what React offers on its own. When choosing a framework built on React, Next.js stands out because it simplifies development with features like built-in routing, server-side rendering, and static site generation.
- **Remix**
  - Remix is a full-stack web framework that focuses on web standards and modern web development patterns. It emphasizes server-side rendering and progressive enhancement to deliver fast and resilient user experiences.
- **SSR**
  - Server-Side Rendering (SSR) is a technique where a web application's HTML is generated on the server in response to each user request. The server then sends the fully rendered HTML to the client's browser, which displays it.

### 1.3 create-next-app
- **SPA**
  - A Single-Page Application (SPA) is a web application that loads a single HTML page and dynamically updates that page as the user interacts with the application. This is achieved by using JavaScript to manipulate the DOM (Document Object Model) directly, rather than requesting new HTML pages from the server for each interaction.

### 1.4 Next.js Routing Basics
- **Next.js Routing Basics**
  - Routing is the process of defining how an application responds to client requests to specific endpoints (URIs). In Next.js, routing is primarily file-system based.

### 1.5 Rendering Strategies
- **CSR**
  - In Client-Side Rendering (CSR) with React, the browser downloads a minimal HTML page and the JavaScript needed for the page. The JavaScript is then used to update the DOM and render the page.
- **SSG**
  - Static Site Generation (SSG) is a rendering method that generates HTML pages at build time. This means that when a user requests a page, the server sends a pre-rendered HTML file, rather than dynamically generating it on each request.

### 1.6 Types of routers
- **Why use App Router?**
  - The App Router in Next.js is a new routing system built on React Server Components, offering enhanced flexibility and performance compared to the traditional Pages Router. Before Next.js 13, the Pages Router was the main way to create routes in Next.js.
- **Pages**
  - The Pages Router in Next.js is a file-system based router built around the pages directory. Each file in the pages directory becomes a route based on its file name.
- **App**
  - The App Router is a file-system based router that uses React's latest features, such as Server Components, Suspense, and Server Functions

### 1.7 Routing Terminology
- **Routing Terminology**
  - In Next.js, routing is primarily handled through the app directory (introduced in Next.js 13) and the older pages directory. Key terms include:

### 1.8 Rendering Pages
- **Rendering Pages**
  - Rendering refers to the process of converting your code into HTML that can be displayed in a web browser. Next.js offers different strategies for this, including server-side rendering (SSR), static site generation (SSG), incremental static regeneration (ISR), and client-side rendering (CSR).

### 1.9 Layouts and Templates
- **Layouts and Templates**
  - Layouts and templates provide a way to share UI elements across multiple pages, maintaining state and avoiding unnecessary re-renders. Layouts wrap around pages, persisting across route changes to preserve things like navigation bars or sidebars.

### 1.10 Loading and Streaming
- **Loading and Streaming**
  - The special file loading.js helps you create meaningful Loading UI with React Suspense. With this convention, you can show an instant loading state from the server while the content of a route segment loads.

---

## 2. Intermediate

### 2.1 Error States
- **Error States**
  - Error states in Next.js routing refer to how your application handles situations where a route cannot be successfully loaded or rendered. Errors can be divided into two categories: expected errors and uncaught exceptions.

### 2.2 Routing Patterns
- **Intercepting Routes**
  - Intercepting routes allows you to load a route from another part of your application within the current layout. This routing paradigm can be useful when you want to display the content of a route without the user switching to a different context.
- **Parallel Routes**
  - Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.

### 2.3 API Endpoints
- **Static vs Dynamic**
  - API endpoints in Next.js allow you to create serverless functions that handle requests. These endpoints can be either static or dynamic, depending on how their routes are defined and how they process data.
- **Streaming**
  - Streaming in Next.js API endpoints allows you to send data to the client in chunks, rather than waiting for the entire response to be generated on the server before sending anything. This can significantly improve perceived performance, especially for long-running processes or when dealing with large datasets.
- **Reditects**
  - Redirects in Next.js API endpoints allow you to send a user from one URL to another. This is useful for various scenarios, such as moving or renaming pages, handling temporary content changes, or guiding users to a different part of your application based on specific conditions.
- **Caching**
  - When you don't know the exact route segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time. One example is catch-all segments, which allow you to extend API Routes to catch all subsequent paths.

### 2.4 Structuring Routes
- **Structuring Routes**
  - Structuring routes in Next.js involves organizing your project's file system to define the different URLs (or routes) of your application. Each file within the app directory (or pages directory in older versions) corresponds to a specific route.

### 2.5 Proxy
- **Setting Headers**
  - Middleware in Next.js allows you to run code before a request is completed. Setting headers within middleware enables you to modify the HTTP response headers, controlling aspects like caching, security policies, or custom information passed to the client.
- **Using Cookies**
  - Cookies are small pieces of data that websites store on a user's computer to remember information about them, such as login details, preferences, or shopping cart items. In Next.js middleware, you can access and modify these cookies before a request is handled by your application's routes, allowing you to implement features like authentication, personalization, and A/B testing based on cookie values.
- **Use cases**
  - Middleware in Next.js allows you to run code before a request is completed. This provides a flexible way to modify the response by rewriting, redirecting, adding headers, or even directly responding.
- **Route Matcher**
  - A route matcher in Next.js middleware allows you to conditionally execute middleware based on the incoming request's path. It defines specific patterns or conditions that the request path must satisfy for the middleware to run.

### 2.6 Internationalization
- **Internationalization**
  - Internationalization is the process of designing and developing applications that can be adapted to various languages and regions without engineering changes. Next.js enables you to configure the routing and rendering of content to support multiple languages.

### 2.7 Fetching Locations
- **Client**
  - Client-side data fetching involves retrieving data directly in the user's browser using JavaScript. This happens after the initial HTML content is loaded.
- **Server**
  - Fetching data on the server in Next.js allows you to retrieve location information before the page is rendered. This approach improves performance by reducing the amount of work the client's browser needs to do, leading to faster initial page loads and better SEO.

### 2.8 Caching Data
- **Memoization in Fetch**
  - Memoization is an optimization technique that speeds up subsequent function calls by caching the results of previous calls with the same input parameters. This approach allows for re-use of data in a React Component tree, prevents redundant network calls and enhances performance For the initial request, data is fetched from an external source and the result is stored in memory Subsequent requests for the same data within the same render pass retrieve the result from memory, bypassing the need to make the request again.
- **React Cache**
  - The React cache function allows you to memoize the return value of a function, allowing you to call the same function multiple times while only executing it once.

### 2.9 Data Fetching Patterns
- **Parallel vs Sequential**
  - When fetching data inside React components, you need to understand parallel and sequential data fetching. Parallel fetching starts independent requests at the same time, while sequential fetching runs requests one after another when later requests depend on earlier results.
- **Preloading Data**
  - Another way to optimize data fetching is to use the preload pattern. You can optionally create a preload function to further optimize parallel data fetching.

### 2.10 Handling Sensitive Data
- **Handling Sensitive Data**
  - Sensitive data, like API keys or user credentials, requires careful management to prevent exposure. In Next.js, you should avoid directly embedding such data in client-side code or committing it to your repository.

### 2.11 Server Actions
- **Server Actions**
  - Server Functions are asynchronous functions that are executed on the server. They can be used in Server and Client Components to handle form submissions and data mutations in Next.js applications.

### 2.12 Runtimes and Types
- **Node.js**
  - Node.js is a JavaScript runtime environment that executes JavaScript code outside of a web browser. It allows developers to use JavaScript for server-side scripting and to build scalable network applications.
- **Edge**
  - The Edge Runtime is a lightweight JavaScript runtime environment based on V8, designed to execute code closer to the user. It allows you to run server-side logic, like API routes and middleware, on a globally distributed network of servers.

### 2.13 Client Rendered
- **Client Rendered**
  - Client-Side Rendering (CSR) means the browser receives a minimal HTML page from the server. The browser then downloads the JavaScript code, which is responsible for rendering the entire user interface.

---

## 3. Advanced

### 3.1 Server Rendered
- **Server Rendered**
  - Server-Side Rendering (SSR) is a technique where a web application's initial HTML is generated on the server in response to a user's request. This pre-rendered HTML is then sent to the client's browser, allowing the user to see the content immediately, even before the JavaScript code is fully executed.

### 3.2 Global CSS
- **Revalidating Cached Data**
  - Revalidation is the process of updating cached data. When you cache data, it's stored for a certain period.
- **Revalidation Errors**
  - When revalidation fails, it means the attempt to refresh the cached data encountered an issue, preventing the application from displaying the most up-to-date information. These errors can stem from various sources, such as network connectivity problems, issues with the data source itself (e.g., a database being unavailable), or problems within the revalidation logic.
- **CSS Modules**
  - CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.
- **Sass**
  - Sass (Syntactically Awesome Style Sheets) is a CSS preprocessor that extends the capabilities of standard CSS. It allows you to use features like variables, nesting, mixins, and functions to write more organized, maintainable, and efficient stylesheets.
- **Tailwind CSS**
  - Next.js support Tailwind CSS to style your apps. Tailwind CSS is a utility-first CSS framework that provides a set of pre-defined CSS classes that you can use to style your HTML elements directly in your markup.

### 3.3 Composition
- **Images**
  - images account for a huge portion of the typical website’s page weight and can have a sizable impact on your website's LCP performance. The Next.js Image component extends the HTML element with features for automatic image optimization, including:
- **Videos**
  - Next.js provides various approaches and techniques to store and display video files without affecting performance. Videos can be embedded on the page using the HTML <video> tag for direct video files and <iframe> for external platform-hosted videos.
- **Fonts**
  - The next/font module automatically optimizes your fonts and removes external network requests for improved privacy and performance. It includes built-in self-hosting for any font file.
- **Metadata**
  - The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:
- **Package Bundling**
  - Bundling external packages can significantly improve the performance of your application. By default, packages imported inside Server Components and Route Handlers are automatically bundled by Next.js for enhanced optimization.

### 3.4 Setting things Up
- **CSS in JS**
  - It's possible to use any existing CSS-in-JS solution in your existing Next.js Apps and Pages. CSS-in-JS is a technique where CSS styles are written in JavaScript files instead of separate CSS files.
- **TypeScript**
  - TypeScript is a syntactic superset of JavaScript which adds static typing. This means that TypeScript adds syntax on top of JavaScript, allowing developers to add types.
- **Prettier**
  - Prettier is an opinionated code formatter that supports many languages, including JavaScript, TypeScript, and CSS. It automatically formats your code to adhere to a consistent style, ensuring readability and maintainability across your project.
- **ESLint**
  - ESLint is an open-source static code analysis tool for JavaScript that identifies problematic patterns and style issues in your code, helping to enforce coding standards and prevent bugs before they occur

### 3.5 Environment Variables
- **Environment Variables**
  - Environment variables are dynamic values that can affect the behavior of programs on a computer. They are typically used to store configuration settings, API keys, and other sensitive information that should not be hardcoded directly into the application's source code.

### 3.6 Markdown and MDX
- **Markdown and MDX**
  - Markdown is a lightweight markup language used to format text. It allows you to write using plain text syntax and convert it to structurally valid HTML.

### 3.7 Custom Server
- **Custom Server**
  - Next.js includes its own server with next start by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server).

### 3.8 Preparing for Production
- **Scripts**
  - Third-party scripts are code snippets from external sources that add functionality to your website, such as analytics, advertising, or social media widgets. Next.js allows you to load a third-party script for multiple routes through the next/script component, optimizing performance and enhancing control over when and how scripts are executed within your application.
- **Lazy Loading**
  - Lazy loading in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route. It allows you to defer loading of Client Components and imported libraries, and only include them in the client bundle when they're needed.
- **Analytics**
  - Next.js has built-in support for measuring and reporting performance metrics. You can either use the useReportWebVitals hook to manage reporting yourself, or alternatively, Vercel provides a managed service to automatically collect and visualize metrics for you.
- **Instrumentation**
  - Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.
- **OpenTelemetry**
  - Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app. With observability, developers can proactively address issues before they become major problems and provide a better user experience.
- **Static Assets**
  - Static content is any file that is stored in a server and is the same every time it is delivered to users. HTML files and images are examples of this kind of content.
- **Third Party Libraries**
  - @next/third-parties is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries, like Google Tag Manager and Google Analytics, in your Next.js application. All third-party integrations provided by @next/third-parties have been optimized for performance and ease of use.
- **Memory Usage**
  - As applications grow and become more feature rich, they can demand more resources when developing locally or creating production builds. Next.js provides several strategies and techniques to optimize memory and address common memory issues in Next.js.

### 3.9 Deployment Options
- **Vitest**
  - Next.js allows you to use Vitest for unit testing. Vitest is a fast unit test framework powered by Vite.
- **Jest**
  - Next.js allows you to use Jest for unit testing and snapshot testing. Jest is a JavaScript testing framework created by Facebook, designed for ensuring the correctness of JavaScript code, especially React applications.
- **Playwright**
  - Next.js supports Playwright for End-to-End (E2E) testing. Playwright is a testing framework that lets you automate Chromium, Firefox, and WebKit with a single API.
- **Cypress**
  - Next.js supports Cypress for End-to-End (E2E) and Component Testing. With Cypress, you can easily create tests for your modern web applications, debug them visually, and automatically run them in your continuous integration builds.
- **Node.js Server**
  - Next.js can be deployed to any provider that supports Node.js. You just have to build your application and start a Node.js server using simple commands.
- **Docker Container**
  - Next.js can be deployed to any provider that supports Docker containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker.
- **Static Export**
  - Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server. Since Next.js supports static exports, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.
- **Adapters**
  - Next.js can be adapted to run on different platforms to support their infrastructure capabilities, including AWS Amplify Hosting, Cloudflare, Deno Deploy, Netlify, and Vercel.

---

## 4. Optional / Specialized Topics

- Tailwind CSS
- Package Bundling
- OpenTelemetry
- Static Assets
- Third Party Libraries
- Memory Usage
- Node.js Server
- Docker Container
- Static Export
- Adapters

---

## 5. References

- [Next.js Roadmap](https://roadmap.sh/nextjs)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Fullstack Developer

### Related Skills
- React
- TypeScript
- JavaScript
- Node.js