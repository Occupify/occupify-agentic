# Android Developer

## Metadata
- Type: Role
- Domain: Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/android
- Related Roles:
  - Frontend Developer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Pick a Language
- **Kotlin**
  - Kotlin is a statically typed programming language developed by JetBrains and officially endorsed by Google for Android development. It runs on the JVM and is fully interoperable with Java.

### 1.2 The Fundamentals
- **Development IDE**
  - Android Studio is the official integrated development environment for Android development. It is built on IntelliJ IDEA and provides tools for code editing, debugging, performance profiling, and device emulation.
- **Basics of Kotlin**
  - Kotlin is a concise, multi-platform, and fun language developed by JetBrains. Learn how to use Kotlin for Android, server-side, and cross-platform development, and explore its features, news, and community.
- **Basics of OOP**
  - The basics of Kotlin cover the syntax and core concepts needed to write Kotlin programs. This includes variables, data types, control flow, functions, lambdas, classes, and Kotlin-specific features like null safety and extension functions.
- **Data Structures and Algorithms**
  - Data structures and algorithms cover how data is organized and processed efficiently in code. Common structures include lists, maps, sets, stacks, and queues; common algorithmic topics include sorting, searching, and recursion.
- **What is and how to use Gradle?**
  - Gradle is the build system used in Android projects to compile code, manage dependencies, and package applications. It uses Groovy or Kotlin DSL scripts to define project configuration.
- **Create a Basic Hello World App**
  - Creating a Hello World app is the starting point for hands-on Android development. It involves setting up a new project in Android Studio, writing a simple activity, and running it on an emulator or physical device.
- **Intent**
  - Intent in Android is a software mechanism used for late runtime binding between components, such as activities, content providers, and services. It is essentially a passive data structure holding an abstract description of an operation that the Android system is requested to perform.
- **Implicit Intents**
  - Implicit Intents do not specify the target component explicitly like Explicit Intents. Instead, they allow the system to find a suitable component matching the Intent description to handle the request.
- **Explicit Intents**
  - Explicit Intents are primarily used within an application's own boundaries. In explicit intents you specify the component that needs to be responded to the intent.
- **Broadcast Receiver**
  - A Broadcast Receiver is a component that listens for system-wide broadcast announcements. Common broadcasts include events like device boot, network connectivity changes, or battery status updates.
- **Content Provider**
  - A Content Provider manages access to a structured set of data and provides a standard interface for sharing data between apps. Platform apps like Contacts, Calendar, and Media Store expose their data through content providers.
- **Services**
  - A Service is an app component that performs long-running operations in the background without a user interface. Services handle tasks like playing music, downloading files, or processing data while the user interacts with other apps.

### 1.3 Version Control
- **Java**
  - Java was the original language for Android development and remains supported on the Android platform. It is a statically typed, object-oriented language that runs on the JVM.
- **Git**
  - Git is a highly efficient and flexible distributed version control system that was created by Linus Torvalds, the creator of Linux. It allows multiple developers to work on a project concurrently, providing tools for non-linear development and tracking changes in any set of files.
- **GitHub**
  - GitHub is a cloud-based hosting service for managing software version control using Git. It provides a platform for enabling multiple developers to work together on the same project at the same time.
- **Bitbucket**
  - Bitbucket is a Git repository hosting service by Atlassian. It integrates with other Atlassian tools like Jira and Confluence, making it a common choice for teams already using Atlassian products.
- **GitLab**
  - GitLab is a DevOps platform that includes Git repository hosting, CI/CD pipelines, issue tracking, and a container registry in a single product. It can be used as a cloud service or self-hosted on private infrastructure.

### 1.4 App Components
- **Activity**
  - An Activity represents a single screen in an Android app with a user interface. Apps are typically made up of multiple activities that users navigate between.
- **Activity LifeCycle**
  - The Activity lifecycle is a set of states and callbacks that an Activity goes through from creation to destruction. Key callbacks include onCreate, onStart, onResume, onPause, onStop, and onDestroy.
- **State Changes**
  - State changes occur when an Activity transitions between lifecycle states due to user actions or system events. Common triggers include pressing the Home button, rotating the device, or receiving a phone call.

---

## 2. Intermediate

### 2.1 Interface & Navigation
- **Tasks & Backstack**
  - A task is a collection of activities that the user interacts with to accomplish a goal, and the back stack keeps track of the order in which those activities were opened. When the user presses Back, activities are popped off the stack in reverse order.
- **Intent Filters**
  - Intent filters declare what types of intents a component can receive. They are defined in the AndroidManifest.xml file and describe the actions, data types, and categories a component supports.
- **Box**
  - A Box layout allows you to arrange UI elements in a single direction, either vertically or horizontally. It's a simple and effective way to organize views in a row or a column, providing control over how they are stacked and spaced.
- **Column / Row**
  - Column and Row are fundamental layout composables in Jetpack Compose used to arrange items vertically (Column) or horizontally (Row). They provide a simple and intuitive way to organize UI elements by stacking them in a single direction, offering control over how items are aligned and spaced within the layout.
- **TextField**
  - A TextField allows users to input and edit text on the screen. It provides a visual component, such as a box or line, where users can type in characters, typically using an on-screen keyboard or physical keyboard.
- **Image**
  - An image, in the context of Android development, refers to a visual representation displayed within an application's user interface. It allows developers to incorporate graphics, photographs, or illustrations into their apps to enhance visual appeal, provide context, or convey information.
- **Button**
  - A button is a fundamental UI element that triggers an action when tapped or clicked by the user. It allows users to initiate specific tasks within an application, such as submitting a form, navigating to another screen, or executing a function.
- **Text**
  - Text in Android refers to the display and manipulation of textual information within an application. It involves using UI elements like TextViews and EditTexts to show static text, collect user input, or dynamically update the content displayed on the screen.
- **BottomSheet**
  - A BottomSheet is a UI pattern that presents supplementary content from the bottom edge of the screen. It typically appears as a sheet that slides up to reveal more information or options related to the current screen or selected item.
- **Card**
  - In Jetpack Compose, a Card is a composable that provides a container with a rounded corner background and a subtle shadow. It's used to group related pieces of information, creating visual separation and improving the user interface's organization.
- **TabRow**
  - The Navigation Drawer in Android is a sliding menu from the left that simplifies navigation between important app links. It opens by sliding or via an icon in the ActionBar.
- **Icon**
  - In Jetpack Compose, an Icon is a composable function that displays a graphical image. You can use it to show vector drawables, raster images, or even custom shapes.
- **Dialog**
  - Animations can add visual cues that notify users about what's going on in your app. They are especially useful when the UI changes state, such as when new content loads or new actions become available.
- **Jetpack Compose**
  - Jetpack Compose is a modern toolkit for building native Android UI. It simplifies and accelerates UI development on Android with less code, powerful tools, and intuitive Kotlin APIs.
- **App Shortcuts**
  - App shortcuts in Android are designed to provide quick and convenient routes to specific actions or functions within your app from the device home screen. To use them, long-press an app's icon and a pop-up menu will appear with the available shortcuts.
- **Navigation Components**
  - The Navigation Components are part of Android Jetpack and are designed to simplify the implementation of navigation in your Android app. These components help you follow best practices, handle deep linking, and provide a consistent user experience across deep and conditional navigation.
- **Lazy Column / Row**
  - LazyColumn and LazyRow are composable functions in Jetpack Compose that efficiently display a large number of items in a scrollable list. Instead of composing all items at once, they only compose and render the items that are currently visible on the screen.
- **Drawer**
  - A Drawer is a panel that slides in from the edge of the screen to display navigation options and app content. Typically, it's triggered by a "hamburger" menu icon and provides a hierarchical way to access different sections within the application, offering a space-saving alternative to tabs or a navigation bar.
- **Animations**
  - Animations, in a broad sense, are visual effects that give the impression of movement by rapidly displaying a sequence of images or frames. In the context of user interfaces, animations enhance the user experience by providing visual feedback, guiding the user's attention, and making the interface feel more responsive and engaging.

### 2.2 Design & Architecture
- **Scaffold**
  - Scaffold, in simple terms, is a structure that provides a foundation for building a user interface. It typically includes common screen elements like an app bar (top bar), a body (the main content area), and optionally, a bottom navigation bar or a drawer.
- **Constraint**
  - ConstraintLayout is a layout manager in Android that gives you flexible control over the positioning and sizing of views within your user interface. It allows you to create complex layouts without nesting multiple view groups, which can improve performance.
- **RecycleView**
  - RecyclerView is a flexible and efficient view for displaying large sets of data in a scrollable list. It provides a mechanism for reusing view holders, which reduces memory consumption and improves performance when dealing with dynamic content.
- **Fragments**
  - A Fragment represents a reusable portion of your app's UI. A fragment defines and manages its own layout, has its own lifecycle, and can handle its own input events.
- **ImageView**
  - ImageView is a UI component that displays images in an Android application. It's used to show pictures, icons, and other visual content to users.
- **ConstraintLayout**
  - ConstraintLayout is a flexible and powerful layout manager for Android that allows you to position and size views using constraints relative to other views, the parent layout, or guidelines. It gives you fine-grained control over the placement of UI elements and helps create complex layouts without nesting multiple layout groups.
- **NavHost**
  - A NavHost is a special Android UI component, typically a Fragment, within your app that serves as a central point for navigating between different destinations. It's like the container that displays different parts of your app's user interface as the user moves from one screen to another.
- **remember / State**
  - remember is a Compose function that retains a value across recompositions within a composable. Combined with mutableStateOf, it creates a state holder that triggers recomposition when its value changes.
- **ViewModel state**
  - ViewModel state refers to the data held within a ViewModel class that persists across configuration changes, such as screen rotations. It allows your UI data to survive these changes, preventing the need to re-fetch or re-create it every time the activity or fragment is recreated.
- **Side effects**
  - In Jetpack Compose, side effects are actions that occur outside the composable function itself, such as updating a database, making a network request, or using shared mutable state. Compose recomposes when its inputs change and to avoid unpredictable behaviour, any code that interacts with the outside world needs to be carefully controlled, so Side Effects is a way for doing it in a predictable and testable manner.

### 2.3 Storage
- **MVI**
  - MVI (Model-View-Intent) is an architectural pattern where user actions are modeled as Intents that flow into the Model, which produces a new immutable State rendered by the View. It enforces strict unidirectional data flow and makes application state predictable and easy to test.
- **MVVM**
  - MVVM (Model-View-ViewModel) is an architectural pattern that separates the UI layer (View) from the business logic and state layer (ViewModel). The ViewModel exposes state and events, and the View observes and renders them reactively.
- **MVP**
  - MVP (Model-View-Presenter) is an architectural pattern where the Presenter acts as a mediator between the View and the Model. The View delegates user actions to the Presenter, which processes them and updates the View through an interface contract.
- **MVC**
  - MVC (Model-View-Controller) is an architectural pattern that divides an application into three components: the Model holds data and business logic, the View renders the UI, and the Controller handles user input. Android does not map cleanly to traditional MVC, as Activities and Fragments often act as both View and Controller simultaneously.
- **Shared Preferences**
  - Shared Preferences in Android are used to store data in key-value pairs. It works similar to a tiny database where you can save small pieces of data such as settings or the state of an application.
- **DataStore**
  - DataStore is Jetpack's modern replacement for Shared Preferences. It provides two implementations: Preferences DataStore for key-value storage and Proto DataStore for typed, schema-based storage using Protocol Buffers.
- **Room Database**
  - Room is an Android Jetpack library that provides an abstraction layer over SQLite. It uses annotations to define database entities, Data Access Objects (DAOs), and queries, and it verifies SQL at compile time.
- **File System**
  - The Android file system allows apps to read and write files to internal storage, external storage, and cache directories. Internal storage is private to the app, while shared storage is accessible to other apps through proper permissions and scoped storage APIs.

### 2.4 Security
- **Security**
  - Android security encompasses the strategies and techniques used to protect Android devices and the data they contain from unauthorized access, use, disclosure, disruption, modification, or destruction. It involves various layers of protection, including hardware security features, the Android operating system's security architecture, and application-level security measures, all working together to safeguard user data and device integrity.

### 2.5 Network
- **Repository Pattern**
  - The Repository Pattern separates the data sources from the rest of the application. It acts as a mediator between different data sources, such as persistent models, web services, or caches.
- **Builder Pattern**
  - The Builder Pattern in Android is used to construct complex objects step by step. It separates the construction of an object from its representation.
- **Factory Pattern**
  - The Factory pattern provides an interface for creating objects without specifying their exact class. It centralizes object creation logic, making it easier to swap implementations without modifying calling code.
- **Observer Pattern**
  - The Observer pattern defines a one-to-many dependency where multiple observers are notified automatically when a subject changes state. In Android, this pattern is the foundation of reactive data streams implemented through LiveData, Kotlin Flow, RxJava, and RxKotlin.
- **Flow**
  - Flow in Android development is part of the Kotlin Coroutines library. It is a type that can emit multiple values sequentially, making it perfect for working with any data streams or any streams of events that aren't instantaneous.
- **RxJava**
  - RxJava, standing for Reactive Extensions for the JVM, is a library in the Java and Android ecosystem that allows developers to write asynchronous, event-based programs. It is developed according to reactive programming principles and it supports multi-threading operations.
- **RxKotlin**
  - RxKotlin is a lightweight library that adds convenient extension functions to RxJava. It allows developers to use RxJava with Kotlin in a more idiomatic way, thus making code more readable and understandable.
- **Retro**
  - Retrofit is a type-safe HTTP client for Android. It's designed to connect your application with an API or a back-end web service.
- **OkHttp**
  - OkHttp is an HTTP client that's extremely efficient, enabling several advanced features in Android app or other platforms that use Java. Developed by Square, it's built for high efficiency and capacity, simplifying many networking tasks, including connection pooling, response caching, and request retries.
- **Apollo-Android**
  - Apollo Android is a GraphQL client for Android and Kotlin that generates type-safe Kotlin models from a GraphQL schema and query files. It handles query execution, caching, and subscriptions, and integrates with Kotlin coroutines.

### 2.6 Asynchronism
- **TextView**
  - TextView displays text to the user. It's a fundamental UI element in Android used to show static or dynamically updated content.
- **Coroutines**
  - Kotlin Coroutines are a concurrency framework that allows writing asynchronous code in a sequential, readable style. They are lightweight, support structured concurrency, and integrate with Android Jetpack through lifecycle-aware CoroutineScopes.
- **Threads**
  - Threads are the basic unit of concurrency in the JVM. Android runs UI operations on the main thread and requires network, database, and other slow operations to run on background threads.
- **RxJava**
  - RxJava (Reactive Extensions for the JVM) is a powerful library for composing asynchronous and event-based programs using observable sequences in Java. If you are an Android developer, you might be familiar with callbacks and async tasks to perform long-running operations in the background.
- **RxKotlin**
  - RxKotlin is a lightweight Kotlin extension library for RxJava. It adds idiomatic Kotlin extension functions and DSL-style utilities for working with RxJava observables.
- **Authentication**
  - Firebase Authentication provides backend services for authenticating users with email and password, phone numbers, or federated identity providers like Google, Facebook, and Apple. It manages tokens and session state securely.
- **Crashlytics**
  - Crashlytics is a lightweight, real-time crash reporter that helps you track, prioritize, and fix stability issues that dismantle your app's quality. It delivers fast and precise information about crashes and helps you gain insights into your app's performance so you can pinpoint the exact line of code your app crashed on.
- **Remote Config**
  - Firebase Remote Config allows developers to change the behavior and appearance of an Android app without publishing an app update. Configuration values are stored in the cloud and fetched at runtime.
- **Cloud Messaging**
  - Firebase Cloud Messaging (FCM) is a cross-platform messaging service for delivering push notifications and data messages to Android apps. Notifications can target individual devices, device groups, or topics that users subscribe to.
- **FireStore**
  - Firestore is Firebase's scalable, flexible NoSQL cloud database. It stores data as collections of documents and supports real-time listeners that push updates to connected clients instantly.

---

## 3. Advanced

### 3.1 Common Services
- **Google Admob**
  - Google AdMob is a mobile advertising platform designed for app developers to monetize their apps by displaying ads from over 1 million Google advertisers. AdMob supports a wide range of ad formats, such as banner ads, interstitial ads, video ads, and more.
- **Google Play Services**
  - Google Play Services is a background service that provides core Google APIs to Android apps, including authentication, location, maps, and in-app payments. It is automatically updated on compatible devices and required for many Android platform features.
- **Google Maps**
  - The Google Maps SDK for Android allows apps to embed interactive maps, display markers, draw routes, and access geolocation data. It is used in apps that require navigation, location search, or geographic visualization.
- **Espresso**
  - Espresso is a testing framework provided by Android to create UI tests for Android applications. It automatically synchronizes your test actions with the UI of your application, ensuring that your test will only proceed when the necessary UI activities have been completed.
- **JUnit**
  - JUnit is the standard testing framework for unit testing Java and Kotlin code on Android. Unit tests run on the local JVM without needing a device or emulator, making them fast to execute.

### 3.2 Linting
- **WorkManager**
  - WorkManager is a Jetpack library for scheduling deferrable, guaranteed background work. It supports constraints like requiring network connectivity or charging, survives app restarts and device reboots, and allows chaining multiple tasks together.
- **Ktlint**
  - Ktlint is a Kotlin linter and formatter that enforces the official Kotlin coding style. It can run manually, as part of a Gradle build, or as a pre-commit hook.
- **Detekt**
  - Detekt is a static code analysis tool for Kotlin that identifies code smells, complexity issues, potential bugs, and style violations. It is more configurable than Ktlint and covers a broader range of quality checks.
- **Timber**
  - Timber is a logging utility library for Android built on top of the standard android.util.Log API. It provides a cleaner logging interface, automatically includes class names in log tags, and makes it easy to control logging behavior per build variant.
- **Leak Canary**
  - LeakCanary is an open-source memory leak detection library for Android. It automatically monitors objects that should be garbage collected and reports leaks with a detailed analysis showing the reference chain causing the problem.

### 3.3 Testing
- **Testing**
  - Testing in Android ensures that app code behaves correctly and that UI interactions work as expected. JUnit is used for unit testing business logic, while Espresso handles UI testing by simulating user interactions on a device or emulator.

### 3.4 Debugging
- **LiveData**
  - LiveData is a lifecycle-aware observable data holder from Android Jetpack. It delivers updates to UI observers only when they are in an active lifecycle state, preventing crashes from updates sent to stopped components.
- **Dependency Injection**
  - Dependency Injection (DI) is a technique where objects receive their dependencies from an external source rather than creating them internally. In Android, DI frameworks manage the creation and lifecycle of dependencies across the app, improving testability and reducing coupling.
- **Dagger**
  - Dagger is a compile-time dependency injection framework for Java and Kotlin. It generates efficient DI code based on annotations, avoiding reflection at runtime.
- **Koin**
  - Koin is a lightweight dependency injection framework developed specifically for Kotlin developers. It uses functional resolution only - no proxy, no code generation, no reflection, and offers simplicity by leveraging Kotlin's language features.
- **Hilt**
  - Hilt is a dependency injection library for Android that reduces the boilerplate code that you would normally need to write when setting up manual dependency injection in your project. It is based on the Dagger library, but it simplifies the implementation process and streamlines the use of Dagger in Android apps.
- **Chucker**
  - Chucker is an in-app HTTP inspector for Android. It intercepts OkHttp network requests and responses and displays them in a dedicated UI within the app during development.
- **Jetpack Benchmark**
  - Jetpack Benchmark is a library within the Android Jetpack Suite that allows developers to quickly and accurately measure the performance of their apps. This library can help measure CPU, memory, and IO performance of code in Android apps.

### 3.5 Distribution
- **Firebase Distribution**
  - Firebase Distribution is a development tool within the Google Firebase suite that allows you to share pre-release versions of your Android apps with your development team. It enables you to distribute your app binaries to multiple testers and teams to get feedback before the app's official launch.
- **Google Playstore**
  - The Google Play Store is the official marketplace for distributing Android apps to users worldwide. Publishing an app requires a Google Play developer account, a signed AAB or APK, and compliance with Google's developer policies.
- **Signed APK**
  - A signed APK is an Android application package that has been digitally signed with a developer's certificate. Signing is required before an app can be published to the Google Play Store.

---

## 4. Optional / Specialized Topics

- What is and how to use Gradle?
- Create a Basic Hello World App
- Intent
- Implicit Intents
- Explicit Intents
- Broadcast Receiver
- Content Provider
- Services
- GitLab
- TextField
- Image
- Button
- Text
- BottomSheet
- Card
- TabRow
- Icon
- Dialog
- Jetpack Compose
- App Shortcuts
- Navigation Components
- Lazy Column / Row
- Drawer
- Animations
- ImageView

---

## 5. References

- [Android Developer Roadmap](https://roadmap.sh/android)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- React Native
- Flutter
- Java
- Spring Boot
- Rust