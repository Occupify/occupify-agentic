# Swift & SwiftUI

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/swift-ui
- Related Roles:
  - iOS Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is Swift?**
  - Swift is a modern, general-purpose programming language developed by Apple. It's designed to be safe, fast, and expressive, making it a great choice for building applications across Apple's platforms, including iOS, macOS, watchOS, and tvOS.
- **Why use Swift?**
  - Swift is a modern, powerful, and intuitive programming language developed by Apple. It's designed to be safe, fast, and expressive, making it an excellent choice for building applications across Apple's ecosystems, including iOS, macOS, watchOS, and tvOS.
- **Swift vs Objective-C**
  - Swift and Objective-C are both programming languages used to develop applications for Apple's operating systems (iOS, macOS, watchOS, tvOS). Objective-C is an older language, built as an extension of C, while Swift is a more modern language designed to be safer, faster, and easier to learn.
- **Where Swift is used?**
  - Swift is a versatile programming language developed by Apple, primarily known for building applications across the Apple ecosystem. This includes creating apps for iPhones, iPads, Macs, Apple Watches, and Apple TVs.

### 1.2 Constants & Variables
- **Constants & Variables**
  - Constants and variables are fundamental building blocks in Swift for storing data. A variable holds a value that can be changed during the execution of a program, while a constant holds a value that, once assigned, cannot be altered.

### 1.3 Installing Swift
- **Installing Swift**
  - Installing Swift involves setting up the Swift compiler and related tools on your system, allowing you to write and run Swift code. This typically involves downloading a Swift toolchain from the official Swift.org website or using a package manager like Homebrew on macOS or apt on Linux.

### 1.4 Type Annotations
- **Type Annotations**
  - Type annotations in Swift are a way to explicitly specify the type of a variable or constant. Instead of letting Swift infer the type based on the initial value, you tell the compiler exactly what kind of data the variable will hold, such as an Int, String, or Bool.

### 1.5 Print & String Interpolation
- **Print & String Interpolation**
  - In Swift, print() is a function used to display values in the console, which helps debug and see the output of your code. String interpolation allows you to embed variables or expressions directly within a string.

### 1.6 Comments
- **Comments**
  - Comments in Swift are notes within your code that the compiler ignores. They're used to explain what the code does, making it easier for you and others to understand.

### 1.7 Semicolons
- **Integers**
  - Integers in Swift are whole numbers, meaning they don't have any fractional or decimal parts. They can be positive, negative, or zero.
- **Floats & Doubles**
  - Floats and Doubles are fundamental data types in Swift used to represent numbers with fractional components (decimal numbers). A Float represents a 32-bit floating-point number, offering a balance between memory usage and precision.
- **Booleans**
  - Booleans represent truth values, either true or false. They are fundamental for controlling program flow, making decisions based on conditions, and representing binary states.
- **Optionals & nil**
  - In Swift, an optional is a type that can hold either a value or the absence of a value (represented by nil). It's a way to indicate that a variable might not have a value at a particular time.

### 1.8 Operators
- **Type Safety**
  - Thanks to type safety, Swift prevents you from accidentally using a value in a way that's not intended. Swift checks the types of your variables and constants during compilation.
- **Type Casting**
  - Type casting is a way to check the type of an instance, or to treat that instance as if it were a different superclass or subclass from somewhere else in its own class hierarchy. It's essentially a way to access an object as a different type than it was originally declared to be.
- **Type Inference**
  - Type inference is a feature in Swift that allows the compiler to automatically deduce the data type of a variable or constant based on the value assigned to it. This means you don't always have to explicitly declare the type when creating variables; Swift can figure it out for you, making your code cleaner and more concise.
- **Memory Safety**
  - Memory safety in Swift is a set of language features that prevent common programming errors related to memory access. It ensures that your program accesses memory predictably and safely, preventing issues like accessing memory that has already been deallocated (dangling pointers) or writing outside the bounds of an allocated memory region (buffer overflows).
- **Arithmetic**
  - Arithmetic operators are special symbols that perform mathematical calculations on values. Swift provides standard arithmetic operators like addition (+), subtraction (-), multiplication (), and division (/).
- **Logical**
  - Logical operators in Swift allow you to combine or modify Boolean (true/false) values. They are used to create more complex conditions in your code.
- **Comparison**
  - Comparison operators are symbols used to compare two values. These operators evaluate to a Boolean value (either true or false) based on the relationship between the values being compared.
- **Nil-Coalescing**
  - The nil-coalescing operator ( ?? ) provides a default value when an optional is nil.

### 1.9 if / else
- **if / else**
  - if and else statements are fundamental control flow structures in Swift that allow your code to execute different blocks of code based on whether a condition is true or false. The if statement evaluates a Boolean expression, and if the expression is true, the code within the if block is executed.

### 1.10 Basic Functions
- **Strings**
  - In Swift, a string is a sequence of characters, like letters, numbers, and symbols. It's a fundamental data type used to represent text.
- **Tuples**
  - Tuples in Swift are a way to group multiple values into a single compound value. Unlike arrays, the values within a tuple can be of different types.

### 1.11 switch / case
- **switch / case**
  - A switch statement allows you to control which block of code is executed based on the value of a variable or expression. It compares the value against several possible cases, and executes the code associated with the first matching case.

### 1.12 Parameters
- **Parameters**
  - Parameters are named values that you pass into a function or closure when you call it. They act as inputs, allowing the function or closure to operate on specific data.

### 1.13 Return Types
- **Return Types**
  - In Swift, a return type specifies the kind of data a function or closure sends back to the caller after it has finished executing. If a function performs a calculation or processes data, the return type indicates what type of result you can expect.

### 1.14 Loops
- **for**
  - In Swift, a for loop provides a clean and concise way to iterate over a sequence of items, such as elements in an array, characters in a string, or a range of numbers. It executes a block of code repeatedly for each item in the sequence.
- **while**
  - A while loop in Swift repeatedly executes a block of code as long as a specified condition is true. The loop checks the condition before each execution of the code block.
- **repeat..while**
  - The repeat...while loop in Swift executes a block of code at least once, and then continues to repeat the block as long as a specified condition is true. Unlike the while loop, which checks the condition before executing the code, the repeat...while loop checks the condition after executing the code.

---

## 2. Intermediate

### 2.1 Error Handling
- **throwing**
  - Throwing errors allows you to signal that something unexpected or problematic has occurred during the execution of your code. When a function encounters a situation it can't handle normally, it can throw an error.
- **propagating**
  - Error propagation in Swift is the process of passing an error up the call stack until it's handled by a catch block. When a function encounters an error it can't resolve, it throws the error.
- **catching**
  - Handling errors involves catching potential problems that may occur during code execution. When a function or method can throw an error, you use a do-catch block to try executing the code that might fail.

### 2.2 Function Types
- **Function Types**
  - In Swift, functions are first-class citizens, meaning they can be treated like any other data type. A function type describes the parameters a function accepts and the type of value it returns.

### 2.3 Nested Functions
- **Nested Functions**
  - Nested functions are functions defined inside the body of another function. The outer function is called the enclosing function, and the inner function is the nested function.

### 2.4 Closures
- **Closures**
  - Closures in Swift are self-contained blocks of functionality that can be passed around and used in your code. Think of them as mini-functions without a name.

### 2.5 Trailing Closures
- **Trailing Closures**
  - A trailing closure is a closure that's written after the function's parentheses. If a function's last parameter is a closure, you can pass the closure outside of the parentheses when you call the function.

### 2.6 Enumerations
- **continue & break**
  - In Swift, continue and break are control flow statements used within loops (like for, while, and repeat-while) to alter their execution. The continue statement skips the rest of the current iteration of the loop and proceeds to the next iteration.

### 2.7 Protocols
- **Protocols**
  - A protocol in Swift defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality. Classes, structures, and enumerations can then adopt these protocols, providing concrete implementations for the requirements specified by the protocol.

### 2.8 Structures & Classes
- **Inheritance**
  - Inheritance is a fundamental concept in object-oriented programming where a new class (called a subclass or derived class) can inherit properties and methods from an existing class (called a superclass or base class). This allows you to create a hierarchy of classes, where subclasses inherit and extend the functionality of their superclasses, promoting code reuse and establishing relationships between different types of objects.
- **Methods**
  - Methods are functions that are associated with a particular type, like a structure or a class. They provide a way to encapsulate behavior and data together.
- **Initialization**
  - Initialization is the process of preparing an instance of a class, structure, or enumeration for use. This involves setting an initial value for each stored property on that instance and performing any other setup or initialization required before the new instance is ready.
- **Properties**
  - Properties associate values with a particular class, structure, or enumeration. Stored properties store constant or variable values as part of an instance, whereas computed properties calculate (rather than store) a value.
- **Optional Chaining**
  - Optional chaining is a feature that allows you to access properties, methods, and subscripts of an optional value. If the optional contains a value, the property, method, or subscript is accessed as normal.
- **Subscripts**
  - Subscripts are shortcuts for accessing elements within a collection, list, or sequence. They allow you to query instances of a type by writing one or more values in square brackets after the instance name.
- **Extensions**
  - Extensions in Swift are a way to add new functionality to an existing class, structure, enumeration, or protocol type. They allow you to extend types even if you don't have access to the original source code.
- **Text**
  - Text is a fundamental view used to display static, read-only text on the screen. It allows you to present strings, apply formatting like fonts, colors, and styles, and handle localization for different languages.
- **Computed**
  - Computed properties in Swift provide a way to calculate a value rather than storing it directly. Unlike stored properties, which hold a value in memory, computed properties offer a getter to retrieve a value and an optional setter to indirectly set other properties.
- **Wrappers**
  - Property wrappers in Swift provide a way to add a layer of code between the property and the code that manages it. They essentially encapsulate code that gets executed when a property is accessed or modified.

### 2.9 Generics
- **Stored**
  - Stored properties are variables or constants that are part of a structure or class. They hold data directly within an instance of that structure or class.
- **Observers**
  - Property observers in Swift allow you to monitor and respond to changes in a property's value. You can define code that will be executed before (willSet) or after (didSet) a property's value is set.

### 2.10 What is SwiftUI
- **UIKit vs SwiftUI**
  - UIKit and SwiftUI are both frameworks for building user interfaces on Apple platforms (iOS, iPadOS, macOS, watchOS, and tvOS). UIKit is the older, imperative framework that has been around since the first iPhone was introduced.

### 2.11 App lifecycle
- **NavigationStack**
  - NavigationStack provides a way to manage hierarchical navigation within your app. It allows users to move forward and backward through a stack of views, similar to how you navigate through folders on a computer.

### 2.12 Views
- **font**
  - The font modifier in SwiftUI allows you to customize the appearance of text within your views by specifying the typeface, weight, and size. It provides a way to control how text is displayed, enabling you to create visually appealing and consistent user interfaces.
- **padding**
  - Padding in Swift and SwiftUI is used to add space around the content of a view. It essentially creates a buffer zone between the view's content and its surrounding elements or the edges of its parent view.

### 2.13 Data Flow
- **@State**
  - @State is a property wrapper in SwiftUI that allows you to manage the state of a view. It's used to store values that can change over time and trigger updates to the view when they do.
- **@ObservedObject**
  - @ObservedObject is a property wrapper in SwiftUI used to subscribe to an external class that conforms to the ObservableObject protocol. When the observable object publishes changes (typically through @Published properties), any views observing it will automatically update to reflect the new data.
- **@StateObject**
  - @StateObject is a property wrapper used to manage the lifecycle of reference type objects (classes) that hold state for a view. It ensures that the object is created only once when the view appears and persists across view updates, preventing the object from being re-initialized every time the view redraws.
- **@Binding**
  - @Binding creates a two-way connection between a view and a source of truth that lives elsewhere. It essentially provides a way for a view to read and modify a value that's owned and managed by another view or data structure.

### 2.14 Animations
- **Image**
  - Image is a fundamental view used to display pictures or graphics within your app's user interface. It allows you to load images from various sources, such as your app's asset catalog, the file system, or even remote URLs, and present them to the user.
- **Button**
  - A Button is a fundamental UI element that triggers an action when tapped or clicked. It's essentially a tappable area on the screen that, when interacted with, executes a predefined piece of code.
- **List**
  - A List is a container view that arranges data in a single column, making it easy to display scrollable collections of items. It's similar to a table view in UIKit, but with a more declarative and flexible approach.
- **Form**
  - In Swift and SwiftUI, a Form is a container view that's designed to organize and display input controls, such as text fields, toggles, and pickers. It automatically handles the layout and styling of these controls, making it easier to create structured and user-friendly interfaces for collecting data or configuring settings.
- **clipShape**
  - clipShape in SwiftUI allows you to mask a view, effectively cropping it to a specific shape. Instead of displaying the entire rectangular area of a view, clipShape lets you define a shape (like a circle, rectangle with rounded corners, or even a custom shape), and only the portion of the view that falls within that shape will be visible.
- **background**
  - The background view modifier in SwiftUI allows you to set a background for a view. This background can be a color, a shape, or even another view.
- **Implicit animations**
  - Implicit animations in Swift UI provide a simple way to animate changes to a view's properties. When a property that affects the view's appearance changes, and an animation modifier is attached to the view, Swift UI automatically animates the transition between the old and new values.
- **Transitions**
  - Transitions define how views appear and disappear from the screen. They control the visual effects applied during these changes, allowing you to create smooth and engaging user experiences.
- **HStack**
  - An HStack is a layout container that arranges its child views in a horizontal line. It's like a row where you place different UI elements side-by-side.
- **VStack**
  - A VStack is a layout container that arranges its child views in a vertical line. It's like stacking building blocks on top of each other.
- **ZStack**
  - ZStack is a layout container that overlays views on top of each other, aligning them in both the horizontal and vertical axes. The views are stacked in the order they are declared, with the last view in the code appearing on top.
- **Grid**
  - A Grid is a layout container that arranges views in a two-dimensional grid, similar to a table. It allows you to organize content into rows and columns, providing a structured way to display information and create complex layouts.
- **GeometryReader**
  - GeometryReader is a container view that provides information about its own size and position within its parent view. It allows you to access the available space offered by the parent, enabling you to create views that adapt dynamically to different screen sizes and orientations.
- **NavigationPath**
  - NavigationPath provides a way to manage the navigation stack programmatically. Instead of relying solely on NavigationLink to push views onto the stack, NavigationPath allows you to manipulate the navigation history directly.
- **TabView**
  - TabView allows you to create an interface with multiple distinct views, each accessible through a tab bar at the bottom (or top, depending on the platform). It's a container view that manages a collection of child views, presenting one at a time based on the user's tab selection.
- **NavigationLink**
  - NavigationLink enables navigation between different views within your app. It acts as a button or tappable element that, when activated, pushes a new view onto the navigation stack, displaying it to the user.
- **ViewBuilder**
  - ViewBuilder is a result builder attribute in Swift that allows you to build complex views in a declarative and concise way. It essentially transforms a series of statements into a single view, automatically handling the logic of combining multiple views together.
- **Explicit animations**
  - Explicit animations involve directly controlling the animation's behavior by specifying its parameters, such as duration, delay, and easing. Instead of relying on implicit transitions triggered by state changes, you define exactly how a view's properties animate from one value to another.
- **Animatable Protocol**
  - The Animatable protocol allows you to customize how changes to your custom data types are animated in SwiftUI. By conforming to this protocol, you define a var animatableData: Self.AnimatableData property that SwiftUI uses to interpolate between the starting and ending values of your data during an animation.

### 2.15 User Interaction
- **@EnvironmentObject**
  - @EnvironmentObject allows you to share data across your entire app or specific parts of your view hierarchy without having to manually pass it down through each view. It's a way to make data accessible to any view that needs it, acting like a global state container that SwiftUI manages.
- **UI Controls**
  - UI Controls are the visual building blocks that users interact with in an app's interface. These elements, such as buttons, text fields, sliders, and switches, allow users to input data, trigger actions, and navigate through the application.
- **Gestures**
  - Gestures are actions performed by a user to interact with a device's screen, such as tapping, swiping, pinching, or rotating. They allow users to directly manipulate and control elements within an application, providing a more intuitive and engaging experience.
- **Drag & Drop**
  - Drag and drop is a user interface interaction that allows users to select an item (the "drag") and move it to a different location (the "drop"). This interaction is commonly used for rearranging items in a list, moving files between folders, or transferring data between different parts of an application.
- **Localization**
  - Localization is the process of adapting your app to different languages, regions, and cultures. This involves translating text, adjusting layouts for different reading directions, and formatting dates, times, and currencies according to local conventions.
- **Accessibility**
  - Accessibility focuses on making your app usable by everyone, including people with disabilities. This involves providing alternative ways to interact with your app's content and controls, such as using screen readers, switch controls, or larger fonts.
- **Core Data**
  - Core Data is a framework provided by Apple for managing the model layer objects in your application. It's not a database itself, but rather an object graph management and persistence framework.
- **SwiftData**
  - SwiftData is Apple's modern framework for managing an app's data model and persisting data locally. It provides a declarative and type-safe way to define your data schema, interact with the underlying storage (typically SQLite), and manage relationships between different data entities.

### 2.16 Access Control
- **Access Control**
  - Access control lets you restrict which parts of your code can be used and accessed by other parts of your code, or from code in other files and modules. It's like setting permissions on different components of your app, ensuring that sensitive data and internal workings are protected from unintended use or modification.

### 2.17 ARC
- **ARC**
  - Automatic Reference Counting (ARC) is a memory management feature in Swift that automatically frees up memory used by class instances when they are no longer needed. It works by tracking how many references exist to each object.

### 2.18 Result Builders
- **Asynchronous Functions**
  - Asynchronous functions allow your program to start a potentially long-running task and then continue executing other code without waiting for that task to complete. When the asynchronous task finishes, it can notify your program, which can then process the results.

---

## 3. Advanced

### 3.1 Macros
- **Asynchronous Sequences**
  - Asynchronous sequences allow you to iterate over a series of values that arrive over time, potentially from different threads or even across a network. Unlike regular sequences, where all elements are immediately available, asynchronous sequences produce elements as they become available, enabling you to handle data streams, network responses, or any other data source that emits values asynchronously.
- **Tasks & Task Groups**
  - Tasks in Swift's concurrency model represent units of work that can be executed concurrently. Task Groups allow you to create and manage collections of child tasks, enabling you to perform parallel operations and aggregate their results.
- **Unstructured Concurrency**
  - Unstructured concurrency in Swift allows you to create and manage concurrent tasks without adhering to a strict parent-child relationship. This means you can launch asynchronous operations independently, and their lifecycles are not necessarily tied to the scope in which they were created.
- **Actors**
  - Actors are a concurrency model that provides a way to isolate state and prevent data races in concurrent Swift programs. They encapsulate mutable state and allow access to that state only through asynchronous message passing.

### 3.2 Data persistance
- **Strict Concurrency Checking**
  - Strict concurrency checking is a feature that helps you write safer and more reliable concurrent code. It detects potential data races and other concurrency-related issues at compile time, preventing unexpected behavior and crashes when your app runs.
- **UserDefaults, AppStorage**
  - UserDefaults and AppStorage are mechanisms in Swift and SwiftUI for storing small amounts of data persistently on a user's device. UserDefaults is a traditional way to store simple data types like strings, numbers, and booleans, using key-value pairs.
- **CloudKit**
  - CloudKit is Apple's cloud storage solution that allows developers to save and retrieve app data in iCloud. It provides a way to store structured data, like records with fields, and binary data, like images or videos, in the cloud.
- **Databases**
  - Databases provide a structured way to store and manage data within your Swift applications. They allow you to persist information beyond the app's runtime, meaning data is saved even when the app is closed.
- **FileManager**
  - FileManager provides a way to interact with the file system. It allows you to perform operations like creating, reading, writing, deleting, and moving files and directories.
- **Firabase**
  - Firebase is a Backend-as-a-Service (BaaS) platform that provides developers with a suite of tools and services to build, manage, and grow their apps. It handles many backend tasks, such as data storage, user authentication, hosting, and analytics, allowing developers to focus on building the front-end user experience.
- **Realm**
  - Realm is a mobile database solution that offers a convenient and efficient way to store and manage data directly on a user's device. It's designed to be faster and easier to use than traditional databases like SQLite, providing a developer-friendly API for reading, writing, and querying data.
- **GRDB**
  - GRDB is a Swift library that provides a convenient and reliable way to interact with SQLite databases. It allows you to perform database operations like creating tables, inserting, querying, updating, and deleting data using Swift code.
- **SwiftUI with Async/Await**
  - Async/Await is a programming paradigm that simplifies asynchronous code, making it easier to read and manage. In SwiftUI, it allows you to perform long-running tasks, like network requests or data processing, without blocking the main thread, ensuring your app remains responsive.

### 3.3 Swift Package Manager
- **Using Packages**
  - Swift Package Manager lets you add external libraries and tools to your Swift projects. Using packages involves declaring dependencies in your Package.swift file, which tells Swift Package Manager where to find the code you want to use.
- **Plugins**
  - Swift Package Manager plugins allow you to extend the build process of your Swift packages with custom tools and scripts. These plugins can automate tasks like code generation, linting, formatting, and other pre-build or post-build operations, streamlining your development workflow and ensuring consistency across your projects.
- **Creating Packages**
  - The Swift Package Manager is a tool for managing the distribution of Swift code. Creating a Swift package allows you to bundle your code into reusable modules, making it easy to share and use in other projects.

### 3.4 App Architecture
- **MVVM**
  - MVVM (Model-View-ViewModel) is a software architectural pattern that facilitates the separation of concerns in application development. It divides an application into three interconnected parts: the Model (data and business logic), the View (the user interface), and the ViewModel (an intermediary that prepares data for the View and handles user input).
- **Clean Architecture**
  - Clean Architecture is a software design philosophy that emphasizes separation of concerns, making applications more maintainable, testable, and scalable. It achieves this by dividing the application into distinct layers, each with its own specific responsibility and dependencies.
- **Dependency Injection**
  - Dependency Injection is a design pattern where a component receives its dependencies from external sources rather than creating them itself. This promotes loose coupling, making code more modular, testable, and reusable.

### 3.5 Swift Package Index
- **swift-log**
  - swift-log is a logging API for Swift that provides a standardized way to record messages from your code. It allows you to capture information about your application's behavior, errors, and performance, making it easier to diagnose issues and understand how your code is running.

### 3.6 Testing
- **XCTest**
  - XCTest is Apple's framework for writing unit, integration, and UI tests for your Swift and Objective-C code. It allows developers to verify the correctness of their code by writing assertions that check for expected outcomes.
- **Swift Testing**
  - The Swift Testing library allows you to leverage the powerful and expressive capabilities of the Swift programming language to develop tests with more confidence and less code. The library integrates seamlessly with Swift Package Manager testing workflow, supports flexible test organization, customizable metadata, and scalable test execution.

### 3.7 Server Frameworks
- **Vapor**
  - Vapor is an open-source web framework written in Swift that allows developers to build robust and scalable server-side applications, APIs, and websites. It provides a clean and expressive syntax, making it easier to handle tasks like routing, database interaction, and templating, all while leveraging the performance and safety features of the Swift language.
- **Hummingbird**
  - Hummingbird is an open-source server-side framework written in Swift, designed to help developers build high-performance web applications and APIs. It leverages Swift's type safety and concurrency features to provide a robust and efficient platform for handling HTTP requests, routing, and middleware.
- **MongoKitten**
  - MongoKitten is a native Swift driver for MongoDB, a popular NoSQL database. It allows Swift applications, including those built with SwiftUI, to interact with MongoDB databases for storing and retrieving data.

### 3.8 Logging & Debugging
- **XCode debugging**
  - The Xcode debugger is a powerful tool built into the Xcode IDE that allows developers to step through their code line by line, inspect variables, and understand the flow of execution. It helps identify and fix bugs by providing insights into the application's state at various points in time.
- **SwiftUI inspector**
  - The SwiftUI Inspector is a built-in tool within Xcode that allows developers to examine and modify the properties of SwiftUI views in real-time while an app is running, either in the simulator or on a physical device. It provides a visual interface to inspect the view hierarchy, adjust attributes like colors, fonts, and layout constraints, and immediately see the changes reflected in the app's UI, facilitating rapid prototyping and debugging.
- **CocoaLumberjack**
  - CocoaLumberjack is a logging framework for Objective-C and Swift that provides a flexible and powerful way to record and manage log messages in your applications. It allows you to log to multiple destinations simultaneously, such as the console, files, or even remote servers, and offers different log levels to filter messages based on their severity.

### 3.9 Networking Libraries
- **Alamofire**
  - Alamofire is a Swift-based HTTP networking library that simplifies the process of making network requests in your iOS, macOS, tvOS, and watchOS applications. It provides an elegant interface built on top of Apple's URLSession to handle common networking tasks like making GET, POST, PUT, and DELETE requests, handling response data, and managing request parameters.
- **Moya**
  - Moya is a Swift networking library that simplifies the process of making API requests. It acts as an abstraction layer on top of URLSession, providing a cleaner and more organized way to define and manage your API endpoints.
- **swift-nio**
  - SwiftNIO is a low-level, cross-platform asynchronous event-driven network application framework. It enables the development of high-performance protocol servers and clients in Swift.

### 3.10 IDEs
- **DocC**
  - DocC is Apple's documentation compiler that allows developers to create rich, interactive documentation directly from their Swift or Objective-C code. It transforms specially formatted comments within your code into a structured and navigable documentation set, complete with articles, tutorials, and API reference.
- **Swift Charts**
  - Swift Charts is a framework within Swift that allows you to create a variety of visually appealing and informative charts directly in your applications. It provides a declarative syntax for defining chart types, data sources, and visual customizations, making it easier to represent data clearly and understandably.
- **Swift Playgrounds**
  - Swift Playgrounds is an Apple application designed to teach coding in a fun and interactive way. It uses a game-like environment where users learn Swift programming concepts by solving puzzles and completing challenges.
- **Xcode**
  - Xcode is Apple's integrated development environment (IDE) used for developing software for macOS, iOS, watchOS, and tvOS. It provides a comprehensive suite of tools for writing, debugging, and testing code, as well as designing user interfaces.
- **VSCode**
  - VSCode (Visual Studio Code) is a free and popular source code editor developed by Microsoft. It's known for its lightweight design, extensive customization options through extensions, and robust support for various programming languages, including Swift.
- **Emacs**
  - Emacs is a highly customizable and extensible text editor, known for its powerful editing capabilities and extensive ecosystem of packages. It's more than just a text editor; it's often described as an operating system within an operating system, allowing users to tailor the environment to their specific needs through Lisp programming.
- **Neovim**
  - Neovim is a free and open-source, heavily refactored and extended version of the Vim text editor. It aims to improve Vim's extensibility, user experience, and maintainability.

### 3.11 Static Linux SDK
- **Static Linux SDK**
  - A Static Linux SDK allows you to compile Swift code into standalone executables that can run on Linux systems without requiring a full Swift runtime environment to be installed. This is achieved by bundling all necessary Swift libraries and dependencies directly into the executable file, making it self-contained and portable.

### 3.12 SDKs for Wasm
- **SDKs for Wasm**
  - WebAssembly (Wasm) is a binary instruction format designed as a portable compilation target for programming languages, enabling high-performance applications on the web and other environments. SDKs for Wasm allow developers to compile Swift and Swift UI code into Wasm, making it possible to run Swift applications in web browsers or other Wasm-compatible environments, effectively extending the reach of Swift beyond Apple's platforms.

### 3.13 Swift for Server Apps
- **Swift for Server Apps**
  - Swift isn't just for iOS and macOS apps; it can also be used to build server-side applications. This allows developers to use their existing Swift knowledge to create backends, APIs, and other server-side components, potentially leading to more efficient development workflows and code sharing between client and server.

---

## 4. Optional / Specialized Topics

- Arithmetic
- Logical
- Comparison
- Nil-Coalescing
- Optional Chaining
- Subscripts
- Extensions
- Text
- Computed
- Wrappers
- clipShape
- background
- Implicit animations
- Transitions
- HStack
- VStack
- ZStack
- Grid
- GeometryReader
- NavigationPath
- TabView
- NavigationLink
- ViewBuilder
- Explicit animations
- Animatable Protocol

---

## 5. References

- [Swift & SwiftUI Roadmap](https://roadmap.sh/swift-ui)

---

## 6. Related Roles / Topics

### Related Roles
- iOS Developer

### Related Skills
- React Native
- Flutter