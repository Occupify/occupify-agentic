# Data Analyst

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/data-analyst
- Related Roles:
  - AI and Data Scientist
  - PostgreSQL DBA
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is Data Analytics**
  - Data analytics is the process of collecting, cleaning, transforming, and analyzing data to discover useful information, identify patterns, and support decisions. It spans a wide range of activities from basic reporting to predictive modeling.
- **Key Concepts of Data**
  - Data analysis is the process of inspecting, cleansing, transforming, and modeling data to discover useful information and support decision-making. In the broadest sense, data can be classified into various types like nominal, ordinal, interval and ratio, each with a specific role and analysis technique.

### 1.2 Types of Data Analytics
- **Descriptive Analytics**
  - Descriptive analytics summarizes historical data to answer the question "what happened?" It produces reports, dashboards, and summaries that describe past performance. Examples include monthly sales reports, website traffic summaries, and customer demographic breakdowns.
- **Diagnostic Analytics**
  - Diagnostic analytics examines data to answer "why did it happen?" It goes beyond describing outcomes to identifying the causes and contributing factors behind them. Techniques include drill-down analysis, data discovery, correlations, and filtering to isolate the drivers of a specific result.
- **Predictive Analytics**
  - Predictive analytics uses historical data and statistical models to forecast future outcomes. It answers the question "what is likely to happen?" Techniques include regression, time series analysis, and machine learning models trained on past data to predict future behavior or events.
- **Prescriptive Analytics**
  - Prescriptive analytics recommends actions to achieve a desired outcome, answering "what should we do?" It builds on predictive analytics by combining forecasts with optimization and decision logic. Examples include recommendation engines, dynamic pricing systems, and supply chain optimization tools.
- **Collection**
  - Data collection is the process of gathering raw data from various sources for analysis. Sources can include databases, spreadsheets, APIs, web scraping, surveys, and sensor data.
- **Cleanup**
  - Data cleanup (or data cleaning) is the process of identifying and correcting errors, inconsistencies, and missing values in a dataset. Common tasks include handling null values, removing duplicates, fixing formatting issues, and standardizing categories.
- **Exploration**
  - Data exploration, or exploratory data analysis (EDA), is the process of examining a dataset to understand its structure, distributions, and relationships before formal analysis. It involves computing summary statistics, creating visualizations, and identifying patterns, outliers, and anomalies.
- **Visualisation**
  - Data visualisation is the representation of data in graphical or visual form. Charts, graphs, and dashboards make patterns and relationships in data easier to perceive and communicate than tables of numbers alone.
- **Statistical Analysis**
  - Statistical analysis applies mathematical techniques to summarize, interpret, and draw inferences from data. Core methods include descriptive statistics, hypothesis testing, correlation analysis, and regression.

### 1.3 Excel
- **Machine Learning**
  - Machine learning is a branch of artificial intelligence where systems learn patterns from data and make predictions or decisions without being explicitly programmed for each task. For data analysts, ML provides tools like classification, clustering, and regression models that automate pattern recognition at scale.
- **IF**
  - The IF function in Excel is a crucial tool for data analysts, enabling them to create conditional statements, clean and validate data, perform calculations based on specific conditions, create custom metrics, apply conditional formatting, automate tasks, and generate dynamic reports. Data analysts use IF to categorize data, handle missing values, calculate bonuses or custom metrics, highlight trends, and enhance visualizations, ultimately facilitating informed decision-making through data analysis.
- **DATEDIF**
  - DATEDIF calculates the difference between two dates in days, months, or years. It is useful for computing ages, tenures, and durations.
- **VLOOKUP / HLOOKUP**
  - VLOOKUP searches for a value in the first column of a table and returns a value from a specified column in the same row. HLOOKUP does the same horizontally, searching across the first row.
- **REPLACE / SUBSTITUTE**
  - REPLACE replaces a portion of a text string based on position and length. SUBSTITUTE replaces all occurrences of a specific substring with another string.

### 1.4 Learn a Language
- **UPPER / LOWER / PROPER**
  - UPPER converts text to all uppercase, LOWER to all lowercase, and PROPER capitalizes the first letter of each word. These functions are used to standardize text formatting in datasets, especially when combining data from multiple sources with inconsistent casing.
- **CONCAT**
  - CONCAT joins two or more text strings into one. It is the modern replacement for the & operator and the older CONCATENATE function.
- **TRIM**
  - Trim is considered a basic yet vital function within the scope of data analysis. It plays an integral role in preparing and cleansing the dataset, which is key to analytical accuracy.
- **AVERAGE**
  - The average, also often referred to as the mean, is one of the most commonly used mathematical calculations in data analysis. It provides a simple, useful measure of a set of data.
- **COUNT**
  - The Count function in data analysis is one of the most fundamental tasks that a Data Analyst gets to handle. This function is a simple yet powerful tool that aids in understanding the underlying data by providing the count or frequency of occurrences of unique elements in data sets.

---

## 2. Intermediate

### 2.1 Data Manipulation Lib's.
- **SUM**
  - Sum is one of the most fundamental operations in data analysis. As a data analyst, the ability to quickly and accurately summarize numerical data is key to draw meaningful insights from large data sets.
- **MIN / MAX**
  - Understanding the minimum and maximum values in your dataset is critical in data analysis. These basic functions, often referred to as Min-Max functions, are statistical tools that data analysts use to inspect the distribution of a particular dataset.

### 2.2 Data Viz. Libraries
- **Charting**
  - Excel charts turn tabular data into visual representations like bar charts, line charts, pie charts, and scatter plots. Charts are created directly from selected data and can be formatted and embedded in reports and dashboards.
- **Pivot Tables**
  - Pivot tables are one of Excel's most powerful features for summarizing and analyzing large datasets. They allow data to be grouped, filtered, and aggregated across multiple dimensions without writing formulas.

### 2.3 Data Collection
- **Databases**
  - Databases are structured storage systems that hold organized data accessible via query languages like SQL. Data analysts connect to databases to extract relevant subsets of data for analysis.
- **CSV Files**
  - CSV (Comma-Separated Values) files are plain text files where each row represents a record and columns are separated by commas. They are the most common format for exchanging tabular data between systems and tools.
- **APIs**
  - Application Programming Interfaces, better known as APIs, play a fundamental role in the work of data analysts, particularly in the process of data collection. APIs are sets of protocols, routines, and tools that enable different software applications to communicate with each other.
- **Web Scraping**
  - Web scraping plays a significant role in collecting unique datasets for data analysis. In the realm of a data analyst's tasks, web scraping refers to the method of extracting information from websites and converting it into a structured usable format like a CSV, Excel spreadsheet, or even into databases.

### 2.4 Data Cleanup
- **Handling Missing Data**
  - Missing data occurs when values are absent in a dataset, which can distort analysis if not handled carefully. Common strategies include removing rows with missing values, imputing with the mean, median, or a predicted value, and flagging missingness as its own category.
- **Removing Duplicates**
  - Duplicate records occur when the same entity appears more than once in a dataset, often due to data entry errors or merging multiple sources. Removing duplicates ensures that counts, sums, and other aggregations are not inflated.
- **Finding Outliers**
  - Outliers are data points that differ significantly from the rest of the dataset. They can result from data entry errors, measurement anomalies, or genuine extreme values.
- **Data Transformation**
  - Data Transformation, also known as Data Wrangling, is an essential part of a Data Analyst's role. This process involves the conversion of data from a raw format into another format to make it more appropriate and valuable for a variety of downstream purposes such as analytics.
- **Pandas**
  - Pandas is used extensively for data cleanup tasks: loading raw data, filling or dropping missing values, removing duplicates, renaming columns, filtering rows, and converting data types. Its DataFrame API provides a comprehensive set of methods for every stage of the cleanup workflow, making it the go-to tool for Python-based data preparation.
- **Dplyr**
  - Dplyr provides the primary toolkit for data transformation in R. Functions like mutate(), filter(), select(), arrange(), and summarise() cover the most common transformation tasks.
- **Dispersion**
  - Dispersion measures how spread out values are in a dataset. High dispersion means values vary widely; low dispersion means they cluster close to the center.

### 2.5 Descriptive Analysis
- **Mean**
  - The mean is the arithmetic average of a set of values, calculated by summing all values and dividing by the count. It is the most commonly used measure of central tendency but is sensitive to outliers.
- **Range**
  - Range is the simplest measure of dispersion, calculated as the difference between the maximum and minimum values in a dataset. It gives a quick sense of how wide the data spans but is sensitive to outliers.
- **Variance**
  - Variance measures the average squared deviation of each value from the mean. It quantifies how much the data points differ from the average.
- **Standard Deviation**
  - Standard deviation is the square root of variance and expresses dispersion in the same units as the original data. It is the most commonly used measure of spread.
- **Central Tendency**
  - Measures of central tendency describe the center or typical value of a dataset. The three main measures are mean (arithmetic average), median (middle value), and mode (most frequent value).
- **Visualizing Distributions**
  - Visualizing distributions helps analysts understand the shape, spread, and outliers of a variable more intuitively than summary statistics alone. Common visualizations include histograms, density plots, box plots, and violin plots.

### 2.6 Data Visualisation
- **Distribution Shape**
  - Distribution space refers to the full range of values a variable takes and how frequently each value or range of values occurs. Understanding distribution shape (symmetric, skewed, bimodal) informs which statistical methods are appropriate.
- **Median**
  - Median signifies the middle value in a data set when arranged in ascending or descending order. As a data analyst, understanding, calculating, and interpreting the median is crucial.
- **Mode**
  - The mode is the value that appears most frequently in a dataset. It is the only measure of central tendency applicable to categorical data.
- **Skewness**
  - Skewness is a crucial statistical concept driven by data analysis and is a significant parameter in understanding the distribution shape of a dataset. In essence, skewness provides a measure to define the extent and direction of asymmetry in data.
- **Kurtosis**
  - Kurtosis measures the heaviness of a distribution's tails compared to a normal distribution. High kurtosis (leptokurtic) means more values in the tails and a sharper peak; low kurtosis (platykurtic) means thinner tails and a flatter peak.
- **Tableau**
  - Tableau is a leading business intelligence and data visualization platform. It allows analysts to connect to data sources and build interactive dashboards and visualizations with a drag-and-drop interface.
- **Matplotlib**
  - Matplotlib is Python's foundational plotting library. It supports a wide range of chart types and gives detailed control over every visual element.
- **Seaborn**
  - Seaborn is a Python visualization library built on top of Matplotlib that provides a higher-level interface for statistical graphics. It simplifies the creation of complex plots like heatmaps, pair plots, and distribution comparisons.
- **ggplot2**
  - ggplot2 is R's most popular visualization library, based on the Grammar of Graphics framework. Plots are built by layering geometric elements (points, lines, bars) on top of aesthetic mappings (x, y, color, size).

---

## 3. Advanced

### 3.1 Statistical Analysis
- **Bar**
  - Bar charts display categorical data with rectangular bars whose lengths represent values. They are used to compare quantities across different categories.
- **Line**
  - Data visualization is a crucial skill for every Data Analyst and the Line Chart is one of the most commonly used chart types in this field. Line charts act as powerful tools for summarizing and interpreting complex datasets.
- **Scatter**
  - A scatter plot, a crucial aspect of data visualization, is a mathematical diagram using Cartesian coordinates to represent values from two different variables. As a data analyst, understanding and interpreting scatter plots can be instrumental in identifying correlations and trends within a dataset, drawing meaningful insights, and showcasing these findings in a clear, visual manner.
- **Funnel**
  - Funnel charts display values decreasing progressively across stages of a process, such as a sales pipeline or user conversion flow. Each stage is represented as a narrowing bar.
- **Histograms**
  - Histograms display the distribution of a numeric variable by grouping values into bins and showing the frequency of each bin. They reveal the shape, center, and spread of the data.
- **Stacked**
  - A stacked chart is an essential tool for a data analyst in the field of data visualization. This type of chart presents quantitative data in a visually appealing manner and allows users to easily compare different categories while still being able to compare the total sizes.
- **Heatmap**
  - A heatmap uses color intensity to represent the magnitude of values in a matrix. It is commonly used to visualize correlation matrices, frequency tables, and geographic data.
- **Pie**
  - Pie charts show the proportional composition of a whole by dividing a circle into slices. They are best used for a small number of categories (typically fewer than five) where the relative sizes are meaningfully different.
- **Hypothesis Testing**
  - Hypothesis testing is a statistical method for evaluating whether observed data provides enough evidence to support or reject a claim about a population. It involves defining a null hypothesis, choosing a significance level, computing a test statistic, and comparing it to a critical value or p-value.
- **Correlation Analysis**
  - Correlation analysis measures the strength and direction of the relationship between two numeric variables. The Pearson correlation coefficient ranges from -1 (perfect negative relationship) to +1 (perfect positive relationship), with 0 indicating no linear relationship.
- **Regression**
  - Regression models the relationship between a dependent variable and one or more independent variables. Simple linear regression fits a line to describe how one variable changes with another.

### 3.2 Machine Learning
- **Reinforcement Learning**
  - Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving rewards or penalties. Unlike supervised learning, it does not require labeled training data.
- **Unsupervised Learning**
  - Unsupervised learning finds patterns in data without labeled training examples. Common techniques include clustering (grouping similar data points together) and dimensionality reduction (compressing data while preserving structure).
- **Supervised Learning**
  - Supervised learning trains models on labeled data, where each example has an input and a known output. The model learns a mapping from inputs to outputs that generalizes to new examples.
- **Big Data Concepts**
  - Big data concepts describe the properties and challenges of working with very large datasets. The three Vs (volume, velocity, variety) capture the main dimensions: how much data there is, how fast it arrives, and how many formats it comes in.
- **Data Storage Solutions**
  - Big data storage solutions are designed to hold large volumes of structured, semi-structured, and unstructured data reliably. Options include distributed file systems like HDFS, object stores like S3, and columnar databases optimized for analytics.

### 3.3 Big Data Technologies
- **Decision Trees**
  - A decision tree is a supervised learning algorithm that splits data into branches based on feature values to reach a prediction. It is interpretable because the decision logic can be visualized and explained.
- **Naive Byes**
  - Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem, with the assumption that features are independent of each other given the class. Despite this simplifying assumption, it performs well in practice for text classification, spam detection, and other categorical problems.
- **K-Means Clustering**
  - K-Means is an unsupervised clustering algorithm that partitions data into K groups by iteratively assigning points to the nearest cluster centroid and updating the centroids. It is simple and scalable but requires specifying K in advance and is sensitive to outliers and initial centroid placement.
- **KNN**
  - K-Nearest Neighbors (KNN) is a simple supervised learning algorithm that classifies a data point based on the majority class of its K nearest neighbors in the feature space. It requires no training phase but is slow at prediction time for large datasets.
- **Parallel Processing**
  - Parallel processing divides a computation into tasks that run simultaneously across multiple processors or machines. It is the core technique that makes big data processing feasible, as tasks that would take hours on a single machine can complete in minutes when distributed.
- **Hadoop**
  - Apache Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters. It consists of HDFS for storage and MapReduce for computation.
- **Spark**
  - Apache Spark is a distributed data processing engine for large-scale batch and streaming workloads. It processes data in memory across a cluster, making it significantly faster than MapReduce for iterative computations.
- **MPI**
  - MPI (Message Passing Interface) is a standard for parallel programming across distributed memory systems. It allows processes on different machines to communicate and coordinate.
- **MapReduce**
  - MapReduce is a programming model for processing large datasets in parallel. The map phase transforms input data into key-value pairs, and the reduce phase aggregates them into a final result.

### 3.4 Deep Learning (Optional)
- **Model Evaluation**
  - Model evaluation measures how well a machine learning model performs on unseen data. Common metrics include accuracy, precision, recall, F1 score for classification, and mean squared error for regression.
- **Logistic Regression**
  - Logistic regression is a supervised classification algorithm that models the probability of a binary outcome using a sigmoid function. Despite its name, it is a classification method, not a regression one.
- **Neural Networks**
  - Neural networks are machine learning models inspired by the structure of the brain, consisting of layers of interconnected nodes (neurons) that transform inputs into outputs. They learn by adjusting connection weights during training to minimize prediction error.
- **CNNs**
  - Convolutional Neural Networks (CNNs) are a type of deep neural network designed for processing grid-structured data like images. They use convolutional layers to automatically learn spatial features such as edges, textures, and shapes.
- **RNN**
  - Recurrent Neural Networks (RNNs) are a type of neural network designed for sequential data, where the output at each step depends on previous steps. They maintain a hidden state that carries information from earlier in the sequence.
- **Tensorflow**
  - TensorFlow, developed by Google Brain Team, has become a crucial tool in the realm of data analytics, particularly within the field of deep learning. It's an open-source platform for machine learning, offering a comprehensive and flexible ecosystem of tools, libraries, and community resources.
- **Pytorch**
  - PyTorch is an open-source deep learning framework developed by Meta. It uses dynamic computation graphs, making it flexible and intuitive for research and experimentation.
- **Image Recognition**
  - Image recognition is the task of identifying objects, scenes, or attributes in images. Deep learning models, particularly CNNs, have achieved human-level performance on standard image recognition benchmarks.
- **NLP**
  - Natural Language Processing (NLP) is the field of enabling computers to understand, interpret, and generate human language. Tasks include text classification, sentiment analysis, named entity recognition, and machine translation.

---

## 4. Optional / Specialized Topics

- Collection
- Cleanup
- Exploration
- Visualisation
- Statistical Analysis
- REPLACE / SUBSTITUTE
- COUNT
- Pandas
- Dplyr
- Dispersion
- Central Tendency
- Visualizing Distributions
- Kurtosis
- Tableau
- Matplotlib
- Seaborn
- ggplot2
- Histograms
- Stacked
- Heatmap
- Pie
- Hypothesis Testing
- Correlation Analysis
- Regression
- Data Storage Solutions

---

## 5. References

- [Data Analyst Roadmap](https://roadmap.sh/data-analyst)

---

## 6. Related Roles / Topics

### Related Roles
- AI and Data Scientist
- PostgreSQL DBA
- Frontend Developer

### Related Skills
- SQL
- Python