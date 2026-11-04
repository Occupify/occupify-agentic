# C

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/c
- Related Roles:
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **Applications**
  - C shows up in operating system kernels (Linux, Windows internals), embedded systems and microcontrollers, device drivers, database engines, and performance-critical libraries. Many other languages, including Python and Ruby, have interpreters written in C, and most language runtimes expose a C interface for interoperability.
- **C vs C++**
  - C is a procedural language with manual memory management and no built-in support for classes, inheritance, or exceptions. C++ extends C with object-oriented features, templates, the standard template library, and stronger compile-time checks, while remaining mostly compatible with C syntax.
- **C vs Assembly**
  - Assembly language maps almost directly to a specific CPU's instruction set, so code written for one processor architecture will not run on another without a rewrite. C sits one level above assembly: it compiles down to machine code but uses portable syntax that works across architectures with little or no change.

### 1.2 Setting up
- **Installing C**
  - Installing C means installing a compiler such as GCC or Clang, since C itself is just a language specification with no official installer. On Linux, package managers like apt or dnf usually provide GCC directly.
- **Code Editors / IDEs**
  - C can be written in a plain text editor, a lightweight code editor, or a full IDE, and the choice affects how much tooling support you get for things like autocomplete, debugging, and build integration. Lightweight editors like vim or VSCode require some manual setup for compiling and debugging, while full IDEs bundle these features together.
- **Running your First Program**
  - Running a first C program means writing a small source file, usually one that prints "Hello, World!", compiling it with a tool like GCC, and executing the resulting binary. This process introduces the basic compile-then-run workflow that every C program follows: source code goes through the compiler to produce machine code, and only that machine code actually runs.

### 1.3 Variables
- **Declaration vs Definition**
  - A declaration tells the compiler that a variable or function exists and states its type, without necessarily allocating memory or providing a function body. A definition actually allocates storage for a variable or provides the function's implementation.
- **Initialization**
  - Initialization is giving a variable its first value at the point it is created, as in int count = 0;. Uninitialized local variables in C hold indeterminate values, whatever bits happened to be in that memory location before, so reading one before assigning it produces undefined behavior.
- **Printing Variables**
  - Printing variables in C typically uses the printf function from the standard library, with format specifiers like %d for integers, %f for floats, or %s for strings telling it how to interpret the data. Each specifier must match the variable's actual type, since printf does not check this at compile time and mismatches can produce garbage output or crashes.
- **integers**
  - Integer types in C, such as int, short, and long, store whole numbers without a fractional part. Their exact size in bytes is not fixed by the language and can vary between platforms, though int is commonly 4 bytes on modern systems.
- **float**
  - The float type stores single-precision floating-point numbers, meaning it can represent fractional values but with limited precision, typically around 6 to 7 significant decimal digits. It follows the IEEE 754 standard on most systems and takes up 4 bytes of memory.
- **vim / nvim**
  - vim and its modern fork neovim are terminal-based text editors known for keyboard-driven, modal editing rather than a traditional mouse-and-menu interface. They are lightweight and run over SSH, which makes them popular for editing C code on remote servers or embedded systems.
- **VSCode**
  - Visual Studio Code is a free, extensible code editor from Microsoft that supports C through extensions like the C/C++ extension pack. It offers syntax highlighting, IntelliSense autocomplete, integrated debugging, and build task configuration through simple JSON files.

### 1.4 Data Types
- **booleans**
  - C did not originally have a dedicated boolean type, relying instead on the convention that zero means false and any nonzero value means true. Since C99, the <stdbool.h> header provides a bool type along with true and false macros for clearer code.
- **Type Qualifiers**
  - Type qualifiers add extra meaning to a variable's declaration beyond its basic type, telling the compiler how the variable can be used or how it might change. C provides four standard qualifiers: const, volatile, restrict, and Atomic.
- **Type Conversion**
  - Type conversion changes a value from one data type to another, either automatically by the compiler (implicit conversion) or explicitly by the programmer using a cast, such as (int)3.9. Implicit conversions follow C's promotion rules, for example converting a char to an int in arithmetic, and can sometimes cause unexpected precision loss or overflow.
- **const**
  - The const qualifier marks a variable as read-only after initialization, so any attempt to modify it later triggers a compile-time error. It is commonly used for function parameters that should not be changed by the function, and for values that are fixed for the program's lifetime, like configuration constants.
- **volatile**
  - The volatile qualifier tells the compiler that a variable's value can change unexpectedly, outside the normal flow of the program, such as through hardware registers or signal handlers. This prevents the compiler from applying optimizations that assume the variable's value stays the same between reads.
- **double**
  - The double type stores double-precision floating-point numbers, offering roughly twice the precision of float, around 15 to 17 significant decimal digits, and typically occupying 8 bytes of memory. It is the default floating-point type used by C's standard library functions unless float is specified explicitly.
- **char**
  - The char type stores a single byte, most often used to represent a character encoded as its numeric value, such as ASCII. It can be signed or unsigned depending on the compiler and platform, which affects how negative values behave.
- **Extended Types**
  - Extended types cover additional numeric and specialized types beyond the basic set, such as long long for larger integer ranges, long double for extended floating-point precision, and complex number types added in later C standards. They exist to handle cases where the basic types are not large or precise enough.
- **Fixed-width integers**
  - Fixed-width integer types, defined in <stdint.h>, such as int32t or uint8t, guarantee an exact bit width regardless of platform, unlike int or long whose sizes can vary. This makes them useful for writing portable code, especially in networking, file formats, and embedded systems where exact sizes matter.

### 1.5 Operators
- **Arithmetic**
  - Arithmetic operators perform basic mathematical operations: + for addition, - for subtraction, for multiplication, / for division, and % for remainder (modulo). Division between two integers truncates toward zero and discards any fractional part, which can surprise programmers expecting a decimal result.
- **Logical**
  - Logical operators, && (AND), || (OR), and ! (NOT), combine or invert boolean conditions and are typically used in control flow statements.
- **Bitwise**
  - Bitwise operators manipulate individual bits within a value, including AND (&), OR (|), XOR (^), NOT (~), and the shift operators (<<, >>). They are used in low-level programming for tasks like setting flags, masking bits, or optimizing certain calculations.
- **restrict**
  - The restrict qualifier, introduced in C99, is a hint to the compiler that a pointer is the only way to access the memory it points to during its lifetime. This allows the compiler to make more aggressive optimizations, since it does not need to guard against another pointer aliasing the same memory.
- **Comparison**
  - Comparison operators, such as ==, !=, <, >, <=, and >=, evaluate two values and produce a result of 1 (true) or 0 (false). They are commonly used in conditions for if statements and loops to control program flow.
- **_Atomic**
  - The Atomic qualifier, introduced in C11, marks a variable so that reads and writes to it happen as a single, indivisible operation, even when accessed from multiple threads. This prevents data races on that variable without needing a separate lock.
- **Ternary**
  - The ternary operator, written as condition ? valueiftrue : valueiffalse, is a compact way to write a simple if-else expression that returns a value.

### 1.6 Control Flow
- **for / while / do while loops**
  - C offers three loop constructs: for, which bundles initialization, condition, and increment in one line and suits a known number of iterations; while, which checks its condition before each iteration and suits an unknown number of repetitions; and do-while, which checks its condition after each iteration, guaranteeing the loop body runs at least once. Choosing between them mostly comes down to whether the number of iterations is known ahead of time and whether the body must run at least once.
- **if else / switch**
  - The if/else statement branches execution based on whether a condition evaluates to true or false, and can be chained with else if for multiple conditions. The switch statement compares a single value against several possible cases and is often clearer than a long if/else if chain when checking one variable against many fixed values.
- **break / continue**
  - break immediately exits the nearest enclosing loop or switch statement, skipping any remaining iterations or cases. continue skips the rest of the current loop iteration and jumps straight to the next one, without exiting the loop entirely.

### 1.7 Functions
- **Recursive Functions**
  - A recursive function is one that calls itself, either directly or indirectly, to solve a problem by breaking it into smaller instances of the same problem. Every recursive function needs a base case that stops the recursion, otherwise it will call itself indefinitely until it exhausts the call stack.
- **Variable Scopes**
  - Variable scope determines where in a program a variable can be accessed. Variables declared inside a function or block are local and only visible within that block, while variables declared outside any function are global and visible throughout the file, or across files if declared extern.
- **Memory Model**
  - C's memory model describes how a running program's memory is organized into distinct regions: the stack for local variables and function call information, the heap for dynamically allocated memory, and separate segments for global/static variables and the compiled program code itself. Understanding this layout helps explain why some memory is automatically reclaimed and other memory must be freed manually.
- **Variadic Functions**
  - Variadic functions accept a variable number of arguments, like printf, which can take any number of values depending on its format string. They are declared using an ellipsis (...) as the last parameter and accessed inside the function using macros from <stdarg.h>, such as vastart, vaarg, and vaend.
- **Command-Line Arguments**
  - Command-line arguments let a program receive input when it starts, passed through main's parameters: argc, the count of arguments, and argv, an array of strings containing the arguments themselves, with argv[0] typically being the program's own name. This is how command-line tools accept options and file paths without needing interactive input.
- **main Function**
  - The main function serves as the designated entry point where the execution of every C program begins. When a program is run, the operating system calls this specific function to start the sequence of instructions defined within the code.

---

## 2. Intermediate

### 2.1 Pointers & Memory
- **Stack vs Heap**
  - The stack is a region of memory that automatically manages local variables and function call data, growing and shrinking as functions are called and return, and it is fast but limited in size. The heap is a region for dynamically allocated memory, managed manually with functions like malloc and free, offering more flexibility in size and lifetime at the cost of more responsibility.
- **Lifetime of Objects**
  - The lifetime of an object is the period during program execution when its memory is guaranteed to hold valid data. Local variables on the stack typically live only until the enclosing block exits, static and global variables live for the entire program, and heap-allocated memory lives until it is explicitly freed.

### 2.2 Arrays
- **Arrays**
  - An array in C is a fixed-size, contiguous block of memory holding multiple elements of the same type, accessed using an index starting at zero. The size of an array must be known at compile time unless it is allocated dynamically on the heap.

### 2.3 Strings
- **Structs**
  - A struct groups multiple variables, possibly of different types, under a single name, so related data can be treated as one unit. Each field, or member, is accessed using the dot operator, or the arrow operator if accessed through a pointer to the struct.
- **Null Pointers**
  - A null pointer is a pointer that intentionally points to no valid memory location, conventionally written as NULL in C. It is used to indicate that a pointer does not currently reference anything, such as before allocation or after freeing memory.
- **Pointer Basics & Syntax**
  - A pointer is declared with an asterisk, such as int p, and holds the memory address of a value rather than the value itself. The & operator retrieves a variable's address, while the operator, when applied to a pointer, dereferences it to access the value it points to.

### 2.4 User-Defined Types
- **Unions**
  - A union allows multiple members to share the same memory location, so only one member holds a valid value at any given time, and the union's size equals that of its largest member. This is useful for saving memory when different pieces of data are never needed simultaneously, or for interpreting the same bytes in different ways.
- **Enums**
  - An enum defines a type consisting of a set of named integer constants, making code more readable than using raw numbers to represent a fixed set of options, such as days of the week or states in a state machine. By default, enum values start at 0 and increase by one for each subsequent name, though explicit values can be assigned.
- **Typedef**
  - typedef creates an alias for an existing type, which can shorten complex type declarations or make code more portable and readable, for example typedef unsigned long sizet;. It is commonly used with structs to avoid repeating the struct keyword every time the type is used.
- **void Pointers**
  - A void pointer, declared as void , can point to any data type but cannot be dereferenced directly, since the compiler has no type information about what it points to. It is typically cast to a specific pointer type before use, and appears often in generic functions like malloc, which returns void because it has no knowledge of what type of data will be stored there.
- **Pointer Arithmetic**
  - Pointer arithmetic lets you add or subtract integers from a pointer to move it to a different memory location, with the step size automatically scaled by the size of the type the pointer points to. This is the mechanism behind array indexing, since arr[i] is equivalent to (arr + i).

### 2.5 Common Data Structures
- **Dynamic Arrays**
  - A dynamic array is an array-like structure that can grow or shrink at runtime, typically implemented by allocating memory on the heap and reallocating a larger block, often using realloc, when it runs out of space. Unlike a fixed-size C array, it tracks both its current length and its allocated capacity separately.
- **Hash Maps**
  - A hash map stores key-value pairs and uses a hash function to convert each key into an index into an underlying array, allowing average constant-time lookup, insertion, and deletion. Since C has no built-in hash map, implementing one involves writing a hash function, handling collisions when two keys hash to the same index, and managing the underlying array's resizing.
- **Ring Buffers / FIFO Queues**
  - A ring buffer, or circular buffer, is a fixed-size buffer that wraps around to the beginning once it reaches the end, making it efficient for implementing first-in-first-out queues without shifting elements. It tracks a read position and a write position that both wrap around the buffer's length.
- **Linked Lists**
  - A linked list stores a sequence of elements as separate nodes, where each node contains a value and a pointer to the next node, rather than storing elements contiguously like an array. This makes inserting or removing elements in the middle of the list efficient, since it only requires updating a few pointers, but accessing an arbitrary element requires walking the list from the start.
- **malloc**
  - malloc is a function used to reserve a specific amount of memory during the execution of a program. When called, it allocates a block of memory of a requested size in bytes on the heap and returns a pointer to the first byte of that block.
- **calloc**
  - calloc is a function used to allocate a specified number of blocks of memory, each of a set size, and initializes every byte in that memory to zero. It takes two arguments: the number of elements to allocate and the size of each element in bytes.
- **realloc**
  - realloc is a function used to change the size of a previously allocated memory block. It takes a pointer to an existing memory block and a new size as arguments, then attempts to resize the block while preserving its existing contents.
- **free**
  - free is a standard library function used to deallocate a block of memory that was previously reserved on the heap. When you call this function, it releases the specified memory back to the system so that it can be used for other purposes in the program.

### 2.6 Structuring Codebase
- **Header Files**
  - Header files, with a .h extension, contain declarations, such as function prototypes, struct definitions, and macros, that are shared across multiple source files using #include. They let multiple .c files agree on the same interface without duplicating code.
- **Linkage**
  - Linkage determines whether a name, like a variable or function, refers to the same entity when it appears in multiple files. External linkage means the name is visible and shared across files, internal linkage restricts it to the file it is defined in, and no linkage applies to names like local variables that exist only within a block.
- **Undefined Behavior**
  - Undefined behavior refers to code whose outcome the C standard places no constraints on, meaning a compiler is free to produce any result, including seemingly correct output, a crash, or subtle corruption that only appears under certain conditions. Common causes include signed integer overflow, reading uninitialized memory, out-of-bounds array access, and dereferencing invalid pointers.
- **static**
  - At file scope, static gives a variable or function internal linkage, restricting its visibility to the file it is defined in and preventing naming conflicts with other files. Inside a function, static on a local variable makes it retain its value between function calls instead of being reinitialized each time, while still keeping it local to that function.
- **extern**
  - The extern keyword declares that a variable or function is defined in another file, giving the compiler the information it needs to reference it without allocating storage again. It is typically placed in a header file so multiple source files can share the same global variable or function.
- **Dynamic Memory Allocation**
  - Dynamic memory allocation reserves memory on the heap at runtime, when the amount of memory needed is not known in advance or needs to outlive the function that created it. C provides malloc, calloc, and realloc for allocation and free for releasing memory back to the system.
- **Memory Leakage**
  - A memory leak happens when dynamically allocated memory is no longer needed but is never freed, so it stays reserved and unavailable for the rest of the program's execution. Leaks accumulate over time, especially in long-running programs, and can eventually exhaust available memory.
- **Dangling Pointers**
  - A dangling pointer points to memory that has already been freed or otherwise become invalid, but the pointer itself still holds the old address. Using a dangling pointer, whether reading or writing through it, results in undefined behavior and can corrupt unrelated data.

### 2.7 Error Handling
- **Input / Output**
  - The standard library's I/O functions, declared mainly in <stdio.h>, handle reading from and writing to streams, including the console and files. Common functions include printf and scanf for formatted console I/O, and fopen, fread, and fwrite for file access.
- **Data Utilities**
  - Data utility functions, largely from <stdlib.h>, provide general-purpose operations such as memory allocation (malloc, free), converting strings to numbers (atoi, strtol), generating pseudo-random numbers (rand), and sorting or searching arrays (qsort, bsearch). They cover common tasks that come up across many kinds of programs regardless of domain.
- **errno**
  - errno is a global variable, declared in <errno.h>, that many standard library functions set to a specific error code when they fail. It is not automatically reset to zero on success, so it should only be checked immediately after a function call that is documented to set it, and typically after confirming the function actually failed.
- **Exit Codes**
  - An exit code is a small integer that a program returns to the operating system when it finishes, indicating whether it succeeded or failed, and if it failed, sometimes why. By convention, an exit code of 0 means success and any nonzero value indicates an error, with EXITSUCCESS and EXITFAILURE from <stdlib.h> providing portable constants for these.
- **setjmp / longjmp**
  - setjmp and longjmp, declared in <setjmp.h>, implement a non-local jump that lets a program save an execution point with setjmp and later jump back to it with longjmp, potentially unwinding several function calls at once. This is sometimes used as a rough substitute for exception handling, for example to recover from an error deep in a call stack.
- **Buffer Overflow**
  - A buffer overflow occurs when a program writes more data into a fixed-size buffer, like an array, than it can hold, overwriting adjacent memory. This can corrupt other variables, crash the program, or in more severe cases be exploited to execute malicious code, making it a well-known security vulnerability.

### 2.8 File I/O
- **Streams**
  - A stream in C is an abstraction representing a source or destination of data, such as a file, the keyboard, or the screen, accessed through a FILE pointer. The standard library provides three streams automatically: stdin for input, stdout for normal output, and stderr for error output.
- **File Pointers**
  - A file pointer, of type FILE , is returned by fopen and represents an open file along with its current read/write position and buffering state. It is passed to subsequent I/O functions like fread, fwrite, and fclose to identify which open file they should operate on.
- **Binary vs Text Mode**
  - Text mode may translate certain characters, most notably line endings, when reading or writing a file, converting between the operating system's native line-ending convention and a consistent internal representation. Binary mode performs no such translation, transferring bytes exactly as they are stored.
- **Text Processing**
  - Text processing functions, mostly from <string.h> and <ctype.h>, handle operations on C strings and characters, such as measuring length (strlen), copying (strcpy), concatenating (strcat), comparing (strcmp), and classifying individual characters as alphabetic, numeric, or whitespace. Many of these functions assume null-terminated strings and do not check buffer sizes, so using safer, bounded variants where available reduces the risk of buffer overflows.
- **Math & Time**
  - Math functions, from <math.h>, provide operations like square roots, trigonometric functions, and logarithms that go beyond the basic arithmetic operators. Time functions, from <time.h>, handle getting the current time, measuring elapsed time, and formatting dates.

### 2.9 Standard Library
- **Diagnostics & Limits**
  - Diagnostic and limit headers, such as <assert.h> and <limits.h>, provide tools for catching bugs and understanding platform constraints. The assert macro checks that a condition holds true during development and aborts the program with a message if it does not, while <limits.h> defines constants like INTMAX describing the range of values each integer type can hold on the current platform.
- **OS & Signal Interfaces**
  - Operating system and signal interfaces, such as <signal.h> and parts of <stdlib.h>, let a C program interact with the underlying operating system, including handling asynchronous events like interrupts (SIGINT) or setting up custom responses to system-generated signals. These functions provide a portable, if limited, way to write programs that respond to external events like a user pressing Ctrl+C.
- **Preprocessors**
  - The preprocessor runs before actual compilation begins, handling directives that start with #, such as #include, #define, and conditional compilation directives. It performs purely textual transformations on the source code, expanding macros and including header file contents, before the compiler ever sees the result.

---

## 3. Advanced

### 3.1 Build & Compilation
- **WinDbg**
  - WinDbg is a debugger from Microsoft for Windows programs, capable of both live debugging and analyzing crash dump files after a program has already terminated. It is commonly used for debugging Windows-specific issues, including kernel-level and driver debugging, that other cross-platform debuggers do not handle.
- **LLDB**
  - LLDB is a debugger built as part of the LLVM project, offering similar functionality to GDB, including breakpoints, stepping through code, and inspecting variables, with a largely compatible but distinct command syntax. It is the default debugger bundled with Xcode on macOS and integrates closely with Clang-compiled binaries.
- **strace**
  - strace is a Linux diagnostic tool that traces and logs the system calls a running program makes to the operating system kernel, such as opening files, reading input, or allocating memory. It helps diagnose problems related to file access, permissions, or unexpected system-level behavior without needing to modify or recompile the program being examined.
- **Macros**
  - A macro, defined with #define, is a preprocessor directive that gives a name to a piece of code, which is then substituted wherever that name appears before compilation. Macros can be simple constants, like #define PI 3.14159, or function-like, taking parameters and expanding into a code pattern.
- **Conditional Compilation**
  - Conditional compilation uses preprocessor directives like #ifdef, #ifndef, #if, and #endif to include or exclude blocks of code before the compiler processes them, based on whether certain macros are defined. It is commonly used for platform-specific code, enabling debug-only sections, or preventing a header file from being included multiple times through header guards.

### 3.2 Debugging
- **Compilers**
  - A compiler translates C source code into machine code that can run directly on a specific processor and operating system. Popular choices include GCC and Clang, which support most platforms, and specialized compilers like TinyCC, designed for speed rather than optimization.
- **GDB**
  - GDB (GNU Debugger) is a command-line debugger that lets a programmer run a C program under its control, set breakpoints to pause execution at specific lines, inspect and modify variable values, and step through code one line or instruction at a time. It works with binaries compiled with debugging information, typically added using the -g compiler flag.
- **ASan & LSan**
  - AddressSanitizer (ASan) and LeakSanitizer (LSan) are compiler-integrated tools, enabled with a flag like -fsanitize=address, that detect memory errors and leaks respectively by instrumenting the compiled code to check memory accesses at runtime. ASan catches issues such as buffer overflows, use-after-free, and use of memory after it goes out of scope, reporting the exact location of the error.
- **Valgrind**
  - Valgrind is a dynamic analysis tool that runs a compiled program inside a virtual environment to detect memory errors, such as reading uninitialized memory, using memory after it has been freed, and memory leaks, at runtime. Its most commonly used tool, Memcheck, reports the exact line where a memory error occurred, including the point where the involved memory was originally allocated.
- **Predefined Macros**
  - Predefined macros are macros that the compiler defines automatically without any explicit #define, providing information such as the current file name (FILE), line number (LINE), compilation date (DATE), or which C standard is in use (STDCVERSION). They are often used in debugging output or conditional compilation to adapt code based on the compiler or platform.

### 3.3 Testing
- **Symbol Tables**
  - A symbol table is a data structure maintained during compilation and linking that maps names, like function and variable identifiers, to information such as their memory addresses or types. Compilers use it internally to resolve references within a single file, while linkers use symbol tables to connect references across multiple object files.
- **GCC / Clang**
  - GCC (GNU Compiler Collection) and Clang are two widely used, open-source C compilers, each supporting multiple platforms and largely compatible command-line interfaces. GCC has a longer history and broader platform support, while Clang is known for faster compilation, more readable error messages, and being built on the LLVM compiler infrastructure.
- **Optimization Levels**
  - Optimization levels, set with compiler flags like -O0 through -O3 in GCC and Clang, control how aggressively the compiler transforms code to improve performance, often at the cost of longer compile times and less predictable debugging behavior. -O0 disables optimization entirely, which is useful during development since the compiled code closely matches the source.
- **TinyCC**
  - TinyCC, also called tcc, is a small, fast C compiler that prioritizes compilation speed over generating optimized machine code. It can compile and run C code almost instantly, making it useful for scripting-like use cases or quick testing, though the resulting binaries are typically slower than those produced by GCC or Clang with optimizations enabled.
- **assert.h**
  - <assert.h> provides the assert macro, which checks that a given condition is true and, if not, prints an error message with the file and line number before terminating the program. It is commonly used during development to catch programming errors early, such as invalid function arguments, rather than letting them cause harder-to-diagnose failures later.
- **Unity**
  - Unity is a lightweight unit testing framework for C, designed with embedded systems in mind, requiring minimal dependencies and working even on platforms without a full standard library. It provides a set of assertion macros for checking expected values and organizing tests into runnable suites.
- **CMocka**
  - CMocka is a unit testing framework for C that includes support for mock objects, letting tests replace real function calls with controlled substitutes to isolate the code under test. It provides assertion macros for checking expected values and can run groups of test cases together while reporting pass/fail results.
- **Check**
  - Check is a unit testing framework for C that runs each test case in its own separate process, so a crash or memory error in one test does not stop the rest of the test suite from running. It provides assertion macros and supports organizing tests into suites, similar to other C testing frameworks.

### 3.4 Idioms & Design Patterns
- **Linking**
  - Linking is the stage after compilation that combines multiple object files and libraries into a single executable, resolving references between them, such as a function called in one file but defined in another. A linker error occurs when a referenced symbol cannot be found anywhere among the provided object files and libraries.
- **ABI**
  - An ABI (Application Binary Interface) defines the low-level conventions that compiled code must follow to be compatible with other compiled code, including how function arguments are passed, how data is laid out in memory, and how the stack is organized. Unlike a language-level API, which concerns source code compatibility, an ABI concerns binary compatibility between already-compiled pieces of code.
- **Build Systems**
  - A build system automates the process of compiling and linking a project's source files into a final executable or library, tracking dependencies so that only files affected by a change need to be rebuilt. Options range from simple tools like GNU Make, which uses explicit rules in a Makefile, to higher-level generators like CMake, which produce build files for other underlying build tools.
- **GNU Make**
  - GNU Make is a build automation tool that reads a file called a Makefile, containing rules that specify how to build targets from their dependencies, and only rebuilds the parts of a project that have actually changed. It is one of the oldest and most widely available build tools on Unix-like systems.
- **CMake**
  - CMake is a cross-platform build system generator that reads a project description, written in its own CMake language, and produces native build files for the target platform, such as Makefiles on Linux or Visual Studio project files on Windows. This lets a single project configuration work across multiple platforms and underlying build tools without maintaining separate build scripts for each.
- **Opaque Pointers**
  - An opaque pointer is a pointer to a struct whose full definition is hidden from the code using it, typically by only declaring the struct's existence in a header file without listing its members. This lets a library expose functions that operate on the type while keeping its internal fields inaccessible and free to change, achieving a form of encapsulation similar to private members in object-oriented languages.
- **Object-Oriented C**
  - Object-oriented programming techniques can be approximated in C, despite the language having no built-in classes, by combining structs to hold data with function pointers to simulate methods, often organized as a table of function pointers resembling a virtual method table. Encapsulation is typically achieved through opaque pointers, hiding a struct's internal fields from code outside the module that defines it.
- **RAII-Simulated Cleanup**
  - RAII (Resource Acquisition Is Initialization) is a pattern from C++ where a resource's cleanup is tied automatically to an object's lifetime. C has no destructors to do this automatically, so similar cleanup guarantees are simulated manually, for example using the goto statement to jump to a single cleanup section at the end of a function that frees all acquired resources.
- **Function pointers & Callbacks**
  - A function pointer stores the address of a function, allowing that function to be called indirectly, passed as an argument, or stored in a data structure, similar to how a regular pointer stores the address of a variable. Callbacks use this to let one function invoke another that is decided at runtime, a pattern used by standard library functions like qsort, which takes a comparison function as a callback.

### 3.5 Concurrency
- **Package Managers**
  - Package managers for C, such as vcpkg and Conan, automate finding, downloading, and building third-party libraries so they can be linked into a project without manually managing source code or prebuilt binaries. This addresses a longstanding pain point in C development, since the language itself has no built-in package management or standard library distribution mechanism.
- **Ninja**
  - Ninja is a build system designed to run builds as fast as possible, focusing on quick incremental rebuilds rather than being written directly by hand. Its input files are typically generated by a higher-level tool like CMake rather than authored manually, since Ninja's own file format is intentionally minimal and low-level.
- **Meson**
  - Meson is a build system that emphasizes speed and a simple, readable configuration language, generating backend build files for tools like Ninja rather than compiling directly itself. It aims to make common build tasks straightforward with sensible defaults, reducing the boilerplate often needed with tools like CMake.
- **POSIX Threads**
  - POSIX Threads, commonly called pthreads, is a standardized API, defined in <pthread.h>, for creating and managing threads on Unix-like systems, letting a single process run multiple sequences of instructions concurrently. Threads created this way share the same memory space, which enables fast communication between them but also introduces the risk of race conditions when multiple threads access the same data without coordination.
- **Mutexes**
  - A mutex (mutual exclusion lock) is a synchronization primitive that ensures only one thread can access a shared resource, like a variable or data structure, at a time, preventing race conditions. A thread acquires (locks) the mutex before accessing the shared resource and releases (unlocks) it afterward, and any other thread attempting to lock it in the meantime must wait.

### 3.6 Process Management
- **vcpkg**
  - vcpkg is an open-source package manager from Microsoft for C and C++ libraries, supporting Windows, Linux, and macOS. It builds libraries from source for the target platform and compiler, then integrates them with build systems like CMake or Visual Studio.
- **Conan**
  - Conan is a package manager for C and C++ that manages both source and prebuilt binary packages, with a focus on handling different build configurations, such as debug versus release, or different compilers. It integrates with build systems including CMake and Meson, and maintains a central repository of package recipes that describe how to build and consume each library.
- **IPC**
  - Inter-process communication (IPC) covers mechanisms that let separate, independent processes exchange data, since processes do not share memory the way threads within one process do. Common IPC mechanisms include pipes for streaming data between related processes, shared memory segments for faster but more manually managed data sharing, and message queues or sockets for more structured or networked communication.

### 3.7 C Standards
- **C89 / C90**
  - C89, also called C90 after its later ISO ratification, was the first standardized version of C, published in 1989 by ANSI. It established the core language and standard library that later versions built on, and remains the baseline that many embedded and legacy systems still target for maximum portability.
- **C99**
  - C99, published in 1999, added several widely used features to the language, including the bool type via <stdbool.h>, variable-length arrays, // single-line comments, and the ability to declare variables anywhere within a block rather than only at its start. It also introduced the restrict keyword and improved support for floating-point behavior.
- **C11**
  - C11, published in 2011, introduced support for multithreading through <threads.h>, atomic operations via Atomic and <stdatomic.h>, and improved Unicode support. It also added optional bounds-checking functions intended to reduce common security vulnerabilities, though these saw limited adoption across compilers.
- **C17**
  - C17, published in 2018, is primarily a bug-fix and clarification release for C11, correcting defects and ambiguities in the standard's wording without introducing significant new language features. It is sometimes referred to as C18 due to its actual publication date.
- **C23**
  - C23 is the most recent major revision of the C standard, adding features such as improved type inference with auto in some contexts, new attributes, and additional standard library functions, while continuing to refine areas like Unicode support. Compiler support for C23 features varies and continues to roll out gradually across GCC, Clang, and other compilers.

---

## 4. Optional / Specialized Topics

- float
- vim / nvim
- VSCode
- volatile
- double
- char
- Extended Types
- Fixed-width integers
- Comparison
- _Atomic
- Ternary
- Command-Line Arguments
- main Function
- Pointer Arithmetic
- malloc
- calloc
- realloc
- free
- extern
- Dynamic Memory Allocation
- Memory Leakage
- Dangling Pointers
- setjmp / longjmp
- Buffer Overflow
- Math & Time

---

## 5. References

- [C Roadmap](https://roadmap.sh/c)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- DevOps Engineer

### Related Skills
- C++
- Rust
- Go