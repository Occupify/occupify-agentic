# LeetCode

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/leetcode
- Related Roles:
  - Software Engineer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 What is LeetCode
- **JavaScript**
  - JavaScript is a solid choice if you already use it professionally or are preparing for frontend-focused roles. Its array methods and object literals are expressive, and most algorithmic patterns translate naturally to it.
- **Ruby**
  - Ruby is an expressive, readable language with clean syntax and strong built-in enumerable methods that make array and hash manipulation concise. It is less common in technical interviews than Python, JavaScript, or Java, but it is a valid choice if you use it professionally and are comfortable with it.

### 1.2 What are coding patterns?
- **C++**
  - C++ is the language of choice for competitive programmers and is common in companies where raw performance matters, such as systems, gaming, or high-frequency trading. It has the fastest execution time of any commonly used interview language and gives you direct access to the standard template library, which includes a heap, set, map, and many other useful structures.

### 1.3 Pick a language
- **Java**
  - Java is one of the most commonly used interview languages, especially at large companies with backend and enterprise codebases. Its type system is verbose but explicit, and the standard library is comprehensive with well-documented data structures including priority queues, linked lists, and tree maps.
- **Go**
  - Go is a statically typed, compiled language designed for simplicity and performance. It is increasingly popular in backend and infrastructure roles and is commonly used at companies like Uber, Cloudflare, and Docker.
- **Python**
  - Python is the most popular language for LeetCode preparation and for good reason. Its syntax is concise, its built-in data structures like lists, dictionaries, and sets map directly to the structures you use in almost every problem, and the standard library includes a heap module and collections utilities that save significant time.
- **Rust**
  - Rust is a systems programming language focused on memory safety and performance without a garbage collector. It is gaining popularity for roles in systems programming, WebAssembly, and performance-critical applications.

### 1.4 Arrays & Hashing
- **Two Sum**
  - You are given an array of integers and a target number. The goal is to find two numbers in the array that add up to the target and return their positions.
- **Valid Anagram**
  - Given two strings, decide if one is an anagram of the other, meaning both contain the exact same characters with the same frequency. The trick is not to sort (which works but is slower), but to count character frequencies using a hash map and compare them.
- **Contains Duplicate**
  - Given an array, return true if any value appears more than once. The brute force compares every pair, but a hash set lets you check for duplicates in a single pass.
- **Group Anagrams**
  - Given a list of strings, group together all strings that are anagrams of each other. Since anagrams share the same characters, sorting each string gives a common key you can use in a hash map.
- **Top K Frequent Elements**
  - Given an array and a number k, return the k most frequent elements. You could sort by frequency, but the optimal approach uses bucket sort.
- **More Exercises**
  - Below you can find other popular questions covering Arrays & Hashing. Work through these once you are comfortable with the five above.

### 1.5 Two Pointers
- **Valid Palindrome**
  - Given a string, determine if it reads the same forward and backwards after removing non-alphanumeric characters and ignoring case. Two pointers start at each end and move inward, comparing characters as they go.
- **3Sum**
  - Given an array of integers, find all unique triplets that sum to zero. You sort the array first, then for each element use two pointers to find pairs that complete the triplet.
- **Container With Most Water**
  - Given an array of bar heights, find two bars that together with the x-axis form a container holding the most water. You start with the widest possible container and move the pointer on the shorter side inward, since that is the only move that could increase the area.
- **Trapping Rain Water**
  - Given an array of bar heights representing an elevation map, compute how much water can be trapped between the bars after rain. For each position, the water level is determined by the shorter of the tallest bars to its left and right.
- **Two Sum II**
  - Given a sorted array, find two numbers that add up to a target and return their positions. Because the array is sorted, you can use two pointers starting from each end and move them based on whether the current sum is too large or too small.
- **More Exercises**
  - Below you can find other popular questions covering Two Pointers. Work through these once you are comfortable with the five above.

### 1.6 Stacks
- **Valid Parentheses**
  - Given a string of brackets, determine if it is valid, meaning every opening bracket is closed by the same type in the correct order. You push opening brackets onto a stack and pop when you see a closing bracket, checking for a match.
- **Min Stack**
  - Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1) time. The trick is to maintain a second stack that tracks the current minimum at each level.
- **Daily Temperatures**
  - Given an array of daily temperatures, return an array where each element is the number of days until a warmer temperature. A monotonic stack stores indices of temperatures in decreasing order, and whenever a warmer day is found, all colder days in the stack get their answer.
- **Generate Parentheses**
  - Given n, generate all combinations of well-formed parentheses. You build strings recursively, adding an opening bracket if you still have some left and a closing bracket only if it would not break validity.
- **Largest Rectangle in Hist.**
  - Given an array of bar heights, find the area of the largest rectangle that fits in the histogram. A monotonic stack tracks bars in increasing order of height, and each time a shorter bar is encountered, rectangles extending from the previous bars are resolved.
- **More Exercises**
  - Below you can find other popular questions covering Stack. Work through these once you are comfortable with the five above.

---

## 2. Intermediate

### 2.1 Binary Search
- **Binary Search**
  - Given a sorted array and a target, return the index of the target or -1 if not found. You repeatedly halve the search space by comparing the middle element to the target.
- **Search in Rotated Array**
  - A sorted array has been rotated at an unknown index. Find a target value in O(log n).
- **Minimum in Rotated Array**
  - Given a rotated sorted array, find the minimum element in O(log n). The minimum is always at the rotation point, and you can locate it by checking which half is sorted and narrowing toward the unsorted side.
- **Koko Eating Bananas**
  - Koko can eat at most k bananas per hour and must finish all piles within h hours. Find the minimum k.
- **Median of Two Arrays**
  - Given two sorted arrays, find the median of their combined elements in O(log(min(m, n))). You binary search on the smaller array to find a partition where all elements on the left side are smaller than all on the right.
- **More Exercises**
  - Below you can find other popular questions covering Binary Search. Work through these once you are comfortable with the five above.

### 2.2 Sliding Window
- **Best Time to Buy and Sell**
  - Given an array of daily stock prices, find the maximum profit from one buy and one sell. You track the minimum price seen so far and the best profit achievable at each step using a single pass.
- **Substring Without Repetition**
  - Find the length of the longest substring that contains no duplicate characters. You expand the right pointer and shrink the left pointer whenever a duplicate enters the window, using a set to track current characters.
- **Minimum Window Substring**
  - Given strings s and t, find the smallest substring of s that contains all characters of t. You expand the right pointer until you have a valid window, then shrink from the left as much as possible while keeping it valid.
- **Character Replacement**
  - Given a string and a number k, find the length of the longest substring where you can replace at most k characters to make all characters the same. You track the count of the most frequent character in the window, and if the window size minus that count exceeds k, you shrink from the left.
- **Sliding Window Maximum**
  - Given an array and a window size k, return the maximum value in each window. A monotonic deque stores indices in decreasing order of value, so the front is always the current maximum.
- **More Exercises**
  - Below you can find other popular questions covering Sliding Window. Work through these once you are comfortable with the five above.

### 2.3 Linked List
- **Reverse Linked List**
  - Given the head of a linked list, reverse it in place and return the new head. You iterate through the list, keeping track of the previous node, current node, and next node, rewiring each pointer as you go.
- **Merge Two Sorted Lists**
  - Given the heads of two sorted linked lists, merge them into one sorted list by splicing nodes together without creating new ones. You compare the heads of both lists at each step and attach the smaller node to your result.
- **Linked List Cycle**
  - Given the head of a linked list, determine if it contains a cycle. The fast and slow pointer technique has one pointer move one step at a time and the other move two steps at a time; if there is a cycle, they will eventually meet.
- **Reorder List**
  - Given a linked list, reorder it so that nodes alternate from the front and back of the original list. You find the middle, reverse the second half, then merge the two halves.
- **Merge K Sorted Lists**
  - Given k sorted linked lists, merge them into one sorted list. The optimal approach uses a min-heap to always extract the smallest current node across all lists.
- **More Exercises**
  - Below you can find other popular questions covering Linked List. Work through these once you are comfortable with the five above.

### 2.4 Trees
- **Binary Tree Level Order**
  - Given a binary tree, return its node values level by level. You use a queue to process all nodes at one level before moving to the next, collecting each level into its own list.
- **Maximum Depth of Binary Tree**
  - Given a binary tree, return its maximum depth, meaning the number of nodes along the longest root-to-leaf path. You recursively compute the depth of left and right subtrees and return one plus the greater.
- **Lowest Common Ancestor**
  - Given a BST and two nodes, find their lowest common ancestor. Because it is a BST, you can use the values to decide whether to go left, right, or stop: the ancestor is where the two nodes diverge.
- **Binary Tree Maximum Path Sum**
  - Given a binary tree where nodes can have negative values, find the maximum sum of any path between any two nodes. At each node you decide whether to extend either child's path or start fresh, tracking the global maximum as you go.
- **Serialize and Deserialize**
  - Design an algorithm to convert a binary tree to a string and reconstruct it exactly from that string. One approach uses BFS level-order, encoding null pointers explicitly so the structure can be recovered.
- **More Exercises**
  - Below you can find other popular questions covering Trees. Work through these once you are comfortable with the five above.

### 2.5 Heap / Priority Queue
- **Kth Largest Element in an Array**
  - Given an unsorted array and an integer k, return the kth largest element. You can use a min-heap of size k: iterate through the array, push each element, and pop when the heap exceeds k.
- **K Closest Points to Origin**
  - Given a list of points, return the k closest to the origin. A max-heap of size k keeps the k smallest distances seen so far, ejecting any point farther than the current kth closest as you iterate.
- **Task Scheduler**
  - Given a list of tasks and a cooldown n, find the minimum time needed to finish all tasks, with the constraint that the same task must wait n intervals between executions. A greedy approach with a max-heap always schedules the most frequent remaining task, filling cooldown gaps with other tasks or idle time.
- **Find Median from Data Stream**
  - Design a data structure that supports adding numbers one by one and returning the median at any point. You maintain two heaps: a max-heap for the lower half and a min-heap for the upper half, keeping them balanced so the median is always accessible at the top.
- **Merge K Sorted Lists**
  - Given k sorted linked lists, merge them into one sorted list using a min-heap. You insert the head of each list into the heap, then repeatedly extract the minimum and push the next node from that list.
- **More Exercises**
  - Below you can find other popular questions covering Heap and Priority Queue. Work through these once you are comfortable with the five above.

### 2.6 Backtracking
- **Subsets**
  - Given an array of unique integers, return all possible subsets, including the empty set. You use backtracking to make a binary decision at each element: include it or skip it, building subsets recursively.
- **Combination Sum**
  - Given an array of distinct integers and a target, return all unique combinations that sum to the target, where each number can be used unlimited times. You use backtracking, and at each step either reuse the current number or move to the next.
- **Permutations**
  - Given an array of distinct integers, return all possible orderings. Unlike subsets, order matters here, so at each step you pick any unused element and continue recursively.
- **Word Search**
  - Given a 2D grid of characters and a word, determine if the word exists in the grid by following adjacent cells. You do DFS from each cell that matches the first character, marking visited cells to avoid reuse in the current path.
- **N-Queens**
  - Place n queens on an n by n chessboard so that no two queens attack each other, and return all valid configurations. You place queens row by row and use sets to track which columns and diagonals are occupied, backtracking when a row has no valid placement.
- **More Exercises**
  - Below you can find other popular questions covering Backtracking. Work through these once you are comfortable with the five above.

### 2.7 Tries
- **Implement Trie**
  - Build a trie data structure that supports inserting a word, searching for an exact word, and checking if any word starts with a given prefix. Each node stores a map of child characters and a flag marking word endings.
- **Design Add and Search Words**
  - Build a data structure that supports adding words and searching for words where a dot can match any letter. Exact characters navigate the trie normally, while a dot triggers DFS across all child nodes.
- **Word Search II**
  - Given a board of characters and a list of words, return all words that exist in the board. You build a trie from the word list and do DFS from each cell, pruning paths that do not match any trie prefix.
- **Longest Common Prefix**
  - Given an array of strings, find the longest common prefix among all of them. One approach inserts all strings into a trie and traverses down as long as each node has exactly one child and is not a word end.
- **Replace Words**
  - Given a dictionary of root words and a sentence, replace each word in the sentence with its shortest matching root from the dictionary. You insert all roots into a trie, then for each word in the sentence traverse the trie character by character until you hit a root or fail.
- **More Exercises**
  - Below you can find other popular questions covering Tries. Work through these once you are comfortable with the five above.

### 2.8 Graphs
- **Number of Islands**
  - Given a 2D grid of land and water cells, count the number of islands. You do DFS from each unvisited land cell, marking the entire connected landmass as visited before moving on.
- **Clone Graph**
  - Given a connected undirected graph, return a deep copy of it. You use DFS or BFS and a hash map to track which nodes have already been cloned, so you do not create duplicate copies when revisiting nodes.
- **Pacific Atlantic Water Flow**
  - Given a matrix of heights, find all cells from which water can flow to both the Pacific and Atlantic oceans. You reverse the problem: do BFS inward from each ocean's border, marking all reachable cells, then return cells reachable from both.
- **Course Schedule**
  - Given a list of courses and prerequisites, determine if it is possible to finish all courses. This is a cycle detection problem in a directed graph: if any cycle exists, the schedule is impossible.
- **Word Ladder**
  - Given a start word and an end word, find the shortest transformation sequence where each step changes exactly one letter and every intermediate word must exist in a given word list. BFS gives the shortest path, and each word's neighbors are found by replacing each character with every letter.
- **More Exercises**
  - Below you can find other popular questions covering Graphs. Work through these once you are comfortable with the five above.

---

## 3. Advanced

### 3.1 Advanced Graphs
- **Network Delay Time**
  - Given a network of nodes and weighted directed edges, find the time it takes for a signal to reach all nodes from a source. This is Dijkstra's algorithm: you use a min-heap to always process the closest unvisited node next.
- **Min Cost to Connect All Points**
  - Given a list of points, find the minimum cost to connect all of them, where cost is the Manhattan distance between two points. This is a minimum spanning tree problem solvable with Prim's algorithm using a min-heap, always picking the cheapest edge to an unvisited node.
- **Cheapest Flights Within K Stops**
  - Given a graph of flights with prices, find the cheapest route from source to destination using at most k stops. This is a modified Dijkstra or Bellman-Ford problem where the constraint is on the number of edges, not just total cost.
- **Swim in Rising Water**
  - Given a grid where each cell has a height, find the earliest time t such that you can travel from top-left to bottom-right, moving only through cells with height at most t. You binary search on t or use Dijkstra treating each cell's height as the cost.
- **Reconstruct Itinerary**
  - Given a list of airline tickets, reconstruct the itinerary in lexical order starting from JFK, using all tickets exactly once. You use DFS with a sorted adjacency list and add nodes to the result only after all their outgoing edges are exhausted, which is Hierholzer's algorithm for Eulerian paths.
- **More Exercises**
  - Below you can find other popular questions covering Advanced Graphs. Work through these once you are comfortable with the five above.

### 3.2 1-D Dynamic Programming
- **Climbing Stairs**
  - You can climb one or two steps at a time. Find the number of distinct ways to reach the top of n stairs.
- **House Robber**
  - You are a robber planning to steal from houses in a row. You cannot rob two adjacent houses.
- **Coin Change**
  - Given coin denominations and a target amount, find the minimum number of coins needed. You build a DP table where each amount stores the fewest coins to make it, using each coin to update future amounts.
- **Longest Increasing Subsequ.**
  - Given an array, find the length of the longest strictly increasing subsequence. For each element, you check all previous elements that are smaller and extend the best subsequence ending there.
- **Word Break**
  - Given a string and a dictionary of words, determine if the string can be segmented into a sequence of dictionary words. You use DP where each position stores whether the substring up to that point can be formed, checking every possible last word.
- **More Exercises**
  - Below you can find other popular questions covering 1-D Dynamic Programming. Work through these once you are comfortable with the five above.

### 3.3 2-D Dynamic Programming
- **Unique Paths**
  - A robot starts at the top-left of an m by n grid and can only move right or down. Find the number of unique paths to the bottom-right.
- **Longest Common Subsequence**
  - Given two strings, find the length of their longest common subsequence. If characters match, you extend the LCS from the diagonal; otherwise you take the best from dropping one character in either string.
- **Edit Distance**
  - Given two strings, find the minimum number of insertions, deletions, or replacements to transform one into the other. A 2D DP table tracks the cost to convert each prefix of one string to each prefix of the other.
- **Burst Balloons**
  - Given an array of balloons with values, burst all of them to maximize coins, where bursting a balloon gives coins equal to the product of itself and its neighbors. You use interval DP: instead of choosing which balloon to burst first, you choose which to burst last within each interval.
- **Regular Expression Matching**
  - Given a string and a pattern with dot and star wildcards, determine if the pattern matches the entire string. A 2D DP table tracks whether each prefix of the string matches each prefix of the pattern, with special handling for the star operator.
- **More Exercises**
  - Below you can find other popular questions covering 2-D Dynamic Programming. Work through these once you are comfortable with the five above.

### 3.4 Greedy
- **Jump Game**
  - Given an array where each element is the maximum jump length from that position, determine if you can reach the last index. You track the furthest position reachable so far and update it at each step.
- **Jump Game II**
  - Given the same setup, find the minimum number of jumps to reach the last index. You greedily track the end of the current jump range and the furthest you can reach within it, incrementing the jump count when you exhaust the current range.
- **Gas Station**
  - Given gas amounts and costs at each station on a circular route, find the starting station from which you can complete the circuit. If total gas is at least total cost, a solution exists, and the starting point is always after the last segment where the running tank went negative.
- **Partition Labels**
  - Given a string, partition it into as many parts as possible so that each letter appears in at most one part. You find the last occurrence of each character first, then greedily extend the current partition's boundary as you scan.
- **Non-overlapping Intervals**
  - Given a list of intervals, find the minimum number of intervals to remove so that the rest do not overlap. You sort by end time and greedily keep every interval that does not conflict with the last kept one.
- **More Exercises**
  - Below you can find other popular questions covering Greedy. Work through these once you are comfortable with the five above.

### 3.5 Intervals
- **Merge Intervals**
  - Given a list of intervals, merge all overlapping ones. You sort by start time and iterate, extending the current interval when the next one overlaps, or starting a new one when it does not.
- **Insert Interval**
  - Given a sorted list of non-overlapping intervals and a new interval, insert it and merge any overlaps. You add all intervals that end before the new one starts, merge all that overlap with it, then add the rest.
- **Non-overlapping Intervals**
  - Given a list of intervals, find the minimum number to remove so that no two intervals overlap. Sorting by end time and greedily keeping non-conflicting intervals gives the maximum number you can keep, and the answer is total minus that.
- **Meeting Rooms**
  - Given a list of meeting time intervals, determine if a person can attend all of them. You sort by start time and check if any meeting starts before the previous one ends.
- **Min. Interval to Include Query**
  - Given a list of intervals and queries, for each query find the length of the smallest interval that contains it. You sort both intervals and queries, use a min-heap keyed by interval length, and process queries in order.
- **More Exercises**
  - Below you can find other popular questions covering Intervals. Work through these once you are comfortable with the five above.

### 3.6 Bit Manipulation
- **Single Number**
  - Given an array where every element appears twice except one, find the element that appears only once. XOR of a number with itself is zero, and XOR of a number with zero is the number itself, so XOR-ing all elements cancels duplicates and leaves the unique one.
- **Number of 1 Bits**
  - Given a 32-bit integer, count how many bits are set to 1. You can check the last bit with a bitwise AND and shift right repeatedly, or use the trick n & (n-1) which clears the lowest set bit, counting until n becomes zero.
- **Counting Bits**
  - Given an integer n, return an array where each element is the number of 1 bits in its binary representation from 0 to n. You can use DP: the number of bits in i equals one plus the bits in i with its lowest set bit removed.
- **Reverse Bits**
  - Given a 32-bit unsigned integer, reverse its bits. You build the result bit by bit by extracting the last bit from the input and shifting it into the result.
- **Sum of Two Integers**
  - Calculate the sum of two integers without using the plus or minus operators. XOR gives the sum without carries, and AND shifted left gives the carries.
- **More Exercises**
  - Below you can find other popular questions covering Bit Manipulation. Work through these once you are comfortable with the five above.

### 3.7 Math & Geometry
- **Rotate Image**
  - Given an n by n matrix, rotate it 90 degrees clockwise in place. You first transpose the matrix (swap across the diagonal), then reverse each row.
- **Spiral Matrix**
  - Given an m by n matrix, return all elements in spiral order. You maintain four boundaries (top, bottom, left, right) and peel one layer at a time, moving right, down, left, then up, shrinking the boundaries after each direction.
- **Set Matrix Zeroes**
  - Given a matrix, if any cell is zero, set its entire row and column to zero, in place. The trick is to record which rows and columns need zeroing before making any changes, using the first row and column as markers to avoid extra space.
- **Happy Number**
  - A happy number is one that eventually reaches 1 when you repeatedly replace it with the sum of the squares of its digits. Detect whether a number is happy.
- **Pow(x, n)**
  - Implement the power function that raises x to the nth power, including negative exponents, in O(log n). You use fast exponentiation: square the base and halve the exponent at each step, handling odd exponents by multiplying in an extra factor.
- **More Exercises**
  - Below you can find other popular questions covering Math and Geometry. Work through these once you are comfortable with the five above.

---

## 4. Optional / Specialized Topics

- Top K Frequent Elements
- More Exercises
- Two Sum II
- Largest Rectangle in Hist.
- Median of Two Arrays
- Sliding Window Maximum
- Merge K Sorted Lists
- Serialize and Deserialize
- N-Queens
- Replace Words
- Word Ladder
- Reconstruct Itinerary
- Word Break
- Regular Expression Matching
- Non-overlapping Intervals
- Min. Interval to Include Query
- Sum of Two Integers
- Pow(x, n)

---

## 5. References

- [LeetCode Roadmap](https://roadmap.sh/leetcode)

---

## 6. Related Roles / Topics

### Related Roles
- Software Engineer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Data Structures & Algorithms