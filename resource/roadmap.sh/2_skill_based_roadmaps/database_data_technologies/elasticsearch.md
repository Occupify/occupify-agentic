# Elasticsearch

## Metadata
- Type: Skill
- Domain: Database & Data Systems
- Source: roadmap.sh
- Source URL: https://roadmap.sh/elasticsearch
- Related Roles:
  - Backend Developer
  - Fullstack Developer
  - Software Architect

---

## 1. Beginner

### 1.1 Introduction
- **JSON**
  - JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It's based on a subset of the JavaScript programming language, and uses a text-based format to represent data objects consisting of attribute-value pairs and array data types.
- **REST API Basics**
  - REST API (Representational State Transfer Application Programming Interface) is an architectural style for building networked applications. It relies on a stateless, client-server communication protocol, typically HTTP, to perform operations on resources.
- **Search Engines vs Relational DBs**
  - Search engines are designed for quickly finding relevant information within large volumes of unstructured or semi-structured text, prioritizing speed and relevance scoring. Relational databases, on the other hand, are structured systems optimized for managing and querying structured data with strong consistency and transactional integrity, using predefined schemas and relationships between tables.
- **The ELK Stack**
  - The ELK Stack is a collection of three open-source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics engine.
- **Elasticsearch Usecases**
  - Elastic use cases can be classified into three main categories:
- **Running with Docker**
  - Docker provides a convenient and isolated environment to run applications, including Elasticsearch. Using Docker, you can quickly set up an Elasticsearch instance without worrying about operating system compatibility or dependency conflicts.
- **Kibana Console**
  - Kibana is a web interface that allows you to explore, visualize, and manage data indexed in Elasticsearch. It provides tools for searching, analyzing, and visualizing your data in real-time.
- **Cluster (System)**
  - A cluster is a collection of one or more Elasticsearch nodes that work together to store and process data. It provides a distributed and scalable system where data is divided into shards and distributed across multiple nodes for redundancy and performance.
- **Node (Instance)**
  - A node is a single server within an Elasticsearch cluster that stores data and participates in the cluster's indexing and search capabilities. Each node is configured with a name and can be assigned specific roles, such as master, data, or ingest, to optimize resource allocation and cluster performance.
- **Index (Database)**
  - An index is a collection of documents that have similar characteristics. Think of it as a database in a relational database system.

### 1.2 Mappings
- **Elastic Cloud**
  - Elastic Cloud is a suite of Elasticsearch-based services offered by Elastic, the company behind Elasticsearch. It provides a managed platform for deploying, managing, and scaling Elasticsearch clusters in the cloud, eliminating the need for users to handle the underlying infrastructure.
- **Document (Row)**
  - A document is a basic unit of information in Elasticsearch, analogous to a row in a relational database table. It's a JSON object containing a set of fields, each with a name and one or more values.
- **ID (Primary Key)**
  - An ID, or Primary Key, is a unique identifier for each document stored within an Elasticsearch index. It distinguishes one document from another, allowing for specific retrieval, updating, and deletion of individual data entries.
- **Master-Elegible Nodes**
  - Master-eligible nodes in Elasticsearch are the nodes that can be elected as the master node. The master node is responsible for cluster-wide management tasks, such as creating or deleting indices, tracking which nodes are part of the cluster, and deciding how to allocate shards across the cluster.
- **Data Nodes**
  - Data nodes in Elasticsearch are the workhorses of the cluster, responsible for storing data and performing CPU and I/O intensive operations like searching, indexing, and data analysis. These nodes hold shards of Elasticsearch indices and manage the actual data storage on disk.
- **Coordinating Nodes**
  - Coordinating nodes in Elasticsearch are like traffic controllers. They receive client requests, route them to the appropriate data nodes that hold the relevant data shards, and then consolidate the results before sending them back to the client.
- **Explicit**
  - Explicit mappings in Elasticsearch involve defining the structure and data types of fields within an index before indexing any documents. This allows you to have precise control over how Elasticsearch analyzes and stores your data, ensuring that fields are treated as intended (e.g., a field containing dates is treated as a date, not just text).
- **Dynamic**
  - Dynamic mapping in Elasticsearch allows the index to automatically detect and add new fields to the mapping when new documents containing previously unseen fields are indexed. This means you don't have to predefine the schema for every field in your data; Elasticsearch infers the data type and adds the field to the index mapping on the fly.
- **Mapping Explosion**
  - Mapping explosion in Elasticsearch refers to the uncontrolled growth of fields within an index's mapping. This typically happens when Elasticsearch automatically creates mappings for new fields as it encounters them in incoming documents.

---

## 2. Intermediate

### 2.1 Data Types
- **Primary Shards**
  - Primary shards are the fundamental units of data storage in Elasticsearch. An index is logically divided into one or more primary shards, each of which contains a portion of the index's data.
- **Replica Shards**
  - Replica shards are copies of primary shards within an Elasticsearch index. They provide redundancy, ensuring data availability even if a primary shard fails.
- **The "Split Brain" Problem**
  - The "split brain" problem occurs in distributed systems when a cluster of nodes becomes partitioned into two or more independent sub-clusters that are unable to communicate with each other. Each sub-cluster may then believe it is the primary cluster and start making independent decisions, potentially leading to data inconsistencies and conflicts as each sub-cluster operates as if it's the only authority.
- **Numeric**
  - Numeric data types in Elasticsearch are used to store numerical values, such as integers and floating-point numbers. These types allow you to efficiently store and query numerical data, enabling operations like range queries, aggregations, and sorting based on numerical values.
- **Boolean**
  - A boolean data type represents a logical value, which can be either true or false. It's used to store binary information, indicating whether a condition is met or not, or representing a simple yes/no state.
- **Text**
  - The text data type in Elasticsearch is designed for storing and indexing full-text content, such as blog posts, articles, or product descriptions. When you index a field as text, Elasticsearch analyzes the text using an analyzer.
- **Keyword**
  - The Keyword data type in Elasticsearch is used for indexing fields that contain structured, string-based data. Unlike the Text data type, Keyword fields are not analyzed or tokenized; the entire string is indexed as a single term.
- **Dates**
  - Dates in Elasticsearch represent points in time. They are stored internally as the number of milliseconds since the Unix epoch (January 1, 1970, 00:00:00 UTC).
- **Geo Points**
  - Geo points are a specific data type in Elasticsearch used to store and index latitude and longitude coordinates. They allow you to represent locations on Earth and perform geospatial queries, such as finding points within a certain distance of a location or identifying points within a defined area.
- **Object**
  - An object is a data type that allows you to store nested JSON documents within a single document. This means you can represent complex, hierarchical data structures where a field can contain other fields and their corresponding values, similar to how objects are structured in programming languages.
- **Nested**
  - The nested data type is used to represent arrays of objects within a document. Each object in the array can be indexed as a separate document, allowing you to query and filter based on the properties of individual objects within the array, without affecting other objects in the same array.
- **Flattened**
  - The flattened data type in Elasticsearch allows you to index an entire JSON object as a single field. This is useful when you have objects with many fields, but you only need to search or aggregate on a small subset of them.
- **Create Index**
  - Creating an index in Elasticsearch using the Document API involves sending a PUT request to the Elasticsearch server. This request specifies the name of the index you want to create.
- **Delete Index**
  - Deleting an index in Elasticsearch removes the entire index and all its associated data. You can achieve this using the Delete Index API.
- **ES|QL**
  - ES|QL is a query language designed for Elasticsearch that allows users to search, transform, and analyze data using a SQL-like syntax. It provides a more familiar and accessible way to interact with Elasticsearch data compared to the traditional JSON-based query DSL, enabling users to perform complex data manipulations and aggregations with relative ease.

### 2.2 Leaf vs Compound Queries
- **Index Document**
  - To add data to Elasticsearch, you use the Index API. This API lets you create a new document within a specific index.
- **Get Document**
  - To retrieve a specific document from an Elasticsearch index, you need to know its unique identifier. You can then use the Get API, providing the index name and the document ID.
- **Update Document**
  - Updating a document in Elasticsearch involves modifying an existing document's data. You can achieve this using the Update API, which allows you to change specific fields or the entire document.
- **Delete Documents**
  - Deleting a document in Elasticsearch involves sending a DELETE request to a specific index and document ID. This action permanently removes the document from the index.
- **Bulk index**
  - Bulk indexing in Elasticsearch is a way to send multiple indexing, updating, or deleting operations to the Elasticsearch cluster in a single request. Instead of sending each document individually, you batch them together, which significantly reduces the overhead of network communication and processing, leading to faster indexing speeds.
- **Optimizing Bulk Indexing**
  - Bulk indexing in Elasticsearch is the process of sending multiple indexing, updating, or deleting operations in a single request. Optimizing this process involves tuning various parameters and strategies to maximize throughput and minimize resource consumption, ensuring data is efficiently loaded into Elasticsearch.
- **Reindex API**
  - The Reindex API in Elasticsearch allows you to copy documents from one index to another. This is useful for a variety of tasks, including changing the mapping of an index, upgrading to a new Elasticsearch version, or splitting a large index into smaller ones.
- **Update by Query**
  - Update by Query is a way to update documents that match a specific query. Instead of retrieving each document individually, modifying it, and then re-indexing it, Update by Query allows you to perform updates on multiple documents in a single operation based on a search query.
- **EQL**
  - Event Query Language (EQL) is a powerful query language designed for security event analysis and threat hunting. It allows users to search for sequences of events that match specific patterns, enabling the detection of complex attack behaviors.
- **SQL**
  - Elasticsearch SQL allows you to query Elasticsearch data using the familiar SQL syntax. Instead of using Elasticsearch's native query DSL (Domain Specific Language), you can write SQL statements to retrieve, filter, and aggregate data stored in Elasticsearch indices.
- **Query DSL**
  - Query DSL (Domain Specific Language) is a JSON-based language used to define and execute search queries in Elasticsearch. It provides a structured way to express complex search criteria, including boolean logic, term matching, range queries, and more, allowing users to precisely specify what data they want to retrieve.
- **KQL**
  - Kibana Query Language (KQL) is a query language used within Kibana to search and filter data in Elasticsearch. It allows users to construct queries using a human-readable syntax, making it easier to find specific information within their Elasticsearch indices without needing to write complex JSON-based Elasticsearch queries.
- **Lucene**
  - Lucene is a powerful text search engine library. Its query syntax provides a way to specify search criteria using terms, phrases, wildcards, and boolean operators.
- **Query**
  - A query is a request for information from a data source. It specifies the criteria for retrieving specific data that matches the defined conditions.
- **Filter**
  - A filter in Elasticsearch is a query that returns documents matching specific criteria in a boolean (yes/no) manner. Unlike regular queries that calculate a relevance score, filters simply determine whether a document matches the condition or not.
- **Match Query**
  - The Match Query is a fundamental full-text search query in Elasticsearch. It allows you to search for documents that contain specific terms within a field.
- **Exists Query**
  - An exists query in Elasticsearch is used to find documents that contain a specific field, regardless of its value. It checks for the presence of the field in the document's source data.
- **Term Query**
  - A term query is a simple search that looks for documents containing an exact, unanalyzed term in a specific field. It's like searching for a specific word or value without any stemming, synonyms, or other text processing applied.
- **ID Query**
  - An ID query retrieves documents from an index based on their unique identifier. It's a simple and efficient way to fetch specific documents when you already know their IDs.
- **Range Query**
  - A range query allows you to find documents where the value of a specific field falls within a specified range. This range can be defined using upper and lower bounds, which can be inclusive or exclusive.
- **Prefix Query**
  - A prefix query finds documents that contain terms starting with a specific prefix. It operates at the term level, meaning it searches for the prefix directly within the indexed terms of a field.

### 2.3 Controlling Search Results
- **Delete by Query**
  - Delete by Query allows you to remove documents from an Elasticsearch index that match a specific query. Instead of deleting documents individually by their ID, you can define criteria based on field values or other search parameters.
- **must_not**
  - mustnot is a clause within a bool query that filters out documents matching the specified query. It defines conditions that documents should not satisfy to be included in the search results.
- **must**
  - A "must" query in Elasticsearch is a type of compound query that specifies conditions that documents must satisfy to be included in the search results. It contributes to the relevance score of each matching document.
- **filter**
  - The filter context within a Bool query in Elasticsearch is used to narrow down the documents that match a query without affecting the relevance score. It's like a pre-filter that efficiently excludes documents that don't meet specific criteria before the scoring process even begins, making it ideal for exact matches, range queries, and other conditions where relevance isn't a factor.
- **should**
  - The should query is a boolean query that returns documents matching one or more of its sub-queries. It increases the relevance score for each matching clause, but doesn't require any clauses to match for a document to be included in the results.
- **Wildcard Query**
  - A wildcard query lets you search for terms that match a specified pattern. This pattern can include special characters like (representing zero or more characters) and ?
- **Pagination**
  - Pagination divides search results into discrete pages, allowing users to navigate through large datasets in manageable chunks. Instead of displaying all results at once, which can be overwhelming and resource-intensive, pagination presents a subset of results per page, improving user experience and reducing server load.
- **Source Filtering**
  - Source filtering in Elasticsearch allows you to control which fields are returned in the source field of your search results. Instead of retrieving the entire document, you can specify which fields you need, reducing network traffic and improving performance.
- **Sorting**
  - Sorting in Elasticsearch lets you order the search results based on the values of specific fields. By default, Elasticsearch sorts results by relevance score, but you can change this to sort by other criteria like date, price, or any other field in your documents.
- **Highlighting**
  - Highlighting in Elasticsearch helps users quickly identify the search terms within the returned documents. It works by surrounding the search keywords in the results with special tags, like <em> and </em>, making them visually distinct.

---

## 3. Advanced

### 3.1 How Search Works
- **The Inverted Index**
  - The inverted index is a data structure that stores a mapping from content, such as words or numbers, to their locations in a document or a set of documents. Instead of listing documents and then the words they contain, an inverted index lists words and then the documents in which those words appear.
- **Doc values**
  - Doc values are a data structure in Elasticsearch that stores field values in a column-oriented fashion, optimized for aggregations, sorting, and scripting. Instead of storing the data alongside the inverted index, doc values are stored separately on disk, making them efficient for retrieving values for a large number of documents.
- **fielddata**
  - Fielddata is an on-disk data structure used by Elasticsearch to enable aggregations, sorting, and scripting on text fields. Because text fields are analyzed (broken down into individual terms), Elasticsearch needs a way to quickly access all the terms for a specific document when performing these operations.
- **Value Count**
  - Value Count is a type of metric aggregation that calculates the total number of values present in a specific field. It essentially counts how many documents have a value for the chosen field, including duplicates if they exist.

### 3.2 Search Analyzer
- **Cardinality**
  - Cardinality aggregation is used to estimate the number of unique values in a field. It's particularly useful when you need to count distinct items but don't need the actual unique values themselves.
- **Avg / Sum / Min / Max**
  - These aggregations are fundamental tools for calculating statistical summaries of numerical data. They compute the average (Avg), total (Sum), smallest value (Min), and largest value (Max) respectively, across a set of documents that match a query.
- **Stats / Extended Stats**
  - Stats and Extended Stats aggregations are used to calculate various statistical measures from a set of numeric values. The Stats aggregation provides basic statistics like count, min, max, average, and sum.
- **Terms**
  - The Terms aggregation is a multi-bucket aggregation that groups documents based on the terms found in a specific field. It analyzes the field's values and creates buckets for each unique term, counting the number of documents that contain that term.
- **Range / Date Range**
  - Range and Date Range aggregations are used to categorize documents into buckets based on numeric or date values falling within specified ranges. These aggregations allow you to define custom intervals for grouping data, providing flexibility in analyzing distributions and trends across your dataset.
- **Nested Aggregations**
  - Nested aggregations allow you to perform aggregations on nested objects within your documents. These nested objects are stored as separate documents internally by Elasticsearch, and nested aggregations provide a way to access and analyze the data within these nested structures as if they were part of the parent document.
- **Pipeline Aggregations**
  - Pipeline aggregations in Elasticsearch take the results of other aggregations as their input, allowing you to perform calculations and derive new insights based on the aggregated data. Instead of operating on the documents themselves, they process the output of other aggregations, enabling you to create complex analytical pipelines within your search queries.
- **Histogram**
  - A histogram aggregation calculates the distribution of numeric values across a set of intervals, or "buckets." It groups data into these buckets based on their values, providing a count of how many data points fall within each bucket's range. This allows you to visualize the frequency of values within specific ranges, revealing patterns and trends in your data.
- **Filter Aggregations**
  - Filter aggregations narrow down the documents that are used to calculate metrics within an aggregation. They work by applying a filter to the documents before the aggregation is performed, effectively creating a subset of the data for analysis.
- **Pivot**
  - The pivot transformation in Elasticsearch is a way to reshape your data by aggregating values from one or more fields into columns. It essentially rotates the data, turning unique values in a field into separate fields in the output.
- **Transform API**
  - The Transform API in Elasticsearch provides a way to summarize and transform data from one or more Elasticsearch indices into a new index. It essentially automates the process of creating aggregated views of your data, allowing you to perform tasks like data reduction, feature engineering, and creating summary indices for faster analysis and visualization.
- **Latest**
  - The "latest" transformation in Elasticsearch is used to identify and extract the most recent document within a group of documents that share a common field value. It allows you to find the most up-to-date information for each unique entity based on a specified sorting criteria, such as a timestamp or version number.
- **Understanding Similarity**
  - Similarity in information retrieval refers to the algorithm used to calculate the relevance score between a search query and a document. It determines how closely a document matches the search terms, influencing the order in which search results are presented.
- **BM25 algorithm**
  - BM25 (Best Matching 25) is a ranking function used by search engines to estimate the relevance of documents to a given search query. It's a bag-of-words retrieval function that scores documents based on the query terms appearing in each document, taking into account term frequency and document length.
- **CAT API**
  - The CAT API in Elasticsearch provides a simple, human-readable way to access cluster-level information using a command-line interface or a RESTful API. It returns data in a tabular format, making it easy to understand and interpret the status, health, and performance metrics of your Elasticsearch cluster.
- **Cluster Monitoring**
  - Cluster monitoring involves continuously observing the health, performance, and resource utilization of an Elasticsearch cluster. This process helps identify potential issues, bottlenecks, and anomalies that could impact the cluster's stability and responsiveness.
- **Segment Merging**
  - Segment merging is the process of combining multiple smaller segments in an Elasticsearch index into larger segments. This optimization reduces the number of segments the search engine needs to consult during a query, leading to faster search performance and more efficient resource utilization.
- **ILM**
  - Index Lifecycle Management (ILM) automates the process of managing Elasticsearch indices over time. It defines policies to control how indices are stored, moved, and deleted based on factors like age, size, or performance.
- **Rollover Policies**
  - Rollover policies in Elasticsearch automate the management of indices over time. They define conditions, such as index size, document count, or age, that trigger the creation of a new index and the transition of write operations to it.
- **Snapshots & restore**
  - Snapshots are backups of your Elasticsearch cluster's data and state, stored in a repository. Restoring from a snapshot allows you to recover data in case of failure, corruption, or accidental deletion.
- **SLM**
  - Snapshot Lifecycle Management (SLM) provides a way to automate the creation, retention, and deletion of Elasticsearch snapshots. It allows you to define policies that specify when snapshots should be taken, how long they should be kept, and how they should be named, ensuring consistent and reliable backups of your Elasticsearch data.
- **Data Tiers**
  - Data tiers in Elasticsearch refer to the strategy of categorizing and storing data based on its access frequency and importance. This approach involves segregating data into different storage types (like hot, warm, cold, and frozen) to optimize performance, cost, and resource utilization.
- **Cross-cluster Replication**
  - Cross-cluster replication (CCR) allows you to replicate indices and their data from one Elasticsearch cluster to another. This enables scenarios like disaster recovery, where a secondary cluster can take over if the primary fails, and data locality, where data is replicated closer to users in different geographic regions for faster access.
- **Vector Search**
  - Vector search is a method of searching for data based on its meaning or context, rather than exact keyword matches. It involves representing data as high-dimensional vectors, where each vector captures the semantic properties of the data.
- **Semantic Search**
  - Semantic search aims to improve search accuracy by understanding the intent and contextual meaning of search queries. Instead of relying solely on keyword matching, it analyzes the relationships between words and concepts to deliver more relevant results.
- **Hybrid Search**
  - Hybrid search combines multiple search techniques to improve the relevance and accuracy of search results. It leverages the strengths of different approaches, such as keyword-based search and semantic search, to provide a more comprehensive and nuanced understanding of the user's query and the available data.
- **Autoscaling**
  - Autoscaling is the ability of a system to automatically adjust its resources (like compute, memory, or storage) based on the current demand. This means that the system can scale up (add more resources) when demand increases and scale down (remove resources) when demand decreases, all without manual intervention.
- **The Analyze API**
  - The Analyze API in Elasticsearch allows you to break down a text string into its individual terms, which are the basic building blocks for searching and indexing. It simulates the analysis process that Elasticsearch performs when indexing or searching documents, letting you see how a specific analyzer would process a given piece of text.
- **Standard Analyzer**
  - The Standard Analyzer is a default text analyzer in Elasticsearch that breaks text into individual words based on whitespace and punctuation. It also converts all terms to lowercase and removes common English stop words like "the," "a," and "is." This analyzer is a good general-purpose choice for many text indexing and searching tasks.
- **Custom Analyzers**
  - Custom analyzers in Elasticsearch provide a way to define how text is processed both when indexing documents and when searching. They allow you to combine character filters, tokenizers, and token filters in a specific order to tailor the analysis process to your specific needs, such as handling language-specific nuances or removing unwanted characters.
- **Boosting Queries**
  - Boosting queries in Elasticsearch allows you to influence the relevance score of documents based on specific criteria. It works by increasing or decreasing the score of documents that match certain query clauses, effectively prioritizing some results over others.
- **Function Score Query**
  - The Function Score Query allows you to modify the score of documents retrieved by a query. It provides a way to apply a function to each document that matches the base query, influencing its final relevance score.
- **Match Phrase Query**
  - The Match Phrase query searches for documents that contain the exact phrase specified in the query. This means the terms must appear in the precise order and be adjacent to each other, as defined in the query string.
- **Synonyms Graph**
  - Synonyms Graph is a feature in Elasticsearch that allows you to expand your search queries by including words or phrases that have similar meanings. Instead of just searching for the exact terms entered by a user, Elasticsearch can also search for related terms defined as synonyms, improving the recall of search results.
- **Roles & Users**
  - Roles and users are fundamental components of security in Elasticsearch. Roles define a set of privileges, specifying what actions a user can perform on which resources (like indices or clusters).
- **API Keys**
  - API keys in Elasticsearch provide a mechanism for authentication and authorization, allowing users or applications to securely access Elasticsearch APIs. They are a more granular alternative to using usernames and passwords, enabling you to restrict access to specific resources and actions.
- **Authentication**
  - Authentication is the process of verifying the identity of a user or system attempting to access a resource. It ensures that only authorized individuals or applications can gain entry by requiring them to prove who they are, typically through credentials like usernames and passwords, API keys, or certificates.

---

## 4. Optional / Specialized Topics

- Elasticsearch Usecases
- Running with Docker
- Kibana Console
- Cluster (System)
- Node (Instance)
- Index (Database)
- Data Nodes
- Coordinating Nodes
- Explicit
- Dynamic
- Mapping Explosion
- Boolean
- Text
- Keyword
- Dates
- Geo Points
- Object
- Nested
- Flattened
- Create Index
- Delete Index
- ES|QL
- Bulk index
- Optimizing Bulk Indexing
- Reindex API

---

## 5. References

- [Elasticsearch Roadmap](https://roadmap.sh/elasticsearch)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer
- Software Architect

### Related Skills
- System Design
- Node.js
- Python
- Go
- Php