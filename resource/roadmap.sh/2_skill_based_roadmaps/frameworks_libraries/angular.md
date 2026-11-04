# Angular

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/angular
- Related Roles:
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction to Angular
- **Angular Architecture**
  - Angular architecture describes the structure of an application through a collection of interconnected building blocks, including modules, components, services, and directives. Components define the user interface by managing specific views, while services handle data and shared business logic.
- **Setting up a New Project**
  - The Angular CLI provides a command-line interface to initialize, develop, and scaffold Angular applications. By running the ng new command, the tool generates a workspace with a predefined directory structure, configuration files, and necessary dependencies.
- **Angular and History**
  - Angular is a TypeScript-based open-source front-end web framework developed and maintained by Google. It is used for building dynamic, single-page web applications (SPAs).
- **Component Anatomy**
  - A component in Angular consists of three main parts: a TypeScript class that handles the logic and data, an HTML template that defines the visual structure, and CSS styles that control the appearance. These parts work together to encapsulate a specific piece of the user interface, allowing developers to define how a section of the application behaves and looks in one unified location.
- **Template**
  - template metadata is a property defined within the @Component decorator that specifies the HTML template for the component. It allows you to define the structure and layout of the component's view.
- **Standalone**
  - A standalone component is a component that sets standalone: true in its component metadata. Standalone components directly import other components, directives, and pipes used in their templates
- **Selector**
  - In Angular, the selector metadata is a crucial property defined within the @Component decorator that specifies how the component can be identified and used in HTML templates. It determines the way the component is rendered in the DOM, allowing developers to create reusable and easily identifiable components.
- **Metadata**
  - Metadata in Angular components refers to the configuration information that is used to define and configure the behavior of a component. It is specified using decorators, which are functions that add metadata to classes, properties, and methods.
- **Module Architecture**
  - Angular's module architecture uses NgModules to organize applications into cohesive units. These modules group related components, directives, pipes, and services, promoting modular development.
- **Creating Components**
  - A component is the fundamental building block of a user interface that consists of an HTML template, a TypeScript class to handle logic, and CSS styles to define the appearance. To create one, you typically use the Angular CLI command ng generate component followed by the component name, which automatically scaffolds the necessary files and registers the new component within your module.

### 1.2 Components
- **Provider**
  - Providers are objects that tell the Angular dependency injection system how to obtain a value or an instance of a dependency. When a component or service needs a specific dependency, the provider acts as a configuration that instructs the injector to create that instance, return an existing one, or use a specific factory function to generate it.

### 1.3 Communication
- **changeDetection**
  - Change detection is the mechanism that keeps the user interface in sync with the underlying application state. It automatically monitors the component's data and updates the Document Object Model (DOM) whenever changes occur.
- **viewProvider**
  - viewProviders is a configuration property used within a component's decorator to define a set of injectable dependencies that are available only to that component and its child components. When services are declared here, they are restricted to the component's shadow DOM and any components nested within its template, effectively scoping the dependency injection container.
- **Encapsulation**
  - Encapsulation determines how the styles defined in a component are applied to the rest of the application. It offers three distinct strategies: Emulated, which uses shadow-piercing CSS to scope styles to the component; ShadowDom, which leverages the native browser Shadow DOM API for true style isolation; and None, which applies component styles globally to the entire document.
- **Styles**
  - This metadata allows developers to apply CSS styles directly to a component, enhancing its appearance and ensuring that styles are scoped to that particular component.
- **Imports**
  - The imports property specifies the standalone component's template dependencies — those directives, components, and pipes that can be used within its template.
- **Parent-Child Interaction**
  - Parent-child interaction refers to the mechanism of data flow between a parent component and its nested child component. A parent component passes data down to a child using the @Input() decorator, which allows the child to receive and display dynamic information.
- **ViewChild**
  - ViewChild is a decorator that allows a component to gain direct access to a child component, directive, or a DOM element within its own template. By using this tool, you can reference specific elements from the HTML and interact with their properties or methods directly from the TypeScript class.
- **ContentChild**
  - ContentChild is a decorator used to access the first element or directive that matches a specific selector from the content projected into a component. It allows a parent component to interact directly with elements or child components passed through <ng-content> by providing a reference to the DOM element or class instance.

### 1.4 Modules
- **Creating Modules**
  - Creating modules in Angular helps organize your application into manageable, cohesive units. Each module can encapsulate related components, directives, pipes, and services.
- **Feature Modules**
  - Feature modules are NgModules for the purpose of organizing code. With feature modules, you can keep code related to a specific functionality or feature separate from other code.
- **Lazy Loading Modules**
  - By default, NgModules are eagerly loaded. This means that as soon as the application loads, so do all the NgModules, whether they are immediately necessary or not.
- **Dependencies**
  - Dependencies are external pieces of code or services that a module needs to function correctly. When a module requires specific functionality provided by another part of the application, it lists these items as requirements to ensure they are available for use within the component ecosystem.

### 1.5 Understand Binding
- **Interpolation**
  - Interpolation refers to embedding expressions into marked up text. By default, interpolation uses the double curly braces {{ and }} as delimiters.
- **Template Statements**
  - Template statements are methods or properties that you can use in your HTML to respond to user events. With template statements, your application can engage users through actions such as displaying dynamic content or submitting forms.
- **Data Binding**
  - In an Angular template, a binding creates a live connection between a part of the UI created from a template (a DOM element, directive, or component) and the model (the component instance to which the template belongs). This connection can be used to synchronize the view with the model, to notify the model when an event or user action takes place in the view, or both.
- **Property Binding**
  - Property binding helps you set values for properties of HTML elements or directives. To bind to an element's property, enclose it in square brackets [] which causes Angular to evaluate the right-hand side of the assignment as a dynamic expression.
- **Attribute Binding**
  - Attribute binding in Angular helps you set values for attributes directly. With attribute binding, you can improve accessibility, style your application dynamically, and manage multiple CSS classes or styles simultaneously.

### 1.6 Templates
- **Structural Directives**
  - Structural directives are instructions used to modify the layout of the DOM by adding, removing, or manipulating elements. These directives are identified by an asterisk () prefix and control the structure of the application view based on specific conditions or data collections.
- **Attribute Directives**
  - Attribute directives are classes that modify the appearance or behavior of an existing DOM element. They are applied to elements as attributes, allowing you to change styles, toggle classes, or register event listeners on specific components.

### 1.7 Template Syntax
- **Component Lifecycle**
  - A component instance has a lifecycle that starts when Angular instantiates the component class and renders the component view along with its child views. The lifecycle continues with change detection, as Angular checks to see when data-bound properties change, and updates both the view and the component instance as needed.
- **Dynamic Components**
  - In addition to using a component directly in a template, you can also dynamically render components. There are two main ways to dynamically render a component: in a template with NgComponentOutlet, or in your TypeScript code with ViewContainerRef.
- **@if**
  - The @if block conditionally displays its content when its condition expression is truthy. Content is added and removed from the DOM based on the evaluation of conditional expressions in the @if and @else blocks.
- **@else**
  - While the @if block can be helpful in many situations, it's common to also show fallback UI when the condition is not met. When you need a fallback, similar to JavaScript's else clause, add an @else block to accomplish the same effect.
- **@else if**
  - With the new control flow syntax, you gain @else if conditional blocks, something that is not possible with @ngIf. This addition makes the control flow syntax close to what we would write with just plain JavaScript.
- **@for**
  - The @for block is a built-in control flow syntax used to render a list of items within a template. It allows you to iterate over collections by specifying a tracking expression that helps the framework efficiently update the DOM when the data changes.
- **@switch**
  - The @switch blocks displays content selected by one of the cases matching against the conditional expression. The value of the conditional expression is compared to the case expression using the === operator.
- **@case**
  - The @case block is a control flow directive used within template expressions to match a specific value against an expression defined in a preceding @switch statement. When the value associated with a @case matches the switch expression, the content inside that block renders to the DOM.
- **@default**
  - The @default clause is used to render a template when none of the @case blocks matches the value of the @switch conditional. @default is optional and can be omitted.
- **@let**
  - The @let declaration is a template syntax feature that allows you to define local variables directly within an Angular template. It enables you to assign values to a variable name that can be reused throughout a specific section of the markup, which helps simplify complex expressions and improves code readability.

### 1.8 Pipes
- **Event Binding**
  - Event binding lets you listen for and respond to user actions such as keystrokes, mouse movements, clicks, and touches.
- **Two-way Binding**
  - Two-way binding gives components in your application a way to share data. Use two-way binding to listen for events and update values simultaneously between parent and child components.
- **Control Flow**
  - Control flow is a syntax mechanism that allows developers to define conditional logic and list rendering directly within HTML templates. It provides built-in directives like @if, @else, and @for to manage the dynamic appearance of elements based on component state.
- **Change Detection**
  - Change detection is the process through which Angular checks to see whether your application state has changed, and if any DOM needs to be updated. At a high level, Angular walks your components from top to bottom, looking for changes.
- **Common Pipes**
  - Common pipes are built-in transformation tools that allow you to format data directly within your templates for display. They handle tasks such as converting dates into readable strings, changing text to uppercase or lowercase, formatting numbers as currency, and transforming objects into JSON strings.
- **Pipes Precedence**
  - Pipes precedence refers to the specific order in which multiple pipes are executed when chained together in a template expression. When you apply several pipes to a single data value, Angular processes them from left to right, passing the output of the first pipe as the input to the next.
- **Custom Pipes**
  - Pipes to transform strings, currency amounts, dates, and other data for display. Pipes are simple functions in template expressions to accept an input value and return a transformed value.

---

## 2. Intermediate

### 2.1 Directives
- **Custom Directives**
  - Custom Directives are user-defined classes that allow you to extend the functionality of HTML elements by attaching custom behavior or transforming the appearance of the Document Object Model. They serve as a mechanism to create reusable components that can manipulate DOM nodes, listen for events, or apply specific styling logic across various parts of an application.
- **Configuration**
  - The configuration of routes in an Angular application involves defining route mappings in an array and providing these routes to the Angular router.

### 2.2 Routing
- **Lazy Loading**
  - Lazy loading is a technique in Angular that allows you to load JavaScript components asynchronously when a specific route is activated. It improves the application load time speed by splitting the application into several bundles.
- **Router Outlets**
  - A router outlet is a placeholder component that marks the specific area on a page where the Angular router displays the content associated with the current URL. It acts as a dynamic container that switches its displayed view based on navigation events triggered by the user.
- **Router Links**
  - In Angular, routerLink when applied to an element in a template, makes that element a link that initiates navigation to a route. Navigation opens one or more routed components in one or more <router-outlet> locations on the page.
- **Router Events**
  - The Angular Router raises events when it navigates from one route to another route. It raises several events such as NavigationStart, NavigationEnd, NavigationCancel, NavigationError, ResolveStart, etc.

### 2.3 Services  & Remote Data
- **@Input & @Output**
  - @Input() and @Output() give a child component a way to communicate with its parent component. @Input() lets a parent component update data in the child component.
- **Template Ref Vars**
  - Template reference variables help you use data from one part of a template in another part of the template. A template variable can refer to a DOM element within a template, component or directive.
- **@defer**
  - The @defer block is a mechanism that allows you to delay the loading of specific parts of your template until a defined condition is met. It works by postponing the initialization of components, directives, and pipes within the block to reduce the initial bundle size and improve the application's startup performance.
- **Dependency Injection**
  - Dependency Injection is one of the fundamental concepts in Angular. DI is wired into the Angular framework and allows classes with Angular decorators, such as Components, Directives, Pipes, and Injectables, to configure dependencies that they need.

### 2.4 Forms
- **Reactive Forms**
  - Reactive Forms provide a model-driven approach to handling form inputs whose values change over time. This system uses explicit, immutable data structures to manage the state of a form, allowing you to track changes, validate inputs, and handle submissions programmatically within your component classes.
- **Typed Forms**
  - Since Angular 14, reactive forms are strictly typed by default. You don't have to define extra custom types or add a ton of type annotations to your form declarations to benefit from this extra type safety, as Angular will infer types from the default value of a form control.
- **Template-driven Forms**
  - Template-driven forms use directives within the HTML template to manage form data and validation. They rely on the ngModel directive to create and bind a control to a data model automatically.
- **Dynamic Forms**
  - Dynamic forms in Angular are a flexible way to create forms where the structure (such as form fields and validation rules) is generated at runtime, rather than being hardcoded. By using Angular's FormBuilder and FormGroup, you can dynamically add, remove, or modify form controls based on user input, data fetched from a server, or other logic.
- **Custom Validators**
  - Custom validators in Angular are functions that allow you to define your own validation logic for form controls. They are used when the built-in validators (like required, minLength, etc.) do not meet your specific validation requirements.
- **Control Value Accessor**
  - Defines an interface that acts as a bridge between the Angular forms API and a native element in the DOM. Implement this interface to create a custom form control directive that integrates with Angular forms.

### 2.5 HTTP Client
- **Setting Up the Client**
  - Before you can use HttpClient in your app, you must configure it using dependency injection. HttpClient is provided using the provideHttpClient helper function, which most apps include in the application providers in app.config.ts.
- **Making Requests**
  - HttpClient has methods corresponding to the different HTTP verbs used to make requests, both to load data and to apply mutations on the server. Each method returns an RxJS Observable which, when subscribed, sends the request and then emits the results when the server responds.

### 2.6 RxJS Basics
- **Guards**
  - Guards are interfaces that tell the router whether it should allow a user to navigate to or away from a requested route. They function by executing a piece of logic that returns a boolean, a promise, or an observable to determine if the navigation process proceeds or is blocked.
- **Observable Pattern**
  - The observable pattern is a software design pattern where an object, known as the subject, maintains a list of dependents called observers and notifies them automatically of any state changes. In this model, the observable acts as a data source that pushes values over time to one or more subscribers.

### 2.7 Signals
- **Observable Lifecycle**
  - An Observable lifecycle defines the stages a stream goes through from its initial creation to its eventual termination. It begins when an observer subscribes to the stream, triggering the execution of the producer function.
- **RxJS vs Promises**
  - RxJS Observables and JavaScript Promises are both patterns used to handle asynchronous operations, but they differ significantly in their capabilities and execution models. A Promise is designed to handle a single asynchronous event that eventually resolves to a value or rejects with an error, making it a one-time operation that cannot be cancelled once initiated.
- **Operators**
  - RxJS operators are crucial functions that enable the declarative composition of complex asynchronous code. There are two primary types: Pipeable Operators, such as filter() or mergeMap(), which are chained using the observableInstance.pipe() method to transform an existing Observable into a new one without altering the original; and Creation Operators, like of() or interval(), which are standalone functions used to generate new Observables from scratch.
- **Filtering**
  - RxJS provides a variety of filtering operators that you can use to filter and transform the data in a stream. You can use these operators in combination with other RxJS operators to create powerful and efficient data processing pipelines.
- **Rate Limiting**
  - Rate limiting operators control the frequency of event emissions within an observable stream by managing how often values are passed through. These operators allow developers to handle high-frequency events, such as keystrokes or scroll movements, by filtering out rapid-fire inputs based on time intervals or specific conditions.
- **Transformation**
  - Transformation operators are functions that take the data emitted by an observable, change its form or content, and then output the modified values to the next part of the stream. These tools allow you to map, project, or group incoming data into new formats before it reaches your components or services.
- **RxJS Interop**
  - Angular's @angular/core/rxjs-interop package provides useful utilities to integrate Angular Signals with RxJS Observables. Use a toSignal function to create a signal that tracks the value of an Observable.

### 2.8 State Management
- **Writing Interceptors**
  - Interceptors are middleware that allows common patterns around retrying, caching, logging, and authentication to be abstracted away from individual requests.
- **NGXS**
  - Ngxs is a state management pattern for the Angular framework. It acts as a single source of truth for our application.

### 2.9 Zones
- **Zoneless Applications**
  - Angular 18 introduced an experimental feature called zoneless change detection. This technology removes the need for Zone.js, a library that was previously used for change detection in Angular from the beginning.

### 2.10 Developer Tools
- **Angular CLI**
  - The Angular CLI is a command-line interface tool that you use to initialize, develop, scaffold, and maintain Angular applications directly from a command shell. we can install angular latest CLI using the following command:
- **Local Setup**
  - To install Angular CLI on your local system, you need to install Node.js. Angular requires an active LTS or maintenance LTS version of Node.
- **Deployment**
  - The Angular CLI command ng deploy executes the deploy CLI builder associated with your project. A number of third-party builders implement deployment capabilities to different platforms.
- **End-to-End Testing**
  - End-to-end or (E2E) testing is a form of testing used to assert your entire application works as expected from start to finish or "end-to-end". E2E testing differs from unit testing in that it is completely decoupled from the underlying implementation details of your code.
- **DevTools**
  - Angular DevTools is a browser extension that provides debugging and profiling capabilities for Angular applications. You can view component trees and change detection cycles.

---

## 3. Advanced

### 3.1 SSR
- **Inputs as Signals**
  - Signal inputs allow values to be bound from parent components. Those values are exposed using a Signal and can change during the lifecycle of your component.
- **Queries as Signals**
  - A component or directive can define queries that find child elements and read values from their injectors. Developers most commonly use queries to retrieve references to components, directives, DOM elements, and more.
- **Model Inputs**
  - Model inputs are a special type of input that enable a component to propagate new values back to another component. Use model inputs in components that exist to modify a value based on user interaction.
- **NgRx**
  - NgRx is a framework for building reactive applications in Angular. NgRx simplifies managing application state by enforcing unidirectional data flow and providing tools like NgRx Store, NgRx Effects, NgRx Router Store, NgRx Signals, NgRx Entity, and NgRx Operators.

### 3.2 SSG
- **Language Service**
  - The Angular Language Service provides code editors with a way to get completions, errors, hints, and navigation inside Angular templates (external and in-line). Anytime you open an Angular application for the first time, an installation prompt will occur.
- **Libraries**
  - Use the Angular CLI and the npm package manager to build and publish your library as an npm package.
- **AnalogJS**
  - AnalogJS is a full-stack meta-framework powered by Vite and Nitro for Angular. Analog supports both Server-Side Rendering (SSR) and Static Site Generation (SSG).

### 3.3 Security
- **Schematics**
  - A schematic is a template-based code generator that supports complex logic. It is a set of instructions for transforming a software project by generating or modifying code.
- **Build Environments**
  - You can define different named build configurations for your project, such as development and production, with different defaults. Each named configuration can have defaults for any of the options that apply to the various builder targets, such as build, serve, and test.
- **CLI Builders**
  - A number of Angular CLI commands run a complex process on your code, such as building, testing, or serving your application. The commands use an internal tool called Architect to run CLI builders, which invoke another tool (bundler, test runner, server) to accomplish the desired task.
- **AoT Compilation**
  - Angular applications require a compilation process before they can run in a browser. The Angular ahead-of-time (AOT) compiler converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.
- **Using Libraries**
  - Libraries are collections of pre-written code, functions, or modules that developers integrate into their projects to perform specific tasks without having to build the functionality from scratch. These resources provide reusable components, utilities, or services that help streamline the development process and maintain consistent project standards.
- **Creating Libraries**
  - If you have developed features that are suitable for reuse, you can create your own libraries. These libraries can be used locally in your workspace, or you can publish them as npm packages to share with other projects or other Angular developers.
- **Cross-site Scripting**
  - Cross-site scripting (XSS) enables attackers to inject malicious code into web pages. Such code can then, for example, steal user and login data, or perform actions that impersonate the user.
- **Sanitization**
  - Sanitization is the process of inspecting and cleaning untrusted data to prevent malicious code from being executed in a web browser. It ensures that values injected into the DOM are stripped of dangerous elements, such as <script> tags or inline event handlers, while preserving safe content.
- **Trusting Safe Values**
  - Sometimes applications genuinely need to include executable code, display an <iframe> from some URL, or construct potentially dangerous URLs. To prevent automatic sanitization in these situations, tell Angular that you inspected a value, checked how it was created, and made sure it is secure.
- **Enforce Trusted Types**
  - It is recommended that you use Trusted Types as a way to help secure your applications from cross-site scripting attacks. Trusted Types is a web platform feature that can help you prevent cross-site scripting attacks by enforcing safer coding practices.
- **HTTP Vulnerabilities**
  - Angular has built-in support to help prevent two common HTTP vulnerabilities, cross-site request forgery (CSRF or XSRF) and cross-site script inclusion (XSSI). Both of these must be mitigated primarily on the server side, but Angular provides helpers to make integration on the client side easier.
- **Cross-site Request Forgery**
  - Cross-site Request Forgery is a security vulnerability that tricks a user's web browser into performing unwanted actions on a different website where the user is currently authenticated. An attacker uses this flaw to execute unauthorized commands by leveraging the browser’s automatic inclusion of session cookies with every request sent to a specific domain.

### 3.4 Accessibility
- **Combination**
  - RxJS combination operators merge multiple observables into a single one using various strategies. Key operators include: Merge (emits items from all sources as they arrive), Concat (emits items from sources sequentially, one after another), Zip (pairs emissions from sources based on index), CombineLatest (emits based on the latest values from all sources whenever any source emits), WithLatestFrom (combines the value of one observable with the latest values of others when the first observable emits), and ForkJoin (emits the last value from each source only after all sources complete).
- **Attributes**
  - Building accessible web experience often involves setting Accessible Rich Internet Applications (ARIA) attributes to provide semantic meaning where it might otherwise be missing. Use attribute binding template syntax to control the values of accessibility-related attributes.
- **UI Components**
  - The Angular Material library, which is maintained by the Angular team, is a suite of reusable UI components that aims to be fully accessible. The Component Development Kit (CDK) includes the a11y package that provides tools to support various areas of accessibility.
- **Containers**
  - Some Angular Material UI components cannot take children, such as an input, so you need to use container elements to customize the UI component.
- **Routing**
  - Tracking and controlling focus in a UI is an important consideration in designing for accessibility. When using Angular routing, you should decide where page focus goes upon navigation.
- **Link Identification**
  - CSS classes applied to active RouterLink elements, such as RouterLinkActive, provide a visual cue to identify the active link. Unfortunately, a visual cue doesn't help blind or visually impaired users.

### 3.5 Performance
- **HttpClient CSRF**
  - HttpClient CSRF protection is a built-in mechanism that helps prevent Cross-Site Request Forgery attacks by validating requests against a security token. When this feature is enabled, the framework automatically reads a token from a cookie and sets it as an HTTP header for subsequent requests.
- **XSRF protection**
  - Cross-Site Request Forgery (XSRF or CSRF) protection is a critical security measure designed to prevent a type of malicious exploit where an attacker tricks a web browser into sending an unauthorized request to a trusted site on behalf of a logged-in user. Unlike phishing, which tries to steal credentials, XSRF exploits a user's active session.
- **Cross-site Script Inclusion**
  - Cross-site script inclusion, also known as JSON vulnerability, can allow an attacker's website to read data from a JSON API. The attack works on older browsers by overriding built-in JavaScript object constructors, and then including an API URL using a <script> tag.
- **Deferrable Views**
  - Deferrable views can be used in component template to defer the loading of select dependencies within that template. Those dependencies include components, directives, and pipes, and any associated CSS.
- **Image Optimization**
  - The NgOptimizedImage directive makes it easy to adopt performance best practices for loading images.
- **Zone Pollution**
  - Zone.js is a signaling mechanism that Angular uses to detect when an application state might have changed. In some cases, scheduled tasks or microtasks don’t make any changes in the data model, which makes running change detection unnecessary.
- **Slow Computations**
  - On every change detection cycle, Angular synchronously evaluates all template expressions in components based on their detection strategy and executes the ngDoCheck, ngAfterContentChecked, ngAfterViewChecked, and ngOnChanges lifecycle hooks. To remove slow computations, you can optimize algorithms, cache data with pure pipes or memoization, and limit lifecycle hook usage.
- **Testing Services**
  - To ensure your services function as expected, you can write dedicated tests for them. Services are typically the easiest files to unit test.

### 3.6 Testing
- **Hydration**
  - Hydration is the process that restores the server-side rendered application on the client. This includes things like reusing the server rendered DOM structures, persisting the application state, transferring application data that was retrieved already by the server, and other processes.
- **Testing Pipes**
  - An Angular Pipe is a special function that is called from a Component template. Its purpose is to transform a value: You pass a value to the Pipe, the Pipe computes a new value and returns it.
- **Testing Requests**
  - As for any external dependency, you must mock the HTTP backend so your tests can simulate interaction with a remote server. The @angular/common/http/testing library provides tools to capture requests made by the application, make assertions about them, and mock the responses to emulate your backend's behavior.
- **Services with Dependencies**
  - When you add a dependency to your service, you must also include it in your tests. For isolated tests, pass an instance of the injectable dependency class into the service’s constructor.
- **Component Bindings**
  - Angular processes all data bindings once for each JavaScript event cycle, from the root of the application component tree through all child components. Data binding plays an important role in communication between a template and its component, and is also important for communication between parent and child components.
- **Testing Directives**
  - Directives are classes that add new behavior or modify the existing behavior to the elements in the template. Basically directives are used to manipulate the DOM, for example adding/removing the element from DOM or changing the appearance of the DOM elements.
- **Debugging Tests**
  - If your tests aren't working as you expect them to, you can inspect and debug them in the browser. Be sure to set breakpoints to track your application's execution.
- **Component Templates**
  - With a component template , you can save and reuse component processes and properties and create components from them; template-based components inherit the template's properties and process.

### 3.7 Internationalization
- **Localize Package**
  - To take advantage of the localization features of Angular, use the Angular CLI to add the @angular/localize package to your project. If @angular/localize is not installed and you try to build a localized version of your project (for example, while using the i18n attributes in templates), the Angular CLI will generate an error, which would contain the steps that you can take to enable i18n for your project.
- **Locales by ID**
  - Angular uses the Unicode locale identifier (Unicode locale ID) to find the correct locale data for internationalization of text strings. A locale ID specifies the language, country, and an optional code for further variants or subdivisions.
- **Translation Files**
  - After you prepare a component for translation, use the extract-i18n Angular CLI command to extract the marked text in the component into a source language file. The marked text includes text marked with i18n, attributes marked with i18n\-attribute, and text tagged with $localize.
- **Multiple Locales**
  - Multiple locales represent the configuration and management of various language and regional settings within an application to support a global user base. This approach involves defining specific locale data, such as date formats, currency symbols, and number representations, for each target region.
- **Transitions & Triggers**
  - In Angular, transition states can be defined explicitly through the state() function, or using the predefined wildcard and void states. An asterisk or wildcard matches any animation state.
- **Complex Sequences**
  - Complex sequences involve orchestrating multiple animation steps or staggered effects to occur in a specific order. This process uses the query and stagger functions to control the timing and execution of individual elements within a container.

### 3.8 Animation
- **Code Coverage**
  - The Angular CLI can run unit tests and create code coverage reports. Code coverage reports show you any parts of your code base that might not be properly tested by your unit tests.
- **Reusable Animations**
  - To create a reusable animation, use the animation() function to define an animation in a separate .ts file and declare this animation definition as a const export variable. You can then import and reuse this animation in any of your application components using the useAnimation() function.
- **Route Transitions**
  - When a user navigates from one route to another, the Angular router maps the URL path to a relevant component and displays its view. Animating this route transition can greatly enhance the user experience.

---

## 4. Optional / Specialized Topics

- Template
- Standalone
- Selector
- Metadata
- Module Architecture
- Creating Components
- Imports
- Parent-Child Interaction
- ViewChild
- ContentChild
- Attribute Binding
- @else if
- @for
- @switch
- @case
- @default
- @let
- Common Pipes
- Pipes Precedence
- Custom Pipes
- Custom Validators
- Control Value Accessor
- Rate Limiting
- Transformation
- RxJS Interop

---

## 5. References

- [Angular Roadmap](https://roadmap.sh/angular)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer

### Related Skills
- JavaScript
- React
- Vue.js
- Node.js