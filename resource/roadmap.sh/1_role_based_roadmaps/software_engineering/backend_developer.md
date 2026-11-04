# Backend Developer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/backend
- Related Roles:
  - Frontend Developer
  - Fullstack Developer
  - DevOps Engineer
  - PostgreSQL DBA

---

## 1. Beginner

### 1.1 Introduction
- **Go**
  - Go (Golang) is Google's statically typed, compiled language combining efficiency with ease of use. Features built-in concurrency via goroutines and channels, simple syntax, fast compilation, and a comprehensive standard library.
- **Ruby**
  - Ruby is a high-level, object-oriented language known for simplicity, productivity, and elegant syntax. Emphasizes developer happiness and supports multiple paradigms.
- **How does the internet work?**
  - The Internet is a global network of interconnected computers using TCP/IP protocols. Requests travel through ISPs to DNS servers for domain-to-IP translation, then are routed across networks via routers to destination servers.
- **What is HTTP?**
  - HTTP (Hypertext Transfer Protocol) transmits hypertext over the web using a request-response model. Defines message formatting and server-browser communication.
- **What is Domain Name?**
  - Domain names are human-readable internet addresses that translate to IP addresses for computer identification. Consists of a second-level domain ("example") and a top-level domain (".com").
- **What is hosting?**
  - Hosting provides server space and resources for storing and delivering websites over the internet. Types include shared hosting, VPS, dedicated hosting, and cloud hosting with scalable resources.
- **DNS and how it works?**
  - DNS (Domain Name System) translates human-readable domain names into IP addresses. Uses hierarchical structure with root servers, TLD servers (.com, .org), authoritative servers, and local DNS servers.
- **Browsers and how they work?**
  - Web browsers interpret HTML, CSS, and JavaScript to render web pages. Modern browsers use rendering engines (Blink, Gecko, WebKit) and JavaScript engines, offering features like tabs, bookmarks, extensions, and security through sandboxing and HTTPS enforcement.

### 1.2 Frontend Basics
- **HTML**
  - HTML (HyperText Markup Language) is the standard markup language for creating web pages. It provides the structure and content of a website by using elements, which are defined by tags, to organize text, images, and other multimedia.
- **CSS**
  - CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML or XML (including XML dialects such as SVG, MathML or XHTML). It controls the layout, colors, fonts, and other visual aspects of web pages, ensuring a consistent and visually appealing user experience.

### 1.3 Pick a Backend Language
- **Rust**
  - Rust is a systems programming language focused on safety, performance, and concurrency. Provides memory safety without garbage collection through ownership model preventing null pointers and data races.
- **PHP**
  - PHP (Hypertext Preprocessor) is an open-source scripting language for web development embedded in HTML to create dynamic pages. Known for simplicity and database integration, particularly MySQL.
- **JavaScript**
  - JavaScript is a versatile, high-level language for web interactivity and dynamic features. Runs client-side in browsers and server-side with Node.js for full-stack development.
- **Java**
  - Java is Oracle's high-level, object-oriented language following "write once, run anywhere" via JVM. Features automatic memory management, vast standard library, and strong security.
- **Python**
  - Python is a high-level, interpreted language known for readability, simplicity, and versatility. Supports multiple paradigms with rich ecosystem including Django/Flask (web), Pandas/NumPy (data), TensorFlow/PyTorch (ML).
- **C#**
  - C# is Microsoft's modern, object-oriented language combining C++ power with Visual Basic simplicity. Used for Windows apps, ASP.NET web development, Unity games, and Xamarin mobile apps.
- **MySQL**
  - MySQL is an open-source RDBMS known for speed, reliability, and ease of use. Supports SQL, transactions, indexing, and stored procedures.

### 1.4 Version Control Systems
- **Git**
  - Git is a distributed version control system created by Linus Torvalds in 2005. Tracks code changes, enables collaborative development, maintains complete history, and supports branching/merging.
- **JavaScript**
  - JavaScript is a programming language primarily used to add interactivity to websites. It allows developers to create dynamic content, control multimedia, animate images, and much more, enhancing the user experience beyond static HTML and CSS.

### 1.5 Repo Hosting Services
- **GitHub**
  - GitHub is Microsoft's web-based Git hosting platform offering repositories, pull requests, issues, and automated workflows. Supports public/private repos, code review, project management, and social coding features.
- **GitLab**
  - GitLab is a comprehensive DevOps platform providing source code management, CI/CD, issue tracking, and more in one application. Features merge requests, built-in pipelines, container registry, and Kubernetes integration.

---

## 2. Intermediate

### 2.1 Relational Databases
- **PostgreSQL**
  - PostgreSQL is an advanced, open-source RDBMS known for robustness, extensibility, and standards compliance. Supports complex queries, custom data types, full-text search, and ACID properties.
- **MS SQL**
  - Microsoft SQL Server is a relational database management system for structured data management. Supports querying, transactions, data warehousing with T-SQL, SSIS integration, SSAS analytics, and SSRS reporting.
- **Oracle**
  - Oracle Database is an enterprise-grade RDBMS known for scalability, reliability, and comprehensive features. Supports complex data management, SQL querying, transaction management, clustering, and multiple data models (relational, spatial, graph).
- **MariaDB**
  - MariaDB is a community-developed MySQL fork created by original MySQL team members. Designed as a feature-rich, stable, drop-in replacement for MySQL with better licensing.
- **N+1 Problem**
  - The N+1 problem occurs when an application retrieves a list then performs additional queries for each item's related data. Results in inefficient query multiplication (1 + N queries instead of optimized joins).
- **JSON APIs**
  - JSON (JavaScript Object Notation) is an encoding scheme eliminating ad-hoc code for server communication. JSON API provides a standardized implementation for data stores and structures, including entity types, bundles, and fields with defined communication protocols.
- **SOAP**
  - SOAP (Simple Object Access Protocol) is a structured message protocol for exchanging information between systems and applications. SOAP APIs are developed in formal, structured ways.
- **gRPC**
  - gRPC is a high-performance, open-source RPC (Remote Procedure Call) framework. Allows programs to execute procedures on remote computers like local functions.
- **REST**
  - REST API is an architectural style using standard HTTP methods (GET, POST, PUT, DELETE) to interact with URI-represented resources. It's stateless, requiring complete request information, uses HTTP status codes, and typically communicates via JSON/XML.
- **SQLite**
  - SQLite is a lightweight, serverless, self-contained SQL database engine storing data in a single file. Used in mobile apps, desktop applications, and small websites.
- **Migrations**
  - Database migrations are version-controlled incremental schema changes that modify database structure without affecting existing data. Ensure consistent, repeatable evolution across environments while maintaining compatibility.

### 2.2 Learn about APIs
- **Open API Specs**
  - OpenAPI Specification (OAS), formerly Swagger, is a standard for defining and documenting RESTful APIs in YAML/JSON format. Describes endpoints, formats, authentication, and metadata.
- **GraphQL**
  - GraphQL is Facebook's query language for APIs, allowing clients to request exactly the data they need. Uses a single endpoint with schema-defined data structure, reducing over-fetching and under-fetching.
- **Authentication**
  - API authentication verifies client identity to ensure only authorized access to resources. Common methods include API keys, OAuth 2.0, JWT, and basic auth.

### 2.3 Caching
- **HTTP Caching**
  - Client-side caching stores data locally on user devices to improve performance and reduce server load. Uses HTTP caching headers, service workers, and local storage APIs.
- **Web Security**
  - Web security protects applications from threats through strong authentication, encryption (SSL/TLS), input validation preventing SQL injection and XSS attacks, secure coding practices, session management, regular updates, and ongoing security testing including penetration testing.
- **Redis**
  - Redis is an open-source, in-memory data structure store supporting strings, lists, sets, hashes, and sorted sets. Used for caching, session management, real-time analytics, and message brokering.
- **Memcached**
  - Memcached is a distributed memory-caching system that speeds up dynamic websites by caching data and objects in RAM. Provides large distributed hash table across multiple machines with LRU eviction.
- **MD5**
  - MD5 (Message-Digest Algorithm 5) produces 128-bit hash values as 32-character hexadecimal strings. Once popular for data integrity and passwords, now considered cryptographically broken due to collision vulnerabilities.
- **SHA**
  - SHA (Secure Hash Algorithm) is a family of cryptographic hash functions generating fixed-size hash values for data integrity and security. Includes SHA-1 (weak, 160-bit), SHA-2 (stronger, 224-512 bits), and SHA-3 (latest with additional security features).
- **JWT**
  - JWT (JSON Web Token) securely transmits information as JSON objects with three parts: header (token type/algorithm), payload (claims/data), and signature (integrity verification). Used for authentication and authorization in web/mobile apps.
- **Basic Authentication**
  - Basic Authentication sends base64-encoded username:password in HTTP headers. Simple to implement but insecure since base64 is easily decoded.
- **Token Authentication**
  - Token-based authentication verifies user identity and provides unique access tokens. Users access protected resources without re-entering credentials while token remains valid.
- **OAuth**
  - OAuth is an open authorization standard allowing third-party applications to access user resources without exposing credentials. Uses access tokens issued after user permission, involving the resource owner, the resource server, and the authorization server.
- **Cookie Based Auth**
  - Cookie-based authentication maintains user sessions by storing session IDs in browser cookies. Server stores session data and uses cookies as keys.
- **OpenID**
  - OpenID is an open standard for decentralized authentication enabling single sign-on across multiple websites using one set of credentials managed by an identity provider. Often works with OAuth 2.0 for authorization, enhancing user convenience and streamlining identity management.
- **SAML**
  - SAML (Security Assertion Markup Language) is an XML-based framework for single sign-on (SSO) and identity federation. Enables authentication exchange between identity providers (IdP) and service providers (SP) through XML assertions containing user identity and permissions.

### 2.4 Learn about Web Servers
- **Nginx**
  - Nginx is a high-performance web server and reverse proxy known for efficiency and low resource consumption. Also used as load balancer, HTTP cache, and mail proxy.
- **Caddy**
  - Caddy is a modern Go-based web server known for simplicity and automatic HTTPS with Let's Encrypt certificates. Features zero-config static file serving, HTTP/2 support, and plugins for reverse proxying and load balancing.
- **Apache**
  - Apache HTTP Server is a popular open-source web server known for flexibility and extensive features. It supports multiple OS platforms, offers virtual hosting, SSL/TLS, and modular architecture.
- **MS IIS**
  - Microsoft IIS is a flexible, secure web server for hosting web applications on Windows Server. Supports ASP.NET, PHP, static content with features like authentication, SSL/TLS, URL rewriting.

### 2.5 Learn the Basics
- **How LLMs work**
  - LLMs, or Large Language Models, are advanced AI models trained on vast datasets to understand and generate human-like text. They can perform a wide range of natural language processing tasks, such as text generation, translation, summarization, and question answering.
- **AI vs Traditional Coding**
  - Traditional software development relies on developers explicitly writing code to instruct computers on how to perform tasks. This involves defining every step and logic manually.
- **Vectors**
  - Vectors are mathematical objects that have both magnitude (length) and direction. They are often represented as ordered lists of numbers, called components.
- **Embeddings**
  - Embeddings are dense, continuous vector representations of data, such as words, sentences, or images, in a lower-dimensional space. They capture the semantic relationships and patterns in the data, where similar items are placed closer together in the vector space.

### 2.6 AI Assisted Coding
- **scrypt**
  - scrypt is a memory-hard key derivation function designed to resist brute-force and hardware-based attacks (GPUs, ASICs). Combines hash functions with high memory usage and CPU-intensive computation, making large-scale attacks costly and impractical.
- **bcrypt**
  - Bcrypt is a secure password-hashing function based on Blowfish cipher with built-in salt protection. Features adaptive cost factor that increases difficulty over time to resist brute-force attacks.
- **HTTPS**
  - HTTPS (Hypertext Transfer Protocol Secure) extends HTTP with SSL/TLS encryption for secure data transmission. Ensures confidentiality, integrity, and authenticity, protecting against interception and tampering.
- **OWASP Risks**
  - OWASP (Open Web Application Security Project) is an online community producing freely-available articles, methodologies, documentation, tools, and technologies for web application security.
- **SSL/TLS**
  - SSL and TLS are cryptographic protocols providing internet communication security through data encryption. SSL is deprecated due to security flaws; modern browsers no longer support it.
- **CORS**
  - CORS (Cross-Origin Resource Sharing) is a browser security mechanism controlling cross-domain resource access. Uses HTTP headers and preflight requests to determine allowed origins.
- **Server Security**
  - Server security protects servers from threats through patch management, access control, firewalls, encryption, security hardening, regular backups, and monitoring. Ensures confidentiality, integrity, and availability of data and services with continuous threat detection and response.
- **CSP**
  - CSP (Content Security Policy) prevents XSS and code injection attacks by specifying trusted content sources. Implemented via HTTP headers or meta tags, defining rules for scripts, stylesheets, images, and fonts.
- **Claude Code**
  - Claude Code is a family of large language models designed for code generation and understanding. It excels at tasks like code completion, bug finding, documentation, and even translating code between different programming languages.
- **Copilot**
  - Copilot is an AI-powered coding assistant developed by GitHub and OpenAI. It suggests lines of code and entire functions in real-time as you type, based on the context of your code and comments.
- **Cursor**
  - Cursor is an AI-powered code editor designed to enhance developer productivity. It leverages large language models to offer features like code completion, generation, and refactoring suggestions.
- **Antigravity**
  - Antigravity is an AI-powered code completion tool designed to enhance developer productivity. It learns from your coding style and project context to provide intelligent suggestions, autocompletions, and code generation snippets directly within your integrated development environment (IDE).
- **Prompting Techniques**
  - Prompt engineering is the process of crafting effective inputs (prompts) to guide AI models to generate desired outputs. It involves strategically designing prompts to optimize the model’s performance by providing clear instructions, context, and examples.
- **RAGs**
  - Retrieval-Augmented Generation (RAG) is an AI approach that combines information retrieval with language generation to create more accurate, contextually relevant outputs. It works by first retrieving relevant data from a knowledge base or external source, then using a language model to generate a response based on that information.
- **MCP**
  - Model Context Protocol (MCP) is a rulebook that tells an AI agent how to pack background information before it sends a prompt to a language model. It lists what pieces go into the prompt—things like the system role, the user’s request, past memory, tool calls, or code snippets—and fixes their order.
- **Skills**
  - AI coding assistants can now leverage "skills" – pre-defined functions or tools exposed to the AI that allow it to perform specific actions. Instead of relying solely on their internal knowledge and large language models, these assistants can call upon these skills (like running tests, deploying code, or querying databases) when needed.
- **Agents**
  - AI agents are autonomous programs designed to help developers write code more efficiently. These agents can automate repetitive tasks, suggest code completions, identify errors, and even generate entire code blocks based on natural language descriptions or existing code patterns.

### 2.7 Applications
- **Code Reviews**
  - AI-powered code reviews leverage machine learning models to analyze source code and identify potential issues, such as bugs, security vulnerabilities, code style violations, and performance bottlenecks. These tools can automate parts of the code review process, freeing up developers to focus on more complex problems and improving the overall quality and maintainability of the codebase.
- **Documentation Generation**
  - AI-powered documentation generation leverages machine learning models to automatically create and maintain software documentation. These tools can analyze code, comments, and other project artifacts to produce API references, tutorials, and other types of documentation, reducing the manual effort required and ensuring accuracy and consistency.
- **Refactoring**
  - Refactoring, in the context of software development, is the process of restructuring existing computer code—changing its internal structure—without changing its external behavior. AI tools can assist in this process by analyzing code for potential improvements in readability, performance, and maintainability.

### 2.8 Integration Patterns
- **Gemini**
  - Gemini is a family of multimodal large language models (LLMs) developed by Google. These models are designed to handle and understand different types of data, including text, code, images, audio, and video.
- **OpenAI**
  - OpenAI provides a suite of artificial intelligence models and tools accessible through an API. These models can perform tasks like generating text, translating languages, writing different kinds of creative content, and answering your questions in an informative way.
- **Anthropic**
  - Anthropic is an AI safety and research company focused on developing reliable, interpretable, and steerable AI systems. They create AI models, like Claude, that are designed to be helpful, harmless, and honest, prioritizing safety through techniques like Constitutional AI, where the AI is guided by a set of principles during its training and operation.
- **Streaming**
  - Streamed and unstreamed responses describe how an AI agent sends its answer to the user. With a streamed response, the agent starts sending words as soon as it generates them.
- **Structured Outputs**
  - Structured outputs involve prompting LLMs to return responses in specific formats like JSON, XML, or other organized structures rather than free-form text. This approach forces models to organize information systematically, reduces hallucinations by imposing format constraints, enables easy programmatic processing, and facilitates integration with applications.
- **Function Calling**
  - LLM native “function calling” lets a large language model decide when to run a piece of code and which inputs to pass to it. You first tell the model what functions are available.

### 2.9 CI / CD
- **CI / CD**
  - CI/CD automates building, testing, and deploying code changes. Continuous Integration merges code frequently with automated builds/tests.

### 2.10 More about Databases
- **ORMs**
  - ORM (Object-Relational Mapping) allows developers to interact with databases using object-oriented concepts. Maps database tables to classes and rows to objects, eliminating raw SQL queries.
- **Normalization**
  - Database normalization structures relational databases using normal forms to reduce data redundancy and improve integrity. Proposed by Edgar F.
- **ACID**
  - ACID stands for four key database transaction properties: Atomicity (all-or-nothing execution), Consistency (valid state maintenance), Isolation (concurrent transaction separation), and Durability (permanent commit survival). These principles ensure reliable data processing and integrity in database systems, which are crucial for financial and e-commerce applications.
- **Failure Modes**
  - Database failure modes include hardware failures, software bugs, data corruption, performance degradation, and distributed system inconsistencies. Common issues: data loss, unavailability, replication lag, deadlocks.
- **Transactions**
  - Database transactions are series of operations executed as atomic units to ensure data integrity. Follow ACID properties: Atomicity (all-or-nothing), Consistency (valid state), Isolation (no interference), Durability (permanent changes).

### 2.11 Testing
- **Integration Testing**
  - Integration testing verifies interactions between software components to ensure they work together correctly. Tests module communication via APIs, databases, and third-party services.
- **Functional Testing**
  - Functional testing ensures software meets functional requirements through black box testing. Testers provide input and compare expected vs actual output without understanding source code.
- **Unit Testing**
  - Unit testing tests individual components or units in isolation to ensure correct functionality. Focuses on smallest testable parts like functions with predefined inputs and expected outcomes.

---

## 3. Advanced

### 3.1 Message Brokers
- **RabbitMQ**
  - RabbitMQ is an open-source message broker using AMQP for asynchronous communication between distributed systems. Enables message queuing, routing, durability, and acknowledgments.
- **Kafka**
  - Apache Kafka is a distributed event streaming platform for high-throughput, fault-tolerant data processing. Acts as message broker with publish/subscribe model.
- **LXC**
  - LXC (Linux Containers) runs multiple Linux systems virtually on a single Linux kernel. Provides userspace interface for kernel containment features with powerful API and simple tools for creating and managing system or application containers.

### 3.2 Search Engines
- **Server Sent Events**
  - Server-Sent Events (SSE) sends real-time updates from server to client over persistent HTTP connection. Enables efficient server push with automatic reconnection.
- **Elasticsearch**
  - Elasticsearch is a document-oriented search engine and database supporting INSERT, DELETE, RETRIEVE operations and analytics. Unlike general databases, it's optimized for search with powerful features for fast data retrieval based on search criteria.
- **Solr**
  - Solr is an open-source, scalable search platform built on Apache Lucene for full-text search, faceted search, and real-time indexing. Supports complex queries, distributed searching, text analysis, highlighting, and geographic search.

### 3.3 Architectural Patterns
- **Profiling Performance**
  - Performance profiling analyzes system behavior to identify bottlenecks and optimization opportunities. Collects data on CPU, memory, I/O operations, and execution times.
- **Monolith**
  - Monolithic applications are single, cohesive units with tightly integrated components running as one service. Simplifies development and deployment but creates scalability and maintainability challenges.
- **Service Mesh**
  - Service mesh enhances communication, security, and management between microservices using intelligent proxies. Provides load balancing, service discovery, observability, and traffic management.
- **SOA**
  - SOA (Service-Oriented Architecture) uses reusable, loosely coupled services that interact over networks through standardized protocols like HTTP and XML. Each service performs specific business functions independently.
- **Twelve Factor Apps**
  - Twelve-Factor App methodology provides principles for building scalable, maintainable cloud applications. Key factors: single codebase, explicit dependencies, environment config, stateless processes, port binding, dev/prod parity, log streams, and graceful shutdown for portability and deployment ease.
- **Microservices**
  - Microservices architecture structures applications as loosely coupled, independently deployable services focused on specific business capabilities. Communicate via HTTP or messaging.
- **Serverless**
  - Serverless computing lets developers build applications without managing server infrastructure. Cloud providers handle scaling and maintenance while developers deploy event-triggered functions.

### 3.4 Real-Time Data
- **WebSockets**
  - WebSockets enable full-duplex, real-time communication over a single persistent connection between client and server. Unlike HTTP's request-response cycles, allows continuous bidirectional data exchange.
- **Long / Short Polling**
  - Long polling technique where server holds client requests instead of sending empty responses. Server waits for specified period for new data, responding immediately when available or after timeout.

### 3.5 Scaling Databases
- **Database Indexes**
  - Database indexes are data structures that speed up data retrieval by creating references to table data without full table scans. Include B-tree, bitmap, and hash types.
- **Sharding Strategies**
  - Sharding splits large datasets into smaller chunks (logical shards) distributed across different machines/database nodes to distribute traffic load. Improves application scalability.
- **Data Replication**
  - Data replication creates multiple copies of data across distributed system nodes for availability, reliability, and performance. Can be synchronous or asynchronous.
- **CAP Theorem**
  - CAP Theorem states distributed systems can only guarantee two of three properties: Consistency (same data across nodes), Availability (system responds to requests), and Partition tolerance (operates despite network failures). Guides distributed system design decisions and database selection.

### 3.6 NoSQL Databases
- **MongoDB**
  - MongoDB is a NoSQL document-oriented database storing data in BSON format without fixed schemas. Supports horizontal scaling via sharding and high availability through replica sets.
- **CouchDB**
  - Apache CouchDB is a document-oriented NoSQL database using JSON for data storage, JavaScript MapReduce for queries, and HTTP for API access. Stores independent documents with self-contained schemas instead of relational tables.
- **Neo4j**
  - Neo4j is an open-source graph database storing data as interconnected nodes and relationships rather than tables. Uses Cypher query language for efficient graph traversal and pattern matching.
- **Redis**
  - Redis is an open-source, in-memory data structure store supporting strings, lists, sets, hashes, and sorted sets. Used for caching, session management, real-time analytics, and message brokering.
- **DynamoDB**
  - AWS DynamoDB is a fully managed, serverless NoSQL database supporting key-value and document models. Offers single-digit millisecond latency, automatic scaling, global tables, and seamless scalability.
- **Firebase**
  - Firebase is Google's comprehensive mobile and web development platform offering real-time database, authentication, cloud storage, hosting, and analytics. Features serverless architecture, real-time synchronization, multiple auth providers, and development tools for testing and monitoring.
- **RethinkDB**
  - RethinkDB is an open-source, distributed NoSQL database for real-time applications. Features changefeed for automatic data update notifications, JSON document model, rich queries with joins and aggregations.
- **Influx DB**
  - InfluxDB is a high-performance, open-source time-series database for handling timestamped data like metrics and events. Optimized for monitoring, IoT, and APM with SQL-like Flux queries.
- **Cassandra**
  - Cassandra is a NoSQL database designed for handling large amounts of data across many commodity servers, providing high availability with no single point of failure. It uses a distributed architecture to achieve scalability and fault tolerance, making it suitable for applications that require continuous uptime and can tolerate eventual consistency.
- **AWS Neptune**
  - AWS Neptune is a fully managed graph database supporting property graph and RDF models. Uses Gremlin and SPARQL query languages for complex relationships in social networks, recommendations, and fraud detection.
- **ClickHouse**
  - ClickHouse is an open-source, column-oriented database management system designed for online analytical processing (OLAP). It excels at processing large volumes of data quickly, making it suitable for applications that require real-time analysis and reporting.
- **ScyllaDB**
  - ScyllaDB is a NoSQL database designed for high performance and low latency. It's built to be compatible with Apache Cassandra, meaning it uses the CQL (Cassandra Query Language) and offers similar data modeling capabilities.
- **DGraph**
  - DGraph is a distributed, fast, and scalable graph database. It's designed to handle large amounts of data and complex relationships between data points.

### 3.7 Building For Scale
- **Graceful Degradation**
  - Graceful degradation ensures systems continue functioning when components or features are unavailable. In web development, applications remain functional even if browsers don't support certain features.
- **Throttling**
  - Throttling controls the rate of request processing to prevent system overload by setting limits on requests per time period. Manages resource consumption, ensures fair usage, maintains stability, and protects against abuse.
- **Backpressure**
  - Backpressure is a flow control mechanism where receivers signal their capacity to senders, preventing system overload. It manages resource allocation, prevents memory overflows, and maintains responsiveness in reactive programming, message queues, and streaming systems.
- **Loadshifting**
  - Load shifting manages computing workloads by redistributing load from peak to off-peak periods. Helps balance resource demand, optimize performance, and reduce costs through job rescheduling, region switching, and dynamic resource allocation.
- **Circuit Breaker**
  - Circuit breaker pattern protects systems from failures by temporarily stopping operations when overloaded. Has three states: closed (normal), open (stopped operations), and half-open (testing recovery).
- **Instrumentation**
  - Instrumentation embeds code to capture metrics, logs, and traces. Monitoring observes real-time metrics for anomalies and performance issues using dashboards and alerts.
- **Monitoring**
  - Monitoring involves continuously collecting, analyzing, and alerting on metrics, logs, and traces from applications and infrastructure. It helps detect issues early, understand performance bottlenecks, and ensure system reliability.
- **Telemetry**
  - Telemetry automates collection, transmission, and analysis of data from distributed systems to monitor performance and health. Provides real-time insights, identifies issues, optimizes performance.
- **TimescaleDB**
  - TimescaleDB is an open-source time-series database built as PostgreSQL extension. Handles large volumes of time-stamped data efficiently for monitoring, IoT, and financial applications.
- **Observability**
  - Observability monitors system internal state through external outputs like metrics, logs, and traces. Involves collecting, analyzing, and visualizing data for performance insights, anomaly detection, and troubleshooting.

---

## 4. Optional / Specialized Topics

- Open API Specs
- Rust
- PHP
- Java
- C#
- Ruby
- GitLab
- MS SQL
- MySQL
- Oracle
- MariaDB
- ORMs
- Sharding Strategies
- Data Replication
- CAP Theorem
- SOAP
- gRPC
- GraphQL
- RabbitMQ
- Caddy
- Apache
- MS IIS
- Memcached
- CouchDB
- OpenID

---

## 5. References

- [Backend Developer Roadmap](https://roadmap.sh/backend)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Fullstack Developer
- DevOps Engineer
- PostgreSQL DBA

### Related Skills
- System Design
- Python
- JavaScript
- Node.js