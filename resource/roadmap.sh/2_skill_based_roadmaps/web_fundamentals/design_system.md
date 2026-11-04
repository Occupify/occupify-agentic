# Design System

## Metadata
- Type: Skill
- Domain: Web & Mobile Development
- Source: roadmap.sh
- Source URL: https://roadmap.sh/design-system
- Related Roles:
  - Frontend Developer
  - Software Architect

---

## 1. Beginner

### 1.1 Understand the Basics
- **What is a Design System?**
  - A design system is a collection of reusable components, design tokens, patterns, and guidelines that a team uses to build products consistently. It combines a component library with documentation, principles, and standards that explain how and when to use each piece.
- **Need of Design System**
  - Having a solid design system speeds up your work by making the product team more efficient, and it creates consistency and harmony within the product and brand ecosystem. A strong design system takes the burden off individual designers to think through commonly recurring design problems.
- **Design System vs Component Library**
  - A component library is just a collection of visuals i.e. colours, button stylings, fonts, etc.
- **What is Atomic Design**
  - Atomic design (by Brad Frost) is a mental model to help you think of user interfaces as a cohesive whole and a collection of parts at the same time. Through the comparison to atoms, molecules, and organisms, we can think of the design of our UI as a composition of self-containing modules put together.
- **Stakeholders Involved in Building**
  - Building a design system requires input from several roles, not just designers. Product designers define visual language and interaction patterns, frontend developers implement and maintain components in code, product managers align the system with business priorities, and accessibility specialists ensure components meet usability standards.
- **Design System Examples**
  - Design system examples are live implementations of design patterns, component libraries, and style guides used by organizations to maintain consistency across their digital products. These examples showcase how visual elements like typography, color palettes, and interactive components are organized into a cohesive framework.
- **Component Library**
  - A component library is a collection of all the components used in a website, software or app. Some of the common tools to showcase and browse components in a component library include are given below:

### 1.2 Terminology
- **Component**
  - A component is a reusable, self-contained UI element, such as a button, input field, or card, built once and used across multiple screens or products. It usually has defined states, like default, hover, and disabled, and accepts configurable properties to adapt to different contexts.
- **Design Language**
  - Design language is the overall visual and interaction style that defines how a product looks and feels, including color, typography, spacing, iconography, and motion. It expresses a brand's personality through consistent visual decisions rather than a specific set of components.
- **Governance**
  - Governance is a framework for clarifying roles, responsibilities, and authority over decisions. Having that clarity ensures that decisions for the design system funnel smoothly through the governance process
- **Guidelines**
  - Design guidelines are sets of recommendations on how to apply design principles to provide a positive user experience. Designers use such guidelines to judge how to adopt principles such as intuitiveness, learnability, efficiency and consistency so they can create compelling designs and meet and exceed user needs.
- **Pattern**
  - Patterns are best practice design solutions for specific user-focused tasks and page types. Patterns often use one or more components and explain how to adapt them to the context.

### 1.3 Making a Design System
- **Pilot**
  - Pilots are one of the best ways to put your design system through its paces, especially before the design system even gets to a v1. Like television pilots help test audience reactions to a series concept without investing significant resources to create the whole thing, application pilots are a good foundation for ensuring your design system’s design and code are battle-tested.
- **Token**
  - Design system tokens are the style values of UI elements such as color, typography, spacing, shadows, etc., that are used across products and capable of being converted to a format for any platform (web, mobile, desktop). Tokens are building blocks of the design system—think of them as sub atoms, the smallest pieces of style values that allow designers to create styles for a product.
- **Making it from Scratch**
  - There are two general paths for building a design system: creating one from scratch with a blank slate, or building one by analyzing and consolidating an existing product's design. The right approach depends on whether a product already exists and how much design debt has accumulated.
- **Making it from Existing Design**
  - Building from existing design means creating a design system by auditing and standardizing the UI of a product that already exists. This path starts with analyzing current screens, identifying inconsistencies, and extracting reusable patterns before formalizing them into tokens and components.
- **Performing a Visual Audit**
  - A visual audit is the process of collecting and examining all existing user interface elements across a product to identify inconsistencies in styles, components, and patterns. This practice involves capturing screenshots of current screens and grouping similar items to reveal discrepancies in typography, color usage, spacing, and iconography.

---

## 2. Intermediate

### 2.1 Existing Design Analysis
- **UI Kit**
  - As it relates to a design system, a UI Kit is a representation of coded components created in a way that designers who don’t know code can create interface mockups. Examples of UI kits are Sketch libraries and Figma design systems.
- **Identify Existing Design Process**
  - Identifying the existing design process involves mapping out how a team currently creates, communicates, and implements design decisions. This phase requires gathering insights into how designers and developers collaborate, documenting the current workflow, and pinpointing the specific tools or manual tasks used to hand off assets.
- **Icons**
  - Icons are visual symbols that communicate meaning quickly. They should maintain consistent style, use a grid system, provide multiple sizes, organize into semantic categories, ensure accessibility, consider cultural neutrality, be available in multiple formats, include interactive states, and follow systematic versioning.
- **Visual Forms**
  - Visual forms focus on aesthetic and interactive design aspects of form components. Effective design should establish clear information architecture, create consistent field styling, develop harmonious label positioning, design clear error communication, implement progressive enhancement, prioritize mobile-first design, and ensure cross-platform consistency.
- **Sizing**
  - Sizing tokens establish consistent dimensions across components and layouts. An effective system should establish a foundational unit, create predefined size variations, ensure minimum accessibility requirements, define standard icon sizes, establish container dimensions, implement fluid sizing, and account for platform-specific requirements.
- **Spaces**
  - Spacing tokens define white space between elements, creating visual rhythm and clear relationships. An effective system should establish a foundational unit, create systematic scales, define consistent internal spacing, establish layout guidelines, implement fluid spacing, create meaningful categories, and ensure cross-platform consistency.
- **Color**
  - Color establishes brand identity and visual hierarchy in design systems. A comprehensive color system should organize colors logically, meet WCAG accessibility standards, support light/dark themes, create semantic categories, establish systematic naming, balance brand expression with function, and provide multiple formats.
- **Typography**
  - Typography establishes hierarchy, readability, and brand personality. An effective system should develop harmonious scales using mathematical ratios, choose appropriate typefaces, implement fluid typography, establish consistent line-heights, define font weight hierarchy, ensure accessibility compliance, and provide clear usage guidelines.
- **A/B Tests & Experiments**
  - A/B tests and experiments compare two or more versions of a design to measure which performs better against a specific metric, such as click-through rate or conversion. When building a design system from an existing product, past experiment results help identify which design variations actually improved outcomes and are worth standardizing.
- **Regional Requirements**
  - Regional requirements are design and content constraints that differ by market, such as right-to-left text direction, date and currency formats, legal disclaimers, or color meanings that vary by culture. A design system built for a global product needs to account for these variations in its tokens and components rather than assuming one region's conventions apply everywhere.
- **Documentation**
  - Organize and document the results of visual audit, design elements, components with variations, states, patterns found, any existing documentation, current design process, and considerations. This documentation will be shared across the team and act as a guide when building the new design system.

### 2.2 Creating Design Language
- **Avatar**
  - Avatars represent users or entities in interfaces. They should support multiple shapes (circular, square), various sizes, handle missing images with initials or default icons, include status indicators, maintain image quality standards, ensure accessibility, provide loading states, and support group arrangements with proper interactive feedback.
- **Badges**
  - Badges are small status indicators that communicate information about objects or actions. Effective design should include numeric indicators for notifications, status badges with distinct colors, category labels, interactive states, multiple sizes, semantic color integration, consistent positioning, content guidelines, and proper accessibility.
- **Banners**
  - Banners communicate important information at the top of pages. They should support different message types with distinct visuals, various positioning options, clear dismissal mechanisms, relevant actions, consistent iconography, mobile adaptations, subtle animations, content guidelines, proper accessibility, and stacking rules for multiple banners.
- **Buttons**
  - Buttons enable user actions and require clear visual hierarchy (primary, secondary, tertiary), comprehensive interactive states, multiple sizes, icon support, content guidelines, minimum 44px touch targets, loading indicators, responsive behavior, proper accessibility with ARIA labels, and subtle animations.
- **Cards**
  - Cards are flexible content containers that group related information and actions. They require clear content hierarchy, consistent elevation systems, responsive behavior, distinct interactive states, media support, defined action areas, content variants, loading states, proper accessibility, and consistent spacing aligned with the design system.
- **Dropdowns**
  - Dropdowns reveal option lists when activated to save space. They need clear triggers with visual indicators, organized options with grouping, search/filtering for long lists, multi-select support, smart positioning, full keyboard navigation, loading states, mobile adaptations, proper accessibility, and performance optimization.
- **Forms**
  - Forms collect user input and require standardized input components, comprehensive validation systems, effective labeling strategies, consistent layouts, clear error handling, progressive disclosure, required field indicators, auto-complete integration, proper accessibility, and mobile optimization.
- **...other**
  - Specialized elements beyond core components include badges for notifications, breadcrumbs for navigation, progress indicators, tooltips for help, pagination for browsing, tab systems, accordions for collapsible content, modals for focused interactions, notification systems, and basic data visualization elements.
- **Writing Guidelines**
  - Writing guidelines define rules for how text should be written across a product, covering grammar conventions, capitalization, punctuation, and formatting for things like button labels and error messages. They keep copy consistent regardless of which team member wrote it.
- **Tone of Voice**
  - Tone of voice describes the personality and style a brand uses when communicating with users through text, such as being friendly, formal, or playful. It shapes word choice, sentence length, and how messages are framed, especially in things like onboarding copy, error messages, and notifications.
- **Terminology**
  - Create the standard terms and phrases that need to be kept the same throughout the user experience, speeding up the design process and unifying your voice.
- **Design Principles**
  - Design principles are a short set of guiding statements that describe the values a team follows when making design decisions, such as prioritizing clarity over cleverness or consistency over novelty. They act as a reference for resolving disagreements or evaluating whether a new component fits the system's intent.
- **Vision**
  - Brand vision serves as the foundation for design system decisions, providing purpose and direction. An effective vision should articulate organizational purpose, identify core values, visualize future success, prioritize user needs, clarify brand uniqueness, account for cultural considerations, and connect to measurable goals.

### 2.3 Defining Design Tokens
- **Monochrome Version**
  - A monochrome version of a logo is a single-color variant used in contexts where the full-color logo doesn't work, such as on colored backgrounds, in print, or in low-contrast situations. It typically comes in both black and white variants to cover light and dark backgrounds.
- **Small Use Guidance**
  - Small use guidance provides specific instructions and design adjustments for rendering a logo at minimal sizes, such as in favicons, mobile headers, or social media avatars. This involves simplifying complex shapes, removing intricate text, or increasing the contrast of visual elements to ensure the brand remains recognizable and legible at very low resolutions.
- **Placement Guidance**
  - Logo placement guidance ensures consistent brand representation through clear positioning, sizing, and clearance rules. Effective guidelines should define minimum clearance areas, establish preferred positions for different contexts, provide size specifications, define background treatments, and account for platform-specific requirements.
- **Usage Guidance**
  - Logo usage guidance provides rules for proper implementation to maintain brand consistency. Effective guidance should establish clear examples of proper usage and mistakes to avoid, define logo variations, specify color requirements, prohibit unauthorized alterations, and include approval processes for new contexts.
- **File Formats**
  - Logo file formats determine how a brand mark is encoded, stored, and rendered across different digital and print environments. Vector formats, such as SVG, EPS, and AI, use mathematical paths to ensure the logo remains crisp and scalable at any size without losing quality.
- **Accessibility**
  - Make sure to have accessible pairings between the main colours in your palette. More importantly, make sure that your background and text colours have at least an AA standard contrast ratio between them.
- **Functional Colors**
  - Functional colors are tokens that communicate a specific meaning or state, such as red for error, green for success, yellow for warning, and blue for informational messages. They are distinct from a brand's primary palette because their purpose is to convey status consistently rather than express brand identity.
- **Dark Mode**
  - Dark mode is an alternate color scheme that uses dark backgrounds and light text instead of the default light theme, often to reduce eye strain in low-light environments. Supporting it as a design token concern means defining a parallel set of color values that map to the same semantic roles as the light theme, such as background, text, and border colors.
- **Guidelines**
  - Color guidelines provide a standardized framework for how colors are applied across an interface to ensure visual consistency and accessibility. These rules define the specific usage for primary, secondary, functional, and neutral color palettes, detailing which shades should be used for elements like backgrounds, text, borders, and interactive states.
- **Units**
  - Units are the most granular building blocks for layout. Defining a set of values with consistent increments (such as 4, 8, 12 and 16 for a 4-point system) will provide you with the foundation when you’re designing your grid and spacing values.
- **Grid**
  - Every layout should sit on a grid that brings order and hierarchy to the interface. Define a grid separately for mobile, tablet and desktop devices with columns, gutters, and margins so your interface can adapt to any platform easily.
- **Breakpoints**
  - Breakpoints are the specific screen width values at which a layout changes to adapt to different device sizes, such as switching from a single column on mobile to multiple columns on desktop. Design systems define a standard set of breakpoints so that every component and page responds consistently at the same screen widths.
- **Spacking**
  - Spacing tokens define the standard set of gap and padding values used between and within components, usually built as a scale of multiples of a base unit. Having a fixed spacing scale prevents designers and developers from picking arbitrary pixel values, which keeps layouts visually consistent.
- **Responsiveness**
  - Desktop devices can usually afford to have bigger font sizes compared to mobile devices. Creating a typography scale that adapts to the viewport size will help with a more meaningful hierarchy and layout.
- **Grid Relation**
  - Grid relation describes how typography or iconography sizes align to the underlying layout grid, ensuring that line heights and icon dimensions land on consistent grid units. Keeping these elements aligned to the grid avoids visual misalignment when text or icons sit next to other grid-based components.
- **Readability**
  - Readability in typography covers the factors that make text easy to read, including font size, line height, line length, and contrast against the background. Design systems set minimum readability standards, such as a maximum number of characters per line or a minimum line height ratio, to prevent overly dense or cramped text.
- **Performance**
  - Custom fonts need to be downloaded before they can be displayed, especially on the web. Make sure that you have sensible fallbacks and fast loading time for your typography assets.

### 2.4 Creating Core Components
- **Accessibility**
  - In the context of design tokens, accessibility refers to ensuring that color and other visual choices meet contrast and legibility standards, such as WCAG guidelines, for users with visual impairments. It means checking that text colors have sufficient contrast against their backgrounds and that icon sizes remain legible at small scales.
- **User Onboarding**
  - User onboarding encompasses the design patterns and instructional elements that guide new users through an interface to help them understand its core value and functionality. These guidelines define how tooltips, walkthroughs, empty state illustrations, and progress indicators should look and behave to ensure a consistent experience across the product.
- **Microcopy Guidelines**
  - Microcopy guidelines provide a standardized framework for writing the small snippets of text that appear throughout an interface, such as button labels, error messages, and tooltips. These instructions outline the preferred voice, tone, vocabulary, and formatting standards to ensure that all user-facing text is clear, concise, and helpful.
- **Style**
  - In iconography, style refers to the consistent visual approach used across a set of icons, such as outlined, filled, or duotone, along with consistent stroke width and corner treatment. Keeping a single style across all icons prevents a product from feeling visually disjointed when icons from different sources get mixed together.
- **Naming**
  - Naming conventions for icons define how each icon file or component is labeled, typically based on what it represents or the action it performs, such as "icon-search" or "icon-trash." Consistent naming makes icons easier to find and reference in code, especially as an icon set grows to hundreds of entries. Design systems usually document a naming pattern to avoid duplicate or ambiguous icon names.
- **Grid Relation**
  - Draw your icons in a bounding box that plays well with your grid. This makes for a better pairing with other UI elements.
- **Sizes**
  - Icon sizes define the standard dimensions an icon set supports, such as 16px, 24px, and 32px, so icons remain crisp and consistent wherever they appear. Design systems typically build icons on a fixed grid at each supported size to keep stroke widths and proportions consistent across the set.
- **Keywords**
  - Keywords are the searchable terms associated with each icon, used to help designers and developers find the right icon in a large icon library. An icon representing a trash can might include keywords like "delete," "remove," and "bin" so it surfaces under multiple search terms.
- **Reserved Icons**
  - Reserving icons that represent common actions will prevent their use in any other context. System icons for navigation or adding and deleting are a good example.
- **Guidelines**
  - Provide guidelines on how and when to use icons, what to keep in mind when working with them and how not to use them.
- **Avatar**
  - An avatar is a graphical representation of a user or entity, typically displayed as a circular or square image, an icon, or a set of initials. It serves as a visual identifier within an interface to provide context about a person, group, or account status.
- **Input Text**
  - An input checkbox component lets users select one or more options from a set of choices, toggling between a checked and unchecked state. It usually supports an indeterminate state as well, used when a checkbox represents a partially selected group of sub-options.
- **Banner**
  - A banner is a UI element used to display prominent, time-sensitive messages, alerts, or announcements to users. It typically appears at the top of a page or section to ensure immediate visibility without blocking the user's interaction with the rest of the interface.
- **Design Editor**
  - There are many design editors available in the market today with the most popular names being Sketch, Figma and Adobe XD. If you're unsure which route to go down it's often best to speak with your team.
- **Plugins**
  - Plugins are add-on tools that extend a design editor's functionality, such as automating token synchronization, checking accessibility contrast, or generating code snippets from design components. They reduce manual work by connecting the design tool directly to other parts of the design system workflow, like a token repository or a documentation site.

---

## 3. Advanced

### 3.1 Tooling
- **Badge**
  - A badge is a small UI element used to display status indicators, notifications, or counts associated with a specific item. It typically appears as a compact label containing text or a number, often positioned near an icon, button, or navigation link to provide quick, at-a-glance information to the user.
- **Button**
  - A button is an interactive element that triggers an action or event when a user clicks or taps on it. It serves as a primary navigation or functional trigger within a user interface, often featuring distinct styles to represent different states such as hover, active, or disabled.
- **Card**
  - A card is a versatile UI container that groups related content, such as text, images, and actions, into a single, cohesive visual unit. It acts as a flexible interface element that helps organize information into manageable blocks, making it easier for users to scan and interact with specific data points.
- **Carousel**
  - A carousel is a UI component that displays a series of visual items or content blocks in a rotating, horizontal, or vertical sequence. It allows users to browse through multiple pieces of media or information within a confined space by interacting with navigation controls like arrows, dots, or swipe gestures.
- **Dropdown**
  - A dropdown is a navigation or selection component that presents a list of options when a user interacts with a toggle element, such as a button or an icon. It serves as an efficient way to save screen space by hiding secondary choices until they are explicitly needed.
- **Icon**
  - An icon is a small graphical symbol used to represent actions, objects, or concepts within a user interface. These visual elements provide immediate visual context and help users navigate applications more efficiently by replacing or supplementing text labels.
- **Input Checkbox**
  - An input checkbox component lets users select one or more options from a set of choices, toggling between a checked and unchecked state. It usually supports an indeterminate state as well, used when a checkbox represents a partially selected group of sub-options.
- **Input Radio**
  - An input radio component lets users select exactly one option from a group of mutually exclusive choices. Radio buttons in a group share a common name so that selecting one automatically deselects the others.
- **Input Switch**
  - An input switch, also called a toggle, lets users turn a single setting on or off, typically represented as a sliding control rather than a checkbox. It's commonly used for binary settings, like enabling notifications, where the on and off states have a clear, immediate effect.
- **List**
  - A list component displays a vertical sequence of items, each following the same layout, such as a list of contacts or notifications. It often supports variants like showing an icon, avatar, or action button alongside each item's text.
- **Loading Indicator**
  - A loading indicator communicates to the user that content is being fetched or processed, typically shown as a spinner, progress bar, or skeleton screen. It prevents the interface from appearing frozen or broken during delays caused by network requests or heavy computation.
- **Modal**
  - A modal component displays content in a layer above the main page, requiring user interaction before returning to the underlying content, commonly used for confirmations or focused tasks. It typically includes a backdrop that dims the rest of the page and traps keyboard focus within the modal while it's open.
- **Tabs**
  - A tabs component lets users switch between different views or sections of content within the same page area, without navigating to a new page. Each tab typically shows a label and, when selected, displays its associated content while hiding the others.
- **Version Control**
  - Version control, in the context of design tooling, means tracking changes to design files over time, similar to how developers track code changes, so past states can be reviewed or restored. Some design editors have built-in version history, while others rely on external plugins or file naming conventions to track changes.
- **Contribution Guidelines**
  - Contribution guidelines document the process for proposing, reviewing, and approving changes to a design system, whether on the design side or the development side. They typically cover how to submit a new component, who reviews proposed changes, and what criteria a contribution needs to meet before acceptance.
- **Component Catalog**
  - A component catalog is a searchable, browsable reference of every component in a design system's code library, usually generated automatically from the component code itself. Tools like Storybook are commonly used to build a catalog that shows each component's variants, props, and usage examples in an interactive interface.
- **Documentation**
  - Documentation serves as the central hub for capturing guidelines, component usage, and design principles, allowing teams to understand how to effectively implement and maintain the system. It bridges the gap between design and development by providing interactive examples, code snippets, and clear instructions for consuming the shared assets.

### 3.2 Project Management
- **Select**
  - A select component is an interface element that allows users to choose one or more options from a predefined list. It typically appears as a dropdown menu that remains collapsed to save screen space until the user clicks or taps on it.
- **Textarea**
  - A textarea component is a multi-line text input used for longer form entries, such as comments or descriptions, as opposed to a single-line text input. It usually supports resizing, character count limits, and validation states like error or success.
- **Toast**
  - A toast component displays a brief, temporary message that appears and disappears automatically, typically used for confirmations like "Changes saved" or lightweight error notices. Unlike a banner, a toast floats above the page content and doesn't require the user to dismiss it manually.
- **Tooltip**
  - A tooltip component displays a small piece of contextual information when a user hovers over or focuses on an element, typically used to explain an icon-only button or provide extra detail. It appears near the triggering element and disappears once the user moves away or shifts focus elsewhere.
- **Code Style**
  - Code style refers to the formatting and structural conventions followed when writing a design system's component code, such as naming conventions, file structure, and formatting rules enforced by tools like ESLint or Prettier. Consistent code style makes the codebase easier to read and maintain as multiple contributors add or update components.
- **Unit Testing**
  - Unit testing means writing automated tests that verify individual components behave correctly in isolation, such as checking that a button calls its click handler or that a checkbox toggles its state correctly. These tests catch regressions early when a component's code changes, before the change reaches production.
- **Accessibility Testing**
  - Accessibility testing checks that components meet standards like WCAG, covering things like sufficient color contrast, proper keyboard navigation, and correct screen reader labeling. It combines automated tools, like axe or Lighthouse, with manual testing using assistive technology to catch issues automated tools miss.
- **Semantic Versioning**
  - Semantic versioning is a version numbering convention, formatted as major.minor.patch, used to communicate the type of change made in each release of a design system's code. A major version bump signals a breaking change, a minor version adds new functionality without breaking existing usage, and a patch fixes bugs.
- **Release Strategy**
  - A release strategy defines how and how often new versions of a design system get published, including whether releases happen on a fixed schedule or whenever changes are ready. It also covers how breaking changes get communicated and how long older versions remain supported.
- **Commit Guidelines**
  - Commit guidelines define a consistent format for writing commit messages when contributing code to a design system, such as the Conventional Commits format that prefixes messages with types like "feat" or "fix." Consistent commit messages make it easier to generate changelogs automatically and to understand a project's history at a glance. They're often enforced through automated checks that reject commits not following the required format.
- **PR Templates**
  - A PR template is a predefined structure that appears when someone opens a pull request, prompting contributors to fill in information like a description of the change, screenshots, and a checklist of required steps. It ensures every contribution includes the context a reviewer needs, rather than relying on contributors to remember what to include.
- **Contribution Guidelines**
  - Contribution guidelines are a set of rules and best practices that define how team members can submit updates, bug fixes, or new components to a shared codebase. They outline the expected workflow, such as how to set up the local environment, follow branching strategies, run automated tests, and format pull requests.
- **Roadmap**
  - A roadmap, in project management terms, is a high-level plan that outlines what a design system team intends to build or improve over a given period, such as new components or major token changes. It helps set expectations with consuming teams about what's coming and in what order.
- **Milestones**
  - Milestones are specific checkpoints within a design system's roadmap that mark the completion of a significant piece of work, such as shipping a new component library version or completing an accessibility audit. They break a larger roadmap into measurable stages, making it easier to track progress over time.
- **Ticketing**
  - Ticketing refers to the system used to track individual tasks, bugs, and feature requests related to a design system, typically using tools like Jira or Linear. Each ticket captures a specific piece of work, such as adding a new component variant or fixing an accessibility issue, along with its status and assignee.
- **Component Analytics**
  - Track the usage of your components. For development you can use built-in tools like Figma’s Design System Analytics.
- **Logging**
  - Logging, in the context of a design system, means recording events and errors that occur when components are used in production, such as a component failing to render or receiving invalid props. Reviewing these logs helps the design system team catch bugs that only surface in real-world usage across different consuming products.
- **Tooling Analytics**
  - Tooling analytics measure how the design system's own supporting tools get used, such as how often a Figma plugin runs, how frequently the documentation site is visited, or how often the component catalog is searched. This data helps the team understand which tools deliver value and which ones go unused.
- **Service and Health Metrics**
  - Service and health metrics track the overall reliability and performance of a design system as a product in its own right, such as build times, uptime of documentation or component hosting, and how quickly reported bugs get resolved. These metrics give the team an objective view of how well the design system is being maintained, beyond just component-level usage.
- **Community Meetings**
  - Community meetings are regularly scheduled sessions where design system maintainers and the teams that consume the system come together to discuss updates, gather feedback, and address concerns. They give consuming teams a direct channel to raise issues or request new components rather than relying solely on written tickets.
- **Communication Channel**
  - A communication channel is the primary medium a design system team uses for day-to-day questions and announcements, such as a dedicated Slack channel or Microsoft Teams space. It gives consuming teams a fast way to ask questions or report issues without going through formal ticketing for every small query.
- **Open Hours**
  - Open hours are scheduled time blocks during which the design system team is available for live questions, pairing sessions, or troubleshooting help from consuming teams. They give teams a predictable way to get direct support without waiting for a response in a ticket or chat channel.
- **FAQs**
  - FAQs are a curated list of frequently asked questions and their answers, covering the most common issues or points of confusion that consuming teams run into when using the design system. Maintaining an FAQ reduces repetitive support requests by pointing people to existing answers before they need to ask directly.

---

## 4. Optional / Specialized Topics

- Stakeholders Involved in Building
- Design System Examples
- Component Library
- Pattern
- Performing a Visual Audit
- Sizing
- Spaces
- Color
- Typography
- A/B Tests & Experiments
- Regional Requirements
- Documentation
- Cards
- Dropdowns
- Forms
- ...other
- Writing Guidelines
- Tone of Voice
- Terminology
- Design Principles
- Vision
- File Formats
- Accessibility
- Functional Colors
- Dark Mode

---

## 5. References

- [Design System Roadmap](https://roadmap.sh/design-system)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Software Architect

### Related Skills
- JavaScript
- React
- Node.js
- System Design