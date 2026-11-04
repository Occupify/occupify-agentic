# Rust

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/rust
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **What is Rust?**
  - Rust is a modern system programming language focused on performance, safety, and concurrency. It accomplishes these goals without having a garbage collector, making it a useful language for a number of use cases other languages aren’t good at.
- **Why use Rust?**
  - Rust is a system programming language that aims to provide memory safety, concurrency, and performance with a focus on zero cost abstractions. It was originally created by Graydon Hoare at Mozilla Research, with contributions from Brendan Eich, the creator of JavaScript.
- **Installing Rust and Cargo**
  - To install Rust, navigate to the rust official website and download the appropriate installation file (or run the appropriate terminal command) for your operating system. You'll be installing rustup, which is the preferred tool for installing, updating, and managing your core Rust tooling.
- **Variables, DataTypes and Constants**
  - In Rust, variables are declared using the let keyword. All variables are immutable by default, which means once a value is bound to a variable, it cannot be changed.
- **Control Flow and Constructs**
  - In Rust, control flow is managed through various structures, like if, else, while, for, loop, match and if let. The if and else structures are used to execute different blocks of code based on certain conditions.

### 1.2 Language Basics
- **IDEs and Rust Toolchains**
  - For the Rust Programming Language, several Integrated Development Environments (IDEs) and editors provide great support. Visual Studio Code is highly preferred among Rust developers due to its support for Rust via the "Rust Language Server" or "rust-analyzer" plugins.
- **Rust REPL (Rust Playground)**
  - Rust REPL (Read-Eval-Print-Loop) is an interactive shell in which you can write and test Rust snippets in real-time. Unlike running a program normally in Rust where you have to manually compile and then run the program, REPL automatically evaluates your inputs, and the result is returned immediately after execution.
- **Functions and Method Syntax**
  - In Rust, functions are declared using the fn keyword. Each function can take a set of input variables with their specified types, and may return data of a specified type.
- **Pattern Matching & Destructuring**
  - In Rust, "pattern matching" is a robust tool that allows you to destructure data types and perform conditional checks in a succinct and clear way. The main structures used for pattern matching are match and if let.

### 1.3 Error Handling
- **Enums**
  - An enum, short for enumeration, is a custom data type that allows you to define a type by enumerating (listing out one-by-one) all of its possible variants. In Rust, if something is one of a given set of possibilities (e.g., Rock or Paper or Scissors), it's probably appropriate to represent that data with an enum, like so: enum RpsChoice { Rock, Paper, Scissors }.
- **Structs**
  - In Rust, a struct is a custom data type used for grouping related values together into one entity. Structs are similar to classes in other programming languages.
- **Traits**
  - Traits in Rust define behaviors that are shared among different data types. Implementing traits for data types is a great way to group method signatures together and define a set of behaviors your types require.
- **Impl Blocks**
  - Impl blocks use the impl keyword, and are used to implement behavior in the form of methods for a struct, enum, or trait. If you want your data type or trait to have methods, you need a corresponding impl block containing functions for the type or trait.
- **Option and Result Enumerations**
  - Option<T> handles nullable values with Some(T) and None variants, replacing null pointers safely. Result<T, E> manages error handling with Ok(T) for success and Err(E) for failures.
- **Propagating Errors and `?` Operator**
  - The ? operator provides concise error propagation in functions returning Result or Option.
- **Custom Error Types and Traits**
  - Custom error types use enum to define specific error variants with attached data. Implement Debug, Display, and optionally std::error::Error traits for proper error handling integration.

### 1.4 Modules & Crates
- **Integers**
  - In Rust, integers are a primitive data type that hold whole number values, both positive and negative. Integer types in Rust can be divided into signed and unsigned ones:
- **Boolean**
  - Rust's bool primitive type represents truth values with two possible states: true or false. Booleans are used in conditional statements and logical operations like && (AND), || (OR), and !
- **Floats**
  - In Rust, floats are a primitive data types used to represent floating-point numbers. They are defined as numerical values with fractional components.
- **Character**
  - Rust's char type represents a Unicode Scalar Value, supporting far more than ASCII including emojis, accented letters, and various scripts. Each char occupies 4 bytes (32 bits) in memory and is defined using single quotes.
- **Tuple**
  - Tuples are fixed-size collections that can hold elements of different types. Access elements using dot notation with zero-based indexing: tuple.0, tuple.1, etc.
- **String**
  - Rust's String is a growable, mutable, UTF-8 encoded string type stored on the heap. Unlike string slices (&str), String owns its data and can be modified.
- **Array**
  - Arrays are fixed-size collections of elements of the same type stored consecutively in memory. Size must be known at compile time and cannot change.
- **Hashmap**
  - HashMap<K, V> stores key-value pairs using hashing for fast lookups, insertions, and removals. Keys must be unique; duplicate keys replace old values.
- **Vector**
  - Vec<T> is Rust's growable, heap-allocated array that stores elements of the same type contiguously. Unlike arrays, vectors can resize at runtime.
- **Hashset**
  - HashSet<T> is a collection of unique elements using hash-based storage for fast lookups, insertions, and deletions. No duplicates are allowed and elements are unordered.
- **LinkedList**
  - LinkedList<T> is a doubly-linked list where each node contains a value and pointers to both next and previous nodes. Provides O(1) insertion/removal at both ends but O(n) indexing.
- **Stack**
  - Stack is a LIFO (Last-In-First-Out) data structure where elements are added and removed from the same end. In Rust, the call stack manages function calls, with each call pushing a frame and returns popping it.
- **Code Organization & Namespacing**
  - Rust organizes code through modules (mod) for grouping related functionality and crates (binary/library projects). Modules provide namespacing and can be nested.
- **Dependency Management with Cargo**
  - Cargo manages Rust projects and dependencies through Cargo.toml files. Dependencies are listed in [dependencies] sections with crate names and semantic version specifications.
- **Publishing on Crates.io**
  - Publishing Rust crates involves creating an account on crates.io, preparing proper Cargo.toml metadata, and using cargo publish. Once published, versions cannot be deleted or overwritten, ensuring dependency stability.

### 1.5 Testing
- **Queue**
  - Queue follows FIFO (First-In-First-Out) ordering where elements are added at one end and removed from the other. Rust doesn't have a built-in queue, but VecDeque provides queue functionality with pushback() for adding and popfront() for removing elements efficiently.
- **Binary Heap**
  - BinaryHeap<T> is a priority queue implemented as a max-heap using a binary tree structure stored in an array. The largest element is always at the root, accessible via peek().
- **Ownsership Rules & Memory Safety**
  - Rust's ownership has three key rules: each value has exactly one owner, only one owner exists at a time, and values are dropped when owners go out of scope. This prevents data races, ensures memory safety without garbage collection, and eliminates common bugs like use-after-free and memory leaks.
- **Borrowing, References and Slices**
  - Borrowing allows accessing data without taking ownership. Immutable borrows (&T) permit multiple read-only references, while mutable borrows (&mut T) allow one exclusive reference that can modify data.
- **Deep Dive: Stack vs Heap**
  - Stack memory stores fixed-size data with automatic allocation/deallocation following LIFO order - fast but limited. Heap memory stores dynamic-size data with manual management - slower but flexible.
- **BTreeMap**
  - BTreeMap<K, V> stores key-value pairs in a sorted binary tree structure. Keys must implement Ord trait and are automatically kept in sorted order.
- **BTreeSet**
  - BTreeSet<T> is a sorted set of unique elements implemented using a B-tree. Elements must implement Ord trait and are kept in sorted order.
- **Mutex**
  - Mutex<T> (Mutual Exclusion) protects shared data from concurrent access by multiple threads. Only one thread can access the protected data at a time through lock().
- **Unit & Integration Testing**
  - Unit tests verify individual functions using #[test] and live alongside code. Integration tests are in separate files/directories and test component interactions.
- **Mocking & Property Based Testing**
  - Mocking creates fake functions/objects for testing different scenarios. Rust uses external libraries like mockito, mockall, and mockalldouble for mocking capabilities.

### 1.6 Concurrency & Parallelism
- **Threads, Channels and Message Passing**
  - Rust provides native threading with std::thread::spawn() and join() for 1:1 OS thread mapping. Channels enable safe message passing between threads, avoiding shared state issues.
- **Atomic Operations & Memory Barriers**
  - Atomic operations provide lock-free concurrency through uninterruptible operations like load, store, swap, and compareandswap. These low-level primitives enable thread-safe data sharing without locks, forming the foundation for higher-level concurrent abstractions and non-blocking data structures.
- **Futures and Async/Await Paradigm**
  - Futures represent asynchronous computations that produce values or errors eventually. The async/await syntax provides ergonomic programming over futures, allowing asynchronous code to look synchronous.

### 1.7 Traits & Generics
- **RC**
  - Rc<T> (Reference Counting) enables multiple owners of the same heap-allocated data in single-threaded contexts. It tracks the number of references and automatically deallocates data when the count reaches zero.
- **Arc**
  - Arc<T> (Atomic Reference Counting) is a thread-safe smart pointer for sharing immutable data across multiple threads. It uses atomic operations to track reference counts, allowing multiple ownership of heap-allocated data.
- **RwLock**
  - RwLock<T> (Read-Write Lock) allows multiple concurrent readers OR one exclusive writer, unlike Mutex which allows only one accessor. Use read() for shared access and write() for exclusive access.
- **Channels**
  - Channels enable thread communication via message passing from std::sync::mpsc (Multiple Producer, Single Consumer). They have Sender for sending data and Receiver for receiving.
- **Trait Definitions & Implementations**
  - Traits define shared behavior as a set of method signatures that types can implement. Define with trait Name { fn method(&self); } and implement with impl TraitName for Type.
- **Trait Bounds and Associated Types**
  - Trait bounds constrain generics by requiring types to implement specific traits (T: Display). Associated types define type placeholders within traits that implementors must specify.
- **Generics & Type-Level Programming**
  - Advanced generics in Rust include where clauses for complex bounds, ?Sized for unsized types, associated types, and higher-kinded types. These enable sophisticated type-level programming, allowing precise control over generic constraints and enabling powerful abstractions while maintaining zero-cost performance.
- **Box**
  - A Box in Rust is a smart pointer that allocates memory on the heap. It's primarily used to store data that has a size that's not known at compile time, or when you want to transfer ownership of data without copying it.

---

## 2. Intermediate

### 2.1 Lifetimes & Borrow Checker
- **Explicit Lifetime Annotations**
  - Explicit lifetime annotations use syntax like 'a to specify relationships between reference lifetimes in function signatures. Required when the compiler can't infer lifetimes automatically.
- **Lifetime Elision Rules**
  - Lifetime elision allows the compiler to infer lifetimes in common patterns, reducing explicit annotations. Rules: each reference parameter gets its own lifetime, single input lifetime applies to all outputs, methods with &self propagate its lifetime to outputs.
- **Covariant & Contravariant Lifetimes**
  - Variance describes how subtyping relationships change when types are nested. Covariant types preserve ordering (&'long T is subtype of &'short T), contravariant reverses it, invariant requires exact matches.

### 2.2 Macros & Metaprogramming
- **Declarative Macros with macro_rules!**
  - Declarative macros use macrorules! for pattern-based code generation at compile time.
- **Procedural Macros & Custom Derive**
  - Procedural macros operate on token streams at compile time, generating new code. Three types exist: custom derive (for #[derive(MyTrait)]), attribute-like (#[myattr]), and function-like (mymacro!()).
- **Domain Specific Languages (DSLs)**
  - DSLs are specialized programming languages for specific domains. Rust macros enable creating DSLs by manipulating syntax trees and defining custom syntax patterns.

### 2.3 Web Development
- **Axum**
  - Axum is a modern, ergonomic web framework built on hyper and designed for async Rust. It features excellent type safety, powerful extractors, middleware support, and seamless Tokio integration.
- **Leptos**
  - Leptos is a rust based web framework that lets you build reactive UIs with Rust and WebAssembly. It supports SSR and CSR, fine-grained reactivity, and a rich ecosystem of libraries and tools.
- **Rocket**
  - Rocket is a web framework for Rust emphasizing ease of use, expressiveness, and type safety. It features code generation via procedural macros, built-in templating, request guards, and comprehensive error handling.

### 2.4 Asynchronous Programming
- **Tokio**
  - Tokio is Rust's most popular async runtime for building fast, reliable network applications. It provides an async/await runtime, I/O drivers, timers, and networking primitives.
- **async-std**
  - async-std provides an asynchronous version of Rust's standard library, offering familiar APIs for async programming. It includes its own runtime, task scheduler, and async I/O primitives, designed as a drop-in replacement for std with async capabilities and intuitive syntax.

### 2.5 Networking
- **Actix**
  - Actix is a high-performance, pragmatic web framework for Rust built on the actor model. It features powerful middleware, WebSocket support, and excellent performance benchmarks.
- **Loco**
  - Loco is a web framework for Rust that is inspired by Ruby on Rails, designed to help developers build MVC-style applications easily. It emphasizes simplicity, rapid development, and integrates features like ORM, background jobs, and templating engines for a productive coding experience.
- **smol**
  - smol is a small, fast async runtime for Rust with minimal API and clean design. Built on async-std and Tokio, it supports async/await natively with efficient scheduling.
- **reqwest**
  - reqwest is a popular HTTP client library for Rust that provides both sync and async APIs for making HTTP requests. Built on hyper and tokio, it supports JSON, forms, cookies, and various authentication methods with an ergonomic, easy-to-use interface for web API interactions.
- **hyper**
  - Hyper is a fast, safe HTTP client/server library for Rust built on Tokio for async I/O. It supports HTTP/1 and HTTP/2 with automatic protocol negotiation.
- **quinn**
  - Quinn is a high-performance QUIC protocol implementation for Rust built on Tokio. QUIC is a modern transport protocol offering better performance than TCP with multiplexing and security.

### 2.6 Serialization / Deserialization
- **Serde**
  - Serde is Rust's most popular serialization framework for converting data structures to/from formats like JSON, YAML, TOML, and Binary. It provides Serialize and Deserialize traits with derive macros for automatic implementation.
- **json-rust**
  - JSON handling in Rust primarily uses serde and serdejson libraries for high-performance serialization/deserialization. These provide seamless conversion between Rust data structures and JSON, with parsing from strings/files, serialization to JSON, and direct manipulation of JSON values.
- **toml-rust**
  - toml-rs parses and serializes TOML (Tom's Obvious, Minimal Language) configuration files in Rust. Uses serde for automatic serialization/deserialization between TOML and Rust types.

### 2.7 Database and ORM
- **Diesel**
  - Diesel is a safe, extensible ORM and query builder for Rust that provides compile-time guarantees against SQL injection and type mismatches. It supports PostgreSQL, MySQL, and SQLite with high-level APIs for database operations while maintaining excellent performance and type safety.
- **sqlx**
  - SQLx is an async, pure-Rust SQL toolkit providing compile-time query checking for PostgreSQL, MySQL, SQLite, and MSSQL. It features macro-based query validation, strong typing, and compatibility with Tokio/async-std runtimes.
- **rusqlite**
  - rusqlite is an ergonomic SQLite library for Rust built around the sqlite3 C library. It provides simple, efficient database operations with minimal SQL knowledge required.

### 2.8 Cryptography
- **rust-crypto**
  - rust-crypto is a collection of cryptographic algorithms implemented in pure Rust including AES, DES ciphers, SHA, MD5 hash functions, and RSA digital signatures. Known for speed and low memory usage, making it suitable for resource-constrained systems requiring cryptographic functionality.
- **sodiumoxide**
  - sodiumoxide is a Rust binding to libsodium cryptography library, designed for easy use and misuse prevention. Provides safe, high-level, idiomatic Rust wrappers for cryptographic primitives with automatic error handling.
- **ring**
  - ring is a safe, fast cryptography library for Rust focused on TLS and core cryptographic primitives. It includes RSA, AES, SHA, and other algorithms with compile-time and runtime safety checks.

### 2.9 CLI Utilities
- **clap**
  - clap is Rust's most popular command-line argument parser library. It provides declarative CLI definition with automatic help generation, subcommands, validation, and error handling.
- **structopt**
  - StructOpt is a library for parsing command-line arguments by defining structs where fields represent flags, options, and arguments. Combines clap's parsing power with Rust's type system for declarative CLI definition with automatic help generation, strong typing, and validation.
- **termion**
  - termion is a pure Rust, zero-dependency library for low-level terminal manipulation and information handling. Provides cross-terminal compatibility with features like color support, input handling, and terminal-specific capabilities.

---

## 3. Advanced

### 3.1 Game Development
- **bevy**
  - Bevy is a modern, data-driven game engine built in Rust featuring an ECS (Entity Component System) architecture. It supports both 2D and 3D games with modular design, custom shaders, and high performance.
- **fyrox**
  - Fyrox is a modern, highly optimized 3D game engine designed specifically for Rust. Leverages Rust's safety and concurrency for high performance and reliability.
- **ggez**
  - ggez is a lightweight 2D game framework for Rust inspired by Love2D. Provides facilities for graphics rendering, input handling, audio manipulation, and game timing with an easy, Rusty interface.
- **macroquad**
  - Macroquad is a simple, cross-platform 2D game engine for Rust focusing on rapid prototyping and development. Features efficient rendering via miniquad, input handling, coroutine-based async programming, and sound support.
- **wgpu-rs**
  - wgpu-rs provides safe, idiomatic Rust graphics programming by abstracting over wgpu-core. Offers high-level convenience with low-level control options.

### 3.2 GUI Development
- **tauri**
  - Tauri is a framework for building lightweight, secure desktop applications using web technologies (HTML, CSS, JS) with a Rust backend. It offers smaller bundle sizes than Electron, enhanced security, and cross-platform support for Windows, macOS, and Linux with native system integration.
- **gtk-rs**
  - gtk-rs provides Rust bindings for GTK+3 and related libraries (GObject, Glib, Cairo, Pango) enabling cross-platform GUI application development. These open-source libraries offer a Rust-friendly interface for GTK components, allowing developers to create graphical applications using Rust with native GTK functionality.
- **Iced**
  - Iced is a cross-platform GUI library for Rust that focuses on simplicity and type safety. Inspired by the Elm architecture, it uses a functional approach where the application state is updated through messages, making it easy to create reactive and predictable user interfaces.
- **GPUI**
  - GPUI is a high-performance, native GUI framework written in Rust, designed to enable the creation of responsive and visually appealing desktop applications. It uses a retained-mode rendering approach, where the framework manages and optimizes the drawing of UI elements based on their state, allowing for smooth animations and efficient updates.

### 3.3 Embedded and Systems
- **embedded-hal**
  - embedded-hal (Hardware Abstraction Layer) provides generic traits for creating portable embedded drivers in Rust. Enables hardware-agnostic code by abstracting digital I/O, UART, I2C, SPI, and other communication protocols into a uniform API, promoting code reuse across different hardware platforms.
- **rppal**
  - RPPAL (Raspberry Pi Peripheral Access Library) provides Rust access to Raspberry Pi GPIO, I2C, PWM, SPI, and UART peripherals. Features comprehensive interrupt handling, software-based PWM, and I2C/SPI buses.
- **nrf-hal**
  - nrf-hal is a Rust Peripheral Access Crate for Nordic Semiconductor nRF52 and nRF91 series chips. Provides high-level, semantic interfaces for GPIO, timers, RNG, RTC, I2C/SPI, temperature sensors, and delay routines.

### 3.4 WebAssembly (WASM)
- **wasm-bindgen**
  - wasm-bindgen facilitates high-level interactions between Rust and JavaScript in WebAssembly. It generates bindings allowing seamless communication, JavaScript API calls from Rust, and vice versa.
- **wasm-pack**
  - wasm-pack is a command-line tool for assembling and packaging Rust crates targeting WebAssembly. It bridges Rust/WASM and JavaScript, generating necessary files for npm publishing.
- **wasmer**
  - Wasmer is a standalone WebAssembly runtime designed to run WASM files on any platform quickly and efficiently. Features a pluggable system with different compiling strategies, friendly CLI, and embedding APIs for calling WASM functions directly from various programming languages.

### 3.5 Debugging
- **rust-gdb**
  - rust-gdb is GDB (GNU Project debugger) enhanced for Rust debugging. It provides low-level debugging capabilities including breakpoints, execution tracing, runtime modification, and memory inspection.
- **rust-lldb**
  - rust-lldb is LLDB debugger enhanced with Rust-specific modifications for understanding Rust data structures and concepts. It includes pretty-printers for standard library types and comes bundled with the Rust compiler, providing better debugging experience for Rust applications.

### 3.6 Documenting with `rustdoc`
- **Documenting with `rustdoc`**
  - RustDoc is an invaluable tool within the Rust ecosystem for generating comprehensive and user-friendly documentation directly from your source code. By leveraging special documentation comments (starting with /// for regular comments and //!

### 3.7 Performance and Profiling
- **Criterion.rs**
  - Criterion.rs is a statistics-driven microbenchmarking library for Rust that provides reliable performance analysis over time. It offers detailed feedback, automatic outlier detection, and statistical methods to compare algorithm performance and track regressions with actionable insights.

---

## 4. Optional / Specialized Topics

- Control Flow and Constructs
- Option and Result Enumerations
- Propagating Errors and `?` Operator
- Custom Error Types and Traits
- Tuple
- String
- Array
- Hashmap
- Vector
- Hashset
- LinkedList
- Stack
- Code Organization & Namespacing
- Dependency Management with Cargo
- Publishing on Crates.io
- Deep Dive: Stack vs Heap
- BTreeMap
- BTreeSet
- Mutex
- Unit & Integration Testing
- Mocking & Property Based Testing
- Trait Definitions & Implementations
- Trait Bounds and Associated Types
- Generics & Type-Level Programming
- Box

---

## 5. References

- [Rust Roadmap](https://roadmap.sh/rust)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- Go
- Node.js
- C++