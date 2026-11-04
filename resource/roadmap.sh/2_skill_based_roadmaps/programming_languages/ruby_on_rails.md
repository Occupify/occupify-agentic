# Ruby on Rails

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ruby-on-rails
- Related Roles:
  - Backend Developer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Introduction
- **MVC architecture**
  - MVC, or Model-View-Controller, is a software design pattern commonly used for developing user interfaces that divides an application into three interconnected parts. The Model manages the application's data and logic, the View displays the data to the user, and the Controller handles user input and updates the Model and View accordingly.
- **Create an App**
  - Creating a new Rails application is the initial step in starting any Rails project. It involves using the rails new command, which sets up the basic directory structure, configuration files, and dependencies needed for a functional Rails application.
- **Rails Command Line**
  - The Rails command line interface (CLI), often accessed via the rails command, is a powerful tool for creating, managing, and interacting with Rails applications. It provides a suite of commands to generate code, run tests, manage databases, and perform various other development tasks, streamlining the development process and reducing boilerplate code.
- **How the web works**
  - The web operates through a client-server model where a client (like a web browser) sends a request to a server, and the server processes that request and sends back a response. This interaction typically involves HTTP (Hypertext Transfer Protocol) for communication, URLs (Uniform Resource Locators) to identify resources, and HTML (Hypertext Markup Language) to structure the content displayed in the browser.
- **Why Web Frameworks?**
  - Web frameworks provide a structured and efficient way to build web applications by offering pre-built components, tools, and conventions. They handle common tasks like routing, database interaction, and templating, allowing developers to focus on the unique features of their application rather than reinventing the wheel.
- **Rails & Frontend**
  - Rails, while primarily a backend framework, works seamlessly with various frontend technologies to build complete web applications. You can use Rails to handle the server-side logic, data management, and API endpoints, while employing frontend frameworks like React, Vue.js, or even Hotwire for the user interface and interactive elements.

### 1.2 Setting up Ruby on Rails
- **Rails Generators**
  - Rails Generators are powerful tools built into the Rails framework that automate the creation of files and directories needed for various parts of your application. They streamline development by providing pre-built templates for models, controllers, views, migrations, and more, reducing boilerplate code and ensuring consistency across your project.
- **Hotwire**
  - Hotwire is an alternative approach to building modern web applications by sending HTML over the wire, instead of complex JSON APIs. It allows you to build rich, dynamic user interfaces without writing large amounts of JavaScript.

### 1.3 Request Reponse Flow
- **app**
  - The app directory in a Rails application is the heart of your project, containing the core logic and components that define its behavior. It's where you'll find the code responsible for handling user requests, interacting with the database, and rendering views.
- **RESTful Routes**
  - RESTful routes provide a standardized way to map HTTP verbs (GET, POST, PUT, DELETE) to controller actions, representing Create, Read, Update, and Delete (CRUD) operations on resources. This convention promotes a clean and predictable URL structure, making applications easier to understand and maintain by aligning routes with the underlying data model.
- **Nested Routes**
  - Nested routes allow you to define hierarchical relationships between resources in your application's URLs. This means you can represent parent-child relationships, such as comments belonging to a specific post, directly in the URL structure.
- **bin**
  - The bin directory in a Rails application contains executable scripts that are specific to your application. These scripts are typically used for tasks like starting the server, running tests, or performing other administrative operations.
- **config**
  - The config directory in a Rails application houses configuration files that control various aspects of the application's behavior. These files define database connections, routing rules, environment-specific settings, and other application-wide configurations, allowing developers to customize the application without modifying the core code.
- **db**
  - The db directory in a Rails application houses everything related to your database. It contains files for database schema definition, migrations, and seed data.
- **Gemfile**
  - The Gemfile is a file in the root directory of a Ruby on Rails application that specifies the gem dependencies required for the project. It uses Ruby's syntax to list the gems and their versions, allowing Bundler to manage and install the correct versions of each gem.
- **public**
  - The public directory in a Ruby on Rails application serves as the root directory for all static assets that are directly accessible by web browsers. It holds files like HTML, CSS, JavaScript, images, and other media that don't require any processing or compilation by Rails before being served to the user.

### 1.4 Routing Fundamentals
- **Non-RESTful Routes**
  - Non-RESTful routes are custom routes that deviate from the standard RESTful conventions (like index, show, create, update, destroy). They are used when an action doesn't naturally map to a typical CRUD operation or when you need a more descriptive or specific URL for a particular function in your application.
- **Redirects**
  - Redirects in web applications are mechanisms to automatically forward a user from one URL to another. This is commonly used for various reasons, such as moving content to a new location, handling outdated URLs, or guiding users through a specific workflow.

### 1.5 Controllers
- **Controller Actions**
  - Controller actions are methods within a Rails controller that handle specific requests from users or other parts of the application. Each action typically corresponds to a specific route and performs a task, such as displaying a form, creating a new record, updating an existing record, or deleting a record.
- **(Strong) Parameters**
  - Controller parameters are the data sent from a client (like a web browser) to your Rails application, typically through forms or API requests. These parameters are accessible within your controller actions.
- **Controller Callbacks (filters)**
  - Controller callbacks, often referred to as filters, are methods that are executed at specific points in the lifecycle of a controller action. They allow you to run code before, after, or around a controller action, providing a way to encapsulate common logic, such as authentication, authorization, or data preparation, and keep your controller actions clean and focused.
- **Creating Controllers**
  - Controllers are the logical center of your application, responsible for receiving specific requests from the user, interacting with the model to retrieve or save data, and then rendering a view to present that data back to the user. Creating a controller involves defining a Ruby class that inherits from ApplicationController and defining methods (called actions) within that class to handle specific routes and user interactions.
- **Basic Queries**
  - Active Record provides a powerful and intuitive interface for interacting with databases in Rails applications. Basic queries allow you to retrieve data from your database tables using simple and expressive methods.
- **Cookies**
  - Cookies are small pieces of data that a server sends to a user's web browser. The browser may store it and send it back with later requests to the same server.
- **Sessions**
  - Beyond processing requests and rendering views, controllers also provide a mechanism for maintaining user sessions. Sessions allow you to store data related to a specific user across multiple requests, enabling features like login persistence, shopping carts, and personalized experiences.

### 1.6 Models
- **Model Relationships**
  - Model relationships in Rails define how different models in your application are connected to each other. These relationships allow you to easily access related data and maintain data integrity.
- **Validations**
  - Validations are rules that you define for your models to ensure that only valid data is saved into your database. They help maintain data integrity by checking if attributes meet specific criteria, such as presence, format, uniqueness, or custom conditions, before a record is created or updated.
- **Customizing Routes**
  - Customizing routes allows developers to define specific URL patterns and map them to particular controller actions. This provides flexibility in designing user-friendly and SEO-optimized URLs, deviating from the default Rails conventions.
- **Data Types**
  - Data types define the kind of information a database column can store. When creating Rails models, you specify data types for each attribute, which then translates into the corresponding column type in your database table.
- **Model Methods**
  - Model methods in Ruby on Rails are custom functions defined within a model class that encapsulate specific business logic related to that model. These methods allow you to perform operations on model instances or the model class itself, such as data validation, calculations, or interactions with other models, promoting code reusability and maintainability within your Rails application.
- **Inspecting Routes**
  - Rails comes with functionalities that allow developers to view all defined routes, their corresponding HTTP methods (GET, POST, PUT, DELETE, etc.), the controller and action they map to, and any route parameters. This is crucial for understanding how URLs are handled within the application and for debugging routing issues.
- **Constraints**
  - Routing constraints allow you to restrict which routes are matched based on specific criteria. These criteria can include the request's subdomain, IP address, HTTP headers, or any other attribute of the request.
- **Named Routes**
  - Named routes provide a convenient way to refer to specific routes within your application's code. Instead of hardcoding URLs, you can use a symbolic name that represents the route, making your code more readable and maintainable.
- **Creating Models**
  - Models in Ruby on Rails represent the data and business logic of your application. They are Ruby classes that inherit from ApplicationRecord and typically correspond to tables in your database.

### 1.7 Active Record
- **Callbacks**
  - Callbacks are methods that get called at certain moments in the lifecycle of an Active Record object. These moments can include creation, updating, deletion, validation, or saving.
- **Scopes**
  - Scopes in Rails models are pre-defined database queries that you can reuse throughout your application. They allow you to encapsulate common query logic, making your code cleaner, more readable, and easier to maintain.
- **Joins**
  - Joins in Active Record allow you to combine data from multiple database tables based on related columns. This is essential for retrieving information that spans across different tables, such as fetching a user's posts or a product's categories.
- **Aggregations**
  - Aggregations in Active Record allow you to derive summary information from your database records. This involves performing calculations like finding the average, minimum, maximum, or sum of values across a set of records, or counting the number of records that meet certain criteria.
- **Query Optimization**
  - Query optimization focuses on improving the efficiency of database queries to reduce execution time and resource consumption. This involves techniques like eager loading to minimize the number of queries, using indexes to speed up data retrieval, and writing efficient query conditions to filter data effectively.
- **Raw SQL**
  - Active Record typically provides an abstraction layer for database interactions, allowing you to work with objects and methods instead of writing SQL queries directly. However, sometimes you need more control or access to database-specific features.
- **Conditions**
  - Active Record conditions are used to specify criteria for retrieving data from a database table. They allow you to filter records based on specific attributes and values, enabling you to retrieve only the data that meets your desired requirements.
- **Ordering**
  - Ordering in Active Record allows you to specify the sequence in which records are retrieved from the database. This is achieved by using the order method, which accepts either a string representing the SQL order clause or a hash/symbol representing the attribute(s) to order by and their direction (ascending or descending).

---

## 2. Intermediate

### 2.1 Databases
- **Migrations**
  - Migrations are a way to evolve your database schema over time in a consistent and manageable way. They are Ruby files that define changes to your database structure, such as creating tables, adding columns, or modifying indexes.
- **Transactions**
  - Transactions are a sequence of operations performed as a single logical unit of work. They ensure data integrity by treating a series of database operations as an "all or nothing" proposition.
- **SQLite**
  - SQLite is a lightweight, file-based database engine. It requires no separate server process and stores the entire database in a single file on disk.
- **PostgreSQL**
  - PostgreSQL is an open-source, object-relational database system known for its reliability, feature robustness, and adherence to standards. It's a popular choice for Rails applications due to its advanced data types, support for complex queries, and strong community support.
- **MySQL**
  - MySQL is a popular open-source relational database management system (RDBMS). In a Ruby on Rails application, MySQL serves as a persistent data store for your application's information, such as user accounts, product details, and blog posts.
- **MariaDB**
  - MariaDB is an open-source relational database management system (RDBMS) that is a popular fork of MySQL. Rails applications can connect to and interact with MariaDB databases using the mysql2 adapter.

### 2.2 Action Views
- **Layouts & yield**
  - Layouts provide a consistent structure for your application's views. They are templates that define the overall look and feel of a page, including elements like headers, footers, and navigation.
- **ERB Templates**
  - ERB (Embedded Ruby) templates are a core component of Rails views, allowing you to embed Ruby code directly within your HTML markup. This enables dynamic content generation, where data from your Rails application can be seamlessly integrated into the presentation layer.
- **Rendering Views**
  - Rendering views in Ruby on Rails involves generating HTML (or other formats) to be displayed to the user. This process typically uses templates written in ERB or other templating languages, combining data from the controller with the template to produce the final output.
- **form_for**
  - formfor is a helper method in Ruby on Rails that simplifies the creation of HTML forms. It automatically generates the necessary HTML tags and attributes for creating forms that are bound to a specific model object.
- **form_with**
  - formwith is a helper method used to create HTML forms. It simplifies the process of generating the necessary HTML tags for form elements, handling attributes like the form's action URL, HTTP method (GET, POST, PUT, PATCH, DELETE), and CSRF protection.
- **Form Elements**
  - Form elements are the individual components within an HTML form that allow users to input data. These elements include text fields, text areas, checkboxes, radio buttons, select boxes, and buttons, each serving a specific purpose in collecting different types of user information.

### 2.3 Pagination
- **Partials**
  - Partials are reusable snippets of view code that can be rendered within other views. They help to keep your views organized and DRY (Don't Repeat Yourself) by extracting common UI elements or logic into separate files.
- **Helpers**
  - Helpers in Rails are methods that you can use in your views to encapsulate complex logic, format data, or generate HTML. They promote code reusability and keep your views clean and readable by moving presentation-related code out of the templates.
- **ViewComponent**
  - ViewComponent is a framework for building reusable, testable & encapsulated UI components in Ruby on Rails. It encourages a component-based architecture within your Rails application, allowing you to define UI elements as Ruby classes with associated templates, similar to components in frameworks like React or Vue.
- **Phlex**
  - Phlex is a Ruby library for building HTML views with a Ruby syntax. It offers a component-based approach, allowing developers to define reusable UI elements as Ruby classes.
- **Nested Forms**
  - Nested forms allow you to manage associated models directly within a parent form. This means you can create, update, and delete records of related models on the same page as the parent model, providing a more streamlined user experience.
- **Form Validation**
  - Form validation is the process of ensuring that the data submitted through a form meets specific requirements before it's saved to the database. This helps prevent errors, maintain data integrity, and provide a better user experience.
- **Kaminari**
  - Kaminari is a Ruby on Rails gem that simplifies the process of adding pagination to your application. It provides an easy-to-use interface for displaying large datasets in manageable chunks, improving performance and user experience by loading only the necessary data for each page.
- **Pagy**
  - Pagy is a gem in Ruby on Rails that simplifies the implementation of pagination in your web applications. It provides a fast and flexible way to divide large datasets into smaller, more manageable pages, improving user experience and server performance.

### 2.4 Caching
- **Caching**
  - Caching is a technique used to store copies of frequently accessed data in a temporary storage location, like memory, to reduce the need to retrieve the data from its source, such as a database or external API, every time it's requested. This results in faster response times and reduced load on the original data source.

### 2.5 Assets Pipeline
- **Advanced Asset Management**
  - You can use advanced asset management techniques to optimize and organize your application's assets (images, stylesheets, JavaScript files) beyond the basic functionality provided by the asset pipeline. This includes strategies like using CDNs for faster delivery, implementing asset versioning for cache busting, precompiling assets for production environments, and employing tools for minification and compression to reduce file sizes and improve performance.

### 2.6 Authentication
- **Devise**
  - Devise is a flexible authentication solution for Rails applications. It provides a complete MVC solution based on Warden that handles user registration, login, password recovery, and other common authentication tasks.

### 2.7 Authorization
- **Pundit**
  - Pundit is a Ruby gem that provides a straightforward way to implement authorization in your Ruby on Rails applications. It focuses on defining authorization rules using plain Ruby objects (policies) that determine whether a given user is allowed to perform a specific action on a particular resource.
- **CanCanCan**
  - CanCanCan is an authorization library for Ruby on Rails applications that restricts what resources a given user is allowed to access. It provides a simple and flexible way to define abilities, which represent the permissions a user has on different resources, and then checks these abilities within your controllers and views to control access and display appropriate content.

### 2.8 Logging
- **Rails Logger**
  - The Rails Logger is a built-in component within Ruby on Rails that provides a standardized way to record events and messages during the execution of an application. It allows developers to track application behavior, diagnose issues, and monitor performance by writing information to various output destinations, such as files or the console.

### 2.9 Debugging
- **pry**
  - Pry is a powerful Ruby runtime developer console and alternative to irb. It allows you to pause your code's execution at any point, inspect variables, step through code line by line, and even modify your code on the fly.
- **debug**
  - The debug helper in Ruby on Rails provides a way to display the contents of a variable or object directly within your views. It's primarily used for debugging purposes, allowing you to quickly inspect data structures and identify issues in your code during development.

### 2.10 Testing
- **Testing**
  - Testing in software development involves verifying that individual units of code (unit tests) and the application as a whole (integration and system tests) function as expected. It helps ensure code quality, prevents regressions, and facilitates easier refactoring by providing a safety net to catch errors early in the development process.

---

## 3. Advanced

### 3.1 Plugins & Engines
- **Minitest**
  - Minitest is a complete testing suite for Ruby, providing support for test-driven development (TDD), behavior-driven development (BDD), mocking, and benchmarking. It's a lightweight and fast testing framework that comes bundled with Ruby, making it readily available for use in Rails applications.
- **Factory Bot**
  - Factory Bot is a library for creating Ruby objects for testing purposes. It provides a simple and clean syntax for defining factories, which are blueprints for creating instances of your models with pre-defined attributes.
- **RSpec**
  - RSpec is a testing framework for Ruby. It provides a domain-specific language (DSL) for writing tests that are easy to read and understand.
- **Capybara**
  - Capybara is a Ruby gem that simplifies acceptance testing for web applications. It simulates how a user interacts with your application through a browser, allowing you to write tests that verify the behavior of your application from an end-user perspective.

### 3.2 Mailbox & Mailer
- **Mailbox & Mailer**
  - The Rails Mailbox and Mailer provide a structured way to handle incoming and outgoing emails. Mailers are used to compose and send emails from your application, defining email content, recipients, and headers.

### 3.3 Background Jobs
- **Background Jobs**
  - Background jobs allow you to perform time-consuming tasks outside of the main request-response cycle. This means your web application can remain responsive and quickly handle user requests, while the longer tasks are processed in the background.

### 3.4 Security
- **Security**
  - Security in web applications involves protecting data and functionality from unauthorized access, use, disclosure, disruption, modification, or destruction. It encompasses various practices and techniques to ensure confidentiality, integrity, and availability of the application and its data.

### 3.5 Storage
- **Storage**
  - Rails itself doesn't directly manage file storage; instead, it relies on external services or libraries to handle the actual saving and retrieval of these files. This allows you to store files locally on your server, or more commonly, in cloud storage services like Amazon S3, Google Cloud Storage, or Azure Blob Storage.

### 3.6 Deployment
- **Kamal**
  - Kamal is a deployment tool created by 37signals (the creators of Ruby on Rails) designed to simplify the process of deploying web applications to one or more servers. It focuses on using Docker containers and modern deployment strategies like zero-downtime deployments, making it easier to manage and scale your Rails applications in production environments.

### 3.7 Rails Internationalization
- **Rails Internationalization**
  - Internationalization (I18n) is the process of designing and developing applications that can be adapted to various languages and regions without engineering changes. It involves extracting text and other locale-specific data from the application's code and storing it in separate files, allowing the application to be translated and formatted for different locales.

---

## 4. Optional / Specialized Topics

- Why Web Frameworks?
- Rails & Frontend
- config
- db
- Gemfile
- public
- Basic Queries
- Cookies
- Sessions
- Model Methods
- Inspecting Routes
- Constraints
- Named Routes
- Creating Models
- Query Optimization
- Raw SQL
- Conditions
- Ordering
- MySQL
- MariaDB
- form_with
- Form Elements
- Nested Forms
- Form Validation
- Kaminari

---

## 5. References

- [Ruby on Rails Roadmap](https://roadmap.sh/ruby-on-rails)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer

### Related Skills
- Ruby
- Django
- Laravel
- Node.js