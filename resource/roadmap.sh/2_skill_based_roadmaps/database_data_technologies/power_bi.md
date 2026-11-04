# Power BI

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/power-bi
- Related Roles:
  - BI Analyst
  - Data Analyst
  - AI and Data Scientist

---

## 1. Beginner

### 1.1 Introduction
- **Power BI Ecosystem**
  - The Power BI ecosystem is made up of three main components: Desktop for building reports, Service for publishing and collaborating in the cloud, and Mobile for viewing content on phones and tablets. Each piece serves a different stage of the workflow, from authoring to consumption.
- **Licensing Tiers**
  - Power BI is offered through a few licensing tiers: Free, Pro, Premium Per User, and Premium capacity, each unlocking a different set of features and limits. Free covers basic report building and viewing, Pro adds sharing and collaboration, and the Premium tiers add larger dataset sizes, more frequent refreshes, and dedicated capacity for an organization.
- **Installing Power BI**
  - Installing Power BI Desktop involves downloading it from the Microsoft Store or the Power BI website and running the setup file; most users require no special configuration. The Service and Mobile app do not need to be installed in the same sense: the Service runs in a browser, and Mobile is installed like any other app from an app store.

### 1.2 Data Source Types
- **Desktop**
  - Power BI Desktop is the free Windows application used to connect to data sources, transform data with Power Query, build the data model, write DAX measures, and design report pages. Most of the development work happens here before a file is published to the Power BI Service.
- **Files**
  - Power BI can import data directly from files such as Excel workbooks, CSV files, text files, XML, JSON, and PDF tables. File-based sources are common for smaller or ad hoc datasets that are not stored in a formal database.
- **Databases**
  - Power BI connects to relational and analytical databases such as SQL Server, PostgreSQL, MySQL, and Oracle through native connectors. These connectors typically support both import and DirectQuery modes, letting the choice depend on data volume and refresh needs.
- **Clouds**
  - Power BI includes connectors for cloud platforms such as Azure, Google services, Amazon Web Services, and Salesforce. These connectors handle the authentication and data structure specific to each cloud provider, so users do not need to write custom code to reach the data.
- **APIs**
  - Power BI can pull data from web APIs that return structured data, usually in JSON or XML format, using the web connector or custom M queries. This lets reports pull in live data from services that expose an API endpoint, such as internal systems or SaaS platforms.
- **Service**
  - Power BI Service is the cloud-based platform, accessed through a browser, where published reports live. It handles workspaces, sharing, scheduled refresh, dashboards, and collaboration features that Desktop alone cannot provide.
- **Mobile**
  - Power BI Mobile is the app for iOS and Android that lets users view reports and dashboards on their phone or tablet. It supports touch-optimized layouts, offline caching of recently viewed reports, and alerts when a metric crosses a threshold.

### 1.3 Connection Modes
- **Import Mode**
  - Import mode loads a copy of the source data into Power BI's own compressed in-memory storage, called VertiPaq. Once imported, report visuals query this local copy, which makes interactions fast regardless of the original source's speed.
- **DirectQuery**
  - DirectQuery is a connection mode where Power BI sends queries directly to the source database each time a report visual is viewed or filtered, rather than storing a copy of the data. This keeps the report always in sync with the source but depends on the source database's performance to respond quickly.
- **Direct Lake**
  - Direct Lake is a storage mode built for Microsoft Fabric that reads data directly from files in a data lake without importing or duplicating it, while still delivering query speed close to Import mode. It avoids the usual DirectQuery performance penalty because it reads the lake's columnar file format natively.
- **Dual Storage Mode**
  - Dual storage mode lets a table be configured to use both Import and DirectQuery, switching between them depending on the type of query Power BI needs to run. It is commonly used for large fact tables where recent data stays in DirectQuery for freshness while historical data is imported for speed.

### 1.4 Power Query
- **Applied Steps**
  - Applied Steps is the panel in Power Query that lists every transformation applied to a query, in the order they were performed. Each step can be renamed, edited, reordered, or deleted, which makes it possible to build a query gradually and adjust earlier steps without starting over.
- **Data Types & Casting**
  - Setting data types in Power Query tells Power BI how to interpret each column, such as whole number, decimal, date, or text. Correct typing affects both storage size and what operations are available later, since date functions or numeric aggregations only work if the column has the matching type.
- **Data Profiling**
  - Data profiling in Power Query shows statistics about a column's contents, such as the distribution of values, the percentage of errors, and the percentage of empty values. It helps catch data quality problems before they reach the model, like unexpected nulls or outliers.
- **Removing Duplicates**
  - Removing duplicates in Power Query eliminates rows that repeat identical values across selected columns, keeping the dataset clean for accurate counts and aggregations. This is done through a built-in step that compares rows and drops repeats, based on the columns chosen for comparison.
- **Handling Errors**
  - Power Query flags rows where a transformation fails, such as a text value that cannot convert to a number, and marks them as errors rather than stopping the whole query. These errors can be removed, replaced with a default value, or kept for review, depending on how the discrepancy should be handled.

### 1.5 M Language Basics
- **Changing Text**
  - Power Query includes text transformation functions for tasks like changing case, trimming whitespace, extracting substrings, and replacing characters within a column. These operations are common when cleaning inconsistent text data coming from different sources, such as mismatched capitalization or extra spaces.
- **Changing Numbers**
  - Numeric transformations in Power Query cover operations like rounding, changing sign, calculating percentages, and applying arithmetic between columns. These are used to standardize numeric data or derive new values, such as converting a raw amount into a percentage of total.
- **Changing Dates**
  - Date transformations in Power Query let users extract parts of a date, such as year, month, or day of week, and calculate differences between dates. This is useful for building time-based fields needed later in reports, like fiscal year or quarter.
- **Conditional Columns**
  - Conditional columns let a user create a new column based on if-then-else logic applied to existing columns, without writing M code by hand. The interface lets you define multiple conditions and their corresponding outputs, similar to a nested if statement.
- **Custom Columns**
  - Custom columns are new columns created in Power Query using a formula written in the M language, giving more flexibility than the conditional column builder. They allow calculations that reference multiple columns or use M functions not exposed in the standard UI.
- **Advanced Editor**
  - The Advanced Editor is a text view in Power Query that shows and lets users directly edit the full M code behind a query. It is used to write custom logic, fix errors that the interface cannot show clearly, or copy queries between files.

### 1.6 Schema Design
- **Splitting Columns**
  - Splitting columns divides a single column into multiple columns, based on a delimiter, a fixed number of characters, or by position. This is useful for cases like separating a full name into first and last name, or breaking apart a combined date and time field.
- **Joins**
  - Joins in Power Query, called merges, combine two tables side by side based on matching values in one or more key columns. Users choose a join type such as inner, left outer, right outer, or full outer, which determines which rows are kept when matches are found or missing.
- **Appending Tables**
  - Appending tables stacks two or more tables with matching columns on top of each other, combining their rows into a single table. It works like a union in SQL and is common when combining monthly files or data pulled from multiple similar sources into one query.
- **Star vs Snowflake Schema**
  - A star schema connects a central fact table directly to each dimension table, keeping dimensions flat and denormalized. A snowflake schema instead breaks dimensions into further related sub-tables, normalizing them, which adds extra joins the model has to traverse.
- **Facts & Dimensions**
  - Fact tables hold measurable, numeric data such as sales amounts or transaction counts, usually at a fine level of detail with many rows. Dimension tables hold descriptive attributes, like product names or customer regions, that get connected to facts through relationships and used to filter or group them.
- **Granularity**
  - Granularity refers to the level of detail represented by each row in a fact table, such as one row per transaction versus one row per day. Choosing the right granularity affects both performance and what kinds of calculations are possible, since aggregating up is easier than breaking data down further after the fact.

### 1.7 Relationships
- **Pivot & Transpose**
  - Pivoting turns unique values in one column into multiple new columns, reshaping data from a long format into a wide format, while transpose flips rows into columns and vice versa entirely. These operations are used to reshape data that arrives in a structure unsuited for reporting, such as a table where dates run down instead of across.
- **Parameters & Functions**
  - Parameters in Power Query are named values that can be reused across queries, such as a file path or a date range, making it easy to update many queries at once by changing a single value. Custom functions extend this by wrapping a query into a reusable block of logic that can be called with different inputs.
- **Relationships and Cardinality**
  - Cardinality describes the relationship between the number of matching rows on each side of a relationship, such as one-to-many, many-to-many, or one-to-one. Power BI needs to know the cardinality to correctly propagate filters between tables.
- **Cross Filter Direction**
  - Cross filter direction determines whether filtering flows only from the one side to the many side of a relationship, or in both directions. Single direction is the default and usually the safer choice, while bidirectional filtering is used carefully in specific cases like many-to-many relationships.

---

## 2. Intermediate

### 2.1 Model Objects
- **Query Folding**
  - Query folding is when Power Query translates its transformation steps back into a query that runs on the source system, such as SQL, instead of pulling all the raw data and transforming it locally. This pushes the processing work to the source, which is usually faster and lighter on memory.
- **Incremental Refresh**
  - Incremental refresh configures a dataset to only reload recent data on each refresh, rather than reprocessing the entire history every time. It uses date-based partitions defined with parameters, refreshing a small recent window while leaving older partitions untouched.
- **Calculated Tables & Columns**
  - Calculated tables and columns are new tables or columns created using DAX formulas rather than loaded directly from a data source. They are computed at data refresh time and stored in the model, unlike measures which calculate on the fly when a visual is rendered.
- **Hierarchies**
  - A hierarchy in the data model groups related columns into a drill path, such as Year, Quarter, Month, and Day, so users can navigate from a summary level down to detail in a single visual. Hierarchies are built by dragging one column onto another in the model view or fields pane.
- **Aggregations**
  - Aggregations in Power BI store pre-summarized versions of a large, detailed table, allowing queries at high summary levels to hit the smaller aggregated table instead of the full detail. This speeds up report performance significantly for very large DirectQuery or Import datasets.

### 2.2 Model Optimization
- **Performance Analyzer**
  - Performance Analyzer is a built-in Power BI Desktop tool that records how long each visual takes to render, broken down by DAX query time, visual display time, and other processing. It helps pinpoint whether a slow report is caused by an inefficient measure, a heavy visual, or the underlying data model.

### 2.3 Fundamentals
- **DAX vs. M Language**
  - DAX and M serve different purposes in Power BI: M transforms and shapes data before it is loaded into the model, while DAX calculates values within the model itself, used for measures, calculated columns, and calculated tables. M operates on the whole table during a query or refresh, whereas DAX often calculates based on the current filter context in a report.
- **DAX Syntax**
  - DAX syntax follows a formula structure similar to Excel, starting with a name and an equals sign, followed by functions and references to columns or tables written in a specific notation. Table names are typically written in plain reference and column references use the table name followed by the column name in brackets.
- **Columns vs Measures**
  - Calculated columns compute a value for every row in a table and store the result physically in the model, while measures calculate a value on the fly based on the current filter context of a visual. Columns are useful when a value needs to be sliced or filtered on directly, while measures are used for aggregations that should respond dynamically to whatever is selected in a report.
- **Aggregation Functions**
  - Aggregation functions in DAX, such as SUM, AVERAGE, COUNT, and MIN, combine values across rows into a single number. They form the basis of most measures, often summing or averaging a column across whatever rows are visible given the current filter context.
- **Logical Functions**
  - Logical functions in DAX, such as IF, AND, OR, and SWITCH, evaluate conditions and return different results depending on whether they are true or false. They are used to build conditional logic within a measure or calculated column, similar to conditional statements in other languages.
- **Variables in DAX**
  - Variables in DAX, defined with VAR and used with RETURN, let a formula store an intermediate result and reuse it later in the same expression instead of recalculating it. This improves both readability, since the logic is broken into named steps, and performance, since the value is computed only once.

### 2.4 Context & Filtering
- **Row vs Filter Context**
  - Row context is the context that exists when a formula evaluates one row at a time, such as inside a calculated column or an iterator function, while filter context is the set of filters currently applied from visuals, slicers, and other measures. A single formula can be affected by both at once, and confusing the two is a frequent source of unexpected results.
- **CALCULATE Function**
  - CALCULATE is the function in DAX that modifies the filter context under which an expression is evaluated, by adding, removing, or replacing filters. It underlies most non-trivial DAX formulas, including time intelligence functions, which are internally built using CALCULATE with date-based filter arguments.
- **Context Transition**
  - Context transition happens when CALCULATE turns the current row context into an equivalent filter context, which occurs whenever CALCULATE is used inside a row context, such as within a calculated column. This mechanism explains behavior that otherwise seems inconsistent, like a measure returning different results depending on where it is called from.
- **Iterator Functions**
  - Iterator functions in DAX, such as SUMX, AVERAGEX, and FILTER, loop through a table row by row, evaluating an expression for each row before combining the results. They are needed when a calculation cannot be expressed as a simple aggregation of an existing column, such as multiplying quantity by price for each row before summing.
- **Window Functions**
  - Window functions in DAX, like OFFSET, INDEX, and WINDOW, let a calculation reference rows relative to the current one within an ordered set, such as the previous row or a moving range. They are newer additions to DAX aimed at simplifying calculations that previously needed more complex workarounds, such as running totals or period-over-period comparisons.
- **Table Manipulation**
  - Table manipulation functions in DAX, such as FILTER, ALL, VALUES, and SUMMARIZE, return or transform entire tables rather than single values, which are then used inside other functions like calculations or iterators. They let a formula work with a modified version of a table, such as removing a filter or reducing it to unique values.
- **Time Intelligence**
  - Time intelligence functions in DAX, such as DATEADD, SAMEPERIODLASTYEAR, and TOTALYTD, handle calculations that compare or accumulate values across time periods. They rely on having a proper date table marked as such in the model, with a continuous range of dates.

### 2.5 Advanced DAX
- **Quick Measures**
  - Quick measures are pre-built DAX calculations generated automatically through a dialog interface, covering common patterns like running totals, year-over-year change, or weighted averages. They are useful for users who need a common calculation without writing DAX from scratch, and the generated formula can be viewed and edited afterward.
- **Field Parameters**
  - Field parameters let report users switch which field or measure a visual displays through a slicer, without needing a separate visual for each option. They are implemented as a special calculated table that lists the available fields, referenced dynamically inside the visual.
- **Visual Calculations**
  - Visual calculations are a newer type of DAX calculation defined directly on a visual rather than in the model, evaluated on the data already aggregated and displayed in that visual. They simplify certain patterns, like running totals or rank within a visual, that would otherwise need more complex model-level DAX.
- **Calculation Groups**
  - Calculation groups let a set of DAX logic, such as time intelligence patterns, be applied to any measure without duplicating that logic per measure. Instead of writing separate year-over-year measures for every existing measure, a single calculation item can apply that transformation to whichever measure a user selects.
- **DAX Performance**
  - DAX performance concerns how efficiently a formula executes, influenced by factors like the choice between iterators and aggregations, the size of tables being filtered, and how CALCULATE's filters are constructed. Poorly written DAX can turn a simple report into a slow one, even on a small dataset.
- **Bar & Column Charts**
  - Bar and column charts represent values as horizontal or vertical bars, sized proportionally to the value they represent, making them well suited for comparing values across categories. Column charts are generally preferred for showing change over time, while bar charts work better with long category labels.
- **Line & Area Charts**
  - Line charts connect data points with a continuous line, making them the standard choice for showing trends over a continuous axis like time. Area charts are a variation that fills the space beneath the line, which can help emphasize volume or make it easier to compare multiple stacked series.
- **Pie & Donut Charts**
  - Pie and donut charts show how a total is divided into parts, with each slice sized proportionally to its share of the whole. They are best used with only a handful of categories, since too many slices become hard to read and compare accurately.

### 2.6 Visualization Basics
- **Accessibility**
  - Accessibility in Power BI covers making reports usable for people with visual, motor, or cognitive impairments, including features like keyboard navigation, screen reader support, and color choices that work for color blindness. Report authors can add alt text to visuals and check contrast ratios to meet these needs.
- **Scatter & Bubble Charts**
  - Scatter charts plot two numeric values against each other on separate axes, revealing relationships or clusters between the two variables. Bubble charts extend this by adding a third dimension, represented by the size of each point.
- **Combination Charts**
  - Combination charts overlay two different visual types, most commonly a column chart and a line chart, sharing the same category axis but often using separate value axes. They are used to compare two related measures with different scales, such as sales volume and profit margin, in a single visual.
- **Gauges, Cards, & KPIs**
  - Gauges, cards, and KPI visuals display a single value prominently, often compared against a target or goal. Cards show one number plainly, gauges represent it on a dial with a target marker, and KPI visuals combine a value, trend, and goal into one compact visual.
- **Matrix & Table Visuals**
  - Table visuals display data in rows and columns similar to a spreadsheet, while matrix visuals add the ability to group rows and columns into a pivot-table style structure with expandable hierarchies. Both are used when users need to see exact numbers rather than a visual summary, or need to drill into totals and subtotals.
- **Maps**
  - Map visuals plot data geographically, using either points on a map for specific locations or shaded regions for values tied to areas like states or countries. Power BI supports a few map types, including standard maps, filled maps, and ArcGIS-based maps for more advanced geographic analysis.
- **Custom Visuals**
  - Custom visuals are chart types built by Microsoft or third parties beyond the default set included in Power BI, imported from the AppSource marketplace or a local file. They extend what can be shown beyond the built-in visual gallery, covering things like specialized chart types or interactive widgets.
- **Design Principles**
  - Design principles in Power BI cover general practices for making reports clear and effective, such as using consistent color schemes, avoiding chart clutter, and prioritizing the most important information. Good design guides the viewer's attention to what matters rather than decorating the report unnecessarily.

### 2.7 Formatting & filtering
- **Formatting & Themes**
  - Formatting and themes control the visual appearance of a report, including colors, fonts, and visual styling, either set individually per visual or applied consistently across a whole report using a theme file. A theme is a JSON file that defines a color palette and style rules, letting an organization apply consistent branding across multiple reports at once.
- **Conditional Formatting**
  - Conditional formatting changes the appearance of values in a visual, such as cell background color in a table, based on rules tied to the underlying data. It is commonly used to highlight values above or below a target, using color scales, rules, or icons like arrows.
- **Sorting Data**
  - Sorting controls the order in which categories or rows appear within a visual, whether alphabetically, by value, or by a custom sort order defined through a separate sort-by column. Getting sort order right matters especially for categorical axes where a meaningful order, like months or a defined ranking, needs to be preserved rather than defaulting to alphabetical.
- **Slicers and Filters**
  - Slicers are visual controls placed directly on a report page that let viewers filter the data interactively, such as choosing a specific year or category. Filters serve a similar purpose but are configured through a separate filter pane and can apply at the visual, page, or entire report level rather than as a visible control.
- **Drill-through & Drill-down**
  - Drill-through lets a user right-click a data point and jump to a separate detail page filtered to that specific selection, while drill-down lets a user click into a hierarchy within the same visual to see a more granular level, like moving from year to month. Both give users a way to go from a summary view into more detail without cluttering the main report with every level at once.
- **Bookmarks**
  - Bookmarks capture the current state of a report page, including filters, slicer selections, and visual visibility, so that state can be restored later with a single click. They are often combined with buttons to build guided navigation, such as toggling between different views of the same data.

### 2.8 Interactivity
- **Buttons & Navigation**
  - Buttons in Power BI can trigger actions like navigating to another page, applying a bookmark, or opening a web URL, letting report builders create custom navigation beyond the default page tabs. This is commonly used to build a menu-style navigation system across a multi-page report.
- **Explore Feature**
  - The Explore feature lets report viewers open a visual into a larger, dedicated analysis view where they can add or remove fields, change the visual type, and dig deeper without editing the original report. It gives non-report-builders a way to do lightweight self-service analysis on top of an existing report.

### 2.9 Advanced Visuals
- **Custom Tooltips**
  - Custom tooltips replace the default hover text on a visual with a separate report page designed specifically to show extra detail, such as a small chart or additional metrics. They are built as a normal report page but marked as a tooltip page and sized accordingly.
- **Cross-filtering**
  - Cross-filtering is the default behavior in Power BI where clicking on a data point in one visual filters the other visuals on the same page automatically. It happens because visuals on a page interact with each other based on shared fields in the data model, without needing extra configuration.
- **Decomposition Tree**
  - The decomposition tree is a visual that lets users break down a total into its contributing parts across multiple dimensions, choosing which dimension to expand at each step or letting Power BI's AI find the highest or lowest contributing value automatically. It is used for root-cause style exploration, such as figuring out which product or region is driving a change in a metric.
- **Key Influencers**
  - The key influencers visual analyzes what factors are most strongly associated with a change in a chosen metric, using a statistical model behind the scenes to identify contributing variables. It ranks factors by their relative influence and shows how each one affects the outcome, such as which customer attributes are associated with churn.
- **Small Multiples**
  - Small multiples splits a single visual into a grid of smaller versions, one per category, all sharing the same axis scale for easy comparison. This lets users compare a trend or pattern across many categories at once without needing a separate visual for each one.
- **Q&A Visual**
  - The Q&A visual lets report viewers type a question in natural language and get an automatically generated chart in response, using Power BI's natural language query engine. It relies on well-named fields and synonyms configured in the model to correctly interpret what is being asked.

---

## 3. Advanced

### 3.1 Publishing & Sharing
- **Workspaces**
  - Workspaces are containers in the Power BI Service that hold related reports, dashboards, datasets, and dataflows, typically organized around a team or project. Access to a workspace is controlled through roles like admin, member, contributor, and viewer, which determine what each user can do inside it.
- **Publishing Reports**
  - Publishing a report uploads it from Power BI Desktop to a chosen workspace in the Service, making the report and its underlying dataset available in the cloud. Once published, the report can be shared, scheduled for refresh, and viewed through a browser without needing Desktop installed.
- **Dashboards vs Reports**
  - A report in Power BI is a multi-page collection of interactive visuals connected to a single dataset, while a dashboard is a single page of pinned tiles that can pull from multiple different reports and datasets. Dashboards are meant for a high-level, at-a-glance summary, while reports support deeper interactive exploration.
- **Sharing & Permissions**
  - Sharing and permissions control who can view or edit Power BI content, managed through workspace roles, direct sharing links, and row-level security for data-specific restrictions. Permissions can be set at different levels, from an entire workspace down to an individual report or dataset.
- **Apps**
  - Apps in Power BI package a workspace's reports and dashboards into a single, polished experience for end users to consume, without giving them access to the underlying workspace itself. They are published separately from the workspace and can be updated on a controlled schedule rather than reflecting every workspace change instantly.
- **Paginated Reports (RDL)**
  - Paginated reports are print-ready, pixel-perfect reports built with Report Builder and defined in RDL format, designed to render consistently across page sizes for printing or PDF export. Unlike regular Power BI reports, they are built for exact layout control rather than interactive exploration.

### 3.2 Data & Infrastructure
- **On-premises Data Gateway**
  - The on-premises data gateway is software installed on a local machine that lets the Power BI Service securely connect to data sources that live inside a private network, such as an on-premises SQL Server. It acts as a bridge, forwarding queries from the cloud to the source without exposing the source directly to the internet.
- **Refresh & Change Detection**
  - Refresh settings determine how often a dataset in the Service pulls updated data from its source, on a schedule or triggered manually. Change detection is a feature that checks a lightweight query first to see whether the underlying data has actually changed before running a full, more expensive refresh.

### 3.3 Collaboration
- **Subscriptions and Alerts**
  - Subscriptions send scheduled snapshots of a report or dashboard by email, while alerts notify a user when a specific metric on a dashboard tile crosses a threshold they define. Both features let users stay informed without needing to actively check the report themselves.

### 3.4 Access Control
- **Row-Level Security**
  - Row-level security restricts which rows of data a user can see within a report, based on rules defined in the data model and tied to the user's identity. Roles are set up in Power BI Desktop with DAX filter expressions, then assigned to specific users or groups in the Service.
- **Object-Level Security**
  - Object-level security restricts access to entire tables or columns in the data model, hiding them completely from certain users rather than just filtering rows. It is used when specific columns, like salary or other sensitive fields, should not be visible to some users at all, regardless of row-level filters.
- **Workspace Roles**
  - Workspace roles define what a user can do within a specific workspace, ranging from admin, with full control, down to viewer, with read-only access. These roles determine actions like who can publish new reports, manage workspace settings, or simply view existing content.

### 3.5 Governance
- **Sensitivity Labels**
  - Sensitivity labels classify Power BI content, such as reports or datasets, according to its confidentiality level, using the same labeling system as Microsoft Purview across other Microsoft 365 apps. These labels can carry protection settings, like restricting export or requiring encryption when the content is exported to a file.
- **Data Loss Prevention**
  - Data loss prevention policies scan Power BI content for sensitive information, such as credit card numbers or personal data, and can flag or block reports that expose it inappropriately. These policies typically integrate with Microsoft Purview's broader data loss prevention framework used across Microsoft 365.
- **Tenant Settings**
  - Tenant settings are organization-wide configuration options managed by Power BI administrators, controlling things like whether users can share content externally, use certain features, or install custom visuals. These settings apply across the entire organization rather than a single workspace.
- **Audit Logs**
  - Audit logs record user activity across the Power BI tenant, such as who viewed, edited, or shared specific content and when. Administrators use these logs to investigate security incidents, monitor usage patterns, or meet compliance requirements.
- **Certified Datasets**
  - Certified datasets are datasets that have been reviewed and approved by a designated authority within an organization, marked with a badge that signals to other users that the data is trustworthy and ready for reuse. Certification helps prevent duplicate, inconsistent versions of the same dataset from spreading across an organization.

### 3.6 Workflow & Lifecycle
- **Power Automate**
  - Power Automate integrates with Power BI to trigger automated workflows based on events in a report, such as a button click that kicks off an approval process or sends a notification. It connects Power BI to hundreds of other services and apps without needing custom code.
- **Deployment Pipelines**
  - Deployment pipelines let teams manage separate development, test, and production environments for their Power BI content, promoting reports and datasets through each stage in a controlled way. This mirrors common software development practices, catching issues in a test environment before they reach production users.

### 3.7 Integrations
- **REST API**
  - The Power BI REST API lets developers interact with Power BI programmatically, covering tasks like refreshing a dataset, managing workspace content, or embedding reports, without using the standard user interface. It is commonly used to automate repetitive administrative tasks or integrate Power BI actions into custom applications.
- **Power BI Embedded**
  - Power BI Embedded lets developers embed Power BI reports and dashboards into their own applications or websites, using a dedicated Azure capacity rather than requiring end users to have their own Power BI license. It is aimed at software vendors who want to include analytics inside their own product.
- **Power BI with Excel**
  - Power BI integrates with Excel in a couple of directions: Excel workbooks can connect to a Power BI dataset to analyze it using PivotTables, and Power BI reports can be exported to Excel for further ad hoc analysis. This lets users work in whichever tool suits a particular task while sharing the same underlying data.
- **Python & R**
  - Power BI supports using Python and R scripts both inside Power Query for data transformation and as visuals for custom charts not available in the standard visual gallery. This requires a local Python or R installation and library setup on the machine running Desktop.
- **Microsoft Fabric**
  - Microsoft Fabric is Microsoft's unified data platform that brings together data engineering, data warehousing, and data science alongside Power BI, all built on a shared storage layer called OneLake. Power BI datasets within Fabric can use Direct Lake mode to query data stored in OneLake without a separate import step.

---

## 4. Optional / Specialized Topics

- APIs
- Service
- Mobile
- Handling Errors
- Custom Columns
- Advanced Editor
- Facts & Dimensions
- Granularity
- Aggregations
- Logical Functions
- Variables in DAX
- Window Functions
- Table Manipulation
- Time Intelligence
- DAX Performance
- Bar & Column Charts
- Line & Area Charts
- Pie & Donut Charts
- Matrix & Table Visuals
- Maps
- Custom Visuals
- Design Principles
- Drill-through & Drill-down
- Bookmarks
- Small Multiples

---

## 5. References

- [Power BI Roadmap](https://roadmap.sh/power-bi)

---

## 6. Related Roles / Topics

### Related Roles
- BI Analyst
- Data Analyst
- AI and Data Scientist

### Related Skills
- Python for Data Analysis