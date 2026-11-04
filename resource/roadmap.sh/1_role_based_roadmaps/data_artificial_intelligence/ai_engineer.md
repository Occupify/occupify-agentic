# AI Engineer

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ai-engineer
- Related Roles:
  - AI and Data Scientist
  - Data Analyst
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is an AI Engineer?**
  - AI engineers are professionals who specialize in designing, developing, and implementing artificial intelligence (AI) systems. Their work is essential in various industries, as they create applications that enable machines to perform tasks that typically require human intelligence, such as problem-solving, learning, and decision-making.
- **AI Engineer vs ML Engineer**
  - An AI Engineer uses pre-trained models and existing AI tools to improve user experiences. They focus on applying AI in practical ways, without building models from scratch.
- **Large Language Model (LLM)**
  - An LLM (Large Language Model) is an AI trained on vast text datasets to understand and generate human-like language via next-token prediction. While it natively handles tasks like translation, summarization, and writing, capabilities like web browsing or code execution come from software layers wrapped around the model.
- **AI vs AGI**
  - AI (Artificial Intelligence) refers to systems designed to perform specific tasks by mimicking aspects of human intelligence, such as pattern recognition, decision-making, and language processing. These systems, known as "narrow AI," are highly specialized, excelling in specific areas such as image classification or recommender algorithms but lacking broader cognitive abilities.
- **Impact on Product Development**
  - AI engineering transforms product development by automating tasks, enhancing data-driven decision-making, and enabling the creation of smarter, more personalized products. It speeds up design cycles, optimizes processes, and allows for predictive maintenance, quality control, and efficient resource management.
- **Roles and Responsiblities**
  - AI Engineers are responsible for designing, developing, and deploying AI systems that solve real-world problems. Their roles include building machine learning models, implementing data processing pipelines, and integrating AI solutions into existing software or platforms.

### 1.2 How LLMs Work
- **Inference**
  - In artificial intelligence (AI), inference refers to the process by which a trained machine learning model makes predictions or draws conclusions from new, unseen data. Unlike training, inference involves the model applying what it has learned to make decisions without needing examples of the exact result.
- **Training**
  - Training refers to the process of teaching a machine learning model to recognize patterns and make predictions by exposing it to a dataset. During training, the model learns from the data by adjusting its internal parameters to minimize errors between its predictions and the actual outcomes.
- **Vector DBs**
  - Vector databases are specialized systems designed to store, index, and retrieve high-dimensional vectors, often used as embeddings that represent data like text, images, or audio. Unlike traditional databases that handle structured data, vector databases excel at managing unstructured data by enabling fast similarity searches, where vectors are compared to find those that are most similar to a query.
- **RAGs**
  - Retrieval-Augmented Generation (RAG) is an AI approach that combines information retrieval with language generation to create more accurate, contextually relevant outputs. It works by first retrieving relevant data from a knowledge base or external source, then using a language model to generate a response based on that information.
- **Prompt Engineering**
  - Prompt engineering is the art and science of crafting effective prompts, which are the instructions or inputs given to a large language model (LLM). The goal is to design prompts that elicit the desired response from the LLM, guiding it to generate accurate, relevant, and creative outputs.
- **AI Agents**
  - In AI engineering, "agents" refer to autonomous systems or components that can perceive their environment, make decisions, and take actions to achieve specific goals. Agents often interact with external systems, users, or other agents to carry out complex tasks.
- **Tokens**
  - Tokens are fundamental units of text that LLMs process, created by breaking text into smaller components such as words, subwords, or characters. Understanding tokens is crucial because models predict the next token in sequences, API costs are based on token count, and models have maximum token limits for input and output.
- **Context**
  - Context, in the realm of Large Language Models (LLMs), refers to the information provided to the model alongside the prompt, which it uses to generate a relevant and coherent response. It encompasses the user's query, any supporting text, previous turns in a conversation, or any other data that helps the LLM understand the desired output.
- **Top-K**
  - Top-K sampling is a method used by Large Language Models (LLMs) during text generation to select the next word. Instead of considering the entire vocabulary, it narrows down the choices to the K most probable words predicted by the model.
- **Top-P**
  - Top-P sampling, also known as nucleus sampling, is a technique used in language models to generate text. Instead of considering all possible next words, it focuses on the smallest set of words whose cumulative probability exceeds a threshold 'P'.
- **Fine-tuning**
  - Fine-tuning involves taking a pre-trained large language model (LLM) and further training it on a smaller, task-specific dataset. This adapts the LLM to perform better on a particular task or domain.
- **Inference Engineering**
  - Inference engineering is the practice of making generative AI models faster, less expensive, and more reliable to serve in production. It spans the full stack from CUDA kernels and GPU architecture to Kubernetes autoscaling and multi-cloud capacity management.
- **Repetition Penalties**
  - Repetition penalties discourage LLMs from repeating words or phrases by reducing the probability of selecting previously used tokens. This includes frequency penalty (scales with usage count) and presence penalty (applies equally to any used token).
- **Embeddings**
  - Embeddings are dense, continuous vector representations of data, such as words, sentences, or images, in a lower-dimensional space. They capture the semantic relationships and patterns in the data, where similar items are placed closer together in the vector space.
- **Sampling Parameters**
  - Sampling parameters are settings that control the randomness and creativity of the text generated by the LLM. They influence how the model chooses the next word in a sequence, impacting the overall coherence, diversity, and relevance of the output.
- **Temperature**
  - Temperature is a parameter used in language models that controls the randomness of the generated text. A higher temperature value (e.g., 1.0) leads to more diverse and unpredictable outputs, as the model is more likely to sample less probable words.
- **Context Window**
  - The context window is the amount of text an LLM can process in a single request, measured in tokens. It includes the system prompt, conversation history, retrieved documents, and the model's own output as it generates a response.

### 1.3 Prompt Engineering
- **Input Format**
  - Input format in prompt engineering deals with how you structure and present your prompt to a large language model (LLM). This includes the specific words used, the overall layout, and the inclusion of any examples or instructions.
- **System Prompting**
  - System prompting sets the overall context, purpose, and operational guidelines for LLMs. It defines the model's role, behavioral constraints, output format requirements, and safety guardrails.
- **Context**
  - Contextual prompting provides specific background information or situational details relevant to the current task, helping LLMs understand nuances and tailor responses accordingly. Unlike system or role prompts, contextual prompts supply immediate, task-specific information that's dynamic and changes based on the situation.
- **Role & Behavior**
  - System prompting involves crafting instructions that define the AI model's role, personality, and overall behavior when interacting with users. This allows you to shape the AI's responses, ensuring they are consistent with desired guidelines, such as adopting a specific persona (e.g., a helpful assistant, an expert) or adhering to constraints on tone and style.
- **Constraints**
  - Constraining system prompts involves explicitly defining boundaries and limitations within the instructions given to a large language model (LLM). This technique focuses on guiding the LLM to operate within a specific scope, preventing it from generating irrelevant, harmful, or factually incorrect responses by setting rules and restrictions on its behavior and output format.
- **Context vs Prompt Eng.**
  - Prompt engineering focuses on how a single instruction is worded to get a better response from a model. Context engineering is broader: it deals with what information reaches the model at all, from which sources, in what order, and in what format, across an entire application or agent workflow.
- **Context Sources**
  - Context sources are the places an AI system pulls information from to build what a model sees at inference time. Common sources include documents and knowledge bases, databases and data warehouses, code repositories, chat and support tools, and the outputs of other tool calls or agents.
- **MCP**
  - MCP, or Model Context Protocol, is an open standard that lets AI applications connect to external tools, data sources, and services in a consistent way. Instead of writing a custom integration for every tool a model might need, developers expose that tool through an MCP server, and any MCP compatible client can then call it.
- **Context Security**
  - Context security covers the risks that come from feeding external or untrusted content into an AI system. A malicious document, email, or web page can contain hidden instructions designed to manipulate the model, a technique known as prompt injection.
- **What is a Context Layer?**
  - A context layer is the part of an AI system responsible for gathering, organizing, and delivering the right information to a model before it generates a response. It sits between raw data sources, such as databases, documents, and APIs, and the model itself, deciding what gets included and what gets left out.
- **Context Engineering**
  - Context engineering is the practice of carefully designing and organizing the information you give to an AI model so it can do its job better. Think of it like preparing everything an AI needs before it starts working (including providing the right instructions, examples, background knowledge, and conversation history), all put together smartly so the model gives you the best possible answer.

### 1.4 Context Engineering
- **ReAct**
  - ReAct (Reason and Act) prompting enables LLMs to solve complex tasks by combining reasoning with external tool interactions. It follows a thought-action-observation loop: analyze the problem, perform actions using external APIs, review results, and iterate until solved.
- **CoT**
  - Chain of Thought (CoT) is a way for an AI agent to think out loud. Before giving its final answer, the agent writes short notes that show each step it takes.
- **Zero-Shot**
  - Zero-shot prompting is a prompt engineering method that relies on the pretraining of a large language model (LLM) to infer an appropriate response. In contrast to other prompt engineering methods, such as few-shot prompting, models aren’t provided with examples of output when prompting with the zero-shot technique.
- **Few-Shot**
  - Few-shot prompting is a technique used with large language models (LLMs) where you provide a small number of example input-output pairs in the prompt itself. These examples demonstrate the desired behavior of the LLM for a specific task.
- **Structured Output**
  - Structured output in system prompting refers to designing prompts that guide a Large Language Model (LLM) to generate responses in a predefined format, such as JSON, XML, or a specific text-based structure. This approach focuses on crafting system prompts to elicit predictable and parseable outputs, making it easier to integrate LLM responses into downstream applications and workflows.
- **Function Calling**
  - Function calling allows Large Language Models (LLMs) to interact with external tools and APIs. Instead of just generating text, the LLM can be instructed to recognize when a specific function should be called based on the user's input, and then output the arguments needed to execute that function.
- **Prompt Caching**
  - Prompt caching is a technique that stores the results of previous LLM prompts, allowing you to quickly retrieve and reuse them instead of re-running the prompt every time. This can significantly improve efficiency and reduce costs when dealing with frequently used or computationally expensive prompts.
- **RAG & Dynamic Filters**
  - Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by providing them with relevant, up-to-date information from external sources. Dynamic filters are techniques that selectively filter the information retrieved for RAG, ensuring that the LLM receives only the most pertinent context based on the specific query and user.
- **Context Compaction**
  - Context compaction is a technique used to reduce the length of the context provided to a large language model (LLM) without sacrificing relevant information. This process aims to remove redundant, irrelevant, or less important information from the context window to make room for more data or improve the efficiency and effectiveness of the LLM's processing.
- **Context Evaluation**
  - Context evaluation measures whether the information delivered to a model actually helps it perform a task well. This includes checking whether retrieved documents are relevant, whether important details are missing, and whether irrelevant or outdated content is crowding out what matters.
- **Long-Context Processing**
  - Long-context processing deals with feeding an AI model large amounts of text, such as entire codebases, long documents, or extended conversation histories, in a way that keeps the model accurate. Even when a model's context window is technically large enough, performance can degrade as the amount of content grows, a problem often called context rot.
- **Memory Systems**
  - Memory systems let an AI agent retain information across interactions instead of starting fresh every time. Short-term memory usually covers the current session, while long-term memory stores facts, preferences, or past decisions that persist across sessions.

### 1.5 Type of Models
- **Pre-trained Models**
  - Pre-trained models are Machine Learning (ML) models that have been previously trained on a large dataset to solve a specific task or set of tasks. These models learn patterns, features, and representations from the training data, which can then be fine-tuned or adapted for other related tasks.
- **Closed vs Open Source Models**
  - Open-source models are freely available for customization and collaboration, promoting transparency and flexibility, while closed-source models are proprietary, offering ease of use but limiting modification and transparency.
- **Streaming Responses**
  - Streamed responses is one of the techniques an AI agent can use to send its answer to the user. With a streamed response, the agent starts sending words as soon as it generates them.
- **Self-Hosted Models**
  - Self-hosted AI models are machine learning models that are deployed and run on your own infrastructure, rather than relying on a third-party service or cloud provider. This means you have complete control over the hardware, software, and data used to run the model, allowing for greater customization, security, and potentially lower long-term costs, depending on your specific needs and scale.
- **Context Isolation**
  - Context isolation is about keeping different tasks or areas of knowledge separate when working with large language models (LLMs). Think of it like giving each task its own dedicated space.
- **Multi-agent Context Sharing**
  - Multi-agent context sharing covers how separate AI agents working on related tasks exchange the information each one needs. When one agent hands off a task to another, it has to pass along enough history and data for the second agent to continue without repeating work or losing important details.
- **State & Historical Context**
  - State and historical context refers to tracking what has already happened in a conversation or workflow so an agent can act consistently over time. This includes the sequence of user messages, past tool calls and their results, and any decisions the agent has already made.
- **Context Failure Modes**
  - Context failure modes are the common ways a context pipeline can go wrong and degrade an agent's performance. These include context poisoning, where incorrect information gets included and treated as fact, context distraction, where too much irrelevant content pulls the model's attention away from what matters, and context rot, where accuracy drops as the amount of content grows even within the model's stated limits.
- **PostHog**
  - PostHog is a product analytics platform that also offers what it calls a context warehouse, a combined store of product event data, session replays, and business context from tools like Slack and support tickets. Rather than requiring a separate ETL pipeline to move data between systems, PostHog exposes this combined data directly to AI agents through its MCP server, letting an agent query product behavior and business context using the same interface a person would use.
- **modus**
  - modus is a Context Warehouse, an infrastructure layer that sits between a company's internal data stack and its AI agents. Instead of asking teams to hand-model semantics, it mines context from how the organization already uses its data (query logs, dbt models, dashboards, pipelines, code, docs) and keeps that understanding current as the business changes.
- **Atlan**
  - Atlan is a data catalog and governance platform that helps organizations discover, document, and manage their data assets across warehouses, pipelines, and BI tools. It provides a searchable inventory of datasets along with lineage, ownership, and quality information, so teams know where data comes from and whether it can be trusted.
- **DataHub**
  - DataHub is an open source metadata platform originally built at LinkedIn for cataloging and managing data across an organization. It tracks where data lives, how it flows between systems, who owns it, and how it is used, giving teams a searchable map of their data assets.

### 1.6 Hugging Face
- **Hugging Face Tasks**
  - Hugging Face supports text classification, named entity recognition, question answering, summarization, and translation. It also extends to multimodal tasks that involve both text and images, such as visual question answering (VQA) and image-text matching.

### 1.7 Choosing the Right Model
- **Anthropic Claude**
  - Anthropic's Claude is an AI language model designed to facilitate safe and scalable AI systems. Named after Claude Shannon, the father of information theory, Claude focuses on responsible AI use, emphasizing safety, alignment with human intentions, and minimizing harmful outputs.
- **Google Gemini**
  - Google Gemini is an advanced AI model by Google DeepMind, designed to integrate natural language processing with multimodal capabilities, enabling it to understand and generate not just text but also images, videos, and other data types. It combines generative AI with reasoning skills, making it effective for complex tasks requiring logical analysis and contextual understanding.
- **OpenAI (GPT, o-series)**
  - OpenAI models, including the GPT and "o-series" (like Whisper), are pre-trained AI models offered by OpenAI, accessible via their API. GPT models excel at natural language tasks like text generation, translation, and question answering.
- **Meta Llama**
  - Meta Llama is a family of large language models (LLMs) developed by Meta AI. These models are designed to be open-source and accessible, allowing researchers and developers to build and experiment with LLMs without the restrictions of proprietary models.
- **Mistral**
  - Mistral AI is a company focused on developing open-weight, large language models (LLMs) to provide high-performance AI solutions. Mistral aims to create models that are both efficient and versatile, making them suitable for a wide range of natural language processing tasks, including text generation, translation, and summarization.
- **Cohere**
  - Cohere offers a suite of closed large language models (LLMs) designed for various natural language processing tasks. These models are accessible through an API and are trained and maintained by Cohere, meaning users don't have to worry about the complexities of training and fine-tuning their own models from scratch.

---

## 2. Intermediate

### 2.1 Ollama
- **Hugging Face Hub**
  - The Hugging Face Hub is a central platform where users can discover, share, and collaborate on pre-trained models, datasets, and demos for machine learning. It hosts a vast repository of resources contributed by the community, allowing users to easily access and integrate these assets into their AI projects.
- **Transformers.js**
  - Transformers.js is a JavaScript library that enables transformer models, like those from Hugging Face, to run directly in the browser or Node.js, without needing cloud services. It supports tasks such as text generation, sentiment analysis, and translation within web apps or server-side scripts.

### 2.2 LM Studio
- **LM Studio**
  - LM Studio is a desktop application designed for discovering, downloading, and running large language models (LLMs) locally on your computer. It provides a user-friendly interface to experiment with different open-source LLMs without needing extensive technical knowledge or cloud infrastructure.

### 2.3 OpenRouter
- **Hugging Face Inference SDK**
  - The Hugging Face Inference SDK is a powerful tool that allows developers to easily integrate and run inference on large language models hosted on the Hugging Face Hub. By using the InferenceClient, users can make API calls to various models for tasks such as text generation, image creation, and more.
- **OpenAI Response API**
  - The OpenAI Response API allows developers to interact with various AI models offered by OpenAI. It provides a structured way to send requests to these models and receive generated text, code, or other outputs.
- **Google Gemini APi**
  - The Google Gemini API provides developers with programmatic access to Google's Gemini family of multimodal AI models. It allows applications to understand and generate content across text, images, audio, and video.
- **Claude Messages API**
  - The Claude Messages API provides a structured way to interact with the Claude AI model. It allows developers to send a series of messages to Claude, mimicking a conversation.

### 2.4 What are Embeddings
- **Semantic Search**
  - Embeddings are used for semantic search by converting text, such as queries and documents, into high-dimensional vectors that capture the underlying meaning and context, rather than just exact words. These embeddings represent the semantic relationships between words or phrases, allowing the system to understand the query’s intent and retrieve relevant information, even if the exact terms don’t match.
- **Recommendation Systems**
  - In the context of embeddings, recommendation systems use vector representations to capture similarities between items, such as products or content. By converting items and user preferences into embeddings, these systems can measure how closely related different items are based on vector proximity, allowing them to recommend similar products or content based on a user's past interactions.
- **Anomaly Detection**
  - Anomaly detection with embeddings works by transforming data, such as text, images, or time-series data, into vector representations that capture their patterns and relationships. In this high-dimensional space, similar data points are positioned close together, while anomalies stand out as those that deviate significantly from the typical distribution.
- **Data Classification**
  - Once data is embedded, a classification algorithm, such as a neural network or a logistic regression model, can be trained on these embeddings to classify the data into different categories. The advantage of using embeddings is that they capture underlying relationships and similarities between data points, even if the raw data is complex or high-dimensional, improving classification accuracy in tasks like text classification, image categorization, and recommendation systems.
- **DeepSeek**
  - DeepSeek refers to a family of large language models (LLMs) developed by DeepSeek AI. These models are designed to be powerful and efficient, capable of handling various natural language processing tasks such as text generation, translation, and question answering.
- **Gemma**
  - Gemma is a family of open-source large language models (LLMs) developed by Google. These models are designed to be lightweight and high-performing, making them suitable for a variety of tasks, including text generation, question answering, and code completion.
- **Qwen**
  - Qwen is a series of large language models (LLMs) developed by Alibaba Group. These models are open-source, meaning their code and architecture are publicly available, allowing researchers and developers to use, study, and modify them for their own purposes.

### 2.5 Embedding Models
- **Open AI Embeddings API**
  - The OpenAI Embeddings API provides a straightforward way to transform text into numerical vector representations called embeddings. These embeddings capture the semantic meaning of text, allowing you to perform tasks like semantic search, clustering, and similarity comparison by analyzing the relationships between these vectors.
- **Purpose and Functionality**
  - A vector database is designed to store, manage, and retrieve high-dimensional vectors (embeddings) generated by AI models. Its primary purpose is to perform fast and efficient similarity searches, enabling applications to find data points that are semantically or visually similar to a given query.
- **OpenAI-compatible APIs**
  - OpenAI-compatible APIs are interfaces that mimic the structure and functionality of OpenAI's API. These APIs allow developers to switch between different language models or providers with minimal code changes.

### 2.6 Vector Databases
- **Cohere**
  - Cohere offers powerful text embeddings, which are numerical representations of text data. These embeddings capture the semantic meaning of words, sentences, and documents, allowing AI models to understand relationships and perform tasks like similarity search, clustering, and information retrieval.
- **Gemini Embedding**
  - The Gemini API offers methods to convert text, images, or other data types into numerical vector representations called embeddings. These embeddings capture the semantic meaning and relationships between different pieces of information, allowing for efficient similarity search, clustering, and other machine learning tasks.
- **Jina**
  - Jina Embeddings are a family of high-performance, open-source, multilingual, and multimodal embedding models developed by Jina AI. They transform text and visual data (like images and charts) into dense numerical vectors for semantic search, RAG, and AI applications.
- **Sentence Transformers**
  - Sentence Transformers are a type of model designed to generate high-quality embeddings for sentences, allowing them to capture the semantic meaning of text. Unlike traditional word embeddings, which represent individual words, Sentence Transformers understand the context of entire sentences, making them ideal for tasks that require semantic similarity, such as sentence clustering, semantic search, and paraphrase detection.
- **Models on Hugging Face**
  - Embedding models are used to convert raw data like text, code, or images into high-dimensional vectors that capture semantic meaning. These vector representations allow AI systems to compare, cluster, and retrieve information based on similarity rather than exact matches.
- **Chroma**
  - Chroma is an open-source vector database and AI-native embedding database designed to handle and store large-scale embeddings and semantic vectors. It is used in applications that require fast, efficient similarity searches, such as natural language processing (NLP), machine learning (ML), and AI systems dealing with text, images, and other high-dimensional data.
- **Pinecone**
  - Pinecone is a managed vector database designed for efficient similarity search and real-time retrieval of high-dimensional data, such as embeddings. It allows developers to store, index, and query vector representations, making it easy to build applications like recommendation systems, semantic search, and AI-driven content discovery.
- **Weaviate**
  - Weaviate is an open-source vector database that allows users to store, search, and manage high-dimensional vectors, often used for tasks like semantic search and recommendation systems. It enables efficient similarity searches by converting data (like text, images, or audio) into embeddings and indexing them for fast retrieval.
- **FAISS**
  - FAISS (Facebook AI Similarity Search) is a library developed by Facebook AI for efficient similarity search and clustering of dense vectors, particularly useful for large-scale datasets. It is optimized to handle embeddings (vector representations) and enables fast nearest neighbor search, allowing you to retrieve similar items from a large collection of vectors based on distance or similarity metrics like cosine similarity or Euclidean distance.
- **LanceDB**
  - LanceDB is a vector database designed for efficient storage, retrieval, and management of embeddings. It enables users to perform fast similarity searches, particularly useful in applications like recommendation systems, semantic search, and AI-driven content retrieval.
- **Qdrant**
  - Qdrant is an open-source vector database designed for efficient similarity search and real-time data retrieval. It specializes in storing and indexing high-dimensional vectors (embeddings) to enable fast and accurate searches across large datasets.
- **Supabase**
  - Supabase Vector is an extension of the Supabase platform, specifically designed for AI and machine learning applications that require vector operations. It leverages PostgreSQL's pgvector extension to provide efficient vector storage and similarity search capabilities.

### 2.7 What are RAGs?
- **MongoDB Atlas**
  - MongoDB Atlas, traditionally known for its document database capabilities, now includes vector search functionality, making it a strong option as a vector database. This feature allows developers to store and query high-dimensional vector data alongside regular document data.
- **Indexing Embeddings**
  - Embeddings are stored in a vector database by first converting data, such as text, images, or audio, into high-dimensional vectors using machine learning models. These vectors, also called embeddings, capture the semantic relationships and patterns within the data.
- **Performing Similarity Search**
  - In a similarity search, the process begins by converting the user’s query (such as a piece of text or an image) into an embedding—a vector representation that captures the query’s semantic meaning. This embedding is generated using a pre-trained model, such as BERT for text or a neural network for images.
- **RAG Usecases**
  - Retrieval-Augmented Generation (RAG) enhances applications like chatbots, customer support, and content summarization by combining information retrieval with language generation. It retrieves relevant data from a knowledge base and uses it to generate accurate, context-aware responses, making it ideal for tasks such as question answering, document generation, and semantic search.
- **RAG vs Fine-tuning**
  - RAG (Retrieval-Augmented Generation) and fine-tuning are two approaches to enhancing language models, but they differ in methodology and use cases. Fine-tuning involves training a pre-trained model on a specific dataset to adapt it to a particular task, making it more accurate for that context but limited to the knowledge present in the training data.
- **Chunking**
  - The chunking step in Retrieval-Augmented Generation (RAG) involves breaking down large documents or data sources into smaller, manageable chunks. This is done to ensure that the retriever can efficiently search through large volumes of data while staying within the token or input limits of the model.
- **Embedding**
  - In Retrieval-Augmented Generation (RAG), embeddings are essential for linking information retrieval with natural language generation. Embeddings represent both the user query and documents as dense vectors in a shared space, enabling the system to retrieve relevant information based on similarity.

### 2.8 AI Agents
- **Vector Database**
  - When implementing Retrieval-Augmented Generation (RAG), a vector database is used to store and efficiently retrieve embeddings, which are vector representations of data like documents, images, or other knowledge sources. During the RAG process, when a query is made, the system converts it into an embedding and searches the vector database for the most relevant, similar embeddings (e.g., related documents or snippets).
- **Retrieval Process**
  - The retrieval process in Retrieval-Augmented Generation (RAG) involves finding relevant information from a large dataset or knowledge base to support the generation of accurate, context-aware responses. When a query is received, the system first converts it into a vector (embedding) and uses this vector to search a database of pre-indexed embeddings, identifying the most similar or relevant data points.
- **Generation**
  - Generation refers to the process where a generative language model, such as GPT, creates a response based on the information retrieved during the retrieval phase. After relevant documents or data snippets are identified using embeddings, they are passed to the generative model, which uses this information to produce coherent, context-aware, and informative responses.
- **Using SDKs Directly**
  - While tools like Langchain and LlamaIndex make it easy to implement RAG, you don't have to necessarily learn and use them. If you know about the different steps of implementing RAG, you can simply do it all yourself e.g., do the chunking using @langchain/textsplitters package, create embeddings using any LLM e.g., use OpenAI Embedding API through their SDK, save the embeddings to any vector database e.g.
- **Tools & Function Calling**
  - Tools and function calling equip AI agents with the ability to interact with the real world and access external information. Instead of just providing text-based responses, the agent can use predefined functions, tools, or APIs to perform specific actions like searching the web, sending emails, or controlling devices.
- **Agents Usecases**
  - AI Agents have a variety of use cases ranging from customer support, workflow automation, cybersecurity, finance, marketing, and sales, and more.
- **ReAct Prompting**
  - ReAct prompting is a technique that combines reasoning and action by guiding language models to think through a problem step-by-step and then take specific actions based on the reasoning. It encourages the model to break down tasks into logical steps (reasoning) and perform operations, such as calling APIs or retrieving information (actions), to reach a solution.
- **Multi-agents**
  - Multi-agent systems involve the coordinated behavior of multiple intelligent agents within an environment. These agents interact with each other, potentially cooperating or competing, to achieve individual or collective goals.

### 2.9 Model Context Protocol (MCP)
- **Langchain**
  - LangChain is a development framework that simplifies building applications powered by language models, enabling seamless integration of multiple AI models and data sources. It focuses on creating chains, or sequences, of operations where language models can interact with databases, APIs, and other models to perform complex tasks.
- **Llama Index**
  - LlamaIndex, formerly known as GPT Index, is a tool designed to facilitate the integration of large language models (LLMs) with structured and unstructured data sources. It acts as a data framework that helps developers build retrieval-augmented generation (RAG) applications by indexing various types of data, such as documents, databases, and APIs, enabling LLMs to query and retrieve relevant information efficiently.
- **Manual Implementation**
  - Manually implementing AI agents involves crafting their logic and behavior from the ground up, without relying heavily on pre-built frameworks or automated tools. This approach requires writing code to define how the agent perceives its environment, makes decisions, and takes actions, often involving explicit programming of algorithms for tasks like perception, planning, and learning.
- **OpenAI AgentKit & Agent SDK**
  - OpenAI AgentKit is a framework designed to simplify the process of creating AI agents that can perform specific tasks by leveraging large language models (LLMs). It provides tools and abstractions for managing agent state, defining agent behavior, and connecting agents to various tools and resources, allowing developers to build more complex and capable AI systems without needing to manage all the low-level details.
- **Claude Agent SDK**
  - The Claude Agent SDK provides tools and libraries to build autonomous AI agents powered by Anthropic's Claude models. It simplifies the development process by offering pre-built components and abstractions for tasks such as planning, tool usage, memory management, and human interaction.
- **Haystack**
  - Haystack is an open-source Python framework that helps you build search and question-answering agents fast. You connect your data sources, pick a language model, and set up pipelines that find the best answer to a user’s query.
- **RAGFlow**
  - RAGFlow is a framework designed to streamline the creation, evaluation, and deployment of Retrieval-Augmented Generation (RAG) pipelines. It provides tools and abstractions for building modular RAG systems, allowing developers to easily experiment with different components like data loaders, retrievers, and generators, and then assess their performance.
- **MCP Host**
  - The MCP Host is a central component within the Model Context Protocol (MCP) framework, responsible for managing and coordinating interactions between AI agents and the environment. It acts as a bridge, providing a standardized interface for agents to access and utilize contextual information, tools, and resources.
- **MCP Server**
  - The MCP Server acts as a central hub for managing and serving contextual information to AI agents. It's responsible for receiving requests from agents, retrieving relevant context from various data sources, and delivering that context in a standardized format.
- **MCP Client**
  - The MCP Client is a software component that allows AI agents to interact with a Model Context Protocol (MCP) server. It handles the communication, serialization, and deserialization of data exchanged between the agent and the server, enabling the agent to access and manage contextual information relevant to its tasks.
- **Vertex AI Agent Builder**
  - Vertex AI is Google Cloud's fully-managed, unified development platform for building, training, deploying, and managing machine learning (ML) models at scale. It provides tools for the entire ML lifecycle, from data preparation and custom training with AutoML to model monitoring and deployment.
- **Google ADK**
  - The Google Agent Development Kit (ADK) is a framework designed to help developers build, test, and deploy AI agents. It provides tools and libraries that streamline the agent development process, offering features like agent orchestration, tool integration, and evaluation metrics.

---

## 3. Advanced

### 3.1 AI Safety and Ethics
- **Prompt Injection Attacks**
  - Prompt injection attacks are a type of security vulnerability where malicious inputs are crafted to manipulate or exploit AI models, like language models, to produce unintended or harmful outputs. These attacks involve injecting deceptive or adversarial content into the prompt to bypass filters, extract confidential information, or make the model respond in ways it shouldn't.
- **Bias and Fairness**
  - Bias and fairness in AI refer to the challenges of ensuring that machine learning models do not produce discriminatory or skewed outcomes. Bias can arise from imbalanced training data, flawed assumptions, or biased algorithms, leading to unfair treatment of certain groups based on race, gender, or other factors.
- **Security and Privacy Concerns**
  - Security and privacy concerns in AI revolve around the protection of data and the responsible use of models. Key issues include ensuring that sensitive data, such as personal information, is handled securely during collection, processing, and storage, to prevent unauthorized access and breaches.
- **Content Moderation APIs**
  - Content Moderation APIs are tools that automatically analyze text, images, video, and audio to detect potentially harmful or inappropriate content. These APIs use machine learning models to identify violations of predefined policies related to areas like hate speech, violence, self-harm, and sexually suggestive material.
- **Adding end-user IDs in prompts**
  - Sending end-user IDs in your requests can be a useful tool to help OpenAI monitor and detect abuse. This allows OpenAI to provide your team with more actionable feedback in the event that we detect any policy violations in your application.
- **Data Layer**
  - The Data Layer within the Model Context Protocol (MCP) is responsible for managing and providing access to the data that AI agents use to reason, learn, and make decisions. It acts as an intermediary between the agent and various data sources, ensuring data is readily available, properly formatted, and securely accessed.
- **Transport Layer**
  - The Transport Layer in the Model Context Protocol (MCP) is responsible for reliably and efficiently moving data between different components of an AI agent system. It defines how messages are packaged, addressed, and transmitted across a network or within a single machine, ensuring that information reaches its intended destination without errors or loss.
- **Building an MCP Server**
  - An MCP (Model Context Protocol) server acts as an intermediary between AI agents and various data sources or tools. It provides a standardized way for agents to access and interact with external information, enabling them to perform tasks that require context beyond their internal knowledge.
- **Building an MCP Client**
  - Building an MCP (Model Context Protocol) client involves creating software that can interact with AI models using a standardized protocol. This client acts as an intermediary, formatting requests for the model, sending them, and then processing the model's responses into a usable format for other applications or systems.
- **Connect to Local Server**
  - A Local Desktop deployment means running the MCP server directly on your own computer instead of a remote cloud or server. You install the MCP software, needed runtimes, and model files onto your desktop or laptop.

### 3.2 LLM Observability
- **Conducting adversarial testing**
  - Adversarial testing involves intentionally exposing machine learning models to deceptive, perturbed, or carefully crafted inputs to evaluate their robustness and identify vulnerabilities. The goal is to simulate potential attacks or edge cases where the model might fail, such as subtle manipulations in images, text, or data that cause the model to misclassify or produce incorrect outputs.
- **Robust prompt engineering**
  - Robust prompt engineering involves carefully crafting inputs to guide AI models toward producing accurate, relevant, and reliable outputs. It focuses on minimizing ambiguity and maximizing clarity by providing specific instructions, examples, or structured formats.
- **Know your Customers / Usecases**
  - To know your customer means deeply understanding the needs, behaviors, and expectations of your target users. This ensures the tools you create are tailored precisely for their intended purpose, while also being designed to prevent misuse or unintended applications.
- **Constraining outputs and inputs**
  - Constraining outputs and inputs in AI models refers to implementing limits or rules that guide both the data the model processes (inputs) and the results it generates (outputs). Input constraints ensure that only valid, clean, and well-formed data enters the model, which helps to reduce errors and improve performance.
- **Connect to Remote Server**
  - Remote or cloud deployment places the MCP server on a cloud provider instead of a local machine. You package the server as a container or virtual machine, choose a service like AWS, Azure, or GCP, and give it compute, storage, and a public HTTPS address.
- **Tracing & logging**
  - Tracing records the full lifecycle of a request through your AI system, from the initial user input through any intermediate LLM calls, tool uses, or retrieval steps, all the way to the final response. Logging captures individual events like errors, latency spikes, or unexpected outputs.
- **Cost/latency monitoring**
  - Cost and latency monitoring tracks token usage, the resulting financial cost, and response times across your AI system. Without this visibility, production costs can compound quickly and silently, especially when using large reasoning models that charge significantly per token.
- **Production monitoring**
  - Production monitoring is the continuous observation of your AI system once it is live and handling real user traffic. Unlike testing in a controlled environment, production surfaces edge cases, unexpected inputs, and failure modes that never appeared during development.

### 3.3 LLM Evaluations
- **LangSmith**
  - LangSmith is an observability and evaluation platform built by the LangChain team, designed specifically for LLM applications. It automatically captures traces of LangChain runs and also works with non-LangChain code.
- **Langfuse**
  - LangFuse is an open-source LLM observability platform that provides tracing, prompt management, and evaluation tooling. You can self-host it or use the cloud version.
- **Helicone**
  - Helicone is a logging and observability proxy for LLM APIs. Instead of calling OpenAI or Anthropic directly, you route requests through Helicone, which captures every request and response with zero code changes.
- **Arize AI**
  - Arize is an ML observability platform that supports both traditional ML models and LLM applications. For LLMs, it provides tracing, drift detection, and evaluation tooling.
- **Deterministic Evals**
  - Deterministic evals use fixed, rule-based checks to score model outputs. Examples include checking whether a response contains a required keyword, matches an expected format, or equals a known correct answer exactly.

### 3.4 Regression Testing
- **Multimodal AI Usecases**
  - Multimodal AI powers applications like visual question answering, content moderation, and enhanced search engines. It drives smarter virtual assistants and interactive AR apps, combining text, images, and audio for richer, more intuitive user experiences across e-commerce, accessibility, and entertainment.
- **Image Understanding**
  - Multimodal AI enhances image understanding by integrating visual data with other types of information, such as text or audio. By combining these inputs, AI models can interpret images more comprehensively, recognizing objects, scenes, and actions, while also understanding context and related concepts.
- **Image Generation**
  - Image generation is a process in artificial intelligence where models create new images based on input prompts or existing data. It involves using generative models like GANs (Generative Adversarial Networks), VAEs (Variational Autoencoders), or more recently, transformer-based models like DALL-E and Stable Diffusion.
- **Model-Based Evals**
  - Model-based evals use a separate AI model to automatically score or assess the outputs of your LLM application. Instead of writing manual rules or relying on human reviewers, you delegate the judgment to another model, a technique commonly known as LLM-as-a-Judge.
- **Human Evals**
  - Human evals involve people directly reviewing and scoring model outputs against defined criteria. They are the most accurate form of evaluation for nuanced or subjective quality dimensions, and serve as the ground truth that other eval methods are validated against.
- **Evaluation Metrics**
  - Evaluation metrics are the specific measurements used to score LLM outputs against defined quality criteria. Each metric targets a different dimension of quality, such as whether the response is factually grounded, relevant to the question, free of harmful content, or genuinely useful to the user.

### 3.5 Multimodal AI
- **Video Understanding**
  - Video understanding with multimodal AI involves analyzing and interpreting both visual and audio content to provide a more comprehensive understanding of videos. Common use cases include video summarization, where AI extracts key scenes and generates summaries; content moderation, where the system detects inappropriate visuals or audio; and video indexing for easier search and retrieval of specific moments within a video.
- **Audio Processing**
  - Audio processing in multimodal AI enables a wide range of use cases by combining sound with other data types, such as text, images, or video, to create more context-aware systems. Use cases include speech recognition paired with real-time transcription and visual analysis in meetings or video conferencing tools, voice-controlled virtual assistants that can interpret commands in conjunction with on-screen visuals, and multimedia content analysis where audio and visual elements are analyzed together for tasks like content moderation or video indexing.
- **Text-to-Speech**
  - In the context of multimodal AI, text-to-speech (TTS) technology converts written text into natural-sounding spoken language, allowing AI systems to communicate verbally. When integrated with other modalities, such as visual or interactive elements, TTS can enhance user experiences in applications like virtual assistants, educational tools, and accessibility features.
- **Speech-to-Text**
  - In the context of multimodal AI, speech-to-text technology converts spoken language into written text, enabling seamless integration with other data types like images and text. This allows AI systems to process audio input and combine it with visual or textual information, enhancing applications such as virtual assistants, interactive chatbots, and multimedia content analysis.
- **Claude Code**
  - Claude Code refers to the code-generation capabilities of Anthropic's Claude AI model. It's designed to assist developers by understanding natural language prompts and translating them into functional code across various programming languages.
- **Gemini**
  - Gemini is a multimodal AI model developed by Google. It's designed to understand and reason across different types of information, including text, code, audio, images, and video.
- **DeepEval**
  - DeepEval is an open-source LLM evaluation framework that lets you write automated tests for your AI application in a way that feels similar to unit testing with pytest. It comes with over 50 built-in metrics covering accuracy, faithfulness, relevance, toxicity, and agent behavior, and it works across RAG pipelines, chatbots, and multi-step agents.
- **RAGAS**
  - RAGAS is an open-source framework specifically designed for evaluating retrieval-augmented generation pipelines. It provides a suite of reference-free metrics, meaning it does not require hand-labeled ground truth answers, which makes it practical to run on real production data.

### 3.6 Development Tools
- **OpenAI Vision API**
  - The OpenAI Vision API enables models to analyze and understand images, allowing them to identify objects, recognize text, and interpret visual content. It integrates image processing with natural language capabilities, enabling tasks like visual question answering, image captioning, and extracting information from photos.
- **DALL-E API**
  - The DALL-E API is a tool provided by OpenAI that allows developers to integrate the DALL-E image generation model into applications. DALL-E is an AI model designed to generate images from textual descriptions, capable of producing highly detailed and creative visuals.
- **Whisper API**
  - The Whisper API by OpenAI enables developers to integrate speech-to-text capabilities into their applications. It uses OpenAI's Whisper model, a powerful speech recognition system, to convert spoken language into accurate, readable text.
- **Hugging Face Models**
  - Hugging Face models are a collection of pre-trained machine learning models available through the Hugging Face platform, covering a wide range of tasks like natural language processing, computer vision, and audio processing. The platform includes models for tasks such as text classification, translation, summarization, question answering, and more, with popular models like BERT, GPT, T5, and CLIP.
- **LangChain for Multimodal Apps**
  - LangChain is a framework designed to build applications that integrate multiple AI models, especially those focusing on language understanding, generation, and multimodal capabilities. For multimodal apps, LangChain facilitates seamless interaction between text, image, and even audio models, enabling developers to create complex workflows that can process and analyze different types of data.
- **LlamaIndex for Multimodal Apps**
  - LlamaIndex enables multi-modal apps by linking language models (LLMs) to diverse data sources, including text and images. It indexes and retrieves information across formats, allowing LLMs to process and integrate data from multiple modalities.
- **Codex**
  - Codex is an AI model created by OpenAI that translates natural language into code. It's designed to understand and generate code in a variety of programming languages, including Python, JavaScript, and more.
- **OpenCode**
  - Devin is an autonomous AI software engineer capable of handling entire development projects from start to finish. It functions by planning, writing, debugging, and deploying code through a simulated environment that mirrors a human developer’s workflow.
- **Cursor**
  - Cursor is an AI-powered code editor designed to enhance developer productivity. It leverages large language models to provide features such as code generation, intelligent autocompletion, and code refactoring suggestions, all within a familiar editor environment.
- **Replit**
  - Replit is an online integrated development environment (IDE) that allows users to write and run code in various programming languages directly in their web browser. It provides a collaborative coding environment with features like real-time collaboration, version control, and package management, making it easy to build and deploy projects without needing to install software locally.
- **NanoBanana API**
  - The NanoBanana API is a tool designed to facilitate the integration and processing of data from multiple modalities, such as text, images, and audio. It provides a unified interface for managing diverse data types, enabling developers to build AI systems that can understand and reason about information from various sources simultaneously.

---

## 4. Optional / Specialized Topics

- Impact on Product Development
- Roles and Responsiblities
- Prompt Engineering
- AI Agents
- Tokens
- Context
- Top-K
- Top-P
- Fine-tuning
- Inference Engineering
- Repetition Penalties
- Embeddings
- Sampling Parameters
- Temperature
- Context Window
- Constraints
- Context vs Prompt Eng.
- Context Sources
- MCP
- Context Security
- What is a Context Layer?
- Context Engineering
- Structured Output
- Function Calling
- Prompt Caching

---

## 5. References

- [AI Engineer Roadmap](https://roadmap.sh/ai-engineer)

---

## 6. Related Roles / Topics

### Related Roles
- AI and Data Scientist
- Data Analyst
- Frontend Developer

### Related Skills
- Prompt Engineering
- Python