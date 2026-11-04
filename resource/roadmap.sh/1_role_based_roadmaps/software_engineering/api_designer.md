# API Designer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/api-design
- Related Roles:
  - Backend Developer
  - DevOps Engineer
  - Frontend Developer

---

## 1. Beginner

### 1.1 Learn the Basics
- **What are APIs**
  - APIs, or Application Programming Interfaces, provide a manner in which software applications communicate with each other. They abstract the complexity of applications to allow developers to use only the essentials of the software they are working with.
- **HTTP**
  - HTTP, or Hypertext Transfer Protocol, is a fundamental piece of any API design. It is the protocol used for transmitting hypermedia data on the web, such as HTML webpages or JSON from a web API.
- **HTTP Versions**
  - HTTP or Hypertext Transfer Protocol is pivotal in the world of API design. HTTP versions specify how data should be packaged and transported, as well as how web servers and browsers should respond to commands.
- **HTTP Methods**
  - HTTP (Hypertext Transfer Protocol) Methods play a significant role in API design. They define the type of request a client can make to a server, providing the framework for interaction between client and server.
- **HTTP Status Codes**
  - HTTP Status Codes are an essential part of API Design, providing important information about the result of a request made to a server. They are 3-digit numbers where the first digit defines the class of response, while the last two digits do not have any categorization value.
- **HTTP Headers**
  - HTTP Headers play a crucial role in API Design as they provide essential information between the client and server regarding the data to be exchanged. Headers are part of the HTTP request and response message, with types including Standard, Non-standard, Common or Uncommon headers.
- **URL, Query & Path Parameters**
  - When designing APIs, an integral part involves dealing with uniform resource locators (URLs), query parameters, and path parameters. These components play crucial parts in how the API sends and retrieves data.
- **Cookies**
  - Cookies play an instrumental role in the field of API (Application Programming Interface) design. Essentially, cookies are small bits of data stored on a user's browser that enables stateful HTTP sessions, by storing pertinent information between server communications.
- **Content Negotiation**
  - In the context of API design, Content Negotiation refers to the process where the client and the server communicate about the data representation which is acceptable for both of them. It allows clients to indicate the preferred response format, such as JSON, XML, or HTML.
- **CORS**
  - Cross-Origin Resource Sharing (CORS) is a critical concept in API Design. It is a mechanism that uses HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin.
- **Understand TCP / IP**
  - When designing APIs, an essential building block is the understanding of TCP/IP. TCP/IP, standing for Transmission Control Protocol/Internet Protocol, is the suite of communications protocols used to connect hosts on the Internet.
- **Basics of DNS**
  - When discussing the foundational elements of API Design, the Basics of DNS (Domain Name System) can't be overlooked. DNS plays a fundamental role in the way APIs function, acting as the internet's equivalent of a phone book, it interprets human-friendly hostnames into IP addresses that APIs need for communication.

### 1.2 Different API Styles
- **RESTful APIs**
  - RESTful APIs, or Representational State Transfer APIs, are a set of conventions for designing networked applications. They utilize HTTP methods to read, update and delete data.
- **Simple JSON APIs**
  - Simple JSON (JavaScript Object Notation) APIs are a popular form of API or "Application Programming Interface" which utilise JSON to exchange data between servers and web applications. This method has gained prominence mainly for its simplicity, light weight, and easy readability.
- **SOAP APIs**
  - SOAP (Simple Object Access Protocol) APIs are a standard communication protocol system that permits programs that run on different operating systems (like Linux and Windows) to communicate using Hypertext Transfer Protocol (HTTP) and its Extensible Markup Language (XML). In the context of API Design, SOAP APIs offer a robust and well-defined process for interaction between various software applications, mostly over a network.
- **GraphQL APIs**
  - GraphQL is an open-source data query and manipulation language for APIs, and a runtime for executing those queries with your existing data. Unlike REST, where you have predefined data return structures for each endpoint, GraphQL APIs are designed around a type system and enable the client application to precisely specify what data it needs from the server.
- **REST Principles**
  - REST (Representational State Transfer) is an important architectural style used in API design. It defines a set of rules and conventions through which systems communicate over a network.
- **URI Design**
  - URI (Uniform Resource Identifier) is a string of characters used to identify a name or a resource on the Internet. Designing URIs carefully is a crucial part of creating a smooth API interface that is easy to understand, remember and use.
- **HTTP Caching**
  - HTTP caching is a key aspect of API design which involves storing copies of responses to HTTP requests to speed up future requests. When an API receives the same request multiple times, instead of processing each request separately, it can use a previously stored response, thereby improving performance and efficiency.
- **gRPC APIs**
  - gRPC is a platform agnostic serialization protocol that is used to communicate between services. Designed by Google in 2015, it is a modern alternative to REST APIs.
- **Resource modeling**
  - Resource modeling is the process of deciding what "things" your API exposes and how they map to URLs. A resource is any noun your API manages, like a user, an order, or a product.
- **Naming Conventions**
  - Naming conventions are the rules you follow to keep your API's URLs, parameters, and field names consistent and predictable. This includes decisions like using plural nouns for collections (/users not /user), lowercase kebab-case for URLs, camelCase or snake\case for JSON fields, and avoiding verbs in resource paths.

### 1.3 Building JSON / RESTful APIs
- **Versioning Strategies**
  - API Versioning is a critical component of API Design and Management. As the APIs evolve over time to meet the new business requirements and functionality enhancements, it is crucial to manage the changes in a way that doesn't break the existing client applications.
- **HATEOAS**
  - Hypertext As The Engine Of Application State (HATEOAS) is a key concept in the design of RESTful APIs (Application Programming Interfaces). It implies that the API delivers data as well as information about available interactions.

### 1.4 Real-time APIs
- **Pagination**
  - Pagination is a crucial aspect of API design, providing a systematic approach to handling large amounts of data in a manageable way. Instead of returning all data in a single response, which can be overwhelming and inefficient, APIs implement pagination to deliver this data in smaller, more convenient parcels.
- **Rate Limiting**
  - Rate Limiting is a critical aspect of API Design that dictates the number of API calls a client can make within a specified timeframe. This helps in managing resource allocation, preventing abuse of the API, and maintaining the overall health of the API system.
- **Idempotency**
  - Idempotency in API design means that making the same request several times has the same effect on the server as making it once. This is what makes retries safe: if a network error hides whether a request succeeded, the client can send it again without, for example, charging a customer twice.
- **CRUD Operations**
  - When designing APIs, one needs to account for various types of interactions with data - these typically revolve around the CRUD operations; Create, Read, Update, and Delete. Whether the API is designed for a banking app or a social media platform, the need to create new data, read or retrieve existing data, update or modify that data, and delete unnecessary data is universal.
- **Web Sockets**
  - Web Sockets provide a long-lived connection between a client and a server over which messages can be sent bi-directionally, in real-time. They play a crucial role in creating real-time APIs by offering a faster and more efficient communication method over the traditional HTTP.
- **Server Sent Events**
  - Server-Sent Events (SSE) represent an explicit concept in the design of Real-time APIs. Unlike traditional approaches where a client sends a request and awaits a response from the server, SSE enables a server to push data to clients whenever a particular event takes place.
- **Filtering, Sorting & Search**
  - Filtering, sorting, and search are query capabilities that let API consumers retrieve exactly the data they need rather than fetching everything and processing it client-side. Filtering narrows results by field values (?status=active), sorting orders them (?sort=created\at&order=desc), and search allows freetext or fuzzy matching across fields.
- **Streaming Responses**
  - Streaming responses allow a server to send data to the client incrementally as it becomes available, rather than buffering the entire response and sending it at once. This is useful for large datasets, file downloads, log tailing, or AI-generated text where the first tokens can be delivered to the user before the full response is ready.

---

## 2. Intermediate

### 2.1 Authentication Methods
- **Error Handling**
  - Error Handling is a crucial aspect of API design that ensures the stability, usability, and reliability of the API in production. APIs are designed to help systems communicate with each other.
- **RFC 7807 -  Problem Details**
  - The practice of API Design includes a significant focus on handling errors effectively and transparently. Among the widespread standards being adopted, the RFC 7807 or Problem Details for HTTP APIs plays a crucial role.
- **Basic Auth**
  - Basic Auth, short for Basic Authentication, is a simple method often used in API design for handling user authentication. In this method, client credentials, consisting of a username and password pair, are passed to the API server in a field in the HTTP header.
- **Token Based Auth**
  - Token-based authentication is a crucial aspect of API design. It involves providing the user with a token that validates their identity after they have successfully logged in.
- **JWT**
  - JSON Web Tokens, or JWT, are a popular and secure method of transferring information between two parties in the domain of API design. As a compact, URL-safe means of representing claims to be transferred between two parties, they play a vital role in security and authorization in modern APIs.
- **OAuth 2.0**
  - OAuth 2.0 is an authorization framework that allows applications to obtain limited access to user accounts on an HTTP service, such as Facebook, GitHub, DigitalOcean, and others. It works by delegating user authentication to the service that hosts the user account and authorizing third-party applications to access the user account.
- **Session Based Auth**
  - Application Programming Interfaces (APIs) are critical for building software applications. Among several key considerations during API design, one is deciding how to implement authentication and security.
- **OIDC**
  - OIDC OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0. While OAuth 2.0 handles authorization (what you can do), OIDC handles authentication (who you are).

### 2.2 Authorization Methods
- **MAC**
  - Mandatory Access Control (MAC) is a security model where the operating system or security kernel controls access to resources based on a fixed set of rules and security clearances. Unlike discretionary access control (DAC) where users can grant access to resources they own, in MAC, access is determined by a central authority.
- **ReBAC**
  - Relationship-Based Access Control (ReBAC) is an authorization model that determines access rights based on the relationships between users and resources. Instead of relying solely on roles or attributes, ReBAC considers the connections and associations between entities within a system.
- **DAC**
  - Discretionary Access Control (DAC) is an access control model where access to resources is determined by the owner of the resource. The owner has the discretion to grant or deny access to other users or groups.
- **ABAC**
  - Attribute Based Access Control (ABAC) is a flexible and powerful authorization method in the realm of API Design. Distinct from Role-Based Access Control (RBAC), which relies on predefined roles and permissions, ABAC uses attributes to build policies and make decisions.
- **PBAC**
  - Policy-Based Access Control (PBAC) is an authorization method that determines access rights based on a set of policies. Instead of directly assigning permissions to users or roles, PBAC evaluates requests against these policies, which define the conditions under which access is granted or denied.
- **RBAC**
  - Role-Based Access Control (RBAC) is a method of managing authorization in API design that assigns system access to users based on their role within an organization. RBAC is crucial in controlling which endpoints a user can call, and what operations they are allowed to execute.

### 2.3 API Keys & Management
- **Scopes & Permissions**
  - Scopes are labels attached to an API key or access token that declare what actions it is allowed to perform. Rather than a single all-or-nothing key, scopes let you issue credentials with fine-grained access.
- **Key Generation & Rotation**
  - Key generation and rotation covers the practices around creating, distributing, and periodically replacing API keys. Generation involves producing keys that are sufficiently random and long to resist brute force.

### 2.4 API Documentation Tools
- **Swagger / Open API**
  - Swagger, also known as OpenAPI (not to be confused with OpenAI), is a set of tools specifically used for designing, building, and documenting RESTful Web services. API developers heavily rely on it due to its incredible feature for designing APIs with a clear and easy-to-understand approach.
- **Postman**
  - Postman is a popular tool in web development for designing, testing, and managing APIs. As a collaborative platform, it simplifies each step of the API lifecycle and streamlines collaboration across teams.
- **Readme.com**
  - Readme.com is an invaluable tool in the realm of API Design, renowned for providing a collaborative platform for creating beautiful, dynamic and intuitive documentation. It's a tool which aids developers in outlining clear, comprehensive documentation for their API interfaces.
- **Stoplight**
  - Stoplight is an advanced tool that offers a comprehensive platform for technical teams to handle all aspects of API design. Leveraging Stoplight, teams can design, document and develop APIs in a more collaborative and streamlined manner.

### 2.5 API Security
- **Common Vulnerabilities**
  - API design is a critical component of modern software development, enabling various applications to communicate and share data. However, as the use of APIs expands, so does the potential for security vulnerabilities.
- **Best Practices**
  - API design has rapidly emerged as a vital component of software development. When designing an API, it is crucial to follow best practices to ensure optimization, scalability, and efficiency.
- **Performance Metrics**
  - API Design performance metrics play a critical role in ensuring APIs are efficient, effective, and absolutely fit for their intended purpose. The performance of an API can profoundly impact the user experience and overall system performance.

### 2.6 API Performance
- **Caching Strategies**
  - Caching in API design serves as a technique that allows you to store copies of data temporarily in places where you can access it more readily. By obtaining this data from high-speed storage rather than slower storage sources, you can help improve the overall speed and performance of the API.
- **Load Balancing**
  - Load Balancing plays a crucial role in the domain of API Design. It primarily revolves around evenly and efficiently distributing network traffic across a group of backend servers, also known as a server farm or server pool.
- **Rate Limiting / Throttling**
  - Rate Limiting, often referred to as Throttling, is a fundamental aspect of API Design aimed at controlling the number of requests a client can make to an API within a specified timeframe. This technique ensures fair usage, enhances security, prevents server overload, and allows an even distribution of resources.
- **Profiling and Monitoring**
  - Profiling and monitoring are critical aspects of API design and implementation. Profiling, in this context, refers to the process of analyzing the behavior of your API in order to understand various performance metrics including response times, request rates, error rates, and the overall health and functionality of your API.
- **Synchronous vs Asynchronous APIs**
  - When designing APIs, one critical decision is whether to create a synchronous or asynchronous API. Synchronous APIs are those that hold a connection open and wait for a response before moving on, hence operating in a sequential manner.

---

## 3. Advanced

### 3.1 API Integration Patterns
- **Performance Testing**
  - Performance Testing in API design refers to the practice of evaluating and ensuring that an API operates reliably and efficiently under varying workloads. Properly conducted performance testing can verify an API's speed, response time, reliability, and scalability.
- **Event Driven Architecture**
  - Event-driven architecture (EDA) is a software design concept that revolves around the production, interpretation, and consumption of events. With regards to API design, EDA grants systems the flexibility to decentralize analytics, microservices, and operations, thus promoting real-time information sharing and reaction.
- **API Gateways**
  - API Gateways act as the main point of entry in a microservices architecture, often responsible for request routing, composition, and protocol translation. They play a significant role in API design by providing a shared layer to handle non-business tasks.
- **Microservices Architecture**
  - When it comes to API Design, Microservices Architecture plays a crucial role. It represents a unique method of developing software systems that focuses on building single-function modules with well-defined interfaces.
- **Error Handling / Retries**
  - Error handling and retries decide how an API and its clients behave when something goes wrong. On the server, good error handling means validating input early, returning the correct HTTP status code (4xx for client mistakes, 5xx for server faults) and a consistent, machine-readable error body, such as the Problem Details format, so clients can react programmatically.

### 3.2 API Testing
- **Webhooks vs Polling**
  - Webhooks and polling are two ways for a client to learn about changes on a server. With polling, the client repeatedly asks the server whether anything has changed, so it controls the request rate but wastes calls when nothing is new and only sees a change on its next check.
- **Batch Processing**
  - Batch Processing refers to the method of handling bulk data requests in API design. Here, multiple API requests are packed and processed as a single group or 'batch'.
- **Unit Testing**
  - Unit Testing, in the context of API design, refers to the process of testing the individual components or functions of an API independently to ensure that each part is working correctly. It is typically performed at the development stage.
- **Integration Testing**
  - Integration testing is a critical aspect of API design. It is a level of software testing where individual units or components are combined and tested as a group.
- **Functional Testing**
  - Functional testing in the context of API design involves validating the endpoints and key-value pairs of an API. It ensures the server response works as expected and assesses the functionality of the API whether it is performing all the intended functions correctly.
- **Load Testing**
  - Load testing is a crucial aspect of API design that ensures reliability, efficiency and performance under varying loads. It primarily focuses on identifying the maximum capacity of the API in terms of the volume of requests it can handle and its subsequent behavior when this threshold is reached or overloaded.
- **BFF Pattern**
  - The Backend for Frontend (BFF) pattern involves creating a dedicated API layer for each type of client, typically one BFF for web, one for mobile, and possibly one for third-party consumers. Rather than forcing all clients to use a single general-purpose API, each BFF is tailored to the exact data shape and interaction patterns its client needs.

### 3.3 Observability
- **Messaging Queues**
  - Messaging Queues play a fundamental role in API design, particularly in creating robust, decoupled, and efficient systems. These queues act like a buffer, storing messages or data sent from a sender (producer), allowing a receiver (consumer) to retrieve and process them at its own pace.
- **Rabbit MQ**
  - RabbitMQ is an open-source message-broker software/system that plays a crucial role in API design, specifically in facilitating effective and efficient inter-process communication. It implements the Advanced Message Queuing Protocol (AMQP) to enable secure and reliable data transmission in various formats such as text, binary, or serialized objects.
- **Kafka**
  - Apache Kafka is a real-time, fault-tolerant, and highly reliable messaging system that's integral to API design. It's primarily used to build real-time data streaming applications and microservices due to its inherent ability to handle high volume data and multi-subscriber support.
- **Mocking APIs**
  - API mocking is a crucial aspect of API design and testing. It involves simulating the behaviors of real APIs to test various aspects of the system without the need of the real API being readily available.
- **Contract Testing**
  - Contract Testing is a critical aspect of maintaining a robust and reliable API infrastructure. In the realm of API design, Contract Testing refers to the method of ensuring that APIs work as anticipated and that changes to them do not break their intended functionality.

### 3.4 API Lifecycle Management
- **GDPR**
  - The General Data Protection Regulation (GDPR) is an essential standard in API Design that addresses the storage, transfer, and processing of personal data of individuals within the European Union. With regards to API Design, considerations must be given on how APIs handle, process, and secure the data to conform with GDPR's demands on data privacy and security.
- **CCPA**
  - The California Consumer Privacy Act (CCPA) is a pivotal state statute meant to enhance privacy rights and consumer protection for individuals within California, United States. API Design greatly impacts compliance with CCPA, as improper management and exposure of user data can potentially violate this law.

### 3.5 Standards and Compliance
- **PCI DSS**
  - Payment Card Industry Data Security Standard (PCI DSS) is a widely accepted set of policies and procedures intended to optimize the security of credit, debit and cash card transactions and protect cardholders against misuse of their personal information. In terms of API Design, building APIs in compliance with PCI DSS is crucial when processing, storing or transmitting credit card information.
- **HIPAA**
  - HIPAA (Health Insurance Portability and Accountability Act) is a critical standard when it comes to API design in the healthcare industry. In essence, it provides the mandate for protecting sensitive patient data.
- **PII**
  - Personal Identifiable Information (PII) under Standards and Compliance is a crucial aspect of API Design. It refers to the secure handling and transmission of personal data such as names, addresses, and credit card numbers, which APIs often deal with.

---

## 4. Optional / Specialized Topics

- HTTP Status Codes
- HTTP Headers
- URL, Query & Path Parameters
- Cookies
- Content Negotiation
- CORS
- Understand TCP / IP
- Basics of DNS
- REST Principles
- URI Design
- HTTP Caching
- gRPC APIs
- Resource modeling
- Naming Conventions
- Web Sockets
- Server Sent Events
- Filtering, Sorting & Search
- Streaming Responses
- JWT
- OAuth 2.0
- Session Based Auth
- OIDC
- PBAC
- RBAC
- Synchronous vs Asynchronous APIs

---

## 5. References

- [API Designer Roadmap](https://roadmap.sh/api-design)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer
- Frontend Developer

### Related Skills
- Python
- Go
- Design System
- Node.js