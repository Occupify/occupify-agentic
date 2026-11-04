# Software Architect

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/software-architect
- Related Roles:
  - Backend Developer
  - DevOps Engineer
  - Frontend Developer

---

## 1. Beginner

### 1.1 Understand the Basics
- **What is Software Architecture**
  - Software architecture is the high level structure of a software system: how it is divided into components, how those components interact, and the principles that guide their design. It defines the technical decisions that are hard to change later, such as how data flows between services or which technology stack underpins the system.
- **What is a Software Architect**
  - A software architect is the person responsible for making high level technical decisions on a project, including choosing technologies, defining system structure, and setting coding standards. They act as a bridge between business requirements and the engineering team, translating goals into a technical roadmap.
- **Levels of Architecture**
  - Architecture can be described at different levels of scope, ranging from a single application to an entire organization. Application architecture deals with the internals of one system, solution architecture connects several systems to solve a business problem, and enterprise architecture aligns technology strategy across a whole company.

### 1.2 Responsibilities
- **Application Architecture**
  - Application architecture focuses on the internal structure of a single software application: its modules, layers, and the patterns used to organize code. It determines how the application handles concerns like data access, business logic, and user interface separation.
- **Solution Architecture**
  - Solution architecture designs how multiple applications and systems work together to satisfy a specific business need. It sits between application architecture and enterprise architecture, dealing with integration points, data flow, and technology choices across several components.
- **Enterprise Architecture**
  - The highest level of architecture. Focus on multiple solutions.

### 1.3 Important Skills to Learn
- **Design & Architecture**
  - This skill covers applying design principles and architectural patterns to real systems, not just knowing them in theory. It means knowing when to use a microservices approach versus a monolith, or when a simple layered design is enough.
- **Decision Making**
  - Decision making covers evaluating trade offs and choosing a direction when there is no single obviously correct answer. Architects constantly weigh factors like cost, performance, team skill, and time to market when picking a technology or pattern.
- **Simplifying Things**
  - Simplifying things means reducing complex problems and systems into clear, manageable parts that others can understand and act on. Architects often deal with many moving pieces, and the ability to cut through unnecessary complexity leads to designs that are easier to build, test, and maintain.
- **How to Code**
  - An architect needs strong coding skills to design realistic solutions and earn credibility with the development team. Writing code themselves helps them understand the practical constraints of the technologies they choose and spot problems before they become costly.
- **Documentation**
  - Architectural documentation is sometimes more and sometimes less important. Important documents are for example architectural decisions or code guidelines.
- **Communication**
  - Communication is central to the architect role, since decisions need to be explained to developers, managers, and other stakeholders with different levels of technical understanding. An architect translates business goals into technical direction and also feeds technical constraints back into business conversations.
- **Estimate and Evaluate**
  - Estimating and evaluating involves judging the time, cost, and effort a technical solution will require, as well as assessing whether an existing system meets its goals. Architects use this skill when planning new projects and when reviewing whether current systems are still fit for purpose.
- **Balance**
  - Balance refers to weighing competing priorities such as speed versus quality, or innovation versus stability. An architect regularly makes trade offs between what is technically ideal and what is practical given time and budget constraints.

### 1.4 Technical Skills
- **GitHub**
  - GitHub has become a central hub for open-source projects and is widely used by developers, companies, and organizations for both private and public repositories. It was acquired by Microsoft in 2018 but continues to operate as a relatively independent entity.

### 1.5 Programming Languages
- **Java / Kotlin / Scala / Swift**
  - Java: Java is a widely-used, object-oriented programming language known for its platform independence, reliability, and scalability. It’s commonly used for building large-scale enterprise applications, Android development, and web services.
- **Python**
  - Python is a multi-paradigm language. Being an interpreted language, code is executed as soon as it is written and the Python syntax allows for writing code in functional, procedural or object-oriented programmatic ways.
- **Ruby**
  - Ruby is a high-level, interpreted programming language that blends Perl, Smalltalk, Eiffel, Ada, and Lisp. Ruby focuses on simplicity and productivity along with a syntax that reads and writes naturally.
- **Go**
  - Go is an open source programming language supported by Google. Go can be used to write cloud services, CLI tools, used for API development, and much more.
- **JavaScript / TypeScript**
  - JavaScript is the primary language of the web, running in browsers and, through Node.js, on servers as well. TypeScript adds static typing on top of JavaScript, catching errors earlier and making large codebases easier to maintain.
- **.NET Framework Based**
  - The .NET ecosystem, built around languages like C#, is widely used for enterprise applications, especially in Windows centric environments. It provides a large set of libraries and tools for building web, desktop, and cloud applications.

---

## 2. Intermediate

### 2.1 Patterns & Design Principles
- **OOP**
  - Object oriented programming organizes code around objects that combine data and behavior, using concepts like encapsulation, inheritance, and polymorphism. It helps model real world entities and relationships in a way that keeps related code together and reusable.
- **MVC, MVP, MVVM**
  - MVC, MVP, and MVVM are patterns for separating an application's data, logic, and user interface into distinct layers. MVC splits responsibilities between model, view, and controller, MVP replaces the controller with a presenter that handles view logic, and MVVM introduces a view model that binds data to the view automatically.
- **CQRS, Eventual Consistency**
  - CQRS, or Command Query Responsibility Segregation, separates the operations that change data from the operations that read data, often using different models for each. This separation pairs naturally with eventual consistency, where updates propagate across a system over time instead of instantly.
- **ACID, CAP Theorem**
  - ACID describes the guarantees a database transaction provides: atomicity, consistency, isolation, and durability, ensuring reliable operations even under failure. The CAP theorem states that a distributed system can only guarantee two of three properties at once: consistency, availability, and partition tolerance.

### 2.2 Tools
- **Git**
  - Git is a distributed version control system that tracks changes to code over time and allows multiple developers to work on the same project without overwriting each other's work. It supports branching and merging workflows that let teams develop features in isolation before combining them.
- **Slack**
  - Slack is a messaging app for business that connects people to the information that they need. By bringing people together to work as one unified team, Slack transforms the way that organisations communicate.
- **Trello**
  - Trello is a visual project management tool based on boards, lists, and cards that represent tasks moving through stages of work. Its simplicity makes it popular for smaller teams or lightweight project tracking compared to more complex tools.
- **Atlassian Tools**
  - Atlassian tools, including Jira and Confluence, support project tracking and documentation for software teams at scale. Jira manages tasks, sprints, and issues in agile workflows, while Confluence stores documentation and design discussions.

### 2.3 Tools
- **Tools**
  - Architect tools are software tools that help architects to design, document, and manage software architectures. These tools can be used to create architecture diagrams, generate code, and automate the software development process.

### 2.4 Architecture
- **Actors**
  - Actor Model is a model that represents actors as the basic unit of a system, they can only communicate through messages and have their own private state, and they can also manage other actors, resulting in an encapsulated and fault-tolerant system.
- **SOLID**
  - SOLID is a set of five object oriented design principles: single responsibility, open closed, Liskov substitution, interface segregation, and dependency inversion. Following these principles leads to code that is easier to extend, test, and maintain as a system grows.
- **TDD**
  - Test driven development (TDD) is the process of writing tests for software's requirements which will fail until the software is developed to meet those requirements. Once those tests pass, then the cycle repeats to refactor code or develop another feature/requirement.
- **DDD**
  - Domain driven design structures software around the business domain it serves, using a shared language between developers and domain experts called the ubiquitous language. It introduces concepts like bounded contexts and aggregates to manage complexity in large systems.
- **Serverless**
  - Serverless architecture (also known as serverless computing or function as a service, FaaS) is a software design pattern where applications are hosted by a third-party service, eliminating the need for server software and hardware management by the developer. Applications are broken up into individual functions that can be invoked and scaled individually.
- **Microservices**
  - Microservice architecture is a pattern in which highly cohesive, loosely coupled services are separately developed, maintained, and deployed. Each component handles an individual function, and when combined, the application handles an overall business function.

### 2.5 Security
- **Consult & Coach**
  - Consulting and coaching means guiding developers and teams toward better technical practices without necessarily writing the code themselves. Architects often review designs, answer technical questions, and mentor less experienced engineers on patterns and standards.
- **Marketing Skills**
  - Marketing skills help an architect present and sell technical ideas internally, convincing stakeholders and teams to adopt a proposed direction. This includes framing technical benefits in terms that matter to business decision makers, such as cost savings or reduced risk.
- **Client / Server**
  - Client-server architecture is a computing model that separates tasks or workloads between service providers (servers) and service requesters (clients). This architecture is widely used in networked applications, including web applications, where clients interact with servers to access resources, services, and data.
- **Hashing Algorithms**
  - Hashing algorithms are used to generate a unique value for a given input. This value is called a hash.
- **PKI**
  - A public key infrastructure (PKI) is a set of roles, policies, hardware, software, and procedures to create, manage, distribute, use, store and revoke digital certificates and public-key encryption. The purpose of a PKI is to facilitate the secure electronic transfer of information for a range of network activities such as e-commerce, internet banking, and confidential email.
- **OWASP**
  - OWASP or Open Web Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.
- **Auth Strategies**
  - Authentication and authorization strategies determine how a system verifies who a user is and what they are allowed to do. Common approaches include session based authentication, token based methods like JWT, and protocols like OAuth for delegated access.

### 2.6 Working with Data
- **Layered**
  - Layered architecture organizes a system into horizontal layers, such as presentation, business logic, and data access, where each layer only communicates with the ones directly above or below it. This separation makes it easier to change one layer without affecting the others, such as swapping a database without touching business rules.
- **Hadoop, Spark, MapReduce**
  - Hadoop, Spark, and MapReduce are frameworks for processing large datasets across clusters of machines. MapReduce, the original model, splits processing into map and reduce steps distributed across nodes, while Spark improves on this with in memory processing for much faster performance.
- **ETL, Datawarehouses**
  - ETL (Extract, Transform, Load) is a key process in data warehousing, enabling the integration of data from multiple sources into a centralized database. The process begins by extracting data from original sources, followed by transforming it to ensure quality, deduplication, and combination, and finally loading it into the target database.
- **SQL Databases**
  - SQL stands for Structured Query Language. It's used for relational databases.
- **NoSQL Databases**
  - NoSQL databases store data in flexible formats like documents, key value pairs, or graphs, without requiring a fixed schema. They often trade strict consistency for better scalability and performance, making them suitable for large scale or rapidly changing data.

### 2.7 APIs & Integrations
- **Apache Spark**
  - Apache Spark is a distributed data processing engine that performs computations in memory, making it significantly faster than earlier tools like MapReduce for many workloads. It supports batch processing, streaming, machine learning, and graph processing through a single unified framework.
- **Hadoop**
  - Hadoop is an open source framework for distributed storage and processing of large datasets across clusters of commodity hardware. Its core components include HDFS for storage and MapReduce for processing, though many projects now pair Hadoop's storage with faster engines like Spark.
- **Datawarehouse Principles**
  - Data warehouse principles cover how to design storage systems optimized for analytical queries rather than transactional workloads. This includes concepts like star and snowflake schemas, fact and dimension tables, and strategies for handling historical data changes.
- **gRPC**
  - gRPC is a high performance remote procedure call framework that uses HTTP/2 and Protocol Buffers to enable fast, efficient communication between services. It supports streaming and strongly typed contracts, making it a common choice for internal service to service communication in microservices architectures.

---

## 3. Advanced

### 3.1 Web, Mobile
- **Distributed Systems**
  - Distributed systems consist of multiple independent components running on different machines that communicate over a network to work as a single system. They introduce challenges like network latency, partial failures, and data consistency that do not exist in single machine applications.
- **Service Oriented**
  - Service oriented architecture structures a system as a set of loosely coupled services that communicate through well defined interfaces, often using standards like SOAP. It predates microservices and shares similar goals of modularity and reuse, but typically involves heavier middleware like an enterprise service bus.
- **Functional Programming**
  - Functional programming treats computation as the evaluation of pure functions, avoiding shared state and mutable data where possible. This style makes code easier to test and reason about, since functions with no side effects behave predictably given the same input.
- **React, Vue, Angular**
  - React, Vue, and Angular are popular JavaScript frameworks and libraries for building interactive web user interfaces through reusable components. React focuses on a flexible component model with a large ecosystem, Vue emphasizes simplicity and gradual adoption, and Angular provides a more complete, opinionated framework out of the box.
- **SPA, SSR, SSG**
  - Single page applications load once and update content dynamically without full page reloads, giving a smooth user experience but sometimes at the cost of slower initial load and weaker search engine visibility. Server side rendering generates HTML on the server for each request, improving initial load time and SEO.
- **Microfrontends**
  - Microfrontends is an architectural style where independently deliverable frontend applications built by different teams using different technologies are composed into a greater whole. Simply, a Micro-Frontend is a portion of a webpage (not the entire page).
- **W3C and WHATWG**
  - The W3C and WHATWG are the organizations responsible for defining and maintaining web standards like HTML, CSS, and related specifications. The W3C historically focused on formal standardization, while WHATWG, formed by browser vendors, drives the living standard for HTML used by modern browsers today.
- **Reactive Programming**
  - Reactive programming describes a design paradigm that relies on asynchronous programming logic to handle real-time updates to otherwise static content. It provides an efficient means -- the use of automated data streams -- to handle data updates to content whenever a user makes an inquiry.

### 3.2 Frameworks
- **ESB, SOAP**
  - ESB (Enterprise Service Bus) and SOAP (Simple Object Access Protocol) are two technologies that enable communication between different systems. ESB is a software architecture that allows for the integration of various systems, such as databases, web services, and mobile applications.
- **GraphQL**
  - GraphQL is a query language and runtime for APIs, developed by Facebook. GraphQL's flexibility and efficiency make it popular for building complex applications, especially those with diverse client requirements.
- **REST**
  - REST is an architectural style for designing APIs around resources, identified by URLs and manipulated through standard HTTP methods like GET, POST, and DELETE. Its simplicity and reliance on existing web standards have made it the most common approach for building public and internal APIs.
- **BPM, BPEL**
  - Business process management describes methodologies and tools for modeling, automating, and optimizing business processes across an organization. BPEL, the Business Process Execution Language, is an XML based language used to define and orchestrate these processes, often within service oriented architectures.
- **BABOK**
  - The guide to the Business Analysis Body of Knowledge (BABOK Guide) is a book from the International Institute of Business Analysis (IIBA) that provides business analysts (BAs) with strategies for using data to improve an organization's workflow processes, technology, products and services.
- **IAF**
  - The Integrated Architecture Framework is a methodology for enterprise architecture that structures architecture work across business, information, and technology domains. It provides a consistent way to model how different aspects of an organization's architecture relate to each other.
- **RUP**
  - The RUP (Rational Unified Process) is not a widely recognized certification like PMP or Scrum, but rather a software development framework created by Rational Software (now IBM). It follows an iterative and incremental approach to project development, based on best practices for delivering high-quality software on time and within budget.

### 3.3 Management
- **PMI**
  - The PMI certification (Project Management Institute) is an internationally recognized credential in project management. The most well-known is the PMP® (Project Management Professional), which validates the skills and knowledge of professionals to manage projects effectively by applying best practices and standards defined in the PMBOK® (Project Management Body of Knowledge) guide.
- **ITIL**
  - ITIL is a framework for IT service management, focused on aligning IT services with the needs of the business through defined processes like incident, change, and problem management. It is commonly adopted in enterprises that need consistent, auditable processes for running IT operations.
- **Prince2**
  - Prince2 is a structured project management method and practitioner certification programme. Prince2 emphasizes dividing projects into manageable and controllable stages.
- **LeSS**
  - LeSS (Large-Scale-Scrum) is an agile framework designed to scale Scrum across multiple teams working on a single product. It adheres to Scrum's principles, emphasizing simplicity and continuous improvement.
- **SaFE**
  - SAFe is an agile framework designed to scale agile practices in large and complex organizations. Unlike LeSS, SAFe is more structured and provides a formal approach to coordinating multiple teams, programs, and portfolios.
- **Kanban**
  - Kanban is an agile method that visualizes work on a board with columns representing stages, helping teams manage flow and limit work in progress. It focuses on continuous delivery rather than fixed length iterations, making it flexible for teams with varying or unpredictable workloads.
- **Scrum**
  - Scrum is an agile framework that organizes work into fixed length iterations called sprints, with defined roles like product owner and scrum master guiding the process. It includes regular ceremonies such as sprint planning, daily standups, and retrospectives to keep the team aligned and improve over time.
- **XP**
  - Extreme Programming is an agile methodology that emphasizes technical practices like pair programming, test driven development, and continuous integration to improve software quality. It focuses heavily on engineering discipline alongside the process and collaboration elements found in other agile frameworks.

### 3.4 Networks
- **UML**
  - The Unified Modeling Language is a standardized set of diagram types used to visualize the design of a system, including class diagrams, sequence diagrams, and use case diagrams. It gives architects and developers a common visual language for describing structure and behavior before or during implementation.
- **TOGAF**
  - TOGAF, The Open Group Architecture Framework, is one of the most widely used frameworks for developing and managing enterprise architecture. It defines a structured process, called the Architecture Development Method, for creating and maintaining architecture that aligns with business goals.
- **OSI**
  - The OSI and TCP/IP model is used to help the developer to design their system for interoperability. The OSI model has 7 layers while the TCP/IP model has a more summarized form of the OSI model only consisting 4 layers.
- **TCP/IP Model**
  - The TCP/IP model is the practical, four layer framework that actually underlies how the internet works, covering link, internet, transport, and application layers. It is simpler than the OSI model and maps more directly to real protocols like IP, TCP, and HTTP.
- **HTTP, HTTPS**
  - HTTP is the protocol that underlies most communication on the web, defining how clients and servers exchange requests and responses. HTTPS adds encryption on top of HTTP using TLS, protecting data in transit from being read or altered by third parties.
- **Proxies**
  - A proxy is an intermediary server that sits between a client and a destination server, forwarding requests and often adding functionality like caching, load balancing, or filtering. Reverse proxies sit in front of backend servers to distribute traffic and hide internal infrastructure, while forward proxies sit in front of clients.

### 3.5 Operations Knowledge
- **Messaging Queues**
  - Message queuing makes it possible for applications to communicate asynchronously, by sending messages to each other via a queue. A message queue provides temporary storage between the sender and the receiver so that the sender can keep operating without interruption when the destination program is busy or not connected.
- **Infrastructure as Code**
  - Infrastructure as code manages servers, networks, and other infrastructure through machine readable configuration files instead of manual setup. Tools like Terraform or CloudFormation let teams version, review, and repeat infrastructure changes just like application code.
- **Cloud Providers**
  - Cloud providers provide a layer of APIs to abstract infrastructure and provision it based on security and billing boundaries. The cloud runs on servers in data centers, but the abstractions cleverly give the appearance of interacting with a single “platform” or large application.
- **Serverless Concepts**
  - Serverless is a cloud-native development model that allows developers to build and run applications without having to manage servers. There are still servers in serverless, but they are abstracted away from app development.
- **Linux / Unix**
  - Knowledge of UNIX is a must for almost all kind of development as most of the codes that you write is most likely going to be finally deployed on a UNIX/Linux machine. Linux has been the backbone of the free and open source software movement, providing a simple and elegant operating system for almost all your needs.
- **Service Mesh**
  - A Service Mesh is a dedicated infrastructure layer for handling service-to-service communication. It’s responsible for the reliable delivery of requests through the complex topology of services that comprise a modern, cloud native application.
- **CI / CD**
  - CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment.
- **Containers**
  - Containers are a construct in which cgroups, namespaces, and chroot are used to fully encapsulate and isolate a process. This encapsulated process, called a container image, shares the kernel of the host with other containers, allowing containers to be significantly smaller and faster than virtual machines.
- **Cloud Design Patterns**
  - These design patterns are useful for building reliable, scalable, secure applications in the cloud. The cloud design patterns where each pattern describes the problem that the pattern addresses, considerations for applying the pattern, and an example based on Microsoft Azure.

### 3.6 Enterprise Software
- **Firewalls**
  - A Firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies. Firewalls usually sit between a trusted network and an untrusted network; oftentimes the untrusted network is the Internet.
- **MS Dynamics**
  - Microsoft Dynamics is a suite of enterprise resource planning and customer relationship management applications used to manage business processes like sales, finance, and operations. It integrates closely with other Microsoft products, making it a common choice for organizations already invested in the Microsoft ecosystem.
- **SAP ERP, HANA, Business Objects**
  - SAP ERP is a widely used enterprise resource planning system that manages core business processes across large organizations, from finance to supply chain. SAP HANA is an in memory database platform that powers faster processing for SAP applications, and SAP Business Objects provides business intelligence and reporting on top of that data.
- **EMC DMS**
  - EMC's document management systems provide enterprise level tools for storing, organizing, and controlling access to documents and records at scale. These systems focus on compliance, versioning, and retention policies important for regulated industries.
- **IBM BPM**
  - IBM Business Process Manager is a platform for modeling, automating, and monitoring business processes within an organization. It provides tools for both business analysts and developers to design workflows and integrate them with existing enterprise systems.
- **Salesforce**
  - Salesforce is a widely used cloud based customer relationship management platform that also supports custom application development through its Apex language and Lightning platform. Many organizations extend Salesforce beyond CRM into custom business applications built on top of its platform.

---

## 4. Optional / Specialized Topics

- Documentation
- Communication
- Estimate and Evaluate
- Balance
- JavaScript / TypeScript
- .NET Framework Based
- Serverless
- Microservices
- PKI
- OWASP
- Auth Strategies
- NoSQL Databases
- SPA, SSR, SSG
- Microfrontends
- W3C and WHATWG
- Reactive Programming
- BABOK
- IAF
- RUP
- SaFE
- Kanban
- Scrum
- XP
- HTTP, HTTPS
- Proxies

---

## 5. References

- [Software Architect Roadmap](https://roadmap.sh/software-architect)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer
- Frontend Developer

### Related Skills
- Software Design & Architecture
- Python
- Go
- Java