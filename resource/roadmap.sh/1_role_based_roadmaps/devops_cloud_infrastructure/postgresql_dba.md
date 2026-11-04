# PostgreSQL DBA

## Metadata
- Type: Role
- Domain: Database Administration
- Source: roadmap.sh
- Source URL: https://roadmap.sh/postgresql-dba
- Related Roles:
  - Backend Developer
  - DevOps Engineer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Introduction
- **What are Relational Databases?**
  - Relational databases are a type of database management system (DBMS) that stores and organizes data in a structured format called tables. These tables are made up of rows, also known as records or tuples, and columns, which are also called attributes or fields.
- **RDBMS Benefits and Limitations**
  - Relational Database Management Systems (RDBMS) offer several benefits, including robust data integrity through ACID (Atomicity, Consistency, Isolation, Durability) compliance, powerful querying capabilities with SQL, and strong support for data relationships via foreign keys and joins. They are highly scalable vertically and can handle complex transactions reliably.
- **PostgreSQL vs Other RDBMS**
  - PostgreSQL stands out among other RDBMS options due to its open-source nature, advanced features, and robust performance. Unlike proprietary systems like Oracle or Microsoft SQL Server, PostgreSQL is free to use and highly extensible, allowing users to add custom functions, data types, and operators.
- **PostgreSQL vs NoSQL Databases**
  - PostgreSQL, a powerful open-source relational database system, excels in handling complex queries, ensuring data integrity, and supporting ACID transactions, making it ideal for applications requiring intricate data relationships and strong consistency. It offers advanced features like JSON support for semi-structured data, full-text search, and extensive indexing capabilities.
- **Queries**
  - Queries are the primary way to interact with a PostgreSQL database and retrieve or manipulate data stored within its tables. In this section, we will cover the fundamentals of querying in PostgreSQL - from basic SELECT statements to more advanced techniques like joins, subqueries, and aggregate functions.
- **Data Types**
  - PostgreSQL offers a rich and diverse set of data types, catering to a wide range of applications and ensuring data integrity and performance. These include standard numeric types such as integers, floating-point numbers, and serial types for auto-incrementing fields.
- **Columns**
  - Columns are a fundamental component of PostgreSQL's object model. They are used to store the actual data within a table and define their attributes such as data type, constraints, and other properties.
- **Schemas**
  - Schemas are an essential part of PostgreSQL's object model, and they help provide structure, organization, and namespacing for your database objects. A schema is a collection of database objects, such as tables, views, indexes, and functions, that are organized within a specific namespace.

### 1.2 Basic RDBMS Concepts
- **Basic RDBMS Concepts**
  - Relational Database Management Systems (RDBMS) are a type of database management system which stores and organizes data in tables, making it easy to manipulate, query, and manage the information. They follow the relational model defined by E.F.

### 1.3 Object Model
- **Rows**
  - A row in PostgreSQL represents a single, uniquely identifiable record with a specific set of fields in a table. Each row in a table is made up of one or more columns, where each column can store a specific type of data (e.g., integer, character, date, etc.).
- **Tables**
  - A table is one of the primary data storage objects in PostgreSQL. In simple terms, a table is a collection of rows or records, organized into columns.
- **Databases**
  - In PostgreSQL, a database is a named collection of tables, indexes, views, stored procedures, and other database objects. Each PostgreSQL server can manage multiple databases, enabling the separation and organization of data sets for various applications, projects, or users.

### 1.4 High Level Database Concepts
- **ACID**
  - ACID are the four properties of relational database systems that help in making sure that we are able to perform the transactions in a reliable manner. It's an acronym which refers to the presence of four properties: atomicity, consistency, isolation and durability
- **MVCC**
  - Multi-Version Concurrency Control (MVCC) is a technique used by PostgreSQL to allow multiple transactions to access the same data concurrently without conflicts or delays. It ensures that each transaction has a consistent snapshot of the database and can operate on its own version of the data.
- **Transactions**
  - Transactions are a fundamental concept in database management systems, allowing multiple statements to be executed within a single transaction context. In PostgreSQL, transactions provide ACID (Atomicity, Consistency, Isolation, and Durability) properties, which ensure that your data remains in a consistent state even during concurrent access or system crashes.
- **Write-ahead Log**
  - The Write Ahead Log, also known as the WAL, is a crucial part of PostgreSQL's data consistency strategy. The WAL records all changes made to the database in a sequential log before they are written to the actual data files.
- **Query Processing**
  - Query processing is an important aspect of a database system, as it is responsible for managing data retrieval and modification using Structured Query Language (SQL) queries. Efficient query processing is crucial for ensuring optimal database performance.

---

## 2. Intermediate

### 2.1 Relational Model
- **Domains**
  - Domains in PostgreSQL are essentially user-defined data types that can be created using the CREATE DOMAIN command. These custom data types allow you to apply constraints and validation rules to columns in your tables by defining a set of values that are valid for a particular attribute or field.
- **Attributes**
  - Attributes in the relational model are the columns of a table, representing the properties or characteristics of the entity described by the table. Each attribute has a domain, defining the possible values it can take, such as integer, text, or date.
- **Tuples**
  - In the relational model, a tuple is a fundamental concept that represents a single record or row in a table. In PostgreSQL, a tuple is composed of a set of attribute values, each corresponding to a specific column or field in the table.
- **Relations**
  - In the relational model, a relation is essentially a table composed of rows and columns, where each row represents a unique record (or tuple) and each column represents an attribute of the data. The structure of a relation is defined by its schema, which specifies the relation's name and the names and data types of its attributes.
- **Constraints**
  - Constraints are an essential part of the relational model, as they define rules that the data within the database must follow. They ensure that the data is consistent, accurate, and reliable.

### 2.2 Installation and Setup
- **NULL**
  - In the relational model used by PostgreSQL, null values represent missing or unknown information within a database. Unlike zero, empty strings, or other default values, null signifies the absence of a value and is treated uniquely in operations and queries.
- **Using Docker**
  - Docker is an excellent tool for simplifying the installation and management of applications, including PostgreSQL. By using Docker, you can effectively isolate PostgreSQL from your system and avoid potential conflicts with other installations or configurations.
- **Package Managers**
  - Package managers are essential tools that help you install, update, and manage software packages on your system. They keep track of dependencies, handle configuration files and ensure that the installation process is seamless for the end-user.
- **Using `systemd`**
  - Using systemd to manage PostgreSQL involves utilizing the system and service manager to control the PostgreSQL service. This allows you to start, stop, and manage PostgreSQL automatically with the boot process.

### 2.3 Learn SQL
- **For Schemas**
  - A schema is a logical collection of database objects within a PostgreSQL database. It behaves like a namespace that allows you to group and isolate your database objects separately from other schemas.
- **ForTables**
  - The primary DDL statements for creating and managing tables in PostgreSQL include CREATE TABLE, ALTER TABLE, and DROP TABLE, these DDL commands allow you to create, modify, and delete tables and their structures, providing a robust framework for database schema management in PostgreSQL.
- **Data Types**
  - PostgreSQL offers a comprehensive set of data types to cater to diverse data needs, including numeric types like INTEGER, FLOAT, and SERIAL for auto-incrementing fields; character types such as VARCHAR and TEXT for variable-length text; and temporal types like DATE, TIME, and TIMESTAMP for handling date and time data. Additionally, PostgreSQL supports BOOLEAN for true/false values, ENUM for enumerated lists, and composite types for complex structures.
- **Querying Data**
  - Querying data with Data Manipulation Language (DML) in PostgreSQL involves using SQL statements to retrieve and manipulate data within the database. The primary DML statements for querying and modifying data are SELECT, INSERT, UPDATE, and DELETE.
- **Filtering Data**
  - Filtering data is an essential feature in any database management system, and PostgreSQL is no exception. When we refer to filtering data, we're talking about selecting a particular subset of data that fulfills specific criteria or conditions.
- **Modifying Data**
  - Modifying data in PostgreSQL is an essential skill when working with databases. The primary DML queries used to modify data are INSERT, UPDATE, and DELETE.
- **Joining Tables**
  - Joining tables is a fundamental operation in the world of databases. It allows you to combine information from multiple tables based on common columns.
- **Import / Export Using `COPY`**
  - In PostgreSQL, one of the fastest and most efficient ways to import and export data is by using the COPY command. The COPY command allows you to import data from a file, or to export data to a file from a table or a query result.
- **Transactions**
  - Transactions are a fundamental concept in database management systems, allowing multiple statements to be executed within a single transaction context. In PostgreSQL, transactions provide ACID (Atomicity, Consistency, Isolation, and Durability) properties, which ensure that your data remains in a consistent state even during concurrent access or system crashes.
- **CTE**
  - A Common Table Expression, also known as CTE, is a named temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement. CTEs are particularly helpful when dealing with complex queries, as they enable you to break down the query into smaller, more readable chunks.
- **Lateral Join**
  - Lateral join allows you to reference columns from preceding tables in a query, making it possible to perform complex operations that involve correlated subqueries and the application of functions on tables in a cleaner and more effective way. The LATERAL keyword in PostgreSQL is used in conjunction with a subquery in the FROM clause of a query.

### 2.4 Configuring
- **Connect using `psql`**
  - psql is an interactive command-line utility that enables you to interact with a PostgreSQL database server. Using psql, you can perform various SQL operations on your database.
- **Deployment in Cloud**
  - In this section, we will discuss deploying PostgreSQL in the cloud. Deploying your PostgreSQL database in the cloud offers significant advantages such as scalability, flexibility, high availability, and cost reduction.
- **Using `pg_ctl`**
  - pgctl is a command-line utility that enables you to manage a PostgreSQL database server. With pgctl, you can start, stop, and restart the PostgreSQL service, among other tasks.
- **Using `pg_ctlcluster`**
  - pgctlcluster is a command-line utility provided by PostgreSQL to manage database clusters. It is especially helpful for users who have multiple PostgreSQL clusters running on the same system.
- **Subqueries**
  - A subquery is a query nested inside another query, often referred to as the outer query. Subqueries are invaluable tools for retrieving information from multiple tables, performing complex calculations, or applying filter criteria based on the results of other queries.
- **Grouping**
  - Grouping is a powerful technique in SQL that allows you to organize and aggregate data based on common values in one or more columns. The GROUP BY clause is used to create groups, and the HAVING clause is used to filter the group based on certain conditions.
- **Set Operations**
  - Set operations are useful when you need to perform actions on whole sets of data, such as merging or comparing them. Set operations include UNION, INTERSECT, and EXCEPT, and they can be vital tools in querying complex datasets.
- **Resource Usage**
  - Configuring PostgreSQL for optimal resource usage involves adjusting settings in the postgresql.conf file to balance memory, CPU, and disk usage.
- **Reporting Logging & Statistics**
  - When working with PostgreSQL, it is often useful to analyze the performance of your queries and system as a whole. This can help you optimize your database and spot potential bottlenecks.
- **Adding Extra Extensions**
  - PostgreSQL provides various extensions to enhance its features and functionalities. Extensions are optional packages that can be loaded into your PostgreSQL database to provide additional functionality like new data types or functions.
- **Default Privileges**
  - PostgreSQL allows you to define object privileges for various types of database objects. These privileges determine if a user can access and manipulate objects like tables, views, sequences, or functions.

### 2.5 Security
- **Write-ahead Log**
  - The Write Ahead Log, also known as the WAL, is a crucial part of PostgreSQL's data consistency strategy. The WAL records all changes made to the database in a sequential log before they are written to the actual data files.
- **Vacuums**
  - Vacuuming is an essential component in PostgreSQL maintenance tasks. By reclaiming storage, optimizing performance, and keeping the database lean, vacuuming helps maintain the health of your PostgreSQL system.
- **Replication**
  - Replication, in simple terms, is the process of copying data from one database server to another. It helps in maintaining a level of redundancy and improving the performance of databases.
- **Query Planner**
  - The PostgreSQL query planner is an essential component of the system that's responsible for optimizing the execution of SQL queries. It finds the most efficient way to join tables, establish subquery relationships, and determine the order of operations based on available data, query structure, and the current PostgreSQL configuration settings.
- **Checkpoints / Background Writer**
  - In PostgreSQL, checkpoints and the background writer are essential for maintaining data integrity and optimizing performance. Checkpoints periodically write all modified data (dirty pages) from the shared buffers to the disk, ensuring that the database can recover to a consistent state after a crash.
- **Object Privileges**
  - Object privileges in PostgreSQL are the permissions given to different user roles to access or modify database objects like tables, views, sequences, and functions. Ensuring proper object privileges is crucial for maintaining a secure and well-functioning database.
- **Grant / Revoke**
  - One of the most important aspects of database management is providing appropriate access permissions to users. In PostgreSQL, this can be achieved with the GRANT and REVOKE commands, which allow you to manage the privileges of database objects such as tables, sequences, functions, and schemas.
- **Advanced Topics**
  - In addition to basic PostgreSQL security concepts, such as user authentication, privilege management, and encryption, there are several advanced topics that you should be aware of to enhance the security of your PostgreSQL databases.
- **Row-Level Security**
  - Row Level Security (RLS) is a feature introduced in PostgreSQL 9.5 that allows you to control access to rows in a table based on a user or role's permissions. This level of granularity in data access provides an extra layer of security for protecting sensitive information from unauthorized access.
- **Authentication Models**
  - PostgreSQL supports various authentication models to control access, including trust (no password, for secure environments), password-based (md5 and scram-sha-256 for hashed passwords), GSSAPI and SSPI (Kerberos for secure single sign-on), LDAP (centralized user management), certificate-based (SSL certificates for strong authentication), PAM (leveraging OS-managed authentication), Ident (verifying OS user names), and RADIUS (centralized authentication via RADIUS servers). These methods are configured in the pghba.conf file, specifying the appropriate authentication method for different combinations of databases, users, and client addresses, ensuring flexible and secure access control.
- **Roles**
  - In PostgreSQL, roles are entities that manage database access permissions, combining user and group functionalities. Roles can own database objects and have privileges, such as the ability to create databases or tables.
- **pg_hba.conf**
  - When securing your PostgreSQL database, one of the most important components to configure is the pghba.conf (short for PostgreSQL Host-Based Authentication Configuration) file. This file is a part of PostgreSQL's Host-Based Authentication (HBA) system and is responsible for controlling how clients authenticate and connect to your database.
- **SSL Settings**
  - Securing the communication channels is a crucial aspect of protecting your PostgreSQL database from different types of attacks. One way to achieve this security is by using SSL (Secure Socket Layer) connections.

### 2.6 Infrastructure Skills
- **SELinux**
  - SELinux, or Security-Enhanced Linux, is a Linux kernel security module that brings heightened access control and security policies to your system. It is specifically designed to protect your system from unauthorized access and data leaks by enforcing a strict security policy, preventing processes from accessing resources they shouldn't, which is a significant tool for database administrators to help secure PostgreSQL instances.
- **PostgreSQL Anonymizer**
  - Visit the following resources to learn more:
- **barman**
  - Barman (Backup and Recovery Manager) is a robust tool designed for managing PostgreSQL backups and disaster recovery. It supports various backup types, including full and incremental backups, and provides features for remote backups, backup retention policies, and compression to optimize storage.
- **WAL-G**
  - WAL-G is an open-source archival and restoration tool for PostgreSQL and MySQL/MariaDB, designed for managing Write-Ahead Logs (WAL) and performing continuous archiving. It extends the capabilities of the traditional pgbasebackup by supporting features like delta backups, compression, and encryption.
- **pgbackrest**
  - Visit the following resources to learn more:
- **pg_probackup**
  - pgprobackup is a backup and recovery manager for PostgreSQL, designed to handle periodic backups of PostgreSQL clusters. It supports incremental backups, merge strategies to avoid frequent full backups, validation, and parallelization for efficiency.
- **pg_dump**
  - pgdump is a utility for backing up a PostgreSQL database by exporting its data and schema. Unlike pgbasebackup, which takes a physical backup of the entire cluster, pgdump produces a logical backup of a single database.
- **pg_dumpall**
  - pgdumpall is a utility for backing up all databases in a PostgreSQL cluster, including cluster-wide data such as roles and tablespaces. It creates a plain text SQL script file that contains the commands to recreate the cluster's databases and their contents, as well as the global objects.
- **pg_restore**
  - Visit the following resources to learn more:
- **pg_basebackup**
  - pgbasebackup is a utility for creating a physical backup of a PostgreSQL database cluster. It generates a consistent backup of the entire database cluster by copying data files while ensuring write operations do not interfere.

---

## 3. Advanced

### 3.1 Learn to Automate
- **Using `pg_upgrade`**
  - pgupgrade is a PostgreSQL utility that facilitates the in-place upgrade of a PostgreSQL database cluster to a new major version. It allows users to upgrade their database without needing to dump and restore the database, significantly reducing downtime.
- **Using Logical Replication**
  - Logical replication is an asynchronous feature that allows data modification to be transferred from a source (publisher) to a target system (subscriber) across different PostgreSQL database versions. It provides more granular control over the data copied and is useful during an upgrade.
- **Simple Stateful Setup**
  - Here are the key components and steps involved in setting up a simple stateful PostgreSQL deployment on Kubernetes:
- **Helm**
  - Helm is a popular package manager for Kubernetes that allows you to easily deploy, manage, and upgrade applications on your Kubernetes cluster. In the Kubernetes world, Helm plays a similar role as "apt" or "yum" in the Linux ecosystem.
- **Operators**
  - Visit the following resources to learn more:
- **HAProxy**
  - HAProxy, short for High Availability Proxy, is a popular open-source software used to provide high availability, load balancing, and proxying features for TCP and HTTP-based applications. It is commonly used to improve the performance, security, and reliability of web applications, databases, and other services.
- **Consul**
  - Consul is a distributed, highly-available, and multi-datacenter aware service discovery and configuration tool developed by HashiCorp. It can be used to implement load balancing in a PostgreSQL cluster to distribute client connections and queries evenly across multiple backend nodes.
- **KeepAlived**
  - Keepalived is a robust and widely-used open-source solution for load balancing and high availability. It helps to maintain a stable and perfect working environment even in the presence of failures such as server crashes or connectivity issues.
- **Etcd**
  - Etcd is a distributed key-value store that provides an efficient and reliable means for storing crucial data across clustered environments. It has become popular as a fundamental component for storing configuration data and service discovery in distributed systems.
- **Prometheus**
  - Prometheus is an open-source systems monitoring and alerting toolkit designed for reliability and scalability. Originally developed at SoundCloud, it is now a part of the Cloud Native Computing Foundation.
- **Zabbix**
  - Zabbix is an open-source monitoring software for networks, servers, virtual machines, and cloud services. It provides real-time monitoring, alerting, and visualization of metrics collected from various IT infrastructure components.
- **check_pgactivity**
  - Visit the following resources to learn more:
- **temBoard**
  - temBoard is an open-source monitoring and management tool for PostgreSQL databases developed by Dalibo. It provides a web-based interface that helps database administrators (DBAs) manage and monitor multiple PostgreSQL instances efficiently.
- **check_pgbackrest**
  - Monitoring pgBackRest helps ensure that your PostgreSQL backups are consistent, up-to-date, and free from any potential issues. By regularly checking your backups, you'll be able to maintain a reliable and efficient backup-restore process for your PostgreSQL database.
- **Backup Validation Procedures**
  - It's not enough to just take backups; you must also ensure that your backups are valid and restorable. A corrupt or incomplete backup can lead to data loss or downtime during a crisis.
- **PgBouncer**
  - Visit the following resources to learn more:
- **PgBouncer Alternatives**
  - Pgpool-II, HAProxy, and Odyssey are prominent tools for enhancing PostgreSQL performance and availability. Pgpool-II is a versatile connection pooler offering load balancing, replication, and connection limits to optimize performance.
- **Logical Replication**
  - Logical replication in PostgreSQL allows the selective replication of data between databases, providing flexibility in synchronizing data across different systems. Unlike physical replication, which copies entire databases or clusters, logical replication operates at a finer granularity, allowing the replication of individual tables or specific subsets of data.
- **Streaming Replication**
  - Streaming Replication is a powerful feature in PostgreSQL that allows efficient real-time replication of data across multiple servers. It is a type of asynchronous replication, meaning that the replication process occurs continuously in the background without waiting for transactions to be committed.
- **Patroni**
  - Patroni is an open-source tool that automates the setup, management, and failover of PostgreSQL clusters, ensuring high availability. It leverages distributed configuration stores like Etcd, Consul, or ZooKeeper to maintain cluster state and manage leader election.
- **Patroni Alternatives**
  - While Patroni is a popular choice for managing PostgreSQL clusters, there are several other tools and frameworks available that you might consider as alternatives to Patroni. Each of these has its unique set of features and benefits, and some may be better suited to your specific requirements or use-cases.
- **Resource Usage / Provisioning / Capacity Planning**
  - Capacity planning and resource management are essential skills for professionals working with PostgreSQL. A well-designed infrastructure balances resource usage among the server, I/O, and storage systems to maintain smooth database operations.
- **Shell Scripts**
  - Shell scripts are a powerful tool used to automate repetitive tasks and perform complex operations. They are essentially text files containing a sequence of commands to be executed by the shell (such as Bash or Zsh).
- **Any Programming Language**
  - PostgreSQL supports various languages for providing server-side scripting and developing custom functions, triggers, and stored procedures. When choosing a language, consider factors such as the complexity of the task, the need for a database connection, and the trade-off between learning a new language and leveraging existing skills.
- **Ansible**
  - Ansible is a widely used open-source configuration management and provisioning tool that helps automate many tasks for managing servers, databases, and applications. It uses a simple, human-readable language called YAML to define automation scripts, known as “playbooks”.
- **Salt**
  - Salt (SaltStack) is an open-source configuration management, remote execution, and automation tool that helps you manage, automate, and orchestrate your PostgreSQL infrastructure. Salt is an excellent choice for managing your PostgreSQL infrastructure, providing a powerful, flexible, and extensible solution to help you maintain consistency and automate common tasks seamlessly.
- **Chef**
  - Chef is a powerful and widely-used configuration management tool that provides a simple yet customizable way to manage your infrastructure, including PostgreSQL installations. Chef is an open-source automation platform written in Ruby that helps users manage their infrastructure by creating reusable and programmable code, called "cookbooks" and "recipes", to define the desired state of your systems.
- **Puppet**
  - Puppet is an open-source software configuration management tool that enables system administrators to automate the provisioning, configuration, and management of a server infrastructure. It helps minimize human errors, ensures consistency across multiple systems, and simplifies the process of managing PostgreSQL installations.
- **Practical Patterns / Antipatterns**
  - Practical patterns for PostgreSQL migrations include using version control tools like Liquibase or Flyway to manage schema changes, applying incremental updates to minimize risk, maintaining backward compatibility during transitions, and employing zero-downtime techniques like rolling updates. Data migration scripts should be thoroughly tested in staging environments to ensure accuracy.
- **Migration Related Tools**
  - Migrations are crucial in the lifecycle of database applications. As the application evolves, changes to the database schema and sometimes data itself become necessary.
- **Bulk Loading / Processing Data**
  - Bulk load process data involves transferring large volumes of data from external files into the PostgreSQL database. This is an efficient way to insert massive amounts of data into your tables quickly, and it's ideal for initial data population or data migration tasks.
- **Data Partitioning**
  - Data partitioning is a technique that divides a large table into smaller, more manageable pieces called partitions. Each partition is a smaller table that stores a subset of the data, usually based on specific criteria such as ranges, lists, or hashes.
- **Sharding Patterns**
  - Sharding is a technique that splits a large dataset across multiple database instances or servers, called shards. Each shard is an independent and self-contained unit that holds a portion of the overall data, and shards can be distributed across different geographical locations or infrastructures.
- **Patterns / Antipatterns**
  - Practical patterns for implementing queues in PostgreSQL include using a dedicated table to store queue items, leveraging the FOR UPDATE SKIP LOCKED clause to safely dequeue items without conflicts, and partitioning tables to manage large volumes of data efficiently. Employing batch processing can also enhance performance by processing multiple queue items in a single transaction.

### 3.2 SQL Query Patterns / Anti-patterns
- **Normalization / Normal Forms**
  - Data normalization in PostgreSQL involves organizing tables to minimize redundancy and ensure data integrity through a series of normal forms: First Normal Form (1NF) ensures each column contains atomic values and records are unique; Second Normal Form (2NF) requires that all non-key attributes are fully dependent on the primary key; Third Normal Form (3NF) eliminates transitive dependencies so non-key attributes depend only on the primary key; Boyce-Codd Normal Form (BCNF) further ensures that every determinant is a candidate key; Fourth Normal Form (4NF) removes multi-valued dependencies; and Fifth Normal Form (5NF) addresses join dependencies, ensuring tables are decomposed without loss of data integrity. These forms create a robust framework for efficient, consistent, and reliable database schema design.
- **PgQ**
  - Skytools is a set of tools developed by Skype to assist with using PostgreSQL databases. One of the key components of Skytools is PGQ, a queuing system built on top of PostgreSQL that provides efficient and reliable data processing.
- **Processes & Memory Architecture**
  - PostgreSQL’s process memory architecture is designed to efficiently manage resources and ensure performance. It consists of several key components:
- **Vacuum Processing**
  - Vacuum processing is an essential aspect of maintaining the performance and stability of a PostgreSQL database. PostgreSQL uses a storage technique called Multi-Version Concurrency Control (MVCC), which allows multiple transactions to access different versions of a database object simultaneously.
- **Buffer Management**
  - PostgreSQL uses a buffer pool to efficiently cache frequently accessed data pages in memory. The buffer pool is a fixed-size, shared memory area where database blocks are stored while they are being used, modified or read by the server.
- **Lock Management**
  - Lock management in PostgreSQL is implemented using a lightweight mechanism that allows database objects, such as tables, rows, and transactions, to be locked in certain modes. The primary purpose of locking is to prevent conflicts that could result from concurrent access to the same data or resources.
- **Physical Storage and File Layout**
  - PostgreSQL's physical storage and file layout optimize data management and performance through a structured organization within the data directory, which includes subdirectories like base for individual databases, global for cluster-wide tables, pgwal for Write-Ahead Logs ensuring durability, and pgtblspc for tablespaces allowing flexible storage management. Key configuration files like postgresql.conf, pghba.conf, and pgident.conf are also located here.
- **System Catalog**
  - The PostgreSQL system catalog is a set of tables and views that store metadata about the database objects, providing critical information for database management and querying. Key system catalog tables include pgdatabase (information about databases), pgtables (details of tables), pgindexes (index information), pgclass (general information about tables, indexes, and sequences), pgattribute (column details for each table), and pgroles (user and role information).
- **Per-User, Per-Database Setting**
  - In PostgreSQL, per-user and per-database settings allow administrators to customize configurations for specific users or databases, enhancing performance and management. These settings are managed using the ALTER ROLE and ALTER DATABASE commands.
- **Storage Parameters**
  - Storage parameters help optimize the database's performance by allowing you to configure settings related to memory usage, storage behavior, and buffer management for specific tables and indexes. PostgreSQL provides several configuration options to tailor the behavior of storage and I/O on a per-table or per-index basis.
- **OLTP**
  - Online Transaction Processing (OLTP) in PostgreSQL refers to a class of systems designed to manage transaction-oriented applications, typically for data entry and retrieval transactions in database systems. OLTP systems are characterized by a large number of short online transactions (INSERT, UPDATE, DELETE), where the emphasis is on speed, efficiency, and maintaining data integrity in multi-access environments.
- **OLAP**
  - Online Analytical Processing (OLAP) in PostgreSQL refers to a class of systems designed for query-intensive tasks, typically used for data analysis and business intelligence. OLAP systems handle complex queries that aggregate large volumes of data, often from multiple sources, to support decision-making processes.
- **HTAP**
  - Hybrid Transactional/Analytical Processing (HTAP) in PostgreSQL refers to a database system's ability to efficiently handle both Online Transaction Processing (OLTP) and Online Analytical Processing (OLAP) workloads simultaneously. PostgreSQL achieves this through its robust architecture, which supports ACID transactions for OLTP and advanced analytical capabilities for OLAP.
- **PL/pgSQL**
  - PL/pgSQL is a procedural language for the PostgreSQL database system that enables you to create stored procedures and functions using conditionals, loops, and other control structures, similar to a traditional programming language. Using PL/pgSQL, you can perform complex operations on the server-side, reducing the need to transfer data between the server and client.
- **Procedures and Functions**
  - In PostgreSQL, functions and procedures encapsulate reusable logic within the database to enhance performance and maintain organization. Functions return a value or a table, take input parameters, and are used in SQL queries, defined with CREATE FUNCTION.
- **Triggers**
  - Triggers are special user-defined functions that get invoked automatically when an event (like INSERT, UPDATE, DELETE, or TRUNCATE) occurs on a specified table or view. They allow you to perform additional actions when data is modified in the database, helping to maintain the integrity and consistency of your data.
- **Recursive CTE**
  - Recursive CTEs are a powerful feature in SQL that allow you to build complex hierarchical queries, retrieve data stored in hierarchical structures or even perform graph traversal. In simple terms, a recursive CTE is a CTE that refers to itself in its own definition, creating a loop that iterates through the data until a termination condition is met.
- **Aggregate and Window functions**
  - Aggregate functions in PostgreSQL perform calculations on a set of rows and return a single value, such as SUM(), AVG(), COUNT(), MAX(), and MIN(). Window functions, on the other hand, calculate values across a set of table rows related to the current row while preserving the row structure.
- **top**
  - top is a command-line utility that comes pre-installed on most Unix-based operating systems such as Linux, macOS, and BSD. It provides a dynamic, real-time view of the processes running on a system, displaying valuable information like process ID, user, CPU usage, memory usage, and more.
- **sysstat**
  - Sysstat is a collection of performance monitoring tools for Linux. It collects various system statistics, such as CPU usage, memory usage, disk activity, network traffic, and more.
- **iotop**
  - iotop is an essential command-line utility that provides real-time insights into the input/output (I/O) activities of processes running on your system. This tool is particularly useful when monitoring and managing your PostgreSQL database's performance, as it helps system administrators or database developers to identify processes with high I/O, leading to potential bottlenecks or server optimization opportunities.
- **gdb**
  - GDB, the GNU Debugger, is a powerful debugging tool that provides inspection and modification features for applications written in various programming languages, including C, C++, and Fortran. GDB can be used alongside PostgreSQL for investigating backend processes and identifying potential issues that might not be apparent at the application level.
- **strace**
  - strace is a powerful command-line tool used to diagnose and debug programs on Linux systems. It allows you to trace the system calls made by the process you're analyzing, allowing you to observe its interaction with the operating system.
- **ebpf**
  - eBPF is a powerful Linux kernel technology used for tracing and profiling various system components such as processes, filesystems, network connections, and more. It has gained enormous popularity among developers and administrators because of its ability to offer deep insights into the system's behavior, performance, and resource usage at runtime.
- **perf-tools**
  - Perf tools is a suite of performance analysis tools that comes as part of the Linux kernel. It enables you to monitor various performance-related events happening in your system, such as CPU cycles, instructions executed, cache misses, and other hardware-related metrics.
- **Core Dumps**
  - A core dump is a file that contains the memory image of a running process and its process status. It's typically generated when a program crashes or encounters an unrecoverable error, allowing developers to analyze the state of the program at the time of the crash.
- **pgBadger**
  - PgBadger is a fast, efficient PostgreSQL log analyzer and report generator. It parses PostgreSQL log files to generate detailed reports on database performance, query statistics, connection information, and more.
- **pgCluu**
  - PgCluu is a powerful and easy-to-use PostgreSQL performance monitoring and tuning tool. This open-source program collects statistics and provides various metrics in order to analyze PostgreSQL databases, helping you discover performance bottlenecks and optimize your cluster's performance.
- **awk**
  - Awk is a versatile text processing tool that is widely used for various data manipulation, log analysis, and text reporting tasks. It is especially suitable for working with structured text data, such as data in columns.
- **grep**
  - Grep is a powerful command-line tool used for searching plain-text data sets against specific patterns. It was originally developed for the Unix operating system and has since become available on almost every platform.
- **sed**
  - Sed is a powerful command-line utility for text processing and manipulation in Unix-based systems, including Linux operating systems. It operates on a text stream – reading from a file, standard input, or a pipe from another command – and applies a series of editing instructions known as "scripts" to transform the input text into a desired output format.
- **pg_stat_activity**
  - pgstatactivity is a crucial system view in PostgreSQL that provides real-time information on current database connections and queries being executed. This view is immensely helpful when troubleshooting performance issues, identifying long-running or idle transactions, and managing the overall health of the database.
- **pg_stat_statements**
  - Pg Stat Statements is a system view in PostgreSQL that provides detailed statistics on the execution of SQL queries. It is particularly useful for developers and database administrators to identify performance bottlenecks, optimize query performance, and troubleshoot issues.
- **pgcenter**
  - pgcenter is a command-line tool that provides real-time monitoring and management for PostgreSQL databases. It offers a convenient interface for tracking various aspects of database performance, allowing users to quickly identify bottlenecks, slow queries, and other potential issues.
- **EXPLAIN**
  - Understanding the performance and efficiency of your queries is crucial when working with databases. In PostgreSQL, the EXPLAIN command helps to analyze and optimize your queries by providing insights into the query execution plan.
- **Depesz**
  - "Depesz" is a popular, online query analysis tool for PostgreSQL, named after Hubert "depesz" Lubaczewski, the creator of the tool. It helps you understand and analyze the output of EXPLAIN ANALYZE, a powerful command in PostgreSQL for examining and optimizing your queries.
- **PEV2**
  - pev2, or Postgres Explain Visualizer v2, is an open-source tool designed to make query analysis with PostgreSQL easier and more understandable. By providing a visual representation of the EXPLAIN ANALYZE output, pev2 simplifies query optimization by displaying the query plan and execution metrics in a readable structure.
- **Tensor**
  - Tensor Query Language (TQL) is a specialized SQL-like language designed for querying and managing datasets stored as tensors, primarily used within the Deep Lake platform. TQL extends traditional SQL capabilities to support multidimensional array operations, making it particularly useful for data science and machine learning workflows.
- **explain.dalibo.com**
  - explain.dalibo.com is a free service that allows you to analyze the execution plan of your queries. It is based on the explain.depesz.com service.
- **USE**
  - The Utilization Saturation and Errors (USE) Method is a methodology for analyzing the performance of any system. It directs the construction of a checklist, which for server analysis can be used for quickly identifying resource bottlenecks or errors.
- **RED**
  - The acronym stands for Rate, Errors, and Duration. These are request-scoped, not resource-scoped as the USE method is.
- **Golden Signals**
  - Golden Signals are a set of metrics that help monitor application performance and health, particularly in distributed systems. These metrics are derived from Google's Site Reliability Engineering (SRE) practices and can be easily applied to PostgreSQL troubleshooting methods.

### 3.3 Schema Design Patterns / Anti-patterns
- **Schema Design Patterns / Anti-patterns**
  - Schema design patterns in PostgreSQL ensure efficient and scalable databases by using normalization to reduce redundancy and maintain data integrity, while denormalization improves read performance for read-heavy applications. Employing star and snowflake schemas optimizes query performance in data warehousing, with the former having a central fact table and the latter normalizing dimension tables.

### 3.4 Indexes and their Usecases
- **B-Tree**
  - B-Tree (short for Balanced Tree) is the default index type in PostgreSQL, and it's designed to work efficiently with a broad range of queries. A B-Tree is a data structure that enables fast search, insertion, and deletion of elements in a sorted order.
- **Hash**
  - Hash Indexes are a type of database index that uses a hash function to map each row's key value into a fixed-length hashed key. The purpose of using a hash index is to enable quicker search operations by converting the key values into a more compact and easily searchable format.
- **GiST**
  - The Generalized Search Tree (GiST) is a powerful and flexible index type in PostgreSQL that serves as a framework to implement different indexing strategies. GiST provides a generic infrastructure for building custom indexes, extending the core capabilities of PostgreSQL.
- **SP-GiST**
  - The Spatial Generalized Search Tree (SP-GiST) is an advanced indexing structure in PostgreSQL designed to efficiently manage spatial and multidimensional data. Unlike traditional balanced trees like GiST, SP-GiST supports space-partitioning trees such as quad-trees and kd-trees, which are particularly useful for spatial data where the data space can be partitioned into non-overlapping regions.
- **GIN**
  - Generalized Inverted Index (GIN) is a powerful indexing method in PostgreSQL that can be used for complex data types such as arrays, text search, and more. GIN provides better search capabilities for non-traditional data types, while also offering efficient and flexible querying.
- **BRIN**
  - BRIN is an abbreviation for Block Range INdex which is an indexing technique introduced in PostgreSQL 9.5. This indexing strategy is best suited for large tables containing sorted data.

### 3.5 Get Involved in Development
- **Mailing Lists**
  - Mailing lists are an essential part of PostgreSQL's development community. They provide a platform for collaboration, discussion, and problem-solving.
- **Reviewing Patches**
  - Reviewing patches is a vital contribution to PostgreSQL, ensuring quality control, maintaining project standards, and helping new contributors understand the system's internals. By identifying bugs, improving performance, and ensuring proper documentation and test coverage, reviewers uphold PostgreSQL's reliability and stability.
- **Writing Patches**
  - If you are an experienced developer or willing to learn, you can contribute to PostgreSQL by writing patches. Patches are important to fix bugs, optimize performance, and implement new features.

---

## 4. Optional / Specialized Topics

- Queries
- Data Types
- Columns
- Schemas
- Query Processing
- Constraints
- Filtering Data
- Modifying Data
- Joining Tables
- Import / Export Using `COPY`
- Transactions
- CTE
- Lateral Join
- Subqueries
- Grouping
- Set Operations
- Resource Usage
- Reporting Logging & Statistics
- Adding Extra Extensions
- Default Privileges
- Checkpoints / Background Writer
- Object Privileges
- Grant / Revoke
- Advanced Topics
- Row-Level Security

---

## 5. References

- [PostgreSQL DBA Roadmap](https://roadmap.sh/postgresql-dba)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer
- Fullstack Developer

### Related Skills
- SQL
- MongoDB