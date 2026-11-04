# System Design

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/system-design
- Related Roles:
  - Software Architect
  - DevOps Engineer
  - Engineering Manager

---

## 1. Beginner

### 1.1 Introduction
- **What is System Design?**
  - System design is the process of defining the architecture, components, modules, and data flow of a system to satisfy a set of requirements. It covers how different parts of an application talk to each other, how data moves through the system, and how the whole thing holds up under load.
- **How to approach System Design?**
  - Approaching a system design problem starts with clarifying requirements: what the system needs to do, how many users it serves, and what scale it must handle. From there, the design moves through estimating capacity, sketching a high-level architecture, and drilling into individual components like databases, caches, and load balancers.

### 1.2 Performance vs Scalability
- **Performance vs Scalability**
  - Performance and scalability describe different problems in a system. A performance problem shows up when a system is slow for a single user, while a scalability problem shows up when the system is fast for one user but slows down under heavy load.

### 1.3 Latency vs Throughput
- **Latency vs Throughput**
  - Latency is the time it takes to complete a single operation, such as the time between a request and its response. Throughput is the number of operations a system can process in a given time period.

### 1.4 Availability vs Consistency
- **CAP Theorem**
  - The CAP theorem states that a distributed system can only guarantee two out of three properties at the same time: consistency, availability, and partition tolerance. Since network partitions are unavoidable in real systems, the practical choice comes down to consistency versus availability during a partition.

### 1.5 Consistency Patterns
- **Weak Consistency**
  - Weak consistency means that after a write, reads are not guaranteed to see that write immediately, or at all. This model works for use cases where occasional data loss or staleness is acceptable, such as real-time voice or video calls, where getting the latest packet matters more than getting every packet.
- **Eventual Consistency**
  - Eventual consistency guarantees that, given enough time without new writes, all replicas of the data will converge to the same value. Reads immediately after a write might return stale data, but the system resolves this over time.
- **Strong Consistency**
  - After an update is made to the data, it will be immediately visible to any subsequent read operations. The data is replicated in a synchronous manner, ensuring that all copies of the data are updated at the same time.

### 1.6 Availability Patterns
- **Availability Patterns**
  - Availability patterns are established architectural approaches used to ensure a system remains operational and accessible to users, even in the face of failures or unexpected events. These patterns focus on minimizing downtime and maintaining a consistent level of service by incorporating redundancy, fault tolerance, and recovery mechanisms into the system's design.

### 1.7 Background Jobs
- **Fail-Over**
  - Fail-over is the process of automatically switching to a standby system or component when the active one fails. It can be active-passive, where the standby stays idle until needed, or active-active, where multiple systems handle traffic simultaneously and absorb the load of a failed node.
- **Replication**
  - Replication means keeping copies of the same data or service on multiple servers. It improves availability, since a failure on one node does not take down the whole system, and it can improve read performance by spreading requests across replicas.
- **Event-Driven**
  - An event-driven background job runs in response to something happening in the system, such as a new file upload or a user signing up. A message or event triggers the job asynchronously, decoupling the action that caused it from the processing that handles it.
- **Schedule Driven**
  - A schedule driven background job runs at fixed times or intervals, regardless of whether a specific event has occurred. Cron jobs are a common example, running tasks like nightly reports or periodic cleanups.

### 1.8 Domain Name System
- **Returning Results**
  - Background jobs execute asynchronously in a separate process, or even in a separate location, from the UI or the process that invoked the background task. Ideally, background tasks are "fire and forget" operations, and their execution progress has no impact on the UI or the calling process.
- **Microservices**
  - Microservices is an architectural style where an application is built as a collection of small, independently deployable services, each responsible for a specific piece of functionality. Services communicate with each other over a network, typically through APIs or messaging.
- **Key-Value Store**
  - A key-value store organizes data as a simple collection of keys, each mapped to a value, with no fixed schema for the value's contents. This simplicity makes lookups by key very fast and the store easy to scale horizontally.

---

## 2. Intermediate

### 2.1 Content Delivery Networks
- **Availability in Numbers**
  - Availability is often expressed as a percentage of uptime over a year, commonly referred to by the number of nines, such as 99.9% or 99.99%. Each additional nine represents significantly less allowed downtime per year, and pushing availability higher gets progressively harder and more expensive.
- **Push CDNs**
  - A push CDN requires the origin server to actively upload content to the CDN ahead of time, rather than waiting for a request. This suits sites with relatively small amounts of content that does not change frequently, since it gives full control over what gets stored and when it updates.
- **Pull CDNs**
  - A pull CDN fetches content from the origin server the first time a user requests it, then caches that content for subsequent requests until it expires. This keeps the CDN in sync with the origin automatically, since new or updated content gets pulled in on demand.

### 2.2 Load Balancers
- **LB vs Reverse Proxy**
  - A load balancer and a reverse proxy both sit in front of backend servers, but they serve different primary purposes. A load balancer's main job is distributing traffic across multiple servers, while a reverse proxy's main job is forwarding requests to a backend and adding features like caching, compression, or SSL termination.
- **Load Balancing Algorithms**
  - Load balancing algorithms determine how a load balancer picks which server handles the next request. Common approaches include round robin, which cycles through servers in order, least connections, which sends traffic to the server with the fewest active requests, and IP hash, which routes based on the client's address.
- **Layer 7 Load Balancing**
  - Layer 7 load balancing operates at the application layer of the network stack, meaning it can inspect the actual content of a request, such as the URL, headers, or cookies. This allows routing decisions based on the content of the request itself, like sending API traffic to one set of servers and image requests to another.
- **Layer 4 Load Balancing**
  - Layer 4 load balancers look at info at the transport layer to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet.
- **Horizontal Scaling**
  - Horizontal scaling means adding more machines to a system to handle increased load, as opposed to vertical scaling, which adds more resources to an existing machine. It generally offers better fault tolerance, since the failure of one machine does not take down the entire system.

### 2.3 Application Layer
- **Service Discovery**
  - Service discovery is the mechanism that lets services in a distributed system find each other's network locations without hardcoding IP addresses. As services scale up, down, or move between hosts, a service discovery system keeps track of where each instance currently lives.
- **Document Store**
  - A document store saves data as documents, typically in formats like JSON or BSON, where each document can have a different structure. This flexibility suits applications with evolving or irregular data shapes, since there is no need to alter a fixed schema for every change.
- **Wide Column Store**
  - A wide column store organizes data into rows and columns, but unlike a relational table, different rows can have different columns, and columns can be grouped for efficient reads and writes. This structure works well for large-scale write-heavy workloads that need fast access to specific columns across huge amounts of data.
- **Graph Databases**
  - A graph database stores data as nodes and edges, representing entities and the relationships between them. This structure is efficient for queries that involve traversing connections, such as finding mutual friends in a social network or recommending related products.

### 2.4 Databases
- **SQL vs NoSQL**
  - SQL databases store data in structured tables with predefined schemas and relationships, and they support complex queries through SQL. NoSQL databases store data in more flexible formats, such as key-value pairs, documents, or graphs, and generally trade strict consistency and rigid schemas for better horizontal scalability.
- **Replication**
  - Replication means keeping copies of the same data or service on multiple servers. It improves availability, since a failure on one node does not take down the whole system, and it can improve read performance by spreading requests across replicas.
- **Sharding**
  - Sharding splits a database horizontally, distributing rows of the same table across multiple database servers based on a shard key, such as user ID. Each shard holds a subset of the total data, which allows the system to scale beyond what a single server could handle.
- **Federation**
  - Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: forums, users, and products, resulting in less read and write traffic to each database and therefore less replication lag.
- **Denormalization**
  - Denormalization is the practice of adding redundant data to a database schema to reduce the number of joins needed for common queries. This trades some storage space and write complexity for faster reads, since related data can be fetched in a single query instead of several.

### 2.5 Caching
- **Refresh Ahead**
  - Refresh-ahead is a caching strategy where the system automatically refreshes a cached item before it expires, based on predicted access patterns. This can reduce latency for frequently accessed data by avoiding cache misses altogether.
- **Write-behind**
  - In the write-behind, or write-back, caching strategy, data is written to the cache first and then asynchronously written to the database after some delay. This makes writes very fast from the application's perspective, since it does not wait on the database.

### 2.6 Asynchronism
- **Write-through**
  - In the write-through caching strategy, data is written to the cache and the database at the same time, as part of the same operation. This keeps the cache always consistent with the database, since no write completes without updating both.
- **Cache Aside**
  - Cache-aside, also called lazy loading, is a caching strategy where the application checks the cache first, and on a miss, fetches the data from the database and writes it into the cache for next time. This keeps the cache populated only with data that has actually been requested.
- **Back Pressure**
  - Back pressure is a mechanism for controlling the flow of data or requests when a system component cannot keep up with incoming volume. Instead of letting a queue or buffer grow unbounded, the system slows down or rejects new work until the backlog clears.
- **Task Queues**
  - A task queue holds units of work, called tasks, that are processed asynchronously by one or more worker processes. Producers add tasks to the queue, and workers pull tasks off and execute them independently of the request that created them.
- **Message Queues**
  - A message queue is a component that receives, holds, and delivers messages between different parts of a system, allowing producers and consumers to operate independently of each other's speed or availability. Producers add messages to the queue, and consumers process them at their own pace.

### 2.7 Communication
- **SQL Tuning**
  - SQL tuning is the process of optimizing database queries and schema design to improve performance. It includes techniques like adding appropriate indexes, rewriting slow queries, avoiding unnecessary joins, and analyzing query execution plans to find bottlenecks.
- **HTTP**
  - HTTP, or Hypertext Transfer Protocol, is the foundational protocol for communication on the web, defining how clients and servers exchange requests and responses. It is stateless, meaning each request is handled independently without relying on previous ones, and it uses methods like GET, POST, and PUT to define the type of operation.
- **TCP**
  - TCP, or Transmission Control Protocol, is a connection-oriented protocol that guarantees reliable, ordered delivery of data between two systems. It establishes a connection before sending data and manages retransmission of lost packets and flow control.
- **UDP**
  - UDP, or User Datagram Protocol, is a connectionless protocol that sends data without guaranteeing delivery, order, or error checking. This makes it faster and lighter than TCP, at the cost of reliability.

### 2.8 Idempotent Operations
- **Client Caching**
  - Client caching stores data directly on the user's device, such as in a browser cache or local storage, so repeated requests for the same resource do not need to reach the server at all. This is the fastest form of caching, since it avoids network round trips entirely.
- **CDN Caching**
  - CDN caching stores static content, like images, stylesheets, and scripts, on distributed edge servers close to end users. This reduces the distance data has to travel and offloads traffic from the origin server.
- **Web Server Caching**
  - Web server caching stores responses at the web server level, such as full HTML pages or static resources, so the server can serve them directly without regenerating them for each request. Reverse proxies like Varnish or Nginx are commonly used for this purpose.
- **Database Caching**
  - Database caching stores the results of frequent or expensive database queries so they do not need to be recalculated on every request. Many databases include a built-in caching layer, and applications can also add an external cache in front of the database.
- **Application Caching**
  - Application caching stores computed results or frequently used data directly within the application layer, often in memory, to avoid repeating expensive operations. It can cache anything from database query results to rendered page fragments.

### 2.9 Performance Antipatterns
- **RPC**
  - Remote Procedure Call, or RPC, lets a program call a function on a remote server as if it were a local function call, hiding the details of the network communication involved. The client sends the function name and arguments, the server executes the function, and the result gets sent back.
- **REST**
  - REST, or Representational State Transfer, is an architectural style for designing APIs around resources, identified by URLs, that clients interact with using standard HTTP methods. It emphasizes statelessness, meaning each request contains all the information needed to process it.
- **gRPC**
  - gRPC is a modern RPC framework developed by Google that uses HTTP/2 for transport and Protocol Buffers for serializing data. It supports features like streaming and bi-directional communication, and its binary format makes it faster and more compact than text-based protocols like JSON over HTTP.
- **GraphQL**
  - GraphQL is a query language for APIs that lets clients specify exactly which fields of data they need, rather than receiving a fixed structure from a fixed endpoint. This avoids the problem of over-fetching or under-fetching data common with REST APIs.
- **Busy Database**
  - The busy database antipattern occurs when too much processing logic, such as complex computations or business rules, runs inside the database instead of the application layer. This overloads the database with work it is not optimized for and limits how well it can scale.
- **Busy Frontend**
  - The busy frontend antipattern happens when resource-intensive tasks that could run in the background are instead performed directly within a user-facing request, making the frontend do more work than necessary. This slows down response times for users and limits how many requests the frontend can handle concurrently.
- **Chatty I/O**
  - Chatty I/O refers to a pattern where an application makes many small, frequent calls to a resource, like a database or another service, instead of batching them into fewer, larger calls. Each individual call carries overhead, and this overhead adds up quickly at scale.
- **Improper Instantiation**
  - Improper instantiation in system design refers to the practice of creating unnecessary instances of an object, class or service, which can lead to performance and scalability issues. This can happen when the system is not properly designed, when the code is not written in an efficient way, or when the code is not optimized for the specific use case.
- **Monolithic Persistence**
  - Monolithic Persistence refers to the use of a single, monolithic database to store all of the data for an application or system. This approach can be used for simple, small-scale systems but as the system grows and evolves it can become a bottleneck, resulting in poor scalability, limited flexibility, and increased complexity.
- **Noisy Neighbor**
  - The noisy neighbor problem occurs when one tenant or workload on a shared resource consumes a disproportionate amount of capacity, degrading performance for other tenants sharing the same infrastructure. It commonly shows up in multi-tenant systems or shared cloud infrastructure.
- **Synchronous I/O**
  - Synchronous I/O blocks the calling thread until an input or output operation, like a network call or disk read, completes. Under high load, this ties up threads waiting on slow operations instead of doing useful work, which limits how many concurrent requests a system can handle.

### 2.10 Monitoring
- **Extraneous Fetching**
  - Extraneous fetching happens when an application retrieves more data than it actually needs for a given operation, wasting bandwidth and processing time. This often occurs from overly broad queries or APIs that always return full objects regardless of what the caller uses.
- **No Caching**
  - The no caching antipattern refers to an application that repeatedly performs expensive operations, like database queries or external API calls, without caching results that could be reused. This creates unnecessary load and latency for data that does not change often.
- **Retry Storm**
  - A retry storm happens when many clients or services retry failed requests at the same time, often after a shared dependency recovers from an outage, overwhelming that dependency again right after it comes back up. This can turn a brief failure into a prolonged outage.
- **Health Monitoring**
  - Health monitoring tracks whether individual components of a system are running and responding correctly, typically through periodic health check requests. A failing health check can trigger alerts or automatic actions, like removing an unhealthy instance from a load balancer's rotation.
- **Availability Monitoring**
  - Availability monitoring tracks whether a system or service is reachable and responding to requests from the perspective of its users. It often involves synthetic checks that simulate real user requests from different locations to measure uptime.
- **Performance Monitoring**
  - Performance monitoring tracks metrics like response time, throughput, and resource usage to understand how well a system is performing under real conditions. It helps identify bottlenecks, slow endpoints, or degrading trends before they cause noticeable problems for users.
- **Security Monitoring**
  - Security monitoring tracks events related to the security of a system, such as failed login attempts, unusual access patterns, or potential intrusions. It helps detect and respond to threats in real time, rather than discovering a breach after the fact.
- **Usage Monitoring**
  - Usage monitoring tracks how a system's resources and features are being used, such as request volume, active users, or feature adoption. This data helps with capacity planning and understanding which parts of a system need more investment.
- **Instrumentation**
  - Instrumentation is the process of adding code to a system that emits data about its internal behavior, such as logs, metrics, and traces. Without instrumentation, there is no data for monitoring tools to collect or analyze.
- **Visualization & Alerts**
  - Visualization and alerts turn raw monitoring data into dashboards and notifications that people can act on. Dashboards give a real-time or historical view of system health, while alerts notify the right people automatically when a metric crosses a concerning threshold.

### 2.11 Cloud Design Patterns
- **Cloud Design Patterns**
  - Cloud design patterns are reusable solutions to common problems encountered when building applications for cloud environments, covering areas like messaging, data management, and resiliency. These patterns address challenges specific to distributed, cloud-hosted systems, such as handling transient failures or coordinating between independently scaled services.

---

## 3. Advanced

### 3.1 Design & Implementation
- **Strangler Fig**
  - Incrementally migrate a legacy system by gradually replacing specific pieces of functionality with new applications and services. As features from the legacy system are replaced, the new system eventually replaces all of the old system's features, strangling the old system and allowing you to decommission it.
- **Static Content Hosting**
  - Static content hosting involves storing fixed files—such as HTML documents, CSS stylesheets, JavaScript files, and images—on a cloud-based storage service rather than serving them directly from a traditional application server. By offloading these files to a distributed storage system, you can serve them to users through a Content Delivery Network (CDN), which caches the data at various geographic locations to reduce latency and decrease the processing load on your primary backend infrastructure.
- **Pipes & Filters**
  - Decompose a task that performs complex processing into a series of separate elements that can be reused. This can improve performance, scalability, and reusability by allowing task elements that perform the processing to be deployed and scaled independently.
- **Leader Election**
  - Coordinate the actions performed by a collection of collaborating instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the others. This can help to ensure that instances don't conflict with each other, cause contention for shared resources, or inadvertently interfere with the work that other instances are performing.
- **Gateway Routing**
  - Gateway routing uses a single entry point to route incoming requests to different backend services based on the request's path, headers, or other attributes. This lets a system present a unified API to clients while internally splitting functionality across multiple services.
- **Gateway Offloading**
  - Offload shared or specialized service functionality to a gateway proxy. This pattern can simplify application development by moving shared service functionality, such as the use of SSL certificates, from other parts of the application into the gateway.

### 3.2 Messaging
- **Sequential Convoy**
  - Sequential Convoy is a pattern that allows for the execution of a series of tasks, or convoy, in a specific order. This pattern can be used to ensure that a set of dependent tasks are executed in the correct order and to handle errors or failures during the execution of the tasks.
- **Scheduling Agent Supervisor**
  - Coordinate a set of distributed actions as a single operation. If any of the actions fail, try to handle the failures transparently, or else undo the work that was performed, so the entire operation succeeds or fails as a whole.
- **Queue-Based Load Leveling**
  - Use a queue that acts as a buffer between a task and a service it invokes in order to smooth intermittent heavy loads that can cause the service to fail or the task to time out. This can help to minimize the impact of peaks in demand on availability and responsiveness for both the task and the service.
- **Publisher/Subscriber**
  - The publisher/subscriber pattern lets a component, the publisher, broadcast messages to multiple subscribers without knowing who or how many are listening. Subscribers register interest in certain types of messages and receive them as they are published.
- **Priority Queue**
  - Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients.
- **Pipes and Filters**
  - Decompose a task that performs complex processing into a series of separate elements that can be reused. This can improve performance, scalability, and reusability by allowing task elements that perform the processing to be deployed and scaled independently.

### 3.3 Data Management
- **Valet Key**
  - The valet key pattern grants a client temporary, limited access directly to a specific resource, like a file in cloud storage, without routing all the data through the application server. This reduces load on the application and improves performance for large data transfers.
- **Static Content Hosting**
  - Static content hosting serves fixed assets, such as images, stylesheets, and scripts, directly from a storage service or CDN instead of through the application server. Since this content does not change per request, serving it separately reduces load on the application and takes advantage of caching and edge distribution.
- **Sharding**
  - Sharding splits a database horizontally, distributing rows of the same table across multiple database servers based on a shard key, such as user ID. Each shard holds a subset of the total data, which allows the system to scale beyond what a single server could handle.
- **Materialized View**
  - Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. This can help support efficient querying and data extraction, and improve application performance.
- **Index Table**
  - Create indexes over the fields in data stores that are frequently referenced by queries. This pattern can improve query performance by allowing applications to more quickly locate the data to retrieve from a data store.
- **Event Sourcing**
  - Event sourcing stores every change to an application's state as a sequence of immutable events, rather than storing just the current state. The current state can always be reconstructed by replaying the events in order, and the full history of changes is preserved.
- **Sidecar**
  - The sidecar pattern deploys supporting components, like logging, monitoring, or networking logic, as a separate process alongside the main application, rather than building that logic directly into the application code. This lets shared infrastructure concerns be updated and reused independently of the application itself.
- **Gateway Aggregation**
  - Gateway aggregation combines multiple backend requests into a single request from the client's perspective, with the gateway making the individual calls to different services and merging the results. This reduces the number of round trips a client needs to make, which is especially useful for clients on slower networks, like mobile devices.
- **CQRS**
  - CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security.
- **Ambassador**
  - The ambassador pattern places a helper service in front of a client to handle networking concerns, like retries, monitoring, or protocol translation, on the client's behalf. This lets the main application focus on its core logic while the ambassador manages the complexity of communicating with external services.

### 3.4 Reliability Patterns
- **Competing Consumers**
  - Enable multiple concurrent consumers to process messages received on the same messaging channel. With multiple concurrent consumers, a system can process multiple messages concurrently to optimize throughput, to improve scalability and availability, and to balance the workload.

### 3.5 Availability
- **External Config Store**
  - Move configuration information out of the application deployment package to a centralized location. This can provide opportunities for easier management and control of configuration data, and for sharing configuration data across applications and application instances.
- **Compute Resource Consolidation**
  - Consolidate multiple tasks or operations into a single computational unit. This can increase compute resource utilization, and reduce the costs and management overhead associated with performing compute processing in cloud-hosted applications.
- **Backends for Frontend**
  - The backends for frontend pattern creates separate backend services tailored to the specific needs of different client types, such as mobile apps versus web browsers, rather than exposing one generic backend to all clients. Each backend can shape its API and responses to fit what that particular client needs.
- **Anti-Corruption Layer**
  - An anti-corruption layer sits between two systems with different data models or logic, translating requests and responses so that one system's design does not leak into and pollute the other. It is often used when integrating a new system with a legacy system, keeping the new system's model clean and independent.
- **Deployment Stamps**
  - The deployment stamp pattern involves provisioning, managing, and monitoring a heterogeneous group of resources to host and operate multiple workloads or tenants. Each individual copy is called a stamp, or sometimes a service unit, scale unit, or cell.
- **Geodes**
  - The Geode pattern involves deploying a collection of backend services into a set of geographical nodes, each of which can service any request for any client in any region. This pattern allows serving requests in an active-active style, improving latency and increasing availability by distributing request processing around the globe.
- **Health Endpoint Monitoring**
  - Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. This can help to verify that applications and services are performing correctly.
- **Throttling**
  - Control the consumption of resources used by an instance of an application, an individual tenant, or an entire service. This can allow the system to continue to function and meet service level agreements, even when an increase in demand places an extreme load on resources.

### 3.6 High Availability
- **CQRS**
  - CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security.
- **Cache-Aside**
  - Load data on demand into a cache from a data store. This can improve performance and also helps to maintain consistency between data held in the cache and data in the underlying data store.
- **Deployment Stamps**
  - The deployment stamps pattern deploys multiple independent copies, or stamps, of an application's infrastructure, each serving a subset of users or tenants. This limits the blast radius of a failure to a single stamp rather than the entire user base, and allows scaling by adding more stamps rather than growing one large deployment.
- **Geodes**
  - The Geode pattern involves deploying a collection of backend services into a set of geographical nodes, each of which can service any request for any client in any region. This pattern allows serving requests in an active-active style, improving latency and increasing availability by distributing request processing around the globe.

### 3.7 Resiliency
- **Choreography**
  - Choreography is an approach to coordinating a distributed workflow where each service reacts to events and decides its own next action, rather than a central controller directing the process. Services publish events when they complete a step, and other services listen and respond accordingly.
- **Claim Check**
  - Split a large message into a claim check and a payload. Send the claim check to the messaging platform and store the payload to an external service.
- **Async Request Reply**
  - The async request-reply pattern decouples a client's request from the actual processing time of a backend operation, useful when that operation takes longer than a typical HTTP request should wait for. The client gets an immediate acknowledgment along with a way to check status later, such as a polling endpoint or callback.
- **Bulkhead**
  - The Bulkhead pattern is a type of application design that is tolerant of failure. In a bulkhead architecture, elements of an application are isolated into pools so that if one fails, the others will continue to function.
- **Circuit Breaker**
  - The circuit breaker pattern monitors calls to a remote service or resource and stops sending requests once failures cross a certain threshold, similar to an electrical circuit breaker tripping to prevent damage. While open, it fails fast instead of waiting on a service that is likely to fail anyway, and it periodically tests whether the service has recovered before resuming normal traffic.
- **Compensating Transaction**
  - A compensating transaction undoes the effects of a previous operation when a later step in a multi-step process fails, since distributed transactions cannot always be rolled back atomically like a single database transaction. Each step in the process has a corresponding compensating action defined in advance.

### 3.8 Security
- **Queue-Based Load Leveling**
  - Use a queue that acts as a buffer between a task and a service it invokes in order to smooth intermittent heavy loads that can cause the service to fail or the task to time out. This can help to minimize the impact of peaks in demand on availability and responsiveness for both the task and the service.
- **Health Endpoint Monitoring**
  - Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. This can help to verify that applications and services are performing correctly.
- **Circuit Breaker**
  - Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application.
- **Leader Election**
  - Coordinate the actions performed by a collection of collaborating instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the others. This can help to ensure that instances don't conflict with each other, cause contention for shared resources, or inadvertently interfere with the work that other instances are performing.
- **Retry**
  - The retry pattern automatically re-attempts a failed operation, under the assumption that many failures in distributed systems are transient and will succeed if tried again shortly after. Retries are usually combined with strategies like exponential backoff to avoid overwhelming a struggling service.
- **Scheduler Agent Supervisor**
  - Coordinate a set of distributed actions as a single operation. If any of the actions fail, try to handle the failures transparently, or else undo the work that was performed, so the entire operation succeeds or fails as a whole.
- **Federated Identity**
  - Delegate authentication to an external identity provider. This can simplify development, minimize the requirement for user administration, and improve the user experience of the application.
- **Gatekeeper**
  - Protect applications and services using a dedicated host instance that acts as a broker between clients and the application or service, validates and sanitizes requests, and passes requests and data between them. This can provide an additional layer of security and limit the system's attack surface.
- **Valet Key**
  - Use a token that provides clients with restricted direct access to a specific resource, in order to offload data transfer from the application. This is particularly useful in applications that use cloud-hosted storage systems or queues, and can minimize cost and maximize scalability and performance.

---

## 4. Optional / Specialized Topics

- Horizontal Scaling
- Denormalization
- Message Queues
- Application Caching
- Busy Database
- Busy Frontend
- Chatty I/O
- Improper Instantiation
- Monolithic Persistence
- Noisy Neighbor
- Synchronous I/O
- Availability Monitoring
- Performance Monitoring
- Security Monitoring
- Usage Monitoring
- Instrumentation
- Visualization & Alerts
- Gateway Routing
- Gateway Offloading
- Priority Queue
- Pipes and Filters
- Index Table
- Event Sourcing
- Sidecar
- Gateway Aggregation

---

## 5. References

- [System Design Roadmap](https://roadmap.sh/system-design)

---

## 6. Related Roles / Topics

### Related Roles
- Software Architect
- DevOps Engineer
- Engineering Manager

### Related Skills
- Python
- Java
- Go