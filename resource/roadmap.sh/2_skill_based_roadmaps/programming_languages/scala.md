# Scala

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/scala
- Related Roles:
  - Data Analyst
  - Data Engineer

---

## 1. Beginner

### 1.1 Introduction
- **Docs**
  - Scala's official documentation is a fantastic place to start learning the language and its features. It provides comprehensive guides, tutorials, and API references that cover everything from basic syntax to advanced concepts.
- **Courses**
  - Courses offer a structured learning path, typically designed by experts, that guides you through the fundamentals to advanced concepts. They often include hands-on exercises, projects, and assessments to reinforce learning and provide practical experience.
- **Books**
  - Books offer a structured and comprehensive way to learn a new programming language. They typically cover fundamental concepts in detail, building upon previous knowledge to provide a solid understanding.
- **YouTube**
  - YouTube can be a fantastic resource for learning Scala. On the platform, you can find a wide variety of content, from beginner-friendly tutorials introducing basic concepts to in-depth explanations of advanced topics.

### 1.2 Setting Up Scala
- **IntelliJ IDEA**
  - IntelliJ IDEA is a popular integrated development environment (IDE) that offers support for Scala through its Scala Plugin. This plugin provides essential features for Scala development, including code completion, refactoring, debugging, and seamless integration with build tools like sbt and Maven.
- **Integers**
  - Integers are whole numbers, meaning they don't have any fractional or decimal parts. In Scala, integers can be positive (like 5), negative (like -10), or zero (0).
- **Strings**
  - Strings represent sequences of characters. They're used to store and manipulate text.
- **Booleans**
  - Booleans represent truth values: either true or false. They are fundamental for decision-making in programs, allowing you to control the flow of execution based on conditions.
- **Float**
  - Floats in Scala are used to represent numbers with decimal points. They are like regular numbers but can have a fractional part, such as 3.14 or -2.7.

### 1.3 Variables & Constants
- **VS Code**
  - Visual Studio Code (VS Code) is a popular IDE known for its lightweight design and extensive customization options. When equipped with the Metals extension, VS Code becomes a powerful tool for Scala development, offering features like code completion, refactoring, debugging, and integration with build tools like sbt and Maven.
- **Vim**
  - Vim is a highly configurable text editor known for its efficiency and features. When equipped with the Metals plugin, Vim becomes a capable environment for Scala development, offering features like code completion, refactoring, and debugging.
- **Emacs**
  - Emacs is a highly extensible and customizable text editor known for its features and flexibility. When equipped with the Metals plugin, Emacs becomes a robust environment for Scala development, offering features like code completion, refactoring, and debugging.
- **Unit**
  - Unit is a data type in Scala that represents a placeholder when no meaningful value needs to be returned. It's similar to void in languages like Java or C.
- **Nothing**
  - Nothing is a special type in Scala that sits at the bottom of the type hierarchy. It's a subtype of every other type, meaning it can be used anywhere any other type is expected.

### 1.4 Operators
- **Zed**
  - Zed is a modern, lightweight, and highly performant code editor designed for efficiency and ease of use. It offers features like real-time collaboration, a minimalistic interface, and editing capabilities.
- **Sublime**
  - Sublime Text is a sophisticated text editor known for its speed, ease of use, and features. It supports a wide range of programming languages, including Scala, through plugins and packages.
- **Type Hierarchy**
  - Generic types allow you to write code that can work with different types while maintaining type safety. Generic classes and traits take a type as a parameter within square brackets.

### 1.5 Conditionals
- **Type Parameters**
  - Type parameters are used to create generic classes, traits, and methods. Type parameters are enclosed in square brackets and can be used to define methods and classes that work with different types while maintaining type safety.

### 1.6 Data Structures
- **Class**
  - A class is a blueprint for creating objects. Classes can contain methods, values, variables, types, objects, and traits.
- **Trait**
  - A trait is a type that defines a contract of fields and methods, which can be either abstract (unimplemented) or concrete (implemented). Traits are used to share behavior across classes, enabling code reuse without relying on single inheritance.
- **Object**
  - The object keyword is used to create a singleton object. A singleton object is a class that has only one instance.
- **Conversions**
  - Implicit conversions allow the compiler to automatically convert one type to another in certain situations. In Scala 3, implicit conversions are defined by a given instance of type scala.Conversion\[S, T\], where S is the source type and T is the target type.

### 1.7 Loops
- **Loops**
  - Loops are used to execute a block of code repeatedly. Scala supports the following types of loops.

### 1.8 Try/Catch
- **Mutable Collections**
  - Mutable collections are used when you need collections that can be updated or extended in place, usually for better performance. After the computations are done, you can transform it to its immutable counterpart.
- **Array**
  - An array is a fixed-size data structure that stores elements of the same data type. Arrays in Scala are mutable, meaning their elements can be updated.
- **Seq**
  - A Seq in Scala represents an ordered collection of elements. Think of it like a list where the order in which you add items matters.
- **Range**
  - A Range in Scala represents an ordered sequence of integers (or other numeric types) with a consistent step size. You define a range by specifying its start, end (inclusive or exclusive), and the increment between elements.
- **List**
  - Lists are ordered, immutable collections of elements of the same type. Once a list is created, you can't change its elements directly; instead, you create a new list with the desired modifications.
- **Vector**
  - Vectors in Scala are indexed, immutable sequences. Think of them as similar to arrays, but with the key advantage of being immutable – meaning their contents cannot be changed after creation.
- **Set**
  - A Set in Scala is a collection that holds unique elements. This means no duplicates are allowed.
- **Map**
  - A Map is a collection that holds key-value pairs. Think of it like a dictionary where each key is associated with a specific value.
- **Functions & Methods**
  - Functions and methods are fundamental building blocks for organizing and reusing code. A function is essentially a block of code that performs a specific task.
- **Method Calls**
  - Method calls can be made using different syntaxes and conventions. Methods can be called using the standard dot notation (e.g., obj.method(params)) or using the infix notation (e.g., obj method params).
- **Anonymous Func / Lambda**
  - Anonymous functions, also known as lambdas, are functions without names. You define them inline where you need them, typically to pass them as arguments to other functions.
- **Case Classes**
  - Case classes are a special type of class that is particularly useful for modeling immutable data. They provide several conveniences over regular classes, including immutability, several synthetic methods like toString, equals, and copy, as well as synthetic apply and unapply methods, which make case classes very useful for pattern matching.
- **Sealed Traits**
  - Sealed traits are used to define closed hierarchies where all possible subclasses are known. They can be extended only in the same file as their declaration, allowing the compiler to perform exhaustiveness checking.
- **apply Method**
  - The apply function is a so-called smart constructor. It's the most popular way in Scala to create new instances of data types.
- **Enums**
  - In Scala 3, enums are used to define a type consisting of a set of named values. They provide a more concise and safer way to define enumerations compared to the traditional Enumeration class in Scala 2.

### 1.9 Working with Strings
- **Total/Partial Funcs**
  - A total function is a function that is defined for every possible input value it can be given. In contrast, a partial function is a function that is only defined for a subset of possible input values.
- **Funcs returning Funcs**
  - In Scala, functions can return other functions. Currying is the process of converting a function with multiple arguments into a sequence of functions that take one argument each.
- **Regex**
  - Regular expressions are supported through the Regex class in the scala.util.matching package. Regular expressions (regex) are patterns used to match character combinations in strings.

### 1.10 Pattern Matching
- **collect / collectFirst**
  - The collect and collectFirst methods are used to apply a partial function to elements of a collection. The collect method takes a partial function as its parameter and applies it to all the elements in the collection to create a new collection.
- **find**
  - The find method is used on collections (like Lists, Sets, or Maps) to locate the first element that satisfies a given condition. You provide find with a function that checks each element, and if the function returns true for an element, find immediately returns Some(element).
- **filter**
  - The filter method in Scala collections lets you pick out the elements you want based on a condition. You give it a function that takes an element and returns true if you want to keep it, and false if you want to discard it.
- **flatMap**
  - The flatMap method is used to apply a function to each element of a collection and then flatten the results into a new collection. It is essentially a combination of the map method followed by the flatten method, but this seemingly very simple property makes it fundamental for Functional Programming.
- **foldLeft**
  - The foldLeft method is used to produce a single result by "folding" all the elements of a collection. The algorithm starts with a "zero" element which is paired with the first element of the collection to create an intermediate result element.
- **foreach**
  - The foreach method is used to apply a function to each element of a collection for its side effects. Unlike methods like map or filter, foreach does not return a value; it is used primarily for operations that have side effects, such as printing elements or modifying external state.
- **map**
  - The map method is used to apply a function to each element of a collection and create a new collection with the same number of elements, where each element is the result of applying that function to the original element. Resources
- **Case Objects**
  - Case objects are similar to regular Scala objects but with additional features that they share with case classes - immutable and with synthetic methods. They are often used for creating singleton objects and are particularly useful in pattern matching and message passing.
- **unapply Method**
  - The unapply method is used to deconstruct instances through pattern matching. It is often used in extractor objects to extract data values compacted in objects.
- **for comprehension**
  - For-comprehensions in Scala are used to evaluate expressions and return a sequence of values. They have the form for (enumerators) yield e, where enumerators refer to a list of enumerators.

---

## 2. Intermediate

### 2.1 Error Handling
- **Option**
  - The Option class in Scala is used to represent optional values. It is a carrier of single or no element for a stated type, and is particularly useful for handling cases where a value might be null.
- **Either**
  - The Either class in Scala is used to represent a value of one of two possible types (a disjoint union). An instance of Either is either an instance of scala.util.Left or scala.util.Right.
- **Try**
  - The Try class in Scala represents a computation that may fail during evaluation by raising an exception. It holds either a successfully computed value or the exception that was thrown.

### 2.2 Laziness
- **Lazy vals**
  - Lazy vals are used to defer the initialization of a variable until it is accessed for the first time. This can be useful for optimizing performance and avoiding unnecessary computations.
- **by-name Parameters**
  - By-name parameters are defined using the => symbol before the parameter type. Such a parameter will be evaluated only when it is used inside the method's body.
- **Lazy Collections**
  - Lazy collections are used to describe successive transformation operations without evaluating intermediate transformations. They are particularly useful for creating infinite collections without blowing the memory.

### 2.3 Scope & Visibility
- **private / protected**
  - The private and protected keywords are used to control the visibility of members (variables and methods) in classes, objects, or packages. If no access modifier is specified, the default access level is public.
- **package**
  - The package keyword is used to create namespaces that can contain entities such as classes, objects, and other packages. In Scala 2, package objects allow defining functions, variables, and types that are accessible to all members of a package.
- **Iterators**
  - An iterator is a mechanism to access a collection's elements sequentially in a performant way. They are often used in loops.
- **Views**
  - Views are used to create lazy versions of collections. They are essentially reusable iterators that implement the same interfaces as regular collections.
- **LazyList**
  - A lazy list is an immutable linked list that computes its elements only when they are needed. Elements are memoized, meaning the value of each element is computed at most once.

### 2.4 Recursion
- **Tail Recursion**
  - Tail recursion is a special form of recursion where the recursive call is the last operation in the function. This allows the Scala compiler to optimize the recursion to prevent stack overflow and improve performance.
- **Trampolines**
  - Trampolines in Scala are used to avoid stack overflow errors in deep recursion by moving the computation from the stack to the heap. The TailRec class is part of the scala.util.control.TailCalls are used to implement trampolining.
- **Implicit Parameter**
  - Implicit parameters are passed to functions without having to explicitly specify them at the call site. This can make your code more concise and readable, especially when dealing with common or boilerplate code.
- **Early returns**
  - This topic brings together several concepts you have already encountered: pattern matching, partial functions, the apply and unapply methods, and lazy collections. Its purpose is to let you see how they work together.

### 2.5 Build Tools
- **ScalaCLI**
  - ScalaCLI is a command-line tool designed to simplify the process of learning and using Scala. It is optimized for speed and ease of use, making it ideal for scripts, playgrounds, and single-module projects.
- **ZIO**
  - ZIO is a Scala framework designed for asynchronous and concurrent programming. It emphasizes type safety, composability, and resource safety, making it suitable for building scalable and resilient applications.

### 2.6 Ecosystems
- **sbt**
  - sbt (Scala Build Tool) is a build tool designed for Scala and Java projects. It allows developers to define tasks in Scala and run them in parallel from an interactive shell.
- **Mill**
  - Mill is a build tool designed for Java, Scala, and Kotlin projects. It focuses on speed and efficiency by automatically caching and parallelizing build tasks and tests.
- **Cats**
  - Cats provides core abstractions for functional programming in Scala. It aims to be modular, approachable, and efficient, while providing a foundation for an ecosystem of pure, typeful libraries.
- **Li Haoyi**
  - The Li Haoyi ecosystem is centered around making Scala easy to use and productive. It includes libraries like Ammonite REPL, Mill Build Tool, os-lib, uPickle, Cask, and Scalatags.
- **Akka / Pekko**
  - Akka and Pekko are toolkits for building concurrent, distributed, and resilient applications on the JVM using Scala. Akka, originally developed by Lightbend, introduced an actor model for managing concurrency, inspired by Erlang.
- **No Ecosystem**
  - The Scala open-source landscape outside of the major ecosystems often focuses on niche use cases or innovative ideas that may not be covered by the larger frameworks. Projects in this space can range from specialized tools for data science, machine learning, and web development to unique solutions for testing, build management, and database connectivity.

### 2.7 Platforms
- **Gradle**
  - Gradle is widely used for building, testing, publishing, and deploying software packages. It is known for its flexibility and efficiency in managing dependencies and resolving version conflicts.
- **Maven**
  - Maven is a build automation and dependency management tool primarily used for Java projects. It simplifies the build process by using a Project Object Model (POM) file, typically named pom.xml, which centralizes project configuration and manages dependencies.
- **JVM**
  - Scala's primary platform is the Java Virtual Machine (JVM). Scala code is compiled into Java bytecode, allowing it to run on any device with a JVM, independent of the underlying machine configuration.
- **Scala Native**
  - Scala Native is an optimizing ahead-of-time compiler and lightweight managed runtime designed specifically for Scala. By leveraging LLVM, Scala Native compiles Scala code directly to native executables, eliminating the need for a Java Virtual Machine (JVM).

### 2.8 Referencial Transparency
- **Scala.js**
  - Scala.js is a Scala compiler that compiles Scala code to JavaScript, enabling Scala programs to run in web browsers or Node.js. It optimizes Scala code into highly efficient JavaScript, ensuring fast turnaround times with incremental compilation.
- **Pure Functions**
  - Pure functions in Scala are functions that always return the same output for the same input and do not have any side effects. They are fundamental to functional programming and provide predictability and reliability.

### 2.9 Monads
- **Category Theory**
  - Category Theory is a branch of mathematics that deals with structures and relationships between them. In the context of Scala and functional programming, Category Theory provides a framework for understanding and designing functional programs.

### 2.10 Capabilities
- **Capture Checking**
  - Capture Checking is an experimental feature in Scala that allows you to track which designated values are captured (i.e., stored as references) by arbitrary other values. This tracking happens at compile time and is currently an opt-in mechanism that can be enabled via an import.

### 2.11 Typeclasses
- **Typeclasses**
  - Typeclasses are a concept used in functional programming to achieve ad-hoc polymorphism. They define a set of functions that can be implemented for a type fulfilling certain requirements, providing a way to add functionality to existing types without modifying their source code.

### 2.12 Type System
- **Variance**
  - Context Bounds in Scala is a feature that provides a shorthand syntax for expressing the common pattern of a context parameter that depends on a type parameter. Context bounds are used to simplify the code for generic types and are particularly useful in the context of type classes.
- **Context Bounds**
  - Context Bounds in Scala is a feature that provides a shorthand syntax for expressing the common pattern of a context parameter that depends on a type parameter. Context bounds are used to simplify the code for generic types and are particularly useful in the context of type classes.

### 2.13 Macros
- **ScalaTest**
  - ScalaTest is a flexible and comprehensive testing framework for Scala. It integrates with various tools like JUnit, TestNG, Ant, Maven, sbt, ScalaCheck, and mocking frameworks such as Mockito and ScalaMock.
- **mUnit**
  - MUnit is a Scala testing library that offers actionable errors and extensible APIs. It is designed to provide clear and helpful error messages when tests fail, making it easier to debug and fix issues.
- **uTest**
  - uTest is a simple and convenient testing library for Scala. It provides essential features in their minimal form, avoiding unnecessary complexity.
- **JUnit**
  - JUnit is a popular open-source unit testing framework for Java. It is part of the xUnit family and is designed to help developers write and run repeatable tests.

---

## 3. Advanced

### 3.1 Testing
- **ScalaTest**
  - ScalaTest is a versatile testing framework for Scala that helps programmers write both integration and performance tests. For integration testing, ScalaTest allows you to test the interactions between different components of your application, such as APIs, databases, or services, ensuring they work together as expected.
- **Gatling**
  - Gatling is an open-source tool for performance and load testing, particularly well-suited for testing web applications. It is built on Scala, Akka, and Netty, and allows you to write test scenarios using expressive SDKs in Scala, Java, Kotlin, JavaScript, or TypeScript.
- **ZIO Test**
  - ZIO Test is a testing library for Scala that makes it easy to test effectual programs. It is tightly integrated with ZIO, allowing tests to be treated as immutable values, which simplifies testing asynchronous and concurrent code.
- **specs2**
  - specs2 is a library for writing executable software specifications in Scala. It allows you to write specifications for individual classes (unit specifications) or entire systems (acceptance specifications).
- **Scalatra**
  - Scalatra is a lightweight, Sinatra-like web framework for Scala. It is designed to be simple, accessible, and easy to use, making it a practical way to learn Scala and build high-performance websites and APIs.
- **Tapir**
  - Tapir is a library to describe HTTP APIs, expose them as a server, consume as a client, and automatically document using open standards. It is designed to be fast and developer-friendly, with a focus on type-safety, readability, and discoverability.

### 3.2 Backend
- **sttp**
  - sttp is an open-source HTTP client for Scala that provides a clean, programmer-friendly API to describe HTTP requests and handle responses. It supports various approaches to writing Scala code, including synchronous (direct-style), Future-based, and functional effect systems like cats-effect, ZIO, Monix, Kyo, and scalaz.
- **AkkaHTTP**
  - Akka HTTP is a modern, fast, asynchronous, and streaming-first HTTP server and client. It implements a full server- and client-side HTTP stack on top of akka-actor and akka-stream.
- **Play**
  - The Play Framework is an open-source web application framework that follows the model–view–controller (MVC) architectural pattern. It is written in Scala and usable from other programming languages that are compiled to JVM bytecode, such as Java.
- **http4s**
  - http4s is a minimal, idiomatic Scala interface for HTTP services. It is built on FS2, a streaming library that allows for processing and emitting large payloads in constant space and implementing websockets.

### 3.3 Effect Systems
- **Cats Effect**
  - Cats Effect is a high-performance, asynchronous, composable framework for building real-world applications in a purely functional style within the Typelevel ecosystem. It provides a concrete tool, known as "the IO monad," for capturing and controlling actions, often referred to as "effects," that your program wishes to perform within a resource-safe, typed context with seamless support for concurrency and coordination.
- **ZIO**
  - ZIO is a Scala framework for asynchronous and concurrent programming. It is designed to be type-safe, composable, and highly scalable, allowing developers to build safe applications.
- **Calico**
  - Calico is a pure, reactive UI library for Scala.js. It enables developers to build reactive web applications using Scala.js, integrating with libraries such as Cats Effect and FS2.
- **Laminar**
  - Laminar is a UI library for Scala.js that focuses on simplicity, expressiveness, and safety. It allows developers to build web application interfaces while keeping the UI state in sync with the underlying application state.

### 3.4 GUI
- **Slinky**
  - Slinky is a framework for writing React apps in Scala, providing an experience similar to using ES6. It allows developers to leverage Scala's type safety and functional programming features while building React applications.
- **React.js**
  - React.js is a popular JavaScript library for building user interfaces, developed and maintained by Facebook. It can be integrated with Scala.js, allowing developers to write React applications using Scala.
- **Ox**
  - Ox is a Scala library designed for safe direct-style streaming, concurrency, and resiliency on the JVM. It offers a comprehensive set of tools for managing concurrency, error handling, and resource management in a developer-friendly manner.
- **Gears**
  - Gears is an experimental asynchronous programming library for Scala 3. It is designed to enable direct-style programming, structured concurrency, and is cross-platform, working on both JVM >=21 and Scala Native.

### 3.5 Concurrency
- **ScalaFX**
  - ScalaFX is a UI DSL written within the Scala Language that sits on top of JavaFX. Every ScalaFX application is also a valid Scala application.
- **JavaFX**
  - JavaFX is a GUI toolkit for Java designed to create rich desktop applications with modern user interfaces. It provides a comprehensive set of UI controls, supports hardware-accelerated graphics, and can be used to build applications that run across multiple platforms, including web, desktop, and mobile.
- **FS2**
  - FS2 is a library for purely functional, effectful, and polymorphic stream processing in the Scala programming language. Its design goals are compositionality, expressiveness, resource safety, and speed.
- **Kyo**
  - Kyo is a toolkit for Scala development, providing a rich standard library for development across Native, JVM, and JavaScript platforms. It introduces a novel approach based on algebraic effects to deliver straightforward APIs in the pure Functional Programming paradigm.
- **Akka & Peko Streams**
  - Akka Streams, now succeeded by Pekko Streams, provide a powerful way to handle streams of data reactively and efficiently. These libraries offer tools to define data processing pipelines with backpressure, ensuring that data flows smoothly between components without overwhelming any part of the system.

### 3.6 Distributed Computing
- **GraalVM Native Image**
  - GraalVM Native Image is a tool that compiles Java applications into native binary executables using ahead-of-time (AOT) compilation. When used with Scala, it can significantly improve the performance and startup time of Scala applications by eliminating the need for a JVM at runtime.
- **scala-android-plugin**
  - The Scala Android Plugin is a tool that allows developers to build Android applications using the Scala programming language. It integrates with the Android build system, enabling you to write your application logic, activities, and UI components in Scala, and then compile them into Dalvik bytecode that can run on Android devices.
- **Scala on Android**
  - This is a repo for examples, small tutorials, and some chaotic notes on how to write Android apps with GraalVM, Gluon Mobile, JavaFX, and Scala.
- **ZIO Streams**
  - ZIO Streams is a purely functional streaming library that uses the ZIO runtime. It is designed for working with large or infinite data, providing automatic backpressure handling, non-blocking and asynchronous processing, and a rich set of stream combinators.
- **Spark**
  - Apache Spark is a framework for big data processing that integrates seamlessly with Scala. It provides a unified engine for various data processing tasks, including batch processing, interactive queries, streaming, machine learning, and graph processing.
- **Akka**
  - Akka is a suite of modules designed for building scalable, resilient, and distributed systems using the actor model. It simplifies concurrency and fault tolerance by providing a framework for handling asynchronous operations and message passing.

### 3.7 Data Handling
- **Pekko**
  - Pekko is an open-source framework for building applications that are concurrent, distributed, resilient, and elastic. It uses the Actor Model to provide intuitive high-level abstractions for concurrency.
- **ScalikeJDBC**
  - ScalikeJDBC is a tidy SQL-based database access library for Scala developers. It naturally wraps JDBC APIs and provides easy-to-use APIs, making it intuitive and highly flexible.
- **Doobie**
  - Doobie is a pure functional JDBC layer for Scala and Cats. It provides a functional way to construct programs and higher-level libraries that use JDBC.

### 3.8 Video game Engines
- **Slick**
  - Slick is a Functional Relational Mapping (FRM) library for Scala that allows developers to query and access databases in a manner similar to working with Scala collections. It provides compile-time safety and composability, making it easier to write and maintain database queries.
- **PlayJSON**
  - PlayJSON is a Scala JSON library originally developed for use with Play Framework. It uses Jackson for JSON parsing and offers features like custom validation while parsing and automatic parsing of JSON in request bodies.
- **Circe**
  - Circe is a JSON library for Scala that is part of the Cats ecosystem. It provides a functional way to handle JSON data, including encoding and decoding using Encoder and Decoder type classes.
- **Quill**
  - Quill is a library for database access in Scala that provides a Quoted Domain Specific Language (QDSL) to express queries in Scala and execute them in a target language. It supports compile-time query generation and validation, making it easier to write type-safe and efficient database queries.
- **Indigo**
  - Indigo is a game engine written in Scala, designed specifically for functional programmers. It aims to address challenges in testing games and managing data flow and state.
- **CosPlay**
  - CosPlay is a 2D ASCII game engine for Scala. It is designed to be a standard Scala3-based program with minimal requirements for code organization.
- **LibGDX w/ Scala**
  - LibGDX is a popular JVM framework for game design that can be used with Scala. It provides a set of tools for creating cross-platform games.

### 3.9 Macros & the Type System
- **Jsoniter**
  - Jsoniter is a library for compile-time generation of safe and ultra-fast JSON codecs for Scala. It uses Scala macros to generate codecs and has its own core mechanics for parsing and serialization.
- **uPickle**
  - uPickle is a simple, fast, and dependency-free JSON serialization library for Scala. It is designed to handle statically-typed, tree-shaped, immutable data structures efficiently.
- **Monocle**
  - Monocle is an optics library for Scala and Scala.js, strongly inspired by Haskell Lens. It provides functionalities for creating and manipulating lenses, prisms, and isomorphisms.
- **Shapeless**
  - Shapeless is a library for type-level programming in Scala, providing functionalities for generic programming using type classes and macros. It allows for type-safe manipulation and transformation of data structures at compile time, leveraging Scala's type system.
- **Chimney**
  - Chimney is a Scala library that provides typeclasses and macros for intuitive and type-safe transformations between data structures. It allows for automatic derivation of transformers between different model case classes, reducing boilerplate code.
- **Scalameta**
  - Scalameta is a metaprogramming tool for Scala that provides high-quality syntactic and semantic analysis and code generation. It was widely used in Scala 2 for advanced metaprogramming scenarios and continues to be relevant in Scala 3.
- **Magnolia**
  - Magnolia is a generic macro for automatic materialization of typeclasses for datatypes composed from case classes (products) and sealed traits (coproducts). It supports recursively-defined datatypes out-of-the-box and incurs no significant time penalty during compilation.

---

## 4. Optional / Specialized Topics

- Float
- Nothing
- List
- Vector
- Set
- Map
- Functions & Methods
- Method Calls
- Anonymous Func / Lambda
- Case Classes
- Sealed Traits
- apply Method
- Enums
- foldLeft
- foreach
- map
- Case Objects
- unapply Method
- for comprehension
- LazyList
- Akka / Pekko
- No Ecosystem
- Scalatra
- Tapir
- Akka & Peko Streams

---

## 5. References

- [Scala Roadmap](https://roadmap.sh/scala)

---

## 6. Related Roles / Topics

### Related Roles
- Data Analyst
- Data Engineer

### Related Skills
- Java