# Machine Learning Engineer

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/machine-learning
- Related Roles:
  - AI and Data Scientist
  - AI Engineer
  - Data Analyst
  - Data Engineer

---

## 1. Beginner

### 1.1 Introduction
- **ML Engineer vs AI Engineer**
  - An ML Engineer primarily concentrates on building, deploying, and maintaining machine learning models in production environments. An AI Engineer, on the other hand, typically has a broader scope, encompassing the design and development of entire AI systems, which may include components beyond just machine learning, such as natural language processing, computer vision, and robotics.
- **Skills and Responsibilities**
  - Machine learning roles require a blend of technical expertise and practical abilities. These roles involve designing, developing, and deploying machine learning models to solve real-world problems.
- **What is an ML Engineer?**
  - An ML Engineer focuses on building, deploying, and maintaining machine learning systems in production. They bridge the gap between data science and software engineering, taking models developed by data scientists and making them scalable, reliable, and efficient for real-world applications.

### 1.2 Linear Algebra
- **Scalars, Vectors, Tensors**
  - Scalars, vectors, and tensors are fundamental building blocks for representing data in machine learning. A scalar is a single numerical value, like a temperature reading.
- **Singular Value Decomposition**
  - Singular Value Decomposition (SVD) is a matrix factorization technique that decomposes a rectangular matrix into three other matrices: a unitary matrix, a diagonal matrix of singular values, and another unitary matrix. This decomposition reveals the underlying structure of the original matrix, highlighting its principal components and allowing for dimensionality reduction and noise removal.
- **Matrix & Matrix Operations**
  - A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. Matrix operations are the rules and procedures for manipulating these matrices.
- **Eigenvalues, Diagonalization**
  - Eigenvalues are special numbers associated with a square matrix that, when multiplied by a corresponding eigenvector, result in the same vector scaled by that eigenvalue. Diagonalization is the process of transforming a square matrix into a diagonal matrix, where all off-diagonal elements are zero, using its eigenvectors and eigenvalues.
- **Determinants, inverse of Matrix**
  - A determinant is a scalar value that can be computed from the elements of a square matrix and encodes certain properties of the linear transformation described by the matrix. The inverse of a matrix, denoted as A⁻¹, is another matrix that, when multiplied by the original matrix A, results in the identity matrix.
- **Basics of Probability**
  - Probability is a way to quantify the likelihood of an event occurring. It provides a numerical measure, ranging from 0 to 1, representing the chance that a specific outcome will happen.
- **Bayes Theorem**
  - Bayes' Theorem is a mathematical formula that describes how to update the probability of a hypothesis based on new evidence. It essentially calculates the probability of an event occurring given that another event has already occurred.

### 1.3 Calculus
- **Chain rule of derivation**
  - The chain rule is a formula for finding the derivative of a composite function. If you have a function that's made up of one function inside another (like sin(x²) ), the chain rule lets you break down the differentiation process.
- **Gradient, Jacobian, Hessian**
  - The gradient, Jacobian, and Hessian are fundamental tools from calculus used to analyze and optimize functions, especially in the context of machine learning. The gradient of a scalar-valued function of multiple variables is a vector containing the partial derivatives with respect to each variable, indicating the direction of the steepest ascent.
- **Derivatives, Partial Derivatives**
  - A derivative measures how a function changes as its input changes. Imagine a curve on a graph; the derivative at a specific point tells you the slope of the line tangent to that curve at that point.

### 1.4 Discrete Mathematics
- **Discrete Mathematics**
  - Discrete mathematics deals with mathematical structures that are fundamentally discrete rather than continuous. This means it focuses on objects that have distinct, separated values, like integers, graphs, and logical statements.

### 1.5 Python
- **Python**
  - Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its significant use of indentation.

### 1.6 Probability
- **Types of Distribution**
  - A distribution describes how data is spread or arranged across its possible values. It provides a way to understand the probability of different outcomes occurring within a dataset.
- **Random Variances, PDFs**
  - A random variable is a variable whose value is a numerical outcome of a random phenomenon. It can be discrete (taking on a finite or countably infinite number of values) or continuous (taking on any value within a given range).

### 1.7 Statistics
- **Descriptive Statistics**
  - Descriptive statistics involves methods for summarizing and organizing data in a meaningful way. It focuses on describing the main features of a dataset using measures like mean, median, mode, standard deviation, and range.
- **Basic concepts**
  - Statistics is the science of collecting, analyzing, interpreting, and presenting data. It provides the foundation for understanding patterns and making inferences from data, which is crucial for machine learning algorithms.
- **Inferential Statistics**
  - Inferential statistics uses sample data to make inferences or predictions about a larger population. Instead of examining the entire population, which is often impractical or impossible, we analyze a representative subset (the sample) and then use statistical methods to draw conclusions about the characteristics of the whole population.
- **Graphs & Charts**
  - Graphs and charts are visual representations of data. They use symbols like bars, lines, and slices to display patterns, trends, and relationships within datasets.

### 1.8 Basic Syntax
- **Variables and Data Types**
  - Variables are named storage locations in a computer's memory used to hold data. Data types classify the kind of value a variable can hold, such as numbers (integers, decimals), text (strings), or boolean values (true/false).
- **Data Structures**
  - Python provides several built-in data structures for organizing and storing data. These structures include lists, which are ordered and mutable collections; tuples, which are ordered and immutable collections; dictionaries, which store data in key-value pairs; and sets, which are unordered collections of unique elements.
- **Loops**
  - Loops in Python are a way to repeat a block of code multiple times. They allow you to execute a set of instructions over and over, either a specific number of times or until a certain condition is met.

### 1.9 Object Oriented Programming
- **Numpy**
  - NumPy is a fundamental Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
- **Matplotlib**
  - Matplotlib is a paramount data visualization library used extensively by data analysts for generating a wide array of plots and graphs. Through Matplotlib, data analysts can convey results clearly and effectively, driving insights from complex data sets.

### 1.10 Essential libraries
- **Pandas**
  - Pandas is a library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.
- **Seaborn**
  - Seaborn is a robust, comprehensive Python library focused on the creation of informative and attractive statistical graphics. As a data analyst, seaborn plays an essential role in elaborating complex visual stories with the data.
- **APIs**
  - Application Programming Interfaces, better known as APIs, play a fundamental role in the work of data analysts, particularly in the process of data collection. APIs are sets of protocols, routines, and tools that enable different software applications to communicate with each other.

### 1.11 Data Sources
- **Databases (SQL, No-SQL)**
  - Databases are organized collections of data, stored and accessed electronically. SQL databases, like MySQL or PostgreSQL, use a structured, table-based format with a predefined schema, enforcing relationships between data through keys.
- **Internet**
  - The internet serves as a vast repository of information that can be leveraged for machine learning projects. This includes publicly available datasets, web pages that can be scraped for relevant information, social media platforms where user-generated content provides insights into opinions and trends, and online databases that offer structured data on various topics.
- **Mobile Apps**
  - Mobile app data refers to the information generated and collected from applications running on mobile devices like smartphones and tablets. This data encompasses a wide range of user interactions, device characteristics, and app performance metrics.
- **IoT**
  - The Internet of Things (IoT) refers to the network of physical devices, vehicles, home appliances, and other items embedded with electronics, software, sensors, and actuators that enable these objects to connect and exchange data. These devices continuously generate vast amounts of data reflecting their status, environment, and interactions.

---

## 2. Intermediate

### 2.1 Data Formats
- **JSON**
  - JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).
- **Parquet**
  - Parquet is a columnar storage format designed for efficient data storage and retrieval. Unlike row-oriented formats, Parquet stores data by columns, which allows for better compression and faster query performance when only a subset of columns are needed.
- **CSV**
  - CSV or Comma Separated Values files play an integral role in data collection for data analysts. These file types allow the efficient storage of data and are commonly generated by spreadsheet software like Microsoft Excel or Google Sheets, but their simplicity makes them compatible with a variety of applications that deal with data.
- **Excel**
  - Excel files are a common way to store data in a structured format using rows and columns. Each cell in the spreadsheet can hold different types of data, like numbers, text, or dates.
- **Other Data Formats**
  - Beyond the common formats like CSV, Excel, JSON, and Parquet, data can exist in a variety of other structures. These include formats optimized for specific applications or data types.

### 2.2 Preprocessing Techniques
- **Conditionals**
  - Conditional statements in Python allow you to execute different blocks of code based on whether a certain condition is true or false. The most common conditional statements are if, elif (else if), and else.
- **Exceptions**
  - Exceptions in Python are events that disrupt the normal flow of a program's execution. They occur when the interpreter encounters an error during runtime, such as trying to divide by zero or accessing an index that's out of bounds in a list.
- **Functions, Builtin Functions**
  - Functions are reusable blocks of code that perform a specific task. They take inputs, process them, and return an output.
- **Data Cleaning**
  - Data cleaning, which is often referred as data cleansing or data scrubbing, is one of the most important and initial steps in the data analysis process. As a data analyst, the bulk of your work often revolves around understanding, cleaning, and standardizing raw data before analysis.
- **Dimensionality Reduction**
  - Dimensionality reduction is the process of reducing the number of random variables under consideration by obtaining a set of principal variables. It can be divided into feature selection and feature extraction.
- **Feature Engineering**
  - Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy. This involves selecting, transforming, and creating new features from existing data.
- **Feature Scaling & Normalization**
  - Feature scaling is a preprocessing technique in machine learning that transforms numerical features to a common scale, ensuring they contribute equally to the model by preventing features with larger ranges from dominating, which is particularly important for algorithms sensitive to feature scales like gradient descent-based methods. Key methods include Standardization (transforming data to a mean of 0 and a standard deviation of 1, often better for outliers), and Normalization (scaling data to a fixed range, often 0 to 1).

### 2.3 What is Machine Learning?
- **Feature Selection**
  - Feature selection is the process of choosing a subset of the most relevant features from your original dataset. The goal is to reduce the dimensionality of the data by removing irrelevant, redundant, or noisy features.

### 2.4 Types of Machine Learning
- **Unsupervised Learning**
  - Unsupervised learning is a type of machine learning where the algorithm learns patterns from unlabeled data. Unlike supervised learning, there are no pre-defined correct answers or target variables provided to guide the learning process.
- **Supervised Learning**
  - Supervised learning is a type of machine learning where an algorithm learns from a labeled dataset. This means that each data point in the dataset is paired with a corresponding correct output, or "label." The algorithm's goal is to learn a function that maps inputs to outputs, so that when given new, unseen inputs, it can predict the correct output based on the patterns it learned from the labeled data.

### 2.5 Scikit-learn
- **Train - Test Data**
  - When building a machine learning model, we usually split our dataset into two parts: a training set and a testing set. The training set is used to teach the model how to make predictions, while the testing set is used to evaluate how well the model has learned.
- **Data Preparation**
  - Scikit-learn provides tools to get your data ready for machine learning models. This often involves cleaning, transforming, and scaling your data.
- **Data Loading**
  - Data loading in Scikit-learn refers to the process of importing datasets into a format that can be used for machine learning tasks. This involves reading data from various sources, such as CSV files, databases, or even directly from NumPy arrays, and structuring it into a format that Scikit-learn's algorithms can understand, typically NumPy arrays or Pandas DataFrames.
- **Tuning**
  - Scikit-learn provides tools to find the best settings (hyperparameters) for your machine learning models. Instead of manually trying different values, you can use techniques like GridSearchCV or RandomizedSearchCV.
- **Prediction**
  - In scikit-learn, prediction means using a trained machine learning model to estimate an output (or target variable) for new, unseen data. After a model is trained on a dataset, it learns the relationship between the input features and the target variable.
- **Model Selection**
  - Model selection is the process of choosing the best machine learning model from a set of candidate models for a given task. Scikit-learn offers a wide range of models, including linear models (like linear regression and logistic regression), tree-based models (like decision trees and random forests), support vector machines (SVMs), and neural networks, enabling you to find the most suitable model for your specific problem.

### 2.6 What is Supervised Learning?
- **Semi-supervised Learning**
  - Semi-supervised learning is a type of machine learning where the training data contains both labeled and unlabeled examples. The goal is to leverage the information from the unlabeled data to improve the performance of a model that would otherwise be trained solely on the labeled data.
- **Reinforcement Learning**
  - Reinforcement learning is a type of machine learning where an agent learns to make decisions in an environment to maximize a reward. The agent interacts with the environment, takes actions, and receives feedback in the form of rewards or penalties.
- **Self-supervised Learning**
  - Self-supervised learning is a type of machine learning where the model learns from unlabeled data by creating its own supervisory signals. This is achieved by masking parts of the input data and training the model to predict the masked portions based on the remaining data.

### 2.7 Classification
- **Logistic Regression**
  - Logistic Regression is a method used to predict the probability of a categorical outcome. Instead of predicting a continuous value, it predicts whether something belongs to a certain category (like yes/no, true/false, or 0/1).
- **Support Vector Machines**
  - Support Vector Machines (SVMs) are a type of supervised learning algorithm used for classification and regression. They work by finding an optimal hyperplane that separates data points belonging to different classes with the largest possible margin.
- **K-Nearest Neighbors (KNN)**
  - K-Nearest Neighbors (KNN) is a simple algorithm used for classifying data points based on their proximity to other data points. Given a new, unclassified data point, KNN identifies the 'K' closest data points (neighbors) from the training dataset.
- **Decision Trees, Random Forest**
  - Decision Trees are a way to make predictions by learning decision rules from data features. Imagine a flowchart where each internal node represents a test on an attribute (like "Is the color red?"), each branch represents the outcome of the test, and each leaf node represents a class label (like "apple" or "banana").

### 2.8 Regression
- **Linear Regression**
  - Linear regression is a simple method used to find the best straight line that describes the relationship between a dependent variable (the one you're trying to predict) and one or more independent variables (the ones you're using to make the prediction). It works by finding the line that minimizes the sum of the squared differences between the actual values and the values predicted by the line.
- **Polynomial Regression**
  - Polynomial regression is a type of supervised learning algorithm used when the relationship between the input features and the output variable is non-linear. Instead of fitting a straight line, it fits a polynomial equation to the data.

### 2.9 What is Unsupervised Learning?
- **Ridge**
  - Ridge Regression is a linear regression technique that adds a penalty to the size of the coefficients. This penalty, known as L2 regularization, shrinks the coefficient values towards zero.

### 2.10 Clustering
- **Overlapping**
  - Overlapping clustering allows data points to belong to multiple clusters simultaneously. Unlike traditional "hard" clustering where each point is assigned to only one cluster, overlapping clustering acknowledges that data points can exhibit characteristics of several groups.
- **Hierarchical**
  - Hierarchical clustering is a method of grouping data points into clusters based on their similarity, building a hierarchy of clusters. It starts by treating each data point as its own cluster and then iteratively merges the closest clusters until only one cluster remains, or a stopping criterion is met.
- **Exclusive**
  - Exclusive clustering, also known as hard clustering, is a type of clustering where each data point can only belong to one cluster. This means there's no overlap between clusters; a data point is definitively assigned to a single group.
- **Probabilistic**
  - Probabilistic clustering assumes that the data is generated from a mixture of probability distributions. Instead of assigning each data point to a single cluster, it provides the probability of a data point belonging to each cluster.

### 2.11 Dimensionality Reduction
- **Gradient Boosting Machines**
  - Gradient Boosting Machines are a type of ensemble learning method that combines multiple weak learners, typically decision trees, to create a strong predictive model for classification tasks. The algorithm works iteratively, with each new tree trained to correct the errors made by the previous trees.
- **Autoencoders**
  - Autoencoders are a type of neural network used to learn efficient data representations in an unsupervised manner. They work by compressing the input data into a lower-dimensional "code" and then reconstructing the original input from this compressed representation.
- **Principal Component Analysis**
  - Principal Component Analysis (PCA) is a technique used to reduce the number of variables in a dataset while preserving the most important information. It transforms the original variables into a new set of variables called principal components, which are ordered by the amount of variance they explain.
- **Lasso**
  - Lasso (Least Absolute Shrinkage and Selection Operator) regression is a linear regression technique that adds a penalty term to the ordinary least squares (OLS) objective function. This penalty is based on the absolute values of the coefficients, effectively shrinking some coefficients towards zero.
- **ElasticNet Regularization**
  - Elastic Net is a regularization technique that combines the penalties of both L1 (Lasso) and L2 (Ridge) regularization methods. It aims to improve model performance by addressing limitations of each individual method, particularly in situations where there are many correlated features.

### 2.12 What is Reinforcement Learning?
- **Policy Gradient**
  - Policy Gradient methods are a type of reinforcement learning algorithm that directly optimizes the policy function, which maps states to actions. Instead of learning a value function (like Q-learning) and then deriving a policy from it, policy gradient methods directly learn the optimal policy by adjusting its parameters to maximize the expected reward.
- **Actor-Critic Methods**
  - Actor-Critic methods in reinforcement learning are a type of algorithm that combines the strengths of both value-based and policy-based approaches. They use two separate models: an "actor" that learns the optimal policy (how to act), and a "critic" that estimates the value function (how good a state or action is).
- **Deep-Q Networks**
  - Deep Q-Networks (DQNs) are a type of reinforcement learning algorithm that combines Q-learning with deep neural networks. Instead of using a traditional Q-table to store Q-values (which represent the expected reward for taking a specific action in a specific state), DQNs use a neural network to approximate the Q-function.
- **Q-Learning**
  - Q-Learning is a type of reinforcement learning algorithm that aims to find the best action to take given the current state. It works by learning a "Q-function," which estimates the expected cumulative reward for taking a specific action in a particular state and following the optimal policy thereafter.

### 2.13 What is Model Evaluation?
- **Precision**
  - Precision measures how accurate a model's positive predictions are. It tells you, out of all the instances the model predicted as positive, what proportion were actually positive.

### 2.14 Why is it important?
- **Recall**
  - Recall measures how well a model identifies all the actual positive cases. It answers the question: "Of all the actual positive instances, how many did the model correctly predict as positive?".

### 2.15 Metrics to Evaluate
- **Accuracy**
  - Accuracy measures how often a machine learning model correctly predicts the outcome. It's calculated by dividing the number of correct predictions by the total number of predictions made.
- **F1-Score**
  - The F1-score is a way to measure how accurate a model is, considering both precision and recall. Precision tells you how many of the positive predictions made by the model were actually correct.
- **ROC-AUC**
  - ROC-AUC, or Receiver Operating Characteristic Area Under the Curve, is a performance measurement for classification problems at various threshold settings. ROC is a probability curve that plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at different threshold values.
- **Confusion Matrix**
  - A confusion matrix is a table that summarizes the performance of a classification model. It displays the counts of true positive, true negative, false positive, and false negative predictions, allowing for a detailed analysis of the model's accuracy and types of errors it makes.

---

## 3. Advanced

### 3.1 Validation Techniques
- **LOOCV**
  - Leave-One-Out Cross-Validation (LOOCV) is a specific type of cross-validation where each single data point in the dataset is used as the test set, while the remaining data points form the training set. This process is repeated for every data point, resulting in as many models being trained and evaluated as there are data points in the original dataset.
- **K-Fold Cross Validation**
  - K-Fold Cross Validation is a technique used to assess how well a machine learning model will generalize to an independent dataset. It works by dividing the available data into k equally sized folds or subsets.

### 3.2 Neural Network (NN) Basics
- **Forward propagation**
  - Forward propagation is the process of feeding input data through a neural network to generate an output. It involves taking the inputs, multiplying them by weights, adding biases, and then passing the result through an activation function at each layer of the network.
- **Back Propagation**
  - Backpropagation is a fundamental algorithm used to train artificial neural networks. It works by calculating the gradient of the loss function with respect to the network's weights.
- **Perceptron, Multi-layer Perceptrons**
  - A perceptron is a fundamental building block of neural networks, acting as a single-layer linear classifier. It takes several inputs, multiplies each by a weight, sums them up, and then applies an activation function to produce an output.
- **Activation Functions**
  - Activation functions in neural networks determine the output of a node given an input or set of inputs. They introduce non-linearity into the network, allowing it to learn complex patterns and relationships in data.

### 3.3 Deep Learning Architectures
- **Log Loss**
  - Log Loss, also known as cross-entropy loss, quantifies the performance of a classification model where the prediction input is a probability value between 0 and 1. It measures the uncertainty of the model's predicted probabilities compared to the actual labels.

### 3.4 Deep Learning Libraries
- **TensorFlow**
  - TensorFlow is an open-source software library created by Google for numerical computation and large-scale machine learning. It provides a flexible architecture and tools that allow users to easily build and deploy machine learning models, particularly deep neural networks.
- **Keras**
  - Keras is a high-level, user-friendly neural networks API written in Python. It acts as an interface for several lower-level backends like TensorFlow, CNTK, and Theano.
- **Scikit-learn**
  - Scikit-learn is a popular Python library mainly used for traditional machine learning tasks like classification, regression, and clustering. While it's not primarily designed for deep learning, it does offer basic tools for creating simple neural networks, specifically multi-layer perceptrons (MLPs).

### 3.5 Convolutional Neural Network
- **Pooling**
  - Pooling is a downsampling technique used in convolutional neural networks (CNNs) to reduce the spatial dimensions of feature maps. It summarizes the features present in a region of the feature map into a single value.
- **Strides**
  - In convolutional neural networks, a stride determines how many pixels the filter (or kernel) shifts horizontally and vertically during the convolution operation. A stride of 1 means the filter moves one pixel at a time, resulting in a more detailed feature map.
- **PyTorch**
  - PyTorch is an open-source machine learning framework primarily developed by Meta AI. It's used for a variety of applications, including computer vision, natural language processing, and reinforcement learning.

### 3.6 Applications of CNNs
- **Image Classification**
  - Convolutional Neural Networks (CNNs) are commonly used for image classification tasks. They work by automatically learning relevant features from images through convolutional layers, which detect patterns like edges and textures.
- **Image Segmentation**
  - Image segmentation involves dividing an image into multiple regions or segments, often to identify objects or boundaries. Convolutional Neural Networks (CNNs) are widely used for this task.
- **Image & Video Recognition**
  - Convolutional Neural Networks (CNNs) are a specialized type of neural network particularly effective at processing images and videos. In image recognition, CNNs can identify objects, scenes, and faces by learning spatial hierarchies of features from pixel data.
- **Recommendation Systems**
  - Convolutional Neural Networks (CNNs), typically used for image processing, can also enhance recommendation systems. They do this by extracting features from user-item interaction data, like purchase history or ratings.
- **LSTM**
  - LSTMs are a special kind of recurrent neural network (RNN) architecture designed to handle the vanishing gradient problem that often occurs when training standard RNNs. They excel at processing sequential data by maintaining a "memory" of past inputs, allowing them to learn long-term dependencies.

### 3.7 Recurrent Neural Networks
- **Loss Functions**
  - Loss functions measure how well the network's predictions match the actual values. They quantify the difference between the predicted output and the true output for a given input.
- **Padding**
  - Padding, in the context of convolutional neural networks, refers to adding extra layers of "pixels" or values around the input image or feature map. This is typically done with zeros (zero-padding), but other values can be used.
- **Convolution**
  - Convolution is a mathematical operation that involves sliding a filter (also known as a kernel) over an input image or feature map. At each location, the filter performs element-wise multiplication with the corresponding part of the input, and then sums the results.
- **RNN**
  - Recurrent Neural Networks (RNNs) are a type of neural network designed to process sequential data. Unlike standard feedforward networks that treat each input independently, RNNs have connections that loop back on themselves, allowing them to maintain a "memory" of past inputs.
- **GRU**
  - A Gated Recurrent Unit (GRU) is a type of recurrent neural network (RNN) architecture. It's designed to handle the vanishing gradient problem often encountered when training standard RNNs, especially with long sequences of data.

### 3.8 Attention Mechanisms
- **Transformers**
  - Transformers are a type of neural network architecture that rely on attention mechanisms to weigh the importance of different parts of the input data. Unlike recurrent neural networks (RNNs) that process data sequentially, transformers can process the entire input at once, allowing for parallelization and capturing long-range dependencies more effectively.
- **Multi-head Attention**
  - Multi-head attention is an attention mechanism that runs through the attention process multiple times independently. Each of these independent attention mechanisms is called a "head." The outputs of all the heads are then concatenated and linearly transformed to produce the final output.
- **Self-Attention**
  - Self-attention is a mechanism that allows a model to focus on different parts of the input sequence when processing it. Instead of treating each element in the sequence independently, self-attention calculates a weighted sum of all elements, where the weights are determined by the relationships between the elements themselves.

### 3.9 Autoencoders
- **Autoencoders**
  - Autoencoders are a type of neural network used for unsupervised learning. They work by compressing the input data into a lower-dimensional representation (encoding) and then reconstructing the original input from this compressed representation (decoding).

### 3.10 Generative Adversarial Networks
- **Generative Adversarial Networks**
  - Generative Adversarial Networks (GANs) are a type of neural network architecture designed to generate new data that resembles the data they were trained on. They consist of two networks: a generator, which creates new data instances, and a discriminator, which evaluates the authenticity of the generated data.

### 3.11 Natural Language Processing
- **Tokenization**
  - Tokenization is the process of breaking down a text string into smaller units called tokens. These tokens can be words, phrases, symbols, or other meaningful elements.
- **Lemmatization**
  - Lemmatization is a text normalization technique in natural language processing used to reduce words to their dictionary form, known as a lemma. Unlike stemming, which simply chops off prefixes or suffixes, lemmatization considers the context of the word and applies morphological analysis to find the base or dictionary form.
- **Stemming**
  - Stemming is a text normalization technique in natural language processing that reduces words to their root or base form, known as the stem. This is achieved by removing suffixes (like "-ing", "-ed", "-s") from words.
- **Embeddings**
  - Embeddings are a way to represent words, phrases, or even entire documents as numerical vectors in a high-dimensional space. The goal is to capture the semantic meaning of the text, so that words with similar meanings are located close to each other in the vector space.
- **Attention Models**
  - Attention models in natural language processing allow a neural network to focus on specific parts of the input sequence when producing an output. Instead of relying on a fixed-length vector representation of the entire input, these models learn to assign weights to different input elements, indicating their relevance to the current output.

### 3.12 Explainable AI
- **Explainable AI**
  - Explainable AI (XAI) focuses on making machine learning models and their decisions understandable to humans. Instead of treating models as black boxes, XAI aims to provide insights into how a model arrives at a particular prediction or decision.

---

## 4. Optional / Specialized Topics

- Determinants, inverse of Matrix
- Basics of Probability
- Bayes Theorem
- Other Data Formats
- Dimensionality Reduction
- Feature Engineering
- Feature Scaling & Normalization
- Prediction
- Model Selection
- ElasticNet Regularization
- LSTM
- GRU
- Attention Models

---

## 5. References

- [Machine Learning Engineer Roadmap](https://roadmap.sh/machine-learning)

---

## 6. Related Roles / Topics

### Related Roles
- AI and Data Scientist
- AI Engineer
- Data Analyst
- Data Engineer

### Related Skills
- Python
- AI Agents