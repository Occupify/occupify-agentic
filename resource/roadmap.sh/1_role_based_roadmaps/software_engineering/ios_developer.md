# iOS Developer

## Metadata
- Type: Role
- Domain: Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ios
- Related Roles:
  - Frontend Developer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Objective-C
- **Objective-C Basics**
  - Objective-C basics cover the core syntax and concepts needed to read and write Objective-C code. This includes pointers, message syntax, classes, categories, protocols, and property declarations.
- **Interoperability with Swift**
  - Swift and Objective-C can coexist in the same Xcode project through a bridging header mechanism. Swift code can call Objective-C APIs, and Objective-C code can use Swift classes marked with the @objc attribute.

### 1.2 Pick a Language
- **Pick a Language**
  - iOS development primarily uses Swift and Objective-C. Swift is Apple's modern recommended language for new projects, while Objective-C is still present in many legacy codebases and system frameworks.

### 1.3 Swift (Recommended)
- **History and Why Swift?**
  - Swift was introduced by Apple in 2014 to address the limitations of Objective-C in terms of safety, performance, and developer experience. It was designed to be faster, more expressive, and safer by eliminating entire classes of bugs through optionals and strong typing.
- **Benefits over Objective-C**
  - Swift offers several advantages over Objective-C including type safety with optionals, modern syntax that reduces boilerplate, cleaner closure support, and better performance in many scenarios. Swift code is generally easier to read, write, and maintain.
- **Swift Basics**
  - Swift basics cover the fundamental syntax and language features needed to write Swift programs. This includes variables, constants, data types, control flow, functions, closures, classes, structs, enums, and optionals.

### 1.4 iOS Architecture
- **Core OS**
  - Core OS is the bottom layer of the iOS architecture, sitting directly above the hardware. It provides the Darwin kernel, security frameworks, and low-level system interfaces.
- **Core Services**
  - Core Services is the second layer of the iOS architecture and provides fundamental system capabilities that apps depend on. It includes frameworks for networking, file access, data management, location, and iCloud.
- **Media**
  - The iOS Media Layer is a collection of frameworks and technologies that enable developers to incorporate rich multimedia experiences into their apps. It includes tools for handling audio, video, and graphics.
- **Core Graphics**
  - Core Graphics, also known as Quartz, is a powerful 2D graphics rendering framework in iOS. It provides essential functions for drawing shapes, images, and text, handling low-level graphic operations with precision and efficiency.
- **Core Animation**
  - Core Animation is a powerful framework in iOS that allows developers to create rich and interactive animations. It works by compositing layers, each representing a view, and uses hardware acceleration to ensure smooth animations.
- **Cocoa Touch**
  - Cocoa Touch is the topmost layer of the iOS architecture and provides the frameworks developers interact with most directly, including UIKit, SwiftUI, MapKit, and GameKit. It handles touch input, notifications, multitasking, and high-level app structure.

### 1.5 Core Programming Concepts
- **AVFoundation**
  - AVFoundation is a comprehensive framework for working with time-based audiovisual media on iOS-based platforms. It enables developers to play, create, and edit QuickTime movies and MPEG-4 files, as well as handle HLS streams.
- **Core Image**
  - Core Image is a powerful framework in iOS for image processing and analysis. It provides a wide array of built-in filters for tasks such as enhancing photos, applying artistic effects, and performing face detection.
- **Core Audio**
  - Core Audio is a low-level framework in iOS designed for handling audio. It provides developers with advanced capabilities for recording, processing, playing back, and streaming audio.
- **Metal**
  - Metal is a high-performance graphics and compute framework for iOS, macOS, and tvOS, designed by Apple. It enables developers to harness the full power of the GPU for advanced 3D graphics, complex visual effects, and data-parallel computation.
- **OOP**
  - Object-Oriented Programming (OOP) is a style where code is organized around "objects," which are instances of classes combining data and methods. It emphasizes encapsulation, abstraction, inheritance, and polymorphism, enabling modular, reusable, and maintainable code.
- **Functional Programming**
  - Functional programming is a style of programming where code is written using pure functions, avoiding changing state and mutable data. It emphasizes the use of mathematical functions to process data, which leads to more predictable and bug-resistant code.
- **Memory Management**
  - iOS uses Automatic Reference Counting (ARC) to manage memory. ARC tracks how many strong references point to each object and deallocates it when the count drops to zero.
- **ViewController Lifecycle**
  - The ViewController lifecycle in iOS refers to the sequence of methods called as a view controller transitions between states. It begins with initialization, followed by loading the view, appearing on screen, disappearing, and potentially being deallocated.
- **Error Handling**
  - Swift provides a structured error handling model using the throw, try, and catch keywords. Functions that can fail declare throws in their signature, and callers handle errors using do-catch blocks.
- **Concurrency (GCD, async/await)**
  - Concurrency in iOS allows multiple tasks to run in parallel to keep the UI responsive. Grand Central Dispatch (GCD) is the traditional approach, using dispatch queues to schedule work on background threads.

### 1.6 Version Control
- **Git**
  - Git is a distributed version control system (VCS) used to track changes in source code during software development. It allows multiple developers to collaborate on a project by managing different versions of the code, enabling them to work on separate branches, merge changes, and keep a complete history of modifications.
- **GitHub**
  - GitHub is a web-based platform that uses Git for version control and collaboration. It provides a centralized repository for hosting and managing Git repositories, allowing developers to share their code, collaborate on projects, and track issues.
- **Installing**
  - Installing Xcode is the first step in setting up an iOS development environment. Xcode is available for free from the Mac App Store and requires macOS and sufficient disk space.
- **Preferences**
  - Xcode preferences allow you to customize your development environment to suit your workflow. They offer various settings across multiple tabs, including General, Accounts, Behaviors, Text Editing, Key Bindings, and more.
- **Components**
  - UIKit components are the built-in UI controls the framework provides, including UIButton, UILabel, UITextField, UISwitch, UISlider, UIImageView, and UITableView. Each component is a UIView subclass and can be customized through properties, subclassing, or delegation.
- **Views**
  - UIKit views are the core visual elements in iOS interfaces, serving as the canvas for all user interface components. At its most basic, a view is an instance of UIView, representing a rectangular area on the screen.

### 1.7 Xcode
- **New Project**
  - To create an Xcode project for your app, select a platform template such as iOS, macOS, watchOS, or tvOS, and choose the type of app you want to develop, like a single view, game, or document-based app. Xcode templates provide essential configuration and files, allowing you to quickly start developing your app.
- **Interface overview**
  - The Xcode interface is organized into a navigator panel on the left, an editor area in the center, an inspector panel on the right, and a debug area at the bottom. The toolbar at the top provides controls for running, stopping, and switching build schemes.
- **Toolbar**
  - The Xcode toolbar provides quick access to common actions, including running and stopping the app, selecting a target device or simulator, and showing or hiding the navigator and inspector panels. It also displays build activity messages and scheme selection controls.
- **Navigators**
  - The navigator panel contains multiple navigators for different purposes. The Project Navigator shows the file hierarchy, the Issue Navigator displays errors and warnings, the Test Navigator lists test suites, and the Debug Navigator shows runtime resource usage.
- **Editors**
  - Xcode provides different editor modes depending on the file being viewed. The standard editor shows a single file, the assistant editor displays two files side by side, and the version editor shows Git history for the current file.

### 1.8 UIKit
- **View Controllers**
  - A UIViewController manages a single screen of content in a UIKit app. It owns a root view, handles the lifecycle events for that view, and coordinates between the model layer and the UI.
- **User Interactions**
  - UIKit User Interactions encompass the various ways users can engage with an iOS app's interface. This includes touch events (taps, swipes, pinches), gesture recognizers for complex interactions, and control events for UI elements like buttons and sliders.
- **Basic Interfaces**
  - Building a basic interface in UIKit involves adding views to a view controller's root view, setting up Auto Layout constraints, and wiring controls to code through IBOutlets and IBActions. Simple interfaces typically combine labels, buttons, text fields, and image views arranged into a readable, functional layout.
- **Storyboards**
  - Storyboards are XML-based files that define multiple view controllers and the transitions between them on a single visual canvas. Developers drag view controllers onto the canvas, design their views, and connect screens with segues.
- **Xibs**
  - UIKit Xibs (XML Interface Builder files) are resource files used to design individual view hierarchies or custom views in iOS development. Unlike Storyboards, which can represent an entire app's interface, Xibs typically focus on smaller, reusable UI components or single view controllers.
- **Navigation**
  - Navigation helps users easily find their way around an app and locate the information they need, minimizing confusion. Utilizing familiar navigation patterns can simplify complex interactions while preserving the app's unique character.
- **View Transitions**
  - View transitions control how the app animates when moving between screens. UIKit provides built-in transition styles like push and modal presentation, and custom transitions are created using the UIViewControllerAnimatedTransitioning protocol.
- **Declarative Syntax**
  - SwiftUI's declarative syntax allows developers to describe the desired UI state rather than the step-by-step process to achieve it. This approach uses Swift code to define what views should appear and how they should behave, with SwiftUI handling the underlying implementation details.
- **Components**
  - Components are built by composing primitive views like Text, Image, and Button, along with container views such as VStack and HStack. They can accept parameters for customization and use @State and @Binding for internal state management and data flow.
- **State Management**
  - State management in SwiftUI determines where data lives and how it flows through the view hierarchy. @State handles local view state, @StateObject owns an observable object, @ObservedObject observes an externally owned object, and @EnvironmentObject injects shared data across the hierarchy.

### 1.9 SwiftUI
- **Project Files**
  - The Project Navigator organizes all files in an Xcode project, including Swift source files, assets, configuration files, and frameworks. Files are listed hierarchically and can be added, deleted, or reorganized within the navigator.
- **Groups**
  - Groups in Xcode are virtual folders used to organize files within the Project Navigator without necessarily reflecting the file system directory structure. They keep large projects organized by feature or layer.
- **Breakpoints**
  - Breakpoints pause app execution at a specific line of code so the developer can inspect the current state of variables and the call stack. Xcode supports line breakpoints, symbolic breakpoints that trigger on a function name, and exception breakpoints that catch crashes automatically.
- **Debug Navigator**
  - The Debug Navigator appears during a debugging session and shows real-time data about the running app, including CPU, memory, disk, and network usage, as well as active threads and their states. It helps identify performance issues and excessive resource consumption without switching to a separate profiling tool.
- **Stepping**
  - Stepping controls in the Xcode debugger allow developers to move through code one statement at a time during a paused breakpoint session. Step Over executes the current line without descending into called functions, Step Into enters a called function, and Step Out completes the current function and returns to the caller.
- **Interface Builder**
  - Interface Builder is the visual design tool embedded in Xcode for creating UI layouts without writing code. Developers drag UI elements onto a canvas, configure properties through the inspector, and set up constraints.
- **IBOutlets**
  - An outlet is a property of an object that references another object. The reference is archived through Interface Builder.
- **Data binding**
  - SwiftUI data binding is a mechanism that creates a two-way connection between a piece of data and a UI element. It uses the @Binding property wrapper to allow child views to share and modify data owned by parent views.
- **Building Interfaces**
  - Building interfaces in SwiftUI involves composing views using container types. VStack arranges views vertically, HStack arranges them horizontally, and ZStack layers them.

### 1.10 UI Design
- **HIG**
  - Human Interface Guidelines (HIG) by Apple are a set of recommendations and best practices for creating user interfaces on Apple devices. These guidelines help developers and designers create applications and interfaces that provide a high-quality experience and consistency with the Apple ecosystem.

---

## 2. Intermediate

### 2.1 UIKit
- **Views, View Controllers**
  - Views and view controllers are the two primary building blocks of UIKit's architecture. Views are responsible for displaying content and receiving touch input, while view controllers manage a screen's lifecycle and coordinate between views and data.
- **Navigation Controllers, Segues**
  - UINavigationController manages a stack of view controllers with a navigation bar at the top. Segues are the transitions between view controllers defined in a Storyboard, triggered by user interaction or called programmatically.
- **Navigation Stacks**
  - The navigation stack in UIKit is managed by UINavigationController using a push-pop model. View controllers are pushed onto the stack when navigating forward and popped when the user taps the Back button or calls popViewController.

### 2.2 SwiftUI
- **Views and Modifiers**
  - SwiftUI views are lightweight structs that describe a piece of UI. Modifiers are methods called on views that return a new, modified version, allowing chaining.
- **Navigation**
  - Navigation in SwiftUI is managed with NavigationStack (iOS 16+) or NavigationView for older deployment targets. NavigationLink connects the current view to a destination, and the navigation stack maintains a history that the user can traverse with the Back button.
- **View Transitions**
  - View transitions in SwiftUI animate changes in the view hierarchy when views appear or disappear. The transition modifier specifies how a view enters and exits the screen using effects like slide, opacity, scale, and move.
- **Pushing Presenting**
  - Pushing a view controller adds it to the navigation stack with a standard slide animation from the right. Presenting a view controller modally overlays it on the current screen, often as a sheet or full-screen cover.
- **Modals and Navigation**
  - Modal presentation in UIKit shows a view controller over the current content, typically for tasks that need the user's attention before they can continue. Modals are dismissed programmatically or by the user via drag or a dismiss button.
- **Navigation Stacks**
  - Navigation stacks in SwiftUI are managed by NavigationStack (iOS 16+), which maintains a path representing the current navigation state. Views are pushed onto the stack by navigating to a value, and the stack handles the back button automatically.
- **Navigation View**
  - NavigationView is the SwiftUI component for hierarchical navigation, used before NavigationStack was introduced in iOS 16. It wraps a view and provides a navigation bar and back navigation behavior.
- **NavigationLink**
  - NavigationLink is a SwiftUI component used to create navigation hierarchies within an app. It enables developers to define navigation paths between views, typically within a NavigationView.

### 2.3 Core Animation
- **IBActions**
  - IBActions connect UI controls in Interface Builder to methods in code that run when a user interacts with a control. Declaring a method with @IBAction allows it to be wired to a button, gesture recognizer, or other control in a Storyboard or XIB.
- **Auto layout**
  - Auto Layout is a constraint-based layout system that defines the size and position of views relative to each other and to the container. It automatically adapts layouts for different screen sizes, orientations, and locales.
- **Basics / Creating Animations**
  - Creating animations with Core Animation involves working with CALayer and CAAnimation subclasses. CABasicAnimation animates a single property from one value to another, while CAKeyframeAnimation defines multiple values along an animation path.
- **Lottie**
  - Lottie is a cross-platform library for iOS, macOS, tvOS, visionOS, Android, and Web that natively renders vector-based animations and art in realtime with minimal code. Lottie loads and renders animations and vectors exported in the bodymovin JSON format.

### 2.4 Architectural Patterns
- **MVC**
  - MVC (Model-View-Controller) is the architectural pattern used by UIKit and historically recommended by Apple for iOS apps. The Model holds data and business logic, the View displays content, and the Controller mediates between them.
- **MVP**
  - MVP (Model-View-Presenter) improves on MVC by separating UIKit view controllers into a passive View and a Presenter that contains all UI logic. The View delegates user interactions to the Presenter, which processes them and updates the View through a protocol-based interface.
- **MVVM**
  - MVVM (Model-View-ViewModel) separates the UI layer from business logic using a ViewModel that exposes observable state. The View binds to the ViewModel and updates automatically when state changes, using Combine, RxSwift, or Swift's observation framework.
- **MVVM-C**
  - MVVM-C extends the MVVM pattern by adding a Coordinator component that manages navigation between screens. Coordinators handle routing logic that would otherwise live in view controllers or ViewModels, making navigation testable and reusable.
- **VIPER**
  - VIPER is an architectural pattern that divides app code into five distinct components: View, Interactor, Presenter, Entity, and Router. Each component has a single, clearly defined responsibility, making the codebase highly modular and testable.
- **TCA**
  - The Composable Architecture (TCA) is an opinionated architecture library for Swift developed by Point-Free. It organizes app logic around unidirectional data flow with state, actions, reducers, and effects.

### 2.5 Reactive Programming
- **Presenting / Dismissing views**
  - Presenting views in SwiftUI is done using modifiers like sheet, fullScreenCover, and popover that show views modally over the current screen. Dismissal is handled using the dismiss environment action or by toggling the Boolean binding that controls the presentation.
- **Combine**
  - Combine is Apple's built-in framework for reactive programming, using the same publisher-subscriber pattern as most modern approaches to this issue. Combine introduces the concept of a Cancellable (i.e.
- **Publishers / Subscribers**
  - The Combine framework in iOS uses Publishers and Subscribers as core components for reactive programming. Publishers are types that can emit a sequence of values over time, representing sources of asynchronous events or data.
- **Operators & Pipelines**
  - Combine operators transform, filter, and combine publishers into processing pipelines. Common operators include map, filter, flatMap, combineLatest, merge, and debounce.
- **Combine and MVVM**
  - Combine integrates naturally with the MVVM pattern. ViewModels expose @Published properties that emit state changes, and Views subscribe to those values to update the UI automatically.
- **RxSwift**
  - RxSwift is the Swift implementation of the ReactiveX library, providing a comprehensive API for reactive programming. It introduces Observable sequences that emit items over time and a large set of operators for combining and transforming them.
- **Observables & observers**
  - An Observable in RxSwift is a sequence that emits zero or more items over time before completing or erroring. Observers subscribe to Observables and receive emitted items, error notifications, or completion events.

### 2.6 Delegate Pattern
- **Implementing Delegates**
  - Implementing a delegate involves defining a protocol with required methods, adding a weak delegate property to the delegating class, and calling delegate methods at the appropriate times. The conforming class implements the protocol methods to respond to events.
- **Understanding and using Closures**
  - Understanding closures involves knowing their syntax, how they capture surrounding values, and how to use them as function parameters and return values. Swift offers shorthand argument names and trailing closure syntax to keep closure usage concise.

### 2.7 Callbacks
- **Closures**
  - Closures are self-contained blocks of code that can capture and store references to values from the surrounding context. In Swift, closures are first-class types that can be passed as arguments, stored in variables, and returned from functions.
- **Capturing Values & Memory Mgmt.**
  - Closures capture references to the variables and constants from their surrounding context. When a closure captures a class instance, it holds a strong reference by default, which can create retain cycles if the instance also holds the closure.

### 2.8 Data Persistence
- **Subjects**
  - Subjects in RxSwift act as both Observables and Observers, making them useful for bridging non-reactive code into reactive streams. PublishSubject emits only new items to subscribers; BehaviorSubject replays the last value to new subscribers; and ReplaySubject replays a configurable number of past values.
- **RxSwift with MVVM**
  - RxSwift integrates seamlessly with the MVVM (Model-View-ViewModel) architecture in iOS development. In this combination, ViewModels expose Observable properties that Views can bind to, creating a reactive data flow.
- **Operators**
  - RxSwift operators are functions that process, transform, or combine observable sequences. They allow developers to manipulate data streams in powerful ways.
- **Schedulers**
  - Schedulers in RxSwift control on which thread or queue Observable work executes. MainScheduler runs work on the main thread for UI updates, while ConcurrentDispatchQueueScheduler and SerialDispatchQueueScheduler run work on background queues.
- **Core Data**
  - Core Data is Apple's framework for persisting complex object graphs and relational data on iOS. It provides an abstraction layer over SQLite with tools for defining data models, fetching, filtering, and observing changes.
- **User Defaults**
  - User Defaults is a simple key-value store for persisting lightweight user preferences and settings across app launches. It stores basic types like strings, numbers, booleans, and dates in a plist file.
- **Keychain**
  - The Keychain is iOS's secure, encrypted storage for sensitive data like passwords, tokens, and cryptographic keys. Data stored in the Keychain persists across app reinstalls and can be shared between apps from the same developer through Keychain Access Groups.
- **File System**
  - The iOS file system sandboxes each app's data into private directories. The Documents directory is for user-facing files that should be backed up, the Caches directory is for regenerable data, and the tmp directory is for temporary files that do not need to persist.
- **SQLite**
  - SQLite is a lightweight, serverless relational database engine embedded in iOS. Apps can use SQLite directly through its C API or through higher-level Swift wrappers like GRDB or SQLite.swift.

### 2.9 Async / Await
- **Callback Hell**
  - Callback hell refers to deeply nested, hard-to-read code that results from chaining multiple asynchronous operations through callbacks. This pattern, sometimes called the pyramid of doom, was common in iOS development when completion handlers were the primary way to handle async work.
- **Concurrency**
  - Swift's structured concurrency builds on async/await with additional primitives for parallel execution. async let runs multiple async operations concurrently, TaskGroup manages a dynamic set of concurrent child tasks, and actors protect shared mutable state from data races.

### 2.10 JSON / XML
- **Parsing**
  - Parsing JSON in Swift is done using Codable and JSONDecoder, which automatically decode JSON data into Swift structs and classes. XMLParser provides a SAX-style parser for processing XML documents event by event.
- **Serializing**
  - Serializing converts Swift data structures into JSON or XML format for storage or network transmission. JSONEncoder turns Codable types into Data.

### 2.11 Networking
- **HTTP / HTTPs**
  - HTTP and HTTPS are the application-layer protocols used for communication between iOS apps and web servers. iOS enforces App Transport Security (ATS) by default, requiring HTTPS for most network requests.
- **REST**
  - REST (Representational State Transfer) is an architectural style for networked APIs that uses standard HTTP methods like GET, POST, PUT, PATCH, and DELETE. iOS apps consume REST APIs by making URLSession or Alamofire requests and decoding JSON responses using Codable.
- **GraphQL**
  - GraphQL is a query language for APIs that allows clients to request exactly the data they need in a single request. iOS apps interact with GraphQL APIs using libraries like Apollo iOS.

### 2.12 Concurrency and Multithreading
- **GCD**
  - Grand Central Dispatch (GCD) is a C-based system for dispatching work to queues managed by the operating system. The main queue runs tasks on the main thread for UI updates, while serial and concurrent dispatch queues run background work.
- **Operation Queues**
  - Operation Queues manage collections of NSOperation objects and execute them concurrently or serially. Operations support dependencies on each other, cancellation, and priority settings.
- **Carthage**
  - Carthage is a decentralized dependency manager for iOS and macOS that builds frameworks from source and links them manually into the project. Unlike CocoaPods, Carthage does not modify the Xcode project file, giving developers full control over integration.

### 2.13 Dependency Manager
- **CocoaPods**
  - CocoaPods is a dependency manager for Swift and Objective-C Cocoa projects. It has over 100 thousand libraries and is used in over 3 million apps.
- **Swift Package Manager**
  - The Swift Package Manager (SwiftPM) is a tool for managing the distribution of Swift code. It’s integrated with the Swift build system to automate the process of downloading, compiling, and linking dependencies.
- **SwiftLint**
  - SwiftLint is an open-source tool developed by Realm, that facilitates maintaining standardized code development by enabling the definition and enforcement of project-specific conventions and guidelines. It ensures developers adhere to these standards, thereby promoting organized code practices.

---

## 3. Advanced

### 3.1 Frameworks & Library
- **XCFramework**
  - An XCFramework is a distributable binary format that bundles frameworks for multiple platforms and architectures in a single package. It supports iOS devices, iOS Simulator, macOS, and other Apple platforms simultaneously.
- **Static Library**
  - A static library is a compiled archive of object code that is copied directly into the app binary at link time. Static libraries increase binary size but have no runtime loading overhead.

### 3.2 Accessibility
- **URLSession**
  - URLSession is Apple's built-in networking API for making HTTP and HTTPS requests. It supports data tasks for simple requests, download and upload tasks for large transfers, and background sessions that continue after the app is suspended.
- **Alamofire**
  - Alamofire is a Swift networking library built on top of URLSession that simplifies common networking tasks. It provides a clean, chainable API for making requests, handling authentication, and serializing responses.
- **Accessibility Inspector**
  - Accessibility Inspector is a tool in Xcode that audits UI elements for accessibility issues. It displays the accessibility properties of each element, runs automated audits to catch missing labels and low-contrast issues, and simulates VoiceOver navigation.
- **Voice Over**
  - VoiceOver is iOS's built-in screen reader that allows users who are blind or have low vision to navigate and interact with apps using gestures and spoken audio feedback. Apps support VoiceOver by providing accessibility labels, traits, and hints on UI elements.
- **Dynamic Type**
  - The Dynamic Type feature allows users to choose the size of textual content displayed on the screen. It helps users who need larger text for better readability.
- **Frameworks**
  - Frameworks in iOS development are modular, reusable packages of code and resources that provide specific functionality to applications. They offer a hierarchical structure containing compiled code, header files, resources like images and localization files, and often documentation.
- **ARKit**
  - ARKit is Apple's augmented reality framework for iOS. It uses the device's camera and motion sensors to track the physical world and overlay digital content on top of it.
- **HealthKit**
  - HealthKit is a powerful framework that allows developers to create health and fitness applications that can interact seamlessly with the iOS Health app. HealthKit provides a central repository for health and fitness data on iPhone and Apple Watch.
- **GameKit**
  - GameKit is Apple's framework for adding social gaming features to iOS apps. It provides APIs for leaderboards, achievements, multiplayer matchmaking, and real-time game sessions through Game Center.
- **Unit & UI Testing**
  - iOS apps are tested at two levels: unit tests verify individual functions and classes in isolation, and UI tests verify app behavior from the user's perspective. XCTest is the framework for both.

### 3.3 Code Quality Tools
- **Tailor**
  - Tailor is a static analysis tool for Swift that checks code style and detects common issues. It is configurable and integrates with Xcode and CI pipelines.
- **SwiftFormat**
  - SwiftFormat is a command-line tool that automatically reformats Swift source code to follow consistent style rules. Unlike SwiftLint, which reports violations, SwiftFormat directly edits source files.

### 3.4 Debugging Techniques
- **Dynamic Library**
  - A dynamic library is a compiled binary loaded into memory at runtime rather than being embedded in the app binary at link time. On iOS, third-party dynamic libraries must be bundled inside the app's framework folder.
- **Xcode Debugger**
  - The Xcode debugger allows developers to pause execution at breakpoints, inspect variable values, evaluate expressions using LLDB commands in the console, and step through code line by line. The debug area displays the current thread, call stack, and local variable state during a paused session.
- **XCTest**
  - XCTest is Apple's framework for writing unit tests in Swift and Objective-C. Tests are organized into subclasses of XCTestCase, and individual test methods begin with "test".

### 3.5 CI / CD
- **Profiling Instruments**
  - Instruments is a performance analysis tool bundled with Xcode that provides templates for profiling CPU usage, memory allocations, energy impact, network activity, and more. The Time Profiler identifies which functions consume the most CPU time, while the Allocations instrument tracks memory usage and helps detect leaks and retain cycles.
- **XCUITest**
  - XCUITest is the UI testing component of XCTest that automates user interactions with a running iOS app. Tests launch the app, query elements by accessibility identifier or type, perform actions like tap, swipe, and type, and assert on UI state.
- **Jenkins**
  - Jenkins is an open-source automation server used for iOS CI/CD, particularly in enterprise environments. It runs on macOS machines and can execute Xcode builds, run tests, and invoke Fastlane workflows.
- **CircleCI**
  - CircleCI is a cloud-based CI/CD platform that supports iOS development through macOS build environments with Xcode installed. It runs builds, executes test suites, and triggers Fastlane lanes for automated distribution.
- **GitHub Actions**
  - GitHub Actions provides CI/CD automation directly within GitHub repositories. For iOS development, it uses macOS runners with Xcode installed to build apps, run tests, and trigger Fastlane workflows.
- **GitLab**
  - GitLab CI/CD is GitLab's built-in automation platform that runs pipelines on code changes. For iOS development, it uses GitLab Runners configured on macOS to execute Xcode builds and test suites.
- **Azure DevOps**
  - Azure DevOps is Microsoft's suite of developer tools that includes a CI/CD pipeline service supporting iOS development. It uses macOS-hosted agents to run Xcode builds and Fastlane workflows, and integrates with Azure Repos, GitHub, and other source control systems.

### 3.6 App Store Distribution
- **MapKit**
  - MapKit is Apple's framework for embedding maps and location-based features into iOS apps. It provides interactive map views, annotation pins, overlays, turn-by-turn directions, and local place search.
- **Core ML**
  - Use Core ML to integrate machine learning models into your app. Core ML provides a unified representation for all models.
- **Test Plan & Coverage**
  - Test plans in Xcode define how tests are executed, including which test targets to include, environment variables, and configurations for multiple runs with different settings. Code coverage reports show which lines of code are exercised by tests, helping identify gaps.

### 3.7 TestFlight
- **TestFlight**
  - TestFlight is Apple's platform for distributing beta versions of iOS apps to testers before public release. Internal testers with access to the developer's App Store Connect account can be added directly, while external testers receive email invitations.

### 3.8 FastLane
- **FastLane**
  - Fastlane is an open-source automation tool for iOS development that handles repetitive tasks like building, testing, code signing, and uploading to App Store Connect. Workflows are defined in Ruby-based scripts called Fastfiles using reusable actions called lanes.

### 3.9 App Store Optimization (ASO)
- **App Store Optimization (ASO)**
  - App Store Optimization (ASO) is the process of improving an iOS app's visibility and conversion rate in the App Store. It involves optimizing the app name, subtitle, keywords, screenshots, and description to rank higher in relevant searches.

### 3.10 Keeping Updated with WWDC
- **Latest Swift Version**
  - Apple releases new Swift versions annually alongside Xcode and iOS updates. New Swift versions introduce language features, performance improvements, and standard library additions.
- **Latest iOS SDK**
  - The iOS SDK is updated each year with new APIs, deprecated frameworks, and changes to system behavior. New SDK features are announced at WWDC and documented in the release notes.
- **New Feature Announcements**
  - Apple announces new platform features at WWDC each year that affect how iOS apps are built and what they can offer users. Recent examples include StoreKit 2, Live Activities, WidgetKit updates, and Vision framework additions.

---

## 4. Optional / Specialized Topics

- Core Animation
- Cocoa Touch
- OOP
- Functional Programming
- Memory Management
- ViewController Lifecycle
- Error Handling
- Concurrency (GCD, async/await)
- Components
- Views
- Editors
- Xibs
- Navigation
- View Transitions
- Declarative Syntax
- State Management
- Stepping
- Interface Builder
- IBOutlets
- Data binding
- Building Interfaces
- Modals and Navigation
- Navigation Stacks
- Navigation View
- NavigationLink

---

## 5. References

- [iOS Developer Roadmap](https://roadmap.sh/ios)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- React Native
- Flutter
- Rust