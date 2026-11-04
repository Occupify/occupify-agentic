# Vue.js

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/vue
- Related Roles:
  - Frontend Developer

---

## 1. Beginner

### 1.1 App Configurations
- **Props**
  - If we are building a blog, we will likely need a component representing a blog post. We want all the blog posts to share the same visual layout, but with different content.
- **Error / Warn Handler**
  - Debugging in Vue.js involves identifying and fixing issues in your Vue applications. It’s an essential part of the development process, and there are several tools and techniques you can use to effectively debug your Vue code.
- **Global Properties**
  - Global properties allows you to add properties or methods that can be accessed throughout your application. This is particularly useful for sharing functionality or data across components without the need to pass props explicitly.
- **Performance**
  - Key areas to improve Vue.js performance include lazy loading components to minimize initial load times, optimizing rendering to prevent unnecessary re-renders, implementing efficient state management using modern libraries like Pinia, reducing the bundle size by code splitting and tree shaking, utilizing virtual scrolling for large lists and tables, continuously monitoring performance to detect potential bottlenecks, and minimizing dependencies to decrease overall load.

### 1.2 Components
- **create-vue**
  - create-vue is a CLI tool that helps you create a new Vue project with a single command. It is a simple and easy-to-use tool that saves you time and effort when setting up a new Vue project.
- **Single File Components**
  - Vue Single-File Components (a.k.a. .vue files, abbreviated as SFC) is a special file format that allows us to encapsulate the template, logic, and styling of a Vue component in a single file.
- **Component Registration**
  - A Vue component needs to be "registered" so that Vue knows where to locate its implementation when it is encountered in a template. There are two ways to register components: global and local.
- **v-model**
  - v-model is a directive that allows you to create two-way data bindings on form input, textarea, and select elements. It automatically picks the correct way to update the element based on the input type.
- **Attribute Inheritance**
  - Attribute inheritance aka "fallthrough attributes" is a feature of Vue.js that allows you to inherit attributes from a parent component.

### 1.3 Templates
- **Events**
  - As we develop our applications we may need to communicate with the parent component in order to notify of some actions e.g. when a user clicks on a button.

### 1.4 API Styles
- **Options API**
  - Vue offers many approaches for how to write components, including the Options API. It is the only API that is available in all versions of Vue.
- **Composition API**
  - Vue offers many approaches for how to write components, including the "Composition API", which is most commonly used via "Script Setup". This approach is based around pulling in low level atomic functions used by Vue's reactivity engine.

### 1.5 Directives
- **v-text**
  - The v-text directive is used to set the textContent property of an element. It's important to note that when using this directive it will overwrite the HTML content inside the element.
- **v-html**
  - The v-html directive is similar to the v-text directive, but the difference is that v-html renders its content as HTML. This means that if you pass an HTML element it will be rendered as an element and not plain text.
- **v-bind**
  - The v-bind directive dynamically binds an HTML attribute to data. The shorthand for this directive is :
- **v-model**
  - v-model is a directive that creates a two-way data binding between a form input element and a piece of reactive state. It automatically syncs the value of the input with the corresponding data property, ensuring that whenever the user types into an input field, the underlying state updates, and whenever the state changes programmatically, the input display updates to match.
- **v-pre**
  - v-pre is a directive used to tell Vue to skip the compilation process for a specific element and all of its children. By using this directive, any mustache-style syntax or Vue-specific expressions inside the element are displayed exactly as they are written in the source code rather than being processed by the framework.

---

## 2. Intermediate

### 2.1 Lifecycle Hooks
- **Conditional Rendering**
  - The directive v-if is used to conditionally render a block. The block will only be rendered if the directive's expression returns a truthy value.

### 2.2 Forms Handling
- **Input Bindings**
  - Input bindings are a way to bind user input to a component's data. This allows the component to react to user input and update its state accordingly.
- **v-model**
  - v-model is a directive that creates a two-way data binding between a form input element and a component's state. It automatically synchronizes the value shown in the input field with the corresponding data property in your script, ensuring that updates in the UI reflect in the application logic and vice versa.
- **Modifiers**
  - Modifiers are special suffixes that can be added to directives (such as v-model and v-bind) to alter their behavior. Modifiers allow you to specify additional functionality or constraints to the binding, making it more flexible and powerful.

### 2.3 Event Handling
- **Binding Events**
  - Vue.js is an open-source Model–View–ViewModel front-end JavaScript framework for building user interfaces and single-page applications. Vue.js has many own directives for DOM manipulation such as v-bind, v-on, v-model, etc.
- **Inline / Method Handlers**
  - In Vue.js, inline handlers are defined directly in the template using expressions, making them suitable for simple tasks. For example, you might use an inline handler to increment a counter.
- **Event Modifiers**
  - In Vue.js, event modifiers are special postfixes that you can add to event handlers to control the behavior of events more easily. They help simplify common tasks such as stopping propagation, preventing default actions, and ensuring that the event is triggered only under certain conditions.
- **Key Modifiers**
  - Input bindings are a way to bind user input to a component's data. This allows the component to react to user input and update its state accordingly.
- **Async Components**
  - In large applications, we may need to divide the app into smaller chunks and only load a component from the server when it's needed. To make that possible, Vue has a defineAsyncComponent function.
- **Teleport Components**
  - Sometimes we may run into the following scenario: a part of a component's template belongs to it logically, but from a visual standpoint, it should be displayed somewhere else in the DOM, outside of the Vue application. This is where the <Teleport> component comes in.
- **Provide / Inject**
  - Usually, when we need to pass data from the parent to a child component, we use props. However, imagine the case where we have a large component tree, and a deeply nested component needs something from a distant ancestor component.
- **Custom Directives**
  - So far you may have covered two forms of code reuse in Vue: components and composables. Components are the main building blocks, while composables are focused on reusing stateful logic.
- **Plugins**
  - Plugins are self-contained code that usually add app-level functionality to Vue.

### 2.4 Computed Properties
- **Rendering Lists**
  - We can use the v-for directive to render a list of items based on an array. The v-for directive requires a special syntax in the form of item in items, where items is the source data array and item is an alias for the array element being iterated on.
- **v-show**
  - v-show is similar to v-if in that it allows you to conditionally render components. However, it does not remove the component from the DOM and merely toggles its display CSS property to be hidden.
- **v-if**
  - v-if is a directive used to conditionally render an element or a block based on the truthiness of an expression. When the expression evaluates to true, the element is added to the Document Object Model (DOM), and when it evaluates to false, the element is removed.
- **v-else**
  - The v-else conditionally renders an element or a template fragment as a function in case the v-if does not fulfil the condition.
- **v-else-if**
  - This directive is used to add additional conditions to a v-if and v-else block.
- **v-for**
  - The v-for directive is used to render an HTML element, a block of elements, or even a component based on an array, an object, or a set number of times. When using this directive it is important to assign a unique key to each item to avoid issues and improve performance.
- **v-on**
  - The v-on directive is placed on an element to attach an event listener. To attach an event listener with v-on we need to provide the event type, and any modifier, and a method or expression that should run when that event occurs.
- **v-once**
  - v-once is a built-in directive used to render an element or component only once and skip future updates during subsequent re-renders. Once the initial content is rendered, the data bindings are removed, meaning any changes to the associated data will not trigger updates to that specific part of the DOM.
- **Optimizing Renders**
  - Optimizing rendering is crucial for ensuring a smooth and efficient user experience across all your frontend projects. Sluggish webpages can lead to frustration for users, and potentially cause them to entirely abandon your web application.
- **Debugging**
  - Debugging in Vue.js involves identifying and fixing issues in your Vue applications. It’s an essential part of the development process, and there are several tools and techniques you can use to effectively debug your Vue code.

### 2.5 SSG
- **Mouse Button Modifiers**
  - Mouse button modifiers are a type of modifier that can be used with event handlers to specify which mouse button or buttons should trigger the event. These modifiers allow you to customize the behavior of event handlers, such as v-on:click, to respond to specific mouse button clicks.
- **Watchers**
  - Computed properties allow us to declaratively compute derived values. However, there are cases where we need to perform "side effects" in reaction to state changes - for example, mutating the DOM, or changing another piece of state based on the result of an async operation.
- **Slots**
  - In some cases, we may want to pass a template fragment to a child component, and let the child component render the fragment within its own template. The <slot> element is a slot outlet that indicates where the parent-provided slot content should be rendered.
- **Quasar**
  - Quasar Framework is an open-source Vue.js based framework for building apps, with a single codebase, and deploy it on the Web as a SPA, PWA, SSR, to a Mobile App, using Cordova for iOS & Android, and to a Desktop App, using Electron for Mac, Windows, and Linux.
- **VitePress**
  - Vitepress is a static site generator that is built on top of Vite. It is a lightweight and fast static site generator that is designed to work with Vue 3.

### 2.6 Routing
- **v-slot**
  - The v-slot directive to define slots in components, allowing you to pass and render content dynamically inside a component. For named slots, you use v-slot with a specific slot name.
- **v-cloak**
  - The v-cloak directive is used to prevent the uncompiled Vue template from being visible while the Vue instance is still loading. It temporarily hides the content until Vue has finished compiling the template.
- **VueUse**
  - VueUse is a collection of utility functions based on Composition API. It has over 200+ functions, is tree-shakable, has first-class TypeScript support, and has a small bundle size.
- **Vue Router**
  - Vue Router is the official router for Vue.js which allows creating static/dynamic routes, has support for navigation interception, allows for component based configuration and much more.
- **Tailwind CSS**
  - CSS Framework that provides atomic CSS classes to help you style components e.g. flex, pt-4, text-center and rotate-90 that can be composed to build any design, directly in your markup.

---

## 3. Advanced

### 3.1 Forms
- **FormKit**
  - FormKit helps build forms faster by simplifying form structure, generation, validation, theming, submission, error handling, and more.
- **Vee Validate**
  - VeeValidate is a form validation library for Vue that allows you to handle input validation, error messages, and form state management with ease. It provides a set of components and composition functions that integrate directly into your templates, making it straightforward to define rules for your inputs and display reactive feedback to the user based on their interactions.

### 3.2 SSR
- **Transition**
  - Transitions are a built-in mechanism that automatically applies CSS classes to elements or components when they enter or leave the DOM. By wrapping content in a special transition component, you can define specific styles for various stages of the animation process—such as the starting point, the active phase, and the finished state.
- **Transition Group**
  - <TransitionGroup> is a built-in component designed for animating the insertion, removal, and order change of elements or components that are rendered in a list.
- **Nuxt.js**
  - Nuxt.js is a free and open source JavaScript library based on Vue.js, Node.js, Webpack and Babel.js. Nuxt is inspired by Next.js, which is a framework of similar purpose, based on React.js.
- **Vitest**
  - Vitest is a fast Vite-native unit test framework with out-of-box ESM and TypeScript support. It Works on React, Vue, Svelte and more projects created with Vite.
- **Vue Testing Library**
  - The Vue Testing Library is a very lightweight solution for testing Vue components. Its primary guiding principle is: The more your tests resemble the way your software is used, the more confidence they can give you.
- **Cypress**
  - Cypress framework is a JavaScript-based end-to-end testing framework built on top of Mocha – a feature-rich JavaScript test framework running on and in the browser, making asynchronous testing simple and convenient. It also uses a BDD/TDD assertion library and a browser to pair with any JavaScript testing framework.

### 3.3 State Management
- **Vuetify**
  - Vuetify is a Vue UI Library with beautifully handcrafted Material Components. No design skills required — everything you need to create amazing applications is at your fingertips.
- **Pinia**
  - Pinia is a store library for Vue.js, and can be used in Vue 2 and Vue 3, with the same API, except in SSR and its installation. It allows state sharing between pages and components around the application.

### 3.4 API Calls
- **Apollo**
  - Apollo is a platform for building a unified graph, a communication layer that helps you manage the flow of data between your application clients (such as web and native apps) and your back-end services.
- **Axios**
  - Axios is a client HTTP API based on the XMLHttpRequest interface provided by browsers. The most common way for frontend programs to communicate with servers is through the HTTP protocol.
- **fetch**
  - The fetch() method in JavaScript is used to request to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON or XML.
- **Tanstack Query**
  - TanStack Query is a data fetching and caching library for Vue.js and React. It is a part of the TanStack ecosystem.

### 3.5 Mobile Apps
- **Vuelidate**
  - Vuelidate is a lightweight, model-based validation library for Vue applications that uses a decoupled approach to handle form validation. It allows you to define validation rules as simple JavaScript objects, which are then mapped to your component's data properties to track their validity status.
- **Playwright**
  - Playwright Test was created specifically to accommodate the needs of end-to-end testing. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
- **Element UI**
  - Element UI is another Vue.js component library with several built-in components to style your Vue.js applications.
- **Capacitor**
  - Since Vue.js is a web framework, it does not natively support mobile app development. So how do we get access to native mobile features such as the camera and geolocation?

---

## 4. Optional / Specialized Topics

- Attribute Inheritance
- v-pre
- Async Components
- Teleport Components
- Provide / Inject
- Custom Directives
- Plugins
- v-else-if
- v-for
- v-on
- v-once
- Optimizing Renders
- Debugging
- VitePress
- Tailwind CSS
- Vue Testing Library
- Cypress

---

## 5. References

- [Vue.js Roadmap](https://roadmap.sh/vue)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer

### Related Skills
- JavaScript
- React
- Angular
- Node.js