# Flutter

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/flutter
- Related Roles:
  - Android Developer
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Basics of Dart
- **Dart Pad**
  - DartPad is an online tool that allows developers to write and run Dart code snippets. It can also be used to run Flutter code, making it a convenient way to try out Flutter apps and widgets without having to set up a full development environment.
- **Variables**
  - In Flutter, variables are used to store values. There are three types of variables in Flutter namely local, global and instance variables.Variables in Flutter can store values of different data types, such as numbers, strings, booleans, and more.
- **Built-in Types**
  - There are several built-in data types, including int, double, String, bool, List, Sets, and Map. Additionally, there are other complex data types like dynamic, var, and Object in Dart programming language, which are used in Flutter.
- **Functions**
  - Dart is a true object-oriented language, so even functions are objects and have a type, Function. This means that functions can be assigned to variables or passed as arguments to other functions.
- **Control Flow Statements**
  - Dart's control flow statements manage program execution: if-else for conditional logic, for, while, and do-while loops for repetition, switch-case for multi-way selection, and break and continue to alter loop behavior, enabling complex program logic.
- **Flutter CLI**
  - Flutter CLI (Command Line Interface) is a command-line tool that is used to develop, build, and run Flutter applications. It provides a set of commands and tools that developers can use to create, test, and deploy Flutter apps from the terminal.
- **FVM**
  - Flutter version manager is a tool used to manage different versions of Flutter SDK on a developer's machine. Flutter is a popular open-source mobile application development framework, and its SDK is updated frequently with new features, bug fixes, and improvements.
- **VS Code**
  - VS Code is a lightweight but powerful code editor developed by Microsoft that provides comprehensive support for Flutter development. It includes a dedicated extension that offers essential features like code completion, syntax highlighting, and an integrated debugger to help developers build and test mobile applications efficiently.

### 1.2 Development Environment
- **Android Studio**
  - Android Studio is the official integrated development environment for Android app development, built by Google on the JetBrains IntelliJ IDEA platform. It provides a comprehensive suite of tools for Flutter developers, including an advanced code editor, integrated debugging, performance profiling, and an emulator for testing applications.
- **IntelliJ Idea**
  - IntelliJ IDEA is a powerful Integrated Development Environment (IDE) created by JetBrains. Essentially, it's a software application that provides comprehensive facilities to computer programmers for software development.

### 1.3 Widgets
- **Responsive Widgets**
  - Responsive widgets are specialized components in Flutter designed to adapt the layout and appearance of an application based on the size, orientation, or platform of the screen. These widgets utilize various builders and constraints to ensure that UI elements remain functional and visually consistent across mobile, tablet, and desktop devices.
- **Inherited Widgets**
  - Inherited widgets in Flutter are a powerful mechanism for efficiently propagating data down the widget tree. They essentially create a shared data scope that descendant widgets can access without needing to explicitly pass the data through constructors.
- **Stateless Widgets**
  - Stateless widgets in Flutter are widgets that don't maintain any mutable state. They are designed to be immutable and rebuild each time the framework needs to update the UI.
- **Stateful Widgets**
  - A stateful widget is dynamic: for example, it can change its appearance in response to events triggered by user interactions or when it receives data. Checkbox, Radio, Slider, InkWell, Form, and TextField are examples of stateful widgets.
- **Styled Widgets**
  - Styled widgets are a set of Flutter components designed to simplify the process of styling UI elements through method chaining. Instead of wrapping widgets in multiple parent containers like Padding, Align, or Container to adjust their appearance, you can directly call extension methods on the widget itself.

### 1.4 Working with Assets
- **Operators**
  - Flutter, and Dart, utilize various operators to manipulate data: arithmetic operators for math, relational operators for comparisons, logical operators for boolean logic, assignment operators for value assignment, and the ternary operator for concise conditional expressions, enabling diverse operations on values and variables.
- **Fonts**
  - Fonts in Flutter are text styles used to define the visual appearance of characters within an application. You can incorporate custom typefaces by adding font files to your project assets and declaring them in the pubspec.yaml file.
- **Images**
  - Images in Flutter are visual components used to display graphical content within an application's user interface. You can load these files from your project's local directory by declaring them in the pubspec.yaml file or fetch them directly from the network using a specific URL.
- **Other File Types**
  - Flutter allows you to include various file types in your application beyond standard images, such as JSON files, configuration files, fonts, or raw text documents. These assets are bundled within the application package and made accessible to the code through the root bundle mechanism.

### 1.5 Version Control Systems
- **Git**
  - Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

### 1.6 Repo Hosting Services
- **GitHub**
  - GitHub is a web-based platform that provides hosting for software development and version control using Git. It is widely used by developers and organizations around the world to manage and collaborate on software projects.

---

## 2. Intermediate

### 2.1 Design Principles
- **Dependency Injection**
  - Dependency Injection is a design pattern that allows objects to receive their dependencies from external sources instead of creating them internally. In Flutter, this can be useful for managing complex state, reducing coupling between components, and making testing easier.
- **Design Patterns**
  - Design patterns are solutions to common problems in software development that can be used to improve the quality and maintainability of your code.
- **SOLID Principles**
  - SOLID is a mnemonic acronym for five design principles intended to make object-oriented designs more understandable, flexible, and maintainable.
- **OOP**
  - Object-oriented programming (OOP) is a programming paradigm that is based on the concept of "objects," which are instances of a class. In OOP, a class is a blueprint for creating objects, which have both data (attributes) and behavior (methods).

### 2.2 Package Managers
- **Material Widgets**
  - Material Widgets are a collection of pre-built UI components in Flutter that follow the Material Design guidelines developed by Google. These widgets provide a standardized look and feel for applications, including common elements like buttons, cards, text fields, and navigation bars.
- **Cupertino Widgets**
  - Cupertino widgets are a set of Flutter widgets that mimic the look and feel of Apple's iOS user interface. They are designed to provide a consistent look and feel on both iOS and Android devices, and include widgets such as CupertinoButton, CupertinoAlertDialog, and CupertinoSlider.
- **pub.dev**
  - pub.dev is the official package repository for Dart and Flutter packages. It is a platform for hosting, managing, and distributing Dart packages and Flutter plugins.
- **flutter pub / dart pub**
  - flutter pub and dart pub are command-line tools used to manage dependencies in Flutter and Dart projects. These tools interact with the pub.dev package repository to download, update, and remove external libraries defined in a project's pubspec.yaml file.

### 2.3 Working with APIs
- **JSON Serialize / Deserialize**
  - JSON serialization and deserialization is the process of converting Dart objects into JSON strings for network transmission and transforming JSON data received from an API back into usable Dart objects. In Flutter, this is typically handled by mapping data fields to class properties using the jsonserializable package or by manually defining fromJson and toJson methods.
- **Web Sockets**
  - In addition to normal HTTP requests, you can connect to servers using WebSockets. Web sockets allows for bidirectional communication between a client (such as a web browser) and a server over a single, long-lived connection.
- **GraphQL**
  - GraphQL is a query language for your API that allows clients to request exactly the data they need, and nothing more. It was developed by Facebook and released as open source in 2015.
- **RESTful APIs**
  - REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.

### 2.4 Storage
- **SQLite**
  - SQLite is an open-source, lightweight relational database management system (RDBMS) used to store and manage data. It is written in C and self-contained, meaning it does not require a separate server process or system.
- **Shared Preferences**
  - In Flutter, SharedPreferences is a plugin allowing you to store data in key-value pairs persistently. It is similar to a local database or cache, but it is specifically designed to store small pieces of data, such as user preferences or settings.
- **Firebase**
  - Firebase is Google's mobile development platform that provides backend services like authentication, the Cloud Firestore database, cloud storage, and push notifications. The FlutterFire plugins integrate these services into Flutter apps, letting you add a backend without running your own servers.
- **Authentication**
  - Firebase Authentication is a service provided by Firebase that allows you to easily add user authentication to your Flutter app. With Firebase Authentication, you can authenticate users using email and password, phone number, or popular identity providers like Google, Facebook, and more.
- **Core Libraries**
  - Dart has a rich set of core libraries that provide essentials for many everyday programming tasks such as working on collections of objects (dart:collection), making calculations (dart:math), and encoding/decoding data (dart:convert).

### 2.5 Advanced Dart
- **Storage**
  - In Flutter, you can use Firebase Storage to store and retrieve binary data, such as images, audio files, and videos. Firebase Storage is a cloud-based storage service provided by Firebase that makes it easy to store and serve large binary data, such as images and videos, in your Flutter app.
- **Lists**
  - Dart Flutter offers various widgets for displaying lists, including ListView, ListTile, SingleChildScrollView with Column, GridView, and CustomScrollView with Slivers, enabling scrolling lists, grids, and customized item appearances through widgets, layouts, and styling.
- **Streams**
  - Streams in Flutter are a way to receive data over time as it becomes available. They are similar to observables in other languages and frameworks.
- **Futures**
  - A Future represents a potential value or error that will be available at some time in the future. It is a core mechanism in Dart used for handling asynchronous operations, allowing a program to initiate a task and continue executing other code while waiting for the task to complete.
- **Collections**
  - Dart provides built-in collections like Lists (ordered, indexed), Sets (unordered, unique), Maps (key-value pairs), Queues (FIFO), and Stacks (LIFO) for efficient data storage and manipulation, useful in various scenarios like data storage, state management, and algorithm implementation.
- **Lambdas**
  - Lambdas, also known as anonymous functions, are a fundamental concept in Dart and Flutter. They are a way to create short, inline functions that can be passed as arguments to other functions or assigned to variables.
- **Functional Programming**
  - Dart supports functional programming through higher-order functions, immutable data structures, lambdas/closures, and pure functions, enabling developers to write code that emphasizes immutability, statelessness, and data transformation via functions.
- **Isolates**
  - Flutter Isolates are parallel execution contexts that enhance performance and concurrency by running intensive tasks in the background, preventing UI freezes. They provide isolated memory spaces for reliable code, enable concurrent execution, and facilitate inter-isolate communication for data sharing and coordination, though developers must consider context-switching and communication overhead.
- **Async / Await**
  - Flutter's async/await pattern simplifies asynchronous programming by enabling code that appears synchronous. The async keyword designates a function as asynchronous, allowing non-blocking execution, while await pauses execution until an asynchronous operation completes, resulting in cleaner and more maintainable asynchronous code.

### 2.6 State Management
- **ChangeNotifier**
  - Flutter's ChangeNotifier is a fundamental class for state management in Flutter. It allows developers to handle and notify listeners of data changes, ensuring efficient updates to the user interface.
- **ValueNotifier**
  - Flutter's ValueNotifier is a lightweight tool for state management in Flutter. It efficiently handles a single value and notifies listeners of changes.
- **Redux**
  - Redux is a state management library for Flutter, commonly used with the Flutter framework to manage the application's state. It helps to maintain a single source of truth for the state of the application, making it easier to understand, test and maintain the code.
- **Riverpod**
  - Riverpod was created by the same author as Provider, and is designed to make it easier to manage application state by providing a more intuitive API and better performance than Provider. One of the key features of Riverpod is its ability to manage and scope state in a more granular way than Provider.
- **BLoC**
  - Bloc (Business Logic Component) is a state management pattern used in Flutter to separate presentation logic from business logic. It helps to manage and maintain the app state, making it easier to test, debug, and reuse code.
- **Provider**
  - Provider is a wrapper around InheritedWidget (base class for widgets that efficiently propagate information down the tree) to make them easier to use and more reusable.
- **GetX**
  - GetX is a lightweight and powerful solution for state management and navigation in Flutter. It provides a clean and simple API for managing app state and navigating between screens.
- **Animation Controller**
  - An Animation Controller is a special class in Flutter that manages the state of an animation by generating a sequence of values over a specific duration. It acts as the engine that drives an animation forward, backward, or stops it completely based on a range typically defined between 0.0 and 1.0.

### 2.7 Reactive Programming
- **Firestore**
  - Firebase Firestore is a cloud-based NoSQL document database service provided by Firebase that makes it easy to store, manage, and retrieve data in your Flutter app. Firestore is a flexible, scalable, and easy-to-use database that allows you to store and retrieve data in the form of documents, collections, and fields.
- **Push Notifications**
  - Implementing Firebase push notifications in Flutter involves setting up a Firebase project, integrating the FCM plugin, handling and displaying incoming notifications within the app, testing through the Firebase Console or tools like Postman, and customizing notification appearance with icons, sounds, and vibration patterns.
- **Remote Config**
  - Firebase Remote Config, accessed in Flutter via the firebaseremoteconfig plugin, enables dynamic app behavior and appearance changes without app updates. This involves adding the plugin, initializing the service, defining default parameter values in the console or code, fetching and retrieving remote parameters, and updating those parameters either through the console or by activating fetched values, allowing for A/B testing and feature control.
- **Cloud Functions**
  - Cloud Functions for Firebase is a serverless computing platform that simplifies backend development by allowing developers to write JavaScript or TypeScript code, which runs automatically in response to events from Firebase services or incoming HTTP requests. This framework leverages Google's cloud infrastructure to provide a scalable and managed environment, making it easier to build powerful serverless applications without the need for server maintenance.
- **RxDart**
  - RxDart is a library for Dart that provides additional functionality for working with reactive programming, specifically with the Streams and Observables classes. It extends the standard Dart Streams API and provides additional features such as the ability to transform and combine streams, and to compose and chain streams together.

### 2.8 Animations
- **Animated Builder**
  - AnimatedBuilder is a widget in Flutter that allows you to build animations. It takes an Animation object and a builder function as input, and it returns a widget that is rebuilt whenever the animation changes.
- **Animated Widget**
  - AnimatedWidget is a Flutter widget that takes an Animation object as an argument and automatically updates whenever the animation changes. This can be useful when you want to create animations that are tightly coupled to a widget, for example, to animate the size or color of a widget.
- **Curved Animation**
  - Curved animations in Flutter can be achieved using the "CurvedAnimation" class. This class takes in a "Curve" object that defines the rate of change of the animation over time.
- **Opacity**
  - Opacity is a Flutter widget that allows you to control the transparency of its child widget. It takes a single opacity argument, which is a value between 0.0 and 1.0, where 0.0 represents complete transparency and 1.0 represents complete opacity.

---

## 3. Advanced

### 3.1 Testing
- **Unit Testing**
  - Unit testing in Flutter is the process of testing individual units of code, such as functions or classes, to ensure that they behave as expected. Unit testing helps to catch bugs early in the development process and increases the confidence in your code by making it easier to refactor or make changes without breaking existing functionality.
- **Widget Testing**
  - Widget testing in Flutter is the process of testing the behavior and appearance of individual widgets, in isolation from the rest of your app. It allows you to verify that a widget works correctly, displays the expected output, and behaves correctly in response to user interactions.
- **Integration Testing**
  - Integration tests in Flutter are tests that verify the behavior of your app as a whole, rather than individual widgets or functions. Integration tests allow you to test the interactions between different parts of your app and verify that the overall behavior of the app is correct.
- **TDD**
  - Test-driven development (TDD) is a software development methodology in which tests are written before the implementation of the code they are testing. The idea behind TDD is to write a failing test first, then write just enough code to make the test pass, and then refactor the code if necessary.
- **BDD**
  - Behavior-driven development (BDD) is a software development methodology that emphasizes collaboration between developers, testers, and stakeholders to define and verify the behavior of an application. BDD uses natural language to describe the expected behavior of the application and provides a shared understanding of the requirements for the development team.

### 3.2 Dev Tools
- **Hero**
  - Hero animations in Flutter refer to the motion that occurs when a widget transitions from one screen to another. By wrapping two widgets on different pages with a Hero widget and assigning them the same unique tag, the framework automatically animates the shared element across the screen transition.
- **Flutter Inspector**
  - It is a tool in the Flutter SDK that provides a visual representation of the widget tree in a Flutter app. It allows developers to inspect the widgets in their app, see the properties and styles applied to each widget, and interact with the app in real-time.
- **Flutter Outline**
  - Flutter Outline is a feature in the Flutter development environment (IDE) that provides a tree-like representation of the widgets and elements in your Flutter app. It shows the hierarchy of the widgets, their relationships, and the structure of your app.

### 3.3 Flutter Internals
- **Render Objects**
  - RenderObject's can be defined as "Objects" that render and manipulate layouts, sizes and draw the UI, providing the actual application rendering. They clean up some resources when dispose method is called, therefore it must be disposed by creator when is no longer used.
- **3 Trees**
  - A tree is a data structure that is used to represent the hierarchy of widgets in a Flutter app. The tree structure allows Flutter to manage the layout, styling, and behavior of the widgets in the app.
- **Immutability**
  - Immutability in Flutter refers to objects that cannot be changed once they are created. In Flutter, immutability is used to ensure that objects in the widget tree are not modified unexpectedly, which can lead to unexpected behavior and bugs in the app.
- **Fast Lane**
  - Fastlane is an open-source tool suite that automates the release process for mobile applications. It handles repetitive tasks such as generating screenshots, managing code signing identities, and deploying builds to the Apple App Store or Google Play Store.
- **Codemagic**
  - Codemagic is a continuous integration and continuous delivery platform specifically designed to automate the build, test, and release process for Flutter applications. It integrates directly with your version control systems to trigger automated pipelines whenever code changes are pushed.

### 3.4 CI / CD
- **Bitrise**
  - Bitrise is a cloud-based continuous integration and delivery (CI/CD) platform that can be used with Flutter mobile app development. Bitrise provides a comprehensive suite of tools for automating the build, test, and deployment process for mobile apps, including apps built with Flutter.
- **GitHub Actions**
  - GitHub Actions is a workflow automation tool provided by GitHub that can be used to automate various tasks in a Flutter mobile app development process. With GitHub Actions, developers can create custom workflows to automate tasks such as building the app, running tests, and deploying the app to various app stores.
- **Firebase App Dist**
  - Firebase App Distribution is a service that allows developers to easily distribute pre-release versions of their applications to trusted testers. It provides a centralized dashboard where you can upload your Flutter build artifacts, such as APK or IPA files, and automatically notify testers via email once a new version is available.

### 3.5 Analytics
- **Memory Allocation**
  - Memory allocation is the process of reserving a portion of the device's memory for the use of your app. The memory allocation in Flutter is managed by the Dart virtual machine, which uses a garbage collector to automatically manage the memory used by the app.
- **Segment**
  - Segment is an analytics platform that provides a single API for collecting, storing, and routing customer data from various sources, including mobile apps built with Flutter. With Segment, Flutter developers can easily add analytics tracking to their app, without having to integrate with multiple analytics tools individually.
- **Mix Panel**
  - Mixpanel is a product analytics platform that provides insights into user behavior for mobile apps, including those built with Flutter. With Mixpanel, Flutter developers can track user interactions with their app, including page views, events, and user properties, and use this data to gain insights into user behavior.
- **Firebase Analytics**
  - Firebase Analytics is a free analytics tool provided by Google that helps to understand user behavior and measure app performance for mobile apps, including those built with Flutter. With Firebase Analytics, Flutter developers can track user interactions with their app, including page views, events, and user properties, and use this data to gain insights into user behavior.
- **Google Analytics**
  - Google Analytics is a free web analytics service provided by Google that helps to understand user behavior and measure app performance for mobile apps, including those built with Flutter. With Google Analytics, Flutter developers can track user interactions with their app, including page views, events, and user properties, and use this data to gain insights into user behavior.

### 3.6 Deployment
- **Guidelines & Protocols**
  - Deployment guidelines and protocols in Flutter encompass the standardized procedures and best practices required to prepare, build, and release applications to app stores or internal distribution channels. This process involves configuring release builds with optimized assets, securing API keys, managing versioning, and adhering to platform-specific submission requirements for both the Apple App Store and Google Play Store.
- **AppStore**
  - The App Store is Apple's platform for distributing iOS and iPadOS applications. Publishing a Flutter app there requires an Apple Developer account, app metadata, signing with certificates and provisioning profiles, and submitting the build for App Review before release.
- **Playstore**
  - The Google Play Store is an online store for Android apps, games, and other digital content. It is operated by Google and is the official app store for Android devices.

---

## 4. Optional / Specialized Topics

- Android Studio
- IntelliJ Idea
- Material Widgets
- Cupertino Widgets
- Images
- Other File Types
- SQLite
- Shared Preferences
- Redux
- BLoC
- Provider
- GetX
- Codemagic
- GitHub Actions
- Segment
- Mix Panel
- Firebase Analytics
- Google Analytics

---

## 5. References

- [Flutter Roadmap](https://roadmap.sh/flutter)

---

## 6. Related Roles / Topics

### Related Roles
- Android Developer
- Backend Developer
- DevOps Engineer

### Related Skills
- React Native
- Python
- Go