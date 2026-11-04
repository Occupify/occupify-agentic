# React

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/react
- Related Roles:
  - Frontend Developer

---

## 1. Beginner

### 1.1 CLI Tools
- **Vite**
  - Vite is a build tool that starts a development server almost instantly and updates the browser as soon as you save a file. It uses native ES modules during development instead of bundling everything upfront, which makes it much faster than older tools.

### 1.2 Components
- **Functional Components**
  - Functional components are some of the more common components that will come across while working in React. These are simply JavaScript functions.
- **JSX**
  - JSX is a syntax extension for JavaScript that lets you write HTML-like code inside your JavaScript files. React uses it to describe what the UI should look like, and it gets compiled into regular JavaScript function calls behind the scenes.
- **Props vs State**
  - Props (short for “properties”) and state are both plain JavaScript objects. While both hold information that influences the output of component render, they are different in one important way: props get passed to the component (similar to function parameters) whereas state is managed within the component (similar to variables declared within a function).
- **Component Lifecycle**
  - The component lifecycle describes the different stages a component goes through, from being created and added to the page, to updating, and finally being removed. In function components, lifecycle behavior is handled through hooks like useEffect instead of separate lifecycle methods.
- **Lists and Keys**
  - Rendering a list in React usually means mapping over an array of data and returning a component for each item. React needs a unique key for each item in the list so it can track which elements changed, were added, or were removed.
- **Render Props**
  - A render prop is a pattern where a component takes a function as a prop and calls it to decide what to render. This allows the component to share logic with whatever gets rendered, without dictating the exact UI.

### 1.3 Rendering
- **Conditional Rendering**
  - Conditional rendering means showing different UI depending on a condition, such as whether a user is logged in or a list is empty. In React, this is often done with plain JavaScript, using if statements, ternary operators, or logical AND.
- **Composition**
  - Composition means building complex components by combining smaller, simpler ones. Instead of relying on inheritance, React encourages passing components as props or nesting them as children to reuse logic and layout.
- **Refs**
  - Refs provide a way to access DOM nodes or React elements created in the render method. In the typical React dataflow, props are the only way that parent components interact with their children.
- **Events**
  - React wraps native browser events in its own system called synthetic events, so they behave consistently across different browsers. You attach event handlers directly in JSX, such as onClick or onChange, and they receive an event object similar to the native one.
- **High Order Components**
  - A higher order component, often shortened to HOC, is a function that takes a component and returns a new component with extra behavior or props added. It is a pattern for reusing logic across multiple components, such as handling authentication checks or loading states.

### 1.4 Hooks
- **useEffect**
  - useEffect is a special hook that lets you run side effects in React. It is similar to componentDidMount and componentDidUpdate, but it only runs when the component (or some of its props) changes and during the initial mount.
- **Creating Custom Hooks**
  - A custom hook is a function you write yourself that starts with "use" and calls other hooks inside it. It lets you extract reusable logic, such as fetching data or tracking window size, out of a component and share it across multiple components.
- **useCallback**
  - useCallback is a React hook that returns a memoized version of a callback function. It's used to optimize performance by preventing unnecessary re-renders.
- **useRef**
  - useRef is a React hook that provides a way to create a mutable reference that persists across component re-renders. It stores a value that doesn't cause re-renders when it changes.
- **useState**
  - useState is a React Hook that lets you add state to functional components. When you call useState, you get back the current state value and a function to update it, allowing components to store and manage data that persists between renders.
- **Hooks Best Practices**
  - To fully leverage the capabilities of React Hooks, it is crucial to adopt best practices that not only enhance code readability but also optimize performance. By adhering to these practices, developers can create cleaner, more maintainable components that make the most of React's powerful features, leading to a more efficient and enjoyable development experience.

### 1.5 Routers
- **useMemo**
  - useMemo is a React hook that memoizes the result of a function. It is used to optimize performance by caching the result of a function and returning the cached result when the inputs to the function have not changed.
- **useReducer**
  - useReducer: An alternative to useState. Accepts a reducer of type (state, action) => newState, and returns the current state paired with a dispatch method.
- **useContext**
  - The useContext Hook lets us share data between components without having to pass props down through every level of the component tree. This is particularly useful when many components need to access the same data or when components are deeply nested.
- **Tanstack Router**
  - Tanstack Router is a routing library built with type safety in mind, generating types based on your route definitions. It supports features like nested routes, loaders for fetching data before a page renders, and search parameter validation.
- **React Router**
  - React Router is a standard library for routing in React applications. It enables navigation between different views or components within a single-page application (SPA) without requiring the browser to reload the page.

### 1.6 State Management
- **Context**
  - Context is a built-in React feature that lets you share data across the component tree without passing it through props at every level. You create a context, provide a value at some point in the tree, and any component below can read that value with useContext.
- **Zustand**
  - Zustand is a small state management library that uses a single store defined with a simple function, without requiring reducers or actions like Redux. Components can read and update the store directly through a hook, with minimal boilerplate.
- **Jotai**
  - Jotai is a state management library built around small, independent units of state called atoms. Instead of one large central store, you create atoms as needed and combine them however you like.

---

## 2. Intermediate

### 2.1 Writing CSS
- **Tailwind CSS**
  - Tailwind CSS is a utility-first CSS framework where you style elements by combining small, single-purpose classes directly in your markup. Instead of writing custom CSS files, you apply classes like flex, p-4, or text-center straight in the JSX.
- **Panda CSS**
  - Panda CSS is a CSS-in-JS tool that generates static CSS at build time instead of at runtime. You write styles using a type-safe API in your components, and Panda extracts and compiles them into optimized CSS files.
- **CSS Modules**
  - CSS Modules let you write regular CSS files where class names are automatically scoped to the component that imports them. This avoids the common problem of class name collisions across a large codebase.
- **MobX**
  - MobX is a state management library based on observable data, where changes to state automatically trigger updates in any component using that data. It relies on decorators or plain functions to mark state as observable, and React components re-render only when the specific data they use changes.

### 2.2 Component / Libraries
- **Chakra UI**
  - Chakra UI is a component library that provides accessible, ready-to-use React components along with a styling system based on style props. It focuses on accessibility and developer experience out of the box, with sensible defaults for spacing, color, and responsive design.
- **Material UI**
  - Material UI, often called MUI, is a component library that implements Google's Material Design guidelines in React. It provides a wide range of components, from buttons to complex data tables, with built-in theming support.
- **Shadcn UI**
  - Shadcn is an open-source framework providing pre-built, accessible, and customizable UI components for rapid web application development. It offers a streamlined approach to construct modern user interfaces.

### 2.3 Headless Components
- **Radix UI**
  - Radix UI is an open-source library designed to make it easier to create accessible and customizable User Interface (UI) components in React. It provides developers with a range of unstyled, fully accessible primitives, giving them complete control over the appearance and behavior of their UI elements.
- **React Aria**
  - React Aria is style-free out of the box, allowing you to build custom designs to fit your application or design system using any styling and animation solution. Each component is broken down into individual parts with built-in states, render props, and slots that make styling a breeze.
- **Ark UI**
  - Ark UI is a headless component library that provides the state and accessibility logic for common UI patterns, and works across multiple frameworks, not just React. It gives full control over markup and styling while handling the more complex interaction logic behind the scenes.
- **Apollo**
  - Apollo Client is a library for working with GraphQL APIs in React. It handles sending queries and mutations, caching the results, and keeping the UI in sync as data changes.
- **Base UI**
  - Understand fundamental concepts, architectures, and implementation practices of Base UI.

### 2.4 API Calls
- **Relay**
  - Relay is a JavaScript client used in the browser to fetch GraphQL data. It's a JavaScript framework developed by Facebook for managing and fetching data in React applications.
- **urql**
  - urql is a lightweight GraphQL client for React, built to be simpler and smaller than alternatives like Apollo or Relay. It supports caching, and its behavior can be extended through a system of exchanges, which are similar to middleware.

### 2.5 Testing
- **swr**
  - SWR is a data fetching library for React whose name comes from "stale-while-revalidate", a caching strategy where old data is shown immediately while fresh data loads in the background. It handles caching, revalidation, and re-fetching on focus or network reconnect with minimal setup.
- **Tanstack Query**
  - TanStack Query, previously known as React Query, is a powerful library for fetching, caching, synchronizing, and updating server state in your React applications. It simplifies the process of handling asynchronous data, reducing boilerplate code and improving the user experience by providing features like automatic retries, background updates, and optimistic updates.
- **Axios**
  - Axios is a promise-based HTTP client used to make requests from a React app to a server. It works similarly to the built-in fetch function but adds features like automatic JSON parsing, request and response interceptors, and easier error handling.
- **rtk-query**
  - RTK Query is a data fetching and caching tool that is included in the Redux Toolkit package. It is designed to simplify common use cases for fetching data, including caching, polling, and invalidation.
- **Jest**
  - Jest is a JavaScript testing framework commonly used for unit and integration tests in React projects. It includes a test runner, assertion library, and mocking tools all in one package, so there is little extra setup needed.
- **Vitest**
  - Vitest is a testing framework built to work closely with Vite, sharing its configuration and fast startup time. It is designed as a drop-in alternative to Jest, with a similar API but faster execution, especially in projects already using Vite for their build setup.
- **react-testing-library**
  - The React Testing Library is a very lightweight solution for testing React components. It provides light utility functions on top of react-dom and react-dom/test-utils, in a way that encourages better testing practices.
- **Cypress**
  - Cypress framework is a JavaScript-based end-to-end testing framework built on top of Mocha – a feature-rich JavaScript test framework running on and in the browser, making asynchronous testing simple and convenient. It also uses a BDD/TDD assertion library and a browser to pair with any JavaScript testing framework.
- **Playwright**
  - Playwright is an end-to-end testing tool built by Microsoft that can run tests across multiple browsers, including Chromium, Firefox, and WebKit. It supports features like automatic waiting for elements and parallel test execution, which helps keep test suites fast and reliable as they grow.

### 2.6 Forms
- **React Hook Form**
  - React Hook Form is a library for managing form state and validation in React with minimal re-renders. It uses uncontrolled inputs by default, registering fields through refs instead of updating state on every keystroke, which improves performance for large forms.
- **Formish**
  - Formisch is a lightweight library designed to simplify the process of handling forms in web applications by managing state, validation, and submission logic with minimal boilerplate. It provides a set of hooks and components that allow you to track user input, display error messages, and handle form resets efficiently.

### 2.7 Frameworks
- **Next.js**
  - Next.js is a React framework that adds features like server-side rendering, static site generation, and file-based routing on top of React. It handles a lot of the setup that would otherwise need to be configured manually, and it is widely used for production applications that need good performance and SEO.
- **Astro**
  - Astro is the web framework for building content-driven websites like blogs, marketing, and e-commerce. Astro is best-known for pioneering a new frontend architecture to reduce JavaScript overhead and complexity compared to other frameworks.
- **react-router**
  - As a framework, react-router extends beyond simple client-side navigation to include features like data loading, actions, and nested layouts, similar to what full frameworks like Next.js offer. It grew out of the original React Router library into a more complete solution for building routed applications.
- **Formik**
  - Formik is a library for building forms in React, handling values, validation, and submission through a consistent API. It uses controlled inputs, meaning form state is tracked in React state as the user types.

### 2.8 Types & Validation
- **TypeScript**
  - TypeScript is a superset of JavaScript that adds static typing, letting you catch type-related errors before running the code. In React, it is used to type props, state, and function signatures, which helps catch mistakes like passing the wrong data to a component.
- **Zod**
  - Zod is a schema validation library for TypeScript that lets you define the shape of your data and validate it at runtime, while also inferring TypeScript types from that same schema. It is commonly used to validate form input or API responses, so the same source of truth defines both validation and types.
- **Valibot**
  - Valibot is a modular and type-safe schema validation library designed to be extremely lightweight and fast. It allows you to define schemas for your data and automatically infer TypeScript types from them, ensuring that the inputs your application receives match the expected structure.

---

## 3. Advanced

### 3.1 Animation
- **Framer Motion**
  - Framer Motion is an animation library for React that lets you animate components with simple props, such as defining an initial state, an animate state, and a transition. It supports gestures, layout animations, and page transitions, and integrates naturally with React's component model.
- **react spring**
  - React Spring is a popular animation library for React that leverages the principles of spring physics to create smooth, natural-looking animations. Unlike traditional animation libraries that rely on keyframes and linear transitions, React Spring uses spring-based physics to produce fluid and realistic animations that can dynamically respond to user interactions and state changes.
- **GSock**
  - GSAP (GreenSock Animation Platform) is a framework-agnostic JavaScript animation library that turns developers into animation superheroes. Build high-performance animations that work in every major browser.

### 3.2 Error Boundaries
- **Error Boundaries**
  - An error boundary is a component that catches JavaScript errors thrown by its child components during rendering, preventing the whole app from crashing. Instead of showing a broken UI, it can display a fallback message.

### 3.3 Server APIs
- **Server APIs**
  - The react-dom/server APIs let you render React components to HTML on the server. These APIs are only used on the server at the top level of your app to generate the initial HTML.

### 3.4 Suspense
- **Suspense**
  - Suspense is a React feature that lets a component "wait" for something, such as data or code, before rendering, showing a fallback UI in the meantime. It was originally built for code splitting with lazy loading, and has since been extended to support data fetching in some frameworks and libraries.

### 3.5 Portals
- **Portals**
  - A portal lets you render a component's children into a different part of the DOM, outside its parent's normal hierarchy. This is useful for things like modals or tooltips that need to visually sit above other content, even though logically they still belong to their original component in React's tree.

### 3.6 Mobile Applications
- **React Native**
  - React Native is an open-source UI software framework created by Meta Platforms, Inc. It is used to develop applications for Android, Android TV, iOS, macOS, tvOS, Web, Windows and UWP by enabling developers to use the React framework along with native platform capabilities.

---

## 4. Optional / Specialized Topics

- Tanstack Router
- Context
- Panda CSS
- Chakra UI
- Material UI
- CSS Modules
- React Aria
- Ark UI
- Relay
- urql
- swr
- Axios
- rtk-query
- Jest
- Cypress
- react-router
- Formik
- react spring
- GSock
- MobX
- Formish
- Valibot

---

## 5. References

- [React Roadmap](https://roadmap.sh/react)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer

### Related Skills
- TypeScript
- JavaScript
- Angular
- Vue.js
- Node.js