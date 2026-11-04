# Go

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/golang
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction to Go
- **Why use Go**
  - Go offers exceptional performance with single binary deployment, built-in concurrency, fast compilation, and comprehensive standard library. Simple language that's easy to learn and maintain.
- **History of Go**
  - Created at Google in 2007 by Griesemer, Pike, and Thompson. Announced publicly in 2009, version 1.0 in 2012.
- **Setting up the Environment**
  - Install Go from official website, configure PATH, and set up workspace. Configure editor with Go support (VS Code, GoLand, Vim/Emacs).
- **Hello World in Go**
  - Traditional first program demonstrating basic structure: package main, importing fmt, and main() function using fmt.Println(). Teaches Go syntax, compilation, execution, and verifies development environment setup.
- **`go` command**
  - Primary tool for managing Go source code with unified interface for compiling, testing, formatting, and managing dependencies. Includes subcommands like build, run, test, fmt, mod.

### 1.2 Variables & Constants
- **var vs :=**
  - Go provides two main ways to declare variables: using var and using the short declaration operator :=.
- **Zero Values**
  - Default values for uninitialized variables: 0 for numbers, false for booleans, "" for strings, nil for pointers/slices/maps. Ensures predictable initial state and reduces initialization errors.
- **const and iota**
  - Constants declared with const represent unchanging compile-time values. iota creates successive integer constants starting from zero, resetting per const block.
- **Scope and Shadowing**
  - Scope determines variable accessibility from universe to block level. Shadowing occurs when inner scope variables hide outer ones with same names.

### 1.3 Data Types
- **Integers (Signed, Unsigned)**
  - Signed integers (int8, int16, int32, int64) handle positive/negative numbers. Unsigned (uint8, uint16, uint32, uint64) handle only non-negative but larger positive range.

### 1.4 Commands & Docs
- **Boolean**
  - The bool type represents true or false values with default zero value of false. Essential for conditional logic, control flow, and binary states.
- **Floating Points**
  - Two types: float32 (single precision) and float64 (double precision, default). Represent real numbers using IEEE 754 standard.
- **Complex Numbers**
  - Built-in support with complex64 and complex128 types. Create using complex() function or literals like 3+4i.
- **Runes**
  - Represent Unicode code points as int32 type. Enable proper handling of international characters and emojis.

### 1.5 Arrays
- **Raw String Literals**
  - Enclosed in backticks (\) and interpret characters literally without escape sequences. Preserve formatting including newlines.
- **Interpreted String Literals**
  - Enclosed in double quotes (") and process escape sequences like \n, \t, \". Support Unicode characters and formatting.

### 1.6 Slices
- **Type Conversion**
  - Convert values between different types using Type(value) syntax. Go requires explicit conversion even between related types like int and int64.
- **Capacity and Growth**
  - Slice capacity determines when reallocation occurs during append operations. Go typically doubles capacity for smaller slices.
- **make()**
  - Creates and initializes slices, maps, and channels. Unlike new(), returns usable values.
- **Slice to Array Conversion**
  - Convert slice to array using [N]T(slice) (Go 1.17+). Copies data from slice to fixed-size array.
- **Array to Slice Conversion**
  - Convert arrays to slices using expressions like array[:] or array[start:end]. Creates slice header pointing to array memory - no data copying.

### 1.7 Strings
- **Strings**
  - Immutable sequences of bytes representing UTF-8 encoded text. String operations create new strings rather than modifying existing ones.

### 1.8 Maps
- **Comma-Ok Idiom**
  - Pattern for safely testing map key existence or type assertion success using value, ok := map[key] or value, ok := interface.(Type). Returns both value and boolean status, preventing panics and distinguishing zero values from missing keys.

### 1.9 Structs
- **Struct Tags & JSON**
  - Struct tags provide metadata about fields using backticks with key-value pairs. JSON tags control field names, omit empty fields, or skip fields.
- **Embedding Structs**
  - Struct embedding includes one struct inside another without field names, making embedded fields directly accessible. Provides composition-based design following Go's philosophy of composition over inheritance.

### 1.10 Conditionals
- **if**
  - Basic conditional statement for executing code based on boolean conditions. Supports optional initialization statement before condition check.
- **if-else**
  - Basic conditional statements for binary decision making. if tests condition, else handles alternative path.
- **switch**
  - Clean way to compare variable against multiple values and execute corresponding code blocks. No break statements needed (no fall-through by default).
- **Functions Basics**
  - Reusable code blocks declared with func keyword. Support parameters, return values, multiple returns.
- **Variadic Functions**
  - Functions accepting variable number of arguments of same type. Syntax: func name(args ...Type).
- **Multiple Return Values**
  - Go functions can return multiple values, commonly used for returning result and error. Syntax: func name() (Type1, Type2).

### 1.11 Loops
- **for loop**
  - Go's only looping construct, incredibly flexible for all iteration needs. Classic form: initialization, condition, post statements.
- **for range**
  - Special form of for loop for iterating over arrays, slices, maps, strings, and channels. Returns index/key and value.
- **Iterating Maps**
  - Use for range to iterate over maps, returns key and value pairs. Iteration order is random for security reasons.
- **Iterating Strings**
  - Iterate over strings with for range to get runes (Unicode code points) not bytes. Returns index and rune value.
- **continue**
  - Skips rest of current iteration and jumps to next loop iteration. Only affects innermost loop unless used with labels.
- **goto (discouraged)**
  - Go includes goto statement but discourages its use. Can only jump to labels within same function.

---

## 2. Intermediate

### 2.1 Functions
- **break**
  - Immediately exits innermost loop or switch statement. In nested loops, only exits immediate loop unless used with labels to break outer loops.

### 2.2 Pointers
- **Anonymous Functions**
  - Functions declared without names, also called function literals or lambdas. Can be assigned to variables, passed as arguments, or executed immediately.
- **Closures**
  - Functions capturing variables from surrounding scope, accessible even after outer function returns. "Close over" external variables for specialized functions, callbacks, state maintenance.
- **Named Return Values**
  - Function return parameters can be named and treated as variables within function. Initialized to zero values.
- **Call by Value**
  - Go creates copies of values when passing to functions, not references to originals. Applies to all types including structs and arrays.
- **Pointers Basics**
  - Variables storing memory addresses of other variables. Declared with Type, dereferenced with ptr, address obtained with &var.
- **Pointers with Structs**
  - Pointers to structs enable efficient passing of large structures and allow modification of struct fields. Access fields with (ptr).field or shorthand ptr.field.
- **With Maps & Slices**
  - Maps and slices are reference types - passing them to functions doesn't copy underlying data. Modifications inside functions affect original.

### 2.3 Methods vs Functions
- **Memory Management**
  - Largely automatic through garbage collection. Runtime decides stack (fast, auto-cleaned) vs heap (slower, GC required) allocation via escape analysis.
- **Garbage Collection**
  - Go's GC automatically reclaims unreachable memory using concurrent, tri-color mark-and-sweep collector designed for minimal pause times. Runs concurrently with your program.
- **Why Generics?**
  - Introduced in Go 1.18 to solve code duplication when working with multiple types. Before generics: separate functions per type, empty interfaces (losing type safety), or code generation.

### 2.4 Pointer Receivers
- **Pointer Receivers**
  - Methods receive pointer to struct rather than copy using func (p Type) methodName() syntax. Necessary when method modifies receiver state or struct is large.

### 2.5 Value Receivers
- **Value Receivers**
  - Methods receive copy of struct rather than pointer. Use func (v Type) methodName() syntax.

### 2.6 Generics
- **Generic Functions**
  - Write functions working with multiple types using type parameters in square brackets like func FunctionNameT any T. Enable reusable algorithms maintaining type safety.
- **Generic Types / Interfaces**
  - Create reusable data structures and interface definitions working with multiple types. Define with type parameters like type Container[T any] struct { value T }.
- **Type Constraints**
  - Specify which types can be used as type arguments for generics. Defined using interfaces with method signatures or type sets.
- **Type Inference**
  - Allows compiler to automatically determine generic type arguments based on function arguments or context. Reduces need for explicit type specification while maintaining type safety.
- **Error Handling Basics**
  - Go uses explicit error handling with error return values. Functions return error as last value.
- **fmt.Errorf**
  - Creates formatted error messages using printf-style verbs. Supports %w verb for error wrapping (Go 1.13+) to create error chains preserving original errors while adding context.

### 2.7 Interfaces
- **Empty Interfaces**
  - The empty interface interface{} can hold values of any type since every type implements at least zero methods. Used for generic programming before Go 1.18 generics.
- **Embedding Interfaces**
  - Create new interfaces by combining existing ones, promoting composition and reusability. Embedded interface methods automatically included.
- **Type Assertions**
  - Extract underlying concrete value from interface. Syntax: value.(Type) or value, ok := value.(Type) for safe assertion.
- **Type Switch**
  - Special form of switch statement that operates on types rather than values. Syntax: switch v := i.(type).
- **Interfaces Basics**
  - Define contracts through method signatures. Types automatically satisfy interfaces by implementing required methods.

### 2.8 Modules & Dependencies
- **go mod init**
  - Initializes new Go module by creating go.mod file with specified module path (typically repository URL). Marks directory as module root and enables module-based dependency management.
- **go mod tidy**
  - Ensures go.mod matches source code by adding missing requirements and removing unused dependencies. Updates go.sum with checksums.
- **go mod vendor**
  - Creates vendor directory with dependency copies for bundling with source code. Ensures builds work without internet access.

### 2.9 Packages
- **`error` interface**
  - Built-in interface with single Error() string method. Any type implementing this method can represent an error.

### 2.10 Package Import Rules
- **errors.New**
  - Simplest way to create error values by taking a string message and returning an error implementing the error interface. Useful for simple, static error messages.

### 2.11 Using 3rd Party Packages
- **Wrapping/Unwrapping Errors**
  - Create error chains preserving original errors while adding context using fmt.Errorf() with %w verb. Use errors.Unwrap(), errors.Is(), and errors.As() to work with wrapped errors.

### 2.12 Goroutines
- **Goroutines**
  - Lightweight threads managed by Go runtime enabling concurrent function execution. Created with go keyword prefix.

### 2.13 Publishing Modules
- **Sentinel Errors**
  - Predefined error values representing specific conditions, defined as package-level variables. Check using errors.Is() or direct comparison.
- **Deadlines & Cancellations**
  - Context package mechanisms for controlling operation lifetime and propagating cancellation signals. Supports deadlines (absolute time) or timeouts (duration).

### 2.14 Channels
- **Select Statement**
  - Multiplexer for channel operations. Waits on multiple channel operations simultaneously, executing first one ready.

---

## 3. Advanced

### 3.1 Worker Pools
- **Buffered vs Unbuffered**
  - Unbuffered channels provide synchronous communication - sender blocks until receiver ready. Buffered channels allow asynchronous communication up to capacity.

### 3.2 `context` Package
- **Common Usecases**
  - Context package common uses: HTTP timeouts, database deadlines, goroutine cancellation coordination, and request-scoped values. Essential for web servers, microservices, circuit breakers, and building responsive APIs that handle cancellation gracefully.

### 3.3 Concurrency Patterns
- **`panic` and `recover`**
  - panic() stops execution and unwinds stack, recover() catches panics in deferred functions. Use sparingly for unrecoverable errors.
- **Stack Traces & Debugging**
  - Go automatically prints stack traces on panic showing call chain. Tools include Delve debugger, pprof profiling, and race detection.
- **fan-in**
  - Concurrency pattern merging multiple input channels into single output channel. Allows collecting results from multiple goroutines.
- **fan-out**
  - Concurrency pattern distributing work from single source to multiple workers. Typically uses one input channel feeding multiple goroutines.
- **pipeline**
  - Concurrency pattern chaining processing stages where output of one stage becomes input of next. Each stage runs concurrently using goroutines and channels.

### 3.4 `sync` Package
- **Mutexes**
  - Mutual exclusion locks from sync package ensuring only one goroutine accesses shared resource at a time. Use Lock() before and Unlock() after critical section.
- **WaitGroups**
  - Synchronization primitive from sync package for waiting on multiple goroutines to complete. Use Add() to increment counter, Done() when goroutine finishes, Wait() to block until counter reaches zero.
- **`testing` package basics**
  - Standard library package for writing tests. Test functions start with Test and take testing.T parameter.
- **Table-driven Tests**
  - Table-driven tests use slices of test cases to test multiple scenarios with the same logic. Each case contains inputs and expected outputs.
- **Mocks and Stubs**
  - Mocks and stubs replace dependencies with controlled implementations for isolated testing. Stubs provide predefined responses while mocks verify method calls.
- **`httptest`  for HTTP Tests**
  - The httptest package provides utilities for testing HTTP servers and clients without network connections. Includes httptest.Server, ResponseRecorder, and helpers for creating test requests.

### 3.5 Race Detection
- **Race Detection**
  - Built-in tool for detecting race conditions in concurrent programs. Enabled with -race flag during build/test/run.

### 3.6 Standard Library
- **I/O & File Handling**
  - Go's I/O system provides comprehensive file and stream handling through io package interfaces (Reader, Writer, Closer) and os package file operations. The interface-based design allows working with files, network connections, and buffers using consistent patterns.
- **flag**
  - Standard library package for parsing command-line flags. Supports string, int, bool, duration flags with default values and descriptions.
- **time**
  - Standard library package for time and date operations. Handles parsing, formatting, arithmetic, timers, tickers, and timezone operations.
- **encoding/json**
  - This package provides robust and efficient functionalities for marshaling (encoding) Go data structures into JSON and unmarshaling (decoding) JSON into Go data structures. This process is largely handled through the json.Marshal and json.Unmarshal functions.
- **os**
  - Standard library package providing operating system interface. Handles file operations, environment variables, process management, and system information.
- **bufio**
  - Provides buffered I/O operations wrapping io.Reader/Writer interfaces for better performance. Reduces system calls by reading/writing larger chunks.
- **slog**
  - Structured logging package introduced in Go 1.21. Provides leveled, structured logging with JSON output support.
- **regexp**
  - Standard library package for regular expression functionality. Implements RE2 syntax for safe, efficient pattern matching.
- **go:embed for embedding**
  - The go:embed directive embeds files and directories into Go binaries at compile time using //go:embed comments. Useful for including static assets, configs, and templates directly in executables, creating self-contained binaries that don't require external files.

### 3.7 Building CLIs
- **Benchmarks**
  - Benchmarks measure code performance by timing repeated executions. Functions start with Benchmark and use testing.B parameter.
- **Coverage**
  - Test coverage measures code execution during testing using go test -cover and -coverprofile. Visualize with go tool cover -html to identify untested code paths.
- **Cobra**
  - Powerful library for modern CLI applications. Used by kubectl, Hugo, GitHub CLI.
- **urfave/cli**
  - urfave/cli is a simple package for building command-line applications with intuitive API for commands, flags, and arguments. Features automatic help generation, bash completion, nested subcommands, and environment variable integration for lightweight CLI tools.
- **bubbletea**
  - Bubble Tea is a framework for building terminal UIs based on The Elm Architecture. Uses model-update-view pattern for interactive CLI applications with keyboard input, styling, and component composition.

### 3.8 Web Development
- **net/http (standard)**
  - Standard library package for HTTP client/server functionality. Provides HTTP server with routing, middleware support, client for making requests.
- **gRPC & Protocol Buffers**
  - gRPC is a high-performance RPC framework using Protocol Buffers for serialization. Provides streaming, authentication, load balancing, and code generation from .proto files.

### 3.9 ORMs & DB Access
- **gin**
  - Popular HTTP web framework emphasizing performance and productivity. Lightweight foundation for APIs/web services with minimal boilerplate.
- **echo**
  - High-performance, minimalist web framework focusing on ease and speed. Provides routing, middleware, data binding, validation, rendering.
- **pgx**
  - pgx is a pure Go PostgreSQL driver providing both database/sql compatibility and native PostgreSQL features. Offers better performance than lib/pq, includes arrays, JSON support, connection pooling, and PostgreSQL-specific features like LISTEN/NOTIFY.
- **GORM**
  - Popular Object-Relational Mapping library for Go. Provides database abstraction with struct-based models, automatic migrations, associations, and query building.

### 3.10 Logging
- **fiber**
  - Fiber is an Express-inspired web framework built on fasthttp for exceptional performance. Provides familiar API with middleware, routing, templates, and WebSocket support.
- **beego**
  - Beego is a full-stack web framework providing MVC architecture, ORM, session management, caching, and admin interface generation. Follows convention over configuration with extensive tooling for rapid development of enterprise applications requiring comprehensive features.
- **Zerolog**
  - Zerolog is a zero-allocation JSON logger focusing on performance and simplicity. Provides structured logging with fluent API, various log levels, and no memory allocations during operations, making it ideal for high-throughput production applications.
- **Zap**
  - Zap is a high-performance structured logging library by Uber offering both structured and printf-style APIs. Features include JSON/console formats, configurable levels, sampling, and production-optimized performance through careful memory management.

### 3.11 Realtime Communication
- **Melody**
  - Melody is a minimalist WebSocket framework for Go providing simple session management, message broadcasting, and connection handling. Features include rooms, automatic ping/pong, message limits, and clean integration with existing web frameworks for real-time apps.
- **Centrifugo**
  - Centrifugo is a real-time messaging server providing WebSocket services for Go applications. It offers channels, presence info, message history, and Redis scalability.
- **go run**
  - Compiles and executes Go programs in one step without creating executable files. Useful for testing, development, and running scripts.
- **go build**
  - Compiles Go packages and dependencies into executable binaries. Supports cross-compilation for different OS/architectures via GOOS/GOARCH.
- **go install**
  - Compiles and installs packages and dependencies. Creates executables in $GOPATH/bin for main packages.
- **go fmt**
  - Automatically formats Go source code according to official style guidelines. Standardizes indentation, spacing, alignment for consistent code style.
- **go mod**
  - Command-line tool for module management. go mod init creates module, go mod tidy cleans dependencies, go mod download fetches modules.
- **go test**
  - Command for running tests in Go packages. Automatically finds and executes functions starting with Test.
- **go clean**
  - Removes object files and cached files from build process. Options include -cache for build cache and -modcache for module downloads.
- **go doc**
  - Prints documentation for Go packages, types, functions, and methods extracted from specially formatted comments. Use go doc package or go doc package.Function to view specific documentation.
- **go version**
  - Displays the currently installed Go version, target OS, and architecture. Essential for verifying installation, troubleshooting environment issues, and ensuring compatibility across different development environments and teams.
- **go generate**
  - The go generate command executes commands specified in //go:generate directives to generate Go source code. Used for code generation from templates, string methods, embedded resources, and running tools like protobuf compilers for build automation.
- **Build Tags**
  - Build tags control file inclusion using //go:build directives based on conditions like OS, architecture, or custom tags. Enable conditional compilation for platform-specific code, feature flags, and environment-specific builds without runtime overhead.
- **go vet**
  - Built-in tool analyzing Go source code for suspicious constructs likely to be bugs. Checks for unreachable code, incorrect printf formats, struct tag mistakes, and potential nil pointer dereferences.
- **goimports**
  - Tool automatically managing Go import statements by adding missing imports and removing unused ones while formatting code. More convenient than manual import management, integrates with editors for automatic execution on save.
- **revive**
  - Fast, configurable Go linter providing rich formatting and many rules for code analysis. Drop-in replacement for golint with better performance, configurable rules, and various output formats.
- **staticcheck**
  - State-of-the-art Go linter catching bugs, performance issues, and style problems through static analysis. Provides more comprehensive checking than go vet with very few false positives.
- **golangci-lint**
  - Fast, parallel runner for multiple Go linters including staticcheck, go vet, and revive. Provides unified configuration, output formatting, and performance optimization.
- **govulncheck**
  - Go's official vulnerability scanner checking code and dependencies for known security vulnerabilities. Reports packages with vulnerabilities from Go database, provides severity info and remediation advice.
- **pprof**
  - Built-in profiling tool for analyzing program performance. Profiles CPU usage, memory allocation, goroutines, blocking operations.
- **trace**
  - The Go trace tool captures execution traces showing goroutine execution, system calls, GC, and scheduling. Generate traces with runtime/trace package, analyze with go tool trace.
- **Race Detector**
  - Runtime tool detecting data races in concurrent programs using the -race flag. Tracks memory accesses and reports conflicts with detailed information including stack traces.
- **Cross-compilation**
  - Build executables for different OS and architectures using GOOS and GOARCH environment variables. Example: GOOS=linux GOARCH=amd64 go build creates Linux binaries.
- **Building Executables**
  - The go build command compiles source code into standalone native executables with static linking. Creates self-contained binaries including all dependencies, requiring no Go installation on target systems.
- **Memory Mgmt. in Depth**
  - Deep memory management involves understanding garbage collection, escape analysis, allocation patterns, and optimization techniques. Covers stack vs heap allocation, memory pooling, reducing allocations, and GC interaction for high-performance applications.
- **Escape Analysis**
  - Compile-time optimization determining whether variables are allocated on stack (fast) or heap (GC required). Variables that "escape" their scope need heap allocation.
- **Reflection**
  - Reflection allows runtime inspection and manipulation of types and values using the reflect package. Enables dynamic method calls and type examination but has performance overhead.
- **Unsafe Package**
  - The unsafe package bypasses Go's type and memory safety for direct memory manipulation and pointer arithmetic. Powerful but dangerous - can cause crashes and vulnerabilities.
- **Build Constraints & Tags**
  - Special comments controlling which files are included when building. Use //go:build directive for platform-specific code, environment builds, or feature toggles.
- **CGO Basics**
  - CGO allows Go programs to call C code and vice versa using special comments. Enables C library integration but disables cross-compilation, reduces performance, and complicates deployment.
- **Compiler & Linker Flags**
  - Build flags control compilation and linking. Common flags include -ldflags for linker options, -gcflags for compiler settings, -tags for build tags, and -race for race detection.
- **Plugins & Dynamic Loading**
  - Go's plugin system allows loading shared libraries (.so files) at runtime using the plugin package. Built with go build -buildmode=plugin.

---

## 4. Optional / Specialized Topics

- `go` command
- Array to Slice Conversion
- Variadic Functions
- Multiple Return Values
- continue
- goto (discouraged)
- Pointers Basics
- Pointers with Structs
- With Maps & Slices
- Error Handling Basics
- fmt.Errorf
- Interfaces Basics
- pipeline
- Mocks and Stubs
- `httptest`  for HTTP Tests
- os
- bufio
- slog
- regexp
- go:embed for embedding
- bubbletea
- go install
- go fmt
- go mod
- go test

---

## 5. References

- [Go Roadmap](https://roadmap.sh/golang)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- Python
- Java
- JavaScript
- Node.js