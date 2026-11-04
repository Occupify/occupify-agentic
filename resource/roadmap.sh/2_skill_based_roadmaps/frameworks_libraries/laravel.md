# Laravel

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/laravel
- Related Roles:
  - Backend Developer
  - Fullstack Developer
  - Software Architect

---

## 1. Beginner

### 1.1 Installing Laravel
- **Laravel Herd**
  - Laravel Herd is a fast, native Laravel and PHP development environment for macOS. It eliminates the need for Docker or virtual machines, offering a streamlined experience for setting up and running Laravel projects.

### 1.2 What is Laravel?
- **Why Web Frameworks?**
  - Web frameworks provide a structured way to develop web applications by offering pre-built components, tools, and conventions. They streamline common tasks like routing, templating, database interaction, and security, allowing developers to focus on the unique features of their application rather than reinventing the wheel for basic functionalities.
- **Laravel for Full Stack**
  - Full-stack development involves building both the front-end (what users see and interact with) and the back-end (the server-side logic, database interactions, and APIs) of a web application. Laravel, primarily a back-end framework, can be effectively used in full-stack development by pairing it with front-end technologies like Vue.js, React, or even Blade templates to create complete web applications.
- **Laravel for Frontend**
  - Laravel, primarily known as a backend framework, can also be effectively utilized for building the frontend of web applications. While Laravel excels at handling server-side logic, routing, database interactions, and APIs, it offers features like Blade templating engine and asset management tools that allow developers to create dynamic and interactive user interfaces directly within the Laravel environment.

### 1.3 Create a new project
- **Create a new project**
  - To start a new Laravel project, you'll typically use Composer, a dependency management tool for PHP. Open your terminal or command prompt, navigate to the directory where you want to create your project, and then run the command composer create-project laravel/laravel your-project-name.

### 1.4 Starter Kits
- **Breeze**
  - Breeze is a minimal, simple implementation of all of Laravel's authentication features, including login, registration, password reset, email verification, and password confirmation. It provides a basic starting point for building a new Laravel application with authentication already configured, allowing developers to quickly scaffold the user authentication system and focus on building the core features of their application.
- **Livewire**
  - Livewire starter kits in Laravel provide a pre-configured foundation for building dynamic, reactive user interfaces using Livewire components. These kits typically include basic layouts, authentication scaffolding, and often pre-built components that demonstrate Livewire's capabilities, allowing developers to quickly begin building interactive features without setting up the underlying infrastructure from scratch.
- **Jetstream**
  - Jetstream is a scaffolding package for Laravel applications. It provides a robust starting point for your next Laravel project, featuring key functionalities such as user registration, login, email verification, two-factor authentication, session management, API support via Laravel Sanctum, and team management.
- **Inertia**
  - Inertia.js allows you to build single-page applications (SPAs) using server-side routing and controllers. Instead of building an API and a separate frontend, Inertia lets you use your existing server-side framework (like Laravel) for both.

### 1.5 Request–Response Flow
- **App**
  - The app directory in a Laravel project houses the core logic of your application. It contains the code that defines your application's behavior, including models, controllers, middleware, services, and other custom classes.
- **Resources**
  - The resources directory in a Laravel project is where you store your application's raw, uncompiled assets. This includes things like your views (HTML templates), language files, CSS, JavaScript, and images.
- **Bootstrap**
  - Bootstrap in a Laravel project is the initial point where the framework starts its execution process. It involves setting up the environment, loading configurations, registering service providers, and handling exceptions.
- **Config**
  - Configuration files in Laravel allow you to manage settings for your application in a centralized and organized manner. These files store key-value pairs that define various aspects of your application's behavior, such as database connections, mail settings, and application-specific parameters.
- **Database**
  - The database directory in a Laravel project houses all files related to your application's database interactions. This includes migrations, which define the structure of your database tables; seeders, which populate your database with initial data; factories, which generate fake data for testing; and any custom database-related logic you might implement.

### 1.6 Basic Routes
- **Basic Routes**
  - Routing in Laravel determines how your application responds to client requests. It essentially maps URLs (like /about or /contact) to specific functions or controllers within your application.

### 1.7 View Routes
- **View Routes**
  - View routes provide a simple way to return a view directly from a route without needing a full controller. Instead of defining a controller method to load and return a view, you can use the Route::view method.

### 1.8 Redirect Routes
- **Route model binding**
  - Route model binding is a way to automatically inject model instances into your route handlers based on the route parameters. Instead of manually querying the database for a model within your controller method using the ID passed in the route, Laravel can automatically resolve the model instance for you, making your code cleaner and more readable.

### 1.9 Route parameters
- **Rate limiting**
  - Rate limiting is a technique used to control the number of requests a user or client can make to a server within a specific time period. This helps to prevent abuse, protect resources, and maintain the stability and performance of an application by preventing it from being overwhelmed by excessive requests.

### 1.10 Named routes
- **Caching**
  - Route caching in Laravel involves storing the compiled routes in a cache file to significantly reduce the time it takes to register all of your application's routes on each request. Instead of re-parsing route definitions every time, Laravel can quickly load the routes from the cached file, leading to improved application performance, especially in larger applications with many routes.

### 1.11 Route groups
- **Route groups**
  - Route groups provide a way to share route attributes, such as middleware, namespaces, prefixes, and subdomain restrictions, across a large number of routes without needing to define them individually for each route. This allows for cleaner and more organized route definitions, reducing redundancy and improving maintainability.

### 1.12 Basic controllers
- **Routes**
  - The routes directory in Laravel houses all the route definitions for your application. These files tell Laravel how to respond to different HTTP requests (like GET, POST, PUT, DELETE) for specific URLs.
- **Storage**
  - The storage directory in Laravel is where the framework stores files generated during the application's runtime. This includes compiled Blade templates, file-based sessions, cache files, and logs.
- **Tests**
  - The tests directory in Laravel projects houses all the automated tests for your application. These tests are designed to verify that your code functions as expected, covering various aspects like models, controllers, routes, and features.
- **Public**
  - The public directory serves as the document root for your Laravel application. It's the only directory that should be directly accessible from the web.
- **Vendor**
  - The vendor directory in a Laravel project houses all the Composer-installed dependencies. These dependencies are third-party packages and libraries that your project relies on for various functionalities, such as database interactions, authentication, or templating.

### 1.13 Resource controllers
- **Resource controllers**
  - Resource controllers provide a standardized way to manage CRUD (Create, Read, Update, Delete) operations for a specific model. They group related request handling logic into a single class, making your code more organized and easier to maintain by mapping conventional HTTP verbs (like GET, POST, PUT, DELETE) to specific controller methods.

---

## 2. Intermediate

### 2.1 Single-action controllers
- **Single-action controllers**
  - Single-action controllers are controllers that contain only one method, typically named invoke. This approach simplifies controller logic when a controller is responsible for performing a single, specific task.

### 2.2 Middleware
- **Global vs Route**
  - Global middleware runs on every HTTP request entering your application. Route middleware, on the other hand, is only applied to specific routes or groups of routes that you define.
- **CORS**
  - Cross-Origin Resource Sharing (CORS) is a browser security feature that restricts web pages from making requests to a different domain than the one that served the web page. This policy prevents malicious websites from accessing sensitive data from other sites.

### 2.3 Dependency injection
- **CRUD Operations**
  - CRUD operations stand for Create, Read, Update, and Delete. These are the four basic functions of persistent storage, and they represent the fundamental operations performed on data within a database.
- **Relationships**
  - Eloquent relationships define how different database tables are connected. They allow you to easily retrieve related data from multiple tables using intuitive methods.

### 2.4 Blade Templating
- **Blade Templating**
  - Blade is a simple yet powerful templating engine provided with Laravel. It allows you to use plain PHP in your views, but also offers convenient shortcuts and directives for common tasks like displaying data, looping through arrays, and conditional statements.

### 2.5 Displaying data
- **Displaying data**
  - Displaying data in Laravel views involves passing information from your application's logic (controllers) to the view templates, which are then rendered into HTML and presented to the user. This process allows you to dynamically generate web pages with content that changes based on user input, database records, or other application data.

### 2.6 Blade Directives
- **if, else**
  - Conditional statements, like if and else, allow you to control the rendering of content in your Blade templates based on certain conditions. This means you can display different parts of your view depending on whether a variable is true, a user is logged in, or any other logical expression you define.
- **loops**
  - Blade directives offer a concise way to work with loops directly within your Laravel views. Instead of using standard PHP loop syntax, Blade provides directives like @for, @foreach, @while, and @forelse to iterate over data and display it in your templates.

### 2.7 Components
- **Components**
  - Components are reusable pieces of code that encapsulate HTML, CSS, and logic to create modular and maintainable user interface elements. They allow developers to define custom HTML tags that can be used throughout their application's views, promoting code reuse and consistency.

### 2.8 Eloquent ORM
- **Casts, Accessors**
  - Eloquent models in Laravel provide a way to interact with your database tables in an object-oriented manner. Casts allow you to modify the data type of an attribute when it's retrieved from or stored in the database.
- **Query scopes**
  - Query scopes in Eloquent provide a way to add constraints to all queries of a given model. They allow you to define common sets of query conditions as reusable methods within your Eloquent models.

### 2.9 Layouts
- **Layouts**
  - Layouts provide a consistent structure for your application's pages. They define the common elements like headers, footers, sidebars, and overall page structure, allowing you to avoid repeating the same HTML code across multiple views.

### 2.10 Blade + Livewire
- **Blade + Livewire**
  - Blade is Laravel's templating engine, allowing developers to use simple syntax to create dynamic web pages. Livewire is a full-stack framework for Laravel that enables you to build dynamic interfaces using Laravel and PHP, without writing JavaScript.

### 2.11 Configuration
- **Configuration**
  - Laravel simplifies database interaction by allowing you to configure database connections within the .env file and the config/database.php file. The .env file stores sensitive information like database credentials, while config/database.php defines the available database connections and their default settings.

### 2.12 Query Builder
- **Query Builder**
  - The Query Builder provides a convenient, fluent interface for creating and running database queries. It allows you to interact with your database without writing raw SQL, offering a more readable and maintainable way to perform common database operations like selecting, inserting, updating, and deleting data.

### 2.13 Migrations, seeders
- **Migrations, seeders**
  - Database migrations are like version control for your database schema, allowing you to modify and share the database structure in a structured and organized way. Seeders, on the other hand, are used to populate your database with initial data, such as default user accounts or categories, making it easier to start working with your application.

### 2.14 Retrieving data & files
- **Retrieving data & files**
  - When a user interacts with a web application, they often send data to the server through forms or file uploads. Retrieving data involves accessing and using the information submitted by the user, such as form inputs or query parameters.

### 2.15 Pagination
- **Pagination**
  - Pagination is the process of dividing content into discrete pages, allowing users to navigate through large datasets in a manageable way. Instead of displaying all the data at once, which can be overwhelming and slow down performance, pagination presents the data in smaller, more digestible chunks, typically with navigation controls to move between pages.

### 2.16 Creating Responses
- **Views**
  - Laravel, beyond processing data and logic, can also present information to the user. One common way to do this is by sending a "view" as a response.
- **Redirects**
  - Redirects are a way to send a user from one URL to another. They are commonly used after a form submission to prevent resubmitting data, or to guide users to a different part of a website after an action has been completed.
- **Manual validation**
  - Manual validation in Laravel involves directly interacting with the validator class to validate data. Instead of relying on request objects or form requests, you create a validator instance, define the validation rules, and then check if the data passes these rules.
- **Error messages**
  - Error messages in validation are the feedback provided to users when the data they submit doesn't meet the defined validation rules. These messages inform users about the specific issues with their input, guiding them to correct the errors and successfully submit the form or data.
- **Forms**
  - Form validation is the process of ensuring that user-submitted data in a form meets specific criteria before it's processed or stored. This involves checking for required fields, verifying data types (like email or number), and ensuring data conforms to specific formats or constraints.
- **Streamed Responses**
  - Streamed responses allow you to send large files or data streams to the user's browser in chunks, rather than loading the entire content into memory at once. This is particularly useful for handling large downloads, video streaming, or any situation where you need to send data incrementally to avoid memory limitations and improve performance.

### 2.17 Authentication
- **Files**
  - File responses in Laravel provide a way to send files, such as images, PDFs, or documents, directly to the user's browser for download or display. This functionality allows you to serve files stored on your server's filesystem to users, enabling features like downloading reports, displaying images, or providing access to other file-based resources.
- **JSON**
  - JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. In Laravel, you can easily return JSON responses from your routes or controllers, allowing you to build APIs or provide data to JavaScript-based frontends.
- **Manual Authentication**
  - Manual authentication involves directly handling user login and logout processes within your application, giving you complete control over how users are identified and authorized. This approach requires you to manage user credentials, session management, and security measures yourself, rather than relying on built-in Laravel features or packages.
- **With Starter Kits**
  - Authentication is the process of verifying a user's identity. Laravel starter kits provide pre-built scaffolding for authentication features like registration, login, password reset, and email verification.

### 2.18 Authorization
- **Policies**
  - Authorization Policies provide a structured way to define authorization logic for your application. They allow you to encapsulate the rules that determine whether a user is authorized to perform a specific action on a given resource.
- **Gates**
  - Authorization gates provide a way to control access to specific resources or actions within your application. They are essentially closures that determine if a user is authorized to perform a given action.

---

## 3. Advanced

### 3.1 Encryption & Hashing
- **Encryption & Hashing**
  - Encryption and hashing are fundamental security techniques used to protect sensitive data. Encryption transforms data into an unreadable format using an algorithm and a key, making it unintelligible to unauthorized parties; decryption reverses this process to restore the original data.

### 3.2 Logging Basics
- **Logging Basics**
  - Logging is the process of recording events that occur during the execution of a software application. These events, often called logs, provide valuable insights into the application's behavior, helping developers track errors, monitor performance, and understand user activity.

### 3.3 Debugging basics
- **Handling Exceptions**
  - Exceptions are unexpected events that disrupt the normal flow of a program's execution. Handling exceptions involves anticipating these potential problems, catching them when they occur, and then gracefully responding to them, preventing the application from crashing and providing informative feedback to the user or logging the error for debugging.
- **HTTP Exceptions**
  - HTTP Exceptions are a specific type of exception used to represent HTTP error responses. They allow you to easily return standard HTTP error codes (like 404 Not Found or 500 Internal Server Error) along with a corresponding message and optional headers directly from your application logic.
- **Sanctum**
  - Sanctum is a lightweight authentication system primarily designed for single-page applications (SPAs), mobile applications, and simple APIs. It provides a straightforward method for authenticating users using API tokens, allowing them to access protected routes and resources.
- **Passport**
  - Passport is a full OAuth 2.0 server implementation for your Laravel application, providing a secure and standardized way to authenticate users and grant access to your API. It allows users to authorize third-party applications to access their data without sharing their credentials, using tokens to represent authorization.
- **Telescope**
  - Telescope is an elegant debug assistant for the Laravel framework. It provides insights into the requests coming into your application, exceptions, log entries, database queries, queued jobs, mail, notifications, cache operations, scheduled tasks, variable dumps, and more.
- **Debugbar**
  - Debugbar is a package that provides a convenient toolbar displayed in the browser, offering insights into your application's performance and debugging information. It allows you to inspect things like queries executed, views rendered, routes matched, and other useful data without having to dig through log files or use dd() statements extensively.
- **Message Customization**
  - Error message customization involves tailoring the default error messages displayed to users when validation or other exceptions occur. This allows developers to provide more user-friendly and contextually relevant feedback, improving the overall user experience by guiding them towards correcting errors more effectively.

### 3.4 Log Stacks & Messages
- **Log Stacks & Messages**
  - Log stacks allow you to send log messages to multiple handlers simultaneously. This provides flexibility in how you manage and store your application's logs, enabling you to route different types of messages to different destinations, such as files, databases, or external services.

### 3.5 Unit & Feature tests
- **Configuration**
  - Deployment configuration involves setting up the necessary environment variables and settings for your Laravel application to run correctly in a production environment. This includes configuring database connections, cache settings, session drivers, and other environment-specific parameters to ensure optimal performance and security when the application is live.
- **Pest**
  - Pest is an elegant PHP testing framework with a focus on simplicity and developer experience. It provides a clean and expressive syntax for writing tests, aiming to make testing more enjoyable and efficient.
- **PHPUnit**
  - PHPUnit is a popular testing framework for PHP that allows developers to write and run automated tests for their code. It provides a structured way to define test cases, assertions, and test suites, ensuring that code behaves as expected.
- **Artisan**
  - Artisan is the command-line interface (CLI) included with Laravel. It provides a number of helpful commands that can assist you while building your application.
- **Sail**
  - Sail is a light-weight command-line interface (CLI) for interacting with Laravel's default Docker development environment. It provides a simple way to manage and run your Laravel application using Docker, without requiring prior Docker experience.
- **Octane**
  - Octane supercharges your Laravel application's performance by serving it using high-powered application servers like Swoole or RoadRunner. Instead of creating a fresh application instance for each request, Octane keeps the application loaded in memory, significantly reducing boot times and overhead.
- **Pint**
  - Pint is an opinionated PHP code style fixer. It automatically corrects coding style issues in your PHP code, ensuring consistency and adherence to defined coding standards.

### 3.6 Queues & Jobs
- **Queues & Jobs**
  - Queues and jobs provide a mechanism to defer the processing of time-consuming tasks, such as sending emails, processing large datasets, or performing complex calculations, to a later time. Instead of executing these tasks immediately within a web request, they are pushed onto a queue.

### 3.7 Events & Listeners
- **Events & Listeners**
  - Events and listeners provide a simple observer pattern implementation, allowing you to subscribe to and react to events that occur in your application. An event signifies that something has happened, while listeners are classes that execute specific actions in response to those events.

### 3.8 Notifications
- **Optimization**
  - Optimization, in the context of deployment, refers to the process of refining and improving a deployed application's performance, efficiency, and resource utilization. This involves identifying bottlenecks, reducing resource consumption (like memory and CPU), and enhancing the overall speed and responsiveness of the application to ensure a smooth and scalable user experience in a production environment.

### 3.9 Task Schedulling
- **Health Route**
  - A health route is a specific endpoint in an application that provides information about its operational status. It's designed to be easily accessible and quickly indicate whether the application is running correctly and its dependencies are healthy.

### 3.10 File Storage
- **File Storage**
  - File storage provides a convenient way to store and retrieve files, whether they are stored locally on the server or in cloud storage services like Amazon S3 or Google Cloud Storage. It offers a unified API for working with different storage systems, allowing you to easily switch between them without modifying your application's code.

### 3.11 Localization
- **Laravel Cloud**
  - Laravel Cloud provides a streamlined platform for deploying and managing Laravel applications. It simplifies the process of setting up servers, configuring databases, and handling deployments, allowing developers to focus on building features rather than managing infrastructure.

### 3.12 Facades
- **Laravel Forge**
  - Laravel Forge is a web-based platform designed to simplify the deployment and management of PHP applications, particularly those built with Laravel. It automates server provisioning, configuration, and deployment processes, allowing developers to focus on writing code rather than managing infrastructure.

### 3.13 Package Management
- **Pulse**
  - Pulse is a real-time monitoring tool designed to provide insights into your application's performance and health. It collects and displays key metrics like slow queries, cache interactions, queue jobs, and server resource usage, allowing developers to quickly identify and address potential bottlenecks or issues.

---

## 4. Optional / Specialized Topics

- Database
- Vendor
- Forms
- Streamed Responses
- Telescope
- Debugbar
- Message Customization
- Sail
- Octane
- Pint

---

## 5. References

- [Laravel Roadmap](https://roadmap.sh/laravel)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer
- Software Architect

### Related Skills
- Php
- System Design