# Kotlin

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/kotlin
- Related Roles:
  - Android Developer

---

## 1. Beginner

### 1.1 Introduction to Kotlin
- **Why use Kotlin**
  - Kotlin is a modern programming language that makes coding easier and more efficient. It's designed to be simple to learn and use, helping developers write cleaner and more reliable code.
- **History of Kotlin**
  - Kotlin is a modern, statically typed programming language developed by JetBrains. It was initially conceived as a new language for the JVM, aiming to address some of the shortcomings of Java while maintaining full interoperability.
- **Java Interoperability**
  - Kotlin is 100% interoperable with the Java programming language, and major emphasis has been placed on making sure that your existing codebase can interact properly with Kotlin. You can easily call Kotlin code from Java and Java code from Kotlin.
- **Setting up the Environment**
  - Setting up the Kotlin environment involves installing the necessary tools and configuring your system to compile and run Kotlin code. This typically includes installing a Java Development Kit (JDK), downloading the Kotlin compiler, and optionally setting up an Integrated Development Environment (IDE) like IntelliJ IDEA or Android Studio with Kotlin plugins for a more streamlined development experience.

### 1.2 Code Organization
- **Code Organization**
  - In pure Kotlin projects, the recommended directory structure follows the package structure with the common root package omitted. For example, if all the code in the project is in the org.example.kotlin package and its subpackages, files with the org.example.kotlin package should be placed directly under the source root, and files in org.example.kotlin.network.socke t should be in the network/socket subdirectory of the source root.

### 1.3 main  Function
- **main  Function**
  - The main function serves as the entry point for a Kotlin program. When you execute a Kotlin application, the code within the main function is the first to be run.

### 1.4 Variables
- **val vs var**
  - In Kotlin, both val and var are used to declare variables, but they differ in mutability. A val variable is immutable, meaning its value cannot be changed after it's initially assigned.

### 1.5 Data types
- **Integers**
  - Integers in Kotlin are whole numbers without any fractional or decimal parts. Kotlin provides several integer types, each differing in the range of values they can represent.
- **Strings**
  - Strings in Kotlin represent sequences of characters. They are used to store and manipulate text.
- **Floats**
  - Floats in Kotlin represent single-precision (Float) and double-precision (Double) floating-point numbers, used to store numbers with decimal points. Float uses 32 bits of memory, offering a smaller range and precision, while Double uses 64 bits, providing a larger range and higher precision.
- **Unsigned Integers**
  - Unsigned integers in Kotlin are data types that represent whole numbers that cannot be negative. Unlike regular integers (like Int), unsigned integers (like UInt) only store positive values and zero.
- **Type Inference**
  - Kotlin, a statically typed language, introduces type inference to enhance code readability and reduce redundancy, making coding simpler without losing type safety. With Kotlin type inference, the Kotlin compiler automatically deduces types in various contexts, saving developers from explicitly declaring them each time.
- **Type Checks & Casts**
  - Kotlin allows you to check the type of a variable at runtime using the is operator. This operator returns true if a variable is of a certain type.
- **Characters**
  - Characters in Kotlin represent single symbols, like letters, numbers, or punctuation marks. They are denoted by the Char type and are enclosed in single quotes (e.g., 'A', '7', '$').

### 1.6 Comments
- **Arrays**
  - Arrays in Kotlin are used to store a fixed-size, sequential collection of elements of the same data type. Think of them as a container that holds multiple values of the same kind, like a list of integers, strings, or even custom objects.
- **Booleans**
  - Booleans represent truth values: either true or false. They are fundamental for decision-making in code, allowing programs to execute different blocks of code based on whether a condition is met.

### 1.7 Collections
- **Lists**
  - Lists in Kotlin are ordered collections of items. They can contain elements of the same type, and you can access these elements by their index (position) in the list.
- **Maps**
  - Maps are data structures that store collections of key-value pairs, where each key is unique. They allow you to efficiently retrieve a value based on its associated key.
- **Sets**
  - Sets in Kotlin are unordered collections of unique elements. This means a set cannot contain duplicate values.
- **read-only vs mutable**
  - Kotlin distinguishes between read-only and mutable collections. Read-only collections provide methods to access data but not to modify it, ensuring data integrity.
- **Iterators**
  - Iterators are objects that allow you to traverse through the elements of a collection (like a list or a set) one by one. They provide a way to access each item in the collection sequentially without needing to know the underlying structure of the collection.

### 1.8 Ranges
- **Ranges**
  - Ranges in Kotlin define an interval of values. You can create them using the ..

### 1.9 Progressions
- **Progressions**
  - Progressions in Kotlin define a sequence of values within a specific range, typically with a defined step. They are most commonly used with numeric types like Int, Long, and Char.

### 1.10 Printing data
- **print & println**
  - In Kotlin, print and println are fundamental functions used to display output to the console. The print function displays its argument without adding a newline character at the end, meaning subsequent output will appear on the same line.
- **String Templates**
  - String templates in Kotlin allow you to embed variables and expressions directly within strings. Instead of using string concatenation, you can include variables by prefixing them with a dollar sign ($).

### 1.11 Sequences
- **Sequences**
  - Sequences in Kotlin provide a way to perform operations on collections of data in a lazy manner. Instead of processing each element immediately, sequences evaluate operations only when the final result is needed.

### 1.12 Conditional Expressions
- **if**
  - To use if in Kotlin, add the condition to check within parentheses () and the action to take if the result is true within curly braces {}. You can use else and else if for additional branches and checks.
- **when**
  - In Kotlin, the when expression is a powerful control flow statement used to execute different blocks of code based on different conditions. It's similar to a switch statement in other languages, but more flexible and expressive.

### 1.13 Loops
- **for**
  - The for loop in Kotlin is used to iterate over a range, collection, or any other iterable object. It executes a block of code for each element in the sequence.
- **Label Loops**
  - Label loops in Kotlin allow you to control which loop is exited or continued when using break or continue statements within nested loops. By assigning a label (an identifier followed by @) to a loop, you can specify which loop the break or continue statement should affect.
- **while**
  - In Kotlin, while and do-while loops are used to repeatedly execute a block of code based on a condition. The while loop checks the condition before each execution of the block; if the condition is true, the block executes, and the process repeats.
- **break & continue**
  - In Kotlin, break and continue are control flow statements used within loops. The break statement immediately terminates the loop's execution and transfers control to the next statement after the loop.

### 1.14 Exceptions
- **Throwing Exceptions**
  - Throwing exceptions indicate when a problem occurs. You can manually throw exceptions with the throw keyword.
- **Catching Exceptions**
  - Catching exceptions handle the unexpected exception manually by resolving the issue or notifying the developer or application user. When an exception is thrown, it interrupts the normal execution of the program.

### 1.15 Standard functions
- **parameters**
  - Function parameters are values that you pass into a function when you call it. These parameters act as inputs, allowing the function to operate on different data each time it's invoked.
- **varargs**
  - Varargs (variable arguments) in Kotlin allow a function to accept a variable number of arguments of the same type. Instead of defining multiple function overloads for different numbers of arguments, you can use the vararg keyword in the function's parameter list.
- **return**
  - In Kotlin, the return statement is used within a function to stop its execution and send a value back to the caller. The value returned must match the function's declared return type.

### 1.16 Local Functions
- **Local Functions**
  - Local functions in Kotlin are functions defined inside another function. They provide a way to organize and reuse code within a specific function's scope.

---

## 2. Intermediate

### 2.1 Member Functions
- **Member Functions**
  - Member functions, also known as methods, are functions that are defined inside a class. They operate on the data of that class and can access its properties.

### 2.2 Tail-recursive Functions
- **Tail-recursive Functions**
  - Kotlin supports a style of functional programming known as tail recursion. For some algorithms that would normally use loops, you can use a recursive function instead without the risk of stack overflow.

### 2.3 Function Types
- **Lambda Functions**
  - Lambda functions in Kotlin are essentially nameless functions that you can treat like values. Think of them as mini-functions you can pass around, store in variables, or execute directly.
- **Higher-order Functions﻿**
  - Higher-order functions in Kotlin are functions that can take other functions as arguments, return functions, or both. This means you can pass a function into another function, treat functions like any other data type (like integers or strings), and even create functions that generate and return new functions.
- **Anonymous Functions**
  - Anonymous functions in Kotlin are functions without a name. They are defined using a lambda expression but with an explicit return type and the return keyword for returning values.
- **Transformations**
  - Transformations in Kotlin collections involve modifying the elements within a collection to create a new collection. These operations allow you to apply a function to each element, changing its value or structure, without altering the original collection.

### 2.4 Extension Functions
- **Retrieving Collection Parts**
  - The Kotlin standard library contains extension functions for retrieving parts of a collection. Functions like slice(),take(),drop(), and chunked(), provide a variety of ways to select elements for the result collection: listing their positions explicitly, specifying the result size, and others.
- **Filtering**
  - Filtering in Kotlin collections involves selecting elements from a collection based on a specific condition. This process creates a new collection containing only the elements that satisfy the given predicate, leaving the original collection unchanged.
- **Retrieving single elements**
  - Kotlin collections provide a set of functions for retrieving single elements from list and sets. You can select single elements by position, by condition, with selectors, and even using random selection.
- **plus & minus Operators**
  - The plus and minus operators in Kotlin collections provide a concise way to create new collections by adding or removing elements from existing ones. The plus operator (+) combines two collections or adds a single element to a collection, returning a new collection containing all elements.
- **Ordering**
  - Ordering in Kotlin collections involves arranging the elements within a collection (like lists or sets) based on a specific criterion. This can be done in ascending or descending order, either using the natural ordering of the elements themselves (if they are comparable) or by providing a custom comparison function that defines how the elements should be compared.
- **Grouping**
  - Grouping in Kotlin involves organizing elements from a collection into subgroups based on a specific criterion. This operation creates a map where the keys represent the grouping criteria, and the values are lists of elements that satisfy that criteria.
- **Aggregate Operations**
  - Aggregate operations in Kotlin collections transform a collection into a single result. These operations combine the elements of a collection using a specific function.

### 2.5 Defining Classess
- **Lists**
  - Kotlin lists offer several operations beyond the general collection operations. These include accessing elements by index (using get() or the [] operator), adding or removing elements at specific positions (using add() or removeAt()), and finding the index of a particular element (using indexOf() or lastIndexOf()).
- **Maps**
  - Maps in Kotlin are collections that hold key-value pairs. Map-specific operations allow you to interact with these pairs in targeted ways.
- **Sets**
  - Sets in Kotlin, like in mathematics, are collections of unique elements. Kotlin provides specific operations to manipulate these sets, including union (combining two sets), intersect (finding common elements), and subtract (finding elements present in one set but not the other).

### 2.6 Creating Instances
- **Properties**
  - Properties in Kotlin classes are variables declared directly inside a class. They represent the state of an object.

### 2.7 Class Members
- **Constructors**
  - Constructors in Kotlin are special member functions within a class that are used to initialize objects of that class. They define how an object is created and what initial values its properties will have.
- **Methods**
  - Methods in Kotlin classes are functions defined within the class that operate on the class's data (properties). They define the behavior of objects created from the class.
- **Nested & Inner Classes**
  - Kotlin allows you to define classes inside other classes. A nested class is declared inside another class but doesn't have access to the outer class's instance.
- **Object Declarations**
  - Object declarations in Kotlin provide a way to define a singleton object. This means you create a class and simultaneously declare a single instance of it.

### 2.8 Inheritance
- **Inheritance**
  - Inheritance in Kotlin allows you to create new classes (child classes or subclasses) based on existing classes (parent classes or superclasses). The child class inherits properties and functions from the parent class, and can also add its own unique properties and functions or override the parent's behavior.

### 2.9 Extension Functions
- **Extension Functions**
  - Extension functions in Kotlin provide a way to add new functions to existing classes without inheriting from them or using any type of design pattern such as Decorator. This is achieved by defining a function that can be called as if it were a member of the class, even though it's defined outside of the class's original declaration.

### 2.10 Visibility Modifiers
- **Visibility Modifiers**
  - Visibility modifiers control the accessibility of classes, objects, interfaces, constructors, properties, and functions in Kotlin. They determine from where these declarations can be accessed.

### 2.11 Property Delegates
- **Abstract Class**
  - An abstract class in Kotlin is a class that cannot be instantiated directly. It's designed to be a blueprint for other classes.
- **Interfaces**
  - Interfaces in Kotlin are blueprints for classes, defining a set of properties and abstract methods that implementing classes must provide. They allow you to define a contract, ensuring that any class implementing the interface will have specific functionalities.

### 2.12 Coroutines
- **Nullable vs Non-nullable**
  - In Kotlin, the type system distinguishes between variables that can hold null values (nullable types) and those that cannot (non-nullable types). By default, variables are declared as non-nullable, meaning they must always contain a value.
- **Nullability Check Operators**
  - Nullability check operators in Kotlin are tools that allow you to safely handle variables that might contain null values. They provide a concise way to access properties or call methods on nullable variables, preventing NullPointerException errors at runtime.
- **What is Null Safety?**
  - Null safety is a feature that helps prevent null pointer exceptions, a common cause of program crashes. Kotlin distinguishes between nullable and non-nullable types.
- **Safe Casts**
  - Safe casts in Kotlin provide a way to convert a variable of one type to another, but unlike regular casts, they handle the possibility of the cast failing gracefully. Instead of throwing a ClassCastException if the cast is not possible, a safe cast returns null.

### 2.13 Suspending Functions
- **Suspending Functions**
  - Suspending functions are the foundation of Kotlin's coroutine-based concurrency. They represent a computation that can be paused and resumed later, potentially without blocking the thread.

### 2.14 Coroutines Builders
- **Coroutines Builders**
  - Coroutine builders in Kotlin are functions that start a new coroutine. They bridge the gap between regular, blocking code and the non-blocking, concurrent world of coroutines.

### 2.15 Understanding Packages
- **Understanding Packages**
  - Packages are namespaces that organize related classes, interfaces, functions, and other declarations in Kotlin. They provide a way to group code logically, prevent naming conflicts, and control visibility.

### 2.16 Coroutines Behavior
- **Coroutines Behavior**
  - Launching a coroutine from a CoroutineScope creates a context that governs its execution. Builder functions like .launch() and .async() automatically create a set of elements that define how the coroutine behaves, including the Job interface, which tracks the coroutine's lifecycle and enables structured concurrency; CoroutineDispatcher, which controls where the coroutine runs; and CoroutineExceptionHandler, which handles uncaught exceptions.

### 2.17 Asynchronous Flow
- **Asynchronous Flow**
  - Asynchronous Flow in Kotlin is a feature built upon coroutines that allows you to represent a stream of data that is computed asynchronously. It's designed to handle sequences of values emitted over time, enabling you to perform operations on each emitted value in a non-blocking manner.

### 2.18 Coroutines Best practices
- **Test Library**
  - kotlin.test is a library in Kotlin that provides a set of tools and functions for writing and running unit tests. It allows developers to verify that their code behaves as expected by defining test cases and assertions.
- **Coroutines**
  - Kotlin Coroutines provide a way to write asynchronous, non-blocking code in a sequential style. They allow you to perform long-running tasks, like network requests or database operations, without blocking the main thread, thus preventing your application from becoming unresponsive.
- **Serialization**
  - Serialization is the process of converting an object's state into a format that can be stored or transmitted, and then reconstructed later. This allows you to save data to a file, send it over a network, or store it in a database, and then recreate the original object from that stored representation.

### 2.19 Importing Packages
- **Data Classes**
  - Data classes in Kotlin are special classes designed to hold data. The compiler automatically generates useful methods like equals(), hashCode(), toString(), componentN() functions (for destructuring), and copy() for you.
- **Sealed Class**
  - A sealed class in Kotlin represents a restricted class hierarchy. It's used when a value can have one of a limited set of types, but no other types.
- **Class Generics**
  - Generics in Kotlin allow you to define classes that can work with different types of data without specifying those types upfront. Think of it like a template for a class.
- **Enum Class**
  - An enum class in Kotlin is a special type of class that represents a fixed set of possible values, often called "enumerations". Think of it like a list of named constants.
- **Inline Class**
  - An inline class in Kotlin is a special type of class that holds only one property. At runtime, instances of inline classes are represented as the underlying value, avoiding the overhead of object allocation.
- **Type Aliases**
  - A type alias in Kotlin provides an alternative name for an existing type. It doesn't create a new type; instead, it introduces a new identifier that you can use interchangeably with the original type.

### 2.20 Standard Library
- **Default Imports**
  - Default imports are a set of pre-defined classes, functions, and interfaces that are automatically available in every Kotlin file without needing explicit import statements. These imports provide access to commonly used functionalities, reducing boilerplate code and making development more convenient.
- **Opt-in Requirements**
  - Opt-in requirements in Kotlin provide a mechanism to enforce that certain APIs or code constructs are used only when the developer explicitly acknowledges and understands the associated risks or special conditions. This is achieved by marking APIs with annotations that require explicit opt-in, forcing users to acknowledge the usage by adding an @OptIn annotation or compiler argument.

### 2.21 Kotlin Libraries
- **Kotlin Libraries**
  - Kotlin benefits from a rich ecosystem of libraries, both those specifically designed for Kotlin and those written in Java. This interoperability allows Kotlin developers to seamlessly use existing Java libraries.

---

## 3. Advanced

### 3.1 Documentation
- **I/O Library**
  - Kotlin leverages both its own kotlin.io package and the standard Java java.io package for input and output operations. kotlin.io provides a set of extension functions and utilities that simplify common I/O tasks, offering a more Kotlin-idiomatic way to interact with files, streams, and the console.
- **Date & Time**
  - Kotlin leverages Java's java.time package (introduced in Java 8) for handling dates and times, offering classes like LocalDate, LocalTime, and LocalDateTime. Kotlin also provides extensions and convenience functions within its standard library, such as the kotlinx.datetime library, to work with dates and times.
- **Dokka**
  - Dokka is a documentation engine for Kotlin, similar to Javadoc for Java. It generates API documentation in various formats (like HTML, Markdown, and more) from Kotlin source code.
- **KDoc**
  - KDoc is Kotlin's documentation generation tool, similar to Javadoc for Java. It allows developers to embed documentation directly within their code, using a specific syntax to describe classes, functions, properties, and other elements.

### 3.2 Build Tools
- **Gradle**
  - Gradle is an open-source build automation tool known for its flexibility and performance. It's used to automate tasks like compiling, testing, and deploying software.
- **JVM Metadata**
  - The kotlin-metadata-jvm library provides tools to read, modify, and generate metadata from Kotlin classes compiled for the JVM. This metadata, stored in the @Metadata annotation within .class files, is used by libraries and tools such as kotlin-reflect to inspect Kotlin-specific constructs such as properties, functions, and classes at runtime.
- **Gradle Pluggins**
  - Gradle plugins are reusable components that extend Gradle's build capabilities. They automate tasks like compiling code, running tests, and packaging applications.
- **Maven**
  - Maven is a powerful build automation tool primarily used for Java projects, but it also works seamlessly with Kotlin. It simplifies dependency management by allowing you to declare external libraries your project needs, and Maven automatically downloads and includes them.

### 3.3 CI/CD Tools
- **TeamCity**
  - TeamCity is a powerful and flexible continuous integration and continuous delivery (CI/CD) server developed by JetBrains. It automates the processes of building, testing, and deploying software, allowing development teams to streamline their workflows and deliver high-quality products faster.

### 3.4 IDEs
- **IntelliJ IDEA**
  - IntelliJ IDEA is a popular Integrated Development Environment (IDE) specifically designed for software development. It provides a comprehensive suite of tools for coding, debugging, testing, and deploying applications.
- **Android Studio**
  - Android Studio is the official Integrated Development Environment (IDE) for Android app development, built on JetBrains' IntelliJ IDEA. It provides a comprehensive suite of tools for designing, developing, debugging, and testing Android applications.
- **Kotline Notebook**
  - Kotlin Notebook is an interactive environment for writing and executing Kotlin code, similar to Jupyter Notebook for Python. It allows you to combine code, text, and visualizations in a single document, making it ideal for data exploration, prototyping, and creating interactive tutorials.

### 3.5 I/O
- **Build Tool API**
  - The Build Tool API in Kotlin provides a way for build tools like Gradle or Maven to interact with the Kotlin compiler and related tooling. It allows these tools to configure the compilation process, access compiler options, and integrate Kotlin code into the overall build lifecycle.
- **Writing & Reading Files**
  - Writing and reading files in Kotlin involves using classes from the java.io package. To write to a file, you typically create a File object and then use classes like FileWriter or BufferedWriter to write data.
- **Buffered Streams**
  - Buffered streams in Kotlin enhance the efficiency of reading from and writing to data sources. Instead of directly interacting with the underlying input or output stream for every read or write operation, buffered streams use an internal buffer.
- **Creating Files**
  - In Kotlin, you can create new files using the File class from the java.io package. To do this, you first create a File object representing the desired file path.

### 3.6 Kotlin Multiplatform
- **Compose Multiplatform**
  - Compose Multiplatform is a declarative UI framework that allows developers to share user interface code across multiple platforms, including Android, iOS, desktop (Windows, macOS, Linux), and web. It's based on Jetpack Compose, Google's modern UI toolkit for Android, and leverages Kotlin's multiplatform capabilities to enable code reuse while maintaining a native look and feel on each target platform.

### 3.7 Kotlin/Java
- **Java from Kotlin**
  - Kotlin is designed to be fully interoperable with Java, meaning you can seamlessly use existing Java code within your Kotlin projects. This allows you to leverage existing Java libraries, frameworks, and codebases without needing to rewrite them in Kotlin.
- **Kotlin from Java**
  - Kotlin from Java refers to the process of using Kotlin code within existing Java projects. It allows developers to gradually introduce Kotlin into their codebase without requiring a complete rewrite.
- **Spring Boot**
  - Spring Boot simplifies building Java applications by providing auto-configuration and a streamlined setup process. When used with Kotlin, it allows developers to leverage Kotlin's concise syntax, null safety, and modern features within the familiar Spring ecosystem.

### 3.8 Kotlin/Native
- **C Interoperability**
  - C Interoperability in Kotlin/Native allows Kotlin code to interact with C libraries and code. This means you can use existing C libraries within your Kotlin/Native projects, and also expose Kotlin/Native code to be used from C.
- **Swift/Objective-C Interop.**
  - Kotlin/Native allows you to use Swift and Objective-C code directly in your Kotlin projects, and vice versa. This means you can leverage existing iOS libraries and frameworks within your Kotlin/Native code, and also expose Kotlin code to be used in Swift/Objective-C projects.

### 3.9 Kotlin/WASM
- **Kotlin/WASM**
  - Kotlin/WASM allows you to compile Kotlin code to WebAssembly (WASM), a binary instruction format designed for efficient execution in web browsers and other environments. This enables Kotlin developers to build high-performance applications that can run directly in the browser, leveraging Kotlin's features and tooling for web development.

### 3.10 Kotlin/JavaScript
- **Kotlin/JavaScript**
  - Kotlin/JavaScript (Kotlin/JS) allows you to compile Kotlin code into JavaScript. This enables you to use Kotlin to develop web applications, Node.js applications, and other JavaScript-based projects.

### 3.11 Kotlin Scripting
- **Spring**
  - Spring is a popular, open-source application framework for building robust and scalable Java applications. It provides a comprehensive infrastructure support for developing enterprise applications, handling concerns like dependency injection, aspect-oriented programming, data access, and transaction management.
- **Vert.x**
  - Vert.x is a toolkit for building reactive applications on the JVM. It provides a non-blocking, event-driven concurrency model, making it well-suited for building scalable and high-performance server-side applications.

### 3.12 Server-side Apps
- **Android SDK**
  - The Android SDK (Software Development Kit) is a set of tools, libraries, documentation, and sample code provided by Google that allows developers to create applications for the Android operating system. It provides the necessary APIs and development environment to build, test, and debug Android apps.
- **Android Studio**
  - Android Studio is the official Integrated Development Environment (IDE) for Android app development, and it fully supports Kotlin. It provides tools for coding, debugging, testing, and designing user interfaces for Android applications.
- **Android Jetpack**
  - Android Jetpack is a suite of libraries, tools, and architectural guidance designed to help developers build robust, testable, and maintainable Android applications more easily. It addresses common Android development challenges by providing pre-built components for tasks like managing UI, data persistence, background processing, and navigation, allowing developers to focus on writing unique application logic.
- **Ktor**
  - Ktor is a framework for building asynchronous server-side applications, client applications, and more, in connected systems. It's built using Kotlin and coroutines, providing a simple and efficient way to handle concurrency and build scalable network applications.
- **Quarkus**
  - Quarkus provides first class support for using Kotlin. The framework is open source and maintained by Red Hat.

### 3.13 Data Analysis
- **Kotlin Notebooks**
  - Kotlin Notebooks provide an interactive environment for writing and executing Kotlin code, often within a web browser. They allow you to combine code, text, and visualizations in a single document, making them ideal for exploring data, prototyping ideas, and creating shareable reports.
- **Kotlin DataFrame**
  - Kotlin DataFrame is a library designed for in-memory data manipulation and analysis. It provides a tabular data structure, similar to data frames in R or Python's Pandas, allowing you to organize data into columns of different types.
- **Kandy**
  - Kandy is a Kotlin library designed for creating visualizations and performing data analysis. It provides a concise and expressive API for generating plots and charts directly from Kotlin code.

### 3.14 Competitive Programming
- **Competitive Programming**
  - Kotlin can be used for competitive programming due to its concise syntax, standard library, and interoperability with Java. It allows programmers to write efficient and readable code, which is crucial for solving algorithmic problems quickly.

### 3.15 AI Development
- **Koog**
  - Koog is a Kotlin library designed to simplify the development of AI applications. It provides tools and abstractions for tasks such as neural network creation, training, and inference.

---

## 4. Optional / Specialized Topics

- Type Inference
- Type Checks & Casts
- Characters
- Iterators
- Ordering
- Grouping
- Aggregate Operations
- Inline Class
- Type Aliases
- Quarkus

---

## 5. References

- [Kotlin Roadmap](https://roadmap.sh/kotlin)

---

## 6. Related Roles / Topics

### Related Roles
- Android Developer

### Related Skills
- Python
- Go
- Rust
- Java
- JavaScript
- TypeScript
- Php
- Node.js