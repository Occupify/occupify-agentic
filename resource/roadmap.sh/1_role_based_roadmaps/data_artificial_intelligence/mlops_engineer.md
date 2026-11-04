# MLOps Engineer

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/mlops
- Related Roles:
  - AI and Data Scientist
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 What is MLOps?
- **MLOps Principles**
  - MLOps principles are the core ideas that guide how teams build and operate ML systems. They include automation of the ML pipeline, reproducibility of experiments and results, continuous testing and monitoring, and collaboration between data scientists, engineers, and operations teams.
- **MLOps Components**
  - MLOps components are the building blocks that together form a working ML pipeline. These usually include version control, CI/CD, orchestration, experiment tracking, data lineage, model training and serving, and monitoring.
- **Version Control**
  - Version control tracks changes to files over time, so teams can see what changed, who changed it, and roll back if needed. In ML projects, this applies not just to code but also to datasets, model files, and configuration.
- **CI/CD**
  - CI/CD stands for Continuous Integration and Continuous Delivery, a practice of automatically testing and shipping code changes. In an ML context, CI/CD pipelines also test data quality, validate model performance, and automate retraining or redeployment when new code or data arrives.
- **Orchestration**
  - Orchestration means coordinating the different steps of an ML workflow so they run in the right order, automatically. A typical pipeline might need to pull data, preprocess it, train a model, evaluate it, then deploy it, and orchestration tools handle scheduling, dependencies, and retries for these steps.
- **Experiment Tracking**
  - Experiment tracking records the details of each model training run, such as hyperparameters, code version, dataset used, and resulting metrics. This makes it possible to compare different runs and understand which changes actually improved the model.
- **Data Lineage**
  - Data lineage is the record of where data comes from, how it moves, and how it gets transformed before reaching a model. It shows the full path from raw source to final training dataset.

### 1.2 Programming Basics
- **Python**
  - Python is a widely used programming language known for its clear syntax and extensive libraries. It's a versatile tool that can handle many tasks, from simple scripting to complex software development.
- **Go**
  - Go, also called Golang, is a programming language known for its simplicity, speed, and strong support for concurrent programs. Many infrastructure and DevOps tools, such as Docker and Kubernetes, are written in Go.
- **Bash**
  - Bash (Bourne Again Shell) is a Unix shell and command language used for interacting with the operating system through a terminal. It allows users to execute commands, automate tasks via scripting, and manage system operations.
- **Model Training & Serving**
  - Model training is the process of teaching a machine learning model to make predictions using data, while serving is making that trained model available to handle real requests. Serving usually involves wrapping the model in an API so applications can send input and get predictions back.
- **Monitoring & Observability**
  - Monitoring and observability track how a system behaves once it is running, using metrics, logs, and alerts. For ML systems, this also means watching model accuracy over time, since predictions can degrade as real-world data shifts away from the training data.
- **SQL**
  - SQL, or Structured Query Language, is a standard language for managing and manipulating data held in relational database management systems (RDBMS). It allows users to define, access, and control data, enabling operations like creating databases, inserting, updating, deleting, and retrieving data based on specific criteria.

### 1.3 Version Control Systems
- **Git**
  - Git is a distributed version control system that tracks changes to files and lets multiple people collaborate on the same codebase. It works by creating commits, which are snapshots of the project at a point in time, and branches, which let people work on separate features in parallel.
- **GitHub**
  - GitHub is a web platform for hosting Git repositories, adding features like pull requests, issue tracking, and code review on top of Git. Teams use it to collaborate on code, review changes before merging, and automate workflows with GitHub Actions.
- **DVC**
  - DVC (Data Version Control) is an open-source tool designed to bring version control principles to machine learning projects, specifically for data and models. It extends Git's capabilities to handle large files, datasets, and machine learning models, which are typically not well-suited for traditional version control systems.

### 1.4 CI/CD
- **Jenkins**
  - Jenkins is an open-source automation server that helps automate the software development processes, including building, testing, and deploying code. It provides a platform for continuous integration and continuous delivery (CI/CD), allowing teams to automate repetitive tasks and streamline their workflows.
- **GItLab**
  - GitLab is a web-based DevOps platform that provides a single application for all stages of the software development lifecycle. It offers features like source code management (using Git), CI/CD pipelines, issue tracking, and project management.
- **GitHub Actions**
  - GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your software development workflows directly in your GitHub repository. You can use it to build, test, and deploy your code, as well as automate other tasks like managing issues and pull requests.
- **CML**
  - Continuous Machine Learning (CML) is a tool designed to bring continuous integration and continuous delivery (CI/CD) principles to machine learning projects. It allows data scientists and machine learning engineers to automate the process of training, evaluating, and deploying machine learning models.

---

## 2. Intermediate

### 2.1 ML Fundamentals
- **TensorFlow**
  - TensorFlow is an open-source software library created by Google for numerical computation and large-scale machine learning. It provides a comprehensive ecosystem of tools, libraries, and community resources that allows researchers and developers to build and deploy ML-powered applications.
- **Scikit-learn**
  - Scikit-learn is a Python library that provides simple and efficient tools for data mining and data analysis. It features various classification, regression, clustering algorithms, and tools for model selection, preprocessing, and dimensionality reduction.
- **PyTorch**
  - PyTorch is an open-source machine learning framework primarily developed by Meta AI. It's used for a variety of applications, including computer vision, natural language processing, and reinforcement learning.
- **MLFlow**
  - MLflow is an open-source platform designed to manage the complete machine learning lifecycle. It provides tools for tracking experiments, packaging code into reproducible runs, and deploying models to various platforms.
- **Deep Learning**
  - Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to analyze data with complex structures. These networks learn hierarchical representations of data, where each layer extracts increasingly abstract features from the previous layer.
- **Machine Learning**
  - Machine learning is a method of teaching computers to find patterns in data and make predictions or decisions without being explicitly programmed for the task. A model learns from examples during training, then applies what it learned to new, unseen data.
- **Maths & Statistics**
  - Mathematics and statistics provide the foundational principles for understanding and building machine learning models. These disciplines offer the tools to analyze data, quantify uncertainty, and optimize model performance.
- **Model Evaluation**
  - Model evaluation is the process of assessing the performance of a machine learning model using various metrics and techniques. It helps determine how well the model generalizes to unseen data and whether it meets the desired performance criteria.

### 2.2 Cloud Computing
- **AWS / Azure / GCP**
  - AWS, Azure, and GCP are the three largest cloud computing providers, each offering a wide range of services for computing, storage, networking, and machine learning. They differ in pricing, tooling, and specific service names, but cover similar core capabilities.
- **Cloud-native ML Services**
  - Cloud-native ML services are pre-built machine learning tools and platforms offered by cloud providers. These services allow users to build, train, and deploy machine learning models without managing the underlying infrastructure.

### 2.3 Containerization
- **Docker**
  - Docker is a platform that uses operating system-level virtualization to deliver software in packages called containers. These containers isolate software from its environment and ensure that it works uniformly despite differences between development and production environments.
- **Kubernetes**
  - Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery.

### 2.4 Data Engineering Basics
- **Data Pipelines**
  - Data pipelines are a series of automated processes that transport and transform data from various sources to a destination for analysis or storage. They typically involve steps like data extraction, cleaning, transformation, and loading (ETL) into databases, data lakes, or warehouses.
- **Data Lakes & Warehouses**
  - Data lakes and data warehouses are both systems for storing large amounts of data, but they differ in structure and purpose. A data lake stores data in its raw, unprocessed format, allowing for flexibility in analysis and exploration.
- **Data Ingestion Arch.**
  - Data ingestion architecture describes how data flows into a system from its original sources, such as databases, APIs, or streaming platforms. It defines whether data arrives in batches or in real time, and how it gets validated and stored along the way.
- **Spark**
  - Spark, or Apache Spark, is an open-source engine for processing large amounts of data across many machines at once. It supports batch and streaming data processing, along with built-in libraries for SQL queries and machine learning.
- **Kafka**
  - Kafka is a distributed, fault-tolerant, high-throughput streaming platform. It's primarily used for building real-time data pipelines and streaming applications, allowing you to publish, subscribe to, store, and process streams of records.
- **Flink**
  - Apache Flink is an open-source stream processing framework designed for real-time and batch data processing with low latency and high throughput. It supports event time processing, fault tolerance, and stateful operations, making it ideal for applications like real-time analytics, fraud detection, and event-driven systems.

### 2.5 Infrastructure as Code
- **Terraform**
  - Terraform is an open-source infrastructure as code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language. It enables you to manage infrastructure resources across various cloud providers and on-premises environments in a consistent and automated manner.
- **Ansible**
  - Ansible is an open-source automation tool used to configure systems, deploy software, and orchestrate more advanced IT tasks. It uses a simple, human-readable language (YAML) to define automation tasks, called playbooks.

---

## 3. Advanced

### 3.1 Orchestration
- **Airflow**
  - Airflow is a platform used to programmatically author, schedule, and monitor workflows. It allows you to define workflows as Directed Acyclic Graphs (DAGs) of tasks, where each task represents a unit of work.
- **KubeFlow**
  - Kubeflow is an open-source machine learning platform designed to simplify the deployment and management of ML workflows on Kubernetes. It provides tools and components for building, training, and deploying machine learning models, allowing users to create portable and scalable ML pipelines.

### 3.2 Monitoring & Observability
- **Prometheus**
  - Prometheus is an open-source monitoring and alerting toolkit originally built at SoundCloud. It collects and stores metrics as time-series data, meaning metrics are stored with a timestamp at which they were recorded, along with optional key-value pairs called labels.
- **Grafana**
  - Grafana is an open-source data visualization and monitoring tool. It allows users to query, visualize, alert on, and explore metrics, logs, and traces.

### 3.3 Edge AI
- **Jetson**
  - NVIDIA Jetson is a series of embedded computing systems designed for AI and robotics applications. These systems-on-modules (SoMs) provide high-performance processing capabilities in a compact, energy-efficient form factor, enabling developers to deploy AI models and perform complex computations directly on edge devices.
- **PyTorch Mobile**
  - PyTorch Mobile is a framework that allows you to run PyTorch models directly on mobile devices, like smartphones and tablets. It enables on-device machine learning inference, meaning the model computations happen locally without needing a network connection to a remote server.

### 3.4 Explainable AI
- **TFLite**
  - TFLite is a lightweight version of TensorFlow, designed for running machine learning models on mobile, embedded, and IoT devices. It enables on-device inference, meaning models can be executed directly on the device without needing a network connection or relying on cloud-based processing.
- **LIME**
  - LIME (Local Interpretable Model-agnostic Explanations) is a technique used to understand the predictions of machine learning models by approximating them locally with a more interpretable model. It focuses on explaining individual predictions by perturbing the input data around a specific instance and observing how the model's prediction changes.
- **SHAP**
  - SHAP (SHapley Additive exPlanations) is a method used to explain the output of any machine learning model. It uses concepts from game theory to assign each feature a value representing its contribution to the prediction.

---

## 4. Optional / Specialized Topics

- Orchestration
- Experiment Tracking
- Data Lineage
- Monitoring & Observability
- SQL
- Deep Learning
- Machine Learning
- Maths & Statistics
- Model Evaluation
- Kafka
- Flink

---

## 5. References

- [MLOps Engineer Roadmap](https://roadmap.sh/mlops)

---

## 6. Related Roles / Topics

### Related Roles
- AI and Data Scientist
- DevOps Engineer
- Backend Developer

### Related Skills
- Python
- Go