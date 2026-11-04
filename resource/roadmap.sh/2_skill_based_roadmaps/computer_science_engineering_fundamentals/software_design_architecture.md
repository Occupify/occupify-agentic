# Software Design & Architecture

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/software-design-architecture
- Related Roles:
  - Backend Developer
  - Software Architect
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Clean Code Principles
- **Clean Code**
  - Clean code refers to code that is easy to read, understand, and modify, following practices like meaningful naming, small functions, and clear structure. It prioritizes clarity over cleverness, since code is read far more often than it is written.
- **Programming Paradigms**
  - A programming paradigm is a fundamental style or approach to structuring and writing code, such as object-oriented, functional, or procedural programming. Each paradigm offers different ways to organize logic, manage state, and handle control flow, and many languages support more than one paradigm.
- **Object Oriented Programming**
  - Object-oriented programming (OOP) is a programming paradigm that is based on the concept of "objects," which are instances of a class. In OOP, a class is a blueprint for creating objects, which have both data (attributes) and behavior (methods).
- **Design Principles**
  - Design principles are fundamental guidelines that help software engineers create systems that are maintainable, scalable, robust, and easy to understand. They represent best practices derived from decades of software engineering experience and are widely used to guide the structure and behavior of code.
- **Design Patterns**
  - Design patterns are general, reusable solutions to common problems that occur when designing software at the level of individual classes and objects. They describe proven approaches to structuring relationships between objects, such as how to create objects flexibly or how to let objects react to changes in other objects.
- **Architectural Principles**
  - Architectural principles refer to a set of guidelines or rules that are used to guide the design and development of a software architecture. These principles are intended to ensure that the resulting architecture is maintainable, scalable, and easy to understand and modify.
- **Architectural Styles**
  - Architectural styles are high-level patterns that define the fundamental structure and organization of a software system. They provide a standardized way to arrange components, define their responsibilities, and establish the communication mechanisms between them.
- **Architectural Patterns**
  - Architectural patterns are reusable solutions to common problems encountered during the high-level design of software systems. They provide a structural template that defines how components within an application interact, organize, and communicate.
- **Enterprise Patterns**
  - Enterprise Patterns are well-documented, reusable solutions to commonly occurring problems in enterprise software development. These patterns provide a vocabulary and a set of best practices for designing robust, scalable, and maintainable enterprise applications, addressing recurring challenges like data access, concurrency, distribution, and integration with legacy systems.
- **Be consistent**
  - Being consistent refers to maintaining a consistent pattern. This can include using consistent naming conventions, data structures, and interfaces throughout the system, as well as adhering to established design principles and best practices.
- **Meaningful names over comments**
  - You should follow the practice of giving clear and descriptive names to different components of a system, such as variables, functions, and classes. This can help to make the system more understandable and maintainable by clearly communicating the purpose of each component and its intended usage.
- **Indentation and Code Style**
  - Indentation and code style refer to the visual layout and formatting rules applied to source code to improve its readability and consistency. This involves standardizing the use of spaces or tabs for nesting, defining line lengths, and following naming conventions for variables and functions.
- **Keep methods / classes / files small**
  - You should design and implement small, focused components that serve a specific purpose, rather than large, monolithic components that try to do everything. This can help to improve the maintainability and scalability of the system by making it easier to understand, test, and modify individual components.

### 1.2 Programming Paradigms
- **Pure functions**
  - Pure functions are a type of function in programming where the output is solely determined by its input values, without any side effects. This means that for the same input, a pure function will always return the same output, and it does not modify any state outside of its own scope.
- **Minimize cyclomatic complexity**
  - Cyclomatic complexity measures the number of linearly independent paths through a program's source code. It's calculated based on the number of decision points (like if, for, while, case) within a function or code block.
- **Avoid passing nulls, booleans**
  - Passing null values or boolean flags into functions often leads to code that is difficult to understand and prone to errors. When a function accepts a boolean, it frequently signals that the function is doing too many things at once, violating the single responsibility principle.
- **Structured Programming**
  - Structured programming is a programming paradigm that emphasizes the use of well-structured control flow constructs such as loops, conditionals, and subroutines. It was developed in the 1960s and 1970s as a reaction to the "spaghetti code" produced by the widespread use of goto statements.
- **Functional Programming**
  - Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It emphasizes the use of functions to solve problems, often using higher-order functions, immutability, and recursion.
- **Object Oriented Programming**
  - Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure and organize code. In OOP, an object is an instance of a class, which is a template that defines the properties and behaviors of the object.

### 1.3 Object Oriented Programming
- **Keep framework code distant**
  - Keeping framework code distant is a design practice that aims to decouple core business logic from the specific libraries or frameworks being used. It involves wrapping third-party tools within abstraction layers, such as interfaces or adapter classes, so that the application remains agnostic of the framework’s internal implementation.
- **Use correct constructs**
  - Using correct constructs involves selecting the most appropriate programming language features, data structures, and syntax to express a specific logic clearly and efficiently. This practice focuses on avoiding the misuse of language capabilities, such as using a loop when a built-in functional method is available or picking an inefficient data type for a simple task.
- **Tests should be fast and independent**
  - Tests should be fast and independent refers to the practice of ensuring that a test suite executes quickly and that each individual test can run in any order without relying on the state of another. Fast tests provide immediate feedback during development, encouraging developers to run them frequently throughout the coding process.
- **Inheritance**
  - Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit the properties and methods of an existing class. The class that is inherited from is called the parent or super class, while the class that inherits is called the child or sub class.
- **Polymorphism**
  - Polymorphism is a core principle in object-oriented programming that allows objects of different classes to be treated as instances of a common base class. It enables a single interface to represent different underlying forms, meaning a method call can behave differently depending on the specific object it is acting upon.
- **Abstraction**
  - Abstraction is the process of hiding complex implementation details and showing only the essential features of an object to the user. It allows developers to interact with a simplified interface while the underlying logic remains encapsulated and separate.
- **Encapsulation**
  - Encapsulation is a fundamental principle of object-oriented programming that bundles data and the methods that operate on that data into a single unit, known as a class. It restricts direct access to an object's internal state by hiding its private implementation details from the outside world.
- **Law of Demeter**
  - The Law of Demeter is a design principle that restricts how objects interact with one another to reduce system coupling. It suggests that a given method should only call methods belonging to its own class, objects created within the method, objects passed as arguments, or direct component objects.
- **SOLID**
  - SOLID is a set of five design guidelines intended to make software designs more understandable, flexible, and maintainable. These principles include the Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.

### 1.4 Design Principles
- **Composition over Inheritance**
  - Composition over inheritance is a design principle that suggests achieving code reuse by assembling complex objects from simpler ones rather than inheriting behavior from a parent class. Instead of creating deep and rigid class hierarchies, this approach encourages developers to define small, focused components that can be combined or swapped out to build specific functionality.
- **Encapsulate what varies**
  - Encapsulate what varies is a fundamental design principle that suggests identifying the parts of an application that are likely to change and separating them from the parts that remain constant. By isolating volatile code behind stable interfaces or abstractions, developers can modify or extend functionality without disrupting the rest of the system.
- **Hollywood Principle**
  - The Hollywood Principle is a design strategy that dictates that high-level components should control the flow of an application while low-level components are only called upon when needed. Instead of low-level modules actively polling or calling higher-level functions, the system informs the lower-level parts of the application when it is their turn to execute.
- **Tell, don't ask**
  - Tell, don't ask is a principle that encourages object-oriented design where you tell an object to perform an action rather than asking for its internal state to make decisions yourself. Instead of retrieving data from an object using getter methods to perform logic externally, you encapsulate that logic within the object itself by providing a command or a method.
- **DRY**
  - DRY is a software development principle aimed at reducing the repetition of information and logic within a system. It suggests that every piece of knowledge or functionality should have a single, unambiguous representation within an application.
- **YAGNI**
  - YAGNI, which stands for "You Ain't Gonna Need It," is a principle in software development that suggests programmers should not add functionality until it is actually necessary. It encourages developers to focus only on the requirements at hand rather than attempting to predict future needs that may never arise.

---

## 2. Intermediate

### 2.1 Design Patterns
- **Organize code by actor it belongs to**
  - Organizing code by the actor it belongs to involves grouping components, classes, or modules based on the specific business entities or users they serve. This approach aligns the physical structure of a codebase with the actual responsibilities and requirements of the stakeholders involved in the system.
- **Command query separation**
  - Command-Query Separation (CQS) is a software design principle that separates the responsibilities of a method or function into two categories: commands and queries. Commands are methods that change the state of the system, while queries are methods that return information but do not change the state of the system.
- **Keep it simple and refactor often**
  - "Keep it simple and refactor often" is a development philosophy that encourages writing straightforward, readable code and frequently improving its internal structure without changing its external behavior. This approach focuses on reducing complexity by removing redundant logic and breaking down large tasks into manageable pieces.
- **GoF Design Patterns**
  - GoF Design Patterns are a set of reusable solutions to common problems encountered during software design. Originally documented by the "Gang of Four" (Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides), these patterns provide standardized approaches for structuring classes and objects to create flexible and maintainable systems.
- **PoSA Patterns**
  - Pattern-Oriented Software Architecture (PoSA) patterns provide a standardized way to describe and organize recurring architectural structures and design solutions within complex software systems. These patterns function as proven blueprints that help developers structure the overall layout of an application, handle communication between components, and manage distributed systems.

### 2.2 Model-Driven Design
- **Domain Models**
  - A domain model is a conceptual representation of the real-world objects, entities, and processes that exist within a specific area of business or subject matter. It acts as a bridge between technical implementation and business requirements by documenting the relationships, attributes, and behaviors of core elements.
- **Class Variants**
  - Class variants are a conceptual approach within object-oriented design used to represent different forms or specialized versions of an entity while maintaining a shared core identity. This technique involves defining a base structure that establishes common attributes and behaviors, which are then extended or modified to support specific functional requirements or domain constraints.
- **Domain Language**
  - Domain language refers to a specialized vocabulary and set of terms used by developers and domain experts to describe the specific concepts, processes, and rules of a business area. By establishing a shared vocabulary, it bridges the gap between technical implementation and business requirements, ensuring that the software design directly reflects the reality of the problem space.
- **Anemic Models**
  - Anemic models are domain objects that contain little or no business logic, acting primarily as simple data holders with public getters and setters. In this design, the actual behavior and decision-making logic are placed in separate service classes, which interact with the data objects to perform operations.
- **Abstract Classes**
  - An abstract class is a restricted base class that cannot be used to create objects. It serves as a blueprint for other classes, providing a common structure by defining methods that subclasses must implement.
- **Concrete Classes**
  - A concrete class is a blueprint in object-oriented programming that provides a complete implementation for all of its defined methods and properties. It serves as a tangible template that allows developers to create direct instances, or objects, which can then be utilized to perform tasks within an application.
- **Scope / Visibility**
  - Scope and visibility define the accessibility of variables, methods, and classes within a codebase. Scope refers to the specific region of the program where a particular identifier is valid and can be referenced.
- **Interfaces**
  - An interface is a programming contract that defines a set of methods or properties that a class must implement without specifying how those members should function. It serves as a blueprint for classes, allowing developers to ensure that different objects adhere to a common structure regardless of their internal implementation.

### 2.3 Messaging
- **Program against abstractions**
  - Programming against abstractions involves interacting with interfaces or abstract base classes rather than concrete implementations. This approach allows a system to remain decoupled from the specific details of how a task is performed, enabling developers to swap or modify underlying components without affecting the rest of the application.
- **Event-Driven**
  - Event-driven architecture structures a system around the production, detection, and consumption of events, which are records of something that happened. Components react to events asynchronously instead of calling each other directly, which reduces coupling between producers and consumers.
- **Publish-Subscribe**
  - Publish-subscribe is a messaging pattern where senders, called publishers, send messages to a channel or topic without knowing who will receive them. Receivers, called subscribers, express interest in specific topics and receive only the messages published to those topics.

### 2.4 Distributed
- **Component Principles**
  - Component principles are a set of guidelines used to organize software into cohesive, reusable, and decoupled modules. These principles address how to group classes and modules together to balance the competing needs of maintainability, flexibility, and independent deployability.
- **Client-Server**
  - Client-server is a distributed architecture where clients request services or resources and servers provide them over a network. The client handles the user interface and user interaction, while the server manages data storage, business logic, and processing.
- **Peer-to-Peer**
  - Peer-to-peer is a distributed architecture where each node, called a peer, acts as both a client and a server, sharing resources directly with other peers instead of relying on a central server. This removes a single point of failure and can spread load across many machines.

### 2.5 Architectural Styles
- **Architectural Styles**
  - Architectural styles are established approaches to organizing the high level structure of a software system, such as how components are distributed, how they communicate, and how they are deployed. Each style, like layered, client-server, or microservices, comes with its own trade-offs around scalability, maintainability, and complexity.

---

## 3. Advanced

### 3.1 Architectural Principles
- **Policy vs Detail**
  - Policy and detail represent a fundamental separation between the core logic of an application and the specific implementation mechanisms that support it. Policies define the high-level business rules, domain entities, and operational requirements that dictate what an application should accomplish.
- **Coupling and Cohesion**
  - Coupling measures how much one module depends on another, while cohesion measures how closely the responsibilities within a single module relate to each other. Low coupling and high cohesion make a codebase easier to change, since a module can be modified or replaced without breaking unrelated parts of the system.
- **Boundaries**
  - Boundaries define the separation between different parts of a system, marking where one component's responsibility ends and another's begins. They control how data and control flow between modules, layers, or services, and they hide internal implementation details behind a stable interface.

### 3.2 Structural
- **Layered Architectures**
  - Layered architecture is a design pattern that organizes a software system into distinct horizontal segments or tiers, each with a specific responsibility. In this approach, components are grouped based on their function, such as presentation, business logic, or data access, with each layer communicating only with the one directly below it.
- **Component-Based**
  - Component-based architecture divides a system into independent, reusable components, each encapsulating a specific piece of functionality behind a well-defined interface. Components can be developed, tested, and replaced separately, as long as their interfaces stay stable.
- **Monolithic**
  - A monolithic architecture builds an application as a single, unified codebase where all components, such as the user interface, business logic, and data access, run as one deployable unit. This simplifies development and deployment early on, since there is only one artifact to build and run.
- **Layered**
  - A layered architecture organizes a system into horizontal layers, such as presentation, business logic, and data access, where each layer only communicates with the layer directly below or above it. This separation makes it easier to reason about and test each layer in isolation.

### 3.3 Architectural Patterns
- **Domain-Driven Design**
  - Domain-Driven Design is an approach to software design that models the software's structure and language around the business domain it serves. It encourages close collaboration between developers and domain experts to build a shared vocabulary, called a ubiquitous language, that is reflected directly in the code.
- **Model-View Controller**
  - Model-View-Controller (MVC) is an architectural pattern that separates the concerns of a software system into three distinct components: the model, the view, and the controller, where the model represents the data and the business logic of the system, the view represents the user interface of the system and the controller acts as an intermediary between the model and the view. The main goal of MVC is to separate the concerns of the system, making it easier to understand, maintain and evolve, it's widely used in web development.
- **Microservices**
  - Microservices is an architectural pattern that is used to design software systems as a collection of small, independent, and loosely-coupled services. Each service is responsible for a specific functionality and can be developed, deployed, and scaled independently.
- **Blackboard Pattern**
  - The Blackboard architectural pattern is a software design pattern that allows for the creation of a centralized repository of information that can be accessed and modified by multiple independent modules or subsystems. The blackboard serves as a communication and coordination mechanism between these modules, allowing them to share information and collaborate to achieve a common goal.
- **Microkernel**
  - A microkernel is an architectural pattern in operating system design that aims to minimize the amount of code running in kernel mode (i.e., privileged mode with direct access to hardware resources) and instead move as much functionality as possible into user mode. This is done by providing a small, minimalistic core kernel that only handles basic tasks such as memory management, process scheduling, and inter-process communication (IPC), and leaving all other functionality to be implemented in user-mode processes.
- **Serverless Architecture**
  - Serverless architecture lets developers build and run applications without managing the underlying servers, since a cloud provider automatically provisions, scales, and manages the infrastructure. Code runs in stateless functions that execute in response to events, and the provider charges based on actual usage rather than reserved capacity.
- **Message Queues / Streams**
  - Message queues and streams are infrastructure components that store and pass messages between producers and consumers, allowing them to operate independently and at different speeds. A queue typically delivers each message to one consumer and removes it once processed, while a stream keeps an ordered log of events that multiple consumers can read and replay.
- **Event Sourcing**
  - Event sourcing stores the state of an application as a sequence of events rather than storing only the current state. Each change to the system is captured as an immutable event, and the current state is derived by replaying those events in order.
- **CQRS**
  - Command Query Responsibility Segregation, or CQRS, separates the operations that change data, called commands, from the operations that read data, called queries, often using different models for each. This separation allows the read and write sides of a system to be optimized, scaled, and even stored independently.

### 3.4 Enterprise Patterns
- **SOA**
  - Service-Oriented Architecture, or SOA, structures an application as a collection of loosely coupled services that communicate over a network, typically through standardized protocols. Each service exposes a well-defined interface and can be reused across different applications within an organization.
- **DTOs**
  - The Data Transfer Object Design Pattern is one of the enterprise application architecture patterns that calls for the use of objects that aggregate and encapsulate data for transfer. A Data Transfer Object is, essentially, like a data structure.
- **Identity Maps**
  - An identity map is a pattern that keeps track of every object loaded from a database during a single unit of work, mapping each object to its unique identifier. When the same object is requested again, the identity map returns the existing instance instead of loading a new copy from the database.
- **Usecases**
  - A use case describes a specific interaction or process that a system supports to fulfill a user's goal, often expressed as a single class or function that orchestrates the steps needed to complete that goal. It sits between the presentation layer and the domain model, coordinating calls to entities, repositories, and other services without containing the core business rules itself.
- **Repositories**
  - A repository is a pattern that provides an abstraction over data storage, exposing methods to retrieve, add, update, or remove objects without exposing the details of how that data is persisted. Application code interacts with the repository's interface instead of writing database queries directly, which makes it easier to change the underlying storage technology or write tests using a fake implementation.
- **Mappers**
  - A mapper converts data between two different representations, such as translating a database row into a domain object or converting a domain object into a format suitable for an API response. This separation keeps the domain model free of persistence or transport concerns, since it does not need to know how it will be stored or transmitted.
- **Transaction Script**
  - Transaction Script is a pattern used in enterprise application development that organizes business logic into a single procedural script. It is often used for simple CRUD (create, read, update, delete) operations, where all of the logic for a specific transaction is contained in a single script or function.
- **Commands / Queries**
  - The Command and Query Responsibility Segregation (CQRS) pattern separates operations that change a system's state, called commands, from operations that read data, called queries. A command performs an action such as creating or updating a record and returns no data, while a query returns data without producing any side effects.
- **Value Objects**
  - A value object is an object defined entirely by its attributes rather than by a unique identity, meaning two value objects with the same attributes are considered equal. Examples include a date range, a monetary amount, or a coordinate pair.
- **Domain Models**
  - A domain model represents the concepts, rules, and relationships of a business domain within the software, combining data and behavior into objects like entities and value objects. It captures business logic directly in these objects rather than spreading it across separate procedural scripts.
- **Entities**
  - An entity is an object defined by a unique identity that persists over time, even as its attributes change. Two entities with identical attributes are still considered different if they have different identities, unlike value objects.
- **ORMs**
  - An Object-Relational Mapper, or ORM, translates data between a relational database and objects in an application's code, letting developers work with database records as regular objects instead of writing raw SQL. It handles tasks like generating queries, mapping rows to objects, and managing relationships between tables.

---

## 4. Optional / Specialized Topics

- Design Patterns
- Architectural Principles
- Architectural Styles
- Architectural Patterns
- Enterprise Patterns
- Be consistent
- Meaningful names over comments
- Indentation and Code Style
- Keep methods / classes / files small
- Functional Programming
- Object Oriented Programming
- Polymorphism
- Abstraction
- Encapsulation
- Law of Demeter
- SOLID
- DRY
- YAGNI
- PoSA Patterns
- Abstract Classes
- Concrete Classes
- Scope / Visibility
- Interfaces
- Microkernel
- Serverless Architecture

---

## 5. References

- [Software Design & Architecture Roadmap](https://roadmap.sh/software-design-architecture)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Software Architect
- DevOps Engineer

### Related Skills
- Python
- Java
- Go