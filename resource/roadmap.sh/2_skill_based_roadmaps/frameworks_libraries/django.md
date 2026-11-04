# Django

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/django
- Related Roles:
  - Backend Developer
  - Fullstack Developer
  - Software Architect

---

## 1. Beginner

### 1.1 Virtual envs
- **Virtual envs**
  - Virtual environments are isolated spaces on your computer that contain specific versions of Python and its packages. This allows you to manage dependencies for different projects separately, preventing conflicts that can arise when projects require different versions of the same library.

### 1.2 Installing  Django
- **Installing  Django**
  - Installing Django involves setting up the Django package on your system so you can start developing web applications. This typically involves using a package installer like pip to download and install the necessary files and dependencies.

### 1.3 Introduction
- **Why use web frameworks**
  - Web frameworks provide a structure and set of tools to streamline the development of web applications. They handle common tasks like routing URLs, managing sessions, interacting with databases, and ensuring security, allowing developers to focus on the unique features of their application rather than reinventing the wheel.
- **How the Web Works**
  - The web operates through a client-server model where a client (like a web browser) sends a request to a server, and the server processes that request and sends back a response. This interaction involves protocols like HTTP for communication, URLs to identify resources, and DNS to translate domain names into IP addresses, enabling users to access and interact with content hosted on servers across the internet.
- **The MVC Model**
  - The Model-View-Controller (MVC) architectural pattern separates an application into three interconnected parts. The Model manages data and business logic, the View displays data to the user, and the Controller handles user input and updates the Model.

### 1.4 Projects & Apps
- **settings.py**
  - settings.py is a crucial Python module in a Django project that contains global configurations and settings for the entire application. It defines things like database connections, installed apps, middleware, template locations, and security settings.
- **manage.py**
  - manage.py is a command-line utility that's automatically created when you start a new Django project. It acts as a central point for running administrative tasks related to your project, such as starting the development server, running tests, creating database migrations, and more.

### 1.5 Running your Project
- **URL patterns**
  - URL patterns in Django define how URLs (web addresses) are mapped to specific views (functions that handle requests). They act like a directory, telling Django which view to execute when a user visits a particular URL.

### 1.6 Request Reponse Flow
- **urls.py**
  - In a Django project, urls.py files are responsible for mapping URL patterns to specific views. They act as a table of contents for your website, telling Django which view function to execute when a user visits a particular URL.
- **Named URLs**
  - Named URLs in Django provide a way to refer to your URL patterns by name instead of hardcoding the URL strings in your templates and views. This allows you to change your URL structure without having to update every place where the URL is used, making your code more maintainable and less prone to errors.
- **Path converters**
  - Path converters in Django are special strings within URL patterns that capture specific parts of the URL and pass them as arguments to your view functions. They define the type of data expected in that part of the URL (like an integer, string, or slug) and ensure that the data is correctly formatted before being passed to the view.
- **Reverse URL**
  - Reverse URL resolution is the process of generating URLs from their names and arguments, instead of hardcoding them directly into your templates or views. This allows you to make changes to your URL patterns without having to update every part of your application that uses those URLs.
- **models.py**
  - models.py is a Python file within a Django app that defines the structure of your application's data. It contains classes that represent database tables, with each class attribute representing a field in the table.
- **Regex Paths**
  - Regular expression paths in Django provide a powerful and flexible way to define URL patterns. Instead of using simple string matching, you can use regular expressions to capture specific parts of the URL and pass them as arguments to your view functions.
- **Routing Middleware**
  - Middleware in Django is a framework of hooks into Django's request/response processing. It's a layer of code that sits between the web server and your Django views, processing every request and response in your application.

### 1.7 Views
- **Function-based views**
  - Function-based views in Django are Python functions that take a web request and return a web response. They are a simple and direct way to handle HTTP requests and generate the appropriate output, such as HTML, JSON, or redirects.
- **Class-based views**
  - Class-based views (CBVs) in Django are an alternative way to implement views using Python classes instead of functions. They provide a structured and reusable approach to handling common view logic, promoting code organization and reducing redundancy.
- **views.py**
  - views.py is a Python file in a Django app that contains the logic for handling web requests and returning responses. It defines functions or classes, known as "views," that receive HTTP requests, process data (often interacting with models), and render templates to generate HTML responses that are sent back to the user's browser.
- **tests.py**
  - tests.py is a Python file within a Django app's directory that is dedicated to containing tests for that specific app. It allows developers to write and execute automated tests to ensure the app's functionality works as expected, covering various aspects like models, views, and forms.
- **admin.py**
  - admin.py is a Python file within a Django app that's responsible for configuring how your models are displayed and managed in Django's automatically generated admin interface. It allows you to register your models, customize their appearance, add search functionality, and define how they can be edited through the admin site.

### 1.8 Customizing Views
- **Generic views**
  - Generic views in Django are pre-built views that handle common web development tasks, like displaying a list of objects, creating new objects, or updating existing ones. They reduce the amount of boilerplate code you need to write by providing reusable logic for interacting with your models and templates.
- **migrations**
  - Migrations in Django are a way to propagate changes you make to your models (like adding a field, deleting a model, etc.) into your database schema. They are essentially Python files that describe how to alter your database tables to match the current state of your models.
- **urls.py**
  - In Django, the urls.py file within an app is responsible for defining the URL patterns for that specific app. It acts as a table of contents, mapping URL paths to specific views (functions or classes) that handle the corresponding requests.
- **ListView**
  - ListView is a type of generic view in Django that simplifies the process of displaying a list of objects from a database. It automates tasks like fetching data, paginating results, and rendering a template with the list of objects, reducing the amount of boilerplate code you need to write when creating list views.
- **DetailView**
  - DetailView is a pre-built class-based view in Django that simplifies the process of displaying the details of a single object. It automatically fetches an object from the database based on a provided lookup (typically a primary key or slug) and renders it using a specified template.

### 1.9 DTL Syntax
- **Variables**
  - Variables in Django templates are placeholders that get replaced with actual values when the template is rendered. They allow you to dynamically display data from your Django views within your HTML templates.
- **static**
  - Within a Django project, the static folder is where you store static files like CSS stylesheets, JavaScript files, images, and fonts. These files are essential for styling and adding interactivity to your web application's user interface.
- **media**
  - The media folder in a Django project is where you store user-uploaded files like images, videos, and documents. Django doesn't automatically create this folder; you typically create it yourself at the project's root or within an app.
- **templates**
  - The templates folder in a Django project is where you store your HTML files. These HTML files define the structure and content of your web pages.
- **Filters & custom filters**
  - Filters in Django Template Language (DTL) are used to modify the output of variables. They are applied using a pipe | symbol and can perform various transformations like changing case, formatting dates, or truncating text.
- **Tags & custom tags**
  - Tags are control structures that Django's template engine uses to perform actions like looping, variable assignment, or conditional logic within templates. Custom tags allow developers to extend the template language by defining their own tags to perform specific tasks or render complex data in a reusable way.
- **for**
  - The for tag in Django Template Language (DTL) provides a way to iterate over items in a list or other iterable object within your templates. It allows you to display data dynamically by looping through each item and rendering it according to the template's structure.

### 1.10 Templates
- **CreateView**
  - CreateView is a powerful generic class-based view in Django that simplifies the process of creating new objects in your database. It handles displaying a form for creating the object, validating the submitted data, and saving the new object to the database if the data is valid.
- **UpdateView**
  - UpdateView is a class-based view in Django that simplifies the process of creating a view to handle updating an existing model instance. It provides a pre-built structure for displaying a form populated with the instance's data, processing the form submission, validating the data, and saving the updated instance to the database.
- **DeleteView**
  - DeleteView in Django is a pre-built class-based view designed to handle the deletion of a specific object from your database. It provides a structured way to present a confirmation page to the user, process the deletion upon confirmation, and then redirect the user to another page.

---

## 2. Intermediate

### 2.1 Template Inheritance
- **if**
  - The if tag in Django Template Language (DTL) allows you to control which parts of your template are rendered based on the truthiness of a variable or expression. It evaluates a variable, and if that variable is "true" (i.e., exists, is not empty, and is not a false boolean value), the block of code within the if tag is rendered.

### 2.2 Models
- **Field options**
  - Field options are attributes you can define within a Django model's field to control its behavior and characteristics. These options allow you to specify constraints, default values, validation rules, and other metadata for each field, influencing how data is stored, displayed, and handled within your application.
- **Custom fields**
  - Custom fields in Django allow you to define your own field types beyond the standard ones provided by Django, such as CharField, IntegerField, and DateTimeField. This is useful when you need to store data in a specific format or require specialized validation logic that isn't covered by the built-in field types.
- **Fields types**
  - Model field types define the kind of data a field in your Django model can hold, such as text, numbers, dates, or relationships to other models. Each field type corresponds to a specific data type in the database and provides built-in validation and form handling.

### 2.3 Model relationships
- **Model relationships**
  - Model relationships in Django define how different models (database tables) are connected. These relationships allow you to link related data, such as a blog post belonging to a specific author or a customer having multiple orders.

### 2.4 Model methods
- **Model methods**
  - Model methods are functions you define within a Django model class to add custom behavior to individual model instances. These methods allow you to encapsulate logic related to a specific object, such as calculating derived values, performing data manipulations, or implementing custom validation rules.

### 2.5 Model inheritance
- **Querying data**
  - The Django ORM (Object-Relational Mapper) provides a powerful and convenient way to interact with your database. Instead of writing raw SQL queries, you use Python code to retrieve data from your models.
- **Aggregations**
  - Aggregations in Django allow you to summarize data from multiple objects in your database. They compute a single summary value (like average, sum, or count) for a group of objects.
- **Create, Update, Delete**
  - The Django ORM (Object-Relational Mapper) provides a high-level interface for interacting with databases. It allows you to perform CRUD (Create, Read, Update, Delete) operations on your database tables using Python code instead of writing raw SQL queries.
- **Filtering & lookups**
  - Filtering and lookups are fundamental mechanisms within Django's Object-Relational Mapper (ORM) that allow you to precisely query your database. They enable you to retrieve specific data based on defined criteria, such as finding all users with a particular name or all articles published within a certain date range.
- **Raw SQL**
  - Raw SQL queries in Django allow you to bypass the Django ORM and write SQL statements directly. This is useful when you need to optimize performance, access database-specific features not supported by the ORM, or execute complex queries that are difficult to express using the ORM's query API.

### 2.6 Setting up the Database
- **PostgreSQL**
  - PostgreSQL is an open-source, advanced relational database management system (RDBMS) known for its reliability, data integrity, and adherence to standards. It offers a wide range of features, including support for complex data types, advanced indexing, and transactional integrity, making it a robust choice for managing structured data.
- **SQLite**
  - SQLite is a self-contained, serverless, zero-configuration, transactional SQL database engine. It's embedded directly into the application, meaning it doesn't require a separate server process to operate.
- **Comments**
  - Comments in Django Template Language (DTL) allow developers to embed explanatory notes or temporarily disable sections of template code without affecting the rendered output. These comments are not visible to the end-user in the final HTML.

### 2.7 Migrations
- **MariaDB**
  - MariaDB is an open-source relational database management system that is often used as a drop-in replacement for MySQL. It's known for its performance, stability, and rich feature set.

### 2.8 Django ORM
- **Django Forms**
  - Form validation in Django involves verifying that the data submitted by a user through a form meets specific requirements before it's processed and saved. This ensures data integrity and prevents errors by checking for things like required fields, correct data types, valid ranges, and unique values.

### 2.9 Static Files
- **MySQL**
  - MySQL is a popular open-source relational database management system. Django supports MySQL as one of its database backends, allowing you to store and manage your application's data using MySQL's robust features.
- **Whitenoise**
  - Whitenoise is a library that allows your web application to serve static files directly from its own WSGI server. This means you don't need to rely on a separate web server like Nginx or Apache to serve static assets such as CSS, JavaScript, and images.

### 2.10 Pagination
- **Pagination**
  - Pagination divides large datasets into smaller, discrete pages, improving user experience and server performance. In Django, this is typically used when displaying a large number of objects, such as blog posts or product listings.

### 2.11 Message Framework
- **Message Framework**
  - The message framework in Django provides a way to deliver one-time notification messages, also known as "flash messages," to users. These messages are typically used to provide feedback about the outcome of an action, such as a successful form submission or an error that occurred.

### 2.12 Django Shell
- **Django Shell**
  - The Django Shell is an interactive Python interpreter that provides direct access to your Django project's models, database, and settings. It allows you to test code snippets, query data, and perform administrative tasks without needing to run your entire application.

### 2.13 Django Admin
- **Admin Customization**
  - Admin customization in Django refers to modifying the default appearance and functionality of the Django admin interface. This involves tailoring the admin site to better suit the specific needs of a project, such as changing the display of fields, adding custom actions, or altering the overall layout.

---

## 3. Advanced

### 3.1 Middleware
- **Query Optimization**
  - Query optimization is the process of improving the efficiency of database queries to reduce execution time and resource consumption. It involves analyzing queries, identifying bottlenecks, and applying techniques like indexing, query rewriting, and caching to minimize the amount of data processed and the number of database operations performed.
- **Customization**
  - Middleware in Django is a framework of hooks into Django's request/response processing. It's a way to modify the incoming request or outgoing response at various points in the process.
- **Model Forms**
  - ModelForm validation in Django involves ensuring that the data entered into a form, which is directly tied to a Django model, meets specific criteria before it's saved to the database. This process includes checking data types, lengths, and any custom validation rules defined in the model or the form itself, guaranteeing data integrity and preventing errors.
- **Form Validation**
  - Form validation in Django is the process of ensuring that the data submitted by a user through a form meets specific requirements before it's saved to the database. This involves checking for things like required fields, correct data types (e.g., email address format), minimum or maximum lengths, and other custom rules you define.
- **CSRF**
  - CSRF (Cross-Site Request Forgery) is a web security vulnerability where a malicious website tricks a user's browser into performing actions on a trusted site without the user's knowledge. In Django forms, CSRF protection works by including a unique, secret token in each form.
- **Transactions**
  - Transactions are a way to group a series of database operations into a single unit of work. This means that either all the operations within the transaction succeed, or none of them do.
- **Fixtures**
  - Fixtures in Django provide a way to populate your database with initial data, useful for testing, development, or providing a default dataset for your application. They are typically data files (JSON, XML, or YAML) containing serialized data for one or more database tables, allowing you to easily load and unload data into your Django project's database.

### 3.2 Authentication
- **Built-in user model**
  - Django provides a default user model that handles common authentication tasks like user registration, login, and permission management. This model includes fields like username, password, email, first name, and last name, and it offers methods for password hashing and user authorization.
- **Custom user model**
  - A custom user model in Django allows developers to define their own user model instead of using the default Django user model. This provides flexibility to include additional fields or methods tailored to the specific requirements of an application, such as storing extra profile information or implementing custom authentication logic.
- **django-allauth**
  - Django-allauth is a reusable Django app that provides comprehensive social authentication, registration, account management, as well as local username/password authentication. It simplifies the process of integrating various authentication providers (like Google, Facebook, Twitter, etc.) into your Django project, handling the complexities of OAuth and other authentication protocols.

### 3.3 Authorization
- **Users & Permissions**
  - User authentication and authorization are fundamental aspects of web application security. Django provides a built-in system for managing users, groups, and permissions, allowing developers to control access to different parts of their application.

### 3.4 Django  REST Framework
- **Routers**
  - Routers in Django REST Framework (DRF) provide an automated way to generate URL patterns for your API views. Instead of manually defining URLs for common API actions like listing, creating, retrieving, updating, and deleting resources, routers handle this automatically based on the viewsets you define.
- **Views & ViewSets**
  - Views in Django REST Framework handle the logic for processing incoming web requests and returning responses, similar to regular Django views. ViewSets provide a way to group related views into a single class, reducing code duplication and simplifying the creation of complex APIs by offering pre-built actions like list, create, retrieve, update, and delete.
- **Serializers**
  - Serializers in Django REST Framework transform complex data, like querysets and model instances, into Python datatypes that can be easily rendered into JSON, XML, or other content types. They also handle the reverse process, allowing parsed data to be converted back into model instances after validation.

### 3.5 Django Ninja
- **Handlers**
  - Handlers in Django's logging framework determine where log messages go. They act as the delivery mechanism, taking log records created by loggers and sending them to specific destinations.
- **Loggers**
  - Loggers are the entry points in Django's logging system that your code uses to record events. They capture messages, optionally filter them based on severity levels (like DEBUG, INFO, WARNING, ERROR, and CRITICAL), and then pass them on to handlers.

### 3.6 Logging
- **Filters**
  - Filters in Django's logging framework provide a way to add extra control over which log records are processed by a handler. They determine whether a specific log record should be emitted based on criteria you define.
- **Formatters**
  - Formatters in Django's logging framework structure log records into human-readable or machine-parseable strings. They define the layout of log messages, specifying which pieces of information (like timestamp, log level, message content, or source file) are included and how they are arranged.

### 3.7 Debugging
- **django_silk**
  - django-silk is a powerful profiling and inspection tool designed for the Django framework. It intercepts and stores HTTP requests and database query data, providing a real-time view of your application's performance.
- **PDB, IPDB**
  - PDB (Python Debugger) is an interactive source code debugger for Python programs. It allows you to pause your program during execution, inspect variables, step through code line by line, and set breakpoints.
- **debug_toolbar**
  - The Django Debug Toolbar is a powerful set of panels that display various debugging information about the current request and response. It appears as a collapsible toolbar in your browser when you're developing a Django application.
- **Error Pages**
  - Error pages in Django are what users see when something goes wrong with your website. Instead of a confusing or blank screen, Django can display informative pages that explain the error.

### 3.8 Django Test Framework
- **pytest**
  - pytest is a popular Python testing framework that simplifies writing and running tests. It offers features like auto-discovery of test functions, simple assertion syntax, extensive plugin support, and detailed error reporting.
- **unittest & TestCase**
  - unittest is Python's built-in testing framework, providing a standard way to write and run tests. TestCase is a class within unittest that's used as a base class for creating individual test cases.
- **Background Tasks**
  - Background tasks in Django are processes that run independently of the main web application, without blocking user requests. They are useful for handling time-consuming or resource-intensive operations like sending emails, processing large datasets, or generating reports.
- **Asynchronous Django**
  - Asynchronous programming allows a program to execute multiple tasks seemingly at the same time without waiting for each task to complete before starting the next. Instead of blocking and waiting, the program can switch between tasks as needed, improving efficiency.
- **Caching**
  - Caching is a technique to store frequently accessed data in a temporary storage location (the cache) to speed up retrieval in the future. When data is requested, the system first checks the cache.
- **Localization**
  - Localization is the process of adapting a product or content to a specific target market. This involves translating text, but also adapting other elements like date formats, currency symbols, and cultural references to make the product feel native to the user's region.
- **Signals**
  - Signals in Django allow certain actions to be triggered when specific events occur in your application. Think of them as a way to let different parts of your code communicate with each other without being directly linked.
- **Celery**
  - Celery is a distributed task queue that allows you to run tasks asynchronously, outside of the typical request-response cycle. It's often used to handle time-consuming or resource-intensive operations, such as sending emails, processing images, or generating reports, without blocking the user's request.

### 3.9 Deployment
- **Production Checklist**
  - A production checklist is a structured list of tasks and configurations that need to be verified and completed before deploying a Django application to a live, production environment. It ensures that the application is secure, performant, and reliable for end-users by covering aspects like security settings, database configurations, static file handling, and monitoring setup.

---

## 4. Optional / Specialized Topics

- models.py
- Regex Paths
- Routing Middleware
- admin.py
- DetailView
- Filters & custom filters
- Tags & custom tags
- for
- Raw SQL
- CSRF
- Transactions
- Fixtures
- Caching
- Localization
- Signals
- Celery

---

## 5. References

- [Django Roadmap](https://roadmap.sh/django)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer
- Software Architect

### Related Skills
- Python
- System Design