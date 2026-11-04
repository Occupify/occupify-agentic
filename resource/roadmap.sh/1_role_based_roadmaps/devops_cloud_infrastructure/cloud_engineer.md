# Cloud Engineer

## Metadata
- Type: Role
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/cloud-computing
- Related Roles:
  - DevOps Engineer
  - Inference Engineering
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **Cloud vs On-Premises**
  - On-premises infrastructure means owning and operating physical servers in your own data center or server room. Cloud infrastructure means renting virtualized resources from a provider who manages the physical layer.
- **Multi-Tenancy**
  - Multi-tenancy means multiple customers share the same physical infrastructure, with each customer's data and workloads isolated from the others. Cloud providers are multi-tenant by default.
- **Region, Availability Zone**
  - A region is a geographic area where a cloud provider operates one or more data centers, such as us-east-1 or europe-west1. Within a region, availability zones are physically separate data centers connected by low-latency links.
- **Instance**
  - An instance is a single virtual server running in the cloud. You choose its size (CPU, memory, storage) from a catalog of instance types and pay for it by the second or hour.
- **Workload**
  - A workload is any application, service, or process running on cloud infrastructure. The term is used to describe what you are running without specifying how: a web application, a batch job, a machine learning training run, and a real-time data pipeline are all workloads.
- **Elasticity**
  - Elasticity is the ability of a system to automatically provision and release resources in response to demand. A highly elastic system scales out when traffic increases and scales back in when it drops, paying only for what it uses.
- **Scalability**
  - Scalability is the capacity of a system to handle growing demand. Vertical scaling adds more power to a single machine (bigger instance).
- **Cluster**
  - A cluster is a group of servers (or instances) that work together as a single system. Clusters are used to distribute workloads, provide redundancy, and scale horizontally.
- **Shell / Bash**
  - Bash is the default shell on most Linux systems and the primary language for writing automation scripts in cloud environments. It is used to chain commands, manage files, interact with CLIs, and automate repetitive tasks.
- **Version Control**
  - Version control tracks changes to code and configuration over time, enabling collaboration and rollback. Git is the standard tool.
- **Networking Basics**
  - Networking basics covers the fundamental concepts that underpin how computers communicate: IP addresses, subnets, ports, protocols (TCP, UDP, HTTP, HTTPS), and DNS. Cloud networking builds directly on these concepts, and without them, topics like VPCs, security groups, and load balancers are difficult to reason about.
- **Python**
  - Python is a general-purpose programming language widely used for scripting, automation, and interacting with cloud APIs. In a cloud context, it is the go-to language for writing infrastructure automation scripts, Lambda functions, CLI tools, and data pipelines.
- **Linux**
  - Linux is the operating system that runs the vast majority of cloud servers, containers, and managed services. Working in the cloud means reading logs, navigating filesystems, managing processes, and configuring services from a Linux shell.

### 1.2 Cloud Deployment Models
- **Public Cloud**
  - A public cloud is infrastructure owned and operated by a third-party provider and shared across multiple customers. AWS, GCP, and Azure are public clouds.
- **Private Cloud**
  - A private cloud is infrastructure dedicated to a single organization, either hosted on-premises or in a colocation facility. It offers more control over hardware, network configuration, and data residency than public cloud, which matters for certain regulatory or security requirements.
- **Hybrid Cloud**
  - A hybrid cloud connects private and public cloud environments, allowing workloads to move between them. A common pattern is running sensitive or latency-critical workloads on-premises while using public cloud for burst capacity, backups, or less sensitive services.
- **Multi-Cloud**
  - Multi-cloud means using services from more than one cloud provider simultaneously. Organizations adopt multi-cloud to avoid vendor lock-in, meet data residency requirements in regions where one provider has no presence, or use best-of-breed services from different providers.
- **Provisioning**
  - Provisioning is the process of setting up and configuring cloud resources so they are ready to use. This includes creating instances, allocating storage, configuring networks, and applying security policies.
- **Latency & Throughput**
  - Latency is the time it takes for a single request to travel from sender to receiver and back. Throughput is the amount of data or number of requests a system can handle per unit of time.
- **Endpoint**
  - An endpoint is a URL or network address where a service can be reached. Cloud services expose endpoints for APIs, storage buckets, databases, and load balancers.
- **SLA**
  - An SLA (Service Level Agreement) is a contract between a cloud provider and a customer that defines the expected level of service, typically expressed as an uptime percentage. AWS S3, for example, offers a 99.99% availability SLA.
- **Cybersecurity Basics**
  - Cybersecurity basics covers the core concepts a cloud practitioner needs before working with security services: what encryption is and how it works, what a firewall does, what a certificate is and why it matters, and the difference between authentication and authorization. Cloud environments expose a large attack surface, and knowing the vocabulary makes the security sections of the roadmap approachable.

### 1.3 Cloud Service Models
- **IaaS**
  - IaaS (Infrastructure as a Service) gives you raw computing resources over the internet: virtual machines, storage, and networking, without the overhead of managing physical hardware. You control the operating system and everything above it; the provider manages the physical layer.
- **PaaS**
  - PaaS (Platform as a Service) provides a managed environment for deploying and running applications, abstracting away the underlying infrastructure. You bring your code; the platform handles the runtime, scaling, patching, and availability.
- **SaaS**
  - SaaS (Software as a Service) delivers fully managed applications over the internet. The provider handles everything: infrastructure, runtime, application code, and updates.
- **FaaS**
  - FaaS (Function as a Service) lets you deploy individual functions that run in response to events, with no server management. The provider handles all infrastructure, scaling to zero when idle and scaling out automatically under load.
- **DaaS**
  - DaaS (Desktop as a Service) delivers a virtual desktop environment from the cloud to any device with a browser or thin client. The provider hosts and manages the underlying infrastructure, operating system, and desktop software.

### 1.4 Provider Landscape
- **Hyperscalers**
  - Hyperscalers are cloud providers that operate at massive global scale, with data centers in dozens of regions and hundreds of services covering compute, storage, networking, AI, databases, and more. AWS, Google Cloud Platform, and Microsoft Azure are the three hyperscalers.
- **Regional Cloud**
  - Regional cloud providers operate in specific geographies and are often chosen for data residency, latency, or cost reasons. Examples include Hetzner and OVH in Europe, and UpCloud in the Nordics.
- **Developer-Focused**
  - Developer-focused cloud providers simplify deployment and operations for smaller teams and individual developers. DigitalOcean, Render, and Fly fall into this category.
- **Provider Lock-In**
  - Provider lock-in occurs when an application becomes so dependent on a specific cloud provider's proprietary services that migrating to another provider is costly or technically difficult. Deep use of provider-specific services (managed databases, serverless platforms, AI APIs) accelerates lock-in.
- **Managed Kubernetes**
  - Some providers specialize in managed Kubernetes as their primary product, targeting teams that want Kubernetes without the complexity of running it on a hyperscaler. Civo and Vultr are examples.
- **Azure**
  - Microsoft Azure is the second-largest cloud provider, with particular strength in enterprise environments due to its deep integration with Microsoft products such as Active Directory, Office 365, and Windows Server. Azure is the preferred choice for organizations already running Microsoft workloads and has strong hybrid cloud capabilities through services like Azure Arc.
- **AWS**
  - AWS (Amazon Web Services) is the largest cloud provider by market share, launched by Amazon in 2006. It offers over 200 services across compute, storage, networking, databases, machine learning, and more, available in regions across every major continent.
- **GCP**
  - GCP (Google Cloud Platform) is Google's public cloud, known for its strengths in data analytics, machine learning, and Kubernetes, which Google originally developed. BigQuery, Vertex AI, and Google Kubernetes Engine are among its most widely used services.

### 1.5 Data Centers
- **Racks, Pods, & Aisles**
  - Servers are housed in vertical metal frames called racks. Racks are grouped into pods, a logical unit of co-located racks managed together for power, cooling, and network purposes.
- **Power & Cooling**
  - Data centers consume enormous amounts of electricity and generate significant heat. Power is delivered through redundant feeds, uninterruptible power supplies (UPS), and diesel generators to ensure no single failure causes an outage.
- **Lights-Out Operations**
  - A lights-out data center is designed to operate without on-site staff. Hardware is monitored, managed, and in many cases repaired remotely through out-of-band management interfaces like IPMI or iDRAC.
- **Network Topology**
  - A data center's internal network connects thousands of servers and must handle massive volumes of east-west traffic (between servers) in addition to north-south traffic (between servers and the internet). Modern data center networks are designed to be non-blocking, highly redundant, and software-configurable to support the dynamic workloads cloud environments demand.
- **Upstream Connectivity**
  - Upstream connectivity is how a data center connects to the public internet. Providers maintain multiple redundant fiber connections to upstream ISPs and peer directly with other networks at internet exchange points (IXPs) to reduce latency and transit costs.

### 1.6 Virtual Machines
- **Hypervisors**
  - A hypervisor is the software layer that makes virtualization possible. It sits between the physical hardware and the virtual machines running on top of it, allocating CPU, memory, and I/O resources to each VM while keeping them isolated from one another.
- **VM Migration, Live Migration**
  - VM migration moves a virtual machine from one physical host to another. Standard migration requires the VM to be powered off, causing downtime.

### 1.7 Containers
- **Docker**
  - Docker is the most widely used container platform. It provides a CLI and daemon for building container images, running containers, and managing their lifecycle on a single host.
- **VMs vs Containers**
  - Virtual machines virtualize hardware, giving each VM its own OS kernel, which provides strong isolation but comes with significant overhead in memory and startup time. Containers share the host OS kernel and isolate processes using Linux namespaces and cgroups, making them faster to start and more resource-efficient.

---

## 2. Intermediate

### 2.1 Databases
- **Managed Relational DBs**
  - Managed relational databases provide SQL-compatible storage with ACID guarantees, automatic backups, and multi-AZ failover, without requiring manual database administration. AWS RDS, Google Cloud SQL, and Azure Database for PostgreSQL are examples.
- **NoSQL Databases**
  - NoSQL databases store data in formats other than relational tables: key-value pairs, documents, wide columns, or graphs. They are designed for horizontal scalability and flexible schemas, making them well suited to workloads with high write volumes, variable data structures, or access patterns that don't fit SQL queries well.

### 2.2 Instance Types
- **Virtual Machine Instances**
  - Cloud providers offer a catalog of virtual machine instance types, each with a fixed combination of CPU, memory, and network bandwidth. Instance families are optimized for different workloads: general-purpose instances balance compute and memory, compute-optimized instances have a higher CPU-to-memory ratio for CPU-intensive tasks, memory-optimized instances suit in-memory databases and analytics, and GPU instances are used for machine learning and graphics workloads.
- **Bare Metal Cloud**
  - Bare metal cloud gives you exclusive access to a physical server with no hypervisor layer. You get the full resources of the machine without virtualization overhead, which matters for workloads that require maximum I/O performance, low and predictable latency, or cannot run in a virtualized environment due to licensing or compliance constraints.

### 2.3 Scaling
- **Auto Scaling**
  - Auto scaling automatically adjusts the number of running instances based on demand. A scaling policy monitors a metric (CPU utilization, request rate, queue depth) and triggers the addition or removal of instances to match load.
- **Spot & Reserved Instances**
  - Spot instances (AWS) and their equivalents on other providers (preemptible VMs on GCP, spot VMs on Azure) use spare provider capacity at discounts of up to 90% compared to on-demand pricing, but can be reclaimed with short notice when the provider needs the capacity back. Reserved instances commit to a one or three year term in exchange for a significant discount on on-demand rates.
- **Virtual Private Cloud**
  - A VPC (Virtual Private Cloud) is a logically isolated network you define within a cloud provider's infrastructure. Your cloud resources run inside it, invisible to other customers on the same physical hardware.

### 2.4 Core Networking
- **Subnets & Routing**
  - A VPC is divided into subnets, each assigned a CIDR block and typically tied to a specific availability zone. Public subnets have a route to an internet gateway, making resources in them reachable from the internet.
- **NAT & IP Management**
  - Resources in private subnets often need to make outbound requests to the internet (to download updates, call external APIs) without being reachable from outside. A NAT gateway handles this by translating private IP addresses to a public one for outbound traffic.
- **VLANs & VXLAN**
  - VLANs (Virtual Local Area Networks) segment a physical network into isolated logical networks at Layer 2. In large-scale cloud environments, VLANs alone cannot provide enough isolation across distributed data centers.
- **SDN**
  - SDN (Software-Defined Networking) separates the network control plane, which decides where traffic goes, from the data plane, which actually forwards packets. In cloud environments, SDN lets providers manage network topology programmatically, enabling VPCs, dynamic routing, network policies, and virtual appliances without touching physical hardware.

### 2.5 Traffic Management
- **VPN & Direct Connect**
  - VPN (Virtual Private Network) tunnels encrypted traffic between an on-premises network and a cloud VPC over the public internet. It is quick to set up and low cost but shares bandwidth with internet traffic.
- **DNS in the Cloud**
  - Cloud DNS services resolve domain names to cloud resources and go beyond basic A record management. They support latency-based routing (directing users to the nearest region), geolocation routing, weighted routing for gradual traffic shifts, and health-check-based failover that automatically removes unhealthy endpoints.
- **Load Balancers**
  - A load balancer distributes incoming traffic across multiple backend instances to prevent any single server from becoming a bottleneck. Layer 4 load balancers operate at the TCP/UDP level and route traffic based on IP and port.
- **Firewalls & Security Groups**
  - Security groups are stateful virtual firewalls attached to individual instances or network interfaces. They define which inbound and outbound traffic is allowed by port, protocol, and source IP or security group.
- **CDN & Edge Caching**
  - A CDN (Content Delivery Network) distributes static and cacheable content (images, scripts, video, API responses) to servers located geographically close to end users, reducing latency and offloading traffic from the origin server. Edge caching stores responses at the CDN layer so repeated requests are served without reaching the origin.

### 2.6 Storage Types
- **Object Storage**
  - Object storage stores data as discrete objects, each consisting of the data itself, metadata, and a unique identifier, in a flat namespace without folder hierarchy. Access is through HTTP APIs rather than a filesystem interface.
- **Block Storage**
  - Block storage provides raw storage volumes that attach to instances and behave like physical disks. The operating system formats them with a filesystem and reads and writes to them at the block level.
- **File Storage**
  - File storage provides a managed shared filesystem accessible by multiple instances simultaneously over standard protocols like NFS or SMB. Unlike block storage, which is attached to a single instance, file storage can be mounted by many instances at once, making it suited for shared application data, content management systems, and HPC workloads that require a common filesystem.
- **NAS and SAN**
  - NAS (Network Attached Storage) provides file-level storage access over a network, typically using NFS or SMB protocols. SAN (Storage Area Network) provides block-level storage access over a dedicated high-speed fabric, appearing to the server as a locally attached disk.

### 2.7 Data Lifecycle
- **Storage Classes & Tiering**
  - Cloud object storage services offer multiple storage classes with different cost and retrieval trade-offs. Hot tiers store frequently accessed data at higher cost per GB but with immediate retrieval.
- **Data Archiving**
  - Data archiving is the long-term retention of data that is rarely accessed but must be preserved for compliance, legal, or historical purposes. Archive storage classes are designed for this use case, offering very low storage costs in exchange for slow retrieval.
- **Retention & Compliance**
  - Data retention policies define how long data must be stored and when it can or must be deleted. Compliance requirements (GDPR, HIPAA, SOC 2, PCI DSS) impose specific rules on data storage duration, access controls, encryption, and audit logging.

### 2.8 Serverless Computing
- **Stateless Functions**
  - Stateless functions are small, single-purpose code segments that process data and return a result without saving any information or "state" from previous executions. Each time the function runs, it treats the request as a completely new event, independent of any prior interactions.
- **Event-Driven Architecture**
  - Event-driven architecture is a design pattern where services communicate by producing and consuming events rather than making direct calls to each other. An event (a file upload, a database write, a user action, a scheduled trigger) causes one or more functions or services to execute in response.
- **Serverless Platforms**
  - The main serverless platforms are AWS Lambda, Google Cloud Run Functions, and Azure Functions. Each executes code in short-lived, stateless containers triggered by events from the provider's ecosystem: API Gateway requests, S3 uploads, Pub/Sub messages, database streams, and more.
- **Trade-offs of Serverless**
  - Serverless reduces operational overhead but introduces its own constraints. Cold starts add latency on the first invocation after a period of inactivity, which matters for latency-sensitive applications.

### 2.9 Microservices
- **Monolithic vs Microservices**
  - A monolithic application packages all functionality into a single deployable unit. Every feature shares the same codebase, runtime, and database, making it straightforward to develop and test locally but increasingly difficult to scale and deploy as it grows.
- **Microservices Communication**
  - Services in a microservices architecture communicate either synchronously or asynchronously. Synchronous communication uses HTTP/REST or gRPC: the caller waits for a response before continuing.
- **Service Mesh**
  - A service mesh is an infrastructure layer that handles service-to-service communication in a microservices architecture. It manages traffic routing, load balancing, retries, timeouts, circuit breaking, and mutual TLS encryption between services, without any of that logic living in application code.

### 2.10 Edge Computing
- **Edge vs Cloud**
  - Cloud computing centralizes compute in large, efficient data centers with global reach but introduces latency for users and devices far from those regions. Edge computing distributes compute to locations near the source of data or the end user, reducing round-trip time at the cost of smaller, less powerful hardware and more complex operations.

---

## 3. Advanced

### 3.1 AI/ML Services
- **AI/ML Services**
  - Cloud providers offer managed AI and machine learning services that remove the need to build and maintain ML infrastructure from scratch. These range from pre-trained model APIs (vision, speech, translation, natural language) to fully managed training and serving platforms (SageMaker, Vertex AI, Azure ML).

### 3.2 Infrastructure as Code
- **Terraform**
  - Terraform is a provider-agnostic IaC tool that uses a declarative configuration language (HCL) to define infrastructure across AWS, GCP, Azure, and hundreds of other providers. You describe the desired state of your resources, and Terraform calculates a plan showing what it will create, change, or destroy, then applies it.
- **Configuration Management**
  - Configuration management tools manage the state of software and settings on existing servers. Ansible, Chef, and Puppet are the main tools.
- **Levels of Automation**
  - Cloud automation exists on a spectrum. At the lowest level, engineers run manual commands through a console or CLI.

### 3.3 Container Orchestration
- **Kubernetes**
  - Kubernetes is the standard container orchestration platform. You define workloads as declarative specs (Pods, Deployments, StatefulSets, Services) and Kubernetes continuously reconciles the actual state of the cluster with the desired state.
- **GitOps**
  - GitOps is an operational model where Git is the single source of truth for both application and infrastructure configuration. All changes are made through pull requests and code review; automated pipelines detect changes and apply them to the cluster without manual intervention.

### 3.4 CI/CD
- **CI/CD Pipelines**
  - A CI/CD pipeline is an automated workflow that runs whenever code changes are committed. Continuous Integration (CI) builds and tests the change to verify it does not break existing functionality.
- **Artifact Registries**
  - An artifact registry stores versioned build outputs produced by CI pipelines: container images, compiled binaries, and software packages. Registries sit between the build system and deployment targets, ensuring that what gets deployed is immutable, traceable, and consistent across environments.
- **Deployment Strategies**
  - Deployment strategies control how new application versions are released to minimize risk and downtime. A blue/green deployment maintains two identical environments and switches all traffic from old to new instantly, with fast rollback by switching back.

### 3.5 Access Control
- **Shared Responsibility Model**
  - The shared responsibility model defines which security tasks the cloud provider handles and which the customer must handle. The provider is responsible for the security of the cloud: physical infrastructure, hardware, hypervisors, and managed service internals.
- **IAM**
  - IAM (Identity and Access Management) is the system that controls who can access cloud resources and what they can do with them. Every action in a cloud environment (launching an instance, reading a bucket, calling an API) is authorized through IAM.
- **RBAC**
  - RBAC (Role-Based Access Control) assigns permissions to roles rather than to individual users. Users or service accounts are then assigned roles, inheriting the permissions those roles define.

### 3.6 Data Protection
- **Zero Trust**
  - Zero Trust is a security model based on the principle of never trust, always verify. No user or system is trusted by default, even if they are inside the corporate network.
- **Encryption**
  - Encryption protects data by transforming it into an unreadable format that can only be decoded with the correct key. Encryption at rest protects stored data (in databases, object storage, disk volumes) from unauthorized access if physical or logical storage is compromised.
- **Secrets Management**
  - Secrets management is the practice of storing, accessing, and rotating sensitive values (API keys, database passwords, certificates, tokens) securely. Hardcoding secrets in application code or environment variables is a common source of security breaches.
- **Privacy & Compliance**
  - Cloud compliance means meeting regulatory and legal requirements for how data is stored, processed, and accessed. Common frameworks include GDPR (EU data privacy), HIPAA (US healthcare data), SOC 2 (service organization controls), and PCI DSS (payment card data).

### 3.7 Pricing Models
- **Cost Monitoring and Budgets**
  - Cloud costs are dynamic and can grow unexpectedly as workloads scale or resources are left running. Cost monitoring tools (AWS Cost Explorer, GCP Cost Management, Azure Cost Analysis) provide visibility into spending by service, region, tag, and time period.
- **Resource Optimization**
  - Resource optimization reduces cloud spend by eliminating waste and right-sizing infrastructure. Common patterns include terminating unused instances and idle resources, downsizing over-provisioned instances based on actual utilization data, using auto scaling to avoid paying for unused capacity, and replacing always-on instances with serverless or spot workloads where appropriate.
- **FinOps**
  - FinOps (Cloud Financial Operations) is a practice and organizational model for managing cloud spending collaboratively across engineering, finance, and business teams. It brings financial accountability to variable cloud costs by establishing processes for cost visibility, allocation, forecasting, and optimization.

---

## 4. Optional / Specialized Topics

- Workload
- Elasticity
- Scalability
- Cluster
- Shell / Bash
- Version Control
- Networking Basics
- Python
- Linux
- Provisioning
- Latency & Throughput
- Endpoint
- SLA
- Cybersecurity Basics
- DaaS
- Managed Kubernetes
- Azure
- AWS
- GCP
- Upstream Connectivity
- CDN & Edge Caching

---

## 5. References

- [Cloud Engineer Roadmap](https://roadmap.sh/cloud-computing)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Inference Engineering
- Frontend Developer

### Related Skills
- AWS
- Backend Beginner