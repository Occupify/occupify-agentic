# CSS

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/css
- Related Roles:
  - Frontend Developer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Introduction
- **HTML**
  - HTML (HyperText Markup Language) is the standard markup language for creating web pages. It provides the structure and content of a website, using elements to define headings, paragraphs, images, links, and other components that are displayed in a web browser.
- **JavaScript**
  - JavaScript is a programming language primarily used to create interactive and dynamic content on websites. It allows developers to add features like animations, form validation, and real-time updates without needing to reload the page.
- **CSS**
  - CSS (Cascading Style Sheets) is a language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and other visual aspects of web pages, ensuring a consistent and visually appealing user experience across different devices and screen sizes.
- **Frontend development**
  - Frontend development involves crafting the user interface and user experience of a website or web application. It focuses on the parts of a website that users directly interact with, such as buttons, text, images, and navigation.

### 1.2 CSS Basics
- **Inline CSS**
  - Inline CSS involves directly embedding CSS styles within HTML elements using the style attribute. This method applies styles to individual elements, overriding external stylesheets or embedded styles.
- **External CSS**
  - External CSS involves writing CSS rules in a separate file (with a .css extension) and then linking that file to your HTML document. This approach promotes cleaner code, easier maintenance, and reusability of styles across multiple web pages.
- **Internal CSS**
  - Internal CSS involves embedding CSS rules directly within an HTML document. This is achieved by using the <style> tag, typically placed inside the <head> section of the HTML file.
- **Cascading order**
  - Cascading order in CSS determines which styles are applied to an element when multiple conflicting rules target the same element. It's a set of rules that browsers follow to resolve these conflicts, prioritizing styles based on factors like importance, specificity, and source order.

### 1.3 Rules
- **Selector**
  - A selector is a fundamental part of a CSS rule. It's essentially a pattern that identifies which HTML elements the rule should be applied to.
- **Declaration**
  - A declaration in CSS is a single statement that specifies a property you want to style and the value you want to assign to that property. It's the fundamental building block for applying styles to HTML elements.
- **Properties & Values**
  - In CSS, properties are like instructions that tell the browser how to style an HTML element. Each property has a value, which specifies the exact styling to apply.

### 1.4 Comments
- **Comments**
  - Comments in CSS are notes that you add to your code to explain what it does, or to temporarily disable parts of your code. Browsers ignore these comments, so they don't affect how your website looks.

### 1.5 Simple selectors
- **element**
  - Element selectors in CSS target HTML elements directly by their tag name. They allow you to apply styles to all occurrences of a specific element, such as all <p> (paragraph) or <h1> (heading) tags on a webpage.
- **universal**
  - The universal selector in CSS is a simple selector that matches any element on a webpage. Represented by an asterisk (\), it applies a specific style to all elements, regardless of their type or position in the document tree.
- **class**
  - Class selectors in CSS are used to select HTML elements based on the class attribute. They allow you to apply specific styles to elements that share a common class name.
- **grouping**
  - Grouping selectors in CSS allows you to apply the same styles to multiple HTML elements simultaneously. Instead of writing the same CSS rules for each element individually, you can list the selectors separated by commas.
- **id**
  - ID selectors in CSS are used to style a single, unique element on a webpage. They target an HTML element based on the value of its id attribute.
- **Direction**
  - The direction property in CSS sets the text direction of block-level elements, influencing how text, table columns, and inline-level boxes flow. While direction can be used to switch between left-to-right (LTR) and right-to-left (RTL) layouts, it's generally better to use the HTML dir global attribute.

### 1.6 Combinator selectors
- **descendant**
  - The descendant combinator in CSS is a way to select HTML elements that are descendants of another element. It uses a single space (" ") between two selectors.
- **Next Sibling**
  - The next-sibling combinator in CSS (represented by the + symbol) selects an element that immediately follows another specific element in the HTML structure. It targets the element that is the very next sibling, meaning it shares the same parent and appears directly after the first element in the source code.
- **child**
  - The child combinator selector in CSS allows you to target elements that are direct children of a specified parent element. It uses the > symbol to denote this direct parent-child relationship.

### 1.7 Attribute selectors
- **Font families**
  - Font families in CSS are a way to specify the typeface used to display text on a webpage. They allow you to define a prioritized list of fonts, so if the user's computer doesn't have the first font available, the browser will try the next one in the list, and so on.
- **Font Size**
  - Font size in CSS determines the size of the text on a webpage. It's a fundamental property that controls the visual prominence and readability of text elements.
- **Font Style**
  - Font style in CSS is used to select the appearance of a font, primarily to italicize or oblique text. It allows you to specify whether a font should be displayed in its normal, italic, or oblique version.

### 1.8 Text Styling
- **Subsequent Sibling**
  - The subsequent-sibling combinator in CSS is a way to select elements that are siblings (elements sharing the same parent) and appear directly after a specified element. It uses the tilde (~) symbol to denote this relationship.
- **Font Shorthand**
  - The font shorthand property in CSS provides a way to set multiple font-related properties in a single declaration. Instead of specifying font-style, font-variant, font-weight, font-size, line-height, and font-family individually, you can use the font property to define them all at once, making your stylesheets more concise and readable.
- **Google Fonts**
  - Google Fonts is a free library of over a thousand different font families that you can easily use on your website. Instead of relying on the limited set of fonts that come pre-installed on a user's computer, you can link to Google's servers and use any font they offer.
- **Color**
  - Color in CSS is used to specify the foreground color of text and other elements. It can be defined using various methods, including named colors (like "red" or "blue"), hexadecimal values (like "#FF0000"), RGB values (like "rgb(255, 0, 0)"), RGBA values (which include an alpha channel for transparency), HSL values (hue, saturation, lightness), and HSLA values (which include an alpha channel for HSL).
- **Text Alignment**
  - Text alignment in CSS controls how text is positioned horizontally within its containing element. It determines whether text is aligned to the left, right, center, or justified (spread evenly across the line).
- **Text Decoration**
  - Text decoration in CSS refers to the styling applied to text to enhance its appearance or convey specific meanings. It primarily involves adding lines above, below, or through the text.
- **Text Transform**
  - Text transform in CSS controls the capitalization of text. It allows you to change the case of letters within an element, regardless of how the text is originally written in the HTML.
- **Text Spacing**
  - Text spacing in CSS involves adjusting the space between characters, words, and lines of text. This control allows for improved readability and visual appeal by fine-tuning the horizontal and vertical spacing within text elements.
- **Line Height**
  - Line height in CSS controls the vertical space between lines of text within an element. It essentially defines the distance from the top of one line of text to the top of the next line.
- **Text Shadows**
  - Text shadows in CSS add depth and visual interest to text by creating a blurred, offset copy of the text behind it. This effect is achieved using the text-shadow property, which allows you to specify the shadow's horizontal offset, vertical offset, blur radius, and color.
- **Font Weight**
  - Font weight refers to the thickness or boldness of characters in a typeface. In CSS, it's a property that allows you to specify how heavy or light the font should appear.

### 1.9 Opacity
- **Font Variant**
  - Font variant in CSS allows you to control the display of different variations of a font, such as small caps, oldstyle numerals, and alternate glyphs. It provides a way to access OpenType features within a font, enabling richer typographic control beyond basic font styling like size and weight.

### 1.10 Background
- **rgb**
  - RGB in CSS allows you to define colors using the Red, Green, and Blue color model. You specify the intensity of each color component (Red, Green, and Blue) as a value between 0 and 255, or as a percentage from 0% to 100%.
- **Named Colors**
  - Named colors in CSS are predefined color values represented by specific keywords. Instead of using hexadecimal codes or RGB values, you can use names like "red," "blue," "green," or "black" to style elements.
- **hsl**
  - HSL (Hue, Saturation, Lightness) is a way to define colors in CSS using three components: Hue, which represents the color type on a color wheel (0-360 degrees); Saturation, which indicates the intensity of the color (0-100%); and Lightness, which determines how bright or dark the color is (0-100%). This model offers a more intuitive way to adjust colors compared to RGB, allowing developers to easily create variations of a color by modifying its hue, saturation, or lightness values.
- **Background Color**
  - Background color in CSS sets the color of an element's background. It fills the entire box of an element, including padding, but not the border or margin.
- **Background Image**
  - A background image in CSS lets you add an image to the background of an HTML element. This image can be a simple pattern, a photograph, or any other visual element you want to display behind the content of your element.
- **Background Gradient**
  - Background gradients in CSS allow you to create smooth transitions between two or more colors for the background of an element. Instead of a solid color, you can define a gradient that blends colors together, adding visual depth and interest to your designs.
- **Background Position**
  - Background position in CSS controls where a background image is placed within its element. It lets you specify the horizontal and vertical placement of the image, using keywords like top, bottom, left, right, and center, or with numerical values (pixels, percentages, etc.) to fine-tune the exact location.
- **Background Attachment**
  - Background attachment in CSS controls how a background image behaves when the page is scrolled. It determines whether the background image scrolls along with the content or remains fixed in place.

---

## 2. Intermediate

### 2.1 Box Model
- **hex**
  - Hex colors in CSS are a way to specify colors using hexadecimal values. They use a six-digit code, prefixed with a hash symbol (#), to represent the red, green, and blue components of a color.

### 2.2 Padding
- **Padding**
  - Padding refers to the space between the content of an element (like text or an image) and its border. It essentially creates a cushion around the content within the element's box.

### 2.3 Margin
- **Margin**
  - Margin in CSS defines the space around an HTML element's border. It creates a gap between the element and surrounding elements, controlling the spacing and layout of content on a webpage.

### 2.4 Width / Height
- **Width / Height**
  - Width and height in CSS define the size of an element's content area. The width property sets the horizontal space an element occupies, while the height property sets the vertical space.

### 2.5 Border
- **Border**
  - In CSS, the border property defines the line that surrounds an HTML element's content and padding. It controls the border's style (like solid, dashed, or dotted), width (thickness), and color.

### 2.6 Outline
- **Outline**
  - In CSS, the outline property draws a line around an element, outside the border. Unlike borders, outlines don't affect the element's dimensions or position in the layout.

### 2.7 Box Shadows
- **Box Shadows**
  - Box shadows in CSS are visual effects that add depth and dimension to elements by creating a shadow around their frames. These shadows can be customized in terms of color, offset (horizontal and vertical distance), blur radius, and spread radius, allowing designers to simulate various lighting conditions and create visually appealing interfaces.

### 2.8 Position
- **Relative**
  - Relative positioning in CSS allows you to shift an element from its normal position in the document flow. Instead of being fixed in place, the element is moved relative to where it would have been if it were statically positioned.
- **Absolute**
  - Absolute positioning in CSS allows you to precisely place an element relative to its nearest positioned ancestor (an ancestor with a position value other than static). If no such ancestor exists, the element is positioned relative to the initial containing block, which is typically the <html> element.
- **Sticky**
  - Sticky positioning in CSS is a hybrid of relative and fixed positioning. An element with position: sticky; is initially positioned relatively, but when the user scrolls to a point where the element would normally scroll off-screen, it becomes fixed, sticking to the specified offset (e.g., top: 0;) until the containing block's boundary is reached.
- **Fixed**
  - Fixed positioning in CSS allows an element to be locked in place relative to the browser window. This means that even when the user scrolls the page, the element remains visible in the same location on the screen.
- **Static**
  - Static positioning is the default way elements are placed on a webpage. Elements with static positioning are rendered in the order they appear in the HTML, following the normal document flow.

### 2.9 Display
- **rgba, hsla**
  - rgba and hsla are color models used in CSS to define colors with added transparency. rgba represents colors using Red, Green, Blue, and Alpha (transparency) values, while hsla uses Hue, Saturation, Lightness, and Alpha values.
- **inline**
  - The display: inline property in CSS is used to specify that an element should be displayed as an inline element. Inline elements flow along with the surrounding content, similar to how text flows within a paragraph.
- **block**
  - The display: block; property in CSS makes an element behave like a block-level element. This means it will take up the full width available to it, starting on a new line and pushing subsequent content to a new line as well.
- **inline-block**
  - inline-block is a value for the CSS display property. It allows an element to flow like an inline element (sitting on the same line as other content) but also allows you to set its width and height, similar to a block-level element.

### 2.10 CSS Units
- **Absolute vs Relative**
  - Absolute units in CSS represent fixed measurements, like pixels (px) or inches (in), and will always render at the same size regardless of screen size or other factors. Relative units, on the other hand, are based on other values, such as the font size of the parent element (em), the viewport width (vw), or the root element's font size (rem), allowing for more flexible and responsive layouts.

### 2.11 Z-Index / Stacking Context
- **Z-Index / Stacking Context**
  - Z-index in CSS controls the vertical stacking order of elements that overlap. Elements with a higher z-index value will appear in front of elements with a lower z-index value.

### 2.12 CSS Specificity
- **CSS Specificity**
  - CSS Specificity is the set of rules that browsers use to determine which CSS declarations apply to an element when multiple conflicting rules exist. It's essentially a weighting system that prioritizes certain CSS selectors over others, ensuring that the most relevant style is applied.

### 2.13 Tables
- **Tables**
  - Tables in CSS are used to format tabular data on a webpage, arranging information into rows and columns. CSS provides properties to control the appearance of tables, including borders, spacing, alignment, and styling of individual cells, rows, and columns.

---

## 3. Advanced

### 3.1 Lists
- **Lists**
  - Lists in CSS are used to style HTML list elements, such as <ul> (unordered list), <ol> (ordered list), and <dl> (definition list). CSS provides properties to control the appearance of list markers (bullets or numbers), their position, and the overall styling of the list items.

### 3.2 Pseudo Classes
- **none**
  - display: none is a CSS property value that completely removes an element from the document flow. When applied, the element will not take up any space on the page, and it will not be rendered at all.
- **visibility**
  - The visibility property in CSS controls whether an element is visible or hidden. When an element's visibility is set to hidden, it disappears from the page, but the space it would have occupied remains.
- **Floating Elements**
  - Floating elements in CSS allow you to take an element out of the normal document flow and position it to the left or right of its containing element. Other content will then flow around the floated element.
- **Multicolumn layout**
  - Multicolumn layout in CSS allows you to divide a block of content into multiple columns, similar to newspaper layouts. This feature enables text and other content to flow automatically from one column to the next, improving readability and making efficient use of screen space, especially for longer articles or lists.
- **Flexbox**
  - Flexbox is a CSS layout model that provides an efficient way to arrange, align, and distribute space among items in a container, even when their size is unknown or dynamic. It simplifies the creation of complex layouts by offering powerful tools for controlling the direction, order, size, and alignment of elements within a container.

### 3.3 Pseudo Elements
- **Units with functions**
  - Units with functions in CSS allow you to dynamically calculate values for properties using functions like calc(), min(), max(), and clamp(). These functions enable you to perform mathematical operations and comparisons directly within your CSS, making your designs more flexible and responsive by adapting to different screen sizes and contexts.

### 3.4 Images and Filters
- **Transforms**
  - Transforms in CSS allow you to alter the shape and position of elements in a two-dimensional or three-dimensional space. This includes operations like rotating, scaling, skewing, and translating elements, providing a way to create visually engaging effects and manipulate the layout without affecting the underlying document flow.
- **Keyframe Animations**
  - Keyframe animations in CSS allow you to control the intermediate steps in a CSS animation sequence. Instead of just defining the start and end states, you can specify multiple points (keyframes) along the animation timeline, defining the styles an element should have at each point.
- **Transitions**
  - Transitions in CSS allow you to smoothly change property values over a specified duration. Instead of an abrupt change, a transition creates a gradual effect when a CSS property changes, such as when hovering over an element or when a class is added or removed.

### 3.5 Flow Layout
- **Flow Layout**
  - Flow layout is the default way elements are positioned on a webpage. Elements are displayed one after another, like words in a sentence, following the natural flow of the HTML.

### 3.6 CSS Functions
- **Sass**
  - Sass (Syntactically Awesome Style Sheets) is a preprocessor scripting language that is compiled into CSS. It extends the capabilities of basic CSS by allowing you to use features like variables, nesting, mixins, functions, and inheritance.
- **PostCSS**
  - PostCSS is a tool that uses JavaScript to transform CSS. It acts as a CSS parser and provides an API to analyze and modify the CSS code.
- **BEM**
  - BEM (Block, Element, Modifier) is a CSS naming convention that helps developers create more modular, reusable, and maintainable code. It structures class names to reflect the relationships between different parts of a user interface.
- **CSS Modules**
  - CSS Modules are a system where CSS class names and animation names are scoped locally by default. This means that the class names you define in your CSS files are automatically transformed to be unique, preventing naming collisions and making it easier to manage styles in large projects.
- **CSS-in-JS**
  - CSS-in-JS is a technique where CSS styles are written with JavaScript instead of external CSS files. This approach allows you to use JavaScript's capabilities, like variables, logic, and component-based architecture, to manage and apply styles directly within your JavaScript code.

### 3.7 CSS Variables
- **Grid**
  - Grid Layout is a two-dimensional layout system for CSS, enabling you to control the placement and sizing of elements within a grid container. It divides a webpage into rows and columns, allowing precise positioning of content and creating complex layouts with ease.
- **Accessibility**
  - Accessibility in CSS focuses on creating web content that is usable by everyone, regardless of their abilities or disabilities. This involves using semantic HTML, providing alternative text for images, ensuring sufficient color contrast, and designing layouts that are navigable with assistive technologies like screen readers.
- **Performance**
  - CSS performance refers to how efficiently CSS code is processed and rendered by a browser, impacting the speed and responsiveness of a website. Optimizing CSS for performance involves techniques like minimizing file sizes, reducing the complexity of selectors, and leveraging browser caching to ensure a smooth user experience.

### 3.8 Media Queries
- **Media Queries**
  - Media Queries are a powerful feature that allows you to apply different CSS styles based on characteristics of the device or screen being used to view a webpage. This enables you to create responsive designs that adapt to various screen sizes, resolutions, and orientations, ensuring an optimal viewing experience across a wide range of devices, from desktops to smartphones.

### 3.9 Container Queries
- **Container Queries**
  - Container Queries are a CSS feature that allows styles to be applied to an element based on the size or other characteristics of its containing element, rather than the viewport. This enables more granular and context-aware styling, where components can adapt their appearance based on the space available within their parent container, leading to more flexible and reusable designs.

### 3.10 Responsive typography
- **Responsive typography**
  - Responsive typography is about making the text on a webpage look good and be easily readable on different screen sizes and devices. It involves adjusting font sizes, line heights, letter spacing, and other text properties to ensure optimal readability, whether someone is viewing the site on a large desktop monitor or a small mobile phone.

---

## 4. Optional / Specialized Topics

- id
- Direction
- Text Alignment
- Text Decoration
- Text Transform
- Text Spacing
- Line Height
- Text Shadows
- Font Weight
- Background Image
- Background Gradient
- Background Position
- Background Attachment
- Static
- Flexbox
- CSS-in-JS

---

## 5. References

- [CSS Roadmap](https://roadmap.sh/css)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Fullstack Developer

### Related Skills
- Html
- JavaScript