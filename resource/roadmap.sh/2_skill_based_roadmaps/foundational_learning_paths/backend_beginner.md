# Backend Beginner

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/backend-beginner
- Related Roles:
  - Software Engineer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Pick a Language
- **Go**
  - Go (Golang) is Google's statically typed, compiled language combining efficiency with ease of use. Features built-in concurrency via goroutines and channels, simple syntax, fast compilation, and a comprehensive standard library.
- **JavaScript**
  - JavaScript is a versatile, high-level language for web interactivity and dynamic features. Runs client-side in browsers and server-side with Node.js for full-stack development.
- **Python**
  - Python is a popular programming language that is easy to learn and read. It is used for building web applications, analyzing data, automating tasks, and creating intelligent systems.

### 1.2 Version Control Systems
- **Git**
  - Git is a distributed version control system used to track changes in source code during software development. It enables multiple developers to collaborate on a project by managing versions of code, allowing for branching, merging, and tracking of revisions.

---

## 2. Intermediate

### 2.1 Repo hosting services
- **Github**
  - GitHub is a web-based platform built on top of Git that provides version control, collaboration tools, and project management features for software development. It enables developers to host Git repositories, collaborate on code through pull requests, and review and track changes.

### 2.2 Relational Databases
- **PostgreSQL**
  - PostgreSQL is an advanced, open-source RDBMS known for robustness, extensibility, and standards compliance. Supports complex queries, custom data types, full-text search, and ACID properties.

### 2.3 Learn about APIs
- **JSON APIs**
  - JSON (JavaScript Object Notation) is an encoding scheme eliminating ad-hoc code for server communication. JSON API provides a standardized implementation for data stores and structures, including entity types, bundles, and fields with defined communication protocols.
- **REST**
  - REST API is an architectural style using standard HTTP methods (GET, POST, PUT, DELETE) to interact with URI-represented resources. It's stateless, requiring complete request information, uses HTTP status codes, and typically communicates via JSON/XML.
- **Authentication**
  - API authentication verifies client identity to ensure only authorized access to resources. Common methods include API keys, OAuth 2.0, JWT, and basic auth.

---

## 3. Advanced

### 3.1 Caching
- **Redis**
  - Redis is an open-source, in-memory data structure store supporting strings, lists, sets, hashes, and sorted sets. Used for caching, session management, real-time analytics, and message brokering.
- **JWT**
  - JWT (JSON Web Token) securely transmits information as JSON objects with three parts: header (token type/algorithm), payload (claims/data), and signature (integrity verification). Used for authentication and authorization in web/mobile apps.

### 3.2 More about Databases
- **ORMs**
  - ORM (Object-Relational Mapping) allows developers to interact with databases using object-oriented concepts. Maps database tables to classes and rows to objects, eliminating raw SQL queries.
- **ACID**
  - ACID represents four database transaction properties: Atomicity (all-or-nothing execution), Consistency (valid state maintenance), Isolation (concurrent transaction separation), and Durability (permanent commit survival). These principles ensure reliable data processing and integrity in database systems, crucial for financial and e-commerce applications.
- **Transactions**
  - Database transactions are a series of operations executed as atomic units to ensure data integrity. Follow ACID properties: Atomicity (all-or-nothing), Consistency (valid state), Isolation (no interference), Durability (permanent changes).
- **N+1 Problem**
  - The N+1 problem occurs when an application retrieves a list then performs additional queries for each item's related data. Results in inefficient query multiplication (1 + N queries instead of optimized joins).

### 3.3 Testing
- **Integration Testing**
  - Integration testing verifies interactions between software components to ensure they work together correctly. Tests module communication via APIs, databases, and third-party services.
- **Functional Testing**
  - Functional testing ensures software meets functional requirements through black box testing. Testers provide input and compare expected vs actual output without understanding the source code.
- **Unit Testing**
  - Unit testing tests individual components or units in isolation to ensure correct functionality. Focuses on the smallest testable parts like functions with predefined inputs and expected outcomes.

---

## 4. Optional / Specialized Topics

- Go
- Python

---

## 5. References

- [Backend Beginner Roadmap](https://roadmap.sh/backend-beginner)

---

## 6. Related Roles / Topics

### Related Roles
- Software Engineer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Git & GitHub
- System Design
- Docker
- Linux
- Testing