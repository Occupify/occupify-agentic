# Node.js

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/nodejs
- Related Roles:
  - Backend Developer
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction to Node.js
- **What is Node.js?**
  - Node.js is a cross-platform, open-source JavaScript runtime that executes code outside of a browser. It was created by Ryan Dahl in 2009 to allow JavaScript to be used for server-side scripting.
- **Why use Node.js?**
  - Node.js is a good choice when you need high-throughput, real-time applications like chat servers, APIs, or streaming services. Its non-blocking architecture means it can handle many concurrent connections without spawning a new thread for each one.
- **History of Node.js**
  - Node.js was first released in 2009 by Ryan Dahl, who wanted a way to build scalable network applications using JavaScript. The project was eventually forked in 2014 to create io.js, which was later merged back in 2015 under the Node.js Foundation.
- **Node.js vs Browser**
  - Node.js and the browser both run JavaScript but in different environments with different APIs. The browser provides access to the DOM, window, and browser-specific APIs, while Node.js provides access to the file system, operating system, and network.
- **Running Node.js Code**
  - You can run Node.js code from the terminal using the node command followed by a filename. For quick experiments, Node.js also includes a REPL (Read-Eval-Print Loop) that lets you execute JavaScript interactively.

### 1.2 Modules
- **CommonJS**
  - CommonJS and ES (EcmaScript) are module systems used in Node. CommonJS is the default module system.
- **ESM**
  - ESM (ECMAScript Modules) is a standardized module system in JavaScript that allows for the organized, maintainable, and reusable structuring of code. It uses import and export statements for including and sharing functions, objects, or primitives between files.
- **Creating & Importing**
  - Creating a module means writing JavaScript in a file and exporting the parts you want to share. Importing means pulling those exports into another file using require() in CommonJS or import in ESM.

### 1.3 npm
- **Global Installation**
  - A global npm installation places a package in a system-wide location, making it available as a command-line tool from any directory. You use it for tools you want to run across multiple projects, like CLI utilities.
- **Local Installation**
  - Locally installed packages are available only to the project where the packages are installed, while the globally installed packages can be used any where without installing them into a project. Another use case of the global packages is when using CLI tools.
- **Updating Packages**
  - npm provides various features to help install and maintain the project's dependencies. Dependencies get updates with new features and fixes, so upgrading to a newer version is recommended.
- **Running Scripts**
  - In Node.js, npm scripts are used for the purpose of initiating a server, starting the build of a project, and also for running the tests. We can define this scripts in the package.json file of the folder.
- **Semantic Versioning**
  - Semantic versioning (SemVer) is a versioning convention used by npm packages. Version numbers follow the format MAJOR.MINOR.PATCH, where breaking changes increment the major number, new features increment the minor, and bug fixes increment the patch.
- **npx**
  - npx is a tool that comes with npm and lets you run Node.js packages without installing them globally. It downloads and executes the package in a temporary environment, which is useful for running CLI tools like scaffolding scripts or code generators.
- **Promises**
  - A promise is an object representing the eventual result of an async operation. It can be in one of three states: pending, fulfilled, or rejected.

### 1.4 Error Handling
- **[global] keyword**
  - In browsers, the top-level scope is the global scope, and its global object is called the window object. Within the browser, var something will define a new global variable inside the window object.
- **System Errors**
  - System errors occur when Node.js interacts with the underlying operating system and the operation fails. Examples include trying to read a file that does not exist or a network connection being refused.
- **User Specified Errors**
  - User specified errors can be created by extending the base Error object, a built-in error class. When creating errors in this manner, you should pass a message string that describes the error.

### 1.5 Async Programming
- **npm workspaces**
  - npm workspaces allow you to manage multiple packages within a single repository (monorepo). You define workspace packages in the root package.json, and npm handles linking them together during installation.
- **Creating Packages**
  - npm packages allow you to bundle some specific functionality into a reusable package which can then be uploaded to some package registry such as npm or GitHub packages and then be installed and reused in projects using npm.
- **JavaScript Errors**
  - JavaScript errors are runtime errors thrown by the language itself, such as TypeError, RangeError, and ReferenceError. These occur when code tries to perform an invalid operation, like calling a method on undefined.
- **Assertion Errors**
  - An AssertionError in Node.js is an error that is thrown when the assert module determines that a given expression is not truthy. The assert module is a built-in Node.js module that provides a simple set of assertion tests that can be used to test the behavior of your code.
- **Uncaught Exceptions**
  - An uncaught exception is an error that is not handled anywhere in the application, causing the Node.js process to crash. You can listen for these with the process.on('uncaughtException', ...) event, though it should be used carefully and mainly for logging before shutting down gracefully.
- **Handling Async Errors**
  - Errors must always be handled. If you are using synchronous programming you could use a try catch.
- **Callstack / Stack Trace**
  - The stack trace is used to trace the active stack frames at a particular instance during the execution of a program. The stack trace is useful while debugging code as it shows the exact point that has caused an error.
- **async/await**
  - Async/Await is a special syntax to work with promises in a more comfortable fashion. It's easy to understand and use.
- **Callbacks**
  - Node.js, being an asynchronous platform, doesn't wait around for things like file I/O to finish - Node.js uses callbacks. A callback is a function called at the completion of a given task; this prevents any blocking, and allows other code to be run in the meantime.
- **setTimeout**
  - setTimeout() executes a callback function once, after a specified delay in milliseconds. It does not block other code from running while waiting.
- **setInterval**
  - setInterval() repeatedly executes a callback function at a fixed time interval, in milliseconds. It keeps running until cleared with clearInterval().
- **setImmediate**
  - setImmediate() schedules a callback to run in the check phase of the event loop, after I/O events have been processed. It is similar to setTimeout(fn, 0) but is guaranteed to run before any timers in some cases.
- **Event Emitter**
  - In Node.js, an event can be described simply as a string with a corresponding callback. An event can be "emitted" (or, in other words, the corresponding callback be called) multiple times or you can choose to only listen for the first time it is emitted.
- **Event Loop**
  - The Event Loop is one of the most critical aspects of Node.js. Why is this so important?

---

## 2. Intermediate

### 2.1 Working with Files
- **Using Debugger**
  - Node.js includes a built-in debugger that can be activated with the --inspect flag or the debugger keyword in code. It lets you pause execution, step through code, and inspect variables at runtime using Chrome DevTools or a compatible IDE.
- **process.cwd()**
  - process.cwd() returns the current working directory of the Node.js process, which is the directory from which the script was launched. Unlike dirname, it reflects the shell's working directory, not the file's location.
- **path module**
  - The path module provides utilities for working with file and directory paths. It's built-in to Node.js core and can simply be used by requiring it.
- **fs module**
  - File System or fs module is a built in module in Node that enables interacting with the file system using JavaScript. All file system operations have synchronous, callback, and promise-based forms, and are accessible using both CommonJS syntax and ES6 Modules.
- **__dirname**
  - The dirname in a node script returns the path of the folder where the current JavaScript file resides. filename and dirname are used to get the filename and directory name of the currently executing file.
- **__filename**
  - The filename in Node.js returns the filename of the executed code. It gives the absolute path of the code file.
- **glob**
  - glob is an npm package for matching files using shell-style wildcard patterns. For example, /.js matches all JavaScript files in all subdirectories.
- **globby**
  - globby is a modern alternative to glob that supports promises and multiple patterns at once. It builds on top of fast-glob and provides a cleaner API.
- **fs-extra**
  - fs-extra adds file system methods that aren't included in the native fs module and adds promise support to the fs methods. It also uses graceful-fs to prevent EMFILE errors.
- **chokidar**
  - Chokidar is an npm package for watching file system changes. It wraps Node.js's native fs.watch and fs.watchFile with a more reliable and consistent API.
- **http module**
  - The http module is Node.js's built-in module for creating HTTP servers and making HTTP requests. It provides low-level access to the HTTP protocol, giving you full control over request and response handling.
- **jsonwebtoken**
  - JWT, or JSON-Web-Token, is an open standard for sharing security information between two parties — a client and a server. Each JWT contains encoded JSON objects, including a set of claims.
- **passport.js**
  - Passport.js is authentication middleware for Node.js. It makes implementing authentication in express apps really easy and fast.

### 2.2 Command Line Apps
- **process.nextTick**
  - Every time the event loop takes a full trip, we call it a tick. When we pass a function to process.nextTick(), we instruct the engine to invoke this function at the end of the current operation before the next event loop tick starts.
- **dotenv package**
  - dotenv is an npm package that loads environment variables from a .env file into process.env. It is commonly used in development to manage configuration like API keys and database URLs without hardcoding them in source code.
- **process.env**
  - process.env is a Node.js object that contains all environment variables available to the current process. These can be set in the shell, in a .env file via a library like dotenv, or by the deployment platform.
- **Exitting / Exit Codes**
  - When a Node.js process finishes, it exits with a numeric exit code that signals whether it succeeded or failed. An exit code of 0 means success; any non-zero code indicates an error.
- **process.stdin**
  - process.stdin is a stream in Node.js that represents the standard input, typically the keyboard. It allows your Node.js programs to receive text input from the command line.
- **prompts package**
  - prompts is a lightweight npm package for building interactive command-line interfaces. It provides a simple API for prompting users with questions and collecting their answers in various formats, like text input, confirmations, and selections.
- **Inquirer Package**
  - Inquirer.js is a popular npm package for building rich, interactive command-line interfaces. It supports many input types including text, passwords, lists, checkboxes, and confirmations.
- **stdout / stderr**
  - The process.stdout property is an inbuilt application programming interface of the process module which is used to send data out of our program. A Writable Stream to stdout.

### 2.3 Building & Consuming APIs
- **chalk package**
  - chalk is an npm package for styling terminal output with colors and formatting like bold, underline, and italic. It is used to make CLI output more readable by highlighting errors in red, success messages in green, and so on.
- **figlet package**
  - figlet is an npm package that renders text as ASCII art using large, decorative fonts. It is typically used in CLI tools to display a stylized application name or welcome message at startup.
- **cli-progress**
  - cli-progress is an npm package for displaying progress bars in the terminal. It is useful for long-running operations like file downloads, database migrations, or batch processing where you want to show completion percentage.
- **Express.js**
  - Express.js is the most widely used Node.js web framework. It provides a minimal set of features for routing HTTP requests and adding middleware.
- **fastify**
  - Fastify is a high-performance web framework for Node.js. It is designed to have low overhead and high throughput, making it one of the fastest Node.js HTTP frameworks available.

### 2.4 Monitor Changes (Dev)
- **process.argv**
  - process.argv is an array containing the command-line arguments passed to the Node.js process. The first two elements are the path to Node.js and the script file; the remaining elements are the arguments provided by the user.
- **commander**
  - Commander is a light-weight, expressive, and powerful command-line framework for node.js. with Commander.js you can create your own command-line interface (CLI).
- **--watch**
  - The --watch flag in Node.js is a powerful feature introduced in Node.js version 19 that enables automatic reloading of your Node.js application whenever changes are detected in the specified files.
- **nodemon**
  - In Node.js, you need to restart the process to make changes take effect. This adds an extra step to your workflow.

### 2.5 Template Engines
- **ejs**
  - EJS is a template language or engine that allows you to generate HTML markup with pure JavaScript. And this is what makes it perfect for Nodejs applications.
- **pug**
  - Pug is a JavaScript template engine. It is a high-performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers.
- **marko**
  - Marko is a fast and lightweight HTML-based templating engine that compiles templates to CommonJS modules and supports streaming, async rendering, and custom tags. It is HTML re-imagined as a language for building dynamic and reactive user interfaces.
- **Mongoose**
  - Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. Mongoose provides a straight-forward, schema-based solution to model your application data.

### 2.6 Working with Databases
- **Prisma**
  - Prisma provides an open source next-generation ORM in the TypeScript ecosystem. It offers a dedicated API for relation filters.
- **Native Drivers**
  - Native database drivers are npm packages provided by database vendors that let Node.js communicate directly with a NoSQL database. For example, the official MongoDB driver connects to MongoDB and lets you run queries against it.

### 2.7 Testing
- **NestJS**
  - NestJS is a framework for building server-side Node.js applications. It uses TypeScript by default and draws heavily from Angular's architecture, using decorators, modules, and dependency injection.
- **Hono**
  - Hono is a lightweight, simple, and fast web framework for Cloudflare Workers, Deno, Bun, and other applications. It is a modern web application that is both fast and flexible.
- **axios**
  - Axios is a promise-based HTTP Client for node.js and the browser. Used for making requests to web servers.
- **ky**
  - Ky is a tiny and elegant HTTP client based on the browser Fetch API. Ky targets modern browsers and Deno.For older browsers, you will need to transpile and use a fetch polyfill.For Node.js, check out Got..
- **fetch**
  - The fetch() method in JavaScript is used to request to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON or XML.
- **got package**
  - Got is a lighter, human-friendly, and powerful HTTP request library explicitly designed to work with Node.js. It supports pagination, RFC compliant caching, makes an API request again if it fails, supports cookies out of the box, etc.
- **Vitest**
  - Vitest is a Vite-native unit testing framework that's Jest-compatible. Vitest is a powerful testing library built on top of Vite that is growing in popularity.
- **node:test**
  - node:test is Node.js's built-in test runner, added in version 18. It provides a simple API for writing and running tests without any additional dependencies.
- **Jest**
  - Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It works with projects using: Babel, TypeScript, Node, React, Angular, Vue and more!
- **Playwright**
  - Playwright is a browser automation and end-to-end testing tool developed by Microsoft. It supports multiple browsers (Chromium, Firefox, WebKit) and allows you to write tests that simulate real user behavior.
- **Cypress**
  - Cypress is an end-to-end testing framework designed for web applications. It runs tests directly in the browser and provides a visual test runner for debugging.

---

## 3. Advanced

### 3.1 Logging
- **Winston**
  - winston is designed to be a simple and universal logging library with support for multiple transports. A transport is essentially a storage device for your logs.
- **Morgan**
  - Morgan is a NodeJS and express.js middleware to log the HTTP request and error, simplifying the debugging process. It provides flexibility in defining the format of log messages and helps override the output destination for your logs.

### 3.2 Keep app Running
- **Knex**
  - Knex.js is a "batteries included" SQL query builder for PostgreSQL, CockroachDB, MSSQL, MySQL, MariaDB, SQLite3, Better-SQLite3, Oracle, and Amazon Redshift designed to be flexible, portable, and fun to use.
- **Drizzle**
  - Drizzle lets you build your project the way you want, without interfering with your project or structure. Using Drizzle you can define and manage database schemas in TypeScript, access your data in a SQL-like or relational way, and take advantage of opt-in tools to make your developer experience amazing.
- **TypeORM**
  - TypeORM is an ORM that can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large scale enterprise applications with multiple databases.
- **pm2**
  - PM2 is a production process manager for Node.js applications with a built-in load balancer. It allows you to keep applications alive forever, to reload them without downtime and to facilitate common system admin tasks.

### 3.3 Threads
- **Sequelize**
  - Sequelize is a mature ORM for Node.js that supports PostgreSQL, MySQL, MariaDB, SQLite, and MSSQL. It provides model definitions, associations, query building, and migration support.
- **Prisma**
  - Prisma is an ORM that helps app developers build faster and make fewer errors. Combined with its Data Platform developers gain reliability and visibility when working with databases.
- **Native Drivers**
  - Native drivers for relational databases let Node.js connect to databases like PostgreSQL or MySQL directly. Examples include the pg package for PostgreSQL and mysql2 for MySQL.
- **Child Process**
  - The child\process module gives the node the ability to run the child process, established through IPC (inter-process communication) by accessing operating system commands. The three main methods inside this module are : childprocess.spawn() childprocess.fork() childprocess.exec()
- **Cluster**
  - The Cluster module allows you to easily create child processes that each runs simultaneously on their own single thread, to handle workloads among their application threads.
- **Worker Threads**
  - Worker thread is a continuous parallel thread that runs and accepts messages until it is explicitly closed or terminated. With worker threads, we can achieve a much efficient application without creating a deadlock situation.

### 3.4 Streams
- **Garbage Collection**
  - Memory management in JavaScript is performed automatically and invisibly to us. We create primitives, objects, functions… All that takes memory.

### 3.5 Debugging
- **Memory Leaks**
  - Memory leaks are caused when your Node.js app’s CPU and memory usage increases over time for no apparent reason. In simple terms, a Node.js memory leak is an orphan block of memory on the Heap that is no longer used by your app because it has not been released by the garbage collector.
- **node --inspect**
  - The --inspect flag starts the Node.js process with a debugging interface enabled. You can then connect to it using Chrome DevTools or a compatible IDE like VS Code to set breakpoints, step through code, and inspect variables.
- **Using APM**
  - APM (Application Performance Monitoring) tools provide real-time visibility into the performance of a Node.js application in production. They track metrics like response times, error rates, memory usage, and database query performance.

### 3.6 Common Built-in Modules
- **Common Built-in Modules**
  - These are the core modules that come with Node.js out of the box. This module provides tools or APIs for performing out certain standard Node.js operations.

---

## 4. Optional / Specialized Topics

- Running Node.js Code
- Semantic Versioning
- npx
- Promises
- Uncaught Exceptions
- Handling Async Errors
- Callstack / Stack Trace
- async/await
- Callbacks
- setTimeout
- setInterval
- setImmediate
- Event Emitter
- Event Loop
- __dirname
- __filename
- glob
- globby
- fs-extra
- chokidar
- http module
- jsonwebtoken
- passport.js
- process.stdin
- prompts package

---

## 5. References

- [Node.js Roadmap](https://roadmap.sh/nodejs)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Frontend Developer

### Related Skills
- JavaScript
- Docker
- TypeScript
- System Design