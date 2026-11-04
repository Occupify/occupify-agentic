# Redis

## Metadata
- Type: Skill
- Domain: Database & Data Systems
- Source: roadmap.sh
- Source URL: https://roadmap.sh/redis
- Related Roles:
  - PostgreSQL DBA

---

## 1. Beginner

### 1.1 What is Redis?
- **In-memory Data Structure Store**
  - An in-memory database is a purpose-built database that relies primarily on internal memory for data storage. It enables minimal response times by eliminating the need to access standard disk drives (SSDs).
- **Key-value Database**
  - Key-value Database is a non-relational (NoSQL) database that stores data as a collection of key-value pairs. In this model, each piece of data is associated with a unique identifier (key) that is used to retrieve the corresponding value.
- **Cache**
  - Redis cache is an in-memory key-value store used to cache frequently accessed data to improve application performance. By storing data in memory rather than on disk, Redis significantly reduces data access latency, making it ideal for use cases such as session management, caching database query results, and storing temporary data.
- **Message Broker**
  - Redis can act as a lightweight message broker using its Pub/Sub system or Streams. Producers publish messages to channels or streams, and consumers receive them either in real time or by reading from a persistent log.
- **Caching**
  - Redis cache is an in-memory key-value store used to cache frequently accessed data to improve application performance. By storing data in memory rather than on disk, Redis significantly reduces data access latency, making it ideal for use cases such as session management, caching database query results, and storing temporary data.
- **Real-time Analytics**
  - Real-time analytics in Redis involves the immediate processing and analysis of data as it is generated or received, enabling businesses and applications to gain insights and make decisions on-the-fly. Redis's in-memory data storage architecture allows for extremely low-latency access to data, making it ideal for scenarios such as monitoring user behavior, tracking metrics, and processing events in real-time.
- **Session Management**
  - Redis session management leverages the database's speed and versatility for efficient web application user session handling by using key-value storage with session IDs as keys, allowing quick access and updates.
- **Pub/Sub Messaging**
  - Redis Pub/Sub allows publishers to send messages to named channels and subscribers to receive them in real time. It follows a fire-and-forget model: messages are delivered to active subscribers but are not stored if no subscriber is listening.
- **Leaderboards and Counters**
  - Sorted Sets in Redis are commonly used to implement leaderboards, where members are ranked by score and rankings update in real time. Atomic increment commands like INCR make counters accurate under concurrent writes without requiring locks.
- **Redis vs SQL/NoSQL DBs**
  - Redis differs from relational databases by offering no query language, no joins, and no schema enforcement. Compared to document stores like MongoDB, Redis is faster but limited to its supported data types.
- **When to choose Redis?**
  - Redis is a good choice when an application needs sub-millisecond response times for reads and writes. It fits use cases like caching, session storage, real-time leaderboards, and message queuing.
- **Using Package Managers**
  - On Linux, Redis can be installed through the system package manager using apt on Debian-based systems or yum on RHEL-based ones. On macOS, Homebrew provides a Redis formula that handles installation and service management.
- **Pre-compiled Binaries**
  - Redis provides pre-compiled binaries for systems where a package manager is not available or where a specific version is needed. Binaries are downloaded from the official Redis website and run directly without compilation.
- **Using Docker**
  - Redis has an official image on Docker Hub that can be started with a single docker run command. Docker is useful for running Redis in an isolated environment or for testing specific versions without affecting the host system.
- **Starting the Server**
  - The Redis server is started with the redis-server command, optionally followed by a path to a configuration file. By default it listens on port 6379.
- **Connecting using Redis CLI**
  - The Redis CLI (redis-cli) is a command-line interface used to interact with a Redis server. It allows users to run Redis commands, monitor the server, manage data, and perform administrative tasks.

### 1.2 Strings
- **Data Persistence Options**
  - Redis offers two main data persistence options: RDB (Redis Database) snapshots and AOF (Append-Only File). RDB creates point-in-time snapshots of the dataset at specified intervals, making it suitable for infrequent backups but with potential data loss between snapshots.
- **Rich Data Structures**
  - Redis goes beyond simple strings by supporting Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLog, and Streams. Each structure comes with commands optimized for common operations on that type.
- **High Performance and Scalability**
  - High performance and scalability in Redis are achieved through its in-memory data storage model, which allows for extremely fast read and write operations with minimal latency. Redis supports data partitioning, replication, and clustering, enabling it to scale horizontally across multiple nodes and handle large volumes of requests simultaneously.
- **SET**
  - SET stores a string value at a key, replacing any existing value. It accepts options for setting expiration (EX, PX), and conditional flags (NX to set only if the key does not exist, XX to set only if it does).
- **GET**
  - The GET command in Redis is used to retrieve the value associated with a specified key. If the key exists, it returns the value as a string; if the key does not exist, it returns a nil response.
- **INCR**
  - INCR command used to increment the value of a string key by 1. If the key does not exist, it initializes the key with a value of 0 before performing the increment operation, resulting in a value of 1.
- **DECR**
  - The DECR command in Redis decreases the integer value of a key by 1. If the key does not exist, it is initialized to 0 before performing the decrement.
- **APPEND**
  - Redis APPEND command is used to add some value in a key. If the key already exists and is a string, this command appends the value at the end of the string.
- **STRLEN**
  - STRLEN returns the length of the string stored at a key in bytes. It returns 0 if the key does not exist.
- **More Commands**
  - Redis strings include a variety of operations that go beyond basic SET and GET functionality. Examples include MSET and MGET for setting and getting multiple keys at once, GETSET to set a new value while returning the old one, and SETEX or PSETEX for setting a value with an expiration time.

### 1.3 Hashes
- **Basic Commands / SET, GET**
  - SET stores a value under a given key, and GET retrieves the value for that key. These are the most fundamental Redis commands and form the basis of all key-value operations.
- **Setting and Getting Keys**
  - In Redis, setting keys refers to the operation of storing keys by associating them with unique identifiers (keys), it's the process of writing or updating data in the systems. Getting keys refers to the process of retrieving data from the system using the associated key.
- **DEL**
  - The DEL command in Redis is used to delete one or more keys from the database. If the specified key(s) exist, they are removed, and the command returns the number of keys that were deleted.
- **Overview of Data Types**
  - Redis supports several native data types: Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLog, and Streams. Each type is optimized for specific access patterns and comes with a dedicated set of commands.
- **expire**
  - The EXPIRE command is used to set a time-to-live (TTL) for a key in seconds, after which the key will be automatically deleted. If you need to specify the expiration time in milliseconds, you can use the PEXPIRE command.
- **TTL**
  - The TTL command returns the remaining time left to live of a key that is specified, this capability allows a Redis client to check how many seconds a given key will continue to be a part of a dataset.
- **HSET**
  - HSET is a Redis command used to set the value of a specified field within a hash. If the field already exists, it updates the value; if not, it adds the field to the hash.
- **HGET**
  - HGET is a Redis command used to retrieve the value of a specified field within a hash. If the field exists, it returns the value; if not, it returns nil.
- **HGETALL**
  - HGETALL is a Redis command that retrieves all the fields and their values from a specified hash. It returns the data as an array of field-value pairs, making it useful for obtaining a complete view of the hash's contents.
- **HDEL**
  - HDEL is a Redis command used to delete one or more specified fields from a hash. If the fields exist in the hash, they are removed, and the command returns the number of fields that were deleted.
- **HEXISTS**
  - HEXISTS is a Redis command used to check if a specified field exists within a hash. It returns 1 if the field is present and 0 if it is not.
- **Usecases**
  - Hashes are well-suited for storing user profiles, product records, and configuration objects where each entity has multiple named attributes. They are more memory-efficient than storing each attribute as a separate string key.
- **More Commands**
  - Redis Hashes include operations like HMSET and HMGET to set or retrieve multiple fields and values at once, HINCRBY and HINCRBYFLOAT to increment the value of a field by a given integer or float, and HLEN to get the number of fields in a hash. Commands like HKEYS and HVALS are used to retrieve all field names or values, respectively, while HSCAN enables incremental iteration over large hashes.

### 1.4 Sorted Sets
- **ZADD**
  - The ZADD command adds all of the specified members with the specified scores to the sorted set defined at key.
- **ZRANGE**
  - The ZRANGE command can perform multiple range queries including by rank, by score or by lexiographical order. The order of elements returned are always from lowest to highest and any score ties are resolved using reverse lexiographical ordering.
- **ZRANGEBYSCORE**
  - This command retrieves elements from a sorted set stored at the specified key. It returns all elements with scores falling within the given min and max range, inclusive of both boundaries.
- **ZREM**
  - Removes the specified members from the sorted set stored at key. Non existing members are ignored.
- **ZINCRBY**
  - ZINCRBY increments the score of a member in a sorted set by the defined increment. If the member targeted does not exists in the sorted set then it will be added and will be assigned the value of the increment.
- **ZRANK**
  - ZRANK returns the rank of member in the sorted set stored at key, with the scores ordered from low to high. The rank is 0-based, which means that the member with the lowest score has rank 0.

### 1.5 Sets
- **SADD**
  - The SADD command will add the specified members to the set which is stored and the defined key, any specified members that are already a member of the set will simply be ignored.
- **SMEMBERS**
  - The SMEMBERS command returns all the members of the set that is defined at key.
- **SREM**
  - The SREM command will remove the specified members from the set stored at the defined key, specified members that are not a member of the set will be ignored.
- **SISMEMBER**
  - The SISMEMBER command will simply return a boolean value is the members is a part of the set stored at key.
- **SINTER**
  - The SINTER command will return members of the set which will result in the intersection of all the given sets, keys that do not exist are considered to be empty sets.
- **SCARD**
  - SCARD is a Redis command used to get the number of members in a set, it returns the cardinality of the specified set, which is the total count of unique elements it contains. If the set does not exist, SCARD returns 0.
- **SDIFF**
  - SDIFF returns the members in the first set that are not present in any of the subsequent sets. This computes the set difference.

### 1.6 Lists
- **Usecases**
  - Strings are used to store cached HTML fragments, serialized JSON objects, session tokens, and numeric counters. Their simplicity and the availability of atomic operations make them the default choice when none of the more specialized types are needed.
- **LPUSH**
  - LPUSH is a Redis command that inserts one or more elements at the beginning (left side) of a list. If the list does not exist, it creates a new list before performing the insertion.
- **RPUSH**
  - The RPUSH command will insert all the specified values at the tail end o the list that is stored at the defined key, if the key does not exist then it will be created as an empty list before performing the push.
- **LPOP**
  - LPOP is a Redis command that removes and returns the first element from the left side of a list. If the list is empty or does not exist, it returns nil.
- **RPOP**
  - The RPOP command removes and then returns the last elements of the list stored and the specified key, by default it will pop only a single element from the list.
- **LRANGE**
  - LRANGE is a Redis command that retrieves a specified range of elements from a list, defined by a start and stop index. The indices can be positive (starting from 0) or negative (e.g., -1 for the last element).
- **LINDEX**
  - LINDEX is a Redis command used to retrieve an element from a list by its index. The index can be positive (starting from 0 for the first element) or negative (e.g., -1 for the last element).
- **LLEN**
  - LLEN is a Redis command used to return the length of a list stored at a specified key. If the list does not exist, it returns 0.
- **LMOVE**
  - LMOVE is a Redis command used to atomically move an element from one list to another. It pops an element from the source list (either from the left or right end) and pushes it to the destination list (either to the left or right end), based on the specified parameters (LEFT or RIGHT).
- **More Commands**
  - Redis Lists include operations like LTRIM to trim the list to a specified range, RPOPLPUSH to remove an element from one list and append it to another, and BLPOP or BRPOP for blocking pop operations that wait until an element is available. Commands like LPOS allow finding the position of elements, and LSET is used to update a list element at a specified index.

### 1.7 Atomicity in Redis
- **ZCOUNT**
  - ZCOUNT returns the number of elements in the sorted set at the targeted key, with a score between min and max.
- **Usecases**
  - Sorted Sets are used for leaderboards, priority queues, and time-series indexes where entries are ordered by a timestamp score. They also support autocomplete features using lexicographic range queries and rate limiting by storing request timestamps as scores.
- **More Commands**
  - Redis Sorted Sets include operations like ZREVRANGE to get elements in reverse order, ZRANGEBYLEX to retrieve elements within a specific lexicographical range, and ZINTERSTORE or ZUNIONSTORE to perform intersection and union operations on multiple sorted sets and store the results. Commands like ZREMrangeBYRANK and ZREMRANGEBYSCORE allow for removing elements based on their rank or score ranges.
- **Naming Conventions**
  - Naming conventions in Redis are crucial for maintaining organized and understandable data structures, especially in large applications. Common practices include using colons (:) as separators for hierarchical keys (e.g., user:1001:settings), employing prefixes to group related keys (e.g., session:, cache:), and using concise, descriptive names to indicate the purpose and type of the key.
- **Retrieval by Pattern**
  - The SCAN command in Redis is a cursor-based iterator that does not guarantee to return all matching keys in one call, even if COUNT is specified. Instead, SCAN returns a small subset of keys that match the pattern, requiring subsequent calls to complete the iteration.
- **Expiration**
  - Key expiration in Redis is set using EXPIRE, PEXPIRE, EXPIREAT, or PEXPIREAT, depending on whether the timeout is in seconds, milliseconds, or as a Unix timestamp. Once a key expires, Redis removes it lazily on access or actively through a background process.

### 1.8 Pipelining
- **Pipelining**
  - Pipelining in Redis is a technique that allows clients to send multiple commands to the server without waiting for individual responses after each command. Instead, the commands are sent in a batch, and responses are read together at the end.

### 1.9 Batch Operations
- **XREAD**
  - The XREAD command reads data from one or more streams, only returning entries with an ID greater than the last received ID.
- **XLEN**
  - The XLEN command used to get the length of a stream, returning the number of entries it contains. This simple yet powerful command provides a quick way to assess the size of a stream without retrieving its contents.
- **GEOADD**
  - The GEOADD command in Redis is used to add geospatial data to a sorted set, where each entry consists of a member (a unique identifier) and its corresponding longitude and latitude coordinates. This command allows you to store location-based data efficiently, enabling geospatial queries such as finding members within a specified radius or calculating distances between points.
- **GEOSEARCH**
  - The GEOSEARCH command in Redis is used to query geospatial data by finding members within a specified geographic area. It allows you to search for entries based on a central point (latitude and longitude) and a defined radius, or by bounding box coordinates.

---

## 2. Intermediate

### 2.1 Bitmaps
- **Usecases**
  - Lists are commonly used to implement task queues, activity feeds, and chat message histories. The ability to push and pop from both ends makes them flexible for FIFO queues and LIFO stacks.
- **SUNION**
  - SUNION returns the union of all specified sets: every member that appears in at least one of them. The result contains no duplicates.
- **More Commands**
  - Understand fundamental concepts, architectures, and implementation practices of More Commands.
- **SETBIT**
  - The SETBIT command sets or clearts the bit at the specified offset in the string value that is stored at the specified key. When the key does not exist, a new string value will be created and the string is grown to make sure it can hold a bit to the same value as the earlier defined offset.
- **GETBIT**
  - The GETBIT command in Redis retrieves the value of a specific bit at a given offset in a string key. It returns either 0 or 1, depending on the state of the bit at that position.
- **BITCOUNT**
  - The BITCOUNT command in Redis is used to count the number of bits set to 1 (i.e., the number of binary 1s) in the value stored at a specific key. Since Redis allows string values to be stored as binary data, the BITCOUNT command becomes useful for operations involving bits, like efficiently tracking and counting bits in binary-encoded data.
- **BITOP**
  - The BITOP command in Redis performs bitwise operations (AND, OR, XOR, and NOT) across one or more string keys, treating the strings as binary data. The result is stored in a destination key.
- **BITPOS**
  - The BITPOS command in Redis is used to find the position of the first bit set to 1 or 0 in a string key. You can specify a starting and ending byte range for the search.
- **XADD**
  - The XADD command used to append new entries to a stream data structure. It allows you to add one or more field-value pairs as a single entry, automatically assigning a unique ID to each new entry.

### 2.2 HyperLogLog
- **PFADD**
  - PFADD command used to add elements to a HyperLogLog data structure, which is designed for estimating the cardinality (number of unique elements) of a dataset. When elements are added using PFADD, Redis updates the internal structure without storing the actual elements, ensuring low memory consumption.
- **PFCOUNT**
  - PFCOUNT is a Redis command used to retrieve the estimated number of unique elements in one or more HyperLogLog structures. It provides an approximate cardinality count with a typical error rate of 0.81%, making it highly efficient for large datasets while using minimal memory.
- **PFMERGE**
  - PFMERGE is a Redis command used to combine multiple HyperLogLog data structures into a single HyperLogLog key, creating a new structure that represents the union of all unique elements. This command is useful when you want to aggregate and estimate the cardinality of distinct elements across multiple datasets.
- **Usecases**
  - HyperLogLog is suited for counting unique visitors, search queries, or distinct events at scale where approximate counts are acceptable. It is far more memory-efficient than storing actual sets of unique values.
- **XRANGE**
  - The XRANGE command used for retrieving messages from a stream. It allows you to query a range of messages based on their IDs, returning them in chronological order.
- **More Commands**
  - Streams include a variety of operations that enhance the core functionality provided by basic commands like XADD and XREAD. Examples include XDEL to remove specific entries from a stream, XTRIM to control the size of a stream by trimming old entries, and XGROUP for managing consumer groups, allowing multiple clients to read from the same stream in a coordinated manner.

### 2.3 Streams
- **Usecases**
  - Streams are used for event sourcing, activity logs, and inter-service messaging where message history and replay capability matter. Consumer groups allow workloads to be distributed across multiple workers while tracking which messages each worker has processed.

### 2.4 Geospatial Indexes
- **Usecases**
  - Geospatial indexes are used for store locators, delivery radius checks, nearby user features, and map-based searches. The ability to query by distance in a single Redis command avoids the need for a dedicated geospatial database for many common use cases.
- **More Commands**
  - Redis Geospatial indexes include operations like GEODIST to calculate the distance between two members of a geospatial set, GEOHASH to retrieve the Geohash representation of locations, and GEOPOS to get the longitude and latitude of specified members. Additionally, GEORADIUS and GEORADIUSBYMEMBER allow searching for members within a given radius based on coordinates or a reference member.

### 2.5 Pub/Sub
- **SUBSCRIBE**
  - The SUBSCRIBE command subscribes the client to the channels specified, once subscribed the client enters a state where it is not supposed to issue any other commands, except from those in the SUBSCRIBE subset i.e. SSUBSCRIBE, PSUBSCRIBE etc.
- **UNSUBSCRIBE**
  - The UNSUBSCRIBE command unsubscribes the client for the given channels, or all channels if none are specifically stated.
- **PUBLISH**
  - PUBLISH is a Redis command used to send messages to a specified channel in the pub/sub messaging system. When a message is published, all clients that are subscribed to that channel receive the message immediately.
- **More Commands**
  - Redis Pub/Sub include operations like PSUBSCRIBE and PUNSUBSCRIBE for subscribing and unsubscribing to channels using pattern matching, allowing for flexible topic-based subscriptions. Additionally, PUBSUB CHANNELS lists active channels, PUBSUB NUMSUB shows the number of subscribers per channel, and PUBSUB NUMPAT returns the count of active pattern subscriptions.

### 2.6 Transactions
- **WATCH**
  - The WATCH command marks the given keys to be watched for conditional execution of a transaction. It's a critical component of Redis's approach to handling race conditions in multi-key transactions.
- **EXEC**
  - The EXEC command in Redis is used to execute a transaction that has been initiated with the MULTI command. When a transaction is started with MULTI, subsequent commands are queued but not executed immediately.
- **MULTI**
  - MULTI is a Redis command used to start a transaction, allowing a group of commands to be executed sequentially and atomically. After initiating a MULTI block, commands are queued instead of being executed immediately.

### 2.7 Lua Scripting
- **EVAL**
  - The EVAL command in Redis allows the execution of Lua scripts directly on the server, enabling complex operations that can be atomically executed. This command takes a Lua script as an argument, along with a list of keys and arguments for the script.
- **EVALSHA**
  - The EVALSHA command in Redis is used to execute a Lua script that has already been loaded into the server with the SCRIPT LOAD command. Instead of sending the entire script each time, you provide the SHA1 hash of the script, which allows for more efficient execution and reduced network overhead.

### 2.8 Persistence Options
- **Usecases**
  - Lua scripting is used when a sequence of reads and writes must happen atomically, such as conditional updates, rate limiting with exact semantics, or multi-step workflows. It avoids the overhead of multiple round trips and removes the need for application-level locking in most cases.
- **How RDB Works?**
  - The RDB (Redis Database Backup) mechanism in Redis creates snapshots of the dataset at specified intervals and saves them to disk as a compact binary file. This process is triggered manually, via the SAVE or BGSAVE commands, or automatically based on predefined conditions.
- **Configuring Save Interval**
  - Configuring the save interval in Redis controls how often data is saved from memory to disk (RDB snapshots). This is done using the save directive in the redis.conf file.
- **No Persistence Option**
  - The No Persistence option in Redis disables all data persistence mechanisms, meaning that no data will be saved to disk. This can be configured by turning off both RDB snapshots and AOF (Append-Only File) logging.

### 2.9 Authentication
- **Usecases**
  - Pub/Sub is used for live notifications, chat rooms, real-time dashboards, and broadcasting configuration changes across services. It is effective when messages are transient and delivery to offline consumers is not required.
- **Optimistic Locking**
  - Optimistic locking in Redis uses WATCH to detect concurrent modifications without holding a lock. The client reads a value, prepares a transaction, and calls EXEC: if the watched key changed since WATCH, the transaction is retried.

### 2.10 Network Security
- **Network Security**
  - Network security for Redis involves restricting access using firewalls, binding Redis to specific interfaces, and using private networks or VPNs. Redis should never be exposed directly to the public internet without authentication.

### 2.11 SSL/TLS Encryption
- **SSL/TLS Encryption**
  - SSL/TLS is supported by Redis starting with version 6 as an optional feature that needs to be enabled at compile time. TLS will add a layer to the communication stack with overheads due to the read and writes from an SSL connection and integrity checks, this will lead to a decrease of achieveable throughput.

### 2.12 Replication Basics
- **Usecases / Best Practices**
  - Understand fundamental concepts, architectures, and implementation practices of Usecases / Best Practices.

---

## 3. Advanced

### 3.1 Redis Sentinel
- **Redis Sentinel**
  - Redis Sentinel serves as a robust high-availability solution for Redis deployments, offering a comprehensive suite of monitoring, notification, and automatic failover capabilities. By continuously overseeing master and replica Redis servers, Sentinel ensures system integrity and swift response to failures.

### 3.2 Clustering
- **How AOF Works?**
  - The Append-Only File (AOF) in Redis is a persistence mechanism that logs every write operation to a file in sequential order, ensuring data durability. Each command is appended to the end of the AOF file, which Redis can replay to rebuild the dataset in case of a restart.
- **AOF rewrite & compaction**
  - Persistence refers to the writing of data to durable storage, such as a solid-state disk (SSD). Redis provides a range of persistence options of which AOF (Append Only File) is one of the options.
- **Truncation / Corruption**
  - Truncation and corruption typically refer to scenarios where data is unexpectedly cut off or altered, compromising its integrity. This can occur due to various reasons, such as sudden power failures, system crashes, or disk errors.
- **Usecases**
  - Append-Only File (AOF) is a persistence strategy that logs every write operation received by the server into a file, which can be replayed to reconstruct the original dataset during a restart. It is most effective in environments where minimizing data loss is a priority, as it allows for per-second synchronization policies that ensure only a minimal amount of recent data is sacrificed in the event of a system failure.
- **Memory Management**
  - Redis provides several tools for managing memory usage. The maxmemory directive caps the amount of RAM Redis can use, and maxmemory-policy determines what happens when the limit is reached (e.g., evicting least-recently-used keys).
- **Max Memory Policy**
  - The maxmemory-policy setting controls how Redis selects keys to evict when the memory limit is reached. Options include evicting the least recently used key (allkeys-lru), evicting keys with TTLs set (volatile-lru), or returning errors instead of evicting (noeviction).
- **Search**
  - Redis Search enhances the Redis experience by offering a robust set of search and query features, including a rich query language, incremental indexing for JSON and hash documents, vector search, full-text search, geospatial queries, and aggregations. These capabilities allow Redis to function as a document database, vector database, secondary index, and search engine, making it suitable for a variety of applications.
- **RedisTimeSeries**
  - RedisTimeSeries is a module for storing and querying time-series data. It supports automatic downsampling, retention policies, and aggregation functions like average, min, and max over time windows.

### 3.3 Redis Modules
- **RDB vs AOF Tradeoffs**
  - RDB produces smaller files, restarts faster, and has lower write overhead, but can lose minutes of data if Redis crashes between snapshots. AOF has higher durability with much smaller potential data loss, but produces larger files and slower restarts on large datasets.
- **Hybrid Persistence**
  - Hybrid persistence in Redis combines both RDB (Redis Database Backup) and AOF (Append-Only File) mechanisms to leverage the benefits of each. RDB provides efficient snapshot-based backups at defined intervals, while AOF logs every write operation to ensure minimal data loss.
- **Slow Log Analysis**
  - The Redis Slow Log in a system to log any queries that take longer than a specified time. The execution time does not include any I/O operations such as talking with the client, just the time need to execute the specified command.
- **redis-benchmark**
  - redis-benchmark is a built-in tool that measures Redis throughput by running a configurable number of commands against a live instance. It reports requests per second for each command type and helps establish performance baselines.
- **Monitoring**
  - Performance monitoring involves tracking metrics like command latency, memory usage, hit/miss ratios, and connection counts over time. Tools like INFO, MONITOR, and external metrics exporters (such as the Redis Prometheus exporter) are used to collect this data.
- **RedisJSON**
  - RedisJSON is a Redis module that adds native JSON support. It allows storing, querying, and modifying JSON documents in place using a path-based syntax.
- **RedisBloom**
  - RedisBloom adds probabilistic data structures to Redis, including Bloom filters, Cuckoo filters, Count-Min Sketch, and Top-K. Bloom filters allow fast membership testing with a configurable false positive rate and no false negatives.

### 3.4 redis.conf
- **INFO**
  - INFO command that provides detailed information and statistics about the server, including memory usage, CPU load, connected clients, replication status, and more. It can be called without arguments to get a full overview or with specific sections (e.g., INFO memory) to retrieve targeted data.
- **MONITOR**
  - MONITOR is a Redis command that provides a real-time feed of all commands executed on the server, displaying each command along with its arguments as they are processed. It is primarily used for debugging, monitoring, or analyzing the behavior of a Redis instance.
- **RedisInsight**
  - RedisInsight is a graphical management tool for Redis provided by Redis Ltd. It allows browsing keys, running commands, viewing memory usage, and analyzing slow logs through a web-based UI.
- **RedisCommander**
  - Redis Commander is an open-source, web-based GUI for managing Redis instances. It provides a key browser, command console, and basic server information.

### 3.5 Upgrading Redis
- **Upgrading Redis**
  - Upgrading Redis typically involves careful planning and execution to ensure minimal downtime and data integrity. The process generally includes backing up your data, installing the new Redis version, updating configuration files to accommodate any new settings or deprecated options, and restarting the Redis server.

### 3.6 Backup and Recovery
- **Backup and Recovery**
  - Backing up and recovering Redis data is crucial for ensuring data persistence and reliability. Redis, by default, stores its data in memory for fast access, but it provides mechanisms to persist data to disk to allow for recovery in case of failure or system restarts.

### 3.7 Disaster Recovery
- **Disaster Recovery**
  - Disaster recovery for Redis involves having off-site backups of RDB or AOF files and a documented process for restoring them. Replication across availability zones or data centers reduces the risk of losing data in a regional failure.

### 3.8 Redis Enterprise
- **Active-Active geo Distribution**
  - An Active-Active architecture is a data resiliency architecture that distributes the database information over multiple data centers via independent and geographically distributed clusters and nodes. It is a network of separate processing nodes, each having access to a common replicated database such that all nodes can participate in a common application ensuring local low latency with each region being able to run in isolation.
- **Redis on Flash**
  - Redis Enterprise is the commercial distribution of Redis provided by Redis Ltd. It extends open-source Redis with features designed for production deployments at scale: active-active geo-distribution, automatic sharding, enhanced security controls, and enterprise support.
- **Security and Compliance**
  - Redis Enterprise provides role-based access control, audit logging, and encryption at rest to meet enterprise compliance requirements. It integrates with LDAP and SAML for centralized identity management.
- **When to consider enterprise?**
  - Redis Enterprise is typically considered when an organization requires enhanced scalability, high availability, and advanced features beyond what open-source Redis provides. It's particularly valuable for large-scale applications with demanding performance requirements, complex architectures, or mission-critical deployments.

---

## 4. Optional / Specialized Topics

- Caching
- Real-time Analytics
- Session Management
- Pub/Sub Messaging
- Leaderboards and Counters
- Redis vs SQL/NoSQL DBs
- When to choose Redis?
- Using Package Managers
- Pre-compiled Binaries
- Using Docker
- Starting the Server
- Connecting using Redis CLI
- GET
- INCR
- DECR
- APPEND
- STRLEN
- More Commands
- expire
- TTL
- HSET
- HGET
- HGETALL
- HDEL
- HEXISTS

---

## 5. References

- [Redis Roadmap](https://roadmap.sh/redis)

---

## 6. Related Roles / Topics

### Related Roles
- PostgreSQL DBA

### Related Skills
- MongoDB
- SQL