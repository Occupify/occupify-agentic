# HTML

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/html
- Related Roles:
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What are markup languages?**
  - Markup languages are systems for annotating text in a way that makes it readable by both humans and computers. They use tags to define elements within a document, specifying how the text should be structured, formatted, and displayed.
- **Frontend Development**
  - Frontend development is the practice of creating the user interface and user experience of a website or web application. It focuses on the parts of a website that users directly interact with, such as buttons, text, images, and navigation menus.

### 1.2 How the web works
- **What is HTTP?**
  - HTTP (Hypertext Transfer Protocol) enables browser-server communication through requests and responses. Stateless protocol using methods like GET and POST.
- **DNS**
  - DNS (Domain Name System) translates human-readable domain names into IP addresses through a global, decentralized server network. Enables easy internet navigation by converting names like www.example.com to numeric addresses browsers can connect to.
- **Domain names**
  - Domain names are human-friendly web addresses (e.g., google.com) substituting numerical IP addresses. Comprise second-level ("google") and top-level (".com") domains.
- **Browsers**
  - Web browsers request and display websites by interpreting HTML, CSS, and JavaScript. Use rendering engines (Blink, Gecko) for display and JavaScript engines (V8) for code execution.
- **Hosting**
  - Web hosting stores website files on servers, making sites accessible online. Types include shared (multiple sites per server) and dedicated (exclusive server) hosting.
- **What is SEO?**
  - Search Engine Optimization, or SEO, is the practice of improving your website to increase its visibility when people search for products or services related to your business in search engines like Google. The better visibility your pages have in search results, the more likely you are to garner attention and attract prospective and existing customers to your business.
- **Tags and Attributes**
  - Tags and attributes are fundamental building blocks of HTML. Tags define the structure and content of a webpage, such as headings, paragraphs, and images.
- **Case Insensitivity**
  - HTML isn't picky about capitalization. You can write tags and attributes using uppercase, lowercase, or a mix of both.
- **HTML**
  - HTML (HyperText Markup Language) is the standard markup language for creating web pages. It provides the structure of a webpage, defining elements like headings, paragraphs, images, and links using tags.
- **CSS**
  - CSS, or Cascading Style Sheets, is a language used to describe the look and formatting of a document written in HTML. It controls things like the layout, colors, fonts, and overall visual presentation of web pages, ensuring a consistent and appealing user experience across different devices and screen sizes.
- **JavaScript**
  - JavaScript is a programming language primarily used to create interactive and dynamic effects within web browsers. It allows developers to implement complex features on web pages, updating content dynamically, controlling multimedia, animating images, and much more, enhancing the user experience beyond static HTML and CSS.

### 1.3 Basic Tags
- **HTML Comments**
  - Comments in HTML are notes that you can add to your code to explain what's going on, make reminders, or temporarily disable parts of your code. These comments are not displayed in the browser, so they're only visible when someone views the source code.
- **Whitespaces**
  - Whitespaces in HTML refer to the spaces, tabs, and line breaks that are used to format the code. Browsers typically collapse multiple consecutive whitespaces into a single space when rendering the content.
- **!DOCTYPE**
  - The <!DOCTYPE> declaration is an instruction to the web browser about the HTML version used to write the page. It's placed at the very top of an HTML document, before the <html> tag, and ensures that the browser renders the page in "standards mode," following the correct specifications for that HTML version.
- **html**
  - The <html> element is the root element of an HTML page. It tells the browser that this is an HTML document.
- **head**
  - The <head> element in HTML acts as a container for metadata (data about data) about the HTML document. This metadata isn't displayed on the page itself, but it provides information like the document's title, character set, linked stylesheets, scripts, and other important configurations that help browsers and search engines understand and process the HTML document correctly.
- **title**
  - The <title> tag in HTML defines the title of the HTML document. This title is displayed in the browser's title bar or tab, and it's also used for bookmarking pages and in search engine results.
- **HTML Entities**
  - HTML entities are special codes used to represent reserved characters or characters that are difficult to type directly in HTML. They allow you to display characters like angle brackets (< and >), ampersands (&), and copyright symbols (©) that have special meanings in HTML or are not readily available on a standard keyboard.

### 1.4 Textual Tags
- **h1 to h6**
  - Headings are used to define the titles and subtitles within a document. HTML provides six levels of headings, from <h1> (the most important and largest) to <h6> (the least important and smallest).
- **b / strong**
  - The <b> and <strong> tags in HTML are used to make text appear bold. While both achieve a similar visual effect, the <b> tag is primarily for stylistic purposes, indicating text that should be visually distinguished without necessarily conveying importance.
- **i / em**
  - The <i> and <em> tags in HTML are used to emphasize text. The <i> tag represents text that is set off from the normal prose, such as technical terms, foreign words, or thoughts.
- **mark**
  - The <mark> tag in HTML is used to highlight specific parts of text within a larger block of content. It's primarily intended to draw the reader's attention to these sections, often because they are relevant to the user's current activity or search query.
- **hr**
  - The <hr> tag in HTML creates a thematic break in an HTML page and is most often displayed as a horizontal rule. It's used to separate content visually, like dividing sections of text or indicating a change in topic.
- **sub**
  - The <sub> tag in HTML is used to display text as subscript. Subscript text appears slightly below the normal line of text and is typically rendered in a smaller font size.
- **br**
  - The <br> tag in HTML creates a line break within a text block. It's used to start a new line without creating a new paragraph, effectively forcing the text that follows to appear on the next line.
- **sup**
  - The <sup> tag in HTML is used to display text as superscript. Superscript text appears slightly above the normal line of text and is typically rendered in a smaller font size.
- **pre**
  - The <pre> tag in HTML represents preformatted text. Text inside a <pre> element is displayed in a fixed-width font, and it preserves both spaces and line breaks.
- **Links**
  - Links, also known as hyperlinks, are elements that connect one web resource to another. They allow users to navigate between different pages on the same website or to external websites.
- **id**
  - The id attribute in HTML provides a unique identifier for an element within a document. This identifier allows you to target and manipulate that specific element using CSS styles, JavaScript code, or even link directly to it using fragment identifiers in URLs (e.g., #section1).

---

## 2. Intermediate

### 2.1 Grouping text
- **body**
  - The <body> tag in HTML defines the main content of an HTML document. It contains all the visible elements of a webpage, such as text, images, links, tables, lists, and more.
- **meta**
  - Meta tags are HTML elements that provide metadata about a webpage. This data is not displayed on the page itself but is used by browsers, search engines, and other web services to understand the content and purpose of the page.
- **div**
  - The <div> element is a generic container for flow content, which in simpler terms means it's a way to group together other HTML elements. It doesn't inherently represent anything specific on its own, but it's commonly used to structure and style sections of a webpage.
- **span**
  - The <span> element is an inline container used to mark up a part of a text, or a part of a document. It is used to group elements for styling purposes or because they share attributes such as lang or dir.

### 2.2 Standard attributes
- **style**
  - The style attribute in HTML allows you to apply CSS (Cascading Style Sheets) directly to individual HTML elements. It's used to define inline styles, overriding external stylesheets or default browser styles.
- **class**
  - The class attribute in HTML is used to specify one or more class names for an HTML element. These class names can then be used by CSS and JavaScript to style and manipulate specific elements or groups of elements that share the same class.
- **Data Attributes**
  - Data attributes are special attributes in HTML that allow you to store extra information directly within HTML elements. These attributes start with data- followed by a name of your choosing.

### 2.3 Lists and Types
- **Ordered lists**
  - Ordered lists in HTML are used to display a series of items in a specific order. Each item in the list is typically numbered, allowing readers to easily follow a sequence or ranking.
- **Definition lists**
  - Definition lists in HTML are used to present terms and their corresponding definitions. They are structured using three main elements: <dl> (definition list), <dt> (definition term), and <dd> (definition description).
- **Unordered lists**
  - Unordered lists present items in a bulleted format, where the order of the items is not significant. They are used to group related content together without implying any specific sequence or priority.
- **Nested lists**
  - Nested lists in HTML allow you to create lists within lists, forming a hierarchical structure. This is achieved by placing one list (either ordered <ol> or unordered <ul>) inside a list item <li> of another list.

### 2.4 Table Tag
- **img vs figure**
  - The <img> tag in HTML is used to embed a simple image directly into a webpage. It requires a src attribute to specify the image source.
- **Priority Hints**
  - Priority Hints in HTML allow developers to indicate the relative priority of fetching resources like images. This helps the browser decide which images to load first, potentially improving page load times and user experience by prioritizing content that is immediately visible or more important to the user.

### 2.5 Embedding Media
- **Images**
  - Images are a way to display visual content on a webpage. They are added to HTML documents using the <img> tag, which links to an image file.
- **Video**
  - The <video> element in HTML is used to embed video content directly into a webpage. It allows you to display video files, control playback, and provide options for users to interact with the video, such as pausing, playing, adjusting volume, and viewing in fullscreen.
- **Audio**
  - Audio on the web involves incorporating sound files into HTML documents. This allows users to listen to music, podcasts, or other audio content directly within a webpage.
- **iframe**
  - An iframe (Inline Frame) is an HTML element that allows you to embed another HTML document within the current HTML page. It essentially creates a window within your webpage where you can display content from a different source, such as another website, a video, or even another HTML file on your own server.
- **CSP**
  - Content Security Policy (CSP) is a security standard introduced to prevent cross-site scripting (XSS), clickjacking, and other code injection attacks. It works by allowing you to define a whitelist of sources that the browser is permitted to load resources from.

### 2.6 Using Forms
- **del**
  - The <del> element in HTML represents text that has been deleted or removed from a document. Browsers typically render deleted text with a strikethrough, visually indicating that the content is no longer valid or accurate.
- **ins**
  - The <ins> element in HTML represents text that has been inserted into a document. It's used to indicate additions or updates to content, often displayed with an underline to visually distinguish it from the original text.
- **Labels and Inputs**
  - Labels and inputs are fundamental building blocks for creating forms in HTML. Labels provide descriptive text that tells users what information is expected in a corresponding input field.
- **Form Validation**
  - Form validation is the process of checking if the information a user provides in a form is correct and complete before it's submitted. This ensures that the data received is accurate and meets the required format, preventing errors and improving data quality.
- **Limitations**
  - HTML form constraints are rules you set on form fields to control what kind of data users can enter. These constraints help ensure that the information submitted is valid and meets your requirements.
- **File Uploads**
  - File uploads allow users to send files from their computer to a web server. This is typically achieved through an HTML form that includes an <input> element with the type attribute set to "file".

---

## 3. Advanced

### 3.1 Semantic Markup
- **cite**
  - The element in HTML is used to define the title of a creative work (e.g., a book, article, song, movie, painting, sculpture, etc.). It's typically used to provide a reference or citation for a source.
- **dfn**
  - The <dfn> element in HTML represents the defining instance of a term. It's used to indicate the specific location where a word or phrase is being defined for the first time within a document.
- **abbr**
  - The <abbr> tag in HTML represents an abbreviation or acronym. It's useful for providing a full description of the abbreviated term when the user hovers over it, improving accessibility and clarity.
- **address**
  - The <address> element in HTML represents contact information for the author or owner of a document or article. This can include physical addresses, email addresses, phone numbers, and social media links.

### 3.2 Styling Basics
- **blockquote**
  - The blockquote element in HTML represents a section of text that is quoted from another source. It's used to indicate that the enclosed content is an extended quotation, often displayed with indentation or other visual cues to distinguish it from the surrounding text.
- **header**
  - The <header> element represents introductory content, typically containing a group of introductory or navigational aids. It might contain a heading, logo, search form, or other relevant content.
- **article**
  - The <article> element in HTML represents a self-contained composition in a document, page, application, or site. It is intended to independently distributable or reusable, for example, in syndication.
- **nav**
  - The <nav> element in HTML is used to define a section of a page that contains navigation links. It's intended for major navigational blocks, like a site's menu, a table of contents, or a set of breadcrumbs.
- **aside**
  - The <aside> element in HTML represents a section of a page that is tangentially related to the main content. It's often used for sidebars, pull quotes, or other content that provides additional information or context but isn't essential to understanding the primary content.
- **main**
  - The <main> element in HTML defines the primary content of a document's <body>. It should contain the central topic of the page, excluding any content that is repeated across multiple pages, such as navigation, headers, or footers.
- **footer**
  - The <footer> element in HTML represents a container for introductory content or navigation links that typically appear at the end of a section or document. It usually contains information about the author, copyright data, terms of use, contact information, related documents, and sometimes navigation.
- **section**
  - The <section> tag in HTML is used to define thematic groupings of content within a document. It's a way to organize related content together, like chapters, introductions, or news items.
- **Inline CSS**
  - Inline CSS involves applying styles directly to individual HTML elements using the style attribute. This method allows you to define specific visual properties for a single element, overriding any styles defined in external stylesheets or internal style blocks.
- **External CSS**
  - External CSS involves creating separate files (with a .css extension) to hold all the styling rules for an HTML document. These CSS files are then linked to the HTML document using the <link> tag, allowing you to apply the same styles across multiple pages and keep your HTML code clean and organized.
- **Internal CSS**
  - Internal CSS allows you to add styles directly within an HTML document using the <style> tag. This tag is typically placed inside the <head> section of your HTML file.

### 3.3 Including JavaScript
- **Including JavaScript**
  - JavaScript can be added to HTML documents to make web pages interactive. This is done by embedding the JavaScript code directly within the HTML or by linking to external JavaScript files.

### 3.4 Accessibility
- **Accessibility**
  - Accessibility in HTML refers to the practice of designing and developing web content that is usable by people with disabilities. This involves ensuring that websites and web applications are perceivable, operable, understandable, and robust for individuals who may have visual, auditory, motor, or cognitive impairments, allowing them to access information and interact with the web effectively.

### 3.5 Basics of SEO
- **Basics of SEO**
  - Search Engine Optimization (SEO) is the practice of improving a website to increase its visibility in search engine results pages (SERPs). This involves optimizing various elements of a website, such as its content, structure, and HTML code, to make it more appealing to search engines like Google.

---

## 4. Optional / Specialized Topics

- Hosting
- What is SEO?
- Tags and Attributes
- Case Insensitivity
- HTML
- CSS
- JavaScript
- head
- title
- HTML Entities
- hr
- sub
- br
- sup
- pre
- Links
- id
- CSP
- Limitations
- File Uploads
- aside
- main
- footer
- section
- Inline CSS

---

## 5. References

- [HTML Roadmap](https://roadmap.sh/html)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer

### Related Skills
- JavaScript
- TypeScript
- Node.js
- React
- Css