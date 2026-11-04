# Server Side Game Developer

## Metadata
- Type: Role
- Domain: Game Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/server-side-game-developer
- Related Roles:
  - Backend Developer
  - Game Developer
  - Software Architect

---

## 1. Beginner

### 1.1 Server-Side Development
- **Server-Side Development**
  - Server-side development refers to the logic and processing that happens on the server in response to client requests. In game development, it covers networking, game state management, matchmaking, persistence, and the infrastructure that keeps multiplayer sessions running reliably.

### 1.2 TCP
- **Checksum**
  - A TCP checksum covers the header and payload, allowing receivers to detect in-transit corruption. Unlike UDP, the TCP checksum is mandatory and is computed over a pseudo-header that includes source and destination IP addresses in addition to the segment data.
- **Segment Structure**
  - A TCP segment consists of a header and a data payload. The header includes source and destination ports, sequence and acknowledgment numbers, control flags (SYN, ACK, FIN, RST), window size, checksum, and optional fields; these fields together govern connection setup, data flow, and teardown.
- **Connection**
  - A TCP connection is established through a three-way handshake (SYN, SYN-ACK, ACK) and torn down through a four-way FIN exchange. The connection state machine tracks phases from LISTEN through ESTABLISHED to TIMEWAIT, and understanding it helps diagnose issues like half-open connections and port exhaustion on game servers.
- **Resource Usage**
  - TCP connections consume memory and file descriptors on both client and server. Game servers handling thousands of simultaneous players need to manage connection pools carefully, tune kernel parameters, and close idle connections promptly to avoid resource exhaustion.
- **Window Scaling**
  - Window scaling is a TCP option that extends the receive window field beyond its default 16-bit limit, allowing much larger windows needed on high-bandwidth or high-latency links. It is negotiated at connection setup and enables efficient use of modern network capacity.
- **Max Segment Size**
  - Max Segment Size (MSS) is a TCP option that specifies the largest payload a host is willing to receive in a single segment. Negotiated during the handshake, it is typically derived from the network's MTU minus IP and TCP header sizes, and tuning it helps avoid IP fragmentation.
- **Vulnerability**
  - TCP has several known vulnerabilities that attackers can exploit to disrupt or hijack connections. Understanding these weaknesses is important when designing game servers exposed to the public internet.
- **Denial of Service**
  - Denial of Service (DoS) is a malicious attempt to disrupt the regular functioning of a network, service, or server by overwhelming the network or server with a flood of internet traffic. The most common type of DoS attack involves flooding the target with unnecessary requests in an attempt to overload the system.

### 1.3 UDP
- **Reliability**
  - Reliability in UDP refers to application-level mechanisms that compensate for the protocol's lack of built-in delivery guarantees. Because UDP drops packets silently, game networking code often implements acknowledgment systems, sequence numbers, and retransmission logic to ensure critical game state reaches its destination.
- **Datagram**
  - A datagram is a self-contained packet of data transmitted over UDP, carrying enough information to be routed independently without a prior connection. Each datagram includes source and destination addresses but travels without ordering guarantees, making the application responsible for reassembly and loss detection.
- **Congestion Control**
  - Congestion control is the process of regulating how much data a sender pushes onto a network to prevent overwhelming routers and links. In UDP-based game networking, congestion control must be implemented manually, typically by monitoring round-trip times and packet loss rates and adjusting send rates accordingly.
- **Checksum**
  - A checksum is a small value computed from packet data and appended to it, allowing the receiver to detect corruption during transit. UDP includes a 16-bit checksum field; if the received data does not match the recomputed value, the packet is discarded.
- **Packet Structure**
  - Packet structure defines how data is laid out inside a network packet, including header fields and payload organization. Designing a compact, well-defined packet structure reduces bandwidth usage and makes serialization and parsing predictable across clients and servers.

### 1.4 TCP vs UDP
- **Max Segment Scaling**
  - Max Segment Scaling (MSS) is a TCP feature that defines the maximum amount of data that can be received in a single TCP segment. It is specified during the TCP connection establishment phase.
- **Timestamp**
  - The TCP timestamp option records send times in packets, allowing more accurate round-trip time estimation and enabling the PAWS (Protection Against Wrapped Sequence numbers) mechanism. It helps the stack reject old duplicate segments on high-speed links where sequence numbers can wrap quickly.
- **Congestion Control**
  - TCP congestion control algorithms (Reno, CUBIC, BBR, and others) regulate the sending rate to match available bandwidth and avoid overloading the network. They maintain a congestion window that grows on success and shrinks on loss or ECN signals.
- **Reliable Transmission**
  - Reliable transmission in TCP is achieved through sequence numbers, acknowledgments, and retransmission timeouts. The sender keeps unacknowledged data in a buffer and retransmits it if an ACK does not arrive within the timeout period.
- **Flow Control**
  - Flow control prevents a fast sender from overwhelming a slow receiver by having the receiver advertise its available buffer space in the window field. The sender limits its outstanding unacknowledged data to the receiver's advertised window.
- **Connection Hijacking**
  - Connection hijacking is an attack where a third party intercepts an established TCP session and injects or modifies packets as if they were the legitimate client. It exploits the predictability of TCP sequence numbers; using TLS encryption prevents most hijacking attempts.
- **Veto**
  - In the context of TCP vulnerabilities, a veto (also called a RST injection or blind reset attack) allows an attacker to forge a TCP RST packet that causes one or both peers to terminate a valid connection. Sequence number randomization and encrypted transports mitigate this risk.
- **Reliable vs Unreliable**
  - Reliable protocols retransmit lost data until acknowledged; unreliable protocols send data once and discard it on loss. Game networking often mixes both: reliable channels for critical events (player joining, scoring) and unreliable channels for frequent position updates where staleness matters more than loss.
- **Ordered vs Unordered**
  - Ordered delivery means packets are received and passed to the application in the sequence they were sent; unordered delivery allows packets to be processed as they arrive. TCP enforces ordering; UDP does not.
- **Heavy vs Lightweight**
  - A heavy protocol includes built-in features like connection management, reliability, and flow control, which simplify application code but add overhead. A lightweight protocol like UDP shifts those responsibilities to the application, enabling more control over latency and bandwidth at the cost of more implementation work.
- **Packet vs Datagram**
  - A packet is a general term for a unit of data at the network layer; a datagram specifically refers to a UDP unit at the transport layer. The distinction matters when discussing protocol behavior: IP routes packets, and UDP delivers datagrams without connection state.
- **Streaming vs Broadcast**
  - Streaming sends data as a continuous flow from one endpoint to another, as TCP does. Broadcast sends a single packet to all devices on a network segment simultaneously, using a special address.

### 1.5 IP
- **Capability**
  - IP's core capabilities include logical addressing of hosts, fragmentation and reassembly of oversized packets, and routing via intermediate routers. These capabilities define how data traverses from source to destination across heterogeneous networks.
- **Reliability**
  - IP itself provides no delivery guarantees; packets can be lost, duplicated, or reordered without notification to the sender. Applications requiring reliability must use TCP or implement their own acknowledgment and retransmission logic over UDP.
- **Link Capacity**
  - Link capacity is the maximum data rate a network link can carry, measured in bits per second. IP routes packets over links with varying capacities, and congestion occurs when traffic demand exceeds a link's capacity, causing queuing delays and packet drops.
- **ARP**
  - ARP (Address Resolution Protocol) maps IPv4 addresses to MAC addresses on a local network segment. When a host needs to send a packet to an IP address on the same subnet, it broadcasts an ARP request; the owner of that IP replies with its MAC address.
- **DNS**
  - DNS (Domain Name System) resolves human-readable hostnames into IP addresses. It uses a hierarchical distributed database of nameservers; resolvers query root, TLD, and authoritative servers in sequence to find the address for a given domain.

### 1.6 Transactions
- **DHCP**
  - DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, gateways, and DNS server addresses to devices on a network. It operates over UDP and follows a four-step DORA process (Discover, Offer, Request, Acknowledge).

### 1.7 Programming Languages
- **Data Transfer**
  - TCP data transfer moves a byte stream reliably from sender to receiver, with the stack splitting data into segments, numbering them, and retransmitting any that are not acknowledged. The receiver buffers out-of-order segments and delivers them to the application in sequence order.
- **Out-of-Band Data**
  - Out-of-band data in TCP is transmitted via the urgent pointer mechanism, allowing a sender to flag certain bytes as high-priority without waiting for the normal data stream to drain. Its use in practice is limited and largely deprecated in modern network programming.
- **Selective Ack.**
  - Selective Acknowledgment (SACK) is a TCP extension that lets the receiver report exactly which segments arrived, so the sender can retransmit only the missing ones rather than everything after the first loss. It significantly improves throughput on lossy connections.
- **Error Detection**
  - TCP detects transmission errors using its mandatory checksum field, which covers the segment header and data. Corrupted segments are silently discarded, triggering retransmission through the normal acknowledgment and timeout mechanism.
- **C#**
  - C# is Microsoft's statically typed language, tightly integrated with the .NET runtime. It is widely used in game server development, particularly with Unity-based games, and offers modern async/await concurrency, LINQ, and a rich standard library.
- **Java**
  - Java is a statically typed, JVM-based language known for its portability and mature ecosystem. Its garbage collector can introduce latency spikes, but frameworks like Netty and careful GC tuning make it viable for game server development where throughput matters more than sub-millisecond jitter.
- **Byte Manipulation**
  - Network protocols transmit data in big-endian (network byte order), while most processors use little-endian. Byte manipulation functions like htons, htonl, ntohs, and ntohl convert between host and network byte order to ensure interoperability.

### 1.8 Category
- **IPv4**
  - IPv4 is the fourth version of the Internet Protocol, using 32-bit addresses that allow roughly 4.3 billion unique addresses. Address exhaustion led to the development of NAT and ultimately IPv6; IPv4 remains the dominant protocol on most networks today.
- **IPv6**
  - IPv6 is the sixth version of the Internet Protocol, using 128-bit addresses to provide a practically unlimited address space. It also simplifies header processing, removes broadcast in favor of multicast, and includes mandatory support for IPsec.

### 1.9 Security
- **TLS**
  - TLS (Transport Layer Security) is a cryptographic protocol that provides authentication, integrity, and encryption for data transmitted over a network. It is layered above TCP and is used to secure game server APIs, login flows, and any channel where tampering or eavesdropping is a concern.

### 1.10 Socket Programming
- **Address Conversion**
  - Address conversion involves translating between human-readable IP address strings and their binary representations using functions like inetpton and inetntop. Correct conversion is necessary before binding or connecting a socket to an address.
- **Descriptor**
  - A socket descriptor (or file descriptor on Unix-like systems) is an integer handle returned by the OS when a socket is created. All subsequent socket operations (bind, connect, send, recv, close) reference this descriptor, and the OS uses it to track the socket's state and buffers.
- **API**
  - The socket API is a set of system calls (socket, bind, listen, accept, connect, send, recv, close) that provide a uniform interface for network communication across operating systems. Game networking code uses this API directly or through wrappers.
- **BSD Socket**
  - The BSD socket API, originating from Berkeley Unix, is the standard interface for network programming on Unix-like systems including Linux and macOS. It defines the core socket calls that most other socket APIs are modeled after.

---

## 2. Intermediate

### 2.1 Function
- **Datagram Construction**
  - An IP datagram is constructed by prepending an IP header to the upper-layer payload. The header contains version, header length, DSCP, total length, fragmentation fields, TTL, protocol number, header checksum, and source and destination IP addresses.
- **IP Addressing**
  - IP addressing assigns unique numerical labels to network interfaces, enabling packets to be delivered to the correct host. IPv4 uses 32-bit addresses written in dotted-decimal notation; IPv6 uses 128-bit addresses in hexadecimal, solving IPv4 exhaustion.
- **Routing**
  - Routing is the process by which routers forward IP packets toward their destination based on routing tables. Static routes are configured manually; dynamic routing protocols (OSPF, BGP) allow routers to exchange and update reachability information automatically.
- **Sharding**
  - Sharding divides a game world or player population into independent partitions (shards) that run on separate servers or threads. It allows horizontal scaling by ensuring each shard handles only a subset of the total load, with minimal cross-shard communication.

### 2.2 Serialization
- **C/C++**
  - C and C++ give direct control over memory and system resources, producing highly performant server code with predictable latency. C++ is the language of choice for performance-critical game servers and networking engines where garbage collection pauses are unacceptable.
- **Erlang**
  - Erlang is a functional language designed for building distributed, fault-tolerant, concurrent systems. Its actor-based concurrency model and lightweight process scheduler make it well suited for game servers that must manage large numbers of concurrent connections with high availability.
- **JavaScript**
  - JavaScript runs on the server via Node.js, using an event-driven, non-blocking I/O model. It is suitable for game servers with I/O-bound workloads and offers a large ecosystem of packages, though its single-threaded event loop can become a bottleneck for CPU-intensive game logic.
- **Go**
  - Go is a statically typed, compiled language developed by Google, designed for simplicity and efficient concurrency. Its goroutine scheduler and channel-based communication make it a popular choice for game backend services where high concurrency and fast compilation are valued.
- **Winsock**
  - Winsock (Windows Sockets API) is Microsoft's implementation of the BSD socket API for Windows. It is largely compatible with BSD sockets but has Windows-specific extensions and initialization requirements (WSAStartup/WSACleanup).
- **JSON**
  - JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy to read and write for humans, also easy to parse and generate for machines. JSON is a text format that is completely language independent but uses conventions familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, and Python.
- **XML**
  - XML (Extensible Markup Language) is a text-based format for encoding structured data using nested tags. It is verbose and slower to parse than JSON or binary formats, but its schema validation and widespread tooling support make it still used in some game configuration and asset pipelines.
- **TOML**
  - TOML, which stands for Tom's Obvious, Minimal Language, is a configuration file format that is easy to read due to its straightforward and simple syntax. The language is designed to be unambiguous and lean, intending to make it easy for a machine to parse.

### 2.3 Multithreading
- **YAML**
  - YAML (YAML Ain't Markup Language) is a human-friendly data serialization format often used for configuration files. Its indentation-based syntax is readable but sensitive to whitespace errors; it is common in DevOps tooling and game server configuration rather than runtime network protocols.
- **Thread Local Storage**
  - Thread Local Storage (TLS) is a mechanism by which variables are allocated such that each thread gets its own individually allocated variable, but the name of the variable is the same in each thread. In other words, the same variable can simultaneously hold different values for different threads.
- **Fiber**
  - A fiber is a lightweight, cooperatively scheduled unit of execution managed by the application rather than the OS. Fibers yield control explicitly, avoiding the overhead of OS thread context switches and enabling high-concurrency server architectures with lower memory footprint per concurrent task.

### 2.4 Synchronization
- **Barrier**
  - A barrier is a synchronization point where all participating threads must arrive before any of them can proceed. It is used in game server simulation loops where multiple threads compute a phase of game logic and must all finish before the next phase begins.
- **Spinlock**
  - A spinlock is a lock where the waiting thread repeatedly checks (spins) whether the lock is available rather than sleeping. It avoids the overhead of sleeping and waking but wastes CPU cycles while spinning, making it suitable only for very short critical sections.
- **Future & Promises**
  - Futures and promises are abstractions for asynchronous computation results. A promise is set by the producer of a value; a future is the consumer's handle to retrieve that value once available.
- **Condition Variable**
  - A condition variable allows threads to block and wait until a specific condition becomes true, then be woken by another thread. It is used alongside a mutex: one thread holds the mutex, checks a condition, waits on the variable if not met, and is signaled when another thread changes the state.
- **Windows**
  - On Windows, thread-local storage is accessed via the TlsAlloc, TlsSetValue, and TlsGetValue APIs, or the declspec(thread) keyword for static TLS. Windows fiber APIs also allow cooperative multitasking within a single thread.
- **pthread**
  - pthreads (POSIX Threads) is the standard threading API on Unix-like systems. It provides functions for creating and joining threads, as well as synchronization primitives like mutexes, condition variables, and read-write locks used extensively in game server code.
- **Redis**
  - Redis is an in-memory key-value store that supports strings, hashes, lists, sets, sorted sets, and more. Its sub-millisecond latency makes it widely used in game servers for session caching, leaderboards (via sorted sets), pub/sub messaging, and rate limiting.
- **Memcached**
  - Memcached is a high-performance, distributed in-memory caching system for simple key-value pairs. It is used to cache frequently read game data (player profiles, item definitions) and reduce load on primary databases, though it offers fewer data structures than Redis.

### 2.5 Programming Techniques
- **Protobuf**
  - Protocol Buffers (Protobuf) is Google's binary serialization format defined by .proto schema files. It produces compact binary output and generates efficient parsing code in multiple languages, making it a popular choice for high-throughput game server communication.
- **Design Patterns**
  - Design patterns are reusable solutions to recurring software design problems. In game server development, patterns like Observer, Command, State, and Entity-Component-System (ECS) help organize game logic, event handling, and object lifecycle in a maintainable way.
- **TDD**
  - TDD (Test-Driven Development) is a practice where tests are written before the implementation code. Each feature starts with a failing test, then minimal code is written to pass it, followed by refactoring.
- **Dependency Injection**
  - Dependency Injection is a technique where a component receives its dependencies from an external source rather than creating them itself. It decouples components, makes unit testing easier, and allows swapping implementations (such as a mock database during tests) without changing business logic.
- **Dump Analysis**
  - Dump analysis is the process of examining a core dump or crash dump file to diagnose what caused a server process to crash. Tools like GDB (for C/C++) or crash dump analyzers read the memory image and stack traces captured at the time of failure.
- **Functional Programming**
  - Functional programming is a paradigm that treats computation as the evaluation of pure functions and avoids mutable state. Applying functional techniques in game servers, such as immutable data structures and pure transformation functions for game state, reduces bugs caused by shared mutable state in concurrent code.

### 2.6 Databases
- **Semaphore**
  - A semaphore is a synchronization primitive that controls access to a resource pool by maintaining a counter. Threads decrement the counter to acquire a resource and increment it to release; if the counter is zero, acquiring threads block.
- **Coroutine**
  - A coroutine is a function that can suspend its execution and resume later, allowing cooperative multitasking without OS threads. Game servers use coroutines to write asynchronous logic in a sequential style, improving readability over callback-based code.
- **Channel**
  - A channel is a typed conduit for passing data between concurrent goroutines or threads. In Go, channels are the primary synchronization and communication mechanism; in other languages, similar constructs exist as queues or pipes between concurrent workers.
- **MS SQL**
  - Microsoft SQL Server is a relational database management system from Microsoft, offering enterprise features like Always On availability groups, in-memory OLTP, and deep integration with the .NET ecosystem. It is used in game backends running on the Microsoft stack.
- **MySQL**
  - MySQL is a widely used open-source relational database with strong performance for read-heavy workloads. It is commonly used in game backends for player data, leaderboards, and matchmaking records, often paired with read replicas to scale query throughput.
- **PostgreSQL**
  - PostgreSQL is an open-source relational database known for its standards compliance, extensibility, and support for advanced features like JSONB, full-text search, and custom types. Game servers use it for player accounts, transactions, and any data requiring complex relational queries and ACID guarantees.
- **DynamoDB**
  - DynamoDB is Amazon's fully managed NoSQL key-value and document database. It offers single-digit millisecond latency at any scale, automatic sharding, and pay-per-request pricing, making it a common choice for game backends hosted on AWS that need predictable performance without operational overhead.
- **MongoDB**
  - MongoDB is a document-oriented NoSQL database that stores data as JSON-like BSON documents. Its flexible schema and horizontal scaling via sharding make it popular for game backends where player data structures vary and rapid iteration on schemas is needed.
- **Cassandra**
  - Apache Cassandra is a distributed NoSQL database designed for high availability and linear write scalability across many nodes with no single point of failure. Its wide-column model and tunable consistency make it a good fit for game telemetry, event logging, and leaderboards at scale.
- **Couchbase**
  - Couchbase is a distributed NoSQL database combining a key-value store with a document model and a SQL-like query language (N1QL). Its memory-first architecture and built-in caching make it suitable for game backends that need both low-latency lookups and flexible document queries.
- **ORM**
  - An ORM (Object-Relational Mapper) maps database tables to in-application objects, allowing developers to query and manipulate data using the host language rather than raw SQL. Examples include Hibernate (Java), Entity Framework (C#), and GORM (Go).
- **DAL**
  - A Data Access Layer (DAL) is an abstraction layer that isolates database access logic from business logic. It provides a clean interface for querying and persisting data, making it easier to swap database backends or add caching without changing game logic code.

### 2.7 Cipher
- **SSL**
  - SSL (Secure Sockets Layer) is the predecessor to TLS, providing encrypted communication over networks. The term "SSL" is still commonly used to refer to TLS-based certificates and connections, though SSLv3 and earlier are deprecated due to known vulnerabilities.
- **Update Process**
  - The update process is the main loop or event cycle that drives game state forward. In reactive servers, updates are triggered by incoming events or fixed-rate ticks, and the update process applies game rules, advances physics, and produces output events for clients.

### 2.8 RPC / REST
- **REST**
  - REST (Representational State Transfer) is an architectural style for networked APIs that uses HTTP methods (GET, POST, PUT, DELETE) and URLs to represent and manipulate resources. Game backends expose REST APIs for client authentication, player profiles, matchmaking, and other request-response workflows.
- **gRPC**
  - gRPC is an open-source RPC framework developed by Google that uses HTTP/2 for transport and Protocol Buffers for serialization. It supports bidirectional streaming, client and server streaming, and code generation from .proto schemas, making it efficient for game microservice communication.

### 2.9 Message Queues
- **Mutex**
  - A mutex (mutual exclusion lock) ensures only one thread at a time can execute a critical section. Threads attempting to acquire a held mutex are blocked until the holder releases it.
- **Apache Kafka**
  - Apache Kafka is a distributed event streaming platform designed for high-throughput, fault-tolerant, ordered message delivery. Game servers use Kafka for telemetry pipelines, real-time analytics, event sourcing, and broadcasting game events to multiple downstream consumers.
- **RabbitMQ**
  - RabbitMQ is an open-source message broker implementing AMQP. It supports flexible routing through exchanges and bindings, message acknowledgment, dead-letter queues, and consumer load balancing, making it suitable for game backend event pipelines and task queues.

### 2.10 Task-Based
- **goroutine (Go)**
  - A goroutine is Go's lightweight concurrency primitive, scheduled by the Go runtime onto OS threads. Goroutines are cheap to create (starting at a few kilobytes of stack) and communicate via channels, enabling game servers to handle thousands of concurrent connections without complex thread management.
- **Concurrency (Java)**
  - Java's concurrency utilities (java.util.concurrent) provide thread pools, futures, locks, atomic variables, and concurrent collections. They are the foundation for building efficient, safe multithreaded game server code on the JVM, complemented by Project Loom's virtual threads for higher concurrency.
- **Asnc-await (C#)**
  - Async-await in C# is a language feature that allows asynchronous operations to be written in a sequential style. When a method awaits an I/O operation, the thread is released to do other work and resumes after the operation completes, improving server throughput without manual thread management.
- **Thread Building Block (C++)**
  - Intel Threading Building Blocks (TBB) is a C++ library for task-based parallelism. It provides a work-stealing thread pool, parallel algorithms (parallelfor, parallelreduce), and concurrent containers, enabling game server code to efficiently parallelize computation-heavy workloads across CPU cores.

### 2.11 Reactive Approach
- **OORP**
  - ODRP (One-Data-Renderer-Per-...) or similar reactive decomposition patterns organize server logic into stages where each stage reacts to data from the previous one. This keeps data flow explicit and avoids shared mutable state between components.
- **FRP**
  - FRP (Functional Reactive Programming) combines functional programming with reactive data streams. Game server logic modeled in FRP expresses behavior as transformations of time-varying values and event streams, making temporal logic like cooldowns and interpolation more declarative.

### 2.12 Reactive Model
- **Synchrony**
  - In a synchronous reactive model, event handlers are called and complete before the next event is processed. This simplifies reasoning about order but can bottleneck throughput if any handler is slow.
- **Determinism**
  - Determinism in a reactive game server means the same sequence of inputs always produces the same sequence of outputs. Deterministic server logic enables reliable replay, lockstep multiplayer, and easier debugging of desync issues.

### 2.13 Reactive Approach
- **Reactive Approach**
  - The reactive approach to game server concurrency models the system as a set of components that react to events (network packets, timers, game state changes) rather than blocking on operations. It improves resource efficiency by using non-blocking I/O and event-driven pipelines.

### 2.14 Multithreading
- **Multithreading**
  - Multithreading allows a game server to execute multiple threads concurrently, parallelizing I/O, game logic, and background tasks across CPU cores. The threading model chosen (reactive, task-based, actor) significantly affects throughput, latency, and code complexity.

---

## 3. Advanced

### 3.1 Asynchronous
- **Asynchronous**
  - Asynchronous programming allows a program to initiate an operation and continue executing other work while waiting for the result. In game servers, asynchronous I/O avoids blocking threads on network or disk operations, increasing the number of concurrent connections a single server can handle.

### 3.2 Actor Model
- **Akk.net (C#)**
  - The Actor Model is a concurrency paradigm where actors are independent units of computation that communicate exclusively by passing messages. Each actor processes one message at a time, eliminating shared mutable state and making concurrent game server logic easier to reason about and scale.
- **Akka (Java)**
  - Akka is a Scala/Java toolkit for building concurrent and distributed systems using the Actor Model. Its actor hierarchy enables fault isolation through supervision, and Akka Cluster supports building distributed game server infrastructure that can span multiple machines.

### 3.3 Proactor
- **select**
  - select is a POSIX system call that monitors a set of file descriptors for readiness to read, write, or error. It has a hard limit on the number of file descriptors it can monitor and is generally replaced by poll or epoll in modern high-concurrency game servers.
- **IOCP**
  - IOCP (I/O Completion Ports) is the Windows kernel mechanism for efficient asynchronous I/O. The OS posts completed I/O operations to a completion port queue, and a pool of threads dequeues and handles them.
- **io_uring**
  - iouring is a Linux kernel interface for asynchronous I/O that uses shared ring buffers between kernel and user space to submit and complete I/O operations with minimal system call overhead. It significantly reduces context switch costs for high-throughput game server networking on Linux.

### 3.4 Reactor
- **WSA Poll**
  - WSAPoll is the Windows implementation of the POSIX poll API for socket readiness monitoring. It allows a server to monitor multiple sockets for read/write readiness in a single call, though for high-connection-count servers, IOCP is generally preferred.

### 3.5 Containerization
- **kqueue**
  - kqueue is the BSD (and macOS) equivalent of Linux's epoll. It provides an efficient event notification interface for file descriptors, timers, signals, and other kernel events, used by high-performance game server networking code on BSD and macOS systems.
- **Docker**
  - Docker is the most widely used container runtime and image format. Developers define a game server's environment in a Dockerfile, build it into an image, and run it as a container on any Docker-compatible host, enabling consistent deployments and simple local development environments.

### 3.6 Cloud
- **Azure**
  - Microsoft Azure is a cloud platform offering virtual machines, managed Kubernetes (AKS), game-specific services like Azure PlayFab, and global networking infrastructure. It integrates tightly with C# and .NET tooling, making it a natural choice for game studios using the Microsoft stack.
- **GCP**
  - Google Cloud Platform (GCP) offers compute, storage, networking, and data services for game server hosting. GCP's global network, Agones game server framework on GKE, and BigQuery analytics are widely used by studios hosting multiplayer games at scale.
- **AWS**
  - Amazon Web Services (AWS) is the largest cloud platform, offering services like EC2 (virtual machines), EKS (managed Kubernetes), GameLift (game server hosting), DynamoDB, and CloudFront. Its breadth of services and global regions make it a common foundation for game backend infrastructure.
- **Serverless**
  - Serverless computing runs application code in stateless functions triggered by events, with the cloud provider managing all server infrastructure. It is used for game backend tasks like authentication, leaderboard queries, and webhooks where traffic is bursty and always-on servers would be wasteful.

### 3.7 Data Clustering
- **epoll**
  - epoll is the Linux kernel's scalable I/O event notification mechanism. Unlike select and poll, it uses event-triggered notifications and does not require iterating over all monitored file descriptors on each call, enabling efficient handling of tens of thousands of concurrent connections.
- **Registered IO**
  - Registered I/O (RIO) is a Windows Sockets extension that reduces kernel-to-user transitions by registering fixed memory buffers with the OS. It is designed for ultra-low-latency, high-throughput network applications where minimizing system call overhead matters.
- **Apache Spark**
  - Apache Spark is a distributed data processing framework designed for large-scale analytics and machine learning. Game studios use Spark to process telemetry data, compute player behavior metrics, run A/B test analyses, and build recommendation systems over large datasets.

### 3.8 AI
- **AI**
  - AI in game server development covers machine learning and cloud-based AI services used to enhance gameplay, personalization, matchmaking, anti-cheat, and analytics. Server-side AI processes player data at scale and feeds decisions back into the game experience.

### 3.9 Cloud ML
- **Docker Compose**
  - Docker Compose is a tool for defining and running multi-container applications using a YAML file. Game server developers use it to spin up local environments with the game server, database, cache, and message queue running together with a single command.
- **Kubernetes**
  - Kubernetes is an open-source container orchestration system that automates deployment, scaling, and management of containerized applications. Game studios use Kubernetes to manage fleets of game server pods, scale on demand, perform rolling updates, and recover from failures automatically.
- **Amazon ML**
  - Amazon ML (and its successor Amazon SageMaker) provides managed services for building, training, and deploying machine learning models on AWS. Game studios use it for player behavior prediction, fraud detection, and real-time recommendation systems integrated with other AWS backend services.
- **Azure ML**
  - Azure Machine Learning is Microsoft's managed ML platform for training, deploying, and monitoring models. It integrates with Azure PlayFab and other Azure services, enabling game studios to build ML-powered features like dynamic difficulty and personalized content within the Azure ecosystem.

### 3.10 Deep Learning
- **TensorFlow**
  - TensorFlow is Google's open-source deep learning framework for building and training neural networks. Game backends use TensorFlow to train models offline and serve predictions via TensorFlow Serving, enabling features like matchmaking quality prediction and real-time player analytics.
- **Pytorch**
  - PyTorch is Facebook's open-source deep learning framework known for its dynamic computation graph and Python-first design. It is widely used in game AI research and is increasingly deployed in production game server backends for real-time inference tasks.

---

## 4. Optional / Specialized Topics

- Window Scaling
- Max Segment Size
- Vulnerability
- Denial of Service
- Packet Structure
- Flow Control
- Connection Hijacking
- Veto
- Reliable vs Unreliable
- Ordered vs Unordered
- Heavy vs Lightweight
- Packet vs Datagram
- Streaming vs Broadcast
- DNS
- C#
- Java
- Byte Manipulation
- Winsock
- JSON
- XML
- TOML
- Windows
- pthread
- Redis
- Memcached

---

## 5. References

- [Server Side Game Developer Roadmap](https://roadmap.sh/server-side-game-developer)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Game Developer
- Software Architect

### Related Skills
- Git & GitHub
- System Design
- Docker
- Linux
- Testing