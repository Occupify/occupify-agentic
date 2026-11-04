# JavaScript

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/javascript
- Related Roles:
  - Frontend Developer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction to JavaScript
- **What is JavaScript**
  - JavaScript is a scripting language used to create dynamic behavior in web applications. It can manipulate HTML and CSS, respond to user events, communicate with servers, and update content without reloading the page.
- **History of JavaScript**
  - JavaScript was initially created by Brendan Eich of NetScape and was first announced in a press release by Netscape in 1995. It has a bizarre history of naming; initially, it was named Mocha by the creator, which was later renamed LiveScript.
- **JavaScript Versions**
  - JavaScript, invented by Brendan Eich, achieved the status of an ECMA standard in 1997 and adopted the official name ECMAScript. This language has evolved through several versions, namely ES1, ES2, ES3, ES5, and the transformative ES6.
- **How to run JavaScript**
  - JavaScript can be run directly in a browser's developer console, embedded in an HTML page using a <script> tag, or executed on the server with Node.js. For development, tools like VS Code with a live server extension or online environments like CodePen and JSFiddle make it easy to write and run JavaScript immediately.
- **var**
  - The var statement declares a function-scoped or globally-scoped variable, optionally initializing it to a value.
- **let**
  - let declares a block-scoped variable that can be reassigned after declaration. Unlike var, it is limited to the block, statement, or expression where it is defined.
- **const**
  - Constants are block-scoped, much like variables declared using the let keyword. The value of a constant can't be changed through reassignment (i.e.

### 1.2 All about Variables
- **Variable Declarations**
  - Variable declarations introduce a variable name into the current scope. JavaScript provides three ways to declare variables: var, let, and const.
- **Hoisting**
  - Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their containing scope before code execution. Variables declared with var are hoisted and initialized as undefined.
- **Variable Naming Rules**
  - A variable name should accurately identify your variable. When you create good variable names, your JavaScript code becomes easier to understand and easier to work with.
- **Variable Scopes**
  - Scope determines where in a program a variable is accessible. JavaScript has three main scope levels: global, function, and block.
- **Block**
  - Block scope limits a variable's visibility to the block of code enclosed in curly braces {} where it is declared. Variables declared with let and const are block-scoped.
- **Function**
  - Function scope means a variable declared inside a function is only accessible within that function. Variables declared with var are function-scoped.
- **Global**
  - Global scope refers to variables declared outside any function or block, making them accessible from anywhere in the program. In browsers, global variables become properties of the window object.
- **Object Prototype**
  - JavaScript is an object-oriented language built around a prototype model. In JavaScript, every object inherits properties from its prototype, if there are any.

### 1.3 Data Types
- **string**
  - String is a primitive type that holds a sequence of characters. String in Javascript is written within a pair of single quotation marks '', double quotation marks "", or backticks (template literals).
- **undefined**
  - undefined is the default value of a variable that has been declared but not assigned a value. It is also the return value of functions that do not explicitly return anything.
- **number**
  - The number type represents both integers and floating-point values in JavaScript. It uses the IEEE 754 double-precision format, which means all numbers are stored as floats.
- **bigint**
  - BigInt is a primitive type for representing integers of arbitrary size, beyond the safe integer limit of the number type. A BigInt is created by appending n to an integer literal or using the BigInt() function.
- **boolean**
  - A boolean is a primitive type with only two possible values: true or false. Booleans are used in conditions, comparisons, and logical operations.
- **null**
  - null is a primitive value that explicitly represents the absence of any value or object. It is typically used to indicate that a variable intentionally holds no value.
- **Symbol**
  - Symbols are a unique and immutable primitive data type in JavaScript, introduced in ECMAScript 6 (ES6). They are often used to create unique property keys for objects, ensuring no property key collisions occur.
- **Object**
  - JavaScript object is a data structure that allows us to have key-value pairs; so we can have distinct keys and each key is mapped to a value that can be of any JavaScript data type. Comparing it to a real-world object, a pen is an object with several properties such as color, design, the material it is made of, etc.
- **Prototypal Inheritance**
  - The Prototypal Inheritance is a feature in javascript used to add methods and properties in objects. It is a method by which an object can inherit the properties and methods of another object.
- **typeof operator**
  - The typeof operator returns a string indicating the type of an operand. It works with primitives and functions but has some quirks, such as returning "object" for null.

### 1.4 Type Casting
- **Type Conversion vs Coercion**
  - Type coercion is the automatic or implicit conversion of values from one data type to another (such as strings to numbers). Type conversion is similar to type coercion because they convert values from one data type to another with one key difference — type coercion is implicit.
- **Explicit Type Casting**
  - Type casting means transferring data from one data type to another by explicitly specifying the type to convert the given data to. Explicit type casting is normally done to make data compatible with other variables.
- **Implicit Type Casting**
  - Implicit type conversion happens when the compiler or runtime automatically converts data types. JavaScript is loosely typed language and most of the time operators automatically convert a value to the right type.

### 1.5 Data Structures
- **Built-in Objects**
  - JavaScript provides a set of built-in objects that are available without any imports. These include Math, Date, JSON, Array, RegExp, Promise, and others.
- **Keyed Collections**
  - Keyed collections are data structures that store values indexed by keys. In JavaScript, Map and WeakMap are keyed collections that allow any value, including objects and functions, to be used as a key.
- **Map**
  - A Map is a keyed collection that stores key-value pairs and remembers insertion order. Unlike plain objects, Map keys can be of any type, including objects and functions.
- **Weak Map**
  - A WeakMap is a collection of key-value pairs where the keys must be objects and are held weakly. If the key object is garbage collected, the entry is automatically removed from the WeakMap.
- **Set**
  - A Set is a collection of unique values with no duplicates. Values in a Set can be of any type, and the Set maintains insertion order.
- **Weak Set**
  - A WeakSet is a collection of objects held with weak references. Unlike a regular Set, it only accepts objects (not primitives), and entries are automatically removed when the object is garbage collected.
- **Indexed Collections**
  - Indexed Collections are collections that have numeric indices i.e. the collections of data that are ordered by an index value.
- **Typed Arrays**
  - Typed Arrays are array-like objects for working with raw binary data of a specific numeric type. Types include Int8Array, Uint8Array, Float32Array, and others, each representing a different size and format.
- **Arrays**
  - Arrays are ordered, indexed collections that can hold values of any type. JavaScript arrays are dynamic, meaning they can grow and shrink, and provide a rich set of built-in methods like map(), filter(), reduce(), push(), and pop().
- **Structured Data**
  - Structured data refers to data organized in a defined, parseable format. In JavaScript, JSON (JavaScript Object Notation) is the primary format for structured data exchange.
- **JSON**
  - JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).
- **for**
  - The for loop is a standard control-flow construct in many programming languages, including JavaScript. It's commonly used to iterate over given sequences or iterate a known number of times and execute a piece of code for each iteration.
- **break / continue**
  - break exits a loop or switch statement immediately, skipping any remaining iterations. continue skips the rest of the current iteration and moves to the next one.

### 1.6 Equality Comparisons
- **==**
  - The == operator compares two values for equality after performing type coercion if the types differ. For example, "5" == 5 returns true because the string is converted to a number before comparison.
- **===**
  - The === operator compares two values for equality without type coercion. Both the value and the type must match for the comparison to return true.
- **Object.is**
  - Object.is() is a method for comparing two values with stricter behavior than ===. It handles two edge cases differently: Object.is(NaN, NaN) returns true (while NaN === NaN is false), and Object.is(+0, -0) returns false (while +0 === -0 is true).
- **isLooselyEqual**
  - The abstract equality comparison (loose equality) is the algorithm behind the == operator. It defines the rules for how values of different types are coerced before comparison.
- **isStrictlyEqual**
  - The strict equality comparison is the algorithm behind the === operator. It returns false if the types differ, without any coercion.

---

## 2. Intermediate

### 2.1 Loops and Iterations
- **do...while**
  - The do...while statement creates a loop that executes a specified statement until the test condition evaluates to false. The condition is evaluated after executing the statement, resulting in the specified statement executing at least once.
- **while**
  - The while loop executes a block of code as long as a specified condition is true. The condition is evaluated before each iteration, so if it is false from the start, the body never runs.
- **for...in loop**
  - The for...in loop iterates over the enumerable properties of an object, including inherited ones. It is mainly used for iterating over object keys.
- **for...of loop**
  - The for...of statement executes a loop that operates on a sequence of values sourced from an iterable object. Iterable objects include instances of built-ins such as Array, String, TypedArray, Map, Set, NodeList (and other DOM collections), and the arguments object, generators produced by generator functions, and user-defined iterables.
- **if...else**
  - The if...else statement executes a block of code if a condition is true, and an optional else block if it is false. Additional conditions can be checked with else if.
- **Switch**
  - The switch statement evaluates an expression and executes the matching case block. It is an alternative to a long chain of if...else if statements when comparing one value against multiple options.

### 2.2 Control Flow
- **Exceptional Handling**
  - In JavaScript, all exceptions are simply objects. While the majority of exceptions are implementations of the global Error class, any old object can be thrown.
- **Conditional Statements**
  - When you write code, you often want to perform different actions for different decisions. You can use conditional statements in your code to do this.
- **throw statement**
  - The throw statement throws a user-defined exception. Execution of the current function will stop (the statements after throw won't be executed), and control will be passed to the first catch block in the call stack.
- **try/catch/finally**
  - The try block contains code that might throw an error. If an error occurs, execution jumps to the catch block, which receives the error object.
- **Error Objects**
  - JavaScript provides a set of built-in error types that extend the base Error class. These include TypeError, RangeError, SyntaxError, ReferenceError, and others.
- **Default Params**
  - Default function parameters allow named parameters to be initialized with default values if no value or undefined is passed.
- **Rest**
  - The rest parameter syntax allows a function to accept an indefinite number of arguments as an array. It is defined by prefixing the last parameter with ..., such as function sum(...numbers).

### 2.3 Expressions & Operators
- **SameValueZero**
  - SameValueZero is an equality algorithm used internally by JavaScript in methods like Array.prototype.includes() and Map key comparison. It behaves like === but treats NaN as equal to itself.
- **Assignment Operators**
  - An assignment operator assigns a value to its left operand based on the value of its right operand. The simple assignment operator is equal (=), which assigns the value of its right operand to its left operand.
- **Comparison Operators**
  - Comparison operators are the operators that compare values and return true or false. The operators include: >, <, >=, <=, ==, ===, != and !==
- **Arithmetic Operators**
  - Arithmetic operators perform mathematical operations on numbers. They include + (addition), - (subtraction), (multiplication), / (division), % (remainder), and (exponentiation).
- **Bitwise Operators**
  - Bitwise operators treat their operands as 32-bit integers and perform operations at the bit level. They include & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift), and >>> (unsigned right shift).
- **Logical Operators**
  - Logical operators combine or invert boolean expressions. The main logical operators are && (AND), || (OR), and !
- **BigInt Operators**
  - Most operators that can be used with the Number data type will also work with BigInt values (e.g. arithmetic, comparison, etc.).
- **String Operators**
  - In addition to the comparison operators, which can be used on string values, the concatenation operator (+) concatenates two string values together, returning another string that is the union of the two operand strings. The shorthand assignment operator += can also be used to concatenate strings.
- **Conditional Operators**
  - The conditional (ternary) operator is the only JavaScript operator that takes three operands: condition ? valueIfTrue : valueIfFalse.
- **Comma Operators**
  - The comma operator (,) evaluates each of its operands (from left to right) and returns the value of the last operand. This lets you create a compound expression in which multiple expressions are evaluated, with the compound expression's final value being the value of the rightmost of its member expressions.
- **Unary Operators**
  - JavaScript Unary Operators are the special operators that consider a single operand and perform all the types of operations on that single operand. These operators include unary plus, unary minus, prefix increments, postfix increments, prefix decrements, and postfix decrements.
- **SameValue**
  - SameValue is the equality algorithm used by Object.is(). It is the strictest equality comparison in JavaScript: it returns true only when two values are identical, treating NaN as equal to NaN and +0 as not equal to -0.

### 2.4 Functions
- **Function Parameters**
  - The parameter is the name given to the variable declared inside the definition of a function. There are two special kinds of syntax: default and rest parameters.
- **Arrow Functions**
  - Arrow functions are a concise syntax for writing function expressions introduced in ES6. They use => instead of the function keyword and do not have their own this, arguments, or super bindings.
- **IIFEs**
  - An IIFE (Immediately Invoked Function Expression) is a function that is defined and called at the same time. It is written as (function() { ...
- **arguments object**
  - The arguments object is an Array-like object accessible inside functions that contains the values of the arguments passed to that function, available within all non-arrow functions. You can refer to a function's arguments inside that function by using its arguments object.
- **Scope & Function Stack**
  - The function stack (call stack) is the mechanism that tracks the execution of function calls. Each time a function is called, a new frame is pushed onto the stack; when it returns, the frame is popped.
- **Built-in Functions**
  - JavaScript offers a variety of built-in functions that simplify common tasks, available globally or within specific objects without requiring explicit definition. Functions like parseInt(), setTimeout(), and Math.random() can be used directly, while objects like Array, String, and Date include built-in methods for efficient data manipulation.

### 2.5 DOM APIs
- **DOM APIs**
  - With HTML DOM, JavaScript can access and change all the elements of an HTML document such as its attributes, CSS styles, remove elements, add and create new elements on the page. Web API means application programming interface for the web.

### 2.6 Strict Mode
- **Strict Mode**
  - Strict mode is an opt-in variant of JavaScript that enforces stricter parsing and error handling. It is enabled by adding "use strict" at the top of a file or function.

### 2.7 Using (this) keyword
- **in a method**
  - Methods are properties of an object which are functions. The value of this inside a method is equal to the calling object.
- **in a function**
  - When a function is called as a method of an object, this refers to the object before the dot. For example, in user.greet(), this inside greet refers to user.
- **using it alone**
  - When this is used outside any function, it refers to the global object. In a browser, that is window.
- **in event handlers**
  - In an event handler attached to a DOM element, this refers to the element that received the event. For example, in a click handler, this is the button or element that was clicked.
- **in arrow functions**
  - Arrow functions do not have their own this binding. Instead, they inherit this from the lexical scope where they were defined.
- **Function Borrowing**
  - Function borrowing allows us to use the methods of one object on a different object without having to make a copy of that method and maintain it in two separate places. It is accomplished through the use of .call(), .apply(), or .bind(), all of which exist to explicitly set this on the method we are borrowing.
- **Explicit Binding**
  - Explicit binding is when you use the call or apply methods to explicitly set the value of this in a function. Explicit Binding can be applied using call(), apply(), and bind().

### 2.8 Asynchronous JavaScript
- **Recursion**
  - One of the most powerful and elegant concept of functions, recursion is when a function invokes itself. Such a function is called a recursive function.
- **Lexical Scoping**
  - Before one can make an intuition of closures in JavaScript, it's important to first get the hang of the term 'lexical environment'. In simple words, the lexical environment for a function f simply refers to the environment enclosing that function's definition in the source code.
- **Closures**
  - Function closures are one of the most powerful, yet most misunderstood, concepts of JavaScript that are actually really simple to understand. A closure refers to a function along with its lexical environment.
- **Event Loop**
  - The Event Loop is one of the most important aspects to understand about Node.js. Why is this so important?
- **setTimeout**
  - setTimeout() schedules a function to run after a specified delay in milliseconds. It is asynchronous: the rest of the code continues executing while the timer runs.
- **setInterval**
  - setInterval() repeatedly executes a function at a specified interval in milliseconds. It continues until clearInterval() is called with the returned ID.
- **Callbacks**
  - A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.
- **Promises**
  - Promises are a much better way to work with asynchronous code in JavaScript than the old and error-prone callback approach. They were introduced into JavaScript with ECMAScript 6.
- **Callback Hell**
  - The callback hell is when we try to write asynchronous JavaScript in a way where execution happens visually from top to bottom, creating a code that has a pyramid shape with many }) at the end.
- **async/await**
  - async/await is a special syntax to work with promises in a more comfortable fashion. We use async keyword to declare a async function that return a Promise, and the await keyword makes a function wait for a Promise.

---

## 3. Advanced

### 3.1 Working with APIs
- **Fetch**
  - The fetch() method in JavaScript is used to request to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON or XML.
- **XMLHTTPRequest**
  - XMLHttpRequest (XHR) is a built-in browser object that can be used to interact with server. XHR allows you to update data without having to reload a web page.

### 3.2 Classes
- **bind**
  - The bind() method in JavaScript allows you to create a new function with a specific context and optionally preset arguments. Unlike call() or apply(), bind() does not immediately invoke the function.

### 3.3 Iterators and Generators
- **call**
  - The call() method allows you to invoke a function with a given this value, and arguments provided individually.
- **apply**
  - The apply() method of Function instances calls this function with a given this value, and arguments provided as an array (or an array-like object).

### 3.4 Modules in JavaScript
- **CommonJS**
  - CommonJS modules are the original way to package JavaScript code for Node.js. Node.js also supports the ESModules standard used by browsers and other JavaScript run-times, but CJS is still widely used in backend Node.js applications.
- **ESM**
  - ESModules is a standard that was introduced with ES6 (2015). The idea was to standardize how JS modules work and implement these features in browsers.

### 3.5 Memory Management
- **Memory Lifecycle**
  - The memory lifecycle has three stages: allocation (memory is reserved when a value is created), use (memory is read and written during execution), and release (memory is freed when it is no longer reachable). In JavaScript, allocation happens implicitly, and release is handled by the garbage collector.
- **Garbage Collection**
  - Memory management in JavaScript is performed automatically and invisibly to us. We create primitives, objects, functions… All that takes memory.

### 3.6 Using Browser DevTools
- **Debugging Issues**
  - The browser DevTools debugger allows developers to set breakpoints, step through code, inspect variable values, and trace the call stack. The console allows logging values and evaluating expressions in the current scope.
- **Debugging Memory Leaks**
  - In JavaScript, memory leaks commonly occur within heap allocated memory, where short lived objects are attached to long lived ones and the Garbage Collector cannot safely de-allocate that memory as it is still referenced from the root set (the global object).
- **Debugging Performance**
  - Enter the dev tools and check out the Lighthouse tab. This is essentially a series of tests that analyses the currently open website on a bunch of metrics related to performance, page speed, accessibility, etc.

---

## 4. Optional / Specialized Topics

- var
- let
- const
- Block
- Function
- Global
- Object Prototype
- boolean
- null
- Symbol
- Object
- Prototypal Inheritance
- typeof operator
- Set
- Weak Set
- Indexed Collections
- Typed Arrays
- Arrays
- Structured Data
- JSON
- for
- break / continue
- isStrictlyEqual
- if...else
- Switch

---

## 5. References

- [JavaScript Roadmap](https://roadmap.sh/javascript)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Backend Developer

### Related Skills
- Node.js
- TypeScript
- React
- Angular
- Vue.js