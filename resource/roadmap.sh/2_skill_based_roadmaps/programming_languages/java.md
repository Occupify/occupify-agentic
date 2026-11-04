# Java

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/java
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Learn the Basics
- **Basic Syntax**
  - Basic syntax in Java defines the set of rules and symbols that determine how programs are written and interpreted by the compiler. It includes the structure of classes and methods, the usage of keywords, case sensitivity, and the implementation of statements terminated by semicolons.
- **Data Types**
  - Data types in Java specify the different sizes and values that can be stored in a variable. They are categorized into two main groups: primitive types, which include basic building blocks like integers, characters, and booleans, and non-primitive types, which include objects and arrays.
- **Conditionals**
  - Conditionals are programming constructs that allow a Java program to execute specific blocks of code based on whether a given boolean condition evaluates to true or false. These statements, such as if, else if, else, and switch, enable developers to control the flow of execution and make decisions within an application.
- **Arrays**
  - Arrays are fundamental data structures used to store a collection of elements of the same data type in contiguous memory locations. They provide a way to organize and access multiple values using a single variable name and an index.
- **Loops**
  - Loops are programming structures that allow a block of code to be executed repeatedly as long as a specified condition remains true. In Java, these control flow statements help automate repetitive tasks by iterating over data or performing actions multiple times without needing to write the same lines of code over and over.
- **Variables and Scopes**
  - Variables are like containers that hold data in a program. Each variable has a name, a type (like integer, text, or boolean), and a value.
- **Type Casting**
  - Type casting is the process of converting a variable from one data type to another. This is often necessary when you need to perform operations between variables of different types, or when you need to store a value of one type in a variable of another type.
- **Strings and Methods**
  - Strings are sequences of characters, like words or sentences, used to represent text in programming. Methods are actions you can perform on these strings, such as finding their length, changing their case (uppercase or lowercase), or extracting parts of them.
- **Math Operations**
  - Math operations involve performing calculations using numbers. These operations include addition, subtraction, multiplication, division, and modulus (finding the remainder).
- **Lifecycle of a Program**
  - The lifecycle of a Java program describes the sequence of stages a source file undergoes to become an executable application. It begins with writing code in a .java file, which is then compiled by the javac compiler into platform-independent bytecode stored in a .class file.
- **Classes and Objects**
  - Classes are blueprints for creating objects, which are instances of those classes. A class defines the characteristics (attributes) and behaviors (methods) that objects of that class will possess.
- **Basics of OOP**
  - Object-Oriented Programming (OOP) is a programming paradigm centered around "objects," which contain data in the form of fields (attributes) and code in the form of procedures (methods). OOP focuses on creating reusable code by grouping related data and behavior into objects, allowing for modularity, abstraction, inheritance, and polymorphism.

### 1.2 Exception Handling
- **Exception Handling**
  - Exception handling is a mechanism in Java used to manage runtime errors that disrupt the normal flow of an application. It utilizes a structured approach involving try, catch, and finally blocks to catch unexpected events, such as invalid user input or network failures, and respond to them gracefully.

### 1.3 Lambda Expressions
- **Object Lifecycle**
  - The object lifecycle refers to the series of stages an object goes through from its creation (allocation of memory) to its destruction (reclaiming of memory). These stages typically include object creation, initialization, usage, and eventual garbage collection when the object is no longer needed.
- **Abstraction**
  - The abstract keyword in Java is used to declare a class or a method that cannot be instantiated directly or must be implemented by subclasses, respectively. It is a key part of Java's abstraction mechanism, allowing developers to define abstract classes and methods that provide a blueprint for other classes.
- **Inheritance**
  - Inheritance is a fundamental concept in object-oriented programming where a new class (called a subclass or derived class) acquires properties and behaviors from an existing class (called a superclass or base class). This allows for code reuse and the creation of hierarchical relationships between classes, promoting a more organized and maintainable codebase.
- **Interfaces**
  - An interface in Java is a blueprint of a class. It specifies a set of methods that a class must implement if it claims to implement the interface.
- **Encapsulation**
  - Encapsulation is a fundamental concept in object-oriented programming where data and the methods that operate on that data are bundled together as a single unit. This unit, often a class, hides the internal state of the object from the outside world and only exposes a controlled interface for interacting with it.

### 1.4 Annotations
- **Method Overloading / Overriding**
  - Method overloading allows you to define multiple methods in the same class with the same name but different parameters (different number, types, or order of parameters). Method overriding, on the other hand, occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
- **Record**
  - A record is a special type of class in Java that is designed to hold immutable data. It automatically generates methods like equals(), hashCode(), and toString() based on the components declared in its header, reducing boilerplate code.

### 1.5 Modules
- **Static vs Dynamic Binding**
  - Static binding, also known as early binding, happens at compile time. The compiler knows exactly which method will be called based on the type of the variable.

### 1.6 Optionals
- **Optionals**
  - Optionals are a container object that may or may not contain a non-null value. They are primarily used to represent the absence of a value, avoiding the need to return null, which can lead to NullPointerExceptions.

---

## 2. Intermediate

### 2.1 Cryptography
- **Attributes and Methods**
  - Attributes are variables that hold data about an object, defining its state or characteristics. Methods are functions that define the behavior of an object, allowing it to perform actions or operations.
- **Access Specifiers**
  - Access specifiers (or access modifiers) in Java are keywords that control the visibility or accessibility of classes, methods, constructors, and other members. They determine from where these members can be accessed.
- **Static Keyword**
  - The static keyword in Java is used to create members (variables and methods) that belong to the class itself, rather than to any specific instance of the class. This means there's only one copy of a static variable shared by all objects of that class, and you can access static members directly using the class name without needing to create an object.
- **Nested Classes**
  - Nested classes are classes defined inside another class. The class that contains the inner class is known as the outer class.
- **Method Chaining**
  - Method chaining is a programming technique where multiple method calls are made sequentially on the same object, one after another, in a single statement. Each method in the chain returns an object, allowing the next method to be called on that returned object.
- **Enums**
  - Enums, short for enumerations, are a special data type in Java that represent a group of named constants. They allow you to define a type that can only take on a specific set of predefined values.
- **Final Keyword**
  - The final keyword in Java is a non-access modifier used to apply restrictions on a variable, method, or class. When applied to a variable, it makes the variable's value constant after initialization.
- **Packages**
  - Packages are a mechanism for organizing related classes, interfaces, and sub-packages into a hierarchical namespace. They act like folders in a file system, allowing developers to group functional components together to improve code maintainability and avoid naming conflicts.
- **Initializer Block**
  - An initializer block in Java is a block of code, enclosed in curly braces {} , that is executed when an instance of a class is created. It's used to initialize instance variables or perform setup tasks before the constructor is called.
- **Pass by Value / Pass by Reference**
  - Pass by value and pass by reference are two different ways of passing arguments to a function or method. In pass by value, a copy of the variable's value is passed to the function, so any changes made to the parameter inside the function do not affect the original variable.
- **volatile keyword**
  - The volatile keyword in Java is a modifier that can be applied to instance variables. It ensures that all threads see the most up-to-date value of a variable.

### 2.2 Dependency Injection
- **Array vs ArrayList**
  - Arrays and ArrayLists are both ways to store collections of elements in Java. An array is a fixed-size, ordered sequence of elements of the same data type.
- **Set**
  - A Set is a data structure that stores a collection of unique elements. This means that no duplicate values are allowed within a Set.
- **Map**
  - A Map is a data structure that stores data in key-value pairs. Each key is unique, and it maps to a specific value.

### 2.3 Date and Time
- **Java Memory Model**
  - The Java Memory Model (JMM) defines how threads in Java interact with memory. It specifies how and when different threads can see writes to shared variables, addressing issues like data visibility and race conditions in concurrent programs.

### 2.4 Networking
- **Networking**
  - Networking in Java refers to the ability of applications to communicate over a network, such as the internet or a local area network, using the java.net package. This package provides classes and interfaces that enable developers to implement client-server architectures, handle data transmission through sockets, and interact with various protocols like TCP and UDP.

### 2.5 Regular Expressions
- **High Order Functions**
  - High Order Functions are functions that can either accept other functions as arguments or return functions as their results. This capability allows for more flexible and reusable code by enabling you to abstract over operations.

### 2.6 I/O Operations
- **Queue**
  - A queue is a fundamental data structure that follows the First-In, First-Out (FIFO) principle. Think of it like a line at a store: the first person to join the line is the first person to be served.
- **Stack**
  - A stack is a fundamental data structure that follows the Last-In, First-Out (LIFO) principle. Imagine a stack of plates; you can only add or remove plates from the top.
- **Dequeue**
  - A Dequeue (pronounced "dee-queue") is a double-ended queue, a data structure that allows you to add and remove elements from both the front (head) and the back (tail) of the queue. Unlike a regular queue (FIFO - First-In, First-Out), a dequeue provides flexibility for both FIFO and LIFO (Last-In, First-Out) operations.
- **Iterator**
  - An Iterator is an object that enables you to traverse through a collection (like a List or Set) one element at a time. It provides a standard way to access elements sequentially without needing to know the underlying structure of the collection.

### 2.7 File Operations
- **Generic Collections**
  - Java Generic methods and generic classes enable programmers to specify, with a single method declaration, a set of related methods, or with a single class declaration, a set of related types, respectively.
- **EBean**
  - Ebean is an object-relational mapping tool written in Java. It supports the standard JPA annotations for declaring entities.
- **JDBC**
  - JDBC is an API(Application programming interface) used in java programming to interact with databases. The classes and interfaces of JDBC allow the application to send requests made by users to the specified database.

### 2.8 Concurrency
- **Maven**
  - Maven is a project management and build automation tool used primarily for Java projects. It uses a project object model (POM) defined in an XML file to manage a project's build process, reporting, and documentation from a central piece of information.
- **Threads**
  - A thread is the smallest unit of execution within a Java process that allows a program to perform multiple tasks simultaneously. It represents an independent path of execution that shares the same memory space as other threads within the same application.
- **Virtual Threads**
  - Virtual Threads are lightweight threads managed by the Java Virtual Machine (JVM). Unlike traditional operating system threads, which are relatively expensive to create and manage, virtual threads are designed to be extremely lightweight, allowing for the creation of millions of them.
- **Functional Interfaces**
  - Functional interfaces are interfaces that contain only one abstract method. They can have multiple default or static methods, but only one method that needs to be implemented.

---

## 3. Advanced

### 3.1 Database Access
- **Spring Data JPA**
  - Spring Data JPA aims to significantly improve the implementation of data access layers by reducing the effort to the amount that's actually needed. As a developer you write your repository interfaces, including custom finder methods, and Spring will provide the implementation automatically.
- **Hibernate**
  - Hibernate is an open source object-relational mapping tool that provides a framework to map object-oriented domain models to relational databases for web applications. Hibernate implements the specifications of JPA.

### 3.2 Web Frameworks
- **Spring (Spring Boot)**
  - Spring Boot is an open source, microservice-based Java web framework. The Spring Boot framework creates a fully production-ready environment that is completely configurable using its prebuilt code within its codebase.
- **Play Framework**
  - Play Framework is a high-productivity web application framework that allows the model-view-controller pattern. It is written in Scala but can also be used for other programming languages that are compiled and run on the JVM.
- **Quarkus**
  - Quarkus is a Kubernetes-native Java framework tailored for GraalVM and HotSpot, designed to optimize Java applications for serverless, cloud, and containerized environments. It focuses on fast startup times and low memory consumption by performing build-time metadata processing and dependency injection.
- **Javalin**
  - Javalin is a lightweight web framework for Java and Kotlin that's designed to be simple, intuitive, and fun to use. It allows developers to quickly build web applications and APIs with minimal boilerplate code.

### 3.3 Build Tools
- **Gradle**
  - Gradle is an open-source build automation tool that helps software engineers to test, build, and release high-performance software products. In addition, Gradle also supports multi-language development.
- **Bazel**
  - Bazel is an open-source build and test tool similar to Make, Maven, and Gradle. It uses a human-readable, high-level build language.
- **Functional Composition**
  - Functional composition is the process of combining two or more functions to produce a new function. The resulting function applies each function in order, passing the output of one function as the input to the next.
- **Stream API**
  - Java provides a new additional package in Java 8 called java.util.stream. This package consists of classes, interfaces and enum to allows functional-style operations on the elements.
- **JUnit**
  - JUnit is a widely-used open-source testing framework for the Java programming language that provides annotations to identify test methods and assertions to check expected results. It allows developers to write and execute repeatable tests to verify the correctness of individual units of source code, such as classes or methods.
- **TestNG**
  - TestNG is a testing framework inspired from JUnit and NUnit but introducing some new functionalities that make it more powerful and easier to use.
- **REST Assured**
  - Testing and validating REST services in Java is harder than in dynamic languages such as Ruby and Groovy. REST Assured brings the simplicity of using these languages into the Java domain.
- **JMeter**
  - Apache JMeter is an Apache project that can be used as a load testing tool for analyzing and measuring the performance of a variety of services, with a focus on web applications.

### 3.4 Logging Frameworks
- **Logback**
  - Logback is one of the most widely used logging frameworks in the Java Community. It's a replacement for its predecessor, Log4j.
- **Log4j2**
  - Log4j2 is an open-source logging library that provides a flexible and efficient way to record application events and diagnostic messages. It serves as an upgrade to the original Log4j framework, offering improved performance through asynchronous loggers and advanced configuration options.
- **SLF4J**
  - The SLF4J or the Simple Logging Facade for Java is an abstraction layer for various Java logging frameworks, like Log4j 2 or Logback. This allows for plugging different logging frameworks at deployment time without the need for code changes.
- **TinyLog**
  - TinyLog is a lightweight logging framework for Java that focuses on simplicity and performance through a minimal API. It functions as a static logging solution that eliminates the need for complex configuration files, allowing developers to output logs to the console or files with just a few lines of code.

### 3.5 Documentation
- **Javadoc**
  - Javadoc is a tool for generating API documentation in HTML format from doc comments in Java source code. These doc comments use a specific syntax, including tags like @param, @return, and @throws, to describe classes, interfaces, methods, and fields.

### 3.6 Testing
- **Cucumber-JVM**
  - Cucumber is a testing tool that supports Behavior Driven Development (BDD). It offers a way to write tests that anybody can understand, regardless of their technical knowledge.
- **Mocking > Mockito**
  - Mockito is a popular open-source testing framework for Java that enables developers to create and configure mock objects for unit testing. It allows you to simulate the behavior of complex dependencies and external services, ensuring that your tests focus solely on the logic of the code being verified.

---

## 4. Optional / Specialized Topics

- Loops
- Variables and Scopes
- Type Casting
- Strings and Methods
- Math Operations
- Lifecycle of a Program
- Classes and Objects
- Basics of OOP
- Encapsulation
- Method Chaining
- Enums
- Final Keyword
- Packages
- Initializer Block
- Pass by Value / Pass by Reference
- volatile keyword
- JUnit
- TestNG
- REST Assured
- JMeter

---

## 5. References

- [Java Roadmap](https://roadmap.sh/java)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- Spring Boot
- Go
- JavaScript