# AI Red Teamer

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/ai-red-teaming
- Related Roles:
  - AI Engineer
  - AI and Data Scientist
  - Data Analyst
  - Cyber Security Specialist

---

## 1. Beginner

### 1.1 Introduction
- **AI Security Fundamentals**
  - This covers the foundational concepts essential for AI Red Teaming, bridging traditional cybersecurity with AI-specific threats. An AI Red Teamer must understand common vulnerabilities in ML models (like evasion or poisoning), security risks in the AI lifecycle (from data collection to deployment), and how AI capabilities can be misused.
- **Why Red Team AI Systems?**
  - AI systems introduce novel risks beyond traditional software, such as emergent unintended capabilities, complex failure modes, susceptibility to subtle data manipulations, and potential for large-scale misuse (e.g., generating disinformation). AI Red Teaming is necessary because standard testing methods often fail to uncover these unique AI vulnerabilities.
- **Ethical Considerations**
  - Ethical conduct is crucial for AI Red Teamers. While simulating attacks, they must operate within strict legal and ethical boundaries defined by rules of engagement, focusing on improving safety without causing real harm or enabling misuse.
- **Role of Red Teams**
  - The role of an AI Red Team is to rigorously challenge AI systems from an adversarial perspective. They design and execute tests to uncover vulnerabilities related to the model's logic, data dependencies, prompt interfaces, safety alignments, and interactions with surrounding infrastructure.
- **Supervised Learning**
  - AI Red Teamers analyze systems built using supervised learning to probe for vulnerabilities like susceptibility to adversarial examples designed to cause misclassification, sensitivity to data distribution shifts, or potential for data leakage related to the labeled training data. Understanding how these models learn input-output mappings is key to devising tests that challenge their learned boundaries.
- **Unsupervised Learning**
  - When red teaming AI systems using unsupervised learning (e.g., clustering algorithms), focus areas include assessing whether the discovered patterns reveal sensitive information, if the model can be manipulated to group data incorrectly, or if dimensionality reduction techniques obscure security-relevant features. Understanding these models helps identify risks associated with pattern discovery on unlabeled data.
- **Reinforcement Learning**
  - Red teaming RL-based AI systems involves testing for vulnerabilities such as reward hacking (exploiting the reward function to induce unintended behavior), unsafe exploration (agent takes harmful actions during learning), or susceptibility to adversarial perturbations in the environment's state. Understanding the agent's policy and value functions is crucial for designing effective tests against RL agents.
- **Confidentiality, Integrity, Availability**
  - The CIA Triad is directly applicable in AI Red Teaming. Confidentiality tests focus on preventing leakage of training data or proprietary model details.

---

## 2. Intermediate

### 2.1 Prompt Hacking
- **Neural Networks**
  - Understanding neural network architectures (layers, nodes, activation functions) is vital for AI Red Teamers. This knowledge allows for targeted testing, such as crafting adversarial examples that exploit specific activation functions or identifying potential vulnerabilities related to network depth or connectivity.
- **Generative Models**
  - AI Red Teamers focus heavily on generative models (like GANs and LLMs) due to their widespread use and unique risks. Understanding how they generate content is key to testing for issues like generating harmful/biased outputs, deepfakes, prompt injection vulnerabilities, or leaking sensitive information from their vast training data.
- **Large Language Models**
  - LLMs are a primary target for AI Red Teaming. Understanding their architecture (often Transformer-based), training processes (pre-training, fine-tuning), and capabilities (text generation, summarization, Q&A) is essential for identifying vulnerabilities like prompt injection, jailbreaking, data regurgitation, and emergent harmful behaviors specific to these large-scale models.
- **Prompt Engineering**
  - For AI Red Teamers, prompt engineering is both a tool and a target. It's a tool for crafting inputs to test model boundaries and vulnerabilities (e.g., creating jailbreak prompts).
- **Threat Modeling**
  - AI Red Teams apply threat modeling to identify unique attack surfaces in AI systems, such as manipulating training data, exploiting prompt interfaces, attacking the model inference process, or compromising connected tools/APIs. Before attacking an AI system, red teamers perform threat modeling to map out possible adversaries (from curious users to state actors) and attack vectors, prioritizing tests based on likely impact and adversary capability.
- **Risk Management**
  - AI Red Teamers contribute to the AI risk management process by identifying and demonstrating concrete vulnerabilities. Findings from red team exercises inform risk assessments, helping organizations understand the likelihood and potential impact of specific AI threats and prioritize resources for mitigation based on demonstrated exploitability.
- **Vulnerability Assessment**
  - While general vulnerability assessment scans infrastructure, AI Red Teaming extends this to assess vulnerabilities specific to the AI model and its unique interactions. This includes probing for prompt injection flaws, testing for adversarial example robustness, checking for data privacy leaks, and evaluating safety alignment failures – weaknesses not typically found by standard IT vulnerability scanners.
- **Jailbreak Techniques**
  - Jailbreaking is a specific category of prompt hacking where the AI Red Teamer aims to bypass the LLM's safety and alignment training. They use techniques like creating fictional scenarios, asking the model to simulate an unrestricted AI, or using complex instructions to trick the model into generating content that violates its own policies (e.g., generating harmful code, hate speech, or illegal instructions).
- **Safety Filter Bypasses**
  - AI Red Teamers specifically target the safety mechanisms (filters, guardrails) implemented within or around an AI model. They test techniques like using synonyms for blocked words, employing different languages, embedding harmful requests within harmless text, or using character-level obfuscation to evade detection and induce the model to generate prohibited content, thereby assessing the robustness of the safety controls.

### 2.2 Model Vulnerabilities
- **Prompt Injection**
  - Prompt injection is a critical vulnerability tested by AI Red Teamers. They attempt to insert instructions into the LLM's input that override its intended system prompt or task, causing it to perform unauthorized actions, leak data, or generate malicious output.
- **Direct**
  - Direct injection attacks occur when malicious instructions are inserted directly into the prompt input field by the user interacting with the LLM. AI Red Teamers use this technique to assess if basic instructions like "Ignore previous prompt" can immediately compromise the model's safety or intended function, testing the robustness of the system prompt's influence.
- **Indirect**
  - Indirect injection involves embedding malicious prompts within external data sources that the LLM processes, such as websites, documents, or emails. AI Red Teamers test this by poisoning data sources the AI might interact with (e.g., adding hidden instructions to a webpage summarized by the AI) to see if the AI executes unintended commands or leaks data when processing that source.
- **Model Weight Stealing**
  - AI Red Teamers assess the risk of attackers reconstructing or stealing the proprietary weights of a trained model, often through API query-based attacks. Testing involves simulating such attacks to understand how easily the model's functionality can be replicated, which informs defenses like query rate limiting, watermarking, or differential privacy.
- **Unauthorized Access**
  - AI Red Teamers test if vulnerabilities in the AI system or its interfaces allow attackers to gain unauthorized access to data, functionalities, or underlying infrastructure. This includes attempting privilege escalation via prompts, exploiting insecure API endpoints connected to the AI, or manipulating the AI to access restricted system resources.

### 2.3 Code Injection
- **Countermeasures**
  - AI Red Teamers must also understand and test defenses against prompt hacking. This includes evaluating the effectiveness of input sanitization, output filtering, instruction demarcation (e.g., XML tagging), contextual awareness checks, model fine-tuning for resistance, and applying the principle of least privilege to LLM capabilities and tool access.
- **Data Poisoning**
  - AI Red Teamers simulate data poisoning attacks by evaluating how introducing manipulated or mislabeled data into potential training or fine-tuning datasets could compromise the model. They assess the impact on model accuracy, fairness, or the potential creation of exploitable backdoors, informing defenses around data validation and provenance.
- **Adversarial Examples**
  - A core AI Red Teaming activity involves generating adversarial examples – inputs slightly perturbed to cause misclassification or bypass safety filters – to test model robustness. Red teamers use various techniques (gradient-based, optimization-based, or black-box methods) to find inputs that exploit model weaknesses, informing developers on how to harden the model.
- **Model Inversion**
  - AI Red Teamers perform model inversion tests to assess if an attacker can reconstruct sensitive training data (like images, text snippets, or personal attributes) by repeatedly querying the model and analyzing its outputs. Success indicates privacy risks due to data memorization, requiring mitigation techniques like differential privacy or output filtering.
- **Insecure Deserialization**
  - AI Red Teamers investigate if serialized objects used by the AI system (e.g., for saving model states, configurations, or transmitting data) can be manipulated by an attacker. They test if crafting malicious serialized objects could lead to remote code execution or other exploits when the application deserializes the untrusted data.

---

## 3. Advanced

### 3.1 Infrastructure Security
- **Adversarial Training**
  - AI Red Teamers evaluate the effectiveness of adversarial training as a defense. They test if models trained on adversarial examples are truly robust or if new, unseen adversarial attacks can still bypass the hardened defenses.
- **Robust Model Design**
  - AI Red Teamers assess whether choices made during model design (architecture selection, regularization techniques, ensemble methods) effectively contribute to robustness against anticipated attacks. They test if these design choices actually prevent common failure modes identified during threat modeling.
- **Continuous Monitoring**
  - AI Red Teamers assess the effectiveness of continuous monitoring systems by attempting attacks and observing if detection mechanisms trigger appropriate alerts and responses. They test if monitoring covers AI-specific anomalies (like sudden shifts in output toxicity or unexpected resource consumption by the model) in addition to standard infrastructure monitoring.
- **Remote Code Execution**
  - AI Red Teamers attempt to achieve RCE on systems hosting or interacting with AI models. This could involve exploiting vulnerabilities in the AI framework itself, the web server, connected APIs, or tricking an AI agent with code execution capabilities into running malicious commands provided via prompts.
- **API Protection**
  - AI Red Teamers rigorously test the security of APIs providing access to AI models. They probe for OWASP API Top 10 vulnerabilities like broken authentication/authorization, injection flaws, security misconfigurations, and lack of rate limiting, specifically evaluating how these could lead to misuse or compromise of the AI model itself.
- **Authentication**
  - AI Red Teamers test the authentication mechanisms controlling access to AI systems and APIs. They attempt to bypass logins, steal or replay API keys/tokens, exploit weak password policies, or find flaws in MFA implementations to gain unauthorized access to the AI model or its management interfaces.
- **Authorization**
  - AI Red Teamers test authorization controls to ensure that authenticated users can only access the AI features and data permitted by their roles/permissions. They attempt privilege escalation, try to access other users' data via the AI, or manipulate the AI to perform actions beyond its authorized scope.
- **Black Box Testing**
  - In AI Red Teaming, black-box testing involves probing the AI system with inputs and observing outputs without any knowledge of the model's architecture, training data, or internal logic. This simulates an external attacker and is crucial for finding vulnerabilities exploitable through publicly accessible interfaces, such as prompt injection or safety bypasses discoverable via API interaction.
- **White Box Testing**
  - White-box testing in AI Red Teaming grants the tester full access to the model's internals (architecture, weights, training data, source code). This allows for highly targeted attacks, such as crafting precise adversarial examples using gradients, analyzing code for vulnerabilities, or directly examining training data for biases or PII leakage.
- **Grey Box Testing**
  - Grey-box AI Red Teaming involves testing with partial knowledge of the system, such as knowing the model type (e.g., GPT-4), having access to some documentation, or understanding the general system architecture but not having full model weights or source code. This allows for more targeted testing than black-box while still simulating realistic external attacker scenarios where some information might be gleaned.
- **Automated vs Manual**
  - AI Red Teaming typically employs a blend of automated tools (for large-scale scanning, fuzzing prompts, generating basic adversarial examples) and manual human testing (for creative jailbreaking, complex multi-stage attacks, evaluating nuanced safety issues like bias). Automation provides scale, while manual testing provides depth and creativity needed to find novel vulnerabilities.
- **Continuous Testing**
  - Applying continuous testing principles to AI security involves integrating automated red teaming checks into the development pipeline (CI/CD). This allows for regular, automated assessment of model safety, robustness, and alignment as the model or application code evolves, catching regressions or new vulnerabilities early.
- **Testing Platforms**
  - Platforms used by AI Red Teamers range from general penetration testing OS distributions like Kali Linux to specific AI red teaming tools/frameworks like Microsoft's PyRIT or Promptfoo, and vulnerability scanners like OWASP ZAP adapted for API testing of AI services. These platforms provide the toolsets needed to conduct assessments.
- **Monitoring Solutions**
  - AI Red Teamers interact with monitoring tools primarily to test their effectiveness (evasion) or potentially exploit vulnerabilities within them. Understanding tools like IDS (Snort, Suricata), network analyzers (Wireshark), and SIEMs helps red teamers simulate attacks that might bypass or target these defensive systems.
- **Benchmark Datasets**
  - AI Red Teamers may use or contribute to benchmark datasets specifically designed to evaluate AI security. These datasets (like HackAprompt, SecBench, NYU CTF Bench, CySecBench) contain prompts or scenarios targeting vulnerabilities, safety issues, or specific cybersecurity capabilities, allowing for standardized testing of models.
- **Custom Testing Scripts**
  - AI Red Teamers frequently write custom scripts (often in Python) to automate bespoke attacks, interact with specific AI APIs, generate complex prompt sequences, parse model outputs at scale, or implement novel exploit techniques not found in standard tools. Proficiency in scripting is essential for advanced AI red teaming.
- **Reporting Tools**
  - AI Red Teamers use reporting techniques and potentially tools to clearly document their findings, including discovered vulnerabilities, successful exploit steps (e.g., effective prompts), assessed impact, and actionable recommendations tailored to AI systems. Good reporting translates technical findings into understandable risks for stakeholders.
- **Specialized Courses**
  - Targeted training is crucial for mastering AI Red Teaming. Look for courses covering adversarial ML, prompt hacking, LLM security, ethical hacking for AI, and specific red teaming methodologies applied to AI systems offered by platforms like Learn Prompting, Coursera, or security training providers.
- **Industry Credentials**
  - Beyond formal certifications, recognition in the AI Red Teaming field comes from practical achievements like finding significant vulnerabilities (responsible disclosure), winning AI-focused CTFs or hackathons (like HackAPrompt), contributing to AI security research, or building open-source testing tools.
- **Lab Environments**
  - AI Red Teamers need environments to practice attacking vulnerable systems safely. While traditional labs (HTB, THM, VulnHub) build general pentesting skills, platforms are emerging with labs specifically focused on AI/LLM vulnerabilities, prompt injection, or adversarial ML challenges.
- **CTF Challenges**
  - Capture The Flag competitions increasingly include AI/ML security challenges. Participating in CTFs (tracked on CTFtime) or platforms like picoCTF helps AI Red Teamers hone skills in reverse engineering, web exploitation, and cryptography applied to AI systems, including specialized AI safety CTFs.
- **Red Team Simulations**
  - Participating in or conducting structured red team simulations against AI systems (or components) provides the most realistic practice. This involves applying methodologies, TTPs (Tactics, Techniques, and Procedures), reconnaissance, exploitation, and reporting within a defined scope and objective, specifically targeting AI vulnerabilities.
- **Conferences**
  - Attending major cybersecurity conferences (DEF CON, Black Hat, RSA) and increasingly specialized AI Safety/Security conferences allows AI Red Teamers to learn about cutting-edge research, network with peers, and discover new tools and attack/defense techniques.
- **Research Groups**
  - Following and potentially contributing to research groups at universities (like CMU, Stanford, Oxford), non-profits (like OpenAI, Anthropic), or government bodies (like UK's AISI) focused on AI safety, security, and alignment provides deep insights into emerging threats and mitigation strategies relevant to AI Red Teaming.
- **Forums**
  - Engaging in online forums, mailing lists, Discord servers, or subreddits dedicated to AI security, adversarial ML, prompt engineering, or general cybersecurity helps AI Red Teamers exchange knowledge, ask questions, learn about new tools/techniques, and find collaboration opportunities.
- **LLM Security Testing**
  - The core application area for many AI Red Teamers today involves specifically testing Large Language Models for vulnerabilities like prompt injection, jailbreaking, harmful content generation, bias, and data privacy issues using specialized prompts and evaluation frameworks.
- **Agentic AI Security**
  - As AI agents capable of autonomous action become more common, AI Red Teamers must test their unique security implications. This involves assessing risks related to goal hijacking, unintended actions through tool use, exploitation of planning mechanisms, and ensuring agents operate safely within their designated boundaries.
- **Responsible Disclosure**
  - A critical practice for AI Red Teamers is responsible disclosure: privately reporting discovered AI vulnerabilities (e.g., a successful jailbreak, data leak method, or severe bias) to the model developers or system owners, allowing them time to remediate before any public discussion, thus preventing malicious exploitation.
- **Emerging Threats**
  - AI Red Teamers must stay informed about potential future threats enabled by more advanced AI, such as highly autonomous attack agents, AI-generated malware that evades detection, sophisticated deepfakes for social engineering, or large-scale exploitation of interconnected AI systems. Anticipating these helps shape current testing priorities.
- **Advanced Techniques**
  - The practice of AI Red Teaming itself will evolve. Future techniques may involve using AI adversaries to automatically discover complex vulnerabilities, developing more sophisticated methods for testing AI alignment and safety properties, simulating multi-agent system failures, and creating novel metrics for evaluating AI robustness against unknown future attacks.
- **Research Opportunities**
  - AI Red Teaming relies on ongoing research. Key areas needing further investigation include scalable methods for finding elusive vulnerabilities, understanding emergent behaviors in complex models, developing provable safety guarantees, creating better benchmarks for AI security, and exploring the socio-technical aspects of AI misuse and defense.
- **Industry Standards**
  - As AI matures, AI Red Teamers will increasingly need to understand and test against emerging industry standards and regulations for AI safety, security, and risk management, such as the NIST AI RMF, ISO/IEC 42001, and sector-specific guidelines, ensuring AI systems meet compliance requirements.

---

## 4. Optional / Specialized Topics

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Confidentiality, Integrity, Availability
- Threat Modeling
- Risk Management
- Vulnerability Assessment
- Jailbreak Techniques
- Safety Filter Bypasses
- Unauthorized Access
- Insecure Deserialization
- API Protection
- Authentication
- Authorization
- Black Box Testing
- White Box Testing
- Grey Box Testing
- Automated vs Manual
- Continuous Testing
- Testing Platforms
- Monitoring Solutions
- Benchmark Datasets
- Custom Testing Scripts
- Reporting Tools
- Specialized Courses

---

## 5. References

- [AI Red Teamer Roadmap](https://roadmap.sh/ai-red-teaming)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer
- AI and Data Scientist
- Data Analyst
- Cyber Security Specialist

### Related Skills
- Prompt Engineering
- AI Agents