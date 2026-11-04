# Prompt Engineering

## Metadata
- Type: Skill
- Domain: Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/prompt-engineering
- Related Roles:
  - AI Engineer
  - AI and Data Scientist
  - Data Analyst
  - MLOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **LLMs and how they work?**
  - LLMs function as sophisticated prediction engines that process text sequentially, predicting the next token based on relationships between previous tokens and patterns from training data. They don't predict single tokens directly but generate probability distributions over possible next tokens, which are then sampled using parameters like temperature and top-K.
- **What is a Prompt?**
  - A prompt is an input provided to a Large Language Model (LLM) to generate a response or prediction. It serves as the instruction or context that guides the AI model's output generation process.
- **What is Prompt Engineering?**
  - Prompt engineering is the practice of designing effective inputs for large language models to achieve desired outputs. It covers techniques like few-shot prompting, chain-of-thought, and parameter tuning.
- **LLM**
  - Large Language Models (LLMs) are AI systems trained on vast text data to understand and generate human-like language. They work as prediction engines, analyzing input and predicting the next most likely token.
- **Tokens**
  - Tokens are fundamental units of text that LLMs process, created by breaking down text into smaller components like words, subwords, or characters. Understanding tokens is crucial because models predict the next token in sequences, API costs are based on token count, and models have maximum token limits for input and output.

### 1.2 Sampling Parameters
- **Context Window**
  - Context window refers to the maximum number of tokens an LLM can process in a single interaction, including both input prompt and generated output. When exceeded, older parts are truncated.
- **Hallucination**
  - Hallucination in LLMs refers to generating plausible-sounding but factually incorrect or fabricated information. This occurs when models fill knowledge gaps or present uncertain information with apparent certainty.
- **Model Weights / Parameters**
  - Model weights and parameters are the learned values that define an LLM's behavior and knowledge. Parameters are the trainable variables adjusted during training, while weights represent their final values.
- **Fine-Tuning vs Prompt Engg.**
  - Fine-tuning trains models on specific data to specialize behavior, while prompt engineering achieves customization through input design without model modification. Prompt engineering is faster, cheaper, and more accessible.
- **RAG**
  - Retrieval-Augmented Generation (RAG) combines LLMs with external knowledge retrieval to ground responses in verified, current information. RAG retrieves relevant documents before generating responses, reducing hallucinations and enabling access to information beyond the model's training cutoff.
- **Agents**
  - AI agents are autonomous systems that use LLMs to reason, plan, and take actions to achieve specific goals. They combine language understanding with tool usage, memory, and decision-making to perform complex, multi-step tasks.
- **Prompt Injection**
  - Prompt injection is a security vulnerability where malicious users manipulate LLM inputs to override intended behavior, bypass safety measures, or extract sensitive information. Attackers embed instructions within data to make models ignore original prompts and follow malicious commands.
- **AI vs AGI**
  - AI (Artificial Intelligence) refers to systems that perform specific tasks intelligently, while AGI (Artificial General Intelligence) represents hypothetical AI with human-level reasoning across all domains. Current LLMs are narrow AI - powerful at language tasks but lacking true understanding or general intelligence like AGI would possess.
- **Temperature**
  - Temperature controls the randomness in token selection during text generation. Lower values (0-0.3) produce deterministic, factual outputs.
- **Top-K**
  - Top-K restricts token selection to the K most likely tokens from the probability distribution. Low values (1-10) produce conservative, factual outputs.
- **Top-P**
  - Top-P (nucleus sampling) selects tokens from the smallest set whose cumulative probability exceeds threshold P. Unlike Top-K's fixed number, Top-P dynamically adjusts based on probability distribution.

---

## 2. Intermediate

### 2.1 Output Control
- **OpenAI**
  - OpenAI develops leading language models including GPT-5.4, o3, and Codex, setting industry standards for prompt engineering. Their API provides access to frontier models with configurable parameters, and their Agents SDK enables building autonomous AI systems.
- **Google**
  - Google develops Gemini, a family of multimodal AI models. The latest flagship, Gemini 3, supports text, image, video, and audio through the Gemini API and Google AI Studio.
- **Anthropic**
  - Anthropic develops Claude, a family of large language models focused on safety and helpfulness. The current lineup includes Claude Opus 4.7 (most capable, for complex reasoning and agentic coding), Claude Sonnet 4.6 (best speed-intelligence balance), and Claude Haiku 4.5 (fastest, near-frontier intelligence).
- **Meta**
  - Meta develops the Llama family of open-source large language models. The latest release, Llama 4, comes in Maverick and Scout variants with strong multimodal and long-context capabilities.
- **xAI**
  - xAI develops Grok, a conversational AI model with real-time web access and integration with X (Twitter). The latest model, Grok 4.20, features a 2M token context window, agentic tool calling, and industry-leading low hallucination rates.
- **Max Tokens**
  - Max tokens setting controls the maximum number of tokens an LLM can generate in response, directly impacting computation cost, response time, and energy consumption. Setting lower limits doesn't make models more concise—it simply stops generation when the limit is reached.

### 2.2 Repetition Penalties
- **Stop Sequences**
  - Stop sequences are specific strings that signal the LLM to stop generating text when encountered, providing precise control over output length and format. Common examples include newlines, periods, or custom markers like "###" or "END".
- **Frequency Penalty**
  - Frequency penalty reduces token probability based on how frequently they have appeared in the text, with higher penalties for more frequent tokens. This prevents excessive repetition and encourages varied language use.
- **Presence Penalty**
  - Presence penalty reduces the likelihood of repeating tokens that have already appeared in the text, encouraging diverse vocabulary usage. Unlike frequency penalty which considers how often tokens appear, presence penalty applies the same penalty to any previously used token, promoting varied content and creativity.

### 2.3 Structured Outputs
- **Zero-Shot Prompting**
  - Zero-shot prompting provides only a task description without examples, relying on the model's training patterns. Simply describe the task clearly, provide input data, and optionally specify output format.
- **One-Shot / Few-Shot Prompting**
  - One-shot provides a single example to guide model behavior, while few-shot includes multiple examples (3-5) to demonstrate desired patterns. Examples show output structure, style, and tone, increasing accuracy and consistency.
- **System Prompting**
  - System prompting sets the overall context, purpose, and operational guidelines for LLMs. It defines the model's role, behavioral constraints, output format requirements, and safety guardrails.
- **Role Prompting**
  - Role prompting assigns a specific character, identity, or professional role to the LLM to generate responses consistent with that role's expertise, personality, and communication style. By establishing roles like "teacher," "travel guide," or "software engineer," you provide the model with appropriate domain knowledge, perspective, and tone for more targeted, natural interactions.
- **Contextual Prompting**
  - Contextual prompting provides specific background information or situational details relevant to the current task, helping LLMs understand nuances and tailor responses accordingly. Unlike system or role prompts, contextual prompts supply immediate, task-specific information that's dynamic and changes based on the situation.
- **Step-back Prompting**
  - Step-back prompting improves LLM performance by first asking a general question related to the specific task, then using that answer to inform the final response. This technique activates relevant background knowledge before attempting the specific problem.
- **Chain of Thought (CoT) Prompting**
  - Chain of Thought prompting improves LLM reasoning by generating intermediate reasoning steps before providing the final answer. Instead of jumping to conclusions, the model "thinks through" problems step by step.
- **Self-Consistency Prompting**
  - Self-consistency prompting generates multiple reasoning paths for the same problem using higher temperature settings, then selects the most commonly occurring answer through majority voting. This technique combines sampling and voting to improve accuracy and provides pseudo-probability of answer correctness.

---

## 3. Advanced

### 3.1 Automatic Prompt Engineering
- **Tree of Thoughts (ToT) Prompting**
  - Tree of Thoughts (ToT) generalizes Chain of Thought by allowing LLMs to explore multiple reasoning paths simultaneously rather than following a single linear chain. This approach maintains a tree structure where each thought represents a coherent step toward solving a problem, enabling the model to branch out and explore different reasoning directions.
- **ReAct Prompting**
  - ReAct (Reason and Act) prompting enables LLMs to solve complex tasks by combining reasoning with external tool interactions. It follows a thought-action-observation loop: analyze the problem, perform actions using external APIs, review results, and iterate until solved.

### 3.2 AI Red Teaming
- **Prompt Debiasing**
  - Prompt debiasing involves techniques to reduce unwanted biases in LLM outputs by carefully crafting prompts. This includes using neutral language, diverse examples, and explicit instructions to avoid stereotypes or unfair representations.
- **Prompt Ensembling**
  - Prompt ensembling combines multiple different prompts or prompt variations to improve output quality and consistency. This technique involves running the same query with different prompt formulations and aggregating results through voting, averaging, or selection.
- **LLM Self Evaluation**
  - LLM self-evaluation involves prompting models to assess their own outputs for quality, accuracy, or adherence to criteria. This technique can identify errors, rate confidence levels, or check if responses meet specific requirements.
- **Calibrating LLMs**
  - Calibrating LLMs involves adjusting models so their confidence scores accurately reflect their actual accuracy. Well-calibrated models express appropriate uncertainty - being confident when correct and uncertain when likely wrong.
- **Prompt Tuning**
  - Prompt tuning is a method for adapting large AI models to new tasks without changing the model itself. Instead of retraining billions of parameters, it learns a small set of special vectors called “soft prompts” that are added to the input.

---

## 4. Optional / Specialized Topics

- Tokens
- RAG
- Agents
- Prompt Injection
- AI vs AGI
- Temperature
- Top-K
- Top-P
- xAI
- Max Tokens
- Contextual Prompting
- Step-back Prompting
- Chain of Thought (CoT) Prompting
- Self-Consistency Prompting
- Prompt Tuning

---

## 5. References

- [Prompt Engineering Roadmap](https://roadmap.sh/prompt-engineering)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer
- AI and Data Scientist
- Data Analyst
- MLOps Engineer

### Related Skills
- AI Agents
- Claude Code
- Vibe Coding