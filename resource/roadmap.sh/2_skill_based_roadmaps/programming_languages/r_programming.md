# R Programming

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/r-programming
- Related Roles:
  - Data Analyst
  - AI Engineer
  - Data Engineer
  - AI and Data Scientist
  - BI Analyst

---

## 1. Beginner

### 1.1 Introduction
- **R vs Python**
  - R and Python solve overlapping problems but come from different roots. R grew out of statistics departments, so its core language and packages treat data frames, vectors, and statistical models as first-class citizens.
- **Installing R**
  - Installing R involves downloading the base software environment from the Comprehensive R Archive Network (CRAN) and executing the installer for your specific operating system. This process sets up the core language engine, allowing you to run R scripts, manage packages, and perform statistical computations directly on your computer.
- **Your First R Script**
  - A first R script is usually a short file with a few lines of code, like assigning a variable and printing it, run to confirm your R installation actually works. Writing and running this first script is where syntax stops being abstract and starts being something you can see execute.
- **CRAN**
  - CRAN, the Comprehensive R Archive Network, is R's official package repository, hosting tens of thousands of vetted packages. Packages published on CRAN go through basic automated checks before release, giving them a baseline level of reliability.
- **Installing Packages**
  - Installing packages adds functionality to R beyond what comes built in, using the base function install.packages() to download and install from CRAN. Running install.packages("dplyr"), for example, fetches the dplyr package and its dependencies.

### 1.2 Setting Up
- **renv**
  - renv manages package versions on a per-project basis instead of one shared library for your whole machine. It records the exact package versions a project uses in a lockfile, so anyone who opens that project later can restore the exact same environment.
- **pak**
  - pak is a newer package installer for R designed to replace install.packages() with something faster and more reliable. It parallelizes downloads, caches packages locally so reinstalls are quicker, and gives clearer error messages when a dependency conflict occurs.
- **RStudio**
  - RStudio is the most established integrated development environment for R, combining a script editor, console, plot viewer, and package tools in one window. It has deep, mature support for building R packages and rendering Quarto or R Markdown documents.

### 1.3 Basic Syntax
- **Operators**
  - Arithmetic operators handle basic math, like +, -, , and /. Relational operators compare values and return a logical result, like == and <.
- **Creating Variables**
  - Creating a variable stores a value under a name so you can reuse it later, most commonly using the <- assignment operator, though = also works in most contexts. Once assigned, a variable holds its value until you reassign or remove it.
- **Comments**
  - Comments start with # and are ignored when R runs the code, letting you leave notes explaining what a piece of code does or why. They don't affect how a script executes, but they make code easier to understand later, whether for someone else or for yourself after time has passed.
- **Conditional Statements**
  - Conditional statements let code branch based on whether something is true or false, using if, else if, and else. R evaluates the condition, runs the matching block, and skips the rest.
- **Loops**
  - A for loop repeats a block of code once for each element in a vector or list. A while loop repeats as long as a condition stays true, useful when you don't know in advance how many iterations you'll need.
- **Positron**
  - Positron is a newer IDE from Posit, built on the same underlying technology as VS Code but tailored for data science work in R and Python. It combines a modern, extensible editor with the data-focused features R users expect, like a variables pane and integrated plots.
- **VS Code**
  - VS Code is a general-purpose code editor from Microsoft that supports R through extensions rather than built-in features. It fits projects where R is just one part of a larger codebase involving other languages, since it shares one consistent editor across all of them.
- **Pipe**
  - The pipe operator takes the result on its left and passes it as the first argument to the function on its right, letting you chain several operations in a readable, top-to-bottom sequence. R now has two common versions: the native pipe |>, built into base R since version 4.1, and the older magrittr pipe %>%, which predates it and is still common in existing code.
- **Quarto**
  - Quarto is a publishing system that renders documents combining text, code, and code output into formats like HTML, PDF, or Word. It works across multiple languages, including R, Python, and Julia, and is positioned as the modern successor to R Markdown.
- **R Markdown**
  - R Markdown documents mix Markdown-formatted text with chunks of R code, rendering into HTML, PDF, or Word output with the code's results embedded directly. It predates Quarto and was the standard tool for this kind of work for many years, so a large amount of existing documentation and tutorials still use it.

### 1.4 Data Types
- **Numeric**
  - Numeric is R's default type for numbers with decimal points, such as 3.14 or 2.0, stored internally as double-precision floating point values. Almost all arithmetic in R produces numeric results unless you explicitly ask for integers.
- **Integer**
  - Integers are whole numbers stored more compactly than numeric values, created by appending an L to a number, like 5L. They matter when memory efficiency counts, since integers take up less space than numeric doubles.
- **Character**
  - Character is R's type for text, written inside single or double quotes, like "hello". R provides many built-in and package functions for searching, splitting, and reformatting text stored this way.
- **Logical**
  - Logical values represent true or false, written as TRUE and FALSE. They result from comparisons like 5 > 3 and drive conditional logic throughout R code, such as if statements and filtering rows in a data frame.
- **Complex**
  - Complex numbers combine a real and imaginary part, written in R as something like 3+2i. They come up in specialized mathematical work, such as signal processing, but most day-to-day data analysis never touches them directly.
- **Vectors**
  - A vector is R's most basic data structure: an ordered collection of values that all share the same type. Nearly everything in R is built on vectors, including single values, which R treats as vectors of length one.

### 1.5 Type Conversion
- **Matrices**
  - A matrix is a two-dimensional grid of values, all of the same type, arranged in rows and columns. Matrices support standard linear algebra operations like multiplication, transposition, and inversion, making them the natural structure for mathematical computation in R.

### 1.6 Data Structures
- **Arrays**
  - An array generalizes a matrix to more than two dimensions, storing values of a single type across any number of dimensions you specify. Arrays are less common in everyday data analysis than vectors or data frames, but they appear in specialized numerical and scientific computing contexts.
- **Factors**
  - A factor represents categorical data, storing a fixed set of possible values called levels, such as "low", "medium", "high". Internally, R stores factors as integers mapped to those level labels, which is more memory-efficient than storing the same category repeatedly as text.
- **Lists**
  - A list is a flexible container that can hold elements of different types and lengths in a single object, unlike a vector, which requires uniform type. A single list might hold a character string, a numeric vector, and a data frame all at once.
- **Data Frames**
  - A data frame is R's standard structure for tabular data, organized into rows and columns where each column can hold a different type but all values within a column share the same type. It's the structure you'll use for almost any real dataset loaded into R, whether from a CSV file, a database, or an API.
- **Data Tables**
  - A data table is the structure provided by the data.table package, built specifically for fast, memory-efficient operations on large datasets. It extends the data frame with a more concise syntax and internal optimizations that make filtering, grouping, and joining noticeably faster on big data.

### 1.7 Functions
- **Tibbles**
  - A tibble is a modern variant of the data frame, introduced by the tidyverse, with a few behavioral differences designed to reduce surprises. Tibbles print more usefully in the console, showing only what fits on screen along with each column's type, and they refuse to silently drop dimensions the way base data frames sometimes do.
- **Arguments & Defaults**
  - Function arguments are the inputs a function accepts, and default values let you specify what an argument should be if the caller doesn't provide one. Writing function(x, na.rm = FALSE) means na.rm defaults to FALSE unless the caller overrides it.
- **Scopes**
  - Scoping determines which variables a function can see and use while it runs. R uses lexical scoping, meaning a function looks first inside itself, then in the environment where it was defined, not the environment where it was called from.
- **Recursion**
  - Recursion is when a function calls itself, typically to break a problem into smaller versions of the same problem until it reaches a simple base case. A classic example is calculating a factorial by having the function call itself with a smaller number each time.
- **Apply Family**
  - The apply family is a set of base R functions that apply another function to every element of a vector, list, or data structure, replacing many uses of explicit loops. lapply() always returns a list, sapply() tries to simplify the result into a vector or matrix, and vapply() works like sapply() but requires specifying the expected output type in advance.

---

## 2. Intermediate

### 2.1 Error Handling
- **CSV**
  - CSV files store tabular data as plain text with values separated by commas, making them one of the most universal formats for exchanging data between tools. Base R can read them with read.csv(), though readr's readcsv() is faster and handles more edge cases well, such as inconsistent column types or unusual encodings.
- **Debugging**
  - Debugging means finding out why code isn't behaving as expected, using tools like browser(), which pauses execution at a specific line so you can inspect variables, and traceback(), which shows the sequence of function calls leading up to an error. RStudio and Positron both provide visual debugging tools built on top of these, including breakpoints you can set by clicking in the editor.
- **tidyverse**
  - The tidyverse is a collection of R packages designed to work together around a shared philosophy and consistent syntax for data science tasks. It includes packages for data manipulation, visualization, string handling, and more, all built to interoperate smoothly with the pipe operator.
- **ggplot2**
  - ggplot2 is the tidyverse's plotting package, built around the grammar of graphics, which describes any plot as a combination of data, a coordinate system, and layered elements mapped to aesthetics like position or color. Instead of choosing a fixed chart type, you build a plot by combining these pieces, which is why the same approach can produce scatterplots, bar charts, or complex faceted layouts.
- **dplyr**
  - dplyr provides a small set of verbs for the most common data manipulation tasks: filtering rows, selecting columns, arranging order, and summarizing groups. These verbs are designed to read almost like plain English, making dplyr code easier to follow than equivalent base R code.

### 2.2 Importing Data
- **Text**
  - Plain text files store unstructured or loosely structured data without the strict comma or tab delimiters of a CSV or TSV file. Reading them into R might mean reading line by line for further parsing, or using a delimiter-aware function if the text has some consistent structure like tab separation.
- **Excel**
  - Excel files store data in a binary or XML-based format that differs from plain text files, often including multiple sheets and formatting within a single file. R doesn't read them with base functions, so packages like readxl are needed to extract the underlying data into a usable data frame.
- **APIs**
  - Web APIs let you request data over the internet from another service, typically returning it in JSON format. Fetching data from an API in R usually means making an HTTP request with a package like httr, then parsing the response.
- **Web Scraping**
  - Web scraping extracts data directly from a website's HTML when that data isn't offered through a proper API or downloadable file. The rvest package reads a webpage's HTML and lets you select specific elements using CSS selectors or XPath, pulling out text, tables, or links.
- **JSON**
  - JSON is a structured text format built around nested key-value pairs, commonly returned by web APIs. Parsing it in R usually means using a package like jsonlite to convert the response into R data structures.
- **tidyr**
  - tidyr handles reshaping data between different layouts, most notably converting between wide and long formats with pivotlonger() and pivotwider(). Many statistical functions and ggplot2 specifically expect data in a particular shape, so tidyr often bridges the gap between how data is stored and how it needs to look for analysis or plotting.
- **readr**
  - readr provides fast, consistent functions for reading flat files like CSVs into R, such as readcsv(), as an improvement over base R's equivalent functions. It handles more edge cases well, like inconsistent column types or unusual encodings, and gives clearer feedback about how it parsed each column.
- **lubridate**
  - lubridate makes working with dates and times considerably easier than base R alone. Functions like ymd(), mdy(), and dmy() parse dates written in different common formats without requiring a manually specified format string.
- **purrr**
  - purrr applies a function to each element of a list or vector and collects the results, similar in spirit to base R's apply family but with more consistent, predictable behavior. Its map() function always returns a list, while variants like mapdbl() return a vector of a specific type, making the expected output explicit.
- **tibble**
  - tibble is the tidyverse package that defines and supports the tibble data structure, a modern variant of the data frame. It provides functions for creating tibbles directly, converting existing data frames into tibbles, and controlling how they print in the console.
- **stringr**
  - stringr provides a consistent, well-documented set of functions for working with text, covering tasks like detecting patterns, extracting substrings, and combining strings. Every function follows a consistent naming pattern starting with str, such as strdetect() or strreplace(), making the package easier to learn than base R's more scattered string functions.
- **forcats**
  - forcats provides tools for working with factors, R's data type for categorical variables, making common tasks like reordering levels or lumping rare categories together more straightforward than base R. Functions like fctreorder() let you control the order categories appear in plots and tables, which matters since default factor ordering is often alphabetical rather than meaningful.

### 2.3 Data Cleaning
- **Filter, Query, Arrange**
  - Filtering keeps rows matching a condition, querying more broadly covers selecting the specific subset of data you need, and arranging sorts rows by one or more columns. In dplyr, these map to filter() and arrange(), both designed to read almost like plain English.
- **Mutate & Transform**
  - Mutating adds new columns or changes existing ones in a data frame, calculating values across every row based on an expression you specify. Multiple new columns can be created in a single step, with later columns able to reference ones created earlier in the same step.
- **Group By & Summarize**
  - Grouping splits a data frame into groups based on one or more columns, and summarizing then collapses each group down to a single summary row, such as a group's average or count. Together they replace the need for manual loops when calculating statistics per category, like average sales per region.
- **Parsing Dates**
  - Parsing dates handles the extra complexity of date formats, since something like "01/02/2024" could mean different things depending on locale conventions. Getting the format specification right, or using a package like lubridate that guesses common formats automatically, avoids silently misreading dates.
- **Encoding Categories**
  - Encoding categories turns text labels into R's factor type, giving categorical data the structure needed for modeling and certain visualizations. It also involves deciding on the order categories should follow, since default alphabetical ordering isn't always meaningful.
- **Casting Types**
  - Casting converts a column to the correct type, such as turning character "42" into the numeric value 42. Data often arrives in the wrong type for analysis, especially numbers or dates stored as plain text.

### 2.4 Data Manipulation
- **Window Functions**
  - Window functions calculate a value for each row based on a set of related rows, without collapsing the data the way summarizing does. Ranking each row within its group, calculating a running total, or comparing a row's value to the previous row are all window function tasks.
- **Joins**
  - Joins combine two data frames based on matching values in one or more shared columns, similar to joins in SQL. An inner join keeps only rows with matches in both tables, a left join keeps all rows from the first table and fills in matches where available, and a full join keeps all rows from both regardless of matches.
- **Map Functions**
  - Map functions apply a function to every element of a list or vector and collect the results, avoiding the need for an explicit loop. purrr's map() always returns a list, while variants like mapdbl() return a vector of a specific type, making the expected output explicit.
- **Working with Data Tables**
  - Working with data tables means using the data.table package's syntax and conventions for fast, memory-efficient data manipulation on large datasets. It uses a distinctive bracket-based syntax, dt[i, j, by], differing from both base R indexing and dplyr's verb-based approach.
- **Reshaping**
  - Reshaping changes the layout of a dataset without changing its underlying content, most commonly converting between wide and long formats. Wide format spreads related values across separate columns, while long format stacks them into fewer columns with an extra column identifying what each value represents.
- **isnull, isna**
  - Detecting missing values in R relies on is.na(), since direct comparison like NA == NA doesn't return TRUE the way you might expect. This function returns a logical vector marking which values are missing, which can then be summed to count them or used to filter rows.
- **Dropping vs. Imputing**
  - Once missing values are found, you have to decide whether to drop rows containing them, which is simple but can lose real information, or impute them, replacing missing values with an estimate like the column mean. The right choice depends heavily on why the data is missing and how much of it there is.
- **Forward / Backward Fill**
  - Forward and backward fill are common in time series data, carrying the last known value forward or the next known value backward to fill gaps. This assumes a value likely stayed the same or is reasonably close to nearby recorded values.
- **strip, replace, split**
  - Stripping removes leading or trailing whitespace from text, replacing swaps out unwanted characters or patterns for something else, and splitting breaks a single string into multiple parts based on a delimiter. These are usually among the first steps in cleaning any dataset with free-text or inconsistently formatted columns.

### 2.5 Strings and Dates
- **String Manipulation**
  - String manipulation covers searching, extracting, replacing, and combining text values, most commonly using the stringr package's consistent str functions. Text data shows up constantly in real datasets: names, categories, free-text responses.
- **Regular Expressions**
  - Regular expressions are a pattern-matching language for describing sequences of characters, used to search, validate, or extract specific pieces of text. A pattern like ^\d{3}-\d{4}$ might describe a phone number format, matching only text that fits that exact shape.
- **R Dates & Times**
  - Base R represents dates and times using specific classes: Date for calendar dates and POSIXct for date-times that include a time component. These classes let you do arithmetic directly, like subtracting two dates to get the number of days between them.
- **IQR**
  - The IQR method for detecting outliers flags values that fall well below or above the interquartile range, the range between the 25th and 75th percentile of the data. It's a robust approach, less sensitive to extreme values than methods based on the mean and standard deviation.
- **Visual Inspection**
  - Visual inspection uses plots, most often boxplots or scatterplots, to spot outliers by eye rather than through a fixed numeric rule. This often reveals context that purely numeric methods miss, such as whether an unusual value looks like a data entry error or a genuine rare event.
- **Z-score**
  - The Z-score method flags values a certain number of standard deviations away from the mean, commonly using a threshold like 2 or 3. It works well for roughly normally distributed data, but poorly for data that's heavily skewed, since the mean and standard deviation themselves get distorted by skew.

### 2.6 Exploratory Data Analysis
- **Summary Statistics**
  - Summary statistics condense a column of data down to a few representative numbers, like the mean, median, and standard deviation. They form the foundation for almost every deeper statistical technique, since you need to understand a variable's basic behavior before modeling relationships involving it.
- **Distribution Analysis**
  - Distribution analysis looks at how values in a dataset are spread across their range, most commonly using histograms and boxplots. A histogram groups values into bins and shows how many observations fall into each, revealing shape characteristics like skewness.
- **Relationship Analysis**
  - Relationship analysis examines how two or more variables relate to each other, using tools like scatterplots for two numeric variables, correlation matrices for many numeric variables at once, and cross-tabulation for categorical variables. This is usually the second step in exploratory analysis, after looking at variables individually.

### 2.7 Base R Plotting
- **Base R Plotting**
  - Base R includes plotting functions like plot(), hist(), and boxplot() that don't require any additional package. They're quick to use for a fast look at data and require no setup.

### 2.8 ggplot2
- **Grammar of Graphics**
  - The grammar of graphics is the conceptual framework ggplot2 is built on, describing any plot as a combination of data, a coordinate system, and layered geometric elements mapped to aesthetics. Instead of choosing a fixed chart type, you build a plot by combining these pieces, which is why the same underlying approach can produce scatterplots, bar charts, or complex layouts using consistent syntax.
- **Aesthetic Mappings**
  - Aesthetic mappings connect columns in your data to visual properties of a plot, like position, color, size, or shape. Writing aes(x = year, y = revenue, color = region) tells ggplot2 to plot year against revenue and color each point by region.
- **Common Plots**
  - Common plot types include line plots for trends over time, bar plots for comparing quantities across categories, histograms for showing the distribution of a single numeric variable, and boxplots for summarizing spread and outliers. Each type suits a different kind of question about the data.
- **Overplotting Techniques**
  - Overplotting happens when too many data points overlap on a plot, making it hard to see the true density or pattern, especially common with large datasets. Jittering adds small random noise to point positions to spread out overlapping points slightly.
- **Faceting & Themes**
  - Faceting splits a single plot into a grid of smaller plots, one for each level of a categorical variable, making it easy to compare patterns across groups side by side. Themes control the overall visual styling of a plot, like background color, gridlines, and font sizes.
- **Best Practices**
  - Good data visualization practice means choosing chart types and design choices that communicate data accurately rather than misleadingly. Common anti-patterns include truncated axes that exaggerate differences and color choices that aren't accessible to colorblind viewers.

### 2.9 Dashboards
- **Shiny**
  - Shiny is a framework for building interactive web applications directly in R, without needing to know HTML, CSS, or JavaScript. An app has two main parts: a UI defining what the user sees, and a server function defining how the app responds when the user interacts with those elements.
- **Power BI / Tableau**
  - Power BI and Tableau are business intelligence tools for building dashboards, connecting to data sources and creating interactive visualizations largely through a visual interface rather than code. R can connect to both, either as a data source feeding into them or, in Power BI's case, running R scripts directly inside the tool for custom visuals or calculations.

---

## 3. Advanced

### 3.1 Interactive Plots
- **plotly**
  - plotly creates interactive charts that let viewers hover, zoom, and filter directly in the browser. It can convert many existing ggplot2 plots into interactive versions with a single function call, or build interactive charts directly with its own syntax.
- **Descriptive Statistics**
  - Descriptive statistics summarize the basic characteristics of a dataset: central tendency, spread, and shape. They form the foundation for almost every deeper statistical technique, since you need to understand a variable's basic behavior before modeling relationships involving it.

### 3.2 Statistical Analysis
- **Probability Distributions**
  - A probability distribution describes how likely different outcomes are for a random variable, such as the normal distribution or the binomial distribution for counting successes in repeated trials. R provides functions for common distributions following a consistent naming pattern: d for density, p for cumulative probability, q for quantiles, and r for random generation.
- **Sampling**
  - Sampling covers the different methods for selecting a subset of a population to study, when studying the entire population isn't feasible, including simple random, stratified, and cluster sampling. It also covers the mechanics of random number generation in R and setting a seed for reproducibility.
- **Correlation**
  - Correlation measures the strength and direction of a linear relationship between two numeric variables, expressed as a single number between negative one and positive one. A value near positive one means the variables tend to increase together, and near zero means little linear relationship exists.
- **stats**
  - stats is the base R package that ships with every R installation, providing core statistical functions like lm() for regression, t.test() for hypothesis testing, and functions for common probability distributions. It requires no separate installation since it's part of base R itself.
- **rstatix**
  - rstatix provides a tidyverse-friendly interface for common statistical tests, wrapping base R functions like t.test() and aov() in a syntax that fits naturally into a dplyr pipeline. It returns results as tidy data frames rather than the more complex object types base R statistical functions typically produce, making the output easier to filter, combine, or feed into a plot.

### 3.3 Machine Learning
- **Linear Regression**
  - Linear regression models the relationship between a numeric outcome and one or more predictor variables, fitting a straight line, or hyperplane with multiple predictors, that best describes the relationship. R's lm() function fits linear models with a simple formula syntax, like lm(sales ~ advertising).
- **Logistic Regression**
  - Logistic regression models a binary outcome, like whether an event happens or not, as a function of one or more predictor variables. It predicts the probability of the outcome falling into one category, using the glm() function with a logistic link in R.
- **tidymodels**
  - tidymodels is a collection of R packages for building and evaluating machine learning models, designed to follow tidyverse conventions and work well with the pipe operator. It splits modeling into distinct, composable steps: preprocessing, specifying a model, fitting it, and evaluating results, each handled by a different package within the collection.

### 3.4 NLP
- **Hypothesis Testing**
  - Hypothesis testing provides a formal framework for deciding whether an observed pattern in data is likely real or could plausibly have occurred by chance alone. It starts with a null hypothesis, typically stating there's no effect, and calculates a p-value representing how surprising the observed data would be if that null hypothesis were true.
- **Time Series Analysis**
  - Time series analysis studies data collected sequentially over time, where the order of observations carries meaning that would be lost if the rows were shuffled. It involves identifying trends, seasonal patterns, and autocorrelation, where a value depends on its own previous values.
- **tidytext**
  - tidytext applies tidyverse conventions to text analysis, representing tokenized text as a data frame with one row per word. This tidy structure lets you use familiar dplyr verbs to filter, count, and summarize text data, rather than working with specialized text-only data structures.
- **quanteda**
  - quanteda is a faster, more powerful text analysis package built for working with large corpora of documents, offering more advanced features than tidytext for tasks like document-feature matrices and topic modeling. It trades some of tidytext's tidyverse-native simplicity for more performance and specialized functionality.

### 3.5 Network Analysis
- **igraph**
  - igraph is the standard R package for building, analyzing, and visualizing network graphs. It provides tools for calculating centrality measures, detecting communities, and computing paths between nodes, covering most of the core graph theory operations needed.
- **tidygraph**
  - tidygraph applies tidyverse conventions to network data, letting you manipulate graph nodes and edges using familiar dplyr-style verbs instead of igraph's more specialized syntax. It works alongside ggraph for visualization, together forming a tidyverse-native alternative to working with igraph directly.
- **sf**
  - sf handles vector spatial data in R, representing points, lines, and polygons, such as store locations or country boundaries. It's built around simple features, a standard format for representing spatial data used across many GIS tools beyond just R.

### 3.6 Geospatial Analysis
- **tmap**
  - tmap creates thematic maps in R, designed specifically for visualizing spatial data like sf objects with a syntax inspired by ggplot2's layered approach. It supports both static maps for reports and interactive maps for exploration, switching between the two with a single setting.
- **leaflet**
  - leaflet creates interactive, web-based maps in R, built on top of the popular Leaflet.js JavaScript library. Unlike static maps, leaflet maps let viewers pan, zoom, and click on individual features to see more detail.
- **terra**
  - terra handles raster data in R, grids of values like satellite imagery or elevation data, and has replaced the older, now retired raster package. It provides functions for reading, manipulating, and analyzing raster layers, including operations like resampling and calculating values across a grid.

### 3.7 Big Data Tools
- **Parallel Computing**
  - Parallel computing splits a computational task across multiple processor cores at once, rather than running everything sequentially, cutting the total time for tasks that can be broken into independent pieces. R provides tools like the parallel package's parLapply() for distributing work across a cluster of R processes.
- **Sparklyr**
  - Sparklyr connects R to Apache Spark, a distributed computing framework built for processing datasets far too large to fit in memory on a single machine. It lets you write familiar dplyr syntax that gets translated into Spark operations running across a cluster of machines.

---

## 4. Optional / Specialized Topics

- Installing Packages
- Loops
- Positron
- VS Code
- Pipe
- Quarto
- R Markdown
- Complex
- Vectors
- Data Tables
- Apply Family
- dplyr
- JSON
- tidyr
- readr
- lubridate
- purrr
- tibble
- stringr
- forcats
- Encoding Categories
- Casting Types
- Reshaping
- isnull, isna
- Dropping vs. Imputing

---

## 5. References

- [R Programming Roadmap](https://roadmap.sh/r-programming)

---

## 6. Related Roles / Topics

### Related Roles
- Data Analyst
- AI Engineer
- Data Engineer
- AI and Data Scientist
- BI Analyst

### Related Skills
- Python for Data Analysis
- Power Bi