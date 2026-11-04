# Python for Data Analysis

## Metadata
- Type: Skill
- Domain: Programming Languages
- Source: roadmap.sh
- Source URL: https://roadmap.sh/python-data-analysis
- Related Roles:
  - Data Analyst
  - Data Engineer
  - Machine Learning Engineer
  - BI Analyst

---

## 1. Beginner

### 1.1 Introduction
- **Arithmetic**
  - Arithmetic operators perform mathematical calculations: + (addition), - (subtraction), (multiplication), / (division), // (floor division), % (modulo), and (exponentiation). They are used constantly for computing derived columns, normalizing values, and performing aggregations.
- **Comparison**
  - Comparison operators evaluate the relationship between two values and return a boolean. They include ==, !=, <, >, <=, and >=.
- **Logical**
  - Logical operators combine boolean expressions. Python uses and, or, and not for this purpose.
- **Conditionals**
  - Conditionals execute different code paths based on whether a condition is true. Python uses if, elif, and else for this.
- **Loops**
  - Loops execute a block of code repeatedly. Python provides for loops for iterating over sequences and while loops for condition-based repetition.
- **Operators**
  - Operators are symbols that perform operations on values and variables. Python supports arithmetic, comparison, and logical operators, each serving a different purpose in data analysis code.
- **Integers**
  - Integers (int) are whole numbers without a decimal point. They appear as counts, indices, IDs, and categorical encodings.
- **Floats**
  - Floats (float) represent real numbers with a decimal point. Most numerical data in analysis involves floats, including prices, measurements, and probabilities.
- **Booleans**
  - Booleans (bool) have two values: True and False. They are the result of comparison and logical operations and are used to control flow and filter data.
- **Strings**
  - Strings (str) represent text data. Column names, categorical values, labels, and file paths are all strings.
- **Type Casting**
  - Type casting converts a value from one data type to another using built-in functions like int(), float(), str(), and bool(). It is frequently needed when data is loaded with incorrect types, such as numbers stored as strings or booleans stored as integers.
- **Lists**
  - Lists are ordered, mutable sequences that can hold elements of any type. They are one of the most used data structures in Python for storing collections of values.
- **Tuples**
  - Tuples are ordered, immutable sequences. Unlike lists, their contents cannot be changed after creation.
- **Sets**
  - Sets are unordered collections of unique values. They support mathematical set operations like union, intersection, and difference.
- **Dictionaries**
  - Dictionaries store key-value pairs and provide fast lookup by key. They are used extensively in Python for mapping labels to values, building frequency counts, and configuring function arguments.
- **Printing Variables**
  - Printing variables is done with Python's built-in print() function. During analysis, printing intermediate values helps verify that transformations are working as expected.
- **Null**
  - Null values represent missing or undefined data within a dataset, signaling that a specific observation or entry is absent. In Python, this is typically represented by None, while libraries like pandas utilize NaN (Not a Number) to denote missing numeric information.

### 1.2 Functions & Methods
- **List Comprehensions**
  - List comprehensions provide a concise syntax for creating lists by applying an expression to each item in an iterable, optionally filtering with a condition. For example: [x2 for x in range(10) if x % 2 == 0].
- **Defining Functions**
  - User-defined functions are created with the def keyword and encapsulate reusable logic. A function takes parameters, executes a body, and returns a value with return.
- **args & kwargs**
  - args allows a function to accept any number of positional arguments as a tuple. kwargs allows any number of keyword arguments as a dictionary.
- **Lambda Functions**
  - Lambda functions are anonymous, single-expression functions defined with the lambda keyword. They are used for short, throwaway operations, particularly as arguments to functions like map(), filter(), and Pandas' apply().
- **Built-in Functions**
  - Python's built-in functions are available without any imports and cover common operations: len(), sum(), min(), max(), sorted(), enumerate(), zip(), map(), filter(), and others. These functions simplify common tasks and are used constantly alongside data analysis libraries.
- **pip**
  - pip is Python's default package installer. It installs packages from the Python Package Index (PyPI) using pip install package-name.
- **conda**
  - conda is an open-source package and environment manager included with the Anaconda and Miniconda distributions. It manages both Python packages and non-Python dependencies, making it well suited for scientific computing.
- **virtualenv / venv**
  - venv is Python's built-in tool for creating isolated virtual environments. Each environment has its own Python interpreter and installed packages, preventing conflicts between projects.
- **Working with Strings**
  - Python provides a rich set of string methods for manipulating text: strip(), split(), replace(), upper(), lower(), startswith(), endswith(), and many more. These methods are applied directly to strings or through Pandas' .str accessor for vectorized text cleaning on entire columns.
- **uv**
  - uv is a Python package and project manager written in Rust. It handles dependency installation, virtual environments, Python version management, and project builds in a single tool, replacing the need for separate tools like pip, pip-tools, virtualenv, and pyenv.

### 1.3 Environment Setup
- **JupyterLab**
  - JupyterLab is the modern, full-featured successor to the classic Jupyter Notebook interface. It supports notebooks where code, output, and narrative text coexist in a single document, while adding a tabbed layout, a file browser, a terminal, and support for multiple file types side by side.

### 1.4 SQL Fundamentals
- **Google Colab**
  - Google Colab is a cloud-hosted Jupyter notebook environment from Google. It requires no local setup and provides free access to GPUs and TPUs, making it popular for machine learning work.
- **VS Code**
  - Visual Studio Code is a lightweight, extensible code editor that supports Python development through extensions. With the Python and Jupyter extensions installed, VS Code supports notebooks, debugging, linting, and IntelliSense.
- **sqlite3**
  - sqlite3 is Python's built-in library for working with SQLite databases. SQLite is a lightweight, file-based relational database that requires no server setup.
- **SQLAlchemy**
  - SQLAlchemy is a Python SQL toolkit and object-relational mapper (ORM) that provides a unified interface for connecting to many database backends including PostgreSQL, MySQL, SQLite, and others. It is used with Pandas via pd.readsql() to load query results directly into DataFrames.
- **DuckDB**
  - DuckDB is an in-process analytical database designed for fast SQL queries on large datasets stored as files or in memory. It can query CSV, Parquet, and Pandas DataFrames directly with SQL syntax.
- **Pandas**
  - Pandas integrates with SQL through pd.readsql(), which executes a SQL query against a database connection and returns the result as a DataFrame. This allows analysts to leverage SQL for initial data extraction and filtering while using Pandas for downstream manipulation and analysis.

### 1.5 NumPy
- **Arrays & ndarray**
  - The ndarray is NumPy's core data structure: a multi-dimensional, homogeneously typed array stored in contiguous memory. It supports element-wise operations, broadcasting, and vectorized computation far faster than Python lists.
- **Array Operations**
  - NumPy supports a wide range of array operations: element-wise arithmetic, aggregation functions (sum, mean, std, min, max), reshaping, stacking, and splitting. These operations are vectorized, meaning they apply to the entire array at once without explicit loops, making them highly efficient.
- **Indexing & Slicing**
  - Indexing and slicing are techniques used to access, extract, or modify specific elements within a NumPy array. Indexing refers to selecting a single item based on its position, typically using square brackets and integer coordinates, while slicing allows you to retrieve a contiguous subset of the array by defining a range of indices using a colon separator.
- **Linear Algebra Basics**
  - NumPy provides linear algebra operations, including matrix multiplication (np.dot, @), matrix inversion, determinants, and eigenvalues. These are used in statistics (covariance matrices), machine learning (feature transformations), and scientific computing.
- **Random Module**
  - NumPy's random module generates pseudorandom numbers and samples. It provides functions for creating random arrays, sampling from distributions (normal, uniform, binomial), and setting a seed for reproducibility.
- **Series and DataFrame**
  - A Series is a one-dimensional labeled array, analogous to a single column in a spreadsheet. A DataFrame is a two-dimensional table of Series that share an index, analogous to a spreadsheet or SQL table.
- **Reading Data**
  - Pandas provides functions to load data from many formats: pd.readcsv(), pd.readexcel(), pd.readjson(), pd.readparquet(), pd.readsql(), and others. Each function returns a DataFrame and accepts parameters for handling headers, delimiters, encoding, and data types.

### 1.6 Pandas
- **Indexing & Slicing**
  - Pandas provides two primary indexing systems: .loc[] for label-based selection and .iloc[] for position-based selection. Both work on rows, columns, or both simultaneously.
- **Filtering & Querying**
  - Filtering in Pandas selects rows that meet specified conditions. Boolean masks, the .query() method, and .isin() are common approaches.
- **Groupby & Aggregation**
  - groupby() splits a DataFrame into groups based on one or more columns, applies a function to each group, and combines the results. Common aggregation functions include sum(), mean(), count(), min(), max(), and custom functions via agg().
- **Polars**
  - Polars is a fast DataFrame library for Python written in Rust. It is designed as a high-performance alternative to Pandas, with a more consistent API and significantly better performance on large datasets.

---

## 2. Intermediate

### 2.1 Reading Local Files
- **Merging & Joining**
  - Pandas provides merge() and join() for combining DataFrames based on common columns or indices. Merge supports inner, left, right, and outer joins, mirroring SQL JOIN behavior.
- **Reshaping**
  - Reshaping transforms the structure of a DataFrame without changing its data. pivot() and pivottable() convert long-format data to wide format.
- **CSV**
  - CSV (Comma-Separated Values) is the most common format for tabular data exchange. pd.readcsv() loads a CSV file into a DataFrame and accepts dozens of parameters for handling separators, missing values, date parsing, and data types.
- **Excel**
  - Excel files (.xlsx, .xls) are loaded with pd.readexcel(), which supports selecting sheets, skipping rows, and reading specific columns. The openpyxl library is required for .xlsx files.
- **JSON**
  - JSON (JavaScript Object Notation) is a text format for structured data commonly returned by APIs. pd.readjson() converts JSON into a DataFrame, though nested structures often require normalization with pd.jsonnormalize().
- **Parquet**
  - Parquet is a columnar file format optimized for analytical workloads. It stores data with type information, supports efficient compression, and reads much faster than CSV for large datasets.

### 2.2 Reading Web Data
- **APIs with requests**
  - The requests library is the standard Python tool for making HTTP requests. It is used to call REST APIs that return JSON or XML data.
- **BeautifulSoup**
  - BeautifulSoup is a Python library for parsing HTML and XML documents. It provides methods for navigating the document tree, searching for elements by tag, class, or attribute, and extracting text and links.
- **scrapy**
  - Scrapy is a Python framework for large-scale web scraping. Unlike BeautifulSoup, which parses individual pages, Scrapy manages the full crawling workflow: following links, handling pagination, managing request queues, and exporting data.
- **isnull, isna**
  - isnull() and isna() are equivalent Pandas methods that return a boolean DataFrame or Series indicating which values are missing (NaN). They are the first step in assessing data completeness.

### 2.3 Data Cleaning
- **IQR**
  - The Interquartile Range (IQR) is the difference between the 75th percentile (Q3) and 25th percentile (Q1) of a dataset. Outliers are commonly defined as values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR.
- **Pandas String Methods**
  - Pandas exposes string methods through the .str accessor on Series, allowing vectorized text operations on entire columns. Methods include .str.strip(), .str.lower(), .str.contains(), .str.replace(), .str.split(), and .str.extract().
- **Dropping vs. Imputing**
  - When handling missing values, dropping removes rows or columns with dropna(), while imputing fills them with a substitute value using fillna() or SimpleImputer from Scikit-learn. Dropping is appropriate when missing data is rare or random.
- **Forward / Backward Fill**
  - Forward fill (ffill) propagates the last valid value forward to fill subsequent missing entries. Backward fill (bfill) does the reverse, filling from the next valid value.
- **Z-score**
  - A Z-score measures how many standard deviations a value is from the mean. Values with a Z-score above 3 or below −3 are commonly flagged as outliers.
- **strip, replace, split**
  - strip() removes leading and trailing whitespace from a string. replace() substitutes one substring with another.
- **re**
  - The re module provides regular expression support for pattern matching and text manipulation. It is used for extracting structured data from unstructured text, validating formats, and performing complex find-and-replace operations.

### 2.4 Exploratory Data Analysis
- **Visual Inspection**
  - Visual inspection uses charts to identify outliers and anomalies that statistical thresholds might miss. Box plots show the IQR and flag points beyond the whiskers.
- **Parsing Dates**
  - Date columns loaded from CSV are typically read as strings and must be converted to datetime objects for time-based operations. pd.todatetime() parses date strings in many formats and accepts a format parameter for custom patterns.
- **Encoding Categories**
  - Categorical encoding converts text category labels into numerical values that machine learning algorithms can process. Common approaches include label encoding (assigning each category an integer), one-hot encoding (creating binary columns for each category with pd.getdummies()), and ordinal encoding for ordered categories.
- **Casting Types**
  - Casting types in Pandas converts a column from one data type to another using .astype(). Common conversions include converting string columns to numeric with pd.tonumeric(), converting to datetime with pd.todatetime(), and converting integers to categories.
- **Mean, Median, Mode**
  - Mean, median, and mode are measures of central tendency that describe the typical value in a distribution. Pandas computes these with mean(), median(), and mode() on Series or DataFrame columns.
- **Variance & Std. Deviation**
  - Variance measures the average squared deviation from the mean, and standard deviation is its square root in the original units. Both quantify how spread out data values are.

### 2.5 Matplotlib
- **Plot Categories**
  - Matplotlib supports a wide range of plot types: line plots (plot), bar charts (bar, barh), scatter plots (scatter), histograms (hist), box plots (boxplot), pie charts (pie), and more. Choosing the right plot type depends on the data structure and the relationship being communicated.
- **Subplots and figures**
  - Matplotlib's Figure is the top-level container, and Axes objects are the individual plots within it. plt.subplots(rows, cols) creates a grid of axes for displaying multiple plots side by side.
- **Customizing Plots**
  - Matplotlib allows extensive customization: titles with settitle(), axis labels with setxlabel() / setylabel(), tick formatting, color palettes, line styles, font sizes, legends, and annotations. Customizing plots ensures they communicate clearly and meet the standards required for reports and presentations.
- **Saving figures**
  - Figures are saved to disk with plt.savefig('filename.png', dpi=300, bboxinches='tight'). Supported formats include PNG, PDF, SVG, and JPEG.
- **Histogram**
  - A histogram groups numeric values into bins and shows the count or frequency of each bin as a bar. It is the primary tool for visualizing the distribution of a single variable: its shape, center, spread, and whether it is skewed or has multiple peaks.
- **Correlation & Covariance**
  - Correlation measures the strength and direction of the linear relationship between two variables, scaled between −1 and +1. Covariance measures the same relationship but is not normalized, making it harder to interpret across variables with different scales.
- **Boxplot**
  - A box plot displays the five-number summary of a variable: minimum, Q1, median, Q3, and maximum. The box covers the IQR, a line marks the median, and whiskers extend to the data range.

### 2.6 Seaborn
- **Scatterplot**
  - A scatter plot displays two numeric variables as points on an x-y axis to reveal their relationship. It is used during EDA to detect correlations, clusters, and outliers.
- **Correlation Matrix**
  - A correlation matrix shows the pairwise correlation coefficients between all numeric columns in a dataset. It is computed with df.corr() and typically visualized as a heatmap using Seaborn.
- **Cross-tabulation**
  - Cross-tabulation (crosstab) counts the frequency of combinations of values across two or more categorical variables. pd.crosstab() produces a table of frequencies or proportions.
- **Distribution plots**
  - Seaborn's distribution plots visualize the distribution of one or two variables. sns.histplot() and sns.kdeplot() show the shape of a single variable's distribution.
- **Categorical Plots**
  - Seaborn's categorical plots visualize the relationship between a numeric variable and one or more categorical variables. sns.boxplot(), sns.violinplot(), sns.barplot(), sns.stripplot(), and sns.countplot() cover the main patterns.
- **Heatmaps**
  - sns.heatmap() visualizes matrix-style data using color intensity. It is most commonly used to display correlation matrices and pivot tables.
- **Customizing Plots**
  - Seaborn plots are customized through function parameters (palette, hue, size, style) and by accessing the underlying Matplotlib axes after creation. sns.settheme() and sns.setstyle() change the global appearance.
- **Regression Plots**
  - Seaborn's regression plots visualize the relationship between two numeric variables with a fitted regression line. sns.regplot() plots data points and a linear regression fit with confidence interval.

### 2.7 Interactive Visualization
- **Plotly**
  - Plotly is a Python library for creating interactive charts and dashboards. It produces web-based visualizations using JavaScript under the hood, with a Python API.

### 2.8 Dashboards
- **Streamlit**
  - Streamlit is an open-source Python framework for building interactive data applications with minimal code. A Streamlit app is a Python script where each widget (slider, dropdown, text input) triggers a rerun of the script with the new value.
- **Dash**
  - Dash is a Python framework for building analytical web applications, developed by Plotly. It combines Plotly charts with reactive UI components and runs as a Flask web server.
- **Power BI / Tableau**
  - Power BI and Tableau are enterprise BI platforms for building interactive dashboards and reports. Python integrates with both: Power BI supports Python visuals and data transformation scripts, and Tableau supports Python through TabPy for custom calculations.

---

## 3. Advanced

### 3.1 OOP for Data Analysis
- **OOP for Data Analysis**
  - Object-oriented programming (OOP) organizes code around classes and objects rather than standalone functions and procedures. A class defines a blueprint with attributes (data) and methods (behavior), and objects are instances of that class.

### 3.2 Statistics & ML
- **SciPy**
  - SciPy is a scientific computing library built on NumPy. It provides modules for statistics (scipy.stats), optimization (scipy.optimize), linear algebra, signal processing, and numerical integration.
- **Scikit-learn**
  - Scikit-learn is the standard machine learning library for Python. It provides a consistent API for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.

### 3.3 Geospatial Analysis
- **GeoPandas**
  - GeoPandas is an open-source library that extends the capabilities of pandas by allowing spatial operations on geometric types. It simplifies working with geospatial data by enabling the use of familiar data structures like GeoSeries and GeoDataFrame, which store and manipulate vector-based geographic information.

### 3.4 Big Data Tools
- **Dask**
  - Dask is a parallel computing library for Python that scales Pandas, NumPy, and Scikit-learn to larger-than-memory datasets. It breaks data into chunks and builds a task graph that is executed lazily.
- **PySpark**
  - PySpark is the Python API for Apache Spark, the distributed data processing engine. It allows Python code to run Spark jobs on clusters, processing datasets at the scale of terabytes.

### 3.5 Data Pipelines
- **Airflow**
  - Apache Airflow is an open-source platform for authoring, scheduling, and monitoring data pipelines. Pipelines are defined as DAGs (Directed Acyclic Graphs) in Python, where each node is a task and edges define dependencies.

---

## 4. Optional / Specialized Topics

- Loops
- Operators
- Integers
- Floats
- Booleans
- Strings
- Type Casting
- Lists
- Tuples
- Sets
- Dictionaries
- Printing Variables
- Null
- Built-in Functions
- pip
- conda
- virtualenv / venv
- Working with Strings
- uv
- DuckDB
- Pandas
- Random Module
- Series and DataFrame
- Reading Data
- JSON

---

## 5. References

- [Python for Data Analysis Roadmap](https://roadmap.sh/python-data-analysis)

---

## 6. Related Roles / Topics

### Related Roles
- Data Analyst
- Data Engineer
- Machine Learning Engineer
- BI Analyst

### Related Skills
- Python
- Devops Beginner