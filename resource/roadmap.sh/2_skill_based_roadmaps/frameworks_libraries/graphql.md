# GraphQL

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/graphql
- Related Roles:
  - Frontend Developer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is GraphQL**
  - GraphQL is a query language for APIs and server-side runtime that lets clients request exactly the data they need. Unlike REST, it uses a type system to define data structure and allows fetching multiple resources in a single request, reducing over-fetching and under-fetching problems.
- **Problems GraphQL Solves**
  - GraphQL solves major API problems including over-fetching (getting unnecessary data), under-fetching (multiple requests needed), inefficient versioning, and lack of flexibility. It enables precise data requests, single queries for multiple resources, seamless versioning through schema evolution, and microservice communication through federation.
- **Thinking in Graphs**
  - "Thinking in Graphs" is a GraphQL mindset where data is organized as a graph with nodes (objects) and edges (relationships). This approach allows flexible and intuitive querying by following relationships between connected data points, making complex data retrieval more natural and efficient.
- **GraphQL on Frontend**
  - GraphQL on the frontend enables efficient data fetching with clients like Apollo, URQL, or Relay. It provides declarative data requirements, intelligent caching, real-time subscriptions, and type safety, allowing frontend applications to request exactly the data they need in a single query.
- **GraphQL on Backend**
  - GraphQL on the backend involves implementing servers that execute GraphQL queries, mutations, and subscriptions. It includes defining schemas, writing resolvers, handling data sources, implementing authentication/authorization, and optimizing performance through caching and batching strategies.

### 1.2 GraphQL Queries
- **What are Queries?**
  - In GraphQL, queries are client requests to retrieve data from the server. They're structured as hierarchical trees of fields that correspond to the properties of the requested data, allowing clients to specify exactly what data they need in a predictable format.
- **Fields**
  - Fields in GraphQL are individual pieces of data that can be queried or modified, representing properties of the requested data. They're defined in the GraphQL schema and serve as building blocks for queries and mutations, specifying what data is available for each type.
- **Aliases**
  - Aliases in GraphQL rename fields in query responses, useful when requesting the same field multiple times with different arguments or when field names aren't suitable for client usage. They distinguish fields in responses and improve query readability and usability.
- **Arguments**
  - Arguments in GraphQL are values passed to fields or directives to specify execution details like filtering, sorting, pagination, or configuration options. They're passed as key-value pairs, can be defined as variables, and may be optional or required depending on the field definition.
- **Directives**
  - Directives in GraphQL modify query execution by adding behavior or validation to fields, operations, and fragments. They can take arguments to configure behavior and include built-in directives like @include and @skip, or custom ones defined by developers for specific functionality.
- **Variables**
  - Variables in GraphQL pass dynamic values to queries and mutations, making them flexible and reusable. Defined with the $ symbol and a type, their values are passed in a separate JSON object.
- **Fragments**
  - Fragments in GraphQL are reusable pieces of queries that retrieve specific fields from one or more types. Defined with the "fragment" keyword, they promote code reuse, reduce duplication, and make complex queries more maintainable by separating common field selections.

### 1.3 Mutations
- **What are Mutations?**
  - Mutations in GraphQL are operations used to modify data on the server - creating, updating, or deleting records. They're structured like queries but use the "mutation" field at the top level and include fields specifying the data to be changed and the operation type.
- **Multiple Fields in Mutation**
  - GraphQL allows multiple mutations in a single query by including multiple mutation fields, a practice often called batching mutations. This approach improves network efficiency by reducing the number of round-trips between the client and server.
- **Operation Name**
  - Operation names are optional identifiers for GraphQL queries and mutations that help uniquely identify operations in documents with multiple operations. They provide meaningful names for operations, improve debugging, and make error identification easier in complex applications.

---

## 2. Intermediate

### 2.1 Subscriptions
- **What are Subscriptions**
  - Subscriptions in GraphQL enable real-time updates by allowing clients to subscribe to specific events or data changes on the server. They're structured like queries with a "subscription" field at the top level and push updates to clients as soon as events occur.
- **Event Based Subscriptions**
  - Event-based subscriptions in GraphQL provide real-time updates by subscribing to specific events or data changes. Clients maintain persistent connections through WebSockets to receive live updates when subscribed events occur, enabling reactive applications with real-time functionality.
- **Live Queries**
  - Live Queries automatically update query results when underlying data changes, providing real-time synchronization without manual subscription management. This advanced feature simplifies building reactive applications by maintaining fresh data automatically, though it requires specialized GraphQL implementations.
- **@defer / @stream directives**
  - Defer and Stream directives are experimental GraphQL features for incremental data delivery. @defer postpones non-critical fields to improve initial response times, while @stream sends list items progressively, enabling better user experiences with large datasets and slow-loading fields.
- **Type System**
  - GraphQL is strongly typed with a type system that defines data types available in applications. It includes Scalar, Object, Query, Mutation, and Enum types.
- **Fields**
  - Fields in GraphQL are units of data that can be queried or manipulated. Each field has a name, type, and optional description, and can return scalar values or objects, enabling complex nested data structures and taking arguments for filtering.

### 2.2 Schema
- **Scalars**
  - Scalars are "leaf" values in GraphQL representing primitive data types. Built-in scalars include String, Int, Float, Boolean, and ID for unique identifiers.
- **Enums**
  - Enums (enumeration types) are special scalars restricted to a particular set of allowed values. They validate arguments against allowed values and communicate through the type system that fields will always be one of a finite set of predefined options.
- **Objects**
  - Objects in GraphQL are types that represent groups of fields, defining the structure of queries and mutations. Each field can return scalar values or other objects, enabling complex nested data structures.

### 2.3 Validation
- **Interfaces**
  - Interfaces in GraphQL define a set of fields that implementing types must include. They enable polymorphism by allowing common field querying across different types that implement the same interface, promoting code reuse and consistent API design.
- **Lists**
  - Lists in GraphQL represent ordered collections of items, defined using square brackets around the item type. They can contain scalars, objects, or other lists, enabling complex nested data structures and array-based field returns in schemas.
- **Unions**
  - Unions allow fields to return multiple types, enabling different handling for various types in clients. They provide schema flexibility by grouping types together, though they don't allow common field querying across types like interfaces do.
- **Arguments**
  - Arguments in GraphQL are values passed to fields in queries and mutations to filter or modify returned data. They're defined in the schema with a name, type, and optional default value, enabling dynamic data retrieval.
- **Root Fields**
  - Root fields are the top-level fields available to clients in GraphQL queries and mutations. They serve as entry points for client requests, with Query fields for retrieving data and Mutation fields for modifying data on the server.
- **Resolvers**
  - Resolvers are functions responsible for fetching data for each field in GraphQL queries and mutations. Defined in the schema and executed by the GraphQL server, they retrieve data from databases, APIs, or other sources and return it to clients.

### 2.4 Execution
- **Synchronous**
  - Synchronous resolvers in GraphQL execute immediately and return their results directly without waiting for external operations. They complete their execution before returning any value, making them simpler but potentially blocking if they perform complex computations.
- **Asynchronous**
  - Asynchronous resolvers in GraphQL are functions that return promises instead of immediate values. They allow resolvers to wait for external operations like database queries or API calls to complete before returning results, enabling non-blocking execution.
- **Scalar Coercion**
  - Scalar coercion in GraphQL converts input values from one type to another when they don't match the expected type but can be successfully converted. This process is implemented using custom scalar types with coerce functions that handle the type conversion.
- **GraphQL Over HTTP Spec**
  - The GraphQL over HTTP specification defines standard practices for serving GraphQL over HTTP, including request/response formats, status codes, and content types. It ensures interoperability between different GraphQL implementations and provides guidance for consistent API behavior across platforms.

---

## 3. Advanced

### 3.1 Serving over Internet
- **Lists**
  - Lists in GraphQL represent ordered collections of items and can be used as return types for fields. They can contain any type of items including scalars and objects, with resolver functions typically returning data as arrays from databases or APIs.
- **Validation**
  - Validation in GraphQL ensures queries and mutations adhere to schema rules by verifying field access, type correctness, and input constraints. GraphQL servers validate all incoming operations before execution, returning errors for invalid queries with specific details about violations.
- **Caching**
  - Caching in GraphQL improves performance by storing query results for reuse. Strategies include HTTP caching, response caching, dataloader for batching requests, and normalized caching at the client level to reduce redundant API calls and improve user experience.
- **Batching**
  - Batching in GraphQL combines multiple queries into a single request to reduce network overhead and improve performance. DataLoader is a common pattern that batches and caches database requests, preventing N+1 query problems and optimizing data fetching efficiency.
- **Authorization**
  - Authorization in GraphQL over HTTP determines whether a client has the necessary permissions to access specific data or perform requested operations. This process typically occurs at the resolver level, where the server evaluates the user's identity and roles against the requested fields before returning any information.

### 3.2 Pagination
- **Producing the Result**
  - Producing the result in GraphQL involves generating the final response to queries and mutations. This process includes parsing the request, validating against the schema, executing resolvers to fetch data, and formatting the response according to the query requirements.
- **Specification**
  - The GraphQL specification is the official standard that defines the GraphQL query language, type system, execution algorithm, and validation rules. It ensures consistency across different GraphQL implementations and serves as the authoritative reference for developers building GraphQL services and tools.
- **Realtime**
  - Realtime GraphQL enables live data updates through subscriptions, allowing clients to receive instant notifications when data changes. Implemented using WebSockets, Server-Sent Events, or polling, it's essential for chat applications, live feeds, and collaborative tools requiring immediate data synchronization.
- **Authorization**
  - Authorization in GraphQL over WebSockets involves validating that a client has the necessary permissions to maintain a persistent connection and receive specific real-time updates. Since standard HTTP headers are typically only sent during the initial handshake, authorization is often handled during the connection initialization phase by passing authentication tokens through connection parameters.
- **GraphQL.js**
  - GraphQL.js is the reference implementation of GraphQL for JavaScript and Node.js. It provides the core functionality for parsing, validating, and executing GraphQL queries, serving as the foundation for many other GraphQL tools and libraries in the JavaScript ecosystem.
- **GraphQL Go**
  - GraphQL Go refers to implementing GraphQL servers and clients using the Go programming language. Popular libraries include graphql-go/graphql for schema-first development and 99designs/gqlgen for code-first generation.
- **GraphQL Java**
  - GraphQL Java is a popular library for implementing GraphQL APIs in Java applications. It provides schema-first development capabilities, runtime query execution, and integrates well with Spring Boot and other Java frameworks, making it a solid choice for enterprise GraphQL implementations.
- **graphql-http**
  - GraphQL over HTTP is a specification that defines how GraphQL queries and mutations should be transported over HTTP. It standardizes request/response formats, HTTP methods, status codes, and headers, ensuring consistent GraphQL API communication across different implementations.
- **GraphQL Yoga**
  - GraphQL Yoga is an open-source GraphQL server library for Node.js built on Express.js. It provides minimal boilerplate setup with built-in authentication, authorization, data validation, and subscription support for real-time updates, making GraphQL server development streamlined.
- **Apollo Server**
  - Apollo Server is a popular open-source library for building GraphQL servers in JavaScript. It provides tools for parsing, validating, executing resolvers, and formatting responses with built-in features for authentication, authorization, data validation, and real-time subscriptions.
- **mercurius**
  - Mercurius is a high-performance GraphQL server library for Fastify, offering excellent performance and minimal memory usage. It provides schema-first development, built-in caching, subscriptions support, and integration with Fastify's ecosystem for building fast, scalable GraphQL APIs.
- **Relay**
  - Relay is Facebook's GraphQL client designed for React applications, emphasizing performance and data consistency. It uses a declarative approach with fragments, automatic query optimization, pagination handling, and strict conventions for building scalable, efficient GraphQL applications.
- **Apollo Client**
  - Apollo Client is a popular GraphQL client library for JavaScript that provides data fetching, caching, and state management. It offers declarative data fetching with React hooks, intelligent caching, optimistic UI updates, and error handling for building efficient GraphQL-powered applications.
- **Urql**
  - URQL is a lightweight, highly customizable GraphQL client for React, Vue, and Svelte. It provides caching, real-time subscriptions, offline support, and a modular architecture with exchanges for extending functionality, offering an alternative to Apollo Client with better performance.
- **Graphene**
  - Graphene is a Python library that facilitates building GraphQL APIs. It allows developers to define GraphQL schemas using Python classes, mapping these classes to data sources and resolvers.

---

## 4. Optional / Specialized Topics

- GraphQL on Backend
- Directives
- Variables
- Fragments
- Type System
- Fields
- Root Fields
- Resolvers
- Authorization
- GraphQL.js
- GraphQL Go
- GraphQL Java
- graphql-http
- GraphQL Yoga
- Apollo Server
- mercurius
- Relay
- Apollo Client
- Urql
- Graphene

---

## 5. References

- [GraphQL Roadmap](https://roadmap.sh/graphql)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Backend Developer

### Related Skills
- Node.js
- JavaScript
- React
- Vue.js
- Angular