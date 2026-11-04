# Data Structures & Algorithms

## Metadata
- Type: Skill
- Domain: Computer Science & Architecture
- Source: roadmap.sh
- Source URL: https://roadmap.sh/datastructures-and-algorithms
- Related Roles:
  - Software Engineer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Pick a Language
- **JavaScript**
  - JavaScript allows you to add interactivity to your pages. Common examples that you may have seen on the websites are sliders, click interactions, popups and so on.
- **Java**
  - Java is a statically typed, object-oriented language that runs on the JVM. It is heavily used in software engineering interviews and large-scale systems.
- **Go**
  - Go is a statically typed, compiled language designed for simplicity and concurrency. It has a small standard library and explicit syntax, which makes it suitable for learners who want to understand how things work without relying on abstractions.
- **C#**
  - C# is a statically typed, object-oriented language developed by Microsoft. It is widely used in enterprise software and game development with Unity.
- **C++**
  - C++ is a compiled, statically typed language known for its speed and fine-grained control over memory. It is the dominant language in competitive programming because of its performance and rich standard library (STL), which includes built-in implementations of common data structures and algorithms.
- **Ruby**
  - Ruby is a high-level, interpreted programming language that blends Perl, Smalltalk, Eiffel, Ada, and Lisp. Ruby focuses on simplicity and productivity along with a syntax that reads and writes naturally.

### 1.2 Programming Fundamentals
- **Python**
  - Python is a dynamically typed, interpreted language with a concise and readable syntax. It is popular for learning DSA because less boilerplate code means the logic of an algorithm stays visible.
- **Rust**
  - Rust is a modern systems programming language focusing on safety, speed, and concurrency. It accomplishes these goals by being memory safe without using garbage collection.
- **Language Syntax**
  - Language syntax refers to the set of rules that define how code must be written in a given programming language. It covers how to declare variables, write expressions, define functions, and structure a program so the compiler or interpreter can parse it.
- **Control Structures**
  - Control structures direct the flow of execution in a program. They include conditionals like if/else, which run code only when a condition is true, and loops like for and while, which repeat a block of code.
- **Functions**
  - A function is a named, reusable block of code that takes inputs, performs a task, and optionally returns a result. Functions let you break a program into smaller, manageable pieces and avoid repeating the same code in multiple places.
- **OOP Basics**
  - Object-oriented programming (OOP) organizes code around objects, which combine data (fields) and behavior (methods). The four main principles are encapsulation, abstraction, inheritance, and polymorphism.
- **Pseudo Code**
  - Pseudocode is an informal way to describe an algorithm using plain language and simple structure, without following the syntax rules of any specific programming language. It helps plan logic before writing real code and is commonly used in textbooks, interviews, and design discussions.

### 1.3 What are Data Structures?
- **What are Data Structures?**
  - A data structure is a way of organizing and storing data in memory so it can be accessed and modified efficiently. Different data structures are suited to different kinds of problems: arrays work well for indexed access, linked lists for frequent insertions, and hash tables for fast lookups.

### 1.4 Why are Data Structures Important?
- **Array**
  - An array is a collection of elements stored in contiguous memory locations, accessed by index. It supports constant-time reads and writes by position but requires shifting elements when inserting or deleting in the middle.
- **Common Runtimes**
  - Common runtimes describe the typical growth rates seen in algorithms, ordered from fastest to slowest: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), and O(n!). Recognizing these patterns helps predict an algorithm's scalability and compare alternatives quickly.

---

## 2. Intermediate

### 2.1 Basic Data Structures
- **Linked Lists**
  - A linked list is a sequence of nodes where each node stores a value and a reference to the next node. Unlike arrays, linked lists do not require contiguous memory, making insertions and deletions at the head or middle efficient.
- **Stacks**
  - A stack is a linear data structure that follows the last-in, first-out (LIFO) principle. Elements are added and removed from the same end, called the top.
- **Queues**
  - A queue is a linear data structure that follows the first-in, first-out (FIFO) principle. Elements are added at the back and removed from the front.
- **Hash Tables**
  - A hash table stores key-value pairs and uses a hash function to compute the index where a value is stored. This allows average constant-time lookups, insertions, and deletions.
- **Constant**
  - An algorithm with constant time complexity, O(1), takes the same amount of time regardless of input size. Accessing an array element by index or looking up a value in a hash table are O(1) operations.
- **Logarithmic**
  - Logarithmic time complexity (O(log n)) often indicates that the algorithm halves the size of the input at each step. It's more efficient compared to linear time complexity.

### 2.2 Algorithmic Complexity
- **Time vs Space Complexity**
  - Time complexity measures how many operations an algorithm performs relative to input size. Space complexity measures how much memory it uses.
- **How to Calculate Complexity?**
  - Calculating complexity involves identifying the dominant operations in an algorithm and counting how many times they run as input size grows. For a single loop over n elements, the time complexity is O(n).
- **Linear**
  - Linear time complexity, denoted as O(n), is one of the best possible algorithmic performance situations. An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of the input data.
- **Polynomial**
  - Polynomial time complexity, denoted as O(n^k), is a class of time complexity that represents the amount of time an algorithm takes to run as being proportional to the size of the input data raised to a constant power 'k'. Polynomial time complexity includes runtimes like O(n), O(n^2), O(n^3), etc.
- **Asymptotic Notation**
  - Asymptotic notation is a way to describe the limiting behavior of a function, typically representing the time or space complexity of an algorithm, as the input size grows. It focuses on the dominant terms and ignores constant factors and lower-order terms, providing a simplified and generalized way to compare the efficiency of different algorithms.

### 2.3 Sorting Algorithms
- **Big-O Notation**
  - Big-O notation describes the upper bound of an algorithm's growth rate, representing the worst-case scenario. An algorithm that is O(n²) will take at most quadratic time for any input of size n.
- **Big-θ Notation**
  - Big-Θ (Theta) notation describes a tight bound, meaning the algorithm grows at exactly that rate in both the best and worst case. If an algorithm is Θ(n log n), its runtime is always proportional to n log n, not just bounded by it.
- **Bubble Sort**
  - Bubble sort repeatedly compares adjacent elements and swaps them if they are out of order, moving the largest unsorted element to its correct position in each pass. It runs in O(n²) time in the average and worst case, making it inefficient for large lists.
- **Merge Sort**
  - Merge sort divides a list in half, recursively sorts each half, and then merges the two sorted halves into one sorted list. It runs in O(n log n) time in all cases and is stable, preserving the relative order of equal elements.
- **Insertion Sort**
  - Insertion sort builds a sorted list one element at a time by taking each new element and inserting it into its correct position among the already-sorted elements. It runs in O(n²) in the worst case but is efficient for small or nearly sorted lists, where it approaches O(n).
- **Selection Sort**
  - Selection sort repeatedly finds the minimum element in the unsorted portion of the list and moves it to the correct position. It always performs O(n²) comparisons regardless of input order.
- **Heap Sort**
  - Heap sort uses a binary heap data structure to sort elements. It first builds a max-heap from the input, then repeatedly extracts the maximum element and places it at the end of the sorted portion.

### 2.4 Search Algorithms
- **Exponential**
  - Exponential time complexity is denoted as O(2^n), where a growth in n leads to an exponential growth in the number of steps required to complete a task. It means that the time complexity will double with every additional element in the input set.
- **Factorial**
  - Factorial complexity, O(n!), grows faster than exponential and represents the number of permutations of n elements. Algorithms that generate every possible ordering of a set, such as brute-force permutation search, run in factorial time.
- **Quick Sort**
  - Quicksort selects a pivot element and partitions the list so that all elements smaller than the pivot come before it and all larger elements come after. It then recursively sorts each partition.
- **Linear Search**
  - Linear search is one of the simplest search algorithms. In this method, every element in an array is checked sequentially starting from the first until a match is found or all elements have been checked.
- **Binary Search**
  - Binary search finds a target value in a sorted list by repeatedly halving the search space. It compares the target to the middle element and discards the half that cannot contain the target.

### 2.5 Tree Data Structures
- **Tree Traversal**
  - Tree traversal refers to visiting every node in a tree in a specific order. The three common strategies for binary trees are in-order, pre-order, and post-order, each visiting nodes in a different sequence relative to the root.
- **Search Algorithms**
  - Tree search algorithms locate a specific node or value within a tree structure. The two primary strategies are breadth-first search, which explores level by level, and depth-first search, which explores as far down a branch as possible before backtracking.
- **Breadth First Search**
  - Breadth-first search (BFS) explores a tree level by level, visiting all nodes at the current depth before moving deeper. It uses a queue to track nodes to visit next.
- **Depth First Search**
  - Depth-first search on a graph explores as far as possible along each path before backtracking. It is used to detect cycles, find connected components, and perform topological sorting.
- **In-Order Traversal**
  - In-order traversal visits the left subtree first, then the current node, then the right subtree. For a binary search tree, this produces nodes in ascending sorted order.
- **Pre-Order Traversal**
  - Pre Order Traversal is a very specific kind of tree traversal in data structures. In this method of traversal, the process starts from the root node, then proceeds to the left subtree, and finally to the right subtree.
- **Post-Order Traversal**
  - Post Order Traversal is a technique used in Binary Tree structure where each node is processed after its child nodes. As the name suggests, it first traverses the left subtree, then the right subtree, and finally the root node.

### 2.6 Graph Data Structures
- **Big-Ω Notation**
  - Big-Ω (Omega) notation describes the lower bound of an algorithm's growth, representing the best-case scenario. If an algorithm is Ω(n), it will always take at least linear time.
- **Binary Trees**
  - A binary tree is a tree where each node has at most two children, referred to as the left and right child. It is the foundation for more specialized structures like binary search trees and heaps.
- **Binary Search Trees**
  - A binary search tree (BST) is a binary tree where every node's left subtree contains only values less than the node, and the right subtree contains only values greater. This property allows efficient search, insertion, and deletion in O(log n) average time.
- **Directed Graph**
  - A Directed Graph, also known as a DiGraph, is a set of vertices and a collection of directed edges. Each directed edge has an initial vertex, also called the tail, and a terminal vertex, also known as the head.
- **Undirected Graph**
  - An Undirected Graph is a type of graph in which the edges are not directed. That is, they do not point in any specific direction and are not ordered pairs.
- **Search Algorithms**
  - Graph search algorithms explore nodes and edges to find paths, detect connectivity, or locate specific nodes. BFS and DFS are the two foundational strategies, each suited to different problems.
- **Breadth First Search**
  - Breadth-first search on a graph visits all neighbors of a node before moving to the next level, using a queue to track the order. It finds the shortest path in unweighted graphs and can determine whether two nodes are connected.
- **Depth First Search**
  - Depth-first search on a graph explores as far as possible along each path before backtracking. It is used to detect cycles, find connected components, and perform topological sorting.
- **Shortest Path Algorithms**
  - Shortest path algorithms find the minimum-cost route between two nodes in a weighted graph. Different algorithms suit different scenarios: Dijkstra's handles non-negative weights, Bellman-Ford handles negative weights, and A\ uses heuristics for faster pathfinding.

---

## 3. Advanced

### 3.1 Advanced Data Structures
- **AVL Trees**
  - An AVL tree is a self-balancing binary search tree where the height difference between the left and right subtrees of any node, called the balance factor, is at most one. After each insertion or deletion, rotations are performed to restore balance.
- **B-Trees**
  - A B-tree is a self-balancing search tree designed for systems that read and write large blocks of data, such as databases and file systems. Unlike binary trees, each node can have many children and keys, reducing the height of the tree and minimizing disk accesses.
- **Dijkstra's Algorithm**
  - Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights. It uses a priority queue to always process the nearest unvisited node.
- **Bellman-Ford Algoritm**
  - The Bellman-Ford algorithm finds the shortest paths from a source node in a weighted graph, including graphs with negative edge weights. It works by relaxing all edges repeatedly for n-1 iterations, where n is the number of nodes.
- **Minimum Spanning Tree**
  - A minimum spanning tree (MST) is a subset of a graph's edges that connects all vertices with the minimum total edge weight and no cycles. MSTs are used in network design, clustering, and approximation algorithms.
- **Prim's Algorithm**
  - Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.
- **Trie**
  - A trie, also called a prefix tree, is a tree-like structure where each node represents a character, and paths from root to leaf represent strings. It allows fast prefix lookups and is commonly used in autocomplete, spell checkers, and IP routing tables.
- **Segment Trees**
  - A segment tree is a binary tree used to answer range queries, such as the sum or minimum of elements in a subarray, in O(log n) time. It also supports point and range updates efficiently.
- **Fenwick Trees**
  - A Fenwick tree, also called a binary indexed tree (BIT), is a data structure that supports prefix sum queries and point updates in O(log n) time. It is more memory-efficient and simpler to implement than a segment tree for problems involving cumulative sums.
- **Disjoint Set (Union-Find)**
  - A disjoint set, or union-find structure, tracks a collection of non-overlapping sets and supports two operations: union, which merges two sets, and find, which identifies which set an element belongs to. With path compression and union by rank, both operations run in nearly constant time.
- **Suffix Trees and Arrays**
  - Suffix Trees and Arrays are advanced data structures used primarily for string manipulation and searches. A Suffix Tree is a compressed trie containing all the suffixes of a given text as their keys and positions as their values.
- **Heap**
  - A heap is a complete binary tree that satisfies the heap property: in a max-heap, every parent node is greater than or equal to its children; in a min-heap, every parent is less than or equal to its children. The top element is always the maximum or minimum, enabling O(1) access to the extreme value.
- **A* Algorithm**
  - A\ is a shortest path algorithm that uses a heuristic to guide its search toward the goal, making it faster than Dijkstra's in practice. The heuristic estimates the cost from the current node to the destination, helping the algorithm prioritize more promising paths.

### 3.2 Complex Data Structures
- **Kruskal's Algorithm**
  - Kruskal's algorithm builds a minimum spanning tree by sorting all edges by weight and adding each edge to the MST if it does not create a cycle. It uses a union-find structure to efficiently check for cycles.
- **B/B+ Trees**
  - A B+ tree is a variant of the B-tree where all data is stored in leaf nodes, and internal nodes contain only keys used for navigation. Leaf nodes are linked together, making range queries efficient.
- **Skip List**
  - A skip list is a probabilistic data structure built from multiple linked lists layered on top of each other, where higher layers allow fast skipping over elements. It achieves O(log n) average-case time for search, insertion, and deletion without the complexity of tree rotations.
- **ISAM**
  - ISAM (Indexed Sequential Access Method) is a disk-based file organization method that stores records in sorted order and maintains a static index for fast access. It supports efficient sequential and random reads but handles insertions poorly once the structure is built.
- **2-3 Trees**
  - A 2-3 tree is a balanced search tree where every internal node has either two or three children, and all leaves are at the same depth. This guarantees O(log n) time for search, insertion, and deletion.
- **Brute Force**
  - Brute force solves a problem by trying every possible solution and returning the one that works. It requires no insight into the problem structure and always finds a correct answer if one exists.
- **Merge Intervals**
  - Merge intervals is a technique for solving problems involving overlapping ranges. The typical approach sorts intervals by start time, then iterates through them, merging any that overlap with the previous one.
- **Two Heaps**
  - The two heaps technique uses a max-heap and a min-heap together to efficiently track the median or partition a dataset. One heap holds the lower half of elements and the other holds the upper half, keeping them balanced so the median is always accessible in O(1).
- **Multi-threaded**
  - Multi-threaded algorithms divide work across multiple threads running concurrently, using parallelism to reduce total execution time. Designing them correctly requires managing shared state to avoid race conditions and deadlocks.
- **Island traversal**
  - Island traversal refers to problems where a 2D grid is searched to identify and count connected regions, often called islands, surrounded by water or empty space. It is typically solved using DFS or BFS starting from unvisited land cells, marking each reachable cell as visited.

### 3.3 Indexing
- **Linear**
  - Linear indexing stores index entries in a sequential structure, where each entry maps directly to a record position. It works well for small datasets and simple range scans but becomes slower as data grows because lookups may require scanning the index itself.
- **Tree-Based**
  - Tree-based indexing uses a tree structure, typically a B-tree or B+ tree, to organize index entries. It supports efficient range queries, equality lookups, and sorted access in O(log n) time.

### 3.4 Problem Solving Techniques
- **Backtracking**
  - Backtracking builds a solution incrementally and abandons a path as soon as it determines the path cannot lead to a valid solution. It explores possibilities using recursion and prunes branches early to reduce the search space.
- **Greedy Algorithms**
  - Greedy algorithms make the locally optimal choice at each step with the hope that this leads to a globally optimal solution. They are fast and simple but do not always produce the best result.
- **Randomised Algorithms**
  - Randomized algorithms use random numbers as part of their logic, either to avoid worst-case behavior or to approximate solutions. Quicksort with a random pivot is a classic example: randomization makes the worst case very unlikely in practice.
- **Divide and Conquer**
  - Divide and conquer is a powerful algorithm design technique that solves a problem by breaking it down into smaller and easier-to-manage sub-problems, until these become simple enough to be solved directly. This approach is usually carried out recursively for most problems.
- **Recursion**
  - Recursion is a technique where a function calls itself with a smaller version of the problem until reaching a base case. It maps naturally to problems with recursive structure, such as tree traversal, divide and conquer, and backtracking.
- **Dynamic Programming**
  - Dynamic programming solves problems by breaking them into overlapping subproblems and storing the results to avoid redundant computation. It applies when a problem has optimal substructure and overlapping subproblems.
- **Two Pointer Technique**
  - The two pointer technique uses two indices that move through an array or list to solve problems more efficiently than nested loops. One common pattern starts both pointers at opposite ends and moves them inward.
- **Sliding Window Technique**
  - The sliding window technique maintains a subset of elements within a fixed or variable-size window that moves across a sequence. As the window slides, elements are added at one end and removed from the other, avoiding the need to recompute results from scratch.
- **Leetcode**
  - LeetCode is the most widely used platform for technical interview preparation. It offers thousands of problems categorized by topic and difficulty, with a built-in code editor and test runner.
- **Kth Element**
  - The Kth element problem asks for the k-th smallest or largest element in an unsorted array without fully sorting it. Efficient solutions include using a min-heap or max-heap of size k, or the quickselect algorithm, which runs in O(n) average time.

### 3.5 Platforms to Practice
- **Edabit**
  - Edabit is a coding practice platform that focuses on smaller, beginner-friendly challenges designed to build programming fluency quickly. Problems are shorter and more approachable than those on LeetCode, making it a good starting point for learners who are still developing confidence with code before moving to interview-style questions.
- **Fast and Slow Pointers**
  - The fast and slow pointers pattern uses two pointers that traverse a data structure at different speeds. It is commonly used to detect cycles in linked lists, find the middle of a list, or locate the kth element from the end, running in O(n) time with constant space.
- **Cyclic Sort**
  - Cyclic sort is a sorting technique for arrays whose values fall in a known, contiguous range, typically 1 to n. Each element is swapped to the position matching its value, placing everything correctly in O(n) time and O(1) space — ideal as a building block for problems such as finding missing or duplicate numbers.

---

## 4. Optional / Specialized Topics

- C++
- Ruby
- Functions
- OOP Basics
- Pseudo Code
- Constant
- Logarithmic
- Asymptotic Notation
- Insertion Sort
- Selection Sort
- Heap Sort
- Binary Search
- In-Order Traversal
- Pre-Order Traversal
- Post-Order Traversal
- Undirected Graph
- Search Algorithms
- Breadth First Search
- Depth First Search
- Shortest Path Algorithms
- Minimum Spanning Tree
- Prim's Algorithm
- Trie
- Segment Trees
- Fenwick Trees

---

## 5. References

- [Data Structures & Algorithms Roadmap](https://roadmap.sh/datastructures-and-algorithms)

---

## 6. Related Roles / Topics

### Related Roles
- Software Engineer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Computer Science
- Python
- C++
- Linux
- Rust