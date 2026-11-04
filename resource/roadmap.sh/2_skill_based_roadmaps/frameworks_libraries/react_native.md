# React Native

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/react-native
- Related Roles:
  - Frontend Developer
  - Android Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is React Native?**
  - React Native is an open-source framework created by Meta that allows developers to build mobile applications for iOS and Android using JavaScript and React. It enables the creation of apps that provide a native look and feel by leveraging native platform components rather than using web views.
- **Why use React Native?**
  - React Native allows developers to build mobile applications for both iOS and Android using a single codebase written in JavaScript and React. It achieves this by bridging your code to native platform components, which provides a smooth user experience and performance similar to apps built with platform-specific languages.
- **React Native Alternatives**
  - React Native is a popular choice for cross-platform application development, but there are other options available. Some of the common alternatives to React Native are Flutter, Ionic and Xamarin.

### 1.2 Learn the Pre-requisites
- **JavaScript Basics**
  - JavaScript is a versatile programming language that serves as the foundation for building interactive and dynamic applications. It enables developers to manipulate content, control multimedia, animate elements, and handle complex logic within a codebase.
- **CSS Basics**
  - CSS is a stylesheet language used for describing the look and formatting of a document written in HTML or XML. It is primarily used for styling web pages and user interfaces written in HTML and XHTML.

### 1.3 Environment Setup
- **Components**
  - React components are the building blocks of the user interface (UI) in a React application. They are used to break down the UI into reusable, isolated, and manageable pieces.
- **State**
  - State is an object that holds data managed within a React component. It allows components to become dynamic and interactive by keeping track of its data changes.
- **JSX**
  - JSX is a syntax extension for JavaScript that allows you to write HTML-like code within your JavaScript code. It was developed to be used with React and has become an integral part of working with React.
- **Props**
  - In React, props are short for properties and are used to pass data from a parent component to a child component. They are similar to function arguments, and they help make components reusable and maintainable.
- **Expo**
  - Expo is a framework and platform for React Native that simplifies the development process by providing a set of tools and services that abstract away complex native code configurations. It allows developers to build, test, and deploy applications across iOS, Android, and the web using a unified codebase.
- **React Native CLI**
  - The React Native Community CLI (@react-native-community/cli) is the command-line tool for creating and running React Native apps without a framework such as Expo. This method requires you to manually set up the native development environment and tools needed for iOS and Android app development.
- **Metro Bundler**
  - Metro Bundler is the default bundler for React Native applications. It's a JavaScript module bundler that takes all your application code and dependencies, and bundles them together into a single JavaScript file or multiple files (based on platform).

### 1.4 Development Workflow
- **create-expo-app**
  - create-expo-app is a command line tool that generates a React Native project that works out of the box with Expo. It is the easiest way to get started building a new React Native application.
- **Expo Snack**
  - Expo Snack is an online playground and development environment for creating and testing React Native projects. With Snack, you can easily edit and preview your code changes directly in your browser or on a mobile device using the Expo Go app.
- **Expo Tradeoffs**
  - Expo is a managed framework that simplifies React Native development by providing a set of pre-built tools, libraries, and services. While it offers a faster development cycle and easier configuration, it comes with specific limitations regarding native code control.
- **Running on Device**
  - Running your React Native application on a physical device allows you to test your code in a real-world environment, providing a more accurate representation of performance, touch interactions, and hardware integration compared to an emulator or simulator. To achieve this, you connect your mobile device to your development machine via USB or a local Wi-Fi network and use tools like Metro Bundler to transmit the application bundle directly to the device.
- **In-App Developer Menu**
  - The In-App Developer Menu is a built-in interface in React Native that provides essential tools for debugging and development. By triggering this menu through a specific gesture or keyboard shortcut, you can access features such as refreshing the application, enabling fast refresh, inspecting elements, and toggling performance monitors.
- **Enabling Fast Refresh**
  - Fast Refresh is a React Native feature that allows you to get near-instant feedback while making changes in your code. It achieves this by reloading only the portion of the app that was changed, without losing the current state.
- **SafeAreaView**
  - SafeAreaView is a component designed to render content within the safe area boundaries of a device screen. It automatically applies padding to ensure that your UI elements, such as text or buttons, are not obscured by system notches, home indicators, or rounded corners found on modern smartphones.

### 1.5 Core Components
- **LogBox**
  - LogBox is React Native's in-app display for logs, warnings, and errors during development. It groups and formats them, with stack traces for errors, so problems are easier to spot and address in your code.
- **Sourcemaps**
  - Sourcemaps are files that act as a bridge between your bundled, minified JavaScript code and the original source code you actually wrote. When an error occurs in a production environment, the stack trace typically points to the transformed bundle, which is difficult to read.
- **DevTools**
  - React Native DevTools is the modern, built-in debugging experience for React Native. It is designed for debugging React app concerns, such as inspecting components, stepping through JavaScript, and profiling, while the native layers are still debugged with the tools in Android Studio and Xcode.
- **Text**
  - The Text component is a basic element in React Native used to display text content on the screen. While it has some basic styling properties, you usually nest it inside other components (e.g., View) to create more complex UIs.
- **Button**
  - A Button is a built-in React Native component used to create clickable buttons. It is a simple, customizable and easy-to-use component that captures touches and triggers an onPress event when pressed.
- **ImageBackground**
  - ImageBackground is a React Native core component that allows you to display an image as a background while still being able to place content inside the component. This helps in creating beautiful layouts with images and text or other content on top.
- **ActivityIndicator**
  - The ActivityIndicator is a core component in React Native that provides a simple visual indication of some ongoing activity or loading state within your application. It shows a spinning animation, which gives the user feedback that something is happening in the background.
- **Modal**
  - A Modal is a component that displays content on top of the current view, creating an overlay that can be used for various purposes, such as displaying additional information, confirmation messages, or a selection menu.
- **View**
  - View is the fundamental layout container in React Native, similar to a div in web development. It supports flexbox layout, styling, touch handling, and nesting, and is the building block for nearly every screen and component.
- **KeyboardAvoidingView**
  - KeyboardAvoidingView is a built-in React Native component that automatically adjusts its children components' position when the keyboard opens, preventing them from being obscured by the on-screen keyboard. It's a useful component, particularly for forms and input fields where the user needs to see the text they're typing.
- **Listings**
  - Listings in React Native — primarily FlatList and SectionList — are the core components for rendering scrollable lists. They are optimized for large data sets with lazy row rendering, pull-to-refresh, header and footer support, and per-row memoization for better performance.

---

## 2. Intermediate

### 2.1 Writing Platform Specific Code
- **ScrollView**
  - In React Native, the ScrollView is a generic scrolling container used to provide a scrollable view to its child components. It is useful when you need to display scrollable content larger than the screen, such as lists, images, or text.
- **ListViews**
  - ListView was the original list component in React Native, now superseded by the more efficient FlatList and SectionList. These components render data in a performant, scrollable way by only mounting rows near the viewport, and support features like separators, empty states, and pull-to-refresh.
- **FlatList**
  - FlatList is a React Native core component that displays a scrolling list of changing, but similarly structured, data. It is an efficient list component that makes use of a limited scrolling renderWindow, reducing the memory footprint and creating smooth scrolling.
- **SectionList**
  - SectionList is a component used to render sections and headers in a scroll view. It helps to manage and optimize a large list of items divided into categories.
- **RefreshControl**
  - RefreshControl is a component in React Native that is used to provide pull-to-refresh functionality for scrollable components like ScrollView, ListView, and FlatList.
- **Platform Module**
  - The Platform module in React Native provides a simple way to detect the operating system on which your application is currently running. It exposes a constant that allows you to branch your code logic based on whether the app is executing on iOS, Android, or other supported platforms.
- **File Extensions**
  - File extensions like .ios.js and .android.js allow React Native to automatically select the correct implementation based on the platform where the application is running. When you import a module with these specific extensions, the packager detects the operating system and loads the file that matches the target platform.

### 2.2 Styling
- **Text Input**
  - TextInput is a core component in React Native that allows the user to enter text. It is commonly used to collect user data, like emails or passwords.
- **Image**
  - The Image component is used to display images in a React Native application. It allows you to load and display local as well as remote images, providing essential props and methods for better image handling and customization.
- **Switch**
  - A Switch is a visual component in React Native that provides a toggle interface for users to switch between two states, typically on and off. It functions as a controlled component, meaning it relies on a boolean value passed through properties to determine its current state and a callback function to handle changes when the user interacts with it.
- **StatusBar**
  - The StatusBar component is used to control the appearance of the status bar on the top of the screen. It may strike as a bit unusual since, unlike other React Native components, it doesn't render any visible content.
- **Pressable**
  - Pressable is a core component in React Native that makes any view respond properly to touch or press events. It provides a wide range of event handlers for managing user interactions, such as onPress, onPressIn, onPressOut, and onLongPress.
- **Stylesheets**
  - In React Native, stylesheets are objects that define the appearance of components. They provide a way to separate styling from the component's logic.
- **Layouts & Flexbox**
  - Layouts and Flexbox in React Native provide a system for arranging elements on the screen. It is based on the CSS Flexbox algorithm, which allows you to define how components are positioned, spaced, and sized within a container.

### 2.3 Networking
- **Connectivity Status**
  - Connectivity refers to the mechanisms that allow data transfer between your React Native app and external resources through various means of communication. It is essential to ensure efficient communication with APIs, servers, and external systems, to update your app's data, fetching content or enabling real-time interactions.
- **WebSockets**
  - WebSockets are a protocol that allows full-duplex communication between a client and a server over a single, long-lived connection. They are useful when real-time communication is needed, such as in chat applications, online gaming, or financial trading platforms.
- **Fetch**
  - Fetch is a JavaScript function available in React Native that is used to make network requests, similar to XMLHttpRequest in web applications. It allows you to handle requests and retrieve data from APIs or other sources.

### 2.4 Push Notifications
- **Accessibility**
  - Accessibility (often abbreviated as a11y) in React Native is a crucial aspect of application development that ensures your applications are usable by everyone, including individuals with disabilities. This commitment to inclusivity is not just a legal requirement in many jurisdictions but also a moral imperative that enhances the user experience for all.

### 2.5 Interactions
- **react-native-web**
  - React Native for Web is a library that allows developers to run React Native components and APIs on the web using React DOM. It maps React Native components, such as Views and Text, to their equivalent HTML elements, enabling the reuse of a single codebase across mobile and browser platforms.
- **Touchables**
  - In React Native, Touchable components are used to handle user interactions like taps, long presses, and double-taps on the appropriate elements. Each of these components is from the react-native package, except TouchableScale which is from react-native-touchable-scale.
- **Gesture Handling**
  - Gesture handling is an essential and powerful feature in React Native that helps create interactive and responsive user interfaces. React Native provides several built-in components and libraries to recognize and respond to different types of user gestures.
- **Scrolling & Swiping**
  - In React Native, scrolling and swiping interactions can be defined and customized with a set of built-in components. These components are efficient and provide fluid navigation through the elements inside them.
- **Screen Navigation**
  - In React Native, navigating from one screen to another is a crucial aspect of app development. The most commonly used navigation libraries are React Navigation and React Native Navigation.
- **Animations**
  - Animations in React Native allow developers to create smooth, fluid, and dynamic user interfaces by changing the properties of components over time. The framework provides the Animated API to handle simple, high-performance transitions, as well as the LayoutAnimation API for animating global layout changes.

### 2.6 DeepLinking
- **DeepLinking**
  - Deep linking in React Native allows your app to open and navigate to a specific screen or content when a user clicks on a URL or a custom URI scheme. It essentially creates a direct pathway into a particular section of your application, bypassing the typical app launch sequence and providing a more seamless user experience.

### 2.7 Security
- **Authentication**
  - Authentication is the process of verifying the identity of a user before granting them access to specific features or data within a mobile application. In React Native, this typically involves managing secure user sessions through methods like OAuth, JWT (JSON Web Tokens), or biometric authentication.
- **Networking**
  - Networking security in React Native involves protecting the data transmitted between your application and a backend server to prevent unauthorized access or interception. This is primarily achieved through the use of HTTPS (SSL/TLS) to encrypt communication, alongside best practices like implementing certificate pinning to verify the server's identity and validating all incoming data from API responses.
- **Storage**
  - Storage in React Native refers to the various methods used to save data persistently on a mobile device so that information remains available even after the application is closed. Developers typically choose between options like AsyncStorage for simple key-value pairs, SQLite for structured relational data, or Encrypted Storage for sensitive information.
- **react-native-async-storage**
  - Async Storage is an unencrypted, asynchronous, persistent key-value storage system for React Native. It was removed from React Native core and now lives in the community package @react-native-async-storage/async-storage.
- **Permissions**
  - Permissions in React Native are how your app requests access to sensitive user data or device features, like the camera, microphone, or location. When your app needs to use one of these features, it must first ask the user for permission.

---

## 3. Advanced

### 3.1 Storage
- **expo-secure-store**
  - Expo Secure Store is a built-in package provided by the Expo SDK to store encrypted data securely on users' devices. It is a key-value storage system, but it is not designed to store larger amounts of data such as app databases or complex data structures.
- **expo-file-system**
  - Expo File System is a universal module that provides access to the file system on the device. Using this module, you can perform various file operations like reading, writing, copying, moving, and deleting files and folders.
- **Jest**
  - Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It works with projects using: Babel, TypeScript, Node, React, Angular, Vue and more!

### 3.2 Testing
- **expo-sqlite**
  - expo-sqlite is a module that provides an interface for a local SQLite database in React Native applications. It allows developers to store, query, and manage structured data directly on a device using standard SQL commands.
- **Other Storage Options**
  - Beyond basic local storage solutions, React Native applications often require more specialized ways to manage data. These options include libraries like SQLite for relational database management, Realm for high-performance object-oriented storage, or WatermelonDB for reactive data synchronization.
- **React Test Renderer**
  - React Test Renderer is a library provided by the React team that allows you to render React components as JavaScript objects without depending on the DOM or a native mobile environment. The package is now deprecated, and the React team recommends migrating tests to React Native Testing Library instead.
- **React Native Testing Library**
  - React Native Testing Library (RNTL) is a collection of tools and utilities to test React Native components. It is built on top of the Testing Library ecosystem, designed to work seamlessly with Jest and other testing frameworks.
- **Detox**
  - Detox is an end-to-end testing framework for React Native applications. It enables you to run tests on an actual device or in a simulator/emulator environment.
- **Appium**
  - Appium is an open-source test automation framework for mobile devices, targeting native, hybrid, or mobile-web apps for iOS, Android, and Windows platforms. Appium works with multiple programming languages, including JavaScript, Ruby, Python, Java, and C#.

### 3.3 Performance
- **Understand Frame Rates**
  - Frame rate measures the frequency at which individual images, known as frames, are displayed on a screen to create the illusion of motion. In React Native applications, maintaining a consistent frame rate—typically 60 frames per second—is essential for ensuring that animations and transitions feel smooth and responsive to the user.
- **Common Problem Sources**
  - Performance issues in React Native often stem from an overloaded JavaScript thread, which handles business logic, API calls, and state management. When this thread becomes blocked by heavy computations or excessive re-renders, the user interface feels unresponsive or choppy.
- **Speeding up Builds**
  - Building your React Native app could be expensive and take several minutes of developers time. This can be problematic as your project grows and generally in bigger organizations with multiple React Native developers.
- **Optimizing Flatlist Config**
  - Optimizing Flatlist configuration involves fine-tuning the properties of the Flatlist component to improve scrolling performance and memory usage in large data lists. By leveraging props such as initialNumToRender, maxToRenderPerBatch, windowSize, and removeClippedSubviews, developers can control how many items are rendered at once and how off-screen elements are handled.
- **RAM Bundles + Inline Requires**
  - Inline requires defer loading a module until it is first used instead of at startup, which trims the time to interactive for apps with many screens or rarely used features. Random Access Module (RAM) bundles are an older format that served the same purpose by loading modules on demand, but they are not supported with Hermes, whose bytecode gives the same or better startup performance.
- **Profiling**
  - Use the built-in profiler to get detailed information about work done in the JavaScript thread and main thread side-by-side. Access it by selecting Perf Monitor from the Debug menu.

### 3.4 Using Native Modules
- **For iOS**
  - iOS native modules in React Native allow developers to tap into the rich ecosystem of iOS features and functionalities that are not directly accessible through the standard React Native APIs. For instance, a Camera module can be implemented using the AVFoundation framework, enabling developers to capture photos and videos directly from their applications.
- **For Android**
  - Native modules in React Native provide a powerful way to access device-specific features and capabilities that are not available through the standard React Native APIs. For example, a Bluetooth module can be created using the Android Bluetooth API, allowing applications to scan for nearby Bluetooth devices, connect to them, and transfer data.

### 3.5 Publishing Apps
- **Apple App store**
  - The App Store is Apple's official platform for distributing iOS apps to users with iPhones, iPads, and iPod Touch devices. To publish an app on the App Store, you need to follow specific guidelines and use the necessary tools provided by Apple.
- **Google Play Store**
  - Google Play Store is a digital distribution platform that allows developers to publish and release their React Native applications to Android users worldwide. To distribute an app, developers must create a Google Play Console account, sign their application with a secure keystore file, and generate an Android App Bundle (AAB).

---

## 4. Optional / Specialized Topics

- Expo
- React Native CLI
- Metro Bundler
- In-App Developer Menu
- Enabling Fast Refresh
- SafeAreaView
- Button
- ImageBackground
- ActivityIndicator
- Modal
- View
- KeyboardAvoidingView
- Listings
- RefreshControl
- Platform Module
- File Extensions
- Pressable
- Stylesheets
- Layouts & Flexbox
- Screen Navigation
- Animations
- Permissions
- Detox
- Appium
- RAM Bundles + Inline Requires

---

## 5. References

- [React Native Roadmap](https://roadmap.sh/react-native)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Android Developer

### Related Skills
- JavaScript
- React
- Flutter