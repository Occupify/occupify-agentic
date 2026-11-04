# C++

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/cpp
- Related Roles:
  - Software Engineer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction to Language
- **What is C++?**
  - C++ is a powerful, general-purpose programming language. It is an extension of the C language, adding features like object-oriented programming, which allows you to structure code into reusable components.
- **Why use C++**
  - C++ is a powerful, general-purpose programming language known for its performance and control over system resources. It combines high-level and low-level features, allowing developers to write efficient code for a wide range of applications.
- **C vs C++**
  - C and C++ are both programming languages, with C++ evolving from C. C is a procedural language focused on structured programming using functions.

### 1.2 Setting up your Environment
- **Installing C++**
  - To use C++, you need to set up the necessary tools on your system to compile and run C++ code. This typically includes a compiler (like GCC or Clang), a build system (like Make or CMake), and an Integrated Development Environment (IDE) or text editor for writing code.
- **Code Editors / IDEs**
  - Choosing the right code editor or IDE is a crucial first step for any C++ developer. These tools provide a platform for writing, editing, and managing your code, often including features like syntax highlighting, code completion, debugging tools, and build automation.

### 1.3 Basic Operations
- **Arithmetic Operators**
  - Arithmetic operators are fundamental building blocks in C++ programming, allowing you to perform mathematical calculations directly within your code. These operators work on numeric data types such as integers and floating-point numbers, enabling addition (+), subtraction (-), multiplication (\), division (/), and modulus (%) operations.
- **Logical Operators**
  - Logical operators in C++ allow you to combine or modify boolean expressions, resulting in a final boolean value of either true (1) or false (0). These operators are crucial for controlling the flow of your program based on multiple conditions.

### 1.4 Control Flow & Statements
- **for / while / do while loops**
  - Loops are fundamental control flow structures that enable the repetition of code blocks based on a condition. C++ provides three primary loop types: for, while, and do-while.
- **if else / switch / goto**
  - if-else, switch, and goto are fundamental control flow mechanisms in C++. if-else constructs enable programs to execute different code blocks based on boolean conditions.

### 1.5 Functions
- **Static Polymorphism**
  - Static polymorphism, also known as compile-time polymorphism, enables the execution of different code depending on the type of data it's handling, but this determination happens at compile time. In C++, static polymorphism is primarily achieved through function overloading, which allows defining multiple functions with the same name but different parameter lists, and templates, which facilitate writing generic functions and classes that operate on various data types without runtime overhead.
- **Function Overloading**
  - Function overloading in C++ allows multiple functions to share the same name, provided they differ in the number or types of parameters. This facilitates compile-time polymorphism, enhancing code readability and maintainability by enabling functions to perform similar operations on different data types or argument counts.
- **Operator Overloading**
  - Operator overloading in C++ is a feature that allows you to redefine the way operators work for user-defined types (such as classes and structs). It lets you specify how operators like +, -, \, ==, etc., behave when applied to objects of your class.
- **Lambdas**
  - Lambdas, also known as lambda expressions, are a concise way to define anonymous functions directly within the code where they are needed. They are essentially nameless functions that can capture variables from the surrounding scope.

### 1.6 Data Types
- **Bitwise Operators**
  - Bitwise operators in C++ allow direct manipulation of individual bits within integer data types. These operators work by treating values as sequences of bits and performing operations at the bit level.
- **Static Typing**
  - Static typing, as implemented in C++, is a system where the data type of a variable is known and checked at compile time, before the program runs. This means each variable is declared with a specific type (like int, double, or char), and the compiler enforces that only values of that type are assigned to it.
- **Dynamic Typing**
  - While C++ is fundamentally a statically-typed language where data types are checked at compile time, it provides mechanisms to achieve a degree of dynamic typing. This involves determining the data types of variables during runtime, primarily through the use of void pointers, which can point to any data type (requiring explicit casting), and the std::any class (introduced in C++17), a type-safe container capable of holding values of any type.
- **RTTI**
  - Run-Time Type Identification (RTTI) in C++ allows you to determine the type of an object during program execution. This is particularly useful when working with polymorphism and inheritance.

---

## 2. Intermediate

### 2.1 Pointers and References
- **Running your First Program**
  - This involves configuring your system to compile and execute C++ code. You'll need a compiler (like GCC or Clang), an IDE or text editor for writing code, and potentially a build system to manage the compilation process.
- **References**
  - In C++, a reference is an alias for an existing variable. It provides an alternative name to access the same memory location.
- **Memory Model**
  - The C++ memory model defines how a program organizes and manages memory during execution. It divides memory into different segments, each serving a specific purpose: the stack for function calls and local variables, the heap for dynamic memory allocation, the data segment for global and static variables, and the code segment for executable instructions.
- **Lifetime of Objects**
  - Object lifetime in C++ dictates when an object comes into existence and when it ceases to exist. This crucial concept influences memory management and program correctness.
- **Smart Pointers**
  - Smart pointers are classes that behave like regular pointers but provide automatic memory management. They help prevent memory leaks by automatically deallocating the memory they point to when they are no longer needed.
- **weak_ptr**
  - weakptr is a smart pointer in C++ that holds a non-owning reference to an object managed by a sharedptr. It doesn't participate in the object's ownership count, meaning that it doesn't prevent the object from being destroyed if the sharedptrs owning the object go out of scope.

### 2.2 Structuring Codebase
- **Forward Declaration**
  - Forward declaration is declaring an identifier (like a class, function, or variable) to the compiler before its full definition is provided. This informs the compiler about the existence and type of the identifier, allowing it to be used in limited contexts, such as pointer or reference usage, without requiring the full definition to be immediately available.
- **shared_ptr**
  - sharedptr is a smart pointer in C++ that manages dynamically allocated memory. It enables multiple pointers to safely own and share the same object.
- **unique_ptr**
  - uniqueptr is a smart pointer in C++ that provides exclusive ownership of a dynamically allocated object. It ensures that only one uniqueptr can point to a given object at any time, preventing memory leaks by automatically deleting the managed object when the uniqueptr goes out of scope or is explicitly reset.
- **Scope**
  - Scope in C++ defines the visibility and lifetime of variables, functions, and other identifiers within a program. It dictates where these entities can be accessed and how long they persist in memory.
- **Namespaces**
  - Namespaces in C++ provide a way to organize code into logical groups, preventing naming conflicts when using code from different libraries or parts of a large project. They act as containers for variables, functions, classes, and even other namespaces.
- **Headers / CPP Files**
  - In C++, organizing code effectively involves splitting programs into header and source files. Header files (with extensions like .h or .hpp) declare interfaces such as classes, functions, and variables, acting as blueprints for other parts of the code.

### 2.3 Structures and Classes
- **Diamond Inheritance**
  - Diamond inheritance arises in C++ when a class inherits from multiple classes that, in turn, inherit from a common base class, creating a diamond-shaped hierarchy. This can lead to ambiguity because the derived class inherits multiple copies of the base class's members.
- **Multiple Inheritance**
  - Multiple inheritance in C++ allows a class to inherit from multiple base classes, combining their properties and behaviors into a single derived class. This means a class can inherit data members and member functions from several parent classes, offering a way to create more complex and specialized classes.
- **Object Oriented Programming**
  - Object-oriented programming is a style of programming centered around "objects," which combine data (attributes) and functions (methods) that operate on that data. OOP enables you to create modular, reusable, and maintainable code by organizing your programs around these objects and their interactions.
- **Virtual Methods**
  - Virtual methods are the cornerstone of dynamic polymorphism in C++ classes. They enable a derived class to provide its own specific implementation of a function that is already defined in a base class.
- **Virtual Tables**
  - Virtual tables (vtables) are compiler-generated lookup tables used in C++ to implement dynamic polymorphism, especially with virtual functions. Each class that declares or inherits virtual functions has a vtable, which contains pointers to the most derived versions of those virtual functions for that class.
- **Dynamic Polymorphism**
  - Dynamic polymorphism is a feature in C++ that allows objects of different classes to be treated as objects of a common type. This is achieved through virtual functions, where a derived class can override a function defined in its base class.
- **SFINAE**
  - SFINAE is a core principle in C++ template metaprogramming that enables the compiler to choose the most suitable function or class template specialization during compilation. It leverages the idea that when the compiler attempts to substitute template arguments into a template and the substitution results in an invalid type or expression, this failure is not immediately treated as a compilation error.

### 2.4 Exception Handling
- **Rule of Zero, Five, Three**
  - The Rule of Zero, Three, and Five are guidelines for managing resources within C++ classes and structs. The Rule of Zero suggests letting the compiler handle resource management if your class doesn't explicitly manage any.
- **Exit Codes**
  - Exit codes are numerical values returned by a program to the operating system upon completion, signaling whether the execution was successful or encountered errors. A return value of 0 typically indicates success, while non-zero values denote failure, with the specific meaning of each non-zero code being application-dependent.
- **Exceptions**
  - Exception handling in C++ provides a mechanism to manage runtime errors, ensuring program stability. This is achieved using try, catch, and throw blocks.
- **Template Specialization**
  - Template specialization in C++ allows you to provide custom implementations of templates for specific types or type patterns. This becomes useful when the generic template implementation doesn't suit a particular type, requiring tailored logic for optimization or specific behavior.
- **Type Traits**
  - Type traits in C++ are a powerful set of tools, implemented as template classes, found in the <typetraits> header. They provide a mechanism to inspect and query the properties of types at compile time, such as whether a type is a pointer, arithmetic type, or function.

### 2.5 Language Concepts
- **Raw Pointers**
  - Raw pointers are variables that store the memory address of another variable. They directly hold the location in memory where a value is stored, allowing you to access and manipulate that value.
- **New/Delete Operators**
  - The new and delete operators in C++ are used for dynamic memory allocation and deallocation. new allocates a block of memory on the heap and returns a pointer to the beginning of that block.
- **Memory Leakage**
  - Memory leakage occurs when dynamically allocated memory is no longer accessible by the program, but the program fails to release it back to the operating system. This results in the memory being unusable by other parts of the program or other applications, gradually reducing the available memory and potentially leading to performance degradation or even program crashes.
- **auto (Automatic Type Deduction)**
  - auto is a keyword in C++ introduced in C++11 that enables automatic type deduction. It allows the compiler to infer the data type of a variable from its initialization expression at compile time.
- **Type Casting**
  - Type casting in C++ involves converting a variable's data type to another. C++ provides several casting methods: C-style casting (inherited from C), staticcast (for explicit conversions at compile time), dynamiccast (for safe downcasting in class hierarchies), reinterpretcast (for low-level bitwise reinterpretation), and constcast (to modify the constness of variables).
- **static_cast**
  - staticcast is a C++ casting operator primarily used for performing conversions between related types at compile time. This includes converting between primitive data types like int and float, and upcasting or downcasting within inheritance hierarchies.
- **dynamic_cast**
  - dynamiccast is a C++ casting operator primarily used within polymorphic class hierarchies to safely convert pointers or references from a base class to a derived class. Unlike static casts, it performs a runtime check to ensure the validity of the conversion.

### 2.6 Standard Library + STL
- **Access Violations**
  - An access violation occurs when a program tries to read from or write to a memory location that it doesn't have permission to access. This is a common error in C++ that can arise from issues like dereferencing null or invalid pointers, accessing arrays beyond their bounds, or attempting to use memory that has already been freed.
- **const_cast**
  - constcast is a C++ casting operator that allows you to explicitly add or remove the const or volatile qualifier from a variable's type. This essentially enables you to modify an object that was initially declared as const or pass a const object to a function that expects a non-const argument.
- **reinterpret_cast**
  - reinterpretcast is a powerful but potentially dangerous type of casting operator in C++. It allows you to convert between unrelated pointer types, integer types, or between pointers and integers.
- **Undefined Behavior (UB)**
  - Undefined behavior in C++ arises when a program violates the rules defined by the C++ standard, leading to unpredictable and unspecified outcomes. This can stem from actions such as accessing uninitialized variables, dereferencing null pointers, performing out-of-bounds memory access, or dividing by zero.
- **Argument Dependent Lookup (ADL)**
  - Argument Dependent Lookup (ADL), also known as Koenig Lookup, is a feature in C++ that extends the function lookup process by allowing the compiler to search for functions in the namespaces of the function arguments' types. This is especially useful when working with overloaded operators and functions defined within namespaces, enabling more intuitive and concise code by automatically finding the appropriate function based on the argument types, even if it's not explicitly qualified.
- **Name Mangling**
  - Name mangling, also known as name decoration, is a technique compilers use to encode extra information like scope, type, and linkage into identifier names (like function and variable names). This allows C++ to support function overloading, where multiple functions can share the same name but have different parameters.
- **Macros**
  - Macros in C++ are preprocessing directives that instruct the preprocessor to perform text substitutions before compilation. Defined using #define, they enable you to create symbolic constants, function-like constructs, and control conditional compilation.
- **Iterators**
  - Iterators in C++'s Standard Template Library (STL) are essential tools for traversing and accessing elements within containers like vectors, lists, and arrays. They act as generalized pointers, offering a way to interact with container elements without needing to know the container's underlying implementation.
- **iostream**
  - iostream is a fundamental header in the C++ Standard Library that handles input and output (I/O) operations. It provides classes like istream for input, ostream for output, and iostream for combined I/O.
- **Algorithms**
  - The C++ Standard Template Library (STL) offers a rich collection of generic algorithms that operate on various container types. These algorithms, found primarily in the <algorithm> header, provide functionalities for common tasks like sorting, searching, and sequence manipulation.
- **Date / Time**
  - The C++ chrono library, part of the Standard Template Library (STL), offers tools for handling dates and times. It allows you to represent time spans as durations (e.g., seconds, minutes, hours), specific moments as timepoints based on clocks, and access the current time using different clock types like systemclock, steadyclock, and highresolutionclock.
- **Multithreading**
  - Multithreading allows concurrent execution of multiple threads within a single process, enhancing application performance by enabling parallel task execution. C++ provides multithreading support through the <thread> library (introduced in C++11), enabling thread creation, argument passing, and synchronization mechanisms like mutexes and locks to manage shared resource access and prevent data races.
- **GDB**
  - GDB, the GNU Project Debugger, is a command-line tool essential for debugging C and C++ programs. It allows developers to examine a program's execution, set breakpoints, step through code, inspect variables, and analyze call stacks to identify and fix bugs.

### 2.7 Templates
- **Variadic Templates**
  - Variadic templates, introduced in C++11, provide a way to create templates that can accept a variable number of arguments. Using the ellipsis (...) notation, you can define parameter packs that represent zero or more arguments of potentially different types.
- **Full Template Specialization**
  - Full template specialization in C++ provides a way to define specific implementations of a template (class or function) for particular types. This allows you to customize the behavior of a template when it's instantiated with a specific set of template arguments, enabling optimized code or special handling for certain types while the generic template handles other cases.
- **Partial Template Specialization**
  - Partial template specialization in C++ allows you to create specialized versions of a template for specific subsets of types. This is achieved by providing a new template definition that is selected by the compiler when the template arguments match the specified criteria.

### 2.8 Idioms
- **Non-Copyable / Non-Moveable**
  - The non-copyable/non-moveable idiom in C++ prevents objects of a class from being copied or moved. This is achieved by deleting the copy constructor, copy assignment operator, move constructor, and move assignment operator.
- **Erase-Remove**
  - The Erase-Remove idiom is a common C++ technique used to efficiently remove elements from a container (like std::vector, std::list, etc.). It involves using std::remove (or std::removeif) to move the elements to be removed to the end of the container, followed by using the container's erase() method to actually remove those elements, effectively shrinking the container.
- **Copy and Swap**
  - Copy and Swap is a C++ idiom used to implement the assignment operator in a safe and efficient manner. It works by creating a copy of the right-hand side object, then swapping the internal state of the copy with the object being assigned to.
- **Copy on Write**
  - The Copy-on-Write (CoW) idiom is an optimization technique used to defer or eliminate the cost of copying resources until the first write operation. Instead of creating a new copy of an object immediately, the original object and the "copy" share the same underlying resource.
- **Pimpl**
  - The Pimpl (Pointer to Implementation) idiom is a C++ technique used to hide the implementation details of a class. This is achieved by declaring a private implementation class and holding a pointer to it within the main class.
- **CRTP**
  - The Curiously Recurring Template Pattern (CRTP) is a C++ idiom where a class template inherits from its own specialization. This technique achieves static polymorphism, offering an alternative to runtime polymorphism using virtual functions.

---

## 3. Advanced

### 3.1 Standards
- **Containers**
  - C++ Containers are a part of the Standard Template Library (STL) that provide data structures to store and organize data. There are several types of containers, each with its own characteristics and use cases.
- **C++ 11 / 14**
  - C++11 and C++14 are significant updates to the C++ language, introducing features to enhance its power and usability. C++11 brought in features like auto for type inference, range-based for loops for simpler iteration, lambda functions for creating anonymous functions, nullptr for safer null pointer representation, and a standard thread support library.
- **C++ 17**
  - C++17 is a significant update to the C++ language, offering new features and enhancements that improve code expressiveness and efficiency. This version introduces features such as structured bindings for easier data unpacking, if and constexpr if statements for compile-time conditional logic, and inline variables for simplified header usage.
- **C++ 20**
  - C++20 represents a significant evolution of the C++ language, introducing key features aimed at improving code clarity, efficiency, and concurrency. Highlights include Concepts, which enforce constraints on template parameters for better error messages; Ranges, a new way to work with sequences of values enhancing standard library algorithms; Coroutines, for writing asynchronous code with improved readability; and enhancements to compile-time evaluation with constexpr and consteval.
- **C++ 23**
  - C++23 is the latest version of the C++ standard, building upon previous iterations to introduce new features, library enhancements, and language improvements. It aims to simplify development, improve performance, and provide more modern tools for C++ programmers.

### 3.2 Debuggers
- **Understanding Debugger Messages**
  - Debugger messages are notifications from a debugger that aid in identifying issues within C++ code. These messages manifest as warnings, errors, or informational outputs, offering insight into the program's state and specific problems encountered during debugging.
- **Debugging Symbols**
  - Debugging symbols are essential for effective debugging in C++. They provide debuggers with information about the program's structure, source code relationships, and variable representations, allowing developers to step through code, inspect variables, and understand the program's behavior.
- **WinDBg**
  - WinDbg, a debugger included in the Microsoft Windows SDK, is a powerful tool for analyzing and debugging Windows applications, both in user mode and kernel mode. It offers a graphical interface and a comprehensive set of features for tasks like analyzing crash dumps, setting breakpoints, and stepping through code execution to identify and resolve issues in your C++ programs.

### 3.3 Compilers
- **Compiler Stages**
  - The compilation process in C++ transforms human-readable source code into an executable program through four distinct stages. These stages are: Preprocessing, which handles directives like #include and macro replacements; Compilation, where the preprocessed code is translated into assembly language; Assembly, which converts the assembly code into object code; and Linking, where object code is combined with libraries to create the final executable.
- **Compilers and Features**
  - C++ compilers translate human-readable C++ code into machine-executable code. They offer various features, including optimization techniques to improve program performance by eliminating redundancies and restructuring code, debugging information generation to aid in troubleshooting, and warning systems to flag potentially problematic code.

### 3.4 Build Systems
- **CMAKE**
  - CMake is a cross-platform build system generator. It uses configuration files (CMakeLists.txt) to describe the build process and generates native build files like Makefiles or project files for IDEs like Visual Studio.
- **Makefile**
  - A Makefile is a configuration file used by the make utility to automate the process of compiling and linking code in a project. It defines a set of rules and dependencies that specify how to build the final executable or library from source code.
- **Ninja**
  - Ninja is a small, fast build system designed for speed and efficiency. Instead of directly interpreting project structure, it executes pre-generated build plans.

### 3.5 Package Managers
- **vcpkg**
  - vcpkg is an open-source, cross-platform package manager for C and C++ libraries that simplifies the acquisition and building of dependencies. Supporting Windows, Linux, and macOS, it streamlines the integration of external libraries into your projects through search, installation, and removal commands.
- **NuGet**
  - NuGet is a package manager initially designed for the .NET ecosystem, but it also extends its functionality to C++ projects through the PackageReference format. It simplifies the process of adding, updating, and managing external libraries and dependencies within your C++ projects, whether you're using Visual Studio's GUI, its integrated command-line tools, or the standalone nuget.exe executable.
- **Conan**
  - Conan is a package manager specifically designed for C and C++ projects. It helps developers manage dependencies, build configurations, and share pre-built libraries across different platforms and build systems like CMake and Visual Studio.
- **Spack**
  - Spack is a package manager designed for flexibility and support for multiple versions, configurations, platforms, and compilers, making it especially useful in High Performance Computing (HPC) environments. It automates the process of installing and managing dependencies, enabling users to build complex software stacks with fine-grained control over their components.

### 3.6 Working with Libraries
- **RAII**
  - RAII (Resource Acquisition Is Initialization) is a C++ idiom that ties the management of resources to the lifetime of objects. Resources are acquired during object construction and automatically released when the object is destroyed, typically in the destructor.
- **C++ 0x**
  - C++11, formerly known as C++0x, represents a significant evolution of the C++ language standard, finalized in 2011. This version introduced features like automatic type inference with auto, simplified container iteration using range-based for loops, the ability to create anonymous functions via lambda expressions, and a safer way to represent null pointers using nullptr.
- **Library Inclusion**
  - In C++, library inclusion is the process of making external code available to your program. This is achieved primarily through the #include preprocessor directive, which allows you to incorporate header files containing declarations of functions, classes, and other entities.
- **Licensing**
  - Licensing governs how you can use, modify, and distribute software libraries, particularly crucial when integrating third-party code into your C++ projects. Common open-source licenses like MIT, GPL, and Apache 2.0 each provide different levels of freedom and obligations.
- **Boost**
  - Boost is a set of peer-reviewed, portable C++ source libraries. It provides a wide range of utilities and tools that can significantly enhance your C++ development, covering areas like data structures, algorithms, mathematical functions, concurrency, and more.
- **OpenCV**
  - OpenCV (Open Source Computer Vision Library) is a comprehensive collection of programming functions primarily aimed at real-time computer vision. It encompasses a vast array of algorithms for image processing, object detection, video analysis, and machine learning, providing developers with tools to analyze and manipulate visual data.
- **POCO**
  - POCO (Portable Components) is a C++ class library that simplifies network-centric, portable applications. It offers a comprehensive set of tools and components for tasks such as networking, data processing, and basic utilities.
- **protobuf**
  - Protobuf (Protocol Buffers) is a language-neutral, platform-neutral, extensible mechanism for serializing structured data. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams, using a variety of languages.
- **gRPC**
  - gRPC is a high-performance, open-source framework developed by Google for building remote procedure calls (RPCs). It uses Protocol Buffers as its Interface Definition Language (IDL) and relies on HTTP/2 for transport.
- **Tensorflow**
  - TensorFlow is an open-source software library developed by Google, primarily used for numerical computation and large-scale machine learning. It allows developers to create and train machine learning models using a variety of tools, libraries, and community resources.
- **pybind11**
  - pybind11 is a lightweight header-only library that allows you to create Python bindings for your existing C++ code. It essentially lets you expose C++ functions, classes, and data structures to Python, enabling seamless interoperability between the two languages.
- **spdlog**
  - spdlog is a fast and cross-platform C++ logging library. It provides a simple interface for writing log messages to different destinations such as the console, files, or custom sinks.
- **opencl**
  - OpenCL (Open Computing Language) is a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, and other processors. It allows developers to harness the parallel processing power of different types of hardware using a unified API, enabling acceleration of computationally intensive tasks.
- **fmt**
  - fmt is a modern formatting library for C++. It provides a simple and efficient way to format text, similar to Python's str.format() or C#'s string.Format().
- **ranges_v3**
  - Ranges v3 is a modern C++ library that provides tools for working with sequences of elements in a more composable and expressive way. It introduces concepts like views and algorithms that operate on ranges, allowing you to chain operations together to process data efficiently and elegantly without relying heavily on iterators.
- **gtest / gmock**
  - Google Test and Google Mock are open-source C++ unit testing frameworks developed by Google. Google Test is a standalone framework for writing and running unit tests, while Google Mock extends it with powerful mocking capabilities.
- **Qt**
  - Qt is a cross-platform application development framework widely used for creating graphical user interfaces (GUIs) and applications that run on various operating systems, such as Windows, macOS, Linux, and embedded systems. It provides a set of tools and libraries that simplify the development process, offering features like widgets, networking, database access, and multimedia support.
- **Catch2**
  - Catch2 is a modern, C++-native, header-only framework for writing unit tests, benchmarks, and even simple command-line applications. It provides a simple and expressive syntax for defining test cases, assertions, and sections, making it easy to write and maintain comprehensive tests for your C++ code.
- **Orbit Profiler**
  - Orbit Profiler is a performance analysis tool designed to help developers identify bottlenecks and optimize the performance of their applications. It provides detailed insights into CPU usage, memory allocation, and other performance metrics through sampling and tracing.
- **PyTorch C++**
  - PyTorch C++ provides a front-end for the PyTorch machine learning framework, allowing you to build and deploy models using C++ instead of Python. This enables you to leverage the performance and control of C++ for computationally intensive tasks, especially in production environments where low latency and resource efficiency are critical.

---

## 4. Optional / Specialized Topics

- Name Mangling
- C++ 0x
- WinDBg
- GDB
- Compilers and Features
- Makefile
- Ninja
- vcpkg
- NuGet
- Conan
- Spack
- OpenCV
- POCO
- protobuf
- gRPC
- Tensorflow
- pybind11
- spdlog
- opencl
- fmt
- ranges_v3
- Qt
- Catch2
- Orbit Profiler
- PyTorch C++

---

## 5. References

- [C++ Roadmap](https://roadmap.sh/cpp)

---

## 6. Related Roles / Topics

### Related Roles
- Software Engineer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- Rust
- Linux
- Python
- Computer Science
- Java
- Data Structures & Algorithms