# PHP

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/php
- Related Roles:
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction to PHP
- **Evolution and History**
  - PHP, originally standing for Personal Home Page, is a popular scripting language used commonly for web development. Rasmus Lerdorf created it in 1994, and since then, it has evolved significantly from a simple set of CGI binaries written in C, to a full-featured language.
- **PHP Versions and Features**
  - PHP (Hypertext Preprocessor) versions are critically important as each release comes with new features, improvements, and bug fixes. PHP versions start from PHP 1.0 released in 1995 and have improved over the years.
- **What is PHP?**
  - PHP, an acronym for Hypertext Preprocessor, is a popular server-side scripting language favored for web development. It's versatile, dynamic, and can be embedded seamlessly into HTML code.
- **Basic PHP Syntax**
  - PHP syntax is generally considered similar to C-style syntax, where code blocks are defined with curly braces, variables start with a dollar sign ($), and statements end with a semicolon (;), making it relatively easy to learn for programmers familiar with C-like languages; PHP scripts are embedded within HTML using opening tags "" to mark where PHP code should be executed within a web page.
- **Variables and Scope**
  - Variables in PHP are declared with a $ prefix and hold values of any type. Scope determines where a variable is accessible: variables defined outside a function are global and not accessible inside functions unless declared with the global keyword.

### 1.2 Installing PHP
- **WAMP**
  - WAMP is a popular software stack used for developing PHP web applications on Windows systems. Acting as an abbreviation for Windows, Apache, MySQL, and PHP, WAMP provides all the components necessary to set up a local web server.
- **XAMPP**
  - XAMP (Cross-Platform, Apache, MariaDB, PHP) is a lightweight local development stack. It bundles Apache, MariaDB, and PHP into a single installer, making it easy to run a web server locally without manual configuration.
- **MAMP**
  - MAMP (Mac, Apache, MySQL, PHP) is a local server environment designed for macOS, though a Windows version also exists. It packages Apache or Nginx, MySQL, and PHP together and provides a graphical interface for managing them.
- **LAMP**
  - LAMP stands for Linux, Apache, MySQL, and PHP. It is a widely used open-source web server stack for deploying PHP applications in production.

### 1.3 Arrays
- **Data Types**
  - PHP supports several data types: integers, floats, strings, booleans, arrays, objects, NULL, and resources. The language is loosely typed, so PHP will automatically convert types when needed.
- **echo**
  - echo outputs one or more strings to the browser or command line. It is a language construct, not a function, so parentheses are optional.
- **print**
  - The 'print' statement in PHP is an in-built function used for outputting one or more strings. Unlike 'echo', it is not a language construct and has a return value.
- **var_dump**
  - vardump() outputs the type and value of one or more variables. For arrays and objects, it recursively displays the structure and types of all nested values.
- **print_r**
  - The print\r function in PHP is used to print human-readable information about a variable, ranging from simple values to more complex, multi-dimensional arrays and objects. It's exceptionally helpful while debugging, providing more information about the variable's contents than the echo or print functions.
- **Casting Data Types**
  - Type casting in PHP converts a value from one type to another. You cast explicitly by placing the target type in parentheses before the value, like (int)$value.
- **Indexed Arrays**
  - Indexed arrays use numeric keys starting at zero. Values are accessed by their position, like $arr[0].
- **Associative Arrays**
  - Associative arrays use named string keys instead of numeric indexes. You define them with explicit key-value pairs: ['name' => 'Alice', 'age' => 30].

### 1.4 Conditionals
- **if/else**
  - The if/else structure executes a block of code when a condition is true and a different block when it is false. elseif adds additional conditions to check in sequence.
- **switch**
  - The switch statement compares a single expression against multiple possible values using case labels. PHP uses loose comparison (==) in switch cases.
- **match**
  - The match expression works like switch but uses strict comparison (===) and returns a value rather than executing statements. Each arm maps one or more conditions to an expression.
- **Null Coalescing Operator**
  - The Null Coalescing Operator (??) in PHP is a simple and useful tool for handling variables that might not be set. It allows developers to provide a default value when the variable happens not to have a value.
- **Null Safe Operator**
  - The Null Safe Operator is a handy feature in PHP which deals with an issue that often pops up when working with objects: trying to access properties or methods on an object that might be null. Instead of a fatal error, the PHP Null Safe Operator (indicated by ?->) allows null values to be returned safely, making your code more robust.

---

## 2. Intermediate

### 2.1 Loops
- **require**
  - require includes and evaluates a specified PHP file. If the file is not found, PHP throws a fatal error and halts execution.
- **require_once**
  - requireonce works like require but checks whether the file has already been included and skips it if so. This prevents duplicate declarations of classes, functions, or constants when the same file might be included from multiple places.
- **include**
  - include inserts the contents of another PHP file into the current script. If the file is not found, PHP emits a warning but continues execution.
- **include_once**
  - includeonce works like include but skips inclusion if the file has already been loaded. It avoids redeclaring functions or classes when the same file is referenced multiple times across a codebase.

### 2.2 Functions
- **Multi-dimensional Arrays**
  - Multi-dimensional arrays contain other arrays as values, creating a nested structure. They are used to represent tables, grids, or grouped data.
- **Function Declaration**
  - A function is declared using the function keyword, followed by the function name, parentheses for parameters, and a code block. Function names are case-insensitive in PHP.
- **Parameters / Return Values**
  - Parameters are variables listed in the function signature that receive values when the function is called. PHP passes arguments by value by default, meaning changes inside the function don't affect the original variable.
- **Default / Optional Params**
  - Default parameter values are assigned in the function signature with =. When a caller omits that argument, the default value is used instead.
- **Named Arguments**
  - Named arguments let you pass values to a function by specifying the parameter name explicitly, like strpad(string: 'hello', length: 10). This removes the need to follow positional order and makes call sites easier to read.
- **Anonymous Functions**
  - Anonymous functions (closures) are functions without a name, typically assigned to a variable or passed as a callback. They are created with the function keyword and can capture variables from the surrounding scope using the use keyword.
- **Arrow Functions**
  - Arrow functions provide a more concise syntax to create anonymous functions. The feature enthusiastically borrowed from modern Javascript significantly improves PHP's functional programming credibility.
- **Callback Functions**
  - A callback function in PHP is a function that is passed as an argument to another function. The receiving function can then invoke this function as needed.
- **Recursion**
  - Recursion is a technique where a function calls itself to solve a smaller version of the same problem. Each recursive call must move toward a base case that stops the recursion.
- **Variadic Functions**
  - Variadic functions accept a variable number of arguments using the ... spread operator in the parameter list, like function sum(...$numbers).

### 2.3 HTTP Methods
- **Constants**
  - Constants are identifiers for fixed values that cannot be changed during script execution. They are defined using define() or the const keyword.
- **$_GET**
  - $GET contains variables passed to the script via URL query parameters. For a URL like page.php?id=5&lang=en, $GET['id'] returns 5.
- **$_POST**
  - $POST holds variables submitted through an HTTP POST request, typically from HTML forms with method="post". Unlike GET data, POST data is not visible in the URL.
- **$_REQUEST**
  - $REQUEST merges the contents of $GET, $POST, and $COOKIE into a single superglobal array. Because it combines multiple sources, it is less predictable and generally avoided in favor of using $GET or $POST directly.
- **$_SERVER**
  - $SERVER is a superglobal array containing information about the server environment and the current HTTP request. Common entries include $SERVER['REQUESTMETHOD'], $SERVER['HTTPHOST'], $SERVER['SCRIPTNAME'], and $SERVER['REMOTEADDR'].

### 2.4 Form Processing
- **Form Processing**
  - Form processing in PHP involves reading submitted input from $GET or $POST, validating and sanitizing the values, and then performing an action such as saving to a database or sending an email. The Post/Redirect/Get (PRG) pattern is commonly used to prevent duplicate form submissions on page reload.

### 2.5 State Management
- **Writing Files**
  - PHP writes to files using fileputcontents() for simple writes or fopen() with fwrite() for more control. The FILEAPPEND flag appends to an existing file instead of overwriting it.
- **Reading Files**
  - PHP reads file contents using functions like filegetcontents() for reading the entire file as a string, and fopen() with fread() for reading in chunks. file() reads a file into an array of lines.
- **File Permissions**
  - File permissions control who can read, write, or execute a file. PHP uses chmod() to set permissions programmatically and fileperms() to read them.
- **JSON Processing**
  - PHP encodes data to JSON with jsonencode() and decodes JSON strings with jsondecode(). jsondecode() returns an object by default or an associative array when the second argument is true.
- **CSV Processing**
  - PHP handles CSV files using fgetcsv() to read rows as arrays and fputcsv() to write arrays as CSV lines. For reading an entire CSV into memory, arraymap('strgetcsv', file($path)) is a common shortcut.
- **XML Processing**
  - PHP processes XML using two main approaches: SimpleXML for straightforward access to XML data as objects, and the DOM extension for full programmatic control over the document tree. XMLReader handles large XML files efficiently by streaming rather than loading the entire document into memory.
- **Cookies**
  - Cookies are small key-value strings stored in the user's browser and sent with every request to the matching domain. PHP sets cookies with setcookie() and reads them through $COOKIE.
- **Sessions**
  - Sessions store user data on the server across multiple requests. A session is started with sessionstart(), and data is stored in the $SESSION superglobal.
- **Input Validation**
  - Input validation checks that user-supplied data conforms to expected formats and constraints before processing it. PHP's filtervar() function supports filters for emails, URLs, integers, floats, and IP addresses.
- **XSS Prevention**
  - Cross-Site Scripting (XSS) occurs when untrusted data is rendered in the browser as executable script. The primary defense in PHP is escaping output with htmlspecialchars() when rendering user-supplied content in HTML.
- **SQL Injection**
  - SQL injection occurs when unvalidated user input is interpolated directly into a SQL query, allowing attackers to manipulate the query. The fix is to use prepared statements with parameterized queries through PDO or MySQLi.
- **CSRF Protection**
  - Cross-Site Request Forgery (CSRF) tricks authenticated users into submitting unintended requests. The standard defense is generating a unique, unpredictable token per session, embedding it in forms, and validating it on the server when the form is submitted.
- **Password Hashing**
  - PHP provides passwordhash() to securely hash passwords using bcrypt or Argon2. The resulting hash includes the algorithm, cost factor, and salt, so no separate salt storage is needed.
- **Auth Mechanisms**
  - When you are developing PHP application, security should always be a top priority and authentication mechanism forms it's very core. It ensures proper establishing of user identities before they can access your system's resources.
- **Sanitization Techniques**
  - Sanitization removes or encodes unsafe characters from user input before using it in output, queries, or commands. PHP provides htmlspecialchars() to escape HTML, striptags() to remove HTML tags, and filtervar() with filters like FILTERSANITIZEEMAIL.

### 2.6 File Uploads
- **PDO**
  - PDO (PHP Data Objects) is a database abstraction layer that provides a consistent interface for connecting to multiple database types, including MySQL, PostgreSQL, and SQLite. It supports prepared statements, which protect against SQL injection.
- **MySQLi**
  - MySQLi is a MySQL-specific database extension that offers both procedural and object-oriented APIs. Like PDO, it supports prepared statements and bound parameters.
- **Object-Relational Mapping (ORM)**
  - An ORM maps database tables to PHP classes and rows to objects, allowing you to interact with the database using object-oriented code instead of raw SQL. Doctrine is the most widely used PHP ORM; Laravel's Eloquent is another popular option.
- **Database Transactions**
  - Database transactions in PHP refer to a unit of work performed within a database system, which is treated in a coordinated manner. This technique is vital when dealing with critical tasks like money transfer between accounts, where data consistency is crucial.

---

## 3. Advanced

### 3.1 OOP Fundamentals
- **Connection Pooling**
  - Connection pooling reuses existing database connections instead of opening a new connection for each request. PHP itself is stateless per request, so persistent connections (PDO::ATTRPERSISTENT) simulate pooling within a single process.
- **Performance Optimization**
  - PHP performance optimization focuses on reducing response time and server load. Common approaches include using opcode caching with OPcache, reducing database queries, leveraging HTTP caching, profiling with Xdebug or Blackfire, and writing efficient loops and data structures.
- **Database Migrations**
  - Database migrations are versioned scripts that define incremental changes to a database schema, such as creating tables, adding columns, or modifying indexes. They allow teams to evolve the database schema in a controlled, reproducible way.
- **Classes and Objects**
  - PHP supports object-oriented programming, offering a multi-paradigm way of coding through classes and objects. A class is like a blueprint for creating objects that encapsulate all faculties, properties and methods.
- **Constructor / Destructor**
  - The constructor (construct) is a special method called automatically when an object is instantiated. It initializes the object's properties.
- **Properties and Methods**
  - Properties are variables defined within a class that hold an object's state. Methods are functions defined within a class that define its behavior.
- **Access Specifiers**
  - Access specifiers, also known as access modifiers, in PHP are keywords used in the class context which define the visibility and accessibility of properties, methods and constants. PHP supports three types of access specifiers: public, private, and protected.
- **Static Methods and Properties**
  - Static members belong to the class itself rather than to any instance. They are declared with the static keyword and accessed using ClassName::method() or self::.
- **Inheritance**
  - Inheritance allows a class to extend another class, inheriting its properties and methods. The child class uses extends and can override parent methods or add new ones.
- **Polymorphism**
  - Polymorphism allows different classes to be used through a common interface while each provides its own implementation. In PHP, this is achieved through method overriding and interface implementation.
- **Abstract classes**
  - Abstract classes in PHP are those which cannot be instantiated on their own. They are simply blueprints for other classes, providing a predefined structure.
- **Interfaces**
  - Interfaces define a contract of methods that implementing classes must provide. A class can implement multiple interfaces, unlike inheritance which is limited to a single parent.
- **Traits**
  - Traits are a mechanism for code reuse in single-inheritance languages like PHP. A trait defines methods that can be inserted into any class using the use keyword.
- **Namespaces**
  - Namespaces organize PHP code into logical groups and prevent naming conflicts between classes, functions, and constants in different libraries. They are declared with the namespace keyword at the top of a file.

### 3.2 PHP-FIG
- **Magic methods**
  - Magic methods are special PHP methods with double-underscore prefixes that are triggered automatically in response to specific events. Common ones include construct, toString, get, set, call, and invoke.
- **Dependency injection**
  - Dependency injection (DI) is a design pattern where a class receives its dependencies from outside rather than creating them internally. This makes classes easier to test and reduces coupling.
- **Type Declarations**
  - Type declarations specify the expected types for function parameters, return values, and class properties. PHP supports scalar types (int, string, bool, float), compound types (array, callable), class types, nullable types (?Type), union types (Type1|Type2), and the mixed type.
- **PSR Standards**
  - PSR (PHP Standard Recommendations) are specifications published by PHP-FIG that define common interfaces and conventions for PHP projects. Key PSRs include PSR-4 (autoloading), PSR-7 (HTTP message interfaces), PSR-12 (coding style), and PSR-3 (logging interface).
- **Profiling Techniques**
  - Profiling identifies which parts of a PHP application consume the most time or memory. Xdebug's profiler generates cachegrind files visualized with tools like KCachegrind.
- **Caching Strategies**
  - Caching Strategies are integral to Performance Optimization in PHP. Caching minimizes server load and enhances application speed by temporarily storing results of expensive operations, so that they can be reused in subsequent requests.
- **Memory Management**
  - PHP allocates and frees memory automatically, but developers can influence it. The memorylimit directive in php.ini caps memory per request.
- **Configuration Tuning**
  - PHP's behavior is controlled through php.ini settings covering memory limits, execution timeouts, error reporting, upload sizes, and more. Tuning these settings for production involves balancing resource usage with application needs.
- **Opcode Caching**
  - Opcode caching stores the compiled bytecode of PHP scripts in memory so subsequent requests skip the parsing and compilation step. OPcache is the built-in PHP opcode cache and is enabled by default in modern PHP.
- **Executing System Commands**
  - PHP can run shell commands using functions like exec(), shellexec(), system(), and passthru(). Each differs in how it captures and returns output.
- **Process Control**
  - PHP can manage processes using the PCNTL extension, which provides functions for forking, signaling, and waiting on child processes. Process control is used in CLI scripts and long-running daemons.
- **Environment Variables**
  - Environment variables are key-value pairs set in the server environment and accessed in PHP via $ENV, getenv(), or $SERVER. They are the standard way to separate configuration from code, especially for secrets, database credentials, and feature flags.
- **Configuration Files**
  - Configuration files are critical for PHP applications because they help manage dynamic settings like database connection information, error reporting, and many other PHP settings without hard coding, making your application flexible and secure. PHP uses an "php.ini" file to hold these settings.
- **PHP-FPM**
  - PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation designed for high-traffic sites. It manages a pool of worker processes that handle incoming requests, supports dynamic and static process scaling, and can be configured with per-pool settings.

### 3.3 Style Tools
- **Yii**
  - Yii is a high-performance PHP framework suited for developing large-scale web applications. It uses a component-based architecture and includes built-in support for caching, authentication, RBAC, and database access via its Active Record implementation.
- **Symfony**
  - Symfony is a mature PHP framework and a collection of reusable components. It follows MVC conventions and emphasizes flexibility through dependency injection, event dispatchers, and a powerful routing and templating system (Twig).
- **PHPUnit**
  - PHPUnit is the de facto testing framework for PHP. It supports unit tests, integration tests, and test doubles (mocks, stubs, fakes).
- **Pest**
  - Pest is a modern PHP testing framework built on top of PHPUnit. It offers a more expressive, function-based syntax that reduces boilerplate and improves readability.
- **PHPCodeSniffer**
  - PHP CodeSniffer is a tool used to ensure your PHP code adheres to a defined coding standard. It works by tokenizing your code and detecting violations of a pre-configured set of rules, covering aspects like indentation, spacing, naming conventions, and more.
- **PHP CS Fixer**
  - PHP CS Fixer automatically reformats PHP code to comply with coding standards. It supports PSR standards and allows custom rule configurations.
- **Xdebug**
  - Xdebug is the most widely used PHP debugging and profiling extension. It supports step debugging via the DAP protocol, integrating with editors like VS Code and PhpStorm.
- **Zend Debugger**
  - Zend Debugger is a PHP extension that enables remote debugging of PHP applications, typically within Zend-based development environments. It allows step-by-step execution, variable inspection, and breakpoints.
- **Apache**
  - Apache is a popular web server that can efficiently host PHP applications. Apache integrates well with PHP, using its modphp module, providing a stable and consistent environment for your PHP scripts to run.
- **Nginx**
  - Nginx is a high-performance web server and reverse proxy commonly used to serve PHP applications via PHP-FPM using the FastCGI protocol. It handles static file serving efficiently and is configured through declarative block-based config files.

### 3.4 Static Analysis
- **Composer**
  - Composer is the standard dependency manager for PHP. It reads a composer.json file to resolve and download packages from Packagist, records exact installed versions in composer.lock, and generates the autoloader.
- **Packagist**
  - Packagist is the primary package repository for PHP, providing a service for hosting and distributing PHP package dependencies. Developers can use it to upload their PHP packages and share them with other developers globally.
- **Autoloading**
  - Autoloading automatically loads PHP class files when they are first used, without requiring manual include or require calls. PHP's splautoloadregister() registers a custom autoloader function.
- **PHPStan**
  - PHPStan is a static analysis tool for PHP that finds bugs by analyzing types and logic without running the code. It operates on configurable strictness levels (0–9), with higher levels catching more issues.
- **Phan**
  - Phan is a static analysis tool specially made for PHP language, greatly useful in catching common issues in the code before execution. It can analyze the syntax and behaviors in PHP code, detecting problems such as undeclared variables, type inconsistencies, uncaught exceptions, and more.
- **Psalm**
  - Psalm is a static analysis tool developed by Vimeo that focuses on type safety in PHP. It uses PHPDoc annotations and native type hints to infer and check types across the codebase.
- **cURL**
  - cURL is a library for making HTTP and other protocol requests from PHP. The curl functions allow you to send GET and POST requests, set headers, handle authentication, and follow redirects.
- **Guzzle**
  - Guzzle is a PHP HTTP client that simplifies making HTTP requests in PHP. It provides a straightforward and powerful way to send HTTP requests.

---

## 4. Optional / Specialized Topics

- Variables and Scope
- print_r
- Casting Data Types
- Indexed Arrays
- Associative Arrays
- Null Safe Operator
- Named Arguments
- Anonymous Functions
- Arrow Functions
- Callback Functions
- Recursion
- Variadic Functions
- $_SERVER
- CSV Processing
- XML Processing
- Cookies
- Sessions
- Input Validation
- XSS Prevention
- SQL Injection
- CSRF Protection
- Password Hashing
- Auth Mechanisms
- Sanitization Techniques
- Constructor / Destructor

---

## 5. References

- [PHP Roadmap](https://roadmap.sh/php)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer

### Related Skills
- System Design
- Linux
- Software Design & Architecture