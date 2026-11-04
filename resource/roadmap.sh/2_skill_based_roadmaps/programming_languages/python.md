# Python

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/python
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Learn the Basics
- **Basic Syntax**
  - Setup the environment for python and get started with the basics.
- **Variables and Data Types**
  - Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves.
- **Conditionals**
  - Conditional Statements in Python perform different actions depending on whether a specific condition evaluates to true or false. Conditional Statements are handled by if-elif-else statements and MATCH-CASE statements in Python.
- **Type Casting**
  - The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion: Implicit and Explicit.
- **Exceptions**
  - Exceptions are runtime errors that occur during program execution in Python. Instead of immediately stopping the program, Python allows developers to handle these errors using try, except, else, and finally blocks.
- **Functions, Builtin Functions**
  - In programming, a function is a reusable block of code that executes a certain functionality when it is called. Functions are integral parts of every programming language because they help make your code more modular and reusable.
- **Lists**
  - Lists are fundamental data structures in Python used to store an ordered collection of items. These items can be of different data types (numbers, strings, or even other lists), and lists are mutable, meaning you can change their contents after they are created by adding, removing, or modifying elements.
- **Tuples**
  - A tuple is an ordered and immutable collection of elements in Python. Unlike lists, tuples cannot be modified after creation, making them useful for storing fixed data such as coordinates, configuration values, or records that should remain unchanged.
- **Sets**
  - Python Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
- **Dictionaries**
  - In Python, a dictionary is a built-in data type that allows you to store key-value pairs. Each key in the dictionary is unique, and each key is associated with a value.
- **Loops**
  - Loops are programming structures that allow you to execute a block of code repeatedly as long as a specific condition remains true or for a set number of iterations. In Python, the two primary types of loops are for loops, which are typically used to iterate over a sequence like a list, tuple, or string, and while loops, which continue running until a defined logical condition evaluates to false.
- **Working with Strings**
  - Strings in Python are sequences of characters used to represent text. You can create them by enclosing characters within single quotes, double quotes, or triple quotes.
- **Operators**
  - Operators are symbols or keywords that perform operations on values and variables. Python includes several types: arithmetic operators (+, -, \, /) for math calculations, comparison operators (==, !=, <, >) for evaluating relationships between values, and logical operators (and, or, not) for combining conditions.
- **Comments**
  - Docstrings and comments document what code does and why. A docstring is a string literal placed right after a function, class, or module definition, and it becomes accessible through the object's doc attribute, which tools use to generate documentation automatically.

### 1.2 Data Structures & Algorithms
- **Arrays and Linked Lists**
  - Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index. Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element.
- **HashMaps**
  - HashMap, HashTable, Map, Dictionary, or Associative are all the names of the same data structure. It is a data structure that implements a set abstract data type, a structure that can map keys to values.
- **PyPI**
  - PyPI, typically pronounced pie-pee-eye, is a repository containing several hundred thousand packages. These range from trivial Hello, World implementations to advanced deep learning libraries.
- **Pip**
  - The standard package manager for Python is pip. It allows you to install and manage packages that aren’t part of the Python standard library.
- **uv**
  - uv is an "extremely fast" python package installer and resolver.

### 1.3 Modules
- **Builtin**
  - Python has a rich standard library of built-in modules that provide a wide range of functionality. Some of the most commonly used built-in modules include: sys, os, math, datetime, random, re, itertools, etc.
- **Custom**
  - Modules refer to a file containing Python statements and definitions. A file containing Python code, for example: example.py, is called a module, and its module name would be example.
- **Type Annot.**
  - Type annotations let developers specify the expected data types of variables, function parameters, and return values in Python. The interpreter does not enforce these hints at runtime, but tools like mypy and pyright use them to catch type errors before execution.

### 1.4 Error Handling
- **Error Handling**
  - Error handling is the process of anticipating, detecting, and resolving runtime issues during program execution. By using constructs like try, except, else, and finally blocks, developers can manage unexpected conditions—such as invalid user input or missing files—without allowing the application to crash.

### 1.5 Lambdas
- **Lambdas**
  - Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python.

### 1.6 Decorators
- **Decorators**
  - Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

### 1.7 Package Managers
- **Heaps, Stacks and Queues**
  - Heaps, stacks, and queues are fundamental data structures used to organize and manage data efficiently based on specific rules of access. A stack follows the Last-In, First-Out (LIFO) principle, where the last element added is the first one removed, similar to a stack of plates.
- **Binary Search Tree**
  - A binary search tree, also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree
- **Conda**
  - Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies.
- **Poetry**
  - Poetry is a dependency management and packaging tool that simplifies the process of handling libraries and project builds in a single configuration file. It manages virtual environments automatically and uses a lock file to ensure that every developer on a project uses the exact same version of every dependency.
- **pdm**
  - PDM is a modern Python package manager that supports PEP 582, which allows packages to be installed in a pypackages directory instead of the traditional site-packages directory. It aims to provide a streamlined and improved experience for managing dependencies, building, and publishing Python projects.

---

## 2. Intermediate

### 2.1 Iterators
- **Iterators**
  - An iterator is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

### 2.2 Common Packages
- **pyproject.toml**
  - This file is used to define the project configuration and dependencies. It is a configuration file that contains metadata about the project, such as its name, version, dependencies, and build settings.

### 2.3 Regular Expressions
- **Regular Expressions**
  - A regular expression is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

### 2.4 Variable Scope
- **mypy**
  - mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.
- **typing**
  - The typing module provides support for type hints in Python, allowing developers to specify expected data types for variables, function parameters, and return values. Type hints improve code readability, enable better editor support and static analysis, and help catch potential bugs early without changing how Python executes programs at runtime.

### 2.5 Object Oriented Programming
- **Recursion**
  - Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. Recursion solves such recursive problems by using functions that call themselves from within their own code.
- **Sorting Algorithms**
  - Sorting refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order.
- **Classes**
  - A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together.
- **Methods**
  - Methods are functions defined within a class that describe the behaviors or actions an object can perform. Dunder methods, short for "double underscore" methods, are special built-in methods—such as init or str—that allow you to define how your objects interact with Python’s built-in operations and syntax.

### 2.6 List Comprehensions
- **List Comprehensions**
  - List comprehensions are a concise way to create a list using a single line of code in Python. They are a powerful tool for creating and manipulating lists, and they can be used to simplify and shorten code.

### 2.7 Generator Expressions
- **Generator Expressions**
  - Generator expressions are a concise way to create a generator using a single line of code in Python. They are similar to list comprehensions, but instead of creating a list, they create a generator object that produces the values on-demand, as they are needed.

### 2.8 Paradigms
- **Paradigms**
  - Paradigms are fundamental styles or approaches to programming that dictate how a developer organizes and executes code. They define the structural logic of a program, offering different ways to solve problems by choosing how to represent data and functions.

### 2.9 Context Manager
- **Context Manager**
  - Context Managers are a construct in Python that allows you to set up context for a block of code, and then automatically clean up or release resources when the block is exited. It is most commonly used with the with statement.

---

## 3. Advanced

### 3.1 Static Typing
- **Pipenv**
  - Pipeline Environment (pipenv) is a tool that aims to bring the best of all packaging worlds (bundled, requirements.txt, setup.py, setup.cfg, etc.) to the Python world. It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages.
- **virtualenv**
  - virtualenv is a tool to create isolated Python environments. It creates a folder which contains all the necessary executables to use the packages that a Python project would need.
- **pyenv**
  - pyenv is a tool for managing multiple versions of the Python programming language on Unix-like systems. It works by setting environment variables to point to the directory where the desired version of Python is installed.
- **Pydantic**
  - Pydantic is a Python library for data validation and settings management using Python type annotations. It enforces type hints at runtime and provides clear, user-friendly error messages when data is invalid.
- **pyright**
  - pyright is a static type checker for Python. It is a Microsoft product and is written in TypeScript.
- **pyre**
  - pyrefly is a static type checker for Python. It is a tool that helps you find type errors in your Python code.

### 3.2 Learn a Framework
- **Pyramid**
  - Pyramid is a general, open source, web application development framework built in python. It allows python developer to create web applications with ease.
- **Plotly Dash**
  - Plotly Dash is a Python framework that allows you to build analytical web applications. It's a high-level library that enables you to create interactive, web-based data visualization dashboards without requiring extensive knowledge of web development.
- **gevent**
  - gevent is a Python library that provides a high-level interface to the event loop. It is based on non-blocking IO (libevent/libev) and lightweight greenlets.
- **Tornado**
  - Tornado is a scalable, non-blocking web server and web application framework written in Python. It was developed for use by FriendFeed; the company was acquired by Facebook in 2009 and Tornado was open-sourced soon after.
- **Fast API**
  - FastAPI is a modern Python web framework used for building APIs with high performance and automatic documentation. It leverages Python type hints for request validation, serialization, and editor support, making API development faster and less error-prone.
- **Django**
  - Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit

### 3.3 Concurrency
- **Inheritance**
  - Inheritance is a fundamental concept in object-oriented programming where a new class (the child class or subclass) is derived from an existing class (the parent class or superclass). The child class inherits attributes and methods from the parent class, allowing for code reuse and the creation of hierarchical relationships between classes.
- **aiohttp**
  - aiohttp is a Python 3.5+ library that provides a simple and powerful asynchronous HTTP client and server implementation.
- **Sanic**
  - Sanic is a Python 3.8+ web server and web framework designed for speed. It fully supports the async/await syntax introduced in Python 3.5, allowing you to write non-blocking request handlers that can handle thousands of concurrent connections efficiently.
- **GIL**
  - GIL is a mechanism that allows only one thread to execute Python code at a time. This limitation is related to memory management in CPython and can reduce the efficiency of multithreaded applications on multi-core systems.
- **Multiprocessing**
  - Multiprocessing utilizes multiple processes, each with its own GIL. This allows full utilization of multiple processor cores, which is effective for computationally intensive tasks.
- **Asynchrony**
  - Asynchronous programming, supported by asyncio, allows code to be executed without blocking, using async and await. This is especially useful for I/O tasks such as networking or file manipulation, allowing thousands of connections to be handled without blocking the main thread.
- **Encapsulation**
  - Encapsulation is a way to bundle data (attributes) and the methods that operate on that data into a single unit, known as a class. It restricts direct access to some of the object's components and prevents the accidental modification of data.

### 3.4 Code Formatting
- **ruff**
  - Ruff is a fast Python linter and code quality tool written in Rust that combines the functionality of multiple linting and formatting tools into a single, high-performance utility. It helps detect errors, enforce coding standards, and improve code quality while running significantly faster than traditional Python linters.
- **black**
  - Black is a python code formatter that automatically formats code according to a consistent style. By removing formatting decisions from developers, Black helps maintain uniform codebases, improves readability, and reduces time spent on style discussions during code reviews.
- **yapf**
  - yapf is a formatter for Python files. It is a tool that automatically formats Python code to conform to the PEP 8 style guide.
- **Sphinx**
  - Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.

### 3.5 File Handling
- **Flask**
  - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
- **Threading**
  - Multithreading allows multiple threads within a single process. However, because of GIL, threads cannot run in parallel on different cores, which makes multithreading suitable for I/O tasks (e.g., network requests) but not for computational tasks.
- **glob**
  - The glob module in Python is a handy tool for finding files and directories whose names match a specific pattern. It uses Unix shell rules for pattern matching, allowing you to easily search for files with certain extensions, files starting with a particular name, or any other combination of criteria you define using wildcards.

### 3.6 Testing
- **doctest**
  - Python’s standard library comes equipped with a test framework module called doctest. The doctest module programmatically searches Python code for pieces of text within comments that look like interactive Python sessions.
- **pytest**
  - pytest is a mature full-featured Python testing tool that helps you write better programs.
- **unittest / pyUnit**
  - PyUnit is an easy way to create unit testing programs and UnitTests with Python. (Note that docs.python.org uses the name "unittest", which is also the module name.)
- **tox**
  - Tox is a tool for automating test environment management and testing against multiple interpreter configurations. It is particularly useful for Python codebase that need to support multiple versions of Python.

---

## 4. Optional / Specialized Topics

- Exceptions
- Functions, Builtin Functions
- Lists
- Tuples
- Sets
- Dictionaries
- Loops
- Working with Strings
- Operators
- Comments
- uv
- pdm
- pyright
- pyre
- Fast API
- Django
- Multiprocessing
- Asynchrony
- Encapsulation

---

## 5. References

- [Python Roadmap](https://roadmap.sh/python)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- Go
- JavaScript
- Node.js