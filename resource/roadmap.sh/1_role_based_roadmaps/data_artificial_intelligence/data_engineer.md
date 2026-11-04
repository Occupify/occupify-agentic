# Data Engineer

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/data-engineer
- Related Roles:
  - AI and Data Scientist
  - PostgreSQL DBA
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is Data Engineering?**
  - Data engineering is the practice of designing and building systems for the aggregation, storage and analysis of data at scale. Data engineers excel at creating and deploying algorithms, data pipelines and workflows that sort raw data into ready-to-use datasets.
- **Data Eng. vs Data Science**
  - Data engineering and data science are distinct but complementary roles within the field of data. Data engineering focuses on building and maintaining the infrastructure for data collection, storage, and processing, essentially creating the systems that make data available for downstream users.
- **Skills & Responsibilities**
  - A data engineer works across a broad set of tools and systems: programming languages, databases, cloud platforms, pipeline orchestration, and distributed computing. Core responsibilities include building and maintaining data pipelines, managing database schemas, optimizing query performance, and ensuring data quality.
- **Data Engineering Lifecycle**
  - The data engineering lifecycle describes the stages data moves through from creation to consumption. These stages typically include generation, ingestion, storage, transformation, and serving.
- **Choosing the Right Technologies**
  - Selecting the right technology stack depends on data volume, team size, latency requirements, and budget. There is no universal best choice; a small startup may do well with a simple Postgres setup, while a large enterprise may need distributed processing and a cloud data warehouse.

### 1.2 Data Engineering Lifecycle
- **Data Generation**
  - Data generation refers to how raw data is produced and originates in a system. Data can come from user interactions, application logs, IoT sensors, databases, APIs, and many other sources.
- **Data Storage**
  - Data storage in the engineering lifecycle refers to where and how data is persisted after it is generated or ingested. The choice of storage system depends on access patterns, data volume, latency requirements, and cost.
- **Data Ingestion**
  - Data ingestion is the third step in the data engineering lifecycle. It entails the process of collecting and importing data files from various sources into a database for storage, processing and analysis.
- **Data Serving**
  - Data serving is the last step in the data engineering process. Once the data is stored in your data architectures and transformed into coherent and useful format, it's time for get value from it.

### 1.3 Programming Skills
- **Python**
  - Python’s inherent characteristics and the wealth of resources that have grown around it have made it the data engineer’s language of choice. Python is a high-level, interpreted, general-purpose programming language.
- **Java**
  - Java has had a big influence on data engineering because many core big data tools and frameworks, like Hadoop, Spark (originally in Scala, which runs on the JVM), and Kafka, are built using Java or run on the Java Virtual Machine (JVM). This means Java’s performance, scalability, and cross-platform capabilities have shaped how large-scale data processing systems are designed.
- **Scala**
  - Scala is a programming language that combines the strengths of object-oriented and functional programming, and it runs on the Java Virtual Machine (JVM). In data engineering, Scala is especially important because Apache Spark, one of the most popular big data processing frameworks, was written in Scala.

### 1.4 Data Structures & Algorithms
- **Go**
  - Go is a compiled language developed by Google, known for its simplicity, fast execution, and strong concurrency model. In data engineering, it is used to build lightweight, high-throughput services and tools.

### 1.5 Git and GitHub
- **Git and GitHub**
  - Git is a distributed version control system that tracks changes to code over time. GitHub is a platform built on top of Git that adds collaboration features like pull requests, code review, and CI/CD integrations.

### 1.6 Linux Basics
- **Linux Basics**
  - Knowledge of UNIX is a must for almost all kind of development as most of the code that you write is most likely going to be finally deployed on a UNIX/Linux machine. Linux has been the backbone of the free and open source software movement, providing a simple and elegant operating system for almost all your needs.

### 1.7 Networking Fundamentals
- **Networking Fundamentals**
  - Networking Fundamentals

### 1.8 Distributed Systems Basics
- **Distributed Systems Basics**
  - A distributed system is a collection of independent computers that communicate and coordinate to appear as a single unified system. They are widely used for scalability, fault tolerance, and high availability in modern applications.

### 1.9 Sources of Data
- **Database**
  - A database is an organized, structured collection of electronic data that is stored, managed, and accessed via a computer system, usually controlled by a Database Management System (DBMS). Databases organize various types of data, such as words, numbers, images, and videos, allowing users to easily retrieve, update, and modify it for various purposes, from managing customer information to analyzing business processes.
- **APIs**
  - APIs (Application Programming Interfaces) expose data from external services in a structured format, typically JSON or XML over HTTP. Many data pipelines pull data from third-party APIs such as payment processors, marketing platforms, or social networks.
- **Logs**
  - Logs are files that record events, activities, and system operations over time. They provide a detailed historical record of what has happened within a system, including timestamps, event details, performance data, errors, and user actions.
- **IoT**
  - IoT, or Internet of Things, refers to a network of connected devices that interact with their environment. IoT devices extend beyond standard devices such as PCs, laptops, and smartphones, including smart locks, connected thermostats, and temperature sensors.

### 1.10 Data Collection Ideas
- **Mobile Apps**
  - Mobile apps are programs for phones and tablets, usually from app stores. They can be native (for one OS like iOS or Android), hybrid (web tech in a native shell), or cross-platform (like React Native).
- **Data Normalization**
  - Data normalization is the process of organizing a relational database to reduce redundancy and improve data integrity. It involves decomposing tables into smaller, related ones according to normal forms (1NF, 2NF, 3NF, etc.).
- **Learn SQL**
  - SQL stands for Structured Query Language. It is a standardized programming language designed to manage and interact with relational database management systems (RDBMS).
- **Indexing**
  - Indexes are data structures that speed up query performance by allowing the database to find rows without scanning the entire table. They are created on one or more columns and come in various types, including B-tree, hash, and full-text indexes.
- **Transactions**
  - Transactions in SQL are units of work that group one or more database operations into a single, atomic unit. They ensure data integrity by following the ACID properties: Atomicity (all or nothing), Consistency (database remains in a valid state), Isolation (transactions don't interfere with each other), and Durability (committed changes are permanent).

### 1.11 Database Fundamentals
- **Data Modelling Techniques**
  - Data modelling is the process of defining how data is structured and related within a storage system. Common techniques include entity-relationship (ER) modelling for transactional databases and dimensional modelling (star and snowflake schemas) for analytics.
- **CAP Theorem**
  - The CAP theorem states that a distributed system can provide at most two of three guarantees: Consistency, Availability, and Partition Tolerance. In practice, network partitions are unavoidable, so systems must choose between consistency and availability when a partition occurs.
- **MySQL**
  - MySQL is an open-source relational database management system (RDBMS) known for its speed, reliability, and ease of use. It uses SQL (Structured Query Language) for database interactions and supports a range of features for data management, including transactions, indexing, and stored procedures.

### 1.12 Relational Databases
- **OLTP vs OLAP**
  - OLTP (Online Transaction Processing) systems are optimized for fast, frequent read and write operations, typically backing operational applications. OLAP (Online Analytical Processing) systems are designed for complex queries over large datasets, used in reporting and analytics.

---

## 2. Intermediate

### 2.1 NoSQL Databases
- **NoSQL Databases**
  - NoSQL databases are a category of database management systems designed for handling unstructured, semi-structured, or rapidly changing data. Unlike traditional relational databases, which use fixed schemas and SQL for querying, NoSQL databases offer flexible data models and can be classified into several types:

### 2.2 Document
- **Slowly Changing Dimension**
  - Slowly Changing Dimensions (SCDs) are a data warehousing technique used to track changes in dimension data over time. Instead of simply overwriting old data with new data, SCDs allow you to maintain historical records of how dimension attributes have changed.
- **Horizontal vs Vertical Scaling**
  - Horizontal scaling is the process of adding more machines or nodes to an existing pool in a system to distribute the workload and address increased load. By contrast, vertical scaling involves increasing the computing power of individual machines in a system.
- **Star vs Snowflake Schema**
  - Star and snowflake schemas are two approaches to organizing data in a data warehouse. A star schema has a central fact table connected directly to dimension tables, making queries simple and fast.
- **MongoDB**
  - MongoDB is a NoSQL, open-source database designed for storing and managing large volumes of unstructured or semi-structured data. It uses a document-oriented data model where data is stored in BSON (Binary JSON) format, which allows for flexible and hierarchical data representation.
- **ElasticSearch**
  - Elasticsearch is a distributed search and analytics engine built on Apache Lucene. It is designed for full-text search, log analysis, and real-time data exploration.

### 2.3 Column
- **Cassandra**
  - Apache Cassandra is an open-source distributed wide-column database designed for high availability and linear scalability. It has no single point of failure and is optimized for fast writes across multiple data centers.
- **BigTable**
  - Bigtable is a high-performance, scalable database that excels at capturing, processing, and analyzing data in real-time. It aggregates data as it's written, providing immediate insights into user behavior, A/B testing results, and engagement metrics.
- **HBase**
  - HBase is a column-oriented No-SQL database management system that runs on top of Hadoop Distributed File System (HDFS), a main component of Apache Hadoop. HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases.

### 2.4 Graph
- **MariaDB**
  - MariaDB server is a community developed fork of MySQL server. Started by core members of the original MySQL team, MariaDB actively works with outside developers to deliver the most feature rich, stable, and sanely licensed open SQL server in the industry.
- **Oracle**
  - Oracle Database is a commercial relational database system widely used in enterprise environments. It is known for its robustness, advanced features, and support for very large-scale deployments.
- **Neo4j**
  - Neo4j is the most widely used graph database. It stores data natively as nodes and relationships and uses Cypher, a declarative query language designed for graph traversal.
- **Neptune**
  - Amazon Neptune is a managed graph database service on AWS that supports both the Property Graph model (with Gremlin) and RDF (with SPARQL). It is designed for highly connected datasets and scales to billions of relationships.

### 2.5 Key-Value
- **PostgreSQL**
  - PostgreSQL is an open-source relational database known for its standards compliance, extensibility, and advanced feature set. It supports complex queries, JSON storage, full-text search, and custom data types.
- **Aurora DB**
  - Amazon Aurora (Aurora) is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. Aurora includes a high-performance storage subsystem.
- **MS SQL**
  - Microsoft SQL Server (MS SQL) is a relational database developed by Microsoft, commonly used in enterprise and Windows-based environments. It integrates tightly with the Microsoft ecosystem, including Azure, Power BI, and .NET.
- **Redis**
  - Redis is an in-memory key-value store known for its extremely low latency. It supports a variety of data structures including strings, lists, sets, sorted sets, and hashes.
- **Memcached**
  - Memcached is a high-performance, distributed in-memory caching system. It is simpler than Redis, supporting only key-value string storage, but is very fast and horizontally scalable.

### 2.6 Data Mesh
- **DynamoDB**
  - Amazon DynamoDB is a fully managed key-value and document database service on AWS. It provides single-digit millisecond performance at any scale and handles replication and scaling automatically.
- **Data Mart**
  - A data mart is a subset of a data warehouse, focused on a specific business function or department. A data mart is streamlined for quicker querying and a more straightforward setup, catering to the specialized needs of a particular team, or function.
- **Data Fabric**
  - Data fabric is an architectural concept that aims to provide a unified layer for accessing and managing data across heterogeneous environments, including on-premises and multiple clouds. It uses metadata, automation, and integration patterns to connect disparate data sources.
- **Data Hub**
  - A data hub is a centralized platform that acts as an integration point for data flowing between multiple systems. Unlike a data warehouse, a data hub focuses on data movement and integration rather than storage for analytics.
- **Metadata-first Architecture**
  - A metadata-first architecture treats metadata as a first-class citizen in data system design. Rather than just documenting data after the fact, metadata is captured and used actively to govern, discover, and lineage-track data across the organization.
- **Serverless Options**
  - Serverless data storage involves using cloud provider services for databases and object storage that automatically scale infrastructure and implement a consumption-based, pay-as-you-go model, eliminating the need for developers to manage, provision, or maintain any physical or virtual servers. This approach simplifies development, reduces operational overhead, and offers cost-effectiveness by charging only for the resources used, allowing teams to focus on applications rather than infrastructure management.

### 2.7 Data Warehouse
- **CosmosDB**
  - Azure Cosmos DB is a native No-SQL database service and vector database for working with the document data model. It can arbitrarily store native JSON documents with flexible schema.
- **CouchDB**
  - Apache CouchDB is an open-source document database that uses JSON for documents and HTTP as its API. It is designed for reliability and offline-first use cases, with a built-in replication protocol that syncs data between devices and servers.
- **Google BigQuery**
  - BigQuery is a managed, serverless data warehouse product by Google, offering scalable analysis over large quantities of data. It is a Platform as a Service (PaaS) that supports querying using a dialect of SQL.
- **Snowflake**
  - Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities.

### 2.8 What is Data Warehouse?
- **What is Data Warehouse?**
  - A data warehouse is a centralized repository for storing large volumes of structured, historical data from multiple sources. It is optimized for analytical queries rather than transactional operations.

### 2.9 Data Warehouse Architectures
- **Data Warehouse Architectures**
  - Data warehousing architectures describe how data is organized, stored, and accessed across a warehouse system. Common patterns include traditional ETL-based warehouses, cloud-native warehouses, data lakehouse architectures, and federated query systems.

### 2.10 Data Lake
- **Amazon Redshift**
  - Amazon Redshift is a cloud-based data warehouse service from Amazon that lets you store and analyze large amounts of data quickly. It’s designed for running complex queries on huge datasets, so businesses can use it to turn raw data into useful reports and insights.
- **Databricks Delta Lake**
  - Delta Lake is the optimized storage layer that provides the foundation for tables in a lakehouse on Databricks. Delta Lake is open source software that extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling.
- **Snowflake**
  - Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities.
- **Onehouse**
  - Onehouse Managed Lakehouse is a cloud-native SaaS product built on top of Apache Hudi. It replaces painful, inefficient do-iy-yourseld data lake management around file sizing, masking, deletion, clustering, access control, caching, etc.

### 2.11 Cloud Computing
- **Cloud Architectures**
  - Cloud architectures describe how systems are designed to run on cloud infrastructure. Common patterns include multi-tier architectures, microservices, event-driven designs, and serverless functions.
- **Amazon EC2 ( Compute)**
  - Amazon EC2 (Elastic Compute Cloud) provides virtual servers in the AWS cloud. Users can choose instance types optimized for compute, memory, or storage, and pay only for what they run.

### 2.12 Types of Data Ingestion
- **S3 (Storage)**
  - Amazon S3 (Simple Storage Service) is an object storage service offered by Amazon Web Services (AWS). It provides scalable, secure and durable storage on the internet.
- **Amazon RDS (Database)**
  - Amazon RDS (Relational Database Service) is a managed relational database service from AWS that supports MySQL, PostgreSQL, MariaDB, Oracle, and MS SQL Server. It handles provisioning, backups, patching, and replication automatically.
- **Glue (ETL)**
  - AWS Glue is a fully managed ETL service that automates the discovery, cataloging, and transformation of data. It includes a data catalog for storing metadata, a job scheduler, and a serverless Spark environment for running transformations.
- **Azure Virtual Machines**
  - Azure Virtual Machines (VMs) enable virtualization without requiring hardware investments. They provide customizable environments for development, testing, and cloud applications so you can run different operating systems like Ubuntu on a Windows host based on your needs.
- **Batch**
  - Batch processing is a method in which large volumes of collected data are processed in chunks or batches. This approach is especially effective for resource-intensive jobs, repetitive tasks, and managing extensive datasets where real-time processing isn’t required.
- **Hybrid**
  - Hybrid data ingestion combines aspects of both real-time and batch ingestion. This approach gives you the flexibility to adapt your data ingestion strategy as your needs evolve.
- **Realtime**
  - Real-time processing, also known as streaming processing, involves the immediate ingestion, as well as analysis, of data as it is generated, providing instantaneous insights and enabling timely decisions in time-sensitive applications like financial trading, medical monitoring, and autonomous vehicles. This differs from batch processing, which handles data in later batches, and typically involves continuous data streaming, low latency, and high availability to deliver immediate outcomes for critical tasks.

### 2.13 Data Pipelines
- **Azure Blob Storage**
  - Azure Blob Storage is Microsoft's object storage solution for the cloud. “Blob” stands for Binary Large Object, a term used to describe storage for unstructured data like text, images, and video.
- **Azure SQL Database**
  - Azure SQL Database is a fully managed Platform as a Service (PaaS) offering. It abstracts the underlying infrastructure, enabling developers to focus on building and deploying applications without worrying about database maintenance tasks.
- **Data Factory (ETL)**
  - Data Factory, most commonly referring to Microsoft's Azure Data Factory, is a cloud-based data integration service that allows you to create, schedule, and orchestrate workflows to move and transform data from various sources into a centralized location for analysis. It provides tools for building Extract, Transform, and Load (ETL) pipelines, enabling businesses to prepare data for analytics, business intelligence, and other data-driven initiatives without extensive coding, thanks to its visual, code-free interface and native connectors.
- **Compute Engine (Compute)**
  - Google Cloud Compute Engine provides virtual machine instances on Google's infrastructure. It supports custom machine types, preemptible VMs for cost savings, and integration with other Google Cloud services.
- **Google Cloud Storage**
  - Google Cloud Storage (GCS) is a scalable, secure, and durable object storage service within Google Cloud Platform (GCP) designed for storing and retrieving unstructured data of any type or size. It allows users to store data in "buckets" and access it through APIs, web interfaces, or command-line tools for applications, backups, media hosting, and big data analytics.
- **Extract Data**
  - The first step in ETL processes involves extract data from data sources to a staging area. Data can come in various types and formats, from SQL or NoSQL databases and plan text to image and video files.
- **Transform Data**
  - In the second step, ETL tools transform and consolidate the raw data in the staging area to prepare it for the target data warehouse. The data transformation phase is normally the most complex and prone to errors, as it can involved multiple transformations, including basic data cleaning operations, deduplication, cata casting, filtering, grouping, encrypting, and many more.
- **Load Data**
  - In the third step, the transformed data is moved from the staging area into the targe data storage solution, such as a data warehouse or data lake. For most organizations, the data loading process is automated, well-defined, continuous and batch-driven.
- **Apache Airflow**
  - Apache Airflow is an open-source tool that helps you schedule, organize, and monitor workflows. Think of it like a to-do list for your data tasks, but smarter — you can set tasks to run in a specific order, track their progress, and see what happens if something fails.

### 2.14 Cluster Computing Basics
- **Cloud SQL (Database)**
  - Google Cloud SQL is a fully-managed, cost-effective and scalable database service that makes it easy to set-up, maintain, manage and administer MySQL, PostgreSQL, and SQL Server databases in the cloud. Hosted on Google Cloud Platform, Cloud SQL provides a database infrastructure for applications running anywhere.
- **Dataflow**
  - Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Typical use cases for Dataflow include Data movement,ETL processes, BI dashboarding, and applying ML in real time to streaming data.
- **dbt**
  - dbt, also known as the data build tool, is designed to simplify the management of data warehouses and transform the data within. This is primarily the T, or transformation, within ELT (or sometimes ETL) processes.
- **Luigi**
  - Luigi is a powerful, easy-to-use open-source framework for building data pipelines with Python. It handles dependency resolution, workflow management, visualization etc.
- **Prefect**
  - Prefect is an open-source orchestration engine that turns your Python functions into production-grade data pipelines with minimal friction. You can build and schedule workflows in pure Python—no DSLs or complex config files—and run them anywhere you can run Python.
- **What is Cluster Computing**
  - Cluster computing is a model where multiple computers are networked together to act as a unified processing system. Tasks are split across nodes in the cluster and executed in parallel.
- **Distributed File Systems**
  - A Distributed File System (DFS) allows multiple computers to access and share files across a network as if they were stored on a single local machine. It distributes data across multiple servers, enhancing accessibility and data redundancy.
- **HDFS**
  - HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines.

### 2.15 Big Data Tools
- **Job Scheduling**
  - A scheduling system manages and distributes computational jobs across multiple interconnected computers (a cluster) to optimize resource utilization and job completion. The goal is to efficiently allocate cluster resources (like processors and memory) to incoming jobs based on factors such as user priority, job requirements, and deadlines.
- **Cluster Management Tools**
  - Cluster management software maximizes the work that a cluster of computers can perform. A cluster manager balances workload to reduce bottlenecks, monitors the health of the elements of the cluster, and manages failover when an element fails.
- **Kubernetes**
  - Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. In data engineering, it is used to run pipeline workers, schedule jobs, and manage microservices.
- **HDFS**
  - HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines.
- **MapReduce**
  - MapReduce is a prominent data processing technique used by Data Analysts around the world. It allows them to handle large data sets with complex, unstructured data efficiently.
- **YARN**
  - Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks.
- **Apache Spark**
  - Apache Spark is a distributed data processing engine for large-scale batch and streaming workloads. It processes data in memory across a cluster, making it significantly faster than MapReduce for many workloads.

### 2.16 Containers & Orchestration
- **Apache Hadoop YARN**
  - Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks.
- **Docker**
  - Docker is the most widely used platform for building, shipping, and running containers. It packages code and its dependencies into a lightweight, portable image that runs the same in any environment.
- **Kubernetes**
  - Kubernetes is an open-source system for automating the deployment, scaling, and operation of containerized applications. It manages clusters of containers across multiple nodes and handles load balancing, self-healing, and rolling updates.
- **Google Cloud GKE**
  - Google Kubernetes Engine (GKE) is Google Cloud's managed Kubernetes service. It handles cluster provisioning, upgrades, and scaling automatically, reducing the operational burden of running Kubernetes.
- **AWS EKS**
  - Amazon EKS (Elastic Kubernetes Service) is AWS's managed Kubernetes service. It runs the Kubernetes control plane across multiple availability zones and integrates with AWS services like IAM, VPC, and ECR.
- **Circle CI**
  - CircleCI is a CI/CD service that can be integrated with GitHub, BitBucket and GitLab repositories. The service that can be used as a SaaS offering or self-managed using your own resources.

---

## 3. Advanced

### 3.1 CI/CD
- **GitLab CI**
  - GitLab offers a CI/CD service that can be used as a SaaS offering or self-managed using your own resources. You can use GitLab CI with any GitLab hosted repository, or any BitBucket Cloud or GitHub repository in the GitLab Premium self-managed, GitLab Premium SaaS and higher tiers.
- **GitHub Actions**
  - GitHub Actions is a CI/CD platform built into GitHub. It allows developers to define automated workflows as YAML files that trigger on code events like pushes and pull requests.
- **ArgoCD**
  - Argo CD is a declarative GitOps continuous delivery tool for Kubernetes. It continuously monitors a Git repository and ensures that the state of the Kubernetes cluster matches the desired state defined in code.

### 3.2 Monitoring
- **Prometheus**
  - Prometheus is a free software application used for event monitoring and alerting. It records real-time metrics in a time series database built using a HTTP pull model, with flexible queries and real-time alerting.
- **Datadog**
  - Datadog is a monitoring and analytics platform for large-scale applications. It encompasses infrastructure monitoring, application performance monitoring, log management, and user-experience monitoring.
- **Sentry**
  - Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services.
- **New Relic**
  - New Relic is an observability platform that helps you build better software. You can bring in data from any digital source so that you can fully understand your system and how to improve it.
- **Integration Testing**
  - Integration Testing is a type of testing where software modules are integrated logically and tested as a group. A typical software project consists of multiple software modules coded by different programmers.
- **Unit Testing**
  - Unit testing is where individual units (modules, functions/methods, routines, etc.) of software are tested to ensure their correctness. This low-level testing ensures smaller components are functionally sound while taking the burden off of higher-level tests.

### 3.3 Testing
- **End-to-End Testing**
  - End-to-end or (E2E) testing is a form of testing used to assert your entire application works as expected from start to finish or "end-to-end". E2E testing differs from unit testing in that it is completely decoupled from the underlying implementation details of your code.
- **Functional Testing**
  - Functional testing is a type of software testing that validates the software system against the functional requirements/specifications. The purpose of functional tests is to test each function of the software application by providing appropriate input and verifying the output against the functional requirements.
- **A/B Testing**
  - A/B testing is a way to compare two versions of something to see which one works better. You split your audience into two groups, one sees version A, the other sees version B — and then you measure which version gets better results, like more clicks, sales, or sign-ups.

### 3.4 Messaging Systems
- **Load Testing**
  - Load Testing is a type of Performance Testing that determines the performance of a system, software product, or software application under real-life-based load conditions. Load testing determines the behavior of the application when multiple users use it at the same time.
- **Smoke Testing**
  - Smoke Testing is a software testing process that determines whether the deployed software build is stable or not. Smoke testing is a confirmation for QA team to proceed with further software testing.
- **What and why use them?**
  - Messaging systems solve the problem of tight coupling between systems. Instead of one service directly calling another, it sends a message to a broker, and the consumer reads it when ready.
- **Async vs Sync Communication**
  - Synchronous communication means the sender waits for a response before continuing. Asynchronous communication means the sender sends a message and continues without waiting.
- **Messages vs Streams**
  - Messages are discrete, individual units of data sent from a producer to a consumer. Streams are continuous, ordered sequences of data that consumers process in real time or replay from a position.
- **Best Practices**
  - Best practices for messaging systems include designing idempotent consumers to handle duplicate delivery, setting appropriate retention and replication policies, monitoring consumer lag, and planning for schema evolution. Dead-letter queues are used to handle messages that fail processing repeatedly without losing them.

### 3.5 Infrastructure as Code - IaC
- **Apache Kafka**
  - Apache Kafka is an open-source stream-processing software platform developed by LinkedIn and donated to the Apache Software Foundation. It is written in Scala and Java and operates based on a message queue, designed to handle real-time data feeds.
- **RabbitMQ**
  - RabbitMQ is an open-source message broker that implements the AMQP protocol. It routes messages between producers and consumers using exchanges and queues, supporting patterns like publish/subscribe, work queues, and routing.
- **Declarative vs Imperative**
  - When it comes to Infrastructure as Code (IaC), there are two fundamental styles: imperative and declarative.
- **Idempotency**
  - Idempotency is a crucial concept in IaC. An idempotent operation produces the same result regardless of how many times it’s executed.
- **Reusability**
  - One of the goals of Infrastructure as Code (IaC) is to create modular, standardized units of code—like modules or templates that can be used across multiple projects, environments, and teams, embodying the "Don't Repeat Yourself" (DRY) principle. This approach significantly boosts efficiency, consistency, and maintainability, as it allows for rapid deployment of identical infrastructure patterns, enforces organizational standards, simplifies complex setups, and improves collaboration by providing shared, tested building blocks for infrastructure management.
- **Environmental Management**
  - Environmental management, or Environment as Code (EaC) takes the concept of Infrastructure as Code (IaC) one step further. EaC applies DevOps principles to manage and automate entire software environments—including infrastructure, applications, and configurations—using code, making them reproducible, versionable, and reliable.

### 3.6 Data Analytics
- **AWS SQS**
  - Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags.
- **AWS SNS**
  - Amazon SNS (Simple Notification Service) is a fully managed pub/sub messaging service from AWS. It allows a single message to be sent to multiple subscribers simultaneously through topics.
- **Terraform**
  - Terraform is an open-source infrastructure as code (IaC) tool developed by HashiCorp, used to define, provision, and manage cloud and on-premises infrastructure using declarative configuration files. It supports multiple cloud providers like AWS, Azure, and Google Cloud, as well as various services and platforms, enabling infrastructure automation across diverse environments.
- **OpenTofu**
  - OpenTofu is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle.

### 3.7 Business Intelligence
- **AWS CDK**
  - The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework used to provision cloud infrastructure resources in a safe, repeatable manner through AWS CloudFormation. AWS CDK offers the flexibility to write infrastructure as code in popular languages like Python, Java, Go, and C#.
- **Google Deployment  Mgr.**
  - Google Cloud Deployment Manager is an infrastructure deployment service that automates the creation and management of Google Cloud resources. It provides users with flexible template and configuration files to create deployments that have a variety of Google Cloud services, such as Cloud Storage, Compute Engine, and Cloud SQL, configured to work together.
- **Microsoft Power BI**
  - Microsoft Power BI is a business intelligence and data visualization platform from Microsoft. It connects to a wide range of data sources and allows users to build interactive dashboards and reports.

### 3.8 Reverse ETL
- **Streamlit**
  - Streamlit is a free and open-source framework to rapidly build and share machine learning and data science web apps. It is a Python-based library specifically designed for data and machine learning engineers.
- **Tableu**
  - Tableau is a powerful data visualization tool utilized extensively by data analysts worldwide. Its primary role is to transform raw, unprocessed data into an understandable format without any technical skills or coding.
- **Looker**
  - Looker is a Google cloud-based business intelligence and data analytics platform. It allows users to explore, analyze, and visualize data to gain insights and make data-driven decisions.
- **ETL vs Reverse ETL**
  - ETL (Extract, Transform, Load) moves data from operational systems into a data warehouse for analysis. Reverse ETL goes in the opposite direction, syncing processed data from the warehouse back into operational tools like Salesforce, HubSpot, or Intercom.
- **Reverse ETL Usecases**
  - Common use cases for reverse ETL include syncing customer health scores to a CRM, pushing segmented user lists to a marketing automation platform, and sending product usage data to customer success tools. It enables business teams to act on insights derived in the data warehouse without needing access to it directly.

### 3.9 Authentication, Authorization
- **Census**
  - Census is a reverse ETL platform that synchronizes data from a data warehouse to various business applications and SaaS apps like Salesforce and Hubspot. It's a crucial part of the modern data stack, enabling businesses to operationalize their data by making it available in the tools where teams work, like CRMs, marketing platforms, and more.
- **Hightouch**
  - Hightouch is a reverse ETL and AI platform crafted for marketing and personalization, allowing companies to uncover insights, execute campaigns, and develop AI agents using their data. It features an AI Decisioning Platform for lifecycle marketing and a Composable Customer Data Platform (CDP) that is adaptable, secure, and quick to deploy, built on top of a data warehouse.

### 3.10 Encryption
- **Segment**
  - Segment is an analytics platform that provides a single API for collecting, storing, and routing customer data from various sources. With Segment, data engineers can easily add analytics tracking to their app, without having to integrate with multiple analytics tools individually.

### 3.11 Tokenization
- **Data Quality**
  - Data quality refers to how well data meets the requirements for its intended use in terms of accuracy, completeness, consistency, timeliness, and validity. Poor data quality leads to incorrect analysis and poor decisions.

### 3.12 Data Masking
- **Data Lineage**
  - Data Lineage refers to the life-cycle of data, including its origins, movements, characteristics and quality. It's a critical component in Data Engineering for tracking the journey of data through every process in a pipeline, from raw input to model output.

### 3.13 Data Obfuscation
- **Metadata Management**
  - Metadata management involves capturing, storing, and governing information about data assets, including their structure, origin, ownership, and usage. A metadata catalog makes data discoverable and helps teams understand what data is available and how it is defined.
- **Data Interoperability**
  - Data interoperability is the ability of diverse systems and applications to access, exchange, and cooperatively use data in a coordinated and meaningful way, even across organizational boundaries. It ensures that data can flow freely, maintaining its integrity and context, allowing for improved efficiency, collaboration, and decision-making by breaking down data silos.
- **Data Quality**
  - Data quality refers to the degree to which a dataset is accurate, complete, consistent, relevant, and timely, making it fit for its intended use. High-quality data is reliable and trustworthy, enabling better decision-making, accurate analysis, and effective strategies, while poor data quality can lead to flawed insights, wasted resources, and negative consequences for an organization.
- **GDPR**
  - GDPR (General Data Protection Regulation) is a data privacy law enacted by the European Union that governs how personal data of EU residents is collected, stored, processed, and shared. It grants individuals rights over their data, including the right to access, correct, and delete it.
- **ECPA**
  - The Electronic Communications Privacy Act (ECPA) is a US federal law that regulates government access to electronic communications and stored data. It sets rules for when law enforcement can intercept communications or compel disclosure of stored data from service providers.
- **EU AI Act**
  - The Artificial Intelligence Act of the European Union, also known as the EU AI Act, is a comprehensive regulatory framework that is established to ensure safety and that fundamental human rights are upheld in the use of AI technologies. It governs the development and/or use of AI in the European Union.

---

## 4. Optional / Specialized Topics

- Choosing the Right Technologies
- Transactions
- ElasticSearch
- Memcached
- Metadata-first Architecture
- Serverless Options
- Batch
- Hybrid
- Realtime
- Google Cloud Storage
- Extract Data
- Transform Data
- Load Data
- Apache Airflow
- Prefect
- What is Cluster Computing
- Distributed File Systems
- HDFS
- MapReduce
- YARN
- Apache Spark
- AWS EKS
- Circle CI
- Integration Testing
- Unit Testing

---

## 5. References

- [Data Engineer Roadmap](https://roadmap.sh/data-engineer)

---

## 6. Related Roles / Topics

### Related Roles
- AI and Data Scientist
- PostgreSQL DBA
- Frontend Developer

### Related Skills
- SQL
- Python