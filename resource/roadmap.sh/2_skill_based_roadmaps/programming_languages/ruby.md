# Ruby

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ruby
- Related Roles:
  - Backend Developer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **Introduction**
  - Ruby is a dynamic, open-source programming language known for its simplicity and productivity. It emphasizes human readability, using a syntax that is easy to learn and write.

### 1.2 Setting things Up
- **Floats**
  - Floats represent real numbers with fractional parts in Ruby. They are used to store numerical values that require more precision than integers can provide.
- **Package Managers**
  - Package managers simplify the process of installing and managing software, including Ruby, on your system. Instead of manually downloading and configuring Ruby, you can use a package manager specific to your operating system.
- **Installers**
  - Installers are software packages designed to simplify the process of setting up Ruby on your computer. They typically handle downloading the necessary files, configuring your system environment, and ensuring that Ruby and its related tools are ready to use.
- **Managers**
  - Ruby version managers are tools that allow you to install and manage multiple versions of Ruby on the same system. This is useful because different projects may require different Ruby versions, and using a version manager prevents conflicts and simplifies switching between them.

### 1.3 Constants & Variables
- **Constants & Variables**
  - In Ruby, variables are named storage locations that hold data, and their values can be changed during the program's execution. Constants, on the other hand, are also named storage locations, but their values are intended to remain fixed throughout the program's runtime.

### 1.4 puts, print, p
- **puts, print, p**
  - puts, print, and p are methods in Ruby used to display output to the console. puts prints the given arguments followed by a newline character, print prints the arguments as they are without adding a newline, and p prints a human-readable representation of the given object, which is useful for debugging.

### 1.5 Comments
- **Comments**
  - Comments are notes in your code that the Ruby interpreter ignores. They're used to explain what the code does, making it easier for you and others to understand.

### 1.6 Naming conventions
- **Naming conventions**
  - Naming conventions are a set of rules or guidelines for choosing names for variables, methods, classes, and other entities in a programming language. These conventions promote code readability, maintainability, and consistency across projects.

---

## 2. Intermediate

### 2.1 Data Types
- **Integers**
  - Integers are whole numbers, meaning they don't have any fractional or decimal parts. They can be positive, negative, or zero.
- **Booleans**
  - Booleans represent truth values: either true or false. They are fundamental for decision-making in Ruby code, allowing programs to execute different blocks of code based on whether a condition is true or false.
- **Strings**
  - Strings are sequences of characters used to represent text. They are a fundamental data type for storing and manipulating textual information.
- **Symbols**
  - Symbols are lightweight, immutable strings often used as identifiers or names within a Ruby program. Unlike regular strings, symbols are guaranteed to be unique; Ruby only creates one copy of a symbol, regardless of how many times it's referenced.
- **Arrays**
  - Arrays in Ruby are ordered collections of items. They can hold any type of data, including numbers, strings, symbols, or even other arrays.
- **Hashes**
  - Hashes are collections of key-value pairs. Think of them like dictionaries, where each word (the key) has a definition (the value).

### 2.2 Type Casting
- **nil**
  - nil represents the absence of a value or a non-existent object. It's a special object in Ruby that signifies emptiness or the lack of a meaningful result.

### 2.3 Operators
- **case**
  - A case statement in Ruby provides a way to execute different blocks of code based on the value of a variable or expression. It's an alternative to using multiple if/elsif/else statements, especially when you need to check for several different possible values.
- **Arithmetic**
  - Arithmetic operators are symbols that perform mathematical calculations on numerical values. These operators allow you to perform addition, subtraction, multiplication, division, and other common arithmetic operations.
- **Comparison**
  - Comparison operators are symbols used to compare two values. These operators evaluate to either true or false based on the relationship between the values being compared.
- **Logical**
  - Logical operators in Ruby let you combine or modify boolean expressions (true or false). The main ones are && (and), || (or), and !
- **Assignment**
  - Assignment operators in Ruby are used to assign values to variables. The most basic assignment operator is the equals sign (=), which assigns the value on the right-hand side to the variable on the left-hand side.
- **Ranges**
  - Ranges in Ruby are used to create a sequence of values. They are defined using two endpoints, which can be numbers, characters, or any objects that can be compared using the <=> operator.

### 2.4 Conditional Statements
- **if, elsif, else**
  - Conditional statements allow you to execute different blocks of code based on whether a certain condition is true or false. The if statement executes a block of code if a condition is true.
- **unless**
  - unless is a conditional statement in Ruby that executes a block of code only if a specified condition is false. It's essentially the opposite of if.

### 2.5 Loops & Enumerations
- **redo**
  - redo is a control flow statement in Ruby used within loops (like for, while, until) and iterators (like each, map). When redo is encountered, it restarts the current iteration of the loop or iterator from the beginning, without evaluating any remaining code in that iteration.
- **break**
  - The break statement in Ruby is a control flow tool used to exit a loop prematurely. When break is encountered within a loop (like for, while, until, or each), the loop's execution is immediately terminated, and the program continues with the next statement after the loop.
- **next**
  - The next keyword in Ruby provides a way to skip the current iteration of a loop and proceed directly to the next iteration. When next is encountered within a loop (like for, while, until, or iterators like each), the remaining code in the current loop cycle is bypassed, and the loop immediately begins its next cycle, if one exists.
- **while**
  - A while loop in Ruby repeatedly executes a block of code as long as a specified condition is true. It checks the condition before each iteration, and if the condition is false from the start, the code block is never executed.
- **until**
  - The until loop in Ruby executes a block of code as long as a specified condition is false. It repeatedly runs the code within the loop until the condition becomes true.
- **times**
  - The times method in Ruby is a simple way to execute a block of code a specified number of times. It's called on an integer, and the block is executed that many times, with an optional block variable representing the current iteration number (starting from zero).
- **for**
  - The for loop in Ruby provides a way to iterate over a sequence of values, such as elements in an array or a range. It executes a block of code for each item in the sequence.
- **each**
  - each is a fundamental method in Ruby used to iterate over elements within a collection, such as an array or a hash. It applies a given block of code to each element in the collection, allowing you to perform operations on every item.
- **do/while**
  - do/while loops are a type of control flow statement that executes a block of code at least once, and then repeatedly executes the block as long as a specified condition is true. The condition is checked after the code block is executed, ensuring the block runs at least one time regardless of the initial state of the condition.

### 2.6 Enumerable
- **Querying**
  - Enumerable querying methods in Ruby allow you to gather information about a collection without necessarily extracting or transforming its elements. These methods check for the presence of elements that meet certain conditions, determine the size or characteristics of the collection, or verify if all or any elements satisfy a given criteria.
- **Fetching**
  - Enumerable comes with some methods that allow you to retrieve entries from the Enumerable, without modifying it. This includes methods to get leading and trailing elements, extract minimum and maximum value elements, as well as conduct groups, slices, and partitions.
- **Searching & Filtering**
  - Enumerable comes with some methods that allow you to select specific elements from a collection based on certain criteria. This allows you to extract subsets of data that meet your desired conditions, making it easier to work with large datasets or focus on relevant information.
- **Sorting**
  - The Enumerable module in Ruby provides several methods for sorting collections. These methods allow you to arrange elements in ascending or descending order based on their natural ordering or a custom comparison logic.
- **Iterating**
  - The Enumerable module in Ruby provides a collection of methods that allow you to traverse and process elements within a collection (like an array or hash). These iterating methods, such as each, map, select, and reject, simplify the process of performing actions on each item in the collection, transforming the collection, or filtering elements based on specific conditions.

### 2.7 Handling exceptions
- **begin, rescue, ensure**
  - Exception handling is a mechanism to deal with errors that occur during the execution of a program. In Ruby, the begin, rescue, and ensure keywords provide a structured way to handle these exceptions.

### 2.8 Interactive Ruby (irb)
- **Defining methods**
  - Methods, also known as functions in other programming languages, are reusable blocks of code designed to perform a specific task. Defining a method involves specifying its name, the parameters it accepts (if any), and the sequence of instructions it executes.
- **Blocks**
  - Blocks are chunks of code that can be passed to methods as if they were arguments. They are defined using either do...end or curly braces {}.
- **RubyGems**
  - RubyGems is a package management system for the Ruby programming language. It provides a standard format for distributing Ruby programs and libraries (called "gems"), a tool for easily installing gems, and a central repository (RubyGems.org) for finding and sharing them.
- **Bundler**
  - Bundler is a dependency manager for Ruby. It ensures that an application uses the exact versions of gems (Ruby libraries) that it needs to function correctly.
- **Procs**
  - A Proc in Ruby is an object that represents a block of code that can be stored, passed around, and executed later. Think of it as a named, reusable chunk of code.
- **Method Parameters**
  - Method parameters, also called arguments, are the values you pass into a method when you call it. There are several types: required parameters, which must be provided; optional parameters, which have default values if not provided; and variable-length arguments (using args), which allow you to pass in an arbitrary number of arguments as an array.
- **Scope**
  - Scope refers to the visibility and accessibility of variables within different parts of a program. It determines where a variable can be accessed and used.
- **Chaining Methods**
  - Chaining methods in Ruby lets you call multiple methods on an object in a single line of code. This works because most methods in Ruby return an object (often self, the object the method was called on).
- **Rbenv**
  - Rbenv is a command-line tool that allows you to easily manage multiple Ruby environments (versions) on a single system. It works by intercepting Ruby commands and determining which Ruby version to use based on the current directory or a global setting.

---

## 3. Advanced

### 3.1 Date & Time
- **Date & Time**
  - Date and Time represent specific points in time. They allow you to work with dates (year, month, day) and times (hour, minute, second) and perform operations like calculating durations, formatting dates for display, and comparing different points in time.

### 3.2 Regex
- **Regex**
  - Regular expressions (regex) are patterns used to match character combinations in strings. In Ruby, you can use regex to search, replace, or validate text within strings.

### 3.3 File I/O
- **RVM**
  - RVM (Ruby Version Manager) is a command-line tool that allows you to easily manage multiple Ruby environments on a single system. It enables you to install, manage, and work with different Ruby versions (like Ruby 2.7, 3.0, or JRuby) and gemsets (isolated collections of gems) independently.
- **Stacks  & queues**
  - Stacks and queues are fundamental data structures used to manage collections of items. A stack operates on the Last-In, First-Out (LIFO) principle, where the last element added is the first one removed, like a stack of plates.
- **Search Algorithms**
  - Search algorithms are methods used to find a specific element within a collection of data, like an array or a hash. These algorithms work by systematically checking each element in the data structure until the desired element is found or it's determined that the element is not present.

### 3.4 Metaprogramming
- **Instance variables**
  - Instance variables in Ruby are variables that hold data specific to an object. They are defined within a class but belong to individual instances (objects) of that class.
- **Lambdas**
  - Lambdas are anonymous functions, meaning they are functions without a name. They are objects in Ruby and can be treated like any other object, such as being passed as arguments to methods or stored in variables.
- **Defining Classes**
  - A class is a blueprint for creating objects. It defines the attributes (data) and behaviors (methods) that objects of that class will possess.
- **Recursion**
  - Recursion is a programming technique where a function calls itself within its own definition. This creates a loop-like behavior, but instead of using explicit loops (like for or while), the function breaks down a problem into smaller, self-similar subproblems until it reaches a base case, which stops the recursion and returns a value.
- **Sorting Algorithms**
  - Sorting algorithms are methods used to rearrange a collection of items (like numbers, strings, or objects) into a specific order, such as ascending or descending. These algorithms work by comparing elements and swapping their positions until the entire collection is ordered according to the desired criteria.
- **method_missing**
  - methodmissing is a Ruby method that gets called when you try to invoke a method on an object that doesn't exist. Instead of raising a NoMethodError, Ruby gives you a chance to handle the missing method call yourself.
- **send**
  - send in Ruby is a method that allows you to call other methods on an object dynamically by their name, which is passed as a symbol or string. It essentially bypasses the usual method call syntax, enabling you to invoke methods at runtime based on conditions or data.
- **define_method**
  - definemethod is a method used to dynamically create new methods within a class or module. Instead of explicitly writing out the method definition with the def keyword, definemethod allows you to generate methods at runtime, often based on data or logic that isn't known until the program is running.
- **Ruby DSL**
  - A Domain Specific Language (DSL) is a programming language designed for a particular kind of application. Instead of being a general-purpose language that can solve a wide range of problems, a DSL is focused on solving problems in a specific domain, making code more readable and maintainable within that domain.

### 3.5 Concurrency
- **Closures**
  - A closure is a block of code that can be passed around and executed later, even after the scope in which it was originally defined has ended. It "closes over" its surrounding environment, capturing the values of variables that were in scope when the closure was created.
- **Attributes accessors**
  - Attributes accessors provide a convenient way to access and modify the instance variables of a class. They automatically generate methods for reading (getting) and writing (setting) the values of these variables.
- **RDoc**
  - RDoc is a documentation generator for Ruby source code. It parses Ruby files and creates HTML or other formatted documentation based on comments and code structure.
- **YARD**
  - YARD (Yet Another Ruby Documentation) is a documentation generation tool for the Ruby programming language. It allows developers to create comprehensive and consistent documentation for their Ruby projects by parsing source code and extracting information based on specially formatted comments.
- **RuboCop**
  - RuboCop is a static code analyzer and formatter for Ruby. It inspects Ruby code and reports style issues, potential errors, and code smells based on a community-driven Ruby style guide.
- **Standard**
  - Standard is a Ruby gem that automatically formats and lints Ruby code, aiming to enforce a consistent style across projects. It combines the functionality of linters like RuboCop with an auto-formatter, providing a single tool to ensure code adheres to a predefined set of style rules.
- **Inheritance**
  - Inheritance in Ruby allows a class (the subclass or derived class) to inherit properties and behaviors from another class (the superclass or base class). This promotes code reuse and establishes an "is-a" relationship.
- **Modules & Mixins**
  - Modules in Ruby are collections of methods, classes, and constants. They provide a way to namespace and prevent naming conflicts.
- **Method Lookup**
  - Method lookup is the process a programming language uses to determine which method to execute when a method is called on an object. It involves searching through the object's class and its ancestors (inheritance hierarchy) to find the appropriate method definition.
- **Monkey Patching**
  - Monkey patching is a technique that allows you to add, modify, or replace existing code in a class or module at runtime. This means you can change the behavior of classes and modules, even those defined in external libraries, without directly altering their source code.
- **Refinements**
  - Refinements provide a way to modify the behavior of a class or module within a specific scope, without affecting the global definition of that class or module. This allows you to introduce changes or extensions to existing code in a localized manner, preventing unintended side effects in other parts of your application.
- **Threads**
  - Threads allow you to run multiple blocks of code seemingly at the same time within a single program. Think of them as lightweight processes that share the same memory space.
- **Fibers**
  - Fibers are a lightweight concurrency construct that allows you to create code blocks that can be paused and resumed. They provide a way to implement cooperative multitasking within a single thread, enabling you to manage multiple tasks without the overhead of creating and managing multiple threads or processes.
- **Pry**
  - Pry is a powerful Ruby runtime developer console and an alternative to irb. It offers features like syntax highlighting, code browsing, documentation lookup, and the ability to step through code execution.
- **irb**
  - IRB (Interactive Ruby) is a powerful tool for debugging Ruby code. It allows you to execute Ruby code line by line, inspect variables, and test code snippets in real-time.
- **Minitest**
  - Minitest is a complete testing suite for Ruby. It provides support for test-driven development (TDD), behavior-driven development (BDD), mocking, and benchmarking.
- **RSpec**
  - RSpec is a testing tool for Ruby. It provides a domain-specific language (DSL) for writing tests in a clear and readable format.
- **Test::Unit**
  - Test::Unit is a testing framework for Ruby, providing a structure for writing and running tests. It allows developers to define test cases as methods within classes, making it easy to organize and execute tests to verify the correctness of their code.
- **byebug**
  - Byebug is a powerful debugger for Ruby programs. It allows you to step through your code line by line, inspect variables, set breakpoints, and evaluate expressions in real-time.
- **debug**
  - debug is a powerful debugging tool integrated directly into Ruby. It allows developers to step through code execution, inspect variables, set breakpoints, and evaluate expressions in real-time.
- **Singleton Classes**
  - A singleton class in Ruby is a special kind of class that is associated with a single object. It allows you to define methods that are specific to that particular object, without affecting other objects of the same class.
- **Concurrent Ruby**
  - A mutex (mutual exclusion) is a synchronization primitive that provides exclusive access to a shared resource. It essentially acts as a lock, ensuring that only one thread or process can access a critical section of code at any given time.
- **VS Code**
  - The VS Code Ruby extension enhances the Visual Studio Code editor with features specifically designed for Ruby development. It provides functionalities like syntax highlighting, code completion, debugging support, linting, and formatting, making it easier for developers to write, test, and maintain Ruby code within the VS Code environment.
- **RubyMine**
  - RubyMine is an Integrated Development Environment (IDE) specifically designed for Ruby and Ruby on Rails development. It provides a comprehensive suite of tools for coding, testing, debugging, and deploying Ruby applications, aiming to enhance developer productivity through features like intelligent code completion, refactoring, and integration with various testing frameworks and version control systems.
- **Ruby on Rails**
  - Ruby on Rails is a server-side web application framework written in Ruby under the MIT License. Rails is a model-view-controller (MVC) framework, providing default structures for a database, a web service, and web pages.
- **Rack**
  - Rack provides a minimal interface between web servers and Ruby frameworks. By abstracting the connection between the server and the application, Rack allows developers to write Ruby web applications that can run on a variety of web servers with minimal configuration.
- **Sinatra**
  - Sinatra is a lightweight and flexible Domain Specific Language (DSL) for creating web applications in Ruby with minimal effort. It provides a simple way to map routes to Ruby code, allowing developers to quickly build web applications without the complexity of larger frameworks.
- **Ractors**
  - Threads are a way to achieve concurrency within a single process. They allow multiple parts of a program to execute seemingly simultaneously by sharing the same memory space.

---

## 4. Optional / Specialized Topics

- Arrays
- Hashes
- Assignment
- Ranges
- until
- times
- for
- each
- do/while
- Iterating
- Procs
- Method Parameters
- Scope
- Chaining Methods
- Rbenv
- Sorting Algorithms
- method_missing
- send
- define_method
- Ruby DSL
- RuboCop
- Standard
- Inheritance
- Modules & Mixins
- Method Lookup

---

## 5. References

- [Ruby Roadmap](https://roadmap.sh/ruby)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Ruby On Rails