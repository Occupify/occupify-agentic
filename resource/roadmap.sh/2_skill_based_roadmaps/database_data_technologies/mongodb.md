# MongoDB

## Metadata
- Type: Skill
- Domain: Database & Data Systems
- Source: roadmap.sh
- Source URL: https://roadmap.sh/mongodb
- Related Roles:
  - PostgreSQL DBA
  - Backend Developer

---

## 1. Beginner

### 1.1 MongoDB Basics
- **SQL vs NoSQL**
  - NoSQL and SQL are two distinct paradigms for managing and storing data in databases. SQL (Structured Query Language) databases are relational and use a structured schema to define data types and relationships, making them ideal for complex queries and transactions.
- **What is MongoDB?**
  - MongoDB is a NoSQL, document-oriented database designed for scalability, flexibility, and high performance. It stores data in JSON-like BSON (Binary JSON) format, allowing for the representation of complex data structures and enabling developers to work with unstructured or semi-structured data easily.
- **When to use MongoDB?**
  - MongoDB is ideal for applications that require flexible schema design, rapid development cycles, and need to handle large volumes of unstructured or semi-structured data. It's particularly well-suited for content management systems, real-time analytics, IoT applications, mobile app backends, and scenarios where you need to scale horizontally across multiple servers, making it an excellent choice when your data model is likely to evolve frequently or when you're dealing with complex nested data structures that don't fit well into traditional relational database tables.
- **What is MongoDB Atlas?**
  - MongoDB Atlas is a fully-managed cloud database service offered by MongoDB that simplifies database management for developers by automating tasks such as provisioning, scaling, and backups. It supports multi-cloud deployments across major providers like AWS, Google Cloud, and Azure, allowing for flexibility and resilience.
- **MongoDB Terminology**
  - MongoDB terminology includes key concepts: databases contain collections (equivalent to tables), which store documents (equivalent to rows) composed of field-value pairs. Other terms include indexes for performance optimization, replica sets for high availability, shards for horizontal scaling, aggregation pipelines for data processing, and ObjectIds for unique document identifiers.
- **BSON vs JSON**
  - BSON (Binary JSON) is MongoDB's binary-encoded serialization format that extends JSON with additional data types like dates, binary data, and 64-bit integers. While JSON is human-readable text format, BSON provides faster parsing, compact storage, and native support for MongoDB's rich data types.
- **Embedded Objects & Arrays**
  - Embedded objects and arrays in MongoDB enable storing related data within a single document, eliminating the need for separate collections and joins. This design pattern improves query performance and maintains data locality.
- **Double**
  - Double data type in MongoDB stores 64-bit floating-point numbers following IEEE 754 standard, providing high precision for decimal calculations. It's the default numeric type for JavaScript numbers and handles both integers and decimals.
- **String**
  - String data type in MongoDB stores UTF-8 encoded text data with no length restrictions within document size limits. Strings support text indexing for search capabilities, regex pattern matching, and various string manipulation operations in aggregation pipelines.
- **Array**
  - Array data type in MongoDB stores ordered lists of values including mixed data types, nested arrays, and embedded documents. Arrays support indexing with multikey indexes, enabling efficient queries on array elements.
- **Object**
  - Object data type is used to store embedded documents, allowing for complex data structures within a single document. This type is essential for organizing related data hierarchically, enabling efficient querying and data manipulation.

### 1.2 Data Model & Data Types
- **Binary Data**
  - Binary data in MongoDB stores non-textual data like images, files, and encoded content using the BSON Binary data type. It supports various subtypes including generic binary, function code, UUID, and MD5 hashes.
- **Undefined**
  - The Undefined type is a BSON data type that represents a value that is not defined. It is primarily used to indicate that a field does not have a value or that a variable has not been assigned a value.
- **Object ID**
  - ObjectId is MongoDB's default primary key type, consisting of a 12-byte identifier that includes timestamp, machine identifier, process ID, and counter components. It ensures uniqueness across distributed systems and provides automatic indexing.
- **Boolean**
  - Boolean data type in MongoDB stores true or false values, representing logical states in documents. Booleans are commonly used for flags, status indicators, and conditional logic in queries and applications.
- **Date**
  - Date data type in MongoDB stores timestamps as 64-bit integers representing milliseconds since Unix epoch (January 1, 1970 UTC). Dates support range queries, sorting, and date arithmetic operations in aggregation pipelines.
- **Null**
  - Null data type in MongoDB represents absent or undefined values, distinct from empty strings or zero values. Null fields can be queried, indexed, and participate in aggregation operations with special handling.

### 1.3 Collections & Methods
- **Regular Expression**
  - Regular expressions in MongoDB are patterns used to match strings within documents in a collection. They are implemented using the Perl Compatible Regular Expressions (PCRE) syntax, allowing for complex string matching capabilities.
- **JavaScript**
  - The JavaScript data type in MongoDB allows you to store JavaScript code as BSON values within documents, enabling the execution of server-side JavaScript functions for operations like map-reduce, stored procedures, and complex data transformations. This type can store JavaScript functions or code snippets that can be executed within the MongoDB server environment, making it useful for scenarios where you need to perform complex calculations, business logic, or custom aggregation operations directly on the database server.
- **Symbol**
  - The symbol is often used in the context of BSON (Binary JSON) data types, which allows for the representation of various data structures. While MongoDB does not have a specific "symbol" data type like some programming languages, it utilizes BSON to store data efficiently, enabling developers to work with complex data types and structures seamlessly.
- **Int32/Int**
  - Int32 data type in MongoDB stores 32-bit signed integers ranging from -2,147,483,648 to 2,147,483,647. This type provides exact integer representation without floating-point precision issues and takes less storage space than doubles.
- **Int64 / Long**
  - Int64 (Long) data type in MongoDB stores 64-bit signed integers with a range from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. This type handles large integer values that exceed Int32 limits while maintaining exact precision.
- **Timestamp**
  - The Timestamp type in MongoDB is a special BSON data type used internally for operations like replication and sharding. It consists of a 32-bit second counter and an incrementing ordinal counter (also 32 bits), representing UTC time accurate to the second.
- **Decimal128**
  - Decimal128 data type in MongoDB provides exact decimal representation for financial and monetary calculations requiring precision. Based on IEEE 754-2008 standard, it supports 34 decimal digits with exact arithmetic operations.
- **Min Key**
  - MinKey is a special value in MongoDB that represents the lowest possible value for a field. It is considered to be less than all other values in the database.
- **Max Key**
  - MaxKey is the counterpart to MinKey in MongoDB, representing the highest possible value for a field. It is considered to be greater than all other values in the database.
- **Counting Documents**
  - Counting documents in MongoDB uses methods like countDocuments() for accurate filtered counts and estimatedDocumentCount() for fast approximate totals. countDocuments() supports query filters and provides precise results but may be slower on large collections.
- **insert() and relevant**
  - Insert operations add new documents to MongoDB collections using insertOne() for single documents and insertMany() for multiple documents. These methods support options like ordered/unordered inserts, write concerns, and automatic ObjectId generation.
- **find() and relevant**
  - The find() method retrieves documents from MongoDB collections using query filters, projections, and modifiers. Related methods include findOne() for single documents, findOneAndUpdate() for atomic updates, findOneAndDelete() for atomic deletions, and cursor methods like limit(), skip(), sort() for result manipulation.
- **update() and relevant**
  - Update operations modify existing documents using updateOne(), updateMany(), and replaceOne() methods with update operators like $set, $unset, $inc, and $push. These methods support upsert operations, array modifications, field updates, and atomic operations.
- **delete() and relevant**
  - Delete operations remove documents from MongoDB collections using deleteOne() for single document removal and deleteMany() for multiple documents. These methods use query filters to specify which documents to delete and support write concerns for reliability.
- **bulkWrite() and relevant**
  - bulkWrite() in MongoDB performs multiple write operations in a single command, improving performance through reduced network round trips. It supports mixed operations including inserts, updates, deletes, and replaces with options for ordered or unordered execution.
- **validate()**
  - The validate() method in MongoDB is a database administration command that checks the integrity and consistency of a collection's data structures, indexes, and storage format, providing detailed information about potential corruption, missing records, or structural issues. This method performs comprehensive validation by examining the collection's namespace, scanning all documents and indexes for consistency, checking BSON document structure validity, and verifying that index entries correctly correspond to their associated documents.

---

## 2. Intermediate

### 2.1 Query Operators
- **$project**
  - The $project stage in MongoDB aggregation pipelines is used to reshape documents by including, excluding, or transforming fields, allowing you to control exactly which data is passed to subsequent pipeline stages. It can perform field selection (similar to SQL SELECT), create computed fields using expressions, rename fields, nest or flatten document structures, and apply various transformations like mathematical operations, string manipulations, or date formatting.
- **$include**
  - The $include projection operator in MongoDB allows you to explicitly specify which fields should be included in query results, providing precise control over the data returned from the database. When using $include (or simply setting fields to 1 or true in a projection document), only the specified fields and the \id field (unless explicitly excluded) will be present in the returned documents, which helps reduce network traffic, improve query performance, and enhance security by limiting data exposure.
- **$exclude**
  - The $exclude projection operator in MongoDB is used to explicitly exclude specific fields from query results, allowing you to return all fields of a document except those that are explicitly excluded. When using $exclude, you specify which fields to omit by setting them to 0 or false in the projection document, and all other fields will be automatically included in the result set.
- **$slice**
  - The $slice projection operator in MongoDB returns a subset of array elements from documents. It supports positive values for elements from the beginning, negative values from the end, and skip/limit combinations for pagination within arrays.
- **$eq**
  - The $eqoperator in MongoDB matches documents where a field value equals a specified value. It performs exact equality comparison and is the default behavior when using field: value syntax.
- **$gt**
  - The $gt (greater than) operator in MongoDB selects documents where a field value is greater than a specified value. It works with numbers, dates, strings (lexicographically), and other comparable BSON types.
- **$lt**
  - The $lt (less than) operator in MongoDB selects documents where a field value is less than a specified value. It supports comparison operations on numbers, dates, strings, and other ordered BSON types.
- **$gte**
  - The $gte (greater than or equal to) operator in MongoDB selects documents where a field value is greater than or equal to a specified value. It provides inclusive comparison for range queries, date boundaries, and numeric filtering.
- **$ne**
  - The $ne (not equal) operator in MongoDB selects documents where a field value is not equal to a specified value. It performs inverse equality comparison and excludes documents with matching values, including exact matches and type equivalence.
- **$in**
  - The $in operator in MongoDB selects documents where a field value matches any value in a specified array. It provides efficient multiple value matching without using multiple $or conditions.
- **$nin**
  - The $nin (not in) operator in MongoDB selects documents where a field value does not match any value in a specified array. It's the logical opposite of $in and excludes documents with field values present in the given array.
- **$all**
  - The $all operator in MongoDB selects documents where an array field contains all specified elements, regardless of order or additional elements. It's useful for tag-based filtering and ensuring multiple required values exist in arrays.
- **$elemMatch**
  - The $elemMatch operator in MongoDB matches documents containing array elements that satisfy multiple specified criteria within a single array element. It ensures all conditions apply to the same array element rather than different elements.
- **$size**
  - The $size operator in MongoDB matches documents where an array field has exactly the specified number of elements. It only works with arrays and requires an exact count match, not range queries.

### 2.2 Creating Indexes
- **Read / Write Concerns**
  - Read and write concerns in MongoDB control data consistency and acknowledgment levels for operations. Write concerns specify acknowledgment requirements from replica set members, while read concerns determine data consistency guarantees for queries.
- **Cursors**
  - Cursors in MongoDB are pointers to query result sets that enable efficient iteration through large datasets without loading all documents into memory. They support methods like hasNext(), next(), forEach(), and limit() for result manipulation.
- **Retryable Reads / Writes**
  - Retryable reads and writes in MongoDB are client-side features that automatically retry certain database operations when they encounter transient network errors or temporary server unavailability, improving application resilience and user experience. The MongoDB drivers can automatically retry read operations and specific write operations (like inserts, updates, deletes, and findAndModify) exactly once when they fail due to network issues, replica set elections, or other recoverable errors, without requiring changes to application code.
- **Single Field**
  - Single field indexes in MongoDB are created on individual document fields to optimize queries filtering, sorting, or ranging on that specific field. They can be ascending (1) or descending (-1) and automatically optimize equality, range, and sort operations.
- **Compound**
  - Compound indexes in MongoDB are built on multiple fields in a specified order, optimizing queries that filter on multiple fields. Field order matters significantly as it determines which queries can efficiently use the index.
- **Text**
  - The $text operator in MongoDB performs full-text search on fields with text indexes. It supports phrase matching, stemming, stop words, and relevance scoring.
- **Expiring**
  - TTL (Time-To-Live) indexes are a special type of index that automatically remove documents from a collection after a certain amount of time has passed or at a specific clock time. By defining a TTL index on a field containing date values, the database background process continuously monitors the collection and deletes documents once the specified duration has elapsed.

### 2.3 Performance Optimization
- **Geospatial Indexes**
  - Geospatial indexes in MongoDB enable efficient querying of geographic coordinate data using 2d, 2dsphere, and geoHaystack index types. They support location-based queries like finding points within a specific distance, polygon intersection, and nearest neighbor searches.
- **Atlas Search Indexes**
  - Atlas Search indexes in MongoDB Atlas provide full-text search capabilities using Apache Lucene technology. They enable sophisticated text search with relevance scoring, autocomplete, faceted search, and synonyms.
- **Query Optimization**
  - Query optimization in MongoDB involves analyzing and improving query performance through various techniques including proper indexing strategies, query plan analysis, and efficient query structure design. It encompasses understanding how MongoDB's query planner works, using tools like explain() to analyze query execution, creating appropriate indexes to support common query patterns, avoiding inefficient operations like full collection scans, and structuring queries to take advantage of MongoDB's document model and aggregation framework for optimal performance and resource utilization.
- **Language Drivers**
  - MongoDB language drivers are official and community-maintained libraries that provide idiomatic APIs for interacting with MongoDB databases from various programming languages including Python (PyMongo), JavaScript/Node.js, Java, C#, Go, PHP, Ruby, and many others. These drivers handle the low-level communication protocols, connection management, authentication, and data serialization between applications and MongoDB servers, while providing language-specific features like object mapping, connection pooling, and async/await support.

### 2.4 Aggregation
- **$lte**
  - The $lte (less than or equal to) operator in MongoDB selects documents where a field value is less than or equal to a specified value. It provides inclusive upper bound comparison for range queries, end date filtering, and maximum value constraints.
- **$exists**
  - The $exists operator in MongoDB matches documents based on the presence or absence of a specified field. When set to true, it finds documents containing the field regardless of value (including null), and when false, it finds documents missing the field entirely.
- **$type**
  - The $type operator in MongoDB selects documents based on the BSON data type of a specified field. It accepts either BSON type numbers or string aliases like "string", "int", "array", "object".
- **$regex**
  - The $regex operator in MongoDB provides regular expression pattern matching for string fields. It supports Perl-compatible regular expressions (PCRE) with options for case sensitivity, multiline matching, and extended syntax.
- **$and**
  - The $and operator in MongoDB performs logical AND operation on multiple query expressions, returning documents that satisfy all specified conditions. It accepts an array of query expressions and is implicitly used when multiple conditions are provided at the same level.
- **$or**
  - The $or operator in MongoDB performs logical OR operation on multiple query expressions, returning documents that satisfy at least one of the specified conditions. It accepts an array of query expressions and enables alternative matching criteria.
- **$not**
  - The $not operator in MongoDB performs logical negation on a query expression, returning documents that do not match the specified condition. It accepts a single query expression and inverts its result.
- **$nor**
  - The $nor operator in MongoDB performs logical NOR operation, selecting documents that fail to match any of the specified query expressions. It's the inverse of $or and returns documents that don't satisfy any of the given conditions.
- **Pipelines, Stages and Operators**
  - MongoDB aggregation pipelines are composed of sequential stages that process and transform documents, where each stage performs a specific operation using various operators before passing results to the next stage. Stages like $match (filtering), $group (grouping and aggregating), $project (field selection and transformation), $sort (ordering), $lookup (joins), and $unwind (array expansion) can be combined in any order to create complex data processing workflows.

---

## 3. Advanced

### 3.1 Transactions
- **$match**
  - The $match aggregation stage filters documents in the pipeline, similar to the find() query operation. It should be placed early in the pipeline to reduce document count and improve performance.
- **$group**
  - The $group aggregation stage groups documents by specified identifier expressions and applies accumulator operators like $sum, $avg, $max, $min, and $push. It's essential for data aggregation, calculating statistics, and creating summary reports.
- **$sort**
  - The $sort aggregation stage orders documents by specified field values in ascending (1) or descending (-1) order. It can sort by multiple fields with different directions and supports sorting by computed values from previous pipeline stages.
- **$project**
  - The $project stage in MongoDB aggregation pipelines is used to reshape documents by including, excluding, or transforming fields, allowing you to control exactly which data is passed to subsequent pipeline stages. It can perform field selection (similar to SQL SELECT), create computed fields using expressions, rename fields, nest or flatten document structures, and apply various transformations like mathematical operations, string manipulations, or date formatting.
- **$skip**
  - The $skip aggregation stage skips a specified number of documents before passing the remaining documents to the next pipeline stage. It's commonly used with $limit for pagination implementation, allowing applications to skip previous pages and retrieve specific result sets.
- **$limit**
  - The $limit aggregation stage restricts the number of documents passed to the next stage in the pipeline. It's commonly used with $sort to get top N results, implement pagination, or reduce data processing overhead.

### 3.2 Developer Tools
- **$unwind**
  - The $unwind aggregation stage deconstructs array fields, creating separate documents for each array element. It's essential for processing documents with embedded arrays by flattening them into individual records.
- **$lookup**
  - The $lookup aggregation stage performs left outer joins between collections, similar to SQL JOINs. It adds an array field containing matching documents from the "joined" collection based on specified local and foreign fields.
- **$sum**
  - The $sum aggregation operator calculates the total sum of numeric values across grouped documents or array elements. It's commonly used with $group to aggregate numeric data, create totals, and perform mathematical operations in aggregation pipelines.
- **Kafka**
  - Apache Kafka is a distributed event streaming platform designed for high-throughput, fault-tolerant, and scalable data streaming. It is primarily used for building real-time data pipelines and streaming applications.
- **Spark**
  - Spark refers to the integration of Apache Spark, a powerful data processing engine, with MongoDB, a NoSQL database. This integration allows users to perform real-time analytics and data processing on MongoDB data using Spark's capabilities, enabling efficient data manipulation and analysis without the need for extensive ETL processes.
- **Elastic Search**
  - The MongoDB Elasticsearch connector enables seamless integration between MongoDB and Elasticsearch, allowing you to automatically synchronize data from MongoDB collections to Elasticsearch indices for powerful full-text search, analytics, and visualization capabilities. This connector streams data changes in real-time using MongoDB's change streams, transforms documents as needed, and maintains data consistency between the two systems, making it ideal for applications that need both MongoDB's flexible document storage and Elasticsearch's advanced search and aggregation features.

### 3.3 Scaling MongoDB
- **mongodump**
  - mongodump is a MongoDB utility that creates binary backups of database content by exporting data in BSON format. It supports selective backup options including specific databases, collections, and query-based filtering.
- **mongorestore**
  - mongorestore is a MongoDB utility that restores data from binary BSON dumps created by mongodump. It can restore entire databases, specific collections, or subsets of data with options for data transformation and index rebuilding.
- **Replicasets**
  - Replica Sets in MongoDB provide high availability and data redundancy through a group of mongod instances that maintain identical data copies. The primary node handles write operations while secondary nodes replicate data and can serve read operations.
- **Sharded Clusters**
  - Sharded Clusters enable horizontal scaling by distributing data across multiple servers based on a shard key. MongoDB automatically partitions collections and balances data distribution across shards, allowing databases to handle massive datasets and high throughput workloads.
- **Tuning Configuration**
  - MongoDB tuning configuration involves optimizing various server parameters and settings to maximize performance, efficiency, and resource utilization based on your specific workload patterns and hardware environment. Key configuration areas include memory management (WiredTiger cache size, storage engine settings), connection pooling (maximum connections, timeout values), journaling options, read/write concerns, chunk size for sharded clusters, and operating system-level optimizations like file descriptor limits and memory allocation.
- **Indexing**
  - Indexing in MongoDB creates data structures that improve query performance by creating shortcuts to documents. Indexes are built on specific fields and allow the database to quickly locate data without scanning entire collections.
- **Query Optimization**
  - Query optimization in MongoDB involves analyzing and improving query performance through various techniques including proper indexing strategies, query plan analysis, and efficient query structure design. It encompasses understanding how MongoDB's query planner works, using tools like explain() to analyze query execution, creating appropriate indexes to support common query patterns, avoiding inefficient operations like full collection scans, and structuring queries to take advantage of MongoDB's document model and aggregation framework for optimal performance and resource utilization.

### 3.4 MongoDB Security
- **Role-based Access Control**
  - Role-Based Access Control (RBAC) in MongoDB is a security framework that manages user permissions by assigning roles that define specific privileges and access levels to database resources. It allows administrators to create custom roles with granular permissions for actions like read, write, or administrative operations on specific databases, collections, or even individual fields, ensuring users only have access to the resources they need for their job functions.
- **X.509 Certificate Auth**
  - x.509 certificate authentication in MongoDB provides secure, certificate-based client and cluster authentication without passwords. It uses public key infrastructure (PKI) for strong identity verification and supports both client authentication and internal cluster member authentication.
- **Kerberos Authentication**
  - Kerberos authentication in MongoDB provides enterprise-grade security through ticket-based authentication protocol. It integrates with existing Active Directory or Kerberos infrastructures, allowing centralized user management and single sign-on capabilities.
- **LDAP Proxy Auth**
  - LDAP Proxy Authentication in MongoDB allows the database to authenticate users through an external LDAP (Lightweight Directory Access Protocol) server, enabling organizations to integrate MongoDB with their existing directory services like Active Directory. This authentication method acts as a proxy between MongoDB and the LDAP server, allowing users to authenticate using their corporate credentials while maintaining centralized user management, making it particularly valuable for enterprise environments that need to enforce consistent security policies and user access controls across multiple systems.
- **MongoDB Audit**
  - MongoDB Audit is a security feature that enables comprehensive logging and monitoring of database activities, including authentication attempts, authorization failures, CRUD operations, and administrative actions. It provides detailed audit trails that track who accessed what data, when operations occurred, and whether they succeeded or failed, which is essential for compliance with regulatory requirements like GDPR, HIPAA, or SOX, and helps organizations detect suspicious activities, investigate security incidents, and maintain accountability in their database operations.
- **Encryption at Rest**
  - Encryption at Rest in MongoDB protects data stored on disk by encrypting database files, indexes, and logs using industry-standard encryption algorithms. This security feature prevents unauthorized access to physical storage media and ensures compliance with data protection regulations.
- **Queryable Encryption**
  - Queryable Encryption is a feature that allows you to perform expressive queries on data while it remains encrypted on the database server. It ensures that sensitive information is stored in an encrypted state at all times, even while in use by the application, by using client-side encryption keys that are never shared with the database.
- **Client-Side Field Level**
  - Client-Side Field Level Encryption (CSFLE) allows applications to encrypt sensitive data fields before storing them in MongoDB. The database receives only encrypted data and remains unaware of the encryption keys, ensuring zero-trust security.
- **TLS / SSL Encryption**
  - TLS (Transport Layer Security) and its predecessor, SSL (Secure Sockets Layer), are cryptographic protocols that establish an encrypted link between a client and a server. By using these protocols, data transmitted over a network is protected from eavesdropping, tampering, and forgery.

---

## 4. Optional / Specialized Topics

- MongoDB Terminology
- BSON vs JSON
- Embedded Objects & Arrays
- Double
- String
- Array
- Object
- Date
- Null
- Int64 / Long
- Timestamp
- Decimal128
- Min Key
- Max Key
- Counting Documents
- insert() and relevant
- find() and relevant
- update() and relevant
- delete() and relevant
- bulkWrite() and relevant
- validate()
- $eq
- $gt
- $lt
- $gte

---

## 5. References

- [MongoDB Roadmap](https://roadmap.sh/mongodb)

---

## 6. Related Roles / Topics

### Related Roles
- PostgreSQL DBA
- Backend Developer

### Related Skills
- Node.js
- Redis