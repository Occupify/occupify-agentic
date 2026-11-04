# ASP.NET Core

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/aspnet-core
- Related Roles:
  - Backend Developer
  - DevOps Engineer
  - Data Analyst

---

## 1. Beginner

### 1.1 Learn the Basics of C#
- **C#**
  - C# is a modern coding language that was developed by Microsoft that focuses on applying the coding style to C++ and making it so that way it's more condensed and simple. It's similar to Java by both being static, strong, and manifestive languages.
- **.NET**
  - .NET (pronounced "dot net") is a software framework developed by Microsoft that can be used to create a wide range of applications, including Windows desktop and web applications, mobile apps, and gaming. The .NET Framework provides a large library of pre-built functionality, including collections, file input/output, and networking, that can be used by .NET applications.
- **.NET CLI**
  - .NET CLI is the command-line interface (CLI) for the .NET platform. It is a tool that provides a common interface for running .NET Core command-line tools and utilities.
- **StyleCop Rules**
  - StyleCop is a tool used for developers to standardize their code and ensure they all follow the same syntax principles. With StyleCop, one standard can be defined in a stylecop.json file and shared across your team so that each member has the same guidelines when formatting your code.

### 1.2 General Development Skills
- **Git - Version Control**
  - Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- **GitHub, GitLab, BitBucket**
  - There are different repository hosting services with the most famous one being GitHub, GitLab and BitBucket. I would recommend creating an account on GitHub because that is where most of the OpenSource work is done and most of the developers are.
- **HTTP / HTTPs Protocol**
  - HTTP (Hypertext Transfer Protocol) is the foundational set of rules used for transmitting data across the internet, enabling communication between web browsers and servers. It functions as a request-response protocol where a client sends a request to a server, and the server returns a response containing the requested resource or status information.
- **Data Structures and Algorithms**
  - As the name indicates, a Data Structure is a way of organizing the data in the memory so it can be used efficiently. Some common data structures are array, linked list, stack, hashtable, queue, tree, heap, and graph.

### 1.3 Database Fundamentals
- **SQL Basics**
  - SQL (Structured Query Language) is a standard programming language designed for managing and manipulating data held in relational databases. It allows developers to perform essential operations such as retrieving data with queries, inserting new records, updating existing information, and deleting entries from database tables.
- **Database Design Basics**
  - Database Design is a collection of processes that facilitate the designing, development, implementation and maintenance of enterprise data management systems. Properly designed database are easy to maintain, improves data consistency and are cost effective in terms of disk storage space.
- **Stored Procedures**
  - Stored procedures are prepared collections of SQL statements that are stored within a database to be executed as a single unit. When working with ASP.NET Core, these procedures allow developers to encapsulate complex logic and multiple queries on the database server side, which helps reduce the amount of data transferred between the application and the database.
- **Constraints**
  - Constraints are rules applied to columns in a database table to limit the type of data that can be inserted, ensuring accuracy and reliability. Common examples include Primary Keys, which uniquely identify each record, Foreign Keys, which maintain relationships between tables, and Unique constraints, which prevent duplicate values in a column.
- **Triggers**
  - A trigger is a specialized type of stored procedure in a database that automatically executes in response to specific events on a particular table or view. These events typically include data modification actions such as inserting, updating, or deleting records.

### 1.4 ASP.NET Core Basics
- **MVC**
  - MVC is an architectural pattern that separates an application into three main components: Models, Views, and Controllers. The Model manages the data and business logic of the application, the View handles the visual representation and user interface, and the Controller processes incoming requests, interacts with the Model, and selects the appropriate View to display to the user.
- **REST**
  - REST (Representational State Transfer) is an architectural style for building web services. In the context of .NET, RESTful web services can be created using the ASP.NET Web API framework, which allows developers to create HTTP-based services that can be consumed by a wide range of clients, including web browsers and mobile devices.
- **Razor Pages**
  - Razor Pages is a page-focused framework within ASP.NET Core that simplifies the process of building dynamic web interfaces by combining HTML with C# code. It uses a file-based routing system where each page consists of a .cshtml file for the view and a .cshtml.cs file for the page model, which handles the logic for handling requests and processing data.
- **Razor Components**
  - Razor Components are the fundamental building blocks of user interfaces in Blazor applications. They are reusable units that combine HTML markup with C# code to define how a part of a webpage should render and behave.
- **Middlewares**
  - Middleware is a component that is assembled into an application pipeline to handle HTTP requests and responses. Each component in the pipeline decides whether to pass the request to the next component or perform actions before and after the next component is invoked.
- **Minimal APIs**
  - Minimal APIs are a lightweight architectural approach for building HTTP APIs in ASP.NET Core with minimal files, dependencies, and configuration. Instead of requiring complex controller classes, this design allows developers to define endpoints directly within the application's configuration file using simple lambda expressions or method groups.

### 1.5 Object Relational Mapping
- **Entity Framework Core**
  - Entity Framework Core (EF Core) is an open-source Object-Relational Mapping (ORM) framework for .NET. It is a lightweight, cross-platform version of Entity Framework, the ORM framework that was part of the .NET Framework.
- **Framework Basics**
  - Entity Framework Core is a lightweight, extensible, and cross-platform version of the popular Entity Framework data access technology. It acts as an object-database mapper that enables .NET developers to work with a database using .NET objects.
- **Code First + Migrations**
  - Code First is a development approach where you define your application's data models as C# classes, and Entity Framework Core generates the corresponding database schema from those classes. Migrations serve as a version control system for your database, tracking changes made to your C# models over time.
- **Dapper**
  - Dapper is a lightweight, open-source object-relational mapper for .NET that acts as a thin wrapper over the ADO.NET IDbConnection interface. It maps database query results directly to plain old CLR objects by executing raw SQL statements provided by the developer.
- **RepoDB**
  - RepoDB is a lightweight, high-performance hybrid Object-Relational Mapper (ORM) for .NET that bridges the gap between micro-ORMs like Dapper and full-featured ORMs like Entity Framework. It allows developers to perform CRUD operations and execute complex SQL queries with minimal overhead while providing the flexibility to write raw SQL when necessary.
- **NHibernate**
  - NHibernate is an object-relational mapping (ORM) framework for .NET that facilitates the interaction between a relational database and object-oriented code. It enables developers to map .NET classes to database tables and map properties to table columns, allowing data to be queried and manipulated using object-oriented principles.
- **Redis**
  - Redis is an open-source, in-memory data store used as a distributed cache to improve the performance and scalability of ASP.NET Core applications. It allows multiple instances of an application to share the same cached data by storing information in a centralized server rather than in the local memory of an individual web server.

### 1.6 Dependency Injection
- **Lazy, Eager, Explicit Loading**
  - Loading patterns in Entity Framework Core determine how and when related data is retrieved from the database when querying a primary entity. Eager loading fetches related data immediately as part of the initial query using the Include method.
- **Change Tracker API**
  - The Change Tracker API is a feature within Entity Framework Core that monitors the state of entities loaded into the application's memory. It automatically detects modifications, additions, and deletions made to objects, keeping track of their current values compared to their original state.

### 1.7 Life Cycles
- **Scrutor**
  - Scrutor is a library for ASP.NET Core that extends the built-in dependency injection container with additional features, primarily focused on assembly scanning and decorator support. It allows developers to automatically register services based on specific conventions or attributes, which helps reduce the amount of boilerplate code required for manual service configuration.
- **Scoped**
  - Scoped services are created once per client request within an ASP.NET Core application. When you register a service with a scoped lifetime, the framework generates a new instance for every individual HTTP request and shares that same instance across all components that process that specific request.
- **Transient**
  - Transient services are created every time they are requested from the service container. This lifecycle is ideal for lightweight, stateless services because a new instance is provided for every controller or service that requires it.
- **Singleton**
  - A Singleton service is created the first time it is requested or when the application starts, and the same instance is then shared across every subsequent request throughout the entire application lifetime. Because this single instance persists for the duration of the app, it is commonly used for managing shared state, configuration settings, or caching services that need to maintain data across different parts of the system.

### 1.8 Caching
- **Memory Cache**
  - Memory caching (often simply referred to as caching) is a technique in which computer applications temporarily store data in a computer’s main memory (i.e., random access memory, or RAM) to enable fast retrievals of that data. The RAM that is used for the temporary storage is known as the cache.
- **Entity Framework 2nd Level Cache**
  - Entity Framework 2nd Level Cache is a caching mechanism that stores the results of database queries in memory to reduce the number of redundant trips to the database. When an application requests data, the system first checks the cache; if the data is already stored there, it retrieves it directly, bypassing the database execution.
- **Distributed Cache**
  - A distributed cache is a cache shared by multiple app servers, typically maintained as an external service to the app servers that access it. A distributed cache can improve the performance and scalability of an ASP.NET Core app, especially when the app is hosted by a cloud service or a server farm.
- **Memcached**
  - Memcached is an open-source, high-performance, distributed memory object caching system which helps in reducing database load. It maintains data as an in-memory key-value store for small chunks of arbitrary data (strings, objects) which can be result of API calls, database reads and so on.

---

## 2. Intermediate

### 2.1 DI Containers
- **Microsoft.Extensions**
  - Microsoft.Extensions.DependencyInjection is the built-in library provided by .NET that implements the dependency injection pattern. It acts as a lightweight container that manages the creation and lifetime of objects within an application.
- **AutoFac**
  - AutoFac is an inversion of control container for .NET applications that manages the dependencies between classes. It facilitates the loose coupling of components by automatically resolving and injecting required services into constructors or properties.

### 2.2 Search Engines
- **Filters and Attributes**
  - In the ASP.NET Core framework, filters and attributes are used to add additional functionality to controllers and action methods, such as authentication, authorization, caching, and exception handling.
- **App Settings and Configs**
  - App settings and configurations provide a way to manage environment-specific variables and application parameters outside of the compiled code. ASP.NET Core uses a centralized configuration system that aggregates data from multiple sources such as JSON files, environment variables, command-line arguments, and user secrets.
- **Elastic Search**
  - Elasticsearch is a distributed, open-source search and analytics engine that can be used to index, search, and analyze large volumes of data quickly and in near real-time. It is built on top of the Apache Lucene library and can be used to perform full-text search, faceted search, and geospatial search, among other things.

### 2.3 Cloud
- **Cosmos DB**
  - Azure Cosmos DB is a fully managed, NoSQL database service designed for high availability and low-latency access to data at any scale. It supports multiple data models, including document, key-value, graph, and column-family, allowing developers to choose the structure that best fits their application needs.

### 2.4 Databases
- **Serilog**
  - Serilog is a third-party logging library for ASP.NET Core that allows developers to easily create structured and searchable log data. It is built on top of the Microsoft.Extensions.Logging framework, which is included in ASP.NET Core.

### 2.5 Relational
- **Solr**
  - Solr is an open-source, enterprise-level search platform built on top of the Apache Lucene library. It provides high-performance, full-text search capabilities, hit highlighting, and faceted search features for large-scale applications.
- **Sphinx**
  - Sphinx is an open-source, full-text search server designed to provide fast and relevant search results for large datasets. It functions as an external indexing engine that allows developers to perform complex searches across databases, XML files, or other data sources without overloading the primary database.
- **SQL Server**
  - MS SQL (or Microsoft SQL Server) is the Microsoft developed relational database management system (RDBMS). MS SQL uses the T-SQL (Transact-SQL) query language to interact with the relational databases.
- **PostgreSQL**
  - PostgreSQL is an open-source, object-relational database management system known for its reliability, feature robustness, and performance. Within the ASP.NET Core ecosystem, it serves as a powerful storage backend that integrates seamlessly with Entity Framework Core to handle complex data relationships and transactions.
- **MariaDB**
  - MariaDB is a community-developed, open-source relational database management system that serves as a binary-compatible drop-in replacement for MySQL. It uses structured query language to store, manage, and retrieve data within tables, maintaining a high level of performance and reliability.

### 2.6 NoSQL
- **Dynamo DB**
  - DynamoDB is a fully managed, serverless NoSQL database service provided by Amazon Web Services that supports key-value and document data structures. In ASP.NET Core applications, it is used to store and retrieve data with consistent single-digit millisecond latency at any scale.
- **MongoDB**
  - MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents rather than traditional tables and rows. In an ASP.NET Core environment, developers interact with MongoDB using the official C# driver, which allows for storing complex data structures that can evolve over time without requiring rigid schema migrations.
- **Cassandra**
  - Apache Cassandra is a distributed NoSQL database designed to handle large amounts of data across many commodity servers while providing high availability with no single point of failure. In an ASP.NET Core environment, it is typically accessed using the DataStax C# Driver, which allows developers to execute CQL (Cassandra Query Language) statements to read and write data.
- **LiteDB**
  - LiteDB is a serverless, single-file NoSQL database engine written in .NET C#. It stores data in a BSON format, making it easy to manage document-based collections directly within an application without needing to install or configure an external database server.

### 2.7 Log Frameworks
- **NLog**
  - NLog is a flexible and free logging platform for various .NET platforms, including ASP.NET Core. It allows developers to route log messages to multiple destinations, such as files, databases, or cloud services, based on configurable rules.

### 2.8 REST
- **Gridlify**
  - Gridify offers a powerful string-based dynamic LINQ query language that is both simple and easy to use. Gridify is a dynamic LINQ library that simplifies the process of converting strings to LINQ queries.
- **Odata**
  - OData is an open protocol that allows for the creation and consumption of queryable and interoperable RESTful APIs. It provides a standardized way to define the data model and the query syntax, enabling clients to request specific data using URL parameters for filtering, sorting, pagination, and selecting properties.

### 2.9 GraphQL
- **GraphQL .NET**
  - GraphQL is a query language for your API, it allows clients to define the structure of the data they need, and the server will return only the requested data. It is an alternative to RESTful web services, and it is gaining popularity because of its flexibility and efficiency.
- **HotChocolate**
  - HotChocolate is a feature-rich, open-source GraphQL server framework for .NET that enables developers to build flexible APIs. It provides tools to define schemas, resolve data, and execute queries by sitting between your client applications and your underlying data sources.

### 2.10 API Clients and Communication
- **gRPC**
  - gRPC is a high-performance, open-source framework that uses HTTP/2 for transport and Protocol Buffers as a message format to enable communication between services. It allows a client application to directly call a method on a server application located on a different machine as if it were a local object.
- **WebApplicationFactory**
  - WebApplicationFactory is a specialized class in ASP.NET Core that simplifies the process of creating a test server for integration testing. It allows developers to host an application in memory, making it possible to send HTTP requests to the system and verify the complete response cycle without needing to deploy the code to a web server.

---

## 3. Advanced

### 3.1 Real-Time Communication
- **MySQL**
  - MySQL is an open-source relational database management system that organizes data into tables with predefined relationships. In an ASP.NET Core environment, it serves as a robust backend storage solution accessed through Entity Framework Core or direct database drivers.
- **CouchDB**
  - CouchDB is an open-source, document-oriented NoSQL database that stores data in JSON format. It is designed to be highly available and handles data synchronization across multiple servers or devices using a master-master replication model.
- **Web Sockets**
  - WebSockets provide a persistent, full-duplex communication channel over a single TCP connection between a client and a server. This technology enables real-time data transfer, allowing servers to push updates to connected clients immediately without the need for the client to constantly request new information.
- **SignalR Core**
  - SignalR Core is a library that simplifies the process of adding real-time web functionality to applications by allowing server-side code to push content to connected clients instantly. It automatically manages connection management, such as handling sockets, while falling back to other compatible technologies like Server-Sent Events or Long Polling when necessary.

### 3.2 Object Mapping
- **AutoMapper**
  - AutoMapper is an object-to-object mapping library that eliminates the need for manual code when transforming one type of object into another. It works by using a convention-based approach to match properties between a source object and a destination object, which simplifies the process of flattening complex models into simpler Data Transfer Objects (DTOs).
- **Mapperly**
  - Mapperly is a source generator for .NET that maps objects without runtime reflection. It generates the mapping code at compile time, making it fast and keeping mappings in sync with your models — just declare a mapper class and it takes care of the rest.
- **Manual Mapping**
  - Manual mapping is the process of explicitly transferring data from one object to another by assigning properties individually within your code. Developers achieve this by creating a new instance of a destination object and setting its fields using the corresponding values from a source object.
- **Native Background Service**
  - A Native Background Service is a class in ASP.NET Core that implements the IHostedService interface or inherits from the BackgroundService base class to execute long-running tasks in the background. These services run independently of the request-response cycle, allowing the application to perform periodic operations like data cleanup, message queue processing, or scheduled report generation.

### 3.3 Task Scheduling
- **Hangfire**
  - Hangfire is an open-source library that allows developers to create, process, and manage background jobs in .NET applications. It provides a persistent storage mechanism that ensures tasks are executed reliably even if the application restarts.
- **Quartz**
  - Quartz is an open-source job scheduling library that allows developers to integrate sophisticated task scheduling into their applications. It enables the execution of background jobs based on complex triggers, such as specific times, recurring intervals, or cron
- **Coravel**
  - Coravel is a library that provides a fluent and easy-to-use syntax for handling common application tasks within ASP.NET Core, such as task scheduling, queuing, and background processing. It acts as a lightweight wrapper around native .NET features, allowing developers to manage complex background operations without needing to configure external dependencies or complex infrastructure.
- **Playwright**
  - Playwright is an open-source library for automating web browsers built by Microsoft, similar to Selenium, it's commonly used for testing web applications. It's built on top of the .NET Core runtime and it provides bindings for C#, it allows developers to write tests for web applications in C# or other .NET languages.
- **Puppeteer**
  - Puppeteer is an open-source library for automating web browsers, similar to Selenium and Playwright. It's built on top of the Chrome DevTools protocol and it provides a set of APIs that allows developers to interact with web browsers and simulate user interactions, such as clicking buttons, filling out forms, and navigating between pages.
- **Test Containers**
  - Testcontainers is a library that runs throwaway Docker containers for your tests. The .NET version lets you spin up real instances of databases, message brokers, and other services inside integration tests, then disposes of them automatically when the tests finish.

### 3.4 Testing
- **Cypress**
  - Cypress is an open-source end-to-end testing framework for web applications, it's built on top of JavaScript and provides a set of APIs that allows developers to automate browser interactions. It's commonly used for testing web applications, as it can be used to automate browser-based tests and assert that the application behaves as expected.
- **.NET Aspire**
  - .NET Aspire is an opinionated stack for building observable, production-ready cloud-native .NET applications. It provides curated packages for common cloud dependencies, service discovery, orchestration for local development, and built-in telemetry to make distributed applications easier to build and debug.
- **Respawn**
  - Respawn is a small .NET utility for resetting test databases to a clean state. It intelligently deletes data by tracking dependencies between tables, so you can run integration tests quickly without manually managing cleanup between test runs.

### 3.5 Microservices
- **RecNRoll**
  - RecNRoll is a .NET testing library designed to facilitate behavior-driven development by recording and replaying user interactions and API calls. It captures the execution flow of an application, allowing developers to generate reproducible test cases that simulate complex user journeys or service communications.
- **Light BDD**
  - LightBDD is a framework designed to support Behavior-Driven Development in .NET applications by providing a way to write human-readable test scenarios. It allows developers to define requirements and expectations using structured, descriptive steps that can be mapped directly to automated code execution.
- **XUnit**
  - xUnit is a free, open-source, community-focused unit testing tool for the .NET framework. It follows a clean and developer-friendly design that isolates tests into individual methods, ensuring that each test run is independent and predictable.
- **NUnit**
  - NUnit is an open-source unit testing framework for the .NET ecosystem that allows developers to write and execute tests to ensure individual sections of code function as intended. It provides a rich set of assertions and attributes that help structure test suites, manage setup and teardown processes, and handle various test scenarios.
- **Shouldly**
  - Shouldly is an assertion library for .NET that focuses on providing human-readable error messages when tests fail. It replaces traditional assertion syntax with a fluent, natural language style, making it easier to understand exactly why a test did not meet your expectations.
- **ActiveMQ**
  - ActiveMQ is an open-source, multi-protocol message broker that facilitates communication between distributed services by acting as a middleman for data exchange. It enables applications to send and receive messages asynchronously, ensuring that services remain decoupled and resilient even when one system is temporarily unavailable.
- **Kafka**
  - Kafka is a distributed event streaming platform used to handle high-throughput data feeds and enable communication between decoupled services. It functions as a publish-subscribe messaging system where producers send records to topics and consumers read those records asynchronously.
- **RabbitMQ**
  - RabbitMQ is an open-source message broker that acts as a middleware for services to communicate asynchronously by sending and receiving messages. In an ASP.NET Core microservices architecture, it enables decoupled communication by allowing one service to place a message into a queue without needing an immediate response from the receiver.
- **NetMQ**
  - NetMQ is a lightweight, high-performance messaging library that serves as a native C# port of the ZeroMQ library. It enables developers to implement various messaging patterns, such as request-reply, pub-sub, and push-pull, for communication between distributed services.
- **Azure Service Bus**
  - Azure Service Bus is a scalable and reliable messaging platform that can handle a high volume of messages, it's also easy to use, has a lot of features like subscription, Topics, Dead Letter, and easy to integrate with other Azure services, and it's a managed service which means Microsoft takes care of the infrastructure and scaling. However, it's worth noting that Azure Service Bus is a paid service and the cost will depend on the number of messages and the size of the data that you are sending and receiving.
- **GitHub Actions**
  - GitHub Actions is a continuous integration and continuous deployment platform that allows developers to automate their software workflows directly within a GitHub repository. It enables the creation of automated pipelines that build, test, and deploy ASP.NET Core applications whenever code changes are pushed.
- **Azure Pipelines**
  - Azure Pipelines is a cloud-based service that allows you to automatically build, test, and deploy your ASP.NET Core applications to any platform or cloud provider. It uses YAML configuration files to define continuous integration and continuous deployment workflows, which trigger automatically whenever you push code to your repository.
- **MSTest**
  - MSTest is a unit testing framework for the .NET framework, it's one of the built-in test frameworks in Visual Studio and it's widely used for unit testing in the .NET ecosystem. In the context of ASP.NET, MSTest can be used to write unit tests for web applications built using the ASP.NET framework.

### 3.6 CI / CD
- **AutoFixture**
  - AutoFixture is an open-source .NET library designed to minimize the 'Arrange' phase of your unit tests by creating object instances automatically with dummy data. It helps reduce boilerplate code and makes tests easier to maintain.
- **Bogus**
  - Bogus is a simple, C#-friendly fake data generator. It lets you create realistic mock objects, lists, and data sets with a fluent API, making it easy to seed tests and demo applications with believable data.
- **Mass Transit**
  - MassTransit is a free, open-source distributed application framework for .NET that simplifies the process of creating message-based applications. It acts as an abstraction layer over various message brokers, such as RabbitMQ or Azure Service Bus, allowing developers to focus on application logic rather than the underlying infrastructure.
- **NServiceBus**
  - NServiceBus is a service bus framework for .NET that simplifies the process of building distributed systems by managing messaging between decoupled services. It provides a reliable abstraction over messaging transports like RabbitMQ, Azure Service Bus, or Amazon SQS, handling complex tasks such as message retries, transactional consistency, and out-of-the-box support for the Saga pattern.
- **EasyNetQ**
  - EasyNetQ is a thin, open-source .NET client library for RabbitMQ that simplifies the process of sending and receiving messages. It provides a high-level API that handles complex tasks like connection management, serialization, and exchange or queue declarations automatically.
- **Ocelot**
  - Ocelot is an open-source API gateway designed for ASP.NET Core applications that acts as a single entry point for a microservices architecture. It functions as a reverse proxy that receives incoming HTTP requests and routes them to the appropriate downstream services based on predefined configuration.
- **YARP**
  - YARP is a library to help create reverse proxy servers that are high-performance, production-ready, and highly customizable. YARP is built on .NET using the infrastructure from ASP.NET and .NET (.NET 6 and newer).
- **Docker**
  - Docker is an open-source platform that automates the deployment of applications inside lightweight, portable containers. It packages an ASP.NET Core application along with its dependencies, libraries, and runtime environment into a single unit to ensure consistent behavior across different computing environments.
- **Kubernetes**
  - Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It organizes containers into logical units called pods and ensures they are running across a cluster of machines according to desired configurations.
- **.NET Aspire**
  - .NET Aspire is an opinionated stack for building observable, production-ready cloud-native .NET applications. It provides curated packages for common cloud dependencies, service discovery, orchestration for local development, and built-in telemetry to make distributed applications easier to build and debug.
- **Orleans**
  - Orleans is a cross-platform framework for building robust, scalable distributed applications in .NET. It simplifies the development process by using a virtual actor model that allows developers to create stateful, distributed objects without needing to manage complex concurrency, persistence, or messaging concerns manually.
- **Dapr**
  - Dapr (Distributed Application Runtime) is an open-source, portable runtime that makes it easy to build microservices-based applications that run on the cloud and edge. It provides a set of building blocks for building microservices, including service discovery, state management, pub-sub messaging, and more.
- **GitLab CI/CD**
  - GitLab CI/CD is the continuous integration and delivery tooling built into GitLab. Pipelines are defined in a .gitlab-ci.yml file, where jobs run on GitLab runners to build, test, and deploy your application automatically on every change.
- **Circle CI**
  - CircleCI is a cloud-based continuous integration and continuous delivery platform that automates the building, testing, and deployment processes for software applications. It utilizes configuration files defined in YAML to manage workflows, allowing developers to execute automated tests and push builds to various environments whenever code changes are committed to a repository.

### 3.7 Template Engines
- **NSubstitute**
  - NSubstitute is a friendly library for .NET used to create and work with mock objects in unit tests. It provides a simple, concise syntax that allows developers to substitute dependencies, define return values for methods, and verify that specific actions were performed during a test execution.
- **Moq**
  - Moq is a popular mocking library for .NET that allows developers to simulate the behavior of complex objects and interfaces during unit testing. It provides a simple API to create "mock" versions of dependencies, enabling you to define specific return values for methods or verify that certain interactions occurred within your code.
- **FakeItEasy**
  - FakeItEasy is a popular mocking library for .NET that allows developers to create fake objects for unit tests with a simple and readable syntax. It simplifies the process of stubbing methods, properties, and events, enabling you to isolate the code being tested from its dependencies.
- **Razor**
  - Razor is a markup syntax that allows developers to embed server-based code into web pages using C#. It enables the seamless integration of dynamic programming logic directly within HTML, which the server processes to generate the final output sent to the browser.
- **Scriban**
  - Scriban is a fast, powerful, and safe text templating language and engine for .NET. It allows developers to define dynamic templates that can be parsed and rendered with custom data objects.
- **Fluid**
  - Fluid is an open-source template engine for .NET that serves as a .NET implementation of the Liquid template language. It allows developers to create and render text-based templates that are secure, portable, and independent of the underlying application logic.

### 3.8 Frameworks
- **SteelToe**
  - Steeltoe is an open-source project that provides a set of libraries for building cloud-native applications on the .NET platform. The libraries are designed to work with the .NET Core runtime and provide a set of abstractions for common cloud-native patterns, such as service discovery, configuration management, and circuit breaking.
- **Blazor**
  - Blazor is a web framework that allows developers to build interactive web user interfaces using C# instead of JavaScript. It runs .NET code directly in the browser via WebAssembly or handles UI updates on the server through a real-time connection.
- **.NET MAUI**
  - .NET MAUI (Multi-platform App UI) is the cross-platform UI framework for .NET. It lets you build native Android, iOS, macOS, and Windows applications from a single C# and XAML codebase, sharing business logic while still allowing per-platform customizations when needed.
- **Scalar**
  - Scalar is a lightweight API platform for .NET that generates interactive API documentation and a UI for testing endpoints. It integrates with ASP.NET Core as a fast, configurable alternative to the default Swagger UI, built on the OpenAPI specification.
- **MediatR**
  - MediatR is an open-source library for .NET that is designed to simplify the process of handling messages and commands in a clean, decoupled manner. It's particularly useful in applications that use the Command-Query Responsibility Segregation (CQRS) pattern and event-driven architecture.
- **FluentValidation**
  - FluentValidation is an open-source library for .NET that provides a fluent, easy-to-use API for validating domain models. It allows developers to define validation rules using a fluent, chainable syntax.
- **Polly**
  - Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner. It helps manage instability in external services by defining how an application should react when a network request fails or a system resource becomes unresponsive.
- **Marten**
  - Marten is a .NET document database library built on PostgreSQL. It turns PostgreSQL into a document store, letting you persist and query .NET objects as JSON documents while still leveraging SQL features such as indexes, transactions, and native Postgres tooling.
- **Nuke**
  - Nuke is a cross-platform build automation system that allows you to define your build processes using C#. It leverages the power of the .NET ecosystem to provide strongly typed build scripts, enabling you to manage complex tasks like compilation, testing, and deployment directly within your IDE.
- **Benchmark.NET**
  - BenchmarkDotNet is an open-source library for .NET that provides a simple and easy-to-use API for benchmarking the performance of code. It allows you to measure the performance of methods, classes, and entire assemblies, and provides a rich set of features for analyzing and comparing the results.
- **Distributed Lock**
  - A distributed lock coordinates access to a shared resource across multiple processes or services. It prevents concurrent modifications and race conditions by ensuring only one client holds the lock at a time, typically backed by a store such as Redis, ZooKeeper, or a database.

---

## 4. Optional / Specialized Topics

- Triggers
- Razor Pages
- Razor Components
- Dapper
- RepoDB
- NHibernate
- Scrutor
- AutoFac
- Entity Framework 2nd Level Cache
- Memcached
- Solr
- Sphinx
- Cosmos DB
- PostgreSQL
- MariaDB
- MySQL
- Cassandra
- LiteDB
- CouchDB
- NLog
- Odata
- GraphQL .NET
- gRPC
- Web Sockets
- AutoMapper

---

## 5. References

- [ASP.NET Core Roadmap](https://roadmap.sh/aspnet-core)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer
- Data Analyst

### Related Skills
- Python
- C++
- Node.js