# Spring Boot

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/spring-boot
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **Configuration**
  - Spring Core Configuration is the process of configuring the Spring Framework, which involves specifying the various configuration details required for an application to function properly. This can include setting up beans, specifying bean dependencies, configuring aspect-oriented programming (AOP) aspects, and more.
- **Dependency Injection**
  - Spring Boot uses the Spring Framework's Inversion of Control (IoC) container to manage objects and their dependencies. The IoC container is responsible for creating objects, wiring them together, and managing their lifecycle.
- **Spring IOC**
  - Spring IOC (Inversion of Control) is the principle behind Spring's container, where the framework, not the application code, controls the creation and lifecycle of objects. The container reads configuration metadata, whether from annotations or XML, to know which beans to create and how to connect them.
- **Spring AOP**
  - Spring AOP (Aspect-Oriented Programming) lets developers add behavior to existing code without changing it directly, by defining cross-cutting concerns like logging, security, or transaction management as separate aspects. It works by intercepting method calls through proxies and applying the extra logic before, after, or around the original method.
- **Spring MVC**
  - Spring MVC is a web framework within Spring that follows the Model-View-Controller pattern to build web applications and REST APIs. A central component called DispatcherServlet receives incoming requests and routes them to the appropriate controller, which processes the request and returns a model and view or a JSON response.
- **Annotations**
  - OAnnotations are metadata markers placed on classes, methods, or fields that tell Spring how to treat a piece of code, such as @Component to register a bean or @Autowired to inject a dependency. Spring Boot relies heavily on annotations to reduce configuration files, using ones like @SpringBootApplication to bootstrap an entire application with sensible defaults.
- **Spring Bean Scope**
  - In the Spring Framework, a bean is an object that is instantiated, assembled, and managed by the Spring IoC container. One of the key features of the Spring container is its ability to manage the lifecycle of beans, which includes creating, configuring, and destroying beans as necessary.
- **Terminology**
  - Spring Boot terminology includes core concepts such as beans, application context, dependency injection, and auto-configuration. A bean is an object managed by the Spring container, while the application context is the environment that holds and wires these beans together.
- **Architecture**
  - Spring's architecture is built around a container that manages application objects, called beans, and wires their dependencies together. It follows a modular design, split into core modules for dependency injection, data access, web, and testing, so applications can use only the parts they need.
- **Why use Spring?**
  - Spring reduces the complexity of building Java applications by handling object creation, dependency wiring, and configuration through its container. It offers a consistent programming model across web, data access, security, and messaging, so teams do not need to combine unrelated libraries by hand.

### 1.2 Spring Security
- **Authentication**
  - Spring Security is a framework for securing Java-based applications. One of its core features is authentication, which is the process of verifying that a user is who they claim to be.
- **Authorization**
  - Spring Security supports a variety of authentication mechanisms, such as username and password authentication, OAuth2, and more. Once a user is authenticated, Spring Security can then be used to authorize that user's access to specific resources or functionality.
- **OAuth2**
  - Spring Security OAuth2 library provides support for both the authorization code grant type (for web apps) and the implicit grant type (for single-page apps). You can also use Spring Security to protect your resources and to configure your application as an OAuth2 resource server.
- **JWT Authentication**
  - Spring Security can be used to implement JWT Authentication and Authorization to your APIs. The library provides a JWT-based authentication filter that you can add to your API endpoints.

### 1.3 Spring Boot Starters
- **Spring Boot Starters**
  - Spring Boot starters are a set of convenient dependency descriptors that you can include in your application. They provide a variety of functionality, such as security, data access, and web services, and help to minimize the amount of boilerplate code and configuration you need to write.

---

## 2. Intermediate

### 2.1 Autoconfiguration
- **Spring Cloud Gateway**
  - Spring Cloud Gateway is a Spring Framework library for building API gateways. An API gateway is a service that acts as an intermediary between an application and a set of microservices.

### 2.2 Actuators
- **Cloud Config**
  - Spring Cloud Config is a library for managing configuration properties for distributed applications. It allows developers to externalize configuration properties for an application, so that they can be easily changed without modifying the application's code.

### 2.3 Embedded Server
- **Spring Cloud Circuit Breaker**
  - Spring Cloud Circuit Breaker is a library for managing the fault tolerance of microservices-based applications using the Circuit Breaker pattern. The Circuit Breaker pattern is a design pattern that helps to prevent cascading failures and improve the resilience of distributed systems.

### 2.4 Hibernate
- **Transactions**
  - A transaction is a group of database operations that are executed as a single unit, so that either all of them succeed or none of them take effect. Spring manages transactions declaratively through the @Transactional annotation, which wraps a method in a transaction and rolls back changes if an exception occurs.
- **Relationships**
  - Using hibernate, if we want to have relationship between two entities, there must exist a foreign key relationship between the tables, we call it as Referential integrity. The main advantage of having relationship between objects is, we can do operation on one object, and the same operation can transfer onto the other object in the database.
- **Entity Lifecycle**
  - Entity lifecycle describes the different states an object managed by Hibernate can go through: transient, persistent, detached, and removed. A transient entity exists only in memory and is not tracked by Hibernate, while a persistent entity is attached to a session and synchronized with the database.

---

## 3. Advanced

### 3.1 Spring Data
- **Spring Data JPA**
  - Spring Data JPA is a library that makes it easy to implement Java Persistence API (JPA) based repositories (a fancy word for "DAO") for Spring applications. It's an abstraction on top of JPA that allows you to use a simpler and more convenient API for performing CRUD (Create, Read, Update, Delete) operations on databases.
- **Spring Data MongoDB**
  - Spring Data MongoDB is a module that provides an abstraction for working with MongoDB, a document-oriented NoSQL database, using the same repository pattern as other Spring Data modules. It maps Java objects to MongoDB documents and lets developers query data using repository method names or the MongoTemplate class for more complex operations.
- **Spring Data JDBC**
  - Spring Data JDBC is a lightweight alternative to Spring Data JPA that maps Java objects to database tables using plain JDBC instead of a full ORM like Hibernate. It follows a simpler model, where entities are loaded and saved as a whole aggregate without lazy loading or a persistence context to track changes.

### 3.2 Microservices
- **Spring Cloud**
  - Spring Cloud is a collection of libraries and tools for building cloud-native applications using the Spring Framework. It provides a set of abstractions and implementations for common patterns and best practices used in cloud-based applications, such as service discovery, configuration management, and circuit breaker patterns, among others.
- **Spring Cloud Open Feign**
  - Spring Cloud OpenFeign is a library for creating declarative REST clients in Spring applications. It allows developers to easily make HTTP requests to other microservices or remote services, without having to manually write the low-level code to handle the requests and responses.

### 3.3 Spring MVC
- **Micrometer**
  - Micrometer is a vendor-neutral metrics facade for Java and the default metrics library in Spring Boot. It exposes application metrics — timers, gauges, counters, and histograms — through a unified API that can report to backends such as Prometheus, Datadog, or Graphite, and integrates with Spring Boot Actuator.
- **Eureka**
  - Eureka is a service discovery tool from Netflix, integrated into Spring Cloud, that lets microservices register themselves and find other services by name instead of hardcoded addresses. Each service instance registers with a Eureka server on startup and sends periodic heartbeats to confirm it is still available.
- **Servlet**
  - A servlet is a Java class that handles requests and generates responses within a web server, following the Java Servlet API. It works by receiving an HTTP request from a servlet container, such as Tomcat, processing it through a service method, and writing back a response.
- **JSP Files**
  - JSP (JavaServer Pages) files are templates that mix HTML with Java code to generate dynamic web pages on the server before sending them to the browser. A JSP file is compiled into a servlet the first time it is requested, and its output is combined with data passed from a controller to render the final page.
- **Architecture**
  - The Spring MVC (Model-View-Controller) is a web application framework that is part of the Spring Framework. It is designed to make it easy to build web applications using the MVC design pattern.
- **Components**
  - The Spring MVC (Model-View-Controller) framework has several key components that work together to handle the requests and generate the appropriate responses in a web application. There are other supporting components that are used to manage the lifecycle of the application's objects, such as the Spring IoC container and different interceptors that provides additional functionality, such as caching and security.
- **JPA Test**
  - Spring JPA (Java Persistence API) is a library that makes it easy to work with databases and other data stores in a Spring application. Spring JPA uses the Java Persistence API (JPA) to interact with databases and provides an abstraction layer to work with different data stores.

### 3.4 Testing
- **Mock MVC**
  - Spring's MockMvc is a class that allows you to test Spring MVC controllers without the need for an actual web server. It is part of the Spring Test module, which provides a set of testing utilities for Spring applications.
- **@SpringBootTest Annotation**
  - @SpringBootTest This annotation is used to create a fully-configured instance of the Spring ApplicationContext for testing. It can be used to test the application's components, including controllers, services, and repositories, in a real application environment.
- **@MockBean Annotation**
  - MockBean is a Spring annotation that can be used to create a mock implementation of a bean in the Spring application context. When a test is annotated with MockBean, Spring creates a mock implementation of the specified bean and adds it to the application context.

---

## 4. Optional / Specialized Topics

- Spring MVC
- Annotations
- Spring Bean Scope
- Terminology
- Architecture
- Why use Spring?
- Components
- JPA Test

---

## 5. References

- [Spring Boot Roadmap](https://roadmap.sh/spring-boot)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- Java
- Python
- Go