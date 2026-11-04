# Computer Science

## Metadata
- Type: Skill
- Domain: Computer Science & Architecture
- Source: roadmap.sh
- Source URL: https://roadmap.sh/computer-science
- Related Roles:
  - Blockchain Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Pick a Language
- **Python**
  - Python is a well known programming language which is both a strongly typed and a dynamically typed language. Being an interpreted language, code is executed as soon as it is written and the Python syntax allows for writing code in functional, procedural or object-oriented programmatic ways.
- **Go**
  - Go is a compiled, statically typed language created at Google to make concurrent, networked software simple to write and deploy. It has built-in support for concurrency through goroutines and channels, and it compiles to a single binary with no external runtime dependencies.
- **C#**
  - C# is an object-oriented language developed by Microsoft that runs on the .NET runtime. It combines a syntax similar to Java with features like properties, LINQ, and async/await for asynchronous programming.
- **Rust**
  - Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency. It achieves memory safety without a garbage collector by using a unique ownership model that tracks the lifetime of data at compile time.
- **C++**
  - C++ extends the C language with object-oriented features like classes, inheritance, and templates, while keeping low-level memory control. It compiles to native machine code and gives direct access to hardware resources, making it a common choice for game engines, operating systems, and performance-critical software.
- **Java**
  - Java is an object-oriented, statically typed language that compiles to bytecode and runs on the Java Virtual Machine (JVM), which lets the same compiled code run on any platform with a JVM installed. It manages memory automatically through garbage collection.

### 1.2 Data Structures
- **Linked List**
  - Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index. Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element.
- **Stack**
  - Stack is a linear collection of items where items are inserted and removed in a particular order. Stack is also called a LIFO Data Structure because it follows the "Last In First Out" principle i.e.
- **Queue**
  - A queue is a data structure that processes elements in the order they arrived, following a first-in, first-out (FIFO) rule. New elements are added at the back and removed from the front.
- **Hash Table**
  - A hash table stores key-value pairs and uses a hash function to compute an index into an underlying array where each value is stored. This gives average-case O(1) time for lookups, insertions, and deletions.
- **Array**
  - An array stores a fixed-size sequence of elements in contiguous memory, where each element is accessed directly by its index. This contiguous layout makes reading or writing any element an O(1) operation.
- **Tree**
  - A tree is a hierarchical data structure made of nodes connected by edges, with one node designated as the root and every other node reachable from it through exactly one path. Each node can have child nodes, and nodes with no children are called leaves.
- **Binary Tree**
  - A binary tree is a tree where each node has at most two children, usually called the left and right child. This constraint makes it simple to reason about and forms the basis for more specialized structures like binary search trees and heaps.
- **Binary Search Tree**
  - A binary search tree (BST) is a binary tree where, for every node, all values in its left subtree are smaller and all values in its right subtree are larger. This ordering allows searching, insertion, and deletion in O(log n) time on average, since each comparison rules out half of the remaining nodes.
- **Full Binary Tree**
  - A full binary tree is a binary tree where every node has either zero or two children, never just one. This property is used in some algorithm proofs and data structures, like certain heap implementations, where a strict shape simplifies reasoning about node counts and depth.
- **Graph**
  - Graphs in data structures are non-linear data structures made up of a finite number of nodes or vertices and the edges that connect them. Graphs in data structures are used to address real-world problems in which it represents the problem area as a network like telephone networks, circuit networks, and social networks.
- **Directed Graph**
  - A directed graph is graph, i.e., a set of objects (called vertices or nodes) that are connected together, where all the edges are directed from one vertex to another. A directed graph is sometimes called a digraph or a directed network.
- **Heap**
  - A heap is a tree-based structure that satisfies the heap property: in a max heap, every parent is greater than or equal to its children, and in a min heap, every parent is smaller than or equal to its children. This makes finding the maximum or minimum element an O(1) operation, while insertion and removal take O(log n).
- **Big O**
  - The Big O notation can be used to describe how the running time of an algorithm scales with the growth of the input size, ignoring implementation details such as programming language and computer speed. Specifically, it denotes the upper bound of the growth rate of a function that relates the running time of an algorithm to its input size.
- **Constant**
  - Constant time, written O(1), means an operation takes the same amount of time regardless of input size. Accessing an array element by index or reading a value from a hash table are typical examples, since neither depends on how much data the structure holds.
- **Logarithmic**
  - Logarithmic time, written O(log n), means the work needed grows very slowly as input size increases, typically because the algorithm cuts the problem size in half (or by some fraction) at each step. Binary search is a classic example: doubling the input size only adds one more comparison.

### 1.3 Asymptotic Notation
- **Complete Binary Tree**
  - A complete binary tree fills every level from left to right, with all levels full except possibly the last, which is filled from the left. This shape allows the tree to be stored efficiently in an array, since a node's children can be found using simple index arithmetic instead of pointers.
- **Balanced Tree**
  - A balanced tree keeps the height difference between subtrees small, typically bounded by a constant, so no path from root to leaf is much longer than another. This guarantees that operations like search, insert, and delete stay close to O(log n) regardless of insertion order.
- **Unbalanced Tree**
  - An unbalanced tree has subtrees of very different heights, which can happen when data is inserted in a sorted or near-sorted order into a plain binary search tree. In the worst case, the tree degenerates into something resembling a linked list, and operations that should take O(log n) instead take O(n).
- **Big-Theta**
  - Big-Theta (Θ) notation describes a tight bound on an algorithm's growth rate, meaning the algorithm's running time grows at the same rate as the given function in both the best and worst case. It gives the most precise asymptotic description when an algorithm's upper and lower bounds match.
- **Big Omega**
  - Big Omega (Ω) notation describes a lower bound on an algorithm's growth rate, meaning the algorithm will take at least this much time or space in the best case. It is used to express the minimum amount of work an algorithm is guaranteed to do for a given input size.
- **Linear**
  - Linear algorithms are algorithms that have a runtime that is directly proportional to the size of the input. This means that the runtime of the algorithm will increase linearly with the size of the input.
- **Polynomial**
  - Polynomial time means an algorithm's running time can be expressed as n raised to some fixed power, such as O(n²) or O(n³). Problems solvable in polynomial time are generally considered tractable in complexity theory, forming the basis of the complexity class P.
- **Exponential**
  - Exponential time, written O(2^n), means the work doubles with each additional unit of input size. Algorithms with exponential time complexity become impractical quickly as input grows, and they often show up in brute-force solutions to problems without known efficient algorithms.
- **Factorial**
  - Factorial time, written O(n!), means the work grows by the factorial of the input size, making it impractical for anything but very small inputs. Algorithms that generate every possible permutation of a set, like a brute-force solution to the traveling salesman problem, run in factorial time.
- **Tail Recursion**
  - Tail recursion is a special kind of recursion where the recursive call is the very last thing in the function. It's a function that does not do anything at all after recursing.
- **Non-Tail Recursion**
  - Non-tail recursion is a form of recursion where work remains to be done after the recursive call returns, such as combining the result with something else. Each call must keep its stack frame until the recursive call underneath it finishes, which means the call stack grows with each level of recursion and cannot be optimized away like tail recursion.
- **Binary Search**
  - Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.
- **Linear Search**
  - Linear search is a very simple algorithm that is used to search for a value in an array. It sequentially checks each element of the array until a match is found or until all the elements have been searched.
- **Pre-Order Traversal**
  - Pre-order traversal is a way to visit every node in a tree data structure. It follows a specific order: first, the current node is processed (or visited).
- **In-Order Traversal**
  - In-order traversal is a tree traversal algorithm that visits the left subtree, the root, and then the right subtree. This is the most common way to traverse a binary search tree.
- **Post Order Traversal**
  - Post-order traversal is a type of tree traversal that visits the left subtree, then the right subtree, and finally the root node. This is the opposite of pre-order traversal, which visits the root node first, then the left subtree, and finally the right subtree.
- **Breadth First Search**
  - Breadth first search is a graph traversal algorithm that starts at the root node and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- **Depth First Search**
  - Depth first search is a graph traversal algorithm that starts at a root node and explores as far as possible along each branch before backtracking.
- **Bellman Ford's Algorithm**
  - Bellman-Ford's algorithm is a graph algorithm that finds the shortest path from a source vertex to all other vertices in a graph. It is a dynamic programming algorithm that uses a bottom-up approach to find the shortest path.
- **Dijkstra's Algorithm**
  - Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It repeatedly picks the closest unvisited vertex and updates the shortest known distances to its neighbors, using a priority queue to make this selection efficient.
- **A* Algorithm**
  - A\ is a graph traversal algorithm that is used to find the shortest path between two nodes in a graph. It is a modified version of Dijkstra's algorithm that uses heuristics to find the shortest path.
- **Small O**
  - Small o notation describes an upper bound that is strictly greater than the actual growth rate, rather than a tight or achievable bound like Big O. It is used to express that one function grows strictly slower than another, useful in more formal algorithm analysis and proofs.
- **Small Omega**
  - Small omega notation describes a lower bound that is strictly less than the actual growth rate, the counterpart to small o. It states that an algorithm's growth rate is strictly greater than a given function, used mainly in theoretical analysis rather than everyday complexity comparisons.

### 1.4 Common Algorithms
- **Undirected Graph**
  - An undirected graph is graph, i.e., a set of objects (called vertices or nodes) that are connected together, where all the edges are bidirectional. An undirected graph is sometimes called an undirected network.
- **Spanning Tree**
  - A spanning tree is a subset of Graph G, which has all the vertices covered with minimum possible number of edges. Hence, a spanning tree does not have cycles and it cannot be disconnected..
- **Adjacency Matrix**
  - An adjacency matrix is a square matrix used to represent a finite graph. It is used to represent the connections between vertices in a graph.
- **Adjacency List**
  - An adjacency list represents a graph by storing, for each vertex, a list of the vertices it connects to. This representation uses memory proportional to the number of edges, which makes it efficient for sparse graphs where most vertices are not directly connected to each other.
- **Bubble Sort**
  - Bubble sort repeatedly steps through a list, comparing adjacent elements and swapping them if they are in the wrong order, until no swaps are needed. Each pass moves the largest unsorted element into its correct position, like a bubble rising to the top.
- **Selection Sort**
  - Selection sort is a sorting algorithm that selects the smallest unsorted item in the list and swaps it with index 0, then finds the next smallest and places it into index 1 and so on.
- **Insertion Sort**
  - Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time by comparisons. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
- **Heap Sort**
  - Heap sort is a comparison based sorting algorithm. It is similar to selection sort where we first find the maximum element and place the maximum element at the end.
- **Quick Sort**
  - Quick Sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

### 1.5 String Search & Manipulations
- **Merge Sort**
  - Merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
- **Search Pattern in Text**
  - Searching pattern in text is a very common task in computer science. It is used in many applications like spell checkers, text editors, and many more.
- **Suffix Arrays**
  - Suffix arrays are a data structure that allows us to quickly find all the suffixes of a string in lexicographical order. This is useful for many problems, such as finding the longest common substring between two strings, or finding the number of distinct substrings of a string.
- **Brute Force Search**
  - Brute force search is a simple algorithm that checks for a pattern in a string by comparing each character of the string with the first character of the pattern. If the first character matches, it then compares the next character of the string with the next character of the pattern and so on.
- **Knuth-Morris Pratt**
  - The Knuth-Morris-Pratt (KMP) algorithm searches for a pattern in text by preprocessing the pattern into a table that tracks the longest proper prefix that is also a suffix. This lets the algorithm skip re-checking characters it has already matched when a mismatch occurs, giving it O(n + m) time complexity.
- **Robin-Karp**
  - Rabin-Karp algorithm is a string searching algorithm that uses hashing to find any one of a set of pattern strings in a text. For strings of average length n, it performs in O(n+m) time with O(m) space, where m is the length of the pattern.
- **Substring Search**
  - Substring search is the problem of finding a substring in a string. This is a very common problem in computer science, and there are many algorithms for solving it.

### 1.6 Floating Point Math
- **LRU Cache**
  - LRU cache is a cache that evicts the least recently used item first. It is a very common cache algorithm.
- **MFU Cache**
  - MFU Cache is another cache algorithm. The difference is that instead of deleting the least frequently used entry, the MFU Cache deletes the most frequently used entry.
- **LFU Cache**
  - LFU Cache is a data structure that stores key-value pairs. It has a fixed size and when it is full, it removes the least frequently used key-value pair.

### 1.7 Endianess
- **Finding Hamiltonian Paths**
  - Hamiltonian paths are paths that visit every node in a graph exactly once. They are named after the famous mathematician Hamilton.
- **Solving N Queen Problem**
  - N Queen Problem is a famous problem in Computer Science. It is a problem of placing n queens on an n x n chessboard such that no two queens attack each other.
- **Maze Solving Problem**
  - Maze solving problem is a classic problem in computer science. It is a problem where we have to find a path from a starting point to an end point in a maze.
- **The Knight's Tour Problem**
  - Knight's Tour Problem is a problem where we have to find a path for a knight to visit all the cells of a chessboard without visiting any cell twice.
- **Dijkstra's Algorithm**
  - Dijkstra's algorithm is a greedy algorithm that finds the shortest path between two nodes in a graph. It is a very common algorithm used in computer science and is used in many applications such as GPS navigation, network routing, and finding the shortest path in a maze.
- **Huffman Coding**
  - Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
- **Kruskal's Algorithm**
  - Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. It is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which form a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.
- **Ford-Fulkerson Algorithm**
  - Ford Fulkerson Algorithm is a greedy algorithm that is used to find the maximum flow in a flow network. It is also known as the Edmonds-Karp Algorithm.
- **Rabin-Karp Algorithm**
  - Rabin-Karp algorithm is a string searching algorithm that uses hashing to find any one of a set of pattern strings in a text. For strings of average length n, it performs in O(n+m) time with O(m) space, where m is the length of the pattern.
- **Big Endian**
  - Big endian is a type of endianness in which the most significant byte is stored at the lowest memory address. This means that the most significant byte is stored first and the least significant byte is stored last.

---

## 2. Intermediate

### 2.1 Character Encodings
- **Prim's Algorithm**
  - Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. A minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Unicode**
  - Unicode is a standard for encoding characters. It is a superset of ASCII, which means that ASCII is a subset of Unicode.
- **ASCII**
  - ASCII is a character encoding standard for electronic communication. It was developed from telegraph code and uses 7 bits to represent 128 different characters.

### 2.2 Bitwise Operators
- **Bitwise Operators**
  - Bitwise operators are used to perform operations on individual bits of a number. They are used in cryptography, image processing, and other applications.

### 2.3 Design Patterns
- **Little Endian**
  - Little Endian is a way of storing data in memory. It is the opposite of Big Endian.
- **GoF Design Patterns**
  - Gang of Four (GoF) design patterns are a set of 23 design patterns that were first described in the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides. The book is commonly referred to as the "Gang of Four book".
- **Architectural Patterns**
  - Architectural patterns are a high-level design pattern that focuses on the overall structure of the system. They are similar to design patterns, but they are more concerned with the structure of the system.
- **Dependency Injection**
  - Dependency injection is a software design pattern that allows us to decouple the dependencies of a class from the class itself. This allows us to write more flexible and testable code.
- **Null Object Pattern**
  - Null object pattern is a design pattern that is used to represent a null value with an object. It is a way to avoid null reference exceptions by providing a default object that does nothing.
- **Type Object Pattern**
  - Type object pattern is a creational design pattern that allows us to create a new object of a type without exposing the object creation logic to the client. It is used when we need to create a new object of a type, but we don't know which type we need to create until runtime.

### 2.4 Common UML Diagrams
- **Class Diagrams**
  - Class Diagrams are used to model the static structure of a system. They are used to show the classes, their attributes, operations (or methods), and the relationships between objects.
- **Usecase Diagrams**
  - A use case diagram shows the interactions between actors, such as users or external systems, and the use cases, or goals, they can achieve within a system. It gives a high-level view of what a system does from the perspective of the people or systems that use it, without describing implementation details.

### 2.5 Basic Math Skills
- **Activity Diagrams**
  - Activity diagrams are used to model the flow of control in a system. They are used in conjunction with use case diagrams to model the behavior of the system for each use case.
- **Statemachine Diagrams**
  - State machine diagrams are used to show the different states an object can be in at a given time. The object can be in one and only one state at a given time.
- **Sequence Diagrams**
  - A sequence diagram shows how objects interact with each other over time by depicting the order in which messages are sent between them. It is commonly used to visualize the flow of a specific scenario, like a user login process, across multiple components.
- **Probability**
  - Probability measures how likely an event is to occur, expressed as a number between 0 and 1. In computer science, it comes up in randomized algorithms, hashing collision analysis, and average-case complexity analysis, where the expected behavior of an algorithm depends on the distribution of its inputs.
- **Combinatorics**
  - Combinatorics is the branch of math concerned with counting, arranging, and combining objects according to given rules, covering concepts like permutations and combinations. It is used in algorithm analysis to count the number of possible states or configurations a problem can have, which often determines the feasibility of a brute-force approach.
- **OSI Model**
  - The OSI and TCP/IP model is used to help the developer to design their system for interoperability. The OSI model has 7 layers while the TCP/IP model has a more summarized form of the OSI model only consisting 4 layers.

### 2.6 Complexity Classes
- **Boyer-Moore**
  - Boyer Moore algorithm is a string searching algorithm that is used to find the index of a substring in a string. It is a very efficient algorithm that is used in many applications.
- **NP**
  - The NP in NP class stands for Non-deterministic Polynomial Time. It is the collection of decision problems that can be solved by a non-deterministic machine in polynomial time.
- **P = NP**
  - P = NP is one of the most famous open problems in computer science, asking whether every problem whose solution can be verified quickly can also be solved quickly. Most researchers believe P does not equal NP, but no one has proven it either way, and a proof in either direction would have major implications for cryptography and optimization.

### 2.7 Tries
- **Tries**
  - Tries are a data structure that can be used to store strings. The idea is to store the characters of the string in a tree-like structure, where each node of the tree represents a single character.

### 2.8 NP Complete
- **NP Hard**
  - An NP-hard problem is at least as hard as the hardest problem in NP and it is the class of the problems such that every problem in NP reduces to NP-hard.
- **Travelling Salesman Problem**
  - The Travelling Salesman Problem (TSP) is a classic problem in computer science. It is a problem that is NP-complete, which means that it is a problem that is hard to solve.
- **Knapsack Problem**
  - KnapSack Problem is a classic problem in computer science. It is a problem in which we are given a set of items, each with a weight and a value, and we need to determine which items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Longest Path Problem**
  - The Longest Path Problem asks for the longest simple path between two vertices in a graph, one that does not repeat any vertex. Unlike the shortest path problem, which has efficient algorithms, finding the longest path is NP-hard in general graphs, though it becomes solvable in polynomial time for special cases like directed acyclic graphs.
- **SQL vs NoSQL Databases**
  - SQL databases store data in structured tables with fixed schemas and use SQL to query relationships between them, prioritizing consistency and complex querying. NoSQL databases store data in more flexible formats, like documents, key-value pairs, or graphs, and generally prioritize horizontal scalability and flexible schemas over strict consistency guarantees.
- **Co-NP**
  - Co-NP stands for the complement of NP Class. It means if the answer to a problem in Co-NP is No, then there is proof that can be checked in polynomial time.

### 2.9 Balanced Search Trees
- **AVL Trees**
  - An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one. When an insertion or deletion violates this balance, the tree performs rotations to restore it, guaranteeing O(log n) time for search, insert, and delete.
- **Red / Black Trees**
  - A red-black tree is a self-balancing binary search tree where each node is colored red or black, and a set of coloring rules ensures the tree never becomes more than roughly twice as tall as the shortest possible balanced tree. It requires fewer rotations on average than an AVL tree, which makes it a common choice for implementing ordered maps and sets in standard libraries.
- **2 3 Search Trees**
  - In practice: 2-3 trees have faster inserts at the expense of slower searches (since height is more compared to AVL trees). You would use 2-3 tree very rarely because its implementation involves different types of nodes.
- **2 3 4 Trees**
  - In practice: For every 2-4 tree, there are corresponding red–black trees with data elements in the same order. The insertion and deletion operations on 2-4 trees are also equivalent to color-flipping and rotations in red–black trees.
- **K-ary / M-ary Tree**
  - A k-ary (or m-ary) tree is a generalization of a binary tree where each node can have up to k children instead of just two. Increasing the branching factor reduces the tree's height for a given number of nodes, which is useful in structures like B-trees where minimizing height matters for disk access.
- **B-Tree**
  - A B-tree is a self-balancing tree where each node can hold multiple keys and have multiple children, keeping the tree shallow even with a large number of elements. This makes B-trees well suited for storage systems like databases and file systems, where each node can be sized to match a disk block and minimize the number of disk reads needed to find data.
- **Caching**
  - Caching is a way of storing data in a temporary storage to make future requests faster. It is one of the most important tools in the computer science toolbox.
- **Proxy**
  - A proxy server is an intermediary piece of hardware/software sitting between the client and the backend server. It receives requests from clients and relays them to the origin servers.
- **gRPC**
  - gRPC is a remote procedure call framework that lets a client call methods on a server as if they were local function calls, using Protocol Buffers for efficient binary serialization. It runs over HTTP/2, which enables features like multiplexed streaming, and is commonly used for fast communication between internal microservices.
- **K-D Trees**
  - K-D Trees are a data structure that allow for fast nearest neighbor search in high dimensional spaces. They are a generalization of binary search trees, and are used in a variety of applications, including computer vision and computational geometry.

---

## 3. Advanced

### 3.1 System Design
- **Horizontal vs Vertical Scaling**
  - Horizontal scaling is the process of adding more machines to your system. This is also known as scaling out.
- **Load Balancing**
  - Load balancing is the process of distributing network or application traffic across a cluster of servers. Load balancing is used to improve responsiveness and reliability of applications, maximize throughput, minimize response time, and avoid overload of any single server.
- **Clustering**
  - At a high level, a computer cluster is a group of two or more computers, or nodes, that run in parallel to achieve a common goal. This allows workloads consisting of a high number of individual, parallelizable tasks to be distributed among the nodes in the cluster.
- **CDN**
  - A CDN is a network of servers that are distributed geographically. The servers are connected to each other and to the internet.
- **Queues**
  - Messaging queues are a common way to decouple systems. They are used to decouple the producer of a message from the consumer of a message.
- **Architectural Styles**
  - Architectural patterns are the fundamental organization of a system, defining how the system is composed and how its components interact. Architectural patterns are identified by their name, like client-server, peer-to-peer, and layered.
- **REST**
  - REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.
- **GraphQL**
  - GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.
- **Cloud Design Patterns**
  - Cloud design patterns are reusable solutions for common problems that arise when building and operating applications on cloud infrastructure, such as handling transient failures, managing configuration across services, or scaling components independently. Patterns like circuit breaker, retry, and sidecar address the distributed and elastic nature of cloud environments.
- **DCL**
  - DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, permissions, and other controls of the database system.

### 3.2 Databases
- **Normalization / Denormalization**
  - Normalization organizes a database schema to reduce data redundancy by splitting data into related tables, following a set of normal forms. Denormalization does the opposite, intentionally duplicating data across tables to reduce the number of joins needed for common queries, trading storage and update complexity for faster reads.
- **Entity-Relationship Model**
  - Entity relationship model is a high-level data model that describes the logical structure of a database. It is a graphical representation of entities and their relationships to each other, typically used in modeling the organization of data within databases or information systems.
- **DDL**
  - DDL or Data Definition Language actually consists of the SQL commands that can be used to define the database schema. It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.
- **DML**
  - The SQL commands that manipulate data in the database belong to DML, or Data Manipulation Language, and this includes most of the SQL statements. DCL is the component of the SQL statement that controls access to data and to the database.
- **DQL**
  - DQL (Data Query Language) is the subset of SQL used to retrieve data from a database, primarily through the SELECT statement. It is used to read and filter existing data without modifying it.
- **Locking**
  - Locks are used to prevent data from being modified by multiple processes at the same time. This is important because if two processes are modifying the same data at the same time, the data can become corrupted.
- **ACID Model**
  - ACID are the four properties of any database system that help in making sure that we are able to perform the transactions in a reliable manner. It's an acronym which refers to the presence of four properties: atomicity, consistency, isolation and durability
- **BASE**
  - BASE describes an alternative to the ACID model used by many distributed and NoSQL databases, standing for basically available, soft state, and eventually consistent. It favors availability and scalability over the strict consistency guarantees of ACID, accepting that data may be temporarily inconsistent across nodes before converging.
- **CAP Theorem**
  - CAP is an acronym for Consistency, Availability, and Partition Tolerance. According to the CAP theorem, any distributed system can only guarantee two of the three properties at any time.
- **PACELC**
  - The PACELC Theorem is an extension of the CAP Theorem. One of the questions that CAP Theorem wasn’t able to answer was “what happens when there is no Partition, What Logical Combination then a Distributed System have?“.
- **Indexes**
  - An index is a data structure that you build and assign on top of an existing table that basically looks through your table and tries to analyze and summarize so that it can create shortcuts.
- **Views**
  - Views in SQL are kind of virtual tables. A view also has rows and columns as they are in a real table in the database.
- **Transactions**
  - In short, a database transaction is a sequence of multiple operations performed on a database, and all served as a single logical unit of work — taking place wholly or not at all. In other words, there's never a case where only half of the operations are performed and the results saved.

### 3.3 Networking
- **TCP/IP Model**
  - The OSI and TCP/IP model is used to help the developer to design their system for interoperability. The OSI model has 7 layers while the TCP/IP model has a more summarized form of the OSI model only consisting 4 layers.
- **DNS**
  - The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com.
- **HTTP**
  - HTTP is the TCP/IP based application layer communication protocol which standardizes how the client and server communicate with each other. It defines how the content is requested and transmitted across the internet.
- **TLS & HTTPS**
  - TLS (Transport Layer Security) is a cryptographic protocol that provides privacy and data integrity between two communicating applications. It is widely used to secure HTTP, although it can be used with any protocol.
- **Sockets**
  - A socket is an interface for network communication. It is a way for two programs to communicate with each other over a network.

### 3.4 Security
- **Stored Procedures**
  - Stored Procedures are created to perform one or more DML operations on Database. It is nothing but the group of SQL statements that accepts some input in the form of parameters and performs some task and may or may not returns a value.
- **Database Federation**
  - Federation (or functional partitioning) splits up databases by function. The federation architecture makes several distinct physical databases appear as one logical database to end-users.
- **Replication**
  - Replication is a process that involves sharing information to ensure consistency between redundant resources such as multiple databases, to improve reliability, fault-tolerance, or accessibility.
- **Sharding**
  - Database sharding is a method of distributing data across multiple machines. It is a horizontal scaling technique, as opposed to vertical scaling, which is scaling by adding more power to a single machine.
- **Public Key Cryptography**
  - Public-key cryptography, or asymmetric cryptography, is the field of cryptographic systems that use pairs of related keys. Each key pair consists of a public key and a corresponding private key.
- **Hashing / Encryption / Encoding**
  - Hashing, encryption, and encoding are often confused but serve different purposes. Hashing produces a fixed-size, one-way output used to verify data integrity or store passwords securely, encryption transforms data reversibly so only someone with the right key can read it, and encoding transforms data into a different format for compatibility, with no security guarantee at all.
- **Hashing Algorithms**
  - Hashing algorithms map an input of any size to a fixed-size value called a hash. Since there are far more possible inputs than hash values, two different inputs can produce the same hash, which is called a collision; a good cryptographic hashing algorithm makes collisions hard to find.
- **OWASP Top 10**
  - OWASP or Open Web Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.

### 3.5 How Computers Work
- **How CPU Executes Programs**
  - The CPU executes programs by repeatedly fetching instructions from memory, decoding them to understand the operation, and then executing those operations. This cycle, called the fetch-decode-execute cycle, continues for each instruction in the program, with the CPU using registers for temporary storage and a program counter to keep track of the next instruction.
- **How Computers Calculate**
  - Computers perform calculations by representing numbers in binary and manipulating them using logic gates built from transistors, which implement operations like addition through circuits called adders. Complex operations, like multiplication or floating point math, are built up from combinations of these basic binary operations at the hardware level.
- **Registers and RAM**
  - Registers are the smallest data-holding elements built into the processor itself. Registers are the memory locations that are directly accessible by the processor.
- **Instructions and Programs**
  - Instructions are the most basic commands a CPU can understand, directing it to perform specific actions like adding numbers or moving data. A program, on the other hand, is a collection of these instructions, organized in a sequence to accomplish a particular task.
- **CPU Cache**
  - A CPU cache is a hardware cache used by the central processing unit of a computer to reduce the average cost to access data from the main memory. A cache is a smaller, faster memory, located closer to a processor core, which stores copies of the data from frequently used main memory locations.

### 3.6 Processes and Threads
- **Long Polling**
  - Long polling is a technique used to implement server push functionality over HTTP. It is a method of opening a request on the server and keeping it open until an event occurs, at which point the server responds.
- **Short Polling**
  - In short polling, the client requests information from the server. The server processes the request.
- **Web Sockets**
  - Web sockets are a bidirectional communication protocol between a client and a server. They are used for real-time applications like chat, multiplayer games, and live data updates.
- **SSE**
  - Server-Sent Events is a server push technology enabling a client to receive automatic updates from a server via an HTTP connection, and describes how servers can initiate data transmission towards clients once an initial client connection has been established.
- **Process Forking**
  - Process forking is a way to create a new process from an existing process. The new process is a copy of the existing process.
- **Memory Management**
  - Memory management is the process of allocating and deallocating memory. It is a very important part of any programming language.
- **Lock / Mutex / Semaphore**
  - A lock or mutex ensures that only one thread can access a shared resource at a time, preventing race conditions when multiple threads read and write the same data. A semaphore is a more general version that allows a set number of threads to access a resource concurrently, using a counter instead of a simple locked or unlocked state.
- **Concurrency in Multiple Cores**
  - Concurrency or Parallelism is simultaneous execution of processes on a multiple cores per CPU or multiple CPUs (on a single motherboard). Concurrency is when Parallelism is achieved on a single core/CPU by using scheduling algorithms that divides the CPU's time (time-slice).
- **Scheduling Algorithms**
  - Scheduling algorithms determine the order in which an operating system runs competing processes or threads on the available CPU cores. Different algorithms, like round robin, shortest job first, or priority scheduling, balance goals such as fairness, responsiveness, and overall throughput differently.
- **CPU Interrupts**
  - CPU Interrupts are a way for the CPU to communicate with the rest of the computer. They are a way for the CPU to tell the rest of the computer that it needs to do something.
- **Processes vs Threads**
  - Processes and threads are the basic building blocks of a computer program. They are the smallest units of execution in a program.
- **Skip Lists**
  - Skip lists are a data structure that allows you to search, insert and delete in a sorted list in O(log n) time on average. Skip lists are a probabilistic data structure: the level of each element is chosen at random, so O(log n) is the expected time of an operation, not a guarantee.

---

## 4. Optional / Specialized Topics

- C++
- Java
- Array
- Tree
- Binary Tree
- Binary Search Tree
- Full Binary Tree
- Graph
- Directed Graph
- Heap
- Big O
- Constant
- Logarithmic
- Big Omega
- Linear
- Polynomial
- Exponential
- Factorial
- Tail Recursion
- Non-Tail Recursion
- Binary Search
- Linear Search
- Pre-Order Traversal
- In-Order Traversal
- Post Order Traversal

---

## 5. References

- [Computer Science Roadmap](https://roadmap.sh/computer-science)

---

## 6. Related Roles / Topics

### Related Roles
- Blockchain Developer
- DevOps Engineer

### Related Skills
- Linux
- Php
- AWS
- Software Design & Architecture