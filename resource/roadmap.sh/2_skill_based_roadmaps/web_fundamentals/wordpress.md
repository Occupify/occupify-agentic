# WordPress

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/wordpress
- Related Roles:
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **How the Web Works?**
  - The internet functions through a network of interconnected computers that communicate using a standardized set of rules called protocols. When you type a website address into your browser, your computer sends a request to a server that hosts the website.
- **What is a CMS?**
  - A Content Management System (CMS), such as WordPress, is a software application that allows users to create, manage, and modify content on a website without needing specialized technical knowledge. It provides a user-friendly interface for tasks like writing and editing text, uploading images, and organizing website structure.
- **What is HTTP?**
  - HTTP, or Hypertext Transfer Protocol, is the foundation of data communication on the World Wide Web. It's the set of rules that govern how web browsers and web servers communicate, allowing users to request and receive resources like HTML documents, images, and other files.
- **Frontend Fundamentals**
  - Frontend fundamentals encompass the core technologies that drive the visual and interactive aspects of a website. This includes HTML for structuring content, CSS for styling and layout, and JavaScript for adding dynamic behavior.
- **HTML**
  - HTML (HyperText Markup Language) is the standard markup language for creating web pages. It provides the structure and content of a website, using elements to define headings, paragraphs, images, links, and other components that a user sees in their browser.
- **CSS**
  - CSS, or Cascading Style Sheets, is a language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and other visual aspects of a website, ensuring a consistent and appealing user experience across different devices and screen sizes.
- **JavaScript**
  - JavaScript is a programming language primarily used to add interactivity and dynamic behavior to websites. It allows developers to create engaging user experiences by manipulating the content, style, and structure of web pages in response to user actions.
- **Backend Fundamentals**
  - Backend fundamentals encompass the core logic and infrastructure that power a website or application. This includes servers, databases, and the code that handles data processing, user authentication, and other essential functions behind the scenes.
- **wordpress.com & wordpress.org**
  - WordPress offers two distinct platforms: WordPress.com and WordPress.org. WordPress.com is a hosted platform where WordPress handles the server and software, offering varying plans with different features.

### 1.2 Installation & Setup
- **Classic**
  - Classic Themes represent the traditional way of designing and structuring a WordPress website, relying heavily on PHP, HTML, CSS, and JavaScript within the theme files themselves. These themes typically involve a more direct approach to coding and customization, often requiring developers to modify template files directly to alter the site's appearance and functionality.
- **SQL**
  - SQL, or Structured Query Language, is a programming language used for managing and manipulating data held in a relational database management system (RDBMS). It allows you to create, read, update, and delete data.

### 1.3 Themes
- **Block**
  - Block themes in WordPress are a modern approach to website design, where the entire site structure, from header to footer, is built using blocks. These blocks, the same ones used to create content in the WordPress editor, offer a visual and intuitive way to customize every aspect of your site's appearance without needing to write code.
- **Hybrid**
  - Hybrid themes in WordPress combine the best aspects of traditional themes and block themes. They allow developers to use both classic PHP templates and the block editor for different parts of their website, offering flexibility in design and development.
- **Universal**
  - Universal themes were the initial iteration of themes designed specifically to leverage the power of WordPress's block editor (Gutenberg). They aimed to provide a seamless and consistent editing experience, allowing users to build entire websites using blocks, from headers and footers to page content, all within the editor interface.
- **Actions**
  - Actions in WordPress are hooks that allow you to execute custom functions at specific points in the WordPress core, plugins, and themes. They provide a way to "do" something at a particular moment during the execution of WordPress code, enabling developers to modify or extend functionality without directly altering the source code.
- **PHP**
  - PHP is a scripting language primarily used for web development. It's embedded within HTML, meaning you can weave PHP code directly into your web pages.
- **Third-Party**
  - Third-party WordPress themes are pre-designed website templates created by developers or companies other than WordPress.org. These themes offer a wide range of designs and functionalities, allowing users to quickly customize the look and feel of their WordPress website without extensive coding knowledge.

### 1.4 Plugins
- **LocalWP**
  - LocalWP is a free tool that simplifies the process of creating and managing local WordPress development environments on your computer. It allows you to quickly set up WordPress sites without needing to configure web servers, databases, or PHP manually.
- **VVV**
  - VVV (Varying Vagrant Vagrants) is an open-source development environment specifically designed for WordPress. It provides a pre-configured virtual machine that includes everything you need to develop WordPress themes, plugins, and even WordPress core itself.
- **XAMPP**
  - XAMPP is a free and open-source cross-platform web server solution stack package, consisting primarily of the Apache HTTP Server, MariaDB database, and interpreters for scripts written in the PHP and Perl programming languages. It allows you to create a local server environment on your computer, enabling you to develop and test websites and web applications before deploying them to a live server.
- **Docker**
  - Docker is a platform that uses containerization to package software with all its dependencies into standardized units for software development. This allows developers to create, deploy, and run applications in isolated environments called containers, ensuring consistency across different computing environments, from development to production.

### 1.5 File Structure
- **File Structure**
  - The WordPress file structure is the organized system of folders and files that make up a WordPress website. It includes core WordPress files, theme files, plugin files, and user-uploaded content, all working together to display your website's content and functionality.

### 1.6 Page Editors
- **Classic**
  - The Classic Editor is the original text-based editor in WordPress. It allows you to create and edit pages and posts using a visual editor similar to a word processor, or directly with HTML code.
- **Third-Party Page Builders**
  - Third-party page builders are plugins that extend WordPress's functionality by providing a visual, drag-and-drop interface for designing and creating website pages. They offer a more intuitive alternative to the standard WordPress editor, allowing users to build complex layouts and designs without needing to write code.
- **Block Editor**
  - The Block Editor, also known as Gutenberg, is the default content editor in WordPress. It allows users to create and format content using individual blocks, each representing a specific element like paragraphs, images, headings, or galleries.

### 1.7 Hooks
- **Filters**
  - Filters in WordPress allow you to modify data as it's being processed. Think of them as checkpoints in the code where you can intercept a variable, change its value, and then pass it along to continue its journey.

### 1.8 The Loop
- **The Loop**
  - The Loop in WordPress is essentially a PHP code structure that fetches and displays your website's posts. Think of it as a cycle that goes through each post in your database, one by one, and presents its content on the page.

### 1.9 Shortcodes
- **Shortcodes**
  - Shortcodes in WordPress are like shortcuts that allow you to easily add dynamic content or functionality to your posts, pages, and widgets. They are special tags enclosed in square brackets, such as [myshortcode], that WordPress recognizes and replaces with the corresponding output defined by the shortcode's associated function.

---

## 2. Intermediate

### 2.1 Custom Post Types
- **Custom Post Types**
  - Custom Post Types allow you to create different types of content beyond the standard posts and pages. Think of them as a way to organize and manage specific kinds of information on your website, like products, events, or testimonials, each with its own unique set of fields and display options.

### 2.2 Style & Script Enqueueing
- **Style & Script Enqueueing**
  - Style and script enqueueing is the proper way to add CSS stylesheets and JavaScript files to your WordPress website. Instead of directly adding code to your theme's header or footer, enqueueing uses WordPress functions to register and load these assets in a controlled and organized manner.

### 2.3 Taxonomies
- **Taxonomies**
  - Taxonomies are ways to group content. Think of them as organizational tools that help you classify and structure your website's information.

### 2.4 WordPress REST API
- **WordPress REST API**
  - The WordPress REST API is an interface that allows other applications to interact with your WordPress site by sending and receiving data in a standardized way. It uses HTTP requests (like GET, POST, PUT, DELETE) to access and manipulate WordPress content, users, media, and other data.

### 2.5 Coding Standards
- **File Structure**
  - A plugin's file structure is the way its files and folders are organized within the WordPress plugins directory. This structure determines how WordPress loads and executes the plugin's code, assets, and other resources.
- **Plugin Basics**
  - WordPress plugins are essentially bundles of code that you can upload to your WordPress site to extend its functionality. They allow you to add new features, modify existing ones, or integrate with third-party services without having to directly edit the core WordPress files.

### 2.6 Classic vs Block Themes
- **Template Hierarchy**
  - The Template Hierarchy is the system WordPress uses to determine which template file to use for displaying a specific page or post. It's essentially a roadmap that WordPress follows, checking for specific template files in your theme's folder.
- **Child Themes**
  - Child themes are sub-themes that inherit the functionality and styling of a parent theme. They allow you to modify the design and code of your WordPress site without directly altering the parent theme files.
- **Template Files**
  - Template files are the building blocks of a WordPress theme, determining how your website's content is displayed. These files, written in PHP, HTML, and CSS, control the layout and design of different pages and sections of your site, such as the homepage, single posts, and archives.
- **style.css**
  - The style.css file is the main stylesheet in a classic WordPress theme. It controls the visual appearance of your website, defining elements like colors, fonts, layout, and responsiveness.
- **functions.php**
  - The functions.php file in a Classic WordPress theme acts as a plugin, adding custom functionality and features to your website. It's a powerful tool for modifying the behavior of your theme and WordPress itself, allowing you to define custom functions, hooks, filters, and more, without directly altering the core theme files.
- **Theme Structure**
  - Block themes in WordPress are structured around blocks, which are the fundamental units for building website content and layout. The theme's structure defines how these blocks are organized and rendered, encompassing template files, template parts, and the theme's theme.json file, which controls global styles and settings.

### 2.7 Licensing & Updates
- **Styles**
  - Block theme styles in WordPress are sets of pre-defined visual settings that control the look and feel of your website. They allow you to quickly change things like colors, typography, and spacing across your entire site without needing to write any code.
- **Overrides**
  - Overrides allow you to modify the default appearance and behavior of blocks and templates without directly editing the core theme files. This ensures that your customizations are preserved during theme updates.
- **Working with Databases**
  - You can enhance the functionalities of plugins by interacting with the WordPress database to store, retrieve, update, and delete data. This allows plugins to manage custom data structures beyond the standard WordPress posts and metadata, enabling features like custom user profiles, complex product catalogs, or specialized data tracking.
- **Custom Tables**
  - Custom tables refer to database tables created and managed by a plugin, separate from the default WordPress tables (like wpposts or wpusers). These tables allow plugins to store and manage their own specific data, offering greater flexibility and control over data structures compared to relying solely on WordPress's built-in database schema.
- **External API Integrations**
  - External API integrations allow plugins to connect and interact with services and data sources outside of the WordPress environment. This involves using code to send requests to external servers, receive data in formats like JSON or XML, and then process and display that information within the WordPress plugin.
- **Custom Fields**
  - Custom fields are a way to add extra information to your WordPress posts, pages, and other content types beyond the standard title, content, and excerpt. They allow you to create specific data entry points for things like product prices, book authors, event dates, or any other unique piece of information you want to associate with your content.
- **Template Tags**
  - |# Template Tags
- **Widgets**
  - Widgets are small blocks of content that you can add to various areas of your WordPress website, typically in sidebars, footers, or other widget-ready areas defined by your theme. They allow you to easily add features and content without needing to write code, such as displaying recent posts, categories, search bars, or custom text.
- **Menus**
  - In classic WordPress themes, menus are how you organize and display navigation links on your website. They allow visitors to easily find different pages, categories, or custom links.
- **Customizer**
  - The WordPress Customizer is a built-in interface that allows users to modify various aspects of their website's theme in a live preview environment. It provides a visual way to adjust settings like site identity, colors, menus, widgets, and more, seeing the changes reflected in real-time before publishing them.
- **ACF**
  - Advanced Custom Fields (ACF) is a WordPress plugin that allows you to add custom fields to your WordPress edit screens. These custom fields can include various types of data, such as text, images, files, and more, enabling you to create more structured and dynamic content for your website without needing to write custom code.
- **Metabox**
  - A metabox is a custom input panel added to the WordPress post or page editing screen. It allows users to enter or select additional data related to the content being created, such as specific details, settings, or options that go beyond the standard title and body text.
- **Full Site Editing (FSE)**
  - Full Site Editing (FSE) is a set of features in WordPress that allows you to customize all parts of your website using blocks. This includes areas like headers, footers, and page templates, giving you complete control over the design and layout of your entire site through the block editor interface.
- **Block Patterns**
  - Block Patterns are pre-designed collections of blocks that you can quickly insert into your WordPress content. They offer a convenient way to create visually appealing layouts and sections without having to configure each block manually.
- **Template Parts**
  - Template Parts are reusable sections of a WordPress block theme that define specific areas of a website's layout, like headers, footers, or sidebars. They are built using blocks and can be easily included in multiple templates, allowing for consistent design and easier content management across a site.
- **AJAX in WordPress**
  - AJAX (Asynchronous JavaScript and XML) is a web development technique that allows web pages to update content dynamically without requiring a full page reload. This is achieved by exchanging data with a server in the background, meaning parts of a webpage can be updated independently, leading to a smoother and more responsive user experience.
- **Cron Jobs**
  - Cron jobs are scheduled tasks that your WordPress site runs automatically in the background. Think of them as a built-in task scheduler.
- **Transients API**
  - The Transients API in WordPress provides a simple way to store temporary data in the database. Think of it as a caching system for storing the results of expensive operations, like complex database queries or external API calls.
- **REST API**
  - The WordPress REST API allows plugins to interact with WordPress core and other plugins using HTTP requests. It provides a standardized way to access and manipulate WordPress data, like posts, pages, users, and settings, through endpoints.

### 2.8 Security & Hardening
- **Firewall & Malware Scanning**
  - A firewall acts as a barrier between your website and the outside world, filtering out malicious traffic and preventing unauthorized access. Malware scanning involves regularly checking your website's files and database for malicious code that could harm your site, steal data, or spread to visitors.
- **Virtual Patching**
  - Virtual patching is a security policy enforcement mechanism that addresses vulnerabilities in real-time. It involves deploying security rules to protect against known exploits, effectively shielding vulnerable systems without requiring immediate code modification.
- **Activity Logging**
  - Activity logging involves tracking and recording actions taken within a system, such as user logins, content modifications, and settings changes. This creates an audit trail that can be used for security analysis, troubleshooting, and compliance purposes.
- **User & Login Security**
  - User and login security focus on protecting user accounts and the login process from unauthorized access. This involves implementing measures like strong passwords, two-factor authentication, limiting login attempts, and regularly monitoring user activity to prevent brute-force attacks and account compromises.
- **Vulnerability Monitoring**
  - Vulnerability monitoring is the process of continuously scanning and assessing systems, applications, and networks for known weaknesses or flaws that could be exploited by attackers. This involves identifying potential security gaps, tracking new vulnerabilities as they are discovered, and prioritizing remediation efforts to minimize risk.
- **Admin Menu**
  - The Admin Menu in WordPress is the navigation panel located on the left side of the WordPress dashboard. It provides access to various administrative functions, such as managing posts, pages, media, users, settings, and plugins.
- **Settings Page**
  - A settings page in a plugin provides a user interface within the WordPress admin area where users can configure the plugin's options and customize its behavior. It allows plugin developers to expose various settings, such as API keys, display preferences, or feature toggles, in an organized and accessible way, enabling users to tailor the plugin to their specific needs.
- **Settings API**
  - The Settings API provides a standardized way for plugin developers to create and manage settings pages within the WordPress admin area. It simplifies the process of registering settings, creating sections, and adding fields, ensuring a consistent user experience across different plugins.
- **Options API**
  - The Options API provides a standardized way for plugins and themes to store, retrieve, and manage settings or configuration data in the WordPress database. It simplifies the process of creating settings pages and handling user preferences, ensuring data is stored securely and consistently.
- **Assets**
  - Assets optimization involves refining the files that make up a website, such as images, CSS, and JavaScript, to improve loading speed and overall performance. This process typically includes techniques such as compressing files to reduce their size, combining multiple files to minimize HTTP requests, and utilizing browser caching to store assets locally for faster retrieval on subsequent visits.
- **Images**
  - Image optimization involves reducing the file size of your images without significantly sacrificing their quality. This makes your website load faster, improves user experience, and can boost your search engine rankings.
- **Database Tuning**
  - Database tuning involves optimizing the performance of a database system to improve its speed, efficiency, and overall responsiveness. This process includes analyzing database queries, adjusting configuration parameters, and reorganizing data structures to minimize resource consumption and maximize throughput.
- **Caching**
  - Caching is a technique used to store copies of files or data in a temporary storage location, allowing for faster access in the future. When a user requests information, the system first checks the cache.
- **Core Web Vitals**
  - Core Web Vitals are a set of specific metrics that Google uses to evaluate user experience on a webpage. They focus on three key aspects: loading performance (Largest Contentful Paint - LCP), interactivity (First Input Delay - FID), and visual stability (Cumulative Layout Shift - CLS).
- **CDN Integration**
  - A Content Delivery Network (CDN) is a geographically distributed group of servers that work together to provide fast delivery of internet content. By caching website assets like images, videos, and scripts on these servers, which are located closer to users, a CDN reduces latency and improves website loading times.

### 2.9 User Roles
- **User Roles**
  - User roles define the capabilities and permissions granted to different users on a WordPress website. They control what actions a user can perform, such as creating posts, managing comments, or installing plugins.

### 2.10 Security Best Practices
- **PHPUnit**
  - PHPUnit is a testing framework for PHP, providing a structured way to write and run automated tests for your code. It allows developers to define specific expectations for their code's behavior and then automatically verify if those expectations are met.

### 2.11 Backups & Recovery
- **WP_DEBUG**
  - WPDEBUG is a PHP constant in WordPress that, when enabled, activates the debugging mode. This mode displays PHP errors, notices, and warnings on your website, which are normally hidden.
- **Log Files**
  - Log files are records that document events occurring within a system or application. They track activities, errors, warnings, and other relevant information, providing a chronological history of what happened.
- **Query Monitor**
  - Query Monitor is a free WordPress plugin designed for developers. It helps identify and debug performance bottlenecks by providing detailed information about database queries, PHP errors, hooks and actions, block editor blocks, enqueued scripts and stylesheets, HTTP API calls, and more.

### 2.12 Update Strategies
- **Update Strategies**
  - Updating WordPress involves keeping your core software, themes, and plugins current to ensure security, performance, and compatibility. You can manage updates directly from your WordPress dashboard by navigating to the "Updates" section.

---

## 3. Advanced

### 3.1 Performance monitoring
- **WP-CLI**
  - WP-CLI is a command-line interface for WordPress. It allows you to manage WordPress installations, update plugins and themes, publish posts, and perform many other administrative tasks without using a web browser.
- **Bedrock**
  - Bedrock is a WordPress boilerplate project designed to improve WordPress development by utilizing modern development standards. It introduces a more structured project setup, dependency management with Composer, and environment configuration, making WordPress projects more maintainable, secure, and easier to deploy.

### 3.2 Migrations
- **Managed**
  - Managed WordPress hosting is a specialized type of web hosting where the provider handles all the technical aspects of running a WordPress website. This includes tasks like security updates, backups, performance optimization, and WordPress core updates, allowing website owners to focus solely on creating content and growing their online presence without worrying about server management.
- **VPS**
  - A Virtual Private Server (VPS) provides a virtualized server environment within a larger physical server. It offers more control and resources compared to shared hosting, as each VPS operates independently with its own operating system, dedicated storage, and allocated RAM.
- **Shared**
  - Shared hosting is a type of web hosting where multiple websites reside on a single physical server. Resources like CPU, memory, and bandwidth are shared among all the websites hosted on that server.

### 3.3 Workflows & Automation
- **Sage**
  - Sage is a WordPress starter theme that offers a modern development workflow. It utilizes tools like Composer, Webpack, and Blade templating to streamline the process of building custom WordPress themes.
- **Composer**
  - Composer is a tool for managing dependencies in PHP projects, including WordPress. It lets you declare the libraries your project needs, and it will install them for you.

### 3.4 Automated Deployments
- **Contribute to WordPress**
  - To elevate your WordPress career, consider contributing directly to the WordPress project. This can involve submitting code to WordPress Core, improving documentation, or helping with translations.
- **Boost your WordPress Career**
  - Want to level up your WordPress career? It's all about exploring different paths, showcasing your skills, and staying in the loop.
- **WordPress Credit Program**
  - The WordPress Credit Program recognizes and rewards individuals who contribute to the WordPress open-source project. By participating in various activities like coding, testing, documentation, translation, and community support, contributors earn credits that are displayed on their WordPress.org profiles.

### 3.5 Accessibility
- **Accessibility**
  - Accessibility refers to designing and developing websites that are usable by people of all abilities, including those with disabilities. This involves ensuring that content is perceivable, operable, understandable, and robust for users who may rely on assistive technologies like screen readers, keyboard navigation, or alternative input devices.

### 3.6 Advanced PHP & Architecture
- **OOP in PHP**
  - Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to structure software design. These objects combine data (properties) and code (methods) that operate on that data.
- **Composer & Autoloading**
  - Composer is a dependency management tool for PHP, allowing you to declare the libraries your project depends on, and it will manage (install/update) them for you. Autoloading is a mechanism that automatically loads PHP class files when the classes are first used in your code, eliminating the need to manually require or include them.
- **Design Patterns**
  - Design patterns are reusable solutions to commonly occurring problems in software design. They represent best practices developed over time by experienced developers.

### 3.7 Localization
- **Localization**
  - Localization is the process of adapting a product or content to a specific target market. This involves translating text, but also modifying other elements like images, dates, and currencies to suit the cultural and technical requirements of the locale.

### 3.8 Multisite
- **Multisite**
  - WordPress Multisite is a feature that allows you to create and manage a network of multiple websites from a single WordPress installation. Instead of installing WordPress separately for each website, you can use Multisite to share core files and plugins, simplifying administration and updates across all sites in the network.

### 3.9 Headless WordPress
- **Headless WordPress**
  - Headless WordPress decouples the content management system from the presentation layer (the front-end). This means WordPress is used solely for creating, storing, and managing content, while a separate technology like React, Vue.js, or Angular is used to build and display the website to visitors.

### 3.10 Basics of SEO
- **Basics of SEO**
  - Search Engine Optimization (SEO) is the practice of improving your website to increase its visibility when people search for products or services related to your business in search engines like Google. The better visibility your pages have in search results, the more likely you are to garner attention and attract prospective and existing customers to your website.

---

## 4. Optional / Specialized Topics

- HTML
- CSS
- JavaScript
- Backend Fundamentals
- wordpress.com & wordpress.org
- PHP
- Third-Party
- functions.php
- Theme Structure
- External API Integrations
- Custom Fields
- Template Tags
- Widgets
- Menus
- Customizer
- ACF
- Metabox
- Full Site Editing (FSE)
- Block Patterns
- Template Parts
- AJAX in WordPress
- Cron Jobs
- Transients API
- REST API
- Vulnerability Monitoring

---

## 5. References

- [WordPress Roadmap](https://roadmap.sh/wordpress)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer

### Related Skills
- JavaScript
- Php
- Css
- Html