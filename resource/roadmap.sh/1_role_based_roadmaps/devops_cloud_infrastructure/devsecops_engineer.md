# DevSecOps Engineer

## Metadata
- Type: Role
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/devsecops
- Related Roles:
  - DevOps Engineer
  - Cyber Security Specialist
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **DevSecOps vs DevOps**
  - DevOps focuses on streamlining and automating the software development lifecycle, emphasizing collaboration between development and operations teams to deliver software faster and more efficiently. DevSecOps builds upon this foundation by integrating security practices and considerations throughout the entire DevOps pipeline, rather than treating security as a separate, end-of-cycle step.
- **Ruby**
  - Ruby is a dynamic, open-source programming language known for its simplicity and readability. Its flexible syntax and powerful features make it useful for automating tasks, building tools, and scripting, which are all valuable in a DevSecOps environment.

### 1.2 Learn a Programming Language
- **Python**
  - Python is a versatile programming language known for its readability and extensive libraries. It's used to automate tasks, build tools, and analyze data.
- **Rust**
  - Rust is a systems programming language focused on safety, speed, and concurrency. Its memory safety features, achieved through a borrow checker and ownership system, help prevent common vulnerabilities like buffer overflows and data races.
- **Go**
  - Go, often referred to as Golang, is a statically typed, compiled programming language designed at Google. Its simple syntax, efficient performance, and built-in concurrency features make it well-suited for building reliable and scalable tools and infrastructure components often used in DevSecOps pipelines.
- **JavaScript / Node.js**
  - JavaScript is a programming language primarily used for front-end web development, making websites interactive. Node.js, on the other hand, allows you to use JavaScript on the back-end, enabling server-side scripting and building scalable network applications.
- **Bash**
  - Bash is a command-line interpreter and scripting language commonly used in Linux and macOS environments. It allows users to automate tasks, manage files, and execute programs through a series of commands written in a script.
- **PowerShell**
  - PowerShell is a cross-platform task automation and configuration management framework, consisting of a command-line shell and associated scripting language. It allows users to automate administrative tasks on both local and remote Windows, Linux, and macOS systems.

### 1.3 Scripting Knowledge
- **Firewalls**
  - Firewalls are network security systems that monitor and control incoming and outgoing network traffic based on predetermined security rules. They act as a barrier between a trusted internal network and an untrusted external network, such as the internet.
- **ACLs**
  - Access Control Lists (ACLs) are sets of rules that determine whether network traffic is allowed or denied to pass through a network interface. They act as a security filter, examining packets based on source and destination IP addresses, ports, and protocols.
- **VLANs**
  - VLANs (Virtual Local Area Networks) are a way to logically segment a physical network into multiple broadcast domains. This allows you to group devices regardless of their physical location, improving network security, performance, and manageability by isolating traffic and reducing broadcast traffic within the network.
- **Vim / Nano / Emacs**
  - Vim, Nano, and Emacs are text editors used for creating, viewing, and modifying files, particularly configuration files and code. They provide different interfaces and functionalities, ranging from simple, beginner-friendly options to highly customizable and powerful environments for advanced users.

### 1.4 CIA Triad
- **CIA Triad**
  - The CIA Triad is a model designed to guide security policies for organizations. It consists of three fundamental principles: Confidentiality, ensuring that information is accessible only to authorized individuals; Integrity, maintaining the accuracy and completeness of data; and Availability, guaranteeing that authorized users have reliable access to information and resources when needed.

### 1.5 Authentication
- **Authentication**
  - Authentication is the process of verifying the identity of a user, device, or application attempting to access a system or resource. It confirms that the entity is who or what it claims to be, typically by requiring them to provide credentials such as a username and password, a digital certificate, or biometric data.

---

## 2. Intermediate

### 2.1 Authorization
- **Authorization**
  - Authorization is the process of determining what a user or system is allowed to access or do. It verifies if a user, once authenticated, has the necessary permissions to perform a specific action on a particular resource.

### 2.2 OWASP Top 10
- **OWASP Top 10**
  - The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.

### 2.3 Encryption
- **Symmetric**
  - Symmetric encryption uses the same secret key for both encrypting and decrypting data. This means that the sender and receiver must both possess the same key before secure communication can begin.
- **Asymmetric**
  - Asymmetric encryption, also known as public-key cryptography, uses a pair of keys: a public key for encryption and a private key for decryption. The public key can be freely distributed, allowing anyone to encrypt data intended for the owner of the private key.
- **Burp Suite**
  - Burp Suite is a platform used for performing security testing of web applications. It acts as a proxy, intercepting and analyzing traffic between a browser and a web server.

### 2.4 Networking Basics
- **DNS**
  - DNS, or Domain Name System, is essentially the phonebook of the internet. It translates human-readable domain names, like "example.com," into IP addresses, like "192.0.2.1," which computers use to identify each other on the network.
- **HTTP**
  - HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the World Wide Web. It's an application-layer protocol that defines how clients (like web browsers) and servers communicate by exchanging messages.
- **TLS**
  - TLS (Transport Layer Security) is a protocol that provides privacy and data integrity between two communicating applications. It's the successor to SSL (Secure Sockets Layer) and is used to encrypt the communication between a client (like a web browser) and a server, ensuring that data transmitted between them remains confidential and tamper-proof.
- **Network Segmentation**
  - Network segmentation divides a network into smaller, isolated segments or subnetworks. This is done to improve security, performance, and manageability.
- **Alert Types**
  - Alert types are the different categories or classifications of notifications generated by monitoring systems when specific events or conditions occur. These alerts signal potential issues, anomalies, or security threats within an application or infrastructure.
- **SIEM**
  - SIEM (Security Information and Event Management) is a system that collects and analyzes security logs and event data from various sources across an organization's IT infrastructure. It helps security teams detect, analyze, and respond to security threats and incidents by providing a centralized view of security-related information and automating threat detection and incident response processes.

### 2.5 Secure Coding
- **SQL Injection Prevention**
  - SQL Injection is a type of security vulnerability that occurs when malicious SQL code is inserted into an application's database query. This can happen when user input is not properly validated or sanitized before being used in a SQL query.
- **Input Validation Patterns**
  - Input validation patterns are techniques used to ensure that data entered into an application conforms to expected formats and values. These patterns involve checking the length, type, format, and range of user-supplied data before it's processed by the application.
- **XSS Prevention**
  - Cross-Site Scripting (XSS) is a type of security vulnerability that allows attackers to inject malicious scripts into websites viewed by other users. These scripts can then execute in the user's browser, potentially stealing sensitive information like cookies, redirecting the user to malicious sites, or defacing the website.

### 2.6 Identity Basics
- **IAM**
  - Identity and Access Management (IAM) is a framework of policies and technologies that ensures the right individuals and services have appropriate access to resources. It defines and manages user identities, authenticates them, and authorizes their access to specific resources based on predefined roles and permissions.
- **Role Based Access**
  - Role-Based Access Control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within an organization. It assigns permissions and privileges to roles, and then assigns users to those roles, simplifying access management and improving security by ensuring users only have the access necessary to perform their job functions.
- **Least Privilege**
  - Least privilege is the concept of granting users or processes only the minimum level of access necessary to perform their required tasks. This means limiting access rights to only what is strictly needed, avoiding broad or unnecessary permissions.
- **SOAR Concepts**
  - SOAR (Security Orchestration, Automation and Response) refers to a collection of technologies that enable organizations to automate and orchestrate security tasks and incident response processes. It integrates various security tools and data sources to streamline workflows, improve efficiency, and reduce the time it takes to detect, analyze, and respond to security threats.

### 2.7 Monitoring
- **Log Analysis**
  - Log analysis involves collecting, reviewing, and interpreting computer-generated records (logs) to identify patterns, anomalies, and potential security threats. These logs contain information about system events, user activities, and application behavior, providing valuable insights into the overall health and security posture of an environment.
- **Wireshark basics**
  - Wireshark is a free and open-source packet analyzer. It captures network traffic in real-time and allows you to examine the data transmitted across a network.
- **Nmap basics**
  - Nmap (Network Mapper) is a free and open-source utility used for network discovery and security auditing. It's used to discover hosts and services on a computer network by sending packets and analyzing the responses.
- **PASTA**
  - PASTA (Process for Attack Simulation and Threat Analysis) is a risk-centric threat modeling methodology. It focuses on aligning security with business objectives by understanding the potential impact of threats on the organization's goals.
- **STRIDE**
  - STRIDE is a threat modeling methodology used to identify potential security threats in a system or application. It provides a framework for categorizing threats based on six key characteristics: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.
- **Threat Modeling Workflows**
  - Threat modeling workflows are structured, repeatable processes used to identify, assess, and mitigate potential security threats in a system or application. These workflows typically involve defining the system's scope, decomposing it into components, identifying potential threats and vulnerabilities, prioritizing those threats based on risk, and then developing and implementing mitigation strategies.

---

## 3. Advanced

### 3.1 Threat Modeling
- **Automated Patching**
  - Automated patching is the process of automatically applying software updates and security fixes to systems and applications. This involves using tools and scripts to identify missing patches, download them from a central repository, and install them on target machines without manual intervention.
- **Attack Surface Mapping**
  - Attack surface mapping is the process of identifying and documenting all the potential entry points or vulnerabilities that an attacker could exploit to gain unauthorized access to a system or application. This involves cataloging all assets, including hardware, software, network components, and data, and then analyzing them to determine their susceptibility to various threats.

### 3.2 Cloud Security
- **CSPM**
  - Cloud Security Posture Management (CSPM) involves continuously assessing and improving the security configuration of cloud resources. It helps organizations identify and remediate misconfigurations, compliance violations, and security risks across their cloud environments.
- **Key Management Service**
  - A Key Management Service (KMS) is a secure system for creating, storing, and managing cryptographic keys. It provides a centralized platform to control access to these keys, ensuring that sensitive data is protected through encryption.
- **IAM**
  - IAM in cloud providers like AWS and GCP controls who can access what resources within your cloud environment. It lets you define users, groups, and roles, and then assign permissions to those roles.
- **Defense in Depth Concepts**
  - Defense in Depth is a security approach that uses multiple layers of security controls to protect assets. If one security measure fails, others are in place to provide continued protection.
- **Secure API Design**
  - Secure API design focuses on building application programming interfaces (APIs) that are resilient to attacks and protect sensitive data. This involves implementing security measures throughout the API lifecycle, from initial design and development to deployment and maintenance.
- **Zero Trust Concepts**
  - Zero Trust is a security framework based on the principle of "never trust, always verify." It assumes that no user or device, whether inside or outside the network perimeter, should be automatically trusted. Instead, every access request is fully authenticated, authorized, and encrypted before granting access to resources.

### 3.3 Container Security
- **Image Scanning**
  - Image scanning is the process of analyzing container images for known vulnerabilities, malware, and configuration issues. It involves examining the layers of the image, including the operating system, installed packages, and application code, against vulnerability databases and security policies.
- **Kubernetes**
  - Kubernetes is a system for managing containerized applications. Securing Kubernetes involves protecting the cluster itself, the containers running within it, and the data they access.
- **Docker**
  - Docker security entails protecting your applications and data within Docker containers. Because containers share the host operating system's kernel, vulnerabilities in the kernel or container configurations can be exploited.

### 3.4 Incident Response
- **IR Lifecycle**
  - The Incident Response (IR) Lifecycle is a structured approach to managing and resolving security incidents. It outlines the key phases involved, from initial preparation and detection to containment, eradication, recovery, and post-incident activity.
- **Forensics**
  - Forensics, in the context of incident response, involves the systematic investigation and analysis of security incidents to understand what happened, how it happened, and who was involved. It's about gathering and preserving digital evidence to reconstruct events, identify root causes, and support potential legal or disciplinary actions.
- **Containment**
  - Containment in incident response refers to the actions taken to limit the scope and impact of a security incident. It involves isolating affected systems or networks to prevent the incident from spreading further, minimizing damage, and preserving evidence for investigation.
- **Root Cause Analysis**
  - Root Cause Analysis (RCA) is a systematic process for identifying the fundamental reasons behind a problem or incident. It goes beyond addressing the immediate symptoms to uncover the underlying factors that led to the issue.
- **Nessus**
  - Nessus is a widely used vulnerability scanner that helps identify security weaknesses in computer systems, networks, and applications. It works by performing a variety of tests, including port scanning, service enumeration, and vulnerability identification, to detect potential security flaws.
- **Nmap**
  - Nmap (Network Mapper) is a free and open-source utility used for network discovery and security auditing. It's designed to scan networks to determine available hosts, the services they offer, the operating systems they run, packet filters/firewalls, and many other characteristics.
- **OpenVAS**
  - OpenVAS (Open Vulnerability Assessment System) is a comprehensive vulnerability scanner. It's a framework of several services and tools offering vulnerability management.
- **Qualys**
  - Qualys is a cloud-based platform that provides a suite of security and compliance solutions. It helps organizations identify vulnerabilities in their IT infrastructure, including servers, applications, and networks.
- **bcrypt**
  - bcrypt is a password-hashing function designed to be computationally intensive and resistant to brute-force attacks. It incorporates a salt to protect against rainbow table attacks and uses an adaptive hashing algorithm, meaning the computational cost can be increased over time to keep pace with advancements in computing power.
- **SHA 256**
  - SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that generates a nearly unique 256-bit (32-byte) hash from any input data. This hash acts as a digital fingerprint, meaning even a small change to the input will result in a drastically different hash value.

### 3.5 Enterprise Operations
- **Multi Region Security Planning**
  - Multi-Region Security Planning involves designing and implementing security measures across multiple geographical locations where an application or service is deployed. This includes considering factors like data residency requirements, regional compliance regulations, and the potential for geographically isolated failures or attacks.
- **Large Scale Identity Strategy**
  - A large-scale identity strategy defines how an organization manages and controls digital identities across a vast and complex environment. This includes defining policies, processes, and technologies for creating, managing, and authenticating users and devices, ensuring secure access to resources while maintaining scalability and usability.
- **Certificate Lifecycle**
  - Certificate lifecycle management encompasses all the processes involved in creating, deploying, managing, and eventually revoking digital certificates. This includes requesting certificates from a Certificate Authority (CA), securely storing private keys, distributing certificates to servers and applications, monitoring certificate expiration dates, and renewing or replacing certificates before they expire to maintain secure communication and authentication.
- **PKI Design and Failover**
  - Public Key Infrastructure (PKI) is a system for creating, managing, distributing, using, storing, and revoking digital certificates. These certificates are used to verify the identity of users, devices, and services, enabling secure communication and data exchange.
- **Cryptographic Hashing**
  - Cryptographic hashing is a process that takes an input (or 'message') and produces a fixed-size string of characters, known as a hash. This hash acts as a unique fingerprint of the input data.
- **IDS**
  - An Intrusion Detection System (IDS) monitors a network or systems for malicious activity or policy violations. It analyzes network traffic, system logs, and other data sources to identify suspicious patterns that may indicate an attack or unauthorized access.
- **SBOMS**
  - A Software Bill of Materials (SBOM) is a comprehensive inventory of all components, libraries, and dependencies used in building a software application. It's essentially a list that details the ingredients of your software, much like a nutrition label for food.
- **DDoS Miligation Strategy**
  - A DDoS (Distributed Denial of Service) mitigation strategy is a plan and set of techniques used to protect a system or network from being overwhelmed by malicious traffic. It involves identifying, analyzing, and filtering out illegitimate requests while allowing legitimate users to access the service.
- **Build Pipeline Hardening**
  - Pipeline hardening focuses on securing the automated process that transforms source code into deployable software. This involves implementing security measures at each stage of the pipeline, from code commit to artifact creation, to prevent vulnerabilities from being introduced or exploited.
- **Secure Network Zoning**
  - Secure network zoning involves dividing a network into distinct segments or zones, each with its own security policies and access controls. This segmentation limits the impact of a security breach by containing it within a specific zone, preventing attackers from easily moving laterally across the entire network.
- **Dependency Risk Management**
  - Dependency Risk Management involves identifying, assessing, and mitigating the risks associated with using third-party libraries, frameworks, and other external components in software development. This includes understanding the potential vulnerabilities, licensing issues, and maintenance status of these dependencies to ensure the security and stability of the application.
- **Supply Chain Security**
  - Supply chain security focuses on protecting the integrity and security of all components, processes, and people involved in the development and delivery of software. It aims to prevent malicious actors from introducing vulnerabilities or malicious code into the software supply chain, ensuring that the final product is trustworthy and free from tampering.
- **Endpoint Detection**
  - Endpoint detection involves monitoring and analyzing activities on devices like laptops, desktops, and servers to identify suspicious behavior that could indicate a security threat. This process typically uses software agents installed on these endpoints to collect data, which is then analyzed for patterns and anomalies that might signal malware, unauthorized access, or other malicious activities.
- **SOAR Automation**
  - SOAR (Security Orchestration, Automation, and Response) automation involves using technologies to collect security data from various sources, analyze it, and then automate responses to security incidents. This includes tasks like threat intelligence gathering, vulnerability scanning, incident investigation, and remediation actions.
- **Response Strategy**
  - A response strategy outlines the planned actions an organization will take when a security incident occurs. It defines roles, responsibilities, communication channels, and procedures for identifying, containing, eradicating, and recovering from security breaches.
- **Audit & Compliance Mapping**
  - Audit & Compliance Mapping involves aligning an organization's security controls and practices with relevant regulatory requirements, industry standards, and internal policies. This process identifies which controls satisfy specific compliance obligations, creating a clear relationship between security efforts and the necessary frameworks for legal and operational adherence.
- **Risk Quantification**
  - Risk quantification is the process of assigning measurable values (often monetary) to the potential impact of identified risks. It involves analyzing the probability of a risk occurring and the potential damage it could cause to an organization's assets, operations, or reputation.
- **IPS**
  - An Intrusion Prevention System (IPS) is a network security tool that monitors network traffic for malicious activity. It actively works to block or prevent detected threats, going beyond simple detection to take automated action.
- **SOC 2**
  - SOC 2 (System and Organization Controls 2) is an auditing procedure that ensures service providers securely manage data to protect the interests of their organization and the privacy of its clients. It defines criteria for managing customer data based on five "trust service principles": security, availability, processing integrity, confidentiality, and privacy.
- **ISO 27001**
  - ISO 27001 is an international standard that specifies the requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS). It provides a framework of policies and procedures that includes all legal, physical, and technical controls involved in an organization's information risk management processes.
- **NIST**
  - The NIST Cybersecurity Framework (CSF) is a voluntary framework primarily intended for organizations to manage and reduce cybersecurity risks. It provides a set of standards, guidelines, and best practices to help organizations assess their current cybersecurity posture, identify areas for improvement, and develop a roadmap for enhancing their security capabilities.

---

## 4. Optional / Specialized Topics

- Bash
- PowerShell
- Alert Types
- SIEM
- STRIDE
- Threat Modeling Workflows
- Secure API Design
- Zero Trust Concepts
- Nessus
- Nmap
- OpenVAS
- Qualys
- bcrypt
- SHA 256
- Cryptographic Hashing
- IDS
- SBOMS
- DDoS Miligation Strategy
- Build Pipeline Hardening
- Secure Network Zoning
- Dependency Risk Management
- Supply Chain Security
- Endpoint Detection
- SOAR Automation
- Response Strategy

---

## 5. References

- [DevSecOps Engineer Roadmap](https://roadmap.sh/devsecops)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Cyber Security Specialist
- Frontend Developer

### Related Skills
- Git & GitHub
- System Design
- Docker
- Linux
- Testing