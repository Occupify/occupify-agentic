# TypeScript

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/typescript
- Related Roles:
  - Frontend Developer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction to TypeScript
- **TypeScript vs JavaScript**
  - TypeScript and JavaScript are both programming languages used for web development. JavaScript is a dynamic language that is interpreted at runtime by the browser, meaning that type errors are only caught when the code is executed.
- **TS and JS Interoperability**
  - TypeScript and JavaScript interoperability refers to the ability of TypeScript code to work seamlessly with existing JavaScript code and vice versa. This means you can use JavaScript libraries in your TypeScript projects and gradually migrate JavaScript code to TypeScript without rewriting everything at once.
- **Installation and Configuration**
  - The installation process of TypeScript generally includes installing the TypeScript compiler, which translates TypeScript code into JavaScript, and configuring your project with a tsconfig.json file to manage compiler options and project settings. This setup enables you to write, compile, and run TypeScript code effectively.
- **Running TypeScript**
  - Running TypeScript involves converting your .ts files into JavaScript files that can be executed by a JavaScript runtime environment, such as a web browser or Node.js. This conversion, known as compilation or transpilation, is performed by the TypeScript compiler (tsc).
- **tsc**
  - tsc is the command-line compiler for TypeScript. It takes TypeScript code as input and transforms it into JavaScript code that can be executed by browsers or other JavaScript runtimes like Node.js.
- **ts-node**
  - ts-node is a package that lets you directly run TypeScript code without needing to pre-compile it into JavaScript. It does this by providing a TypeScript execution environment for Node.js, allowing you to execute .ts files directly from the command line or by using it as a Node.js module.
- **TS Playground**
  - The TS Playground is an online, interactive environment that allows you to write, compile, and share TypeScript code directly in your web browser. It provides immediate feedback on your code, showing compilation errors and the resulting JavaScript output in real-time.

### 1.2 TypeScript Types
- **boolean**
  - A boolean type represents a logical value that can be either true or false. It is commonly used in programming to control the flow of execution based on certain conditions, allowing programs to make decisions and execute different code blocks depending on whether a condition is met.
- **number**
  - The number type in TypeScript represents numeric values. This includes integers (whole numbers like 1, 42, -10) and floating-point numbers (numbers with decimal points like 3.14, -0.5).
- **string**
  - A string represents a sequence of characters. It's used to store and manipulate textual data, like words, sentences, or any sequence of symbols.
- **void**
  - The void type in TypeScript represents the absence of a value. It is commonly used as the return type of functions that do not return any value, essentially indicating that the function performs an action but doesn't produce a result.
- **undefined**
  - undefined is a primitive type in TypeScript that represents a variable that has been declared but has not yet been assigned a value. When a variable is initialized without a value or a function reaches the end of its execution without a return statement, it implicitly holds this value.
- **null**
  - The null type represents the intentional absence of a value. It's a primitive data type that has only one possible value: null.
- **Interface**
  - An interface in TypeScript is a way to define a contract for the shape of an object. It names a set of properties and their types that an object must have.
- **Class**
  - A class is a blueprint for creating objects (instances) that share similar characteristics. It defines the properties (data) and methods (functions) that the objects will possess.
- **Enum**
  - An "enum" (short for enumeration) is a way to define a set of named constants. It provides a way to give more friendly names to sets of numeric values, making code more readable and maintainable.
- **Array**
  - An array is a data structure that stores an ordered collection of elements, where each element is accessed using its numerical index. Arrays are fundamental for managing lists of items, and in TypeScript, you define the types of elements that an array can hold, enforcing consistency and preventing errors.
- **Tuple**
  - A tuple is a typed array with a pre-defined length and types for each index. Each position in the tuple can have its own specific type, allowing you to create arrays with a known structure where the type of element is known at each index.
- **Object**
  - In TypeScript, an object type defines the structure of a JavaScript object. It specifies the names, types, and optionality of the properties an object should have.
- **as const**
  - as const is a TypeScript feature that allows you to tell the compiler to infer the narrowest or most specific type possible for an expression. Instead of the compiler widening the type of a value to its general type (like inferring a string variable as string), as const makes the compiler infer the value as a constant type (like inferring a string variable as the specific string literal type "hello").
- **as [type]**
  - Type assertions in TypeScript are a way to tell the compiler the specific type of a variable. They allow you to override TypeScript's type inference when you know more about the type of a value than the compiler does.
- **as any**
  - The as any syntax in TypeScript is a type assertion that instructs the compiler to treat a value as the any type, effectively disabling all type checking for that specific expression. When this assertion is used, you bypass the type system, allowing you to access any properties or methods on the object regardless of its original definition.

### 1.3 Type Inference
- **tsconfig.json**
  - tsconfig.json is a configuration file that specifies how the TypeScript compiler should transpile your TypeScript code into JavaScript. It controls various compilation options such as target ECMAScript version, module system, and source maps.
- **Compiler Options**
  - Compiler options in TypeScript provide fine-grained control over how the TypeScript compiler (tsc) transforms .ts files into JavaScript. These options are typically configured within a tsconfig.json file or passed directly via the command line.

### 1.4 Type Compatibility
- **Union Types**
  - Union types allow a variable to hold values of different types. This means you can specify that a variable can be, for example, either a string or a number.
- **Intersection Types**
  - Intersection types in TypeScript allow you to combine multiple types into a single type. The resulting type has all the features (properties, methods, etc.) of all the constituent types.

---

## 2. Intermediate

### 2.1 Combining Types
- **Type Aliases**
  - Type aliases in TypeScript create a new name for an existing type. This new name can then be used anywhere you would normally use the original type.
- **keyof Operator**
  - The keyof operator in TypeScript creates a union of all the keys (property names) of a given object type. It essentially extracts the names of the properties as string literal types.

### 2.2 TypeScript Interfaces
- **unknown**
  - The unknown type in TypeScript represents a value that can be anything. Unlike any, which essentially disables type checking, unknown forces you to perform type checks or type assertions before you can perform operations on a value declared as unknown.
- **any**
  - any is a type in TypeScript that acts as a top type by opting out of type checking for a variable. When a value is assigned the any type, you can perform any operation on it, such as accessing arbitrary properties or calling it as a function, without the compiler raising errors.
- **never**
  - The never type in TypeScript represents the type of values that will never occur. This means a function that always throws an error or runs forever (infinite loop) implicitly returns never.
- **Non-null Assertion**
  - The non-null assertion operator in TypeScript is a way to tell the compiler that you are certain a value is not null or undefined, even if the TypeScript's type checker thinks it could be. It is denoted by an exclamation mark (!) placed after a variable or expression.
- **satisfies keyword**
  - The satisfies keyword in TypeScript is used to ensure that a value conforms to a specific type without explicitly declaring that type. This is particularly useful when you want to check that an object's structure matches a type definition but still allow TypeScript to infer a more specific type for the object's properties.
- **Types vs Interfaces**
  - In TypeScript, both types and interfaces are ways to define the shape of an object. They specify what properties an object should have and the data type of those properties.
- **Extending Interfaces**
  - Extending interfaces in TypeScript allows you to create new interfaces based on existing ones. This means a new interface can inherit all the properties and methods of a parent interface and add its own unique members, promoting code reuse and establishing a clear hierarchy of types.
- **Interface Declaration**
  - An interface declaration introduces a new named type into the TypeScript type system. It specifies a contract that an object (or other type) can adhere to, defining the names and types of properties and methods that implementing objects must possess.
- **Hybrid Types**
  - Hybrid types describe objects that act as both an object and a function. In essence, they possess properties and methods like a regular object, but they can also be invoked or called directly like a function.

### 2.3 Type Guards / Narrowing
- **instanceof**
  - The instanceof operator checks if an object is an instance of a specific class or constructor function. It determines if the prototype property of a constructor appears anywhere in the prototype chain of an object.
- **typeof**
  - typeof in TypeScript is a way to narrow down the type of a variable based on its JavaScript typeof operator result. This allows you to write more precise code by checking the type of a variable (like string, number, boolean, symbol, or object) and then treating it accordingly within a specific block of code.
- **Equality**
  - Equality in the context of type guards and narrowing refers to using comparison operators (like ===, !==, ==, !=) to refine the type of a variable within a TypeScript program. By comparing a variable against a specific value (or another variable), TypeScript can infer a more specific type for that variable within a certain scope, enabling safer and more accurate code execution by ruling out possibilities.
- **Truthiness**
  - Truthiness in TypeScript, as in JavaScript, refers to the concept of a value evaluating to true when encountered in a Boolean context. Certain values are inherently "truthy" while others are "falsy." TypeScript uses this understanding to refine the type of a variable based on the outcome of a truthiness check, effectively narrowing its potential types to those that are compatible with a true outcome.
- **Type Predicates**
  - Type predicates are a way to refine the type of a variable within a TypeScript function. They're used to tell the TypeScript compiler that a specific condition guarantees a variable is of a certain type.

### 2.4 TypeScript Functions
- **Typing Functions**
  - Functions in programming are reusable blocks of code that perform specific tasks. Typing functions in TypeScript means defining the types of the parameters a function accepts and the type of value it returns.
- **Function Overloading**
  - Function overloading allows you to define multiple function signatures with the same name but different parameter types or numbers of parameters. This lets you provide specific type information based on how the function is called, enhancing type safety and code clarity.
- **Partial**
  - The Partial<Type> utility type in TypeScript constructs a type where all properties of the original Type are set to optional. This means that when you use Partial<Type>, you can create objects that only include a subset of the properties defined in the original Type, or even have no properties at all.

### 2.5 Classes
- **Constructor Params**
  - In TypeScript classes, constructor parameters provide a concise way to define and initialize class properties directly within the constructor's parameter list. By using access modifiers like public, private, or protected before a constructor parameter, TypeScript automatically creates a corresponding class property with that name and assigns the constructor argument's value to it.

### 2.6 Generics
- **Access Modifiers**
  - Access modifiers in object-oriented programming control the visibility of class members (properties and methods). They determine which parts of your code, or even external code, can access and modify those members.
- **Abstract Classes**
  - An abstract class is a class that cannot be instantiated directly. Its primary purpose is to define a blueprint for other classes.
- **Generic Types**
  - Generic types allow you to write code that can work with a variety of types without sacrificing type safety. Think of them as placeholders for types that you specify later when you use the code.
- **Generic Constraints**
  - Generic constraints in TypeScript allow you to limit the types that can be used as type arguments for a generic type or function. They ensure that the type argument satisfies a specific requirement, like having certain properties or methods.

---

## 3. Advanced

### 3.1 Decorators
- **Constructor Overloading**
  - Constructor overloading allows a class to have multiple constructors with different parameter lists. This enables you to create objects of the class in different ways, providing flexibility in initialization based on the provided arguments.
- **Inheritance vs Polymorphism**
  - Inheritance is a mechanism where a class (the subclass or derived class) acquires the properties and methods of another class (the superclass or base class), establishing an "is-a" relationship. Polymorphism, meaning "many forms," allows objects of different classes to be treated as objects of a common type, enabling you to write code that can work with objects of multiple classes without knowing their specific types at compile time.
- **Method Overriding**
  - Method overriding allows a subclass to provide a specific implementation for a method that is already defined in its superclass. When a method in a subclass has the same name, same parameters, and same return type (or a more specific return type, known as covariant return type) as a method in its superclass, the subclass's method overrides the superclass's method.
- **Namespaces**
  - Namespaces in TypeScript are a way to organize code into logical groups, preventing naming collisions and improving code maintainability. They create a named container where you can define variables, functions, classes, and interfaces.
- **Ambient Modules**
  - Ambient modules in TypeScript are used to describe the shape of existing JavaScript code when you don't have the TypeScript declaration files (.d.ts) readily available. They essentially allow you to tell the TypeScript compiler about the existence and structure of a JavaScript module, so you can import and use it in your TypeScript code without getting type errors, even if the module itself wasn't written in TypeScript.

### 3.2 Utility Types
- **Pick**
  - Pick is a utility type that constructs a new type by selecting a set of properties from an existing type. You specify which properties you want to include in the new type using their keys.
- **Omit**
  - Omit is a utility type in TypeScript that constructs a new type by picking all properties from an existing type and then removing the specified properties (keys). Essentially, it creates a subset of the original type by excluding certain keys you define.
- **Readonly**
  - The Readonly utility type in TypeScript constructs a new type where all properties of the original type are set as read-only. This means that once a property is initialized, its value cannot be changed later.
- **Record**
  - The Record utility type in TypeScript is used to construct a new type where the keys are of a specific type (typically a string, number, or symbol) and the values are of another specified type. This is useful when you want to define an object structure with a predefined set of keys and a consistent type for the values associated with those keys.
- **Exclude**
  - Exclude is a utility type in TypeScript that constructs a new type by removing types from a union type. Given two types, Type and ExcludedUnion, Exclude<Type, ExcludedUnion> creates a type that includes all members of Type that are not assignable to ExcludedUnion.
- **Extract**
  - Extract allows you to create a new type by picking out specific types from a union based on a condition. Essentially, it filters a union type, keeping only those members that are assignable to a specified type.
- **NonNullable**
  - NonNullable is a utility type that removes null and undefined from a type. If you have a type that could potentially be null or undefined, applying NonNullable ensures that the resulting type will only consist of the original type's other possible values, effectively guaranteeing that null and undefined are excluded.
- **Parameters**
  - The Parameters utility type in TypeScript extracts the parameter types of a function type into a tuple. This allows you to programmatically determine the expected arguments of a function and use them in other type definitions, providing type safety and flexibility when working with function signatures.
- **ReturnType**
  - ReturnType is a utility type that extracts the return type of a function. Given a function type, ReturnType<Type> produces a new type that represents the type of value that the function returns.
- **InstanceType**
  - InstanceType is a built-in utility type that constructs a type consisting of the instance type of a constructor function. It extracts the type returned by a class constructor when it is instantiated with the new keyword.
- **Awaited**
  - Awaited is a utility type that models the process of unwrapping a Promise. It is used to determine the type that a Promise resolves to, regardless of how many layers of nested Promises are involved.

### 3.3 Advanced Types
- **Mapped Types**
  - Mapped types in TypeScript allow you to create new types based on existing ones by transforming each property. They iterate over the keys of an existing type and apply a transformation to each key and/or value, effectively mapping the original type to a new type structure.
- **Conditional Types**
  - Conditional types in TypeScript allow you to define types that depend on other types, similar to a ternary operator in JavaScript. They enable you to express type relationships that change based on whether a specific type condition is met.
- **Literal Types**
  - Literal types are a feature that allows you to specify the exact value a variable can hold. Instead of just saying a variable is a string or a number, you can specify that it can only be a particular string like "hello" or a particular number like 42.
- **Template Literal Types**
  - Template literal types in TypeScript are a way to create new string literal types by combining existing string literal types, much like template literals in JavaScript. They allow you to define string types that are composed of other string types with specific patterns or structures.

### 3.4 TypeScript Modules
- **External Modules**
  - External modules in TypeScript are files containing code that can be imported and used in other files. They help organize and structure your project by dividing code into logical units, improving maintainability and reusability.
- **Namespace Augmentation**
  - Namespace augmentation in TypeScript allows you to add new properties or methods to an existing namespace, even if that namespace is defined in a separate file or module. This feature is particularly useful for extending namespaces declared in external libraries or modules without directly modifying the original source code.
- **Global Augmentation**
  - Global augmentation in TypeScript lets you add or modify existing global types and interfaces. This is particularly useful when working with JavaScript libraries that don't have TypeScript definitions or when you want to extend existing TypeScript definitions to suit your specific project needs.

### 3.5 Ecosystem
- **Recursive Types**
  - Recursive types in TypeScript allow you to define types that refer to themselves. This is especially useful for representing data structures that have a nested or hierarchical structure, like trees or linked lists.
- **Formatting**
  - Formatting tools automatically adjust the way your code looks, making it consistent and easier to read. These tools can handle things like spacing, indentation, and line breaks.
- **Linting**
  - Linting is the process of running a program that analyzes code for potential errors, stylistic issues, and code quality problems. It helps developers identify and fix issues early in the development cycle, leading to more maintainable and consistent codebases.
- **Useful Packages**
  - TypeScript has a large ecosystem of packages that can be used to extend the language or to add functionality to your project.
- **Build Tools**
  - Task runners automatically execute commands and carry out processes behind the scenes. This helps automate your workflow by performing mundane, repetitive tasks that you would otherwise waste an egregious amount of time repeating.

---

## 4. Optional / Specialized Topics

- tsc
- ts-node
- TS Playground
- undefined
- null
- Interface
- Class
- Enum
- Array
- Tuple
- Object
- as const
- as [type]
- as any
- satisfies keyword
- Types vs Interfaces
- Extending Interfaces
- Interface Declaration
- Hybrid Types
- Type Predicates
- Ambient Modules
- Exclude
- Extract
- NonNullable
- Parameters

---

## 5. References

- [TypeScript Roadmap](https://roadmap.sh/typescript)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Backend Developer

### Related Skills
- JavaScript
- Node.js
- React