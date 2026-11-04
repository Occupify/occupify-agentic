# AWS

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/aws
- Related Roles:
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is Cloud Computing?**
  - Cloud Computing refers to the delivery of computing services over the internet instead of using local servers. It offers reliable, scalable, and inexpensive cloud computing services which include data storage, databases, applications, analytics, machine learning, and even setting up virtual servers.
- **IaaS vs PaaS vs SaaS**
  - These are the three main cloud service models. IaaS (Infrastructure as a Service) gives you raw compute, storage, and networking, and you manage everything above the OS.
- **Public vs Private vs Hybrid Cloud**
  - Public cloud refers to infrastructure shared across many customers and operated by a provider like AWS. Private cloud is dedicated infrastructure run by a single organization, either on-premises or hosted.
- **Introduction to AWS**
  - AWS is organized into regions and availability zones around the world, each hosting a range of services. You access AWS through the console, CLI, or SDKs, and most services are billed based on actual usage.

### 1.2 EC2
- **Instance Types**
  - EC2 instance types determine the hardware profile of a virtual machine, covering combinations of CPU, memory, storage, and networking capacity. They are grouped into families optimized for different workloads: general purpose, compute optimized, memory optimized, storage optimized, and accelerated computing.
- **CPU Credits**
  - CPU credits apply to burstable instance types in the T family. These instances earn credits when running below their baseline CPU threshold and spend credits when bursting above it.
- **Storage / Volumes**
  - EC2 instances use EBS (Elastic Block Store) volumes as their primary block storage. EBS volumes persist independently of the instance lifecycle and can be snapshotted for backup.
- **Keypairs**
  - Key pairs are part of Amazon EC2 and are used to securely log into your instances. A key pair consists of a public key and a private key.
- **Elastic IP**
  - "Elastic IP" in AWS EC2 is a static IPv4 address designed for dynamic cloud computing. An Elastic IP address is associated with your AWS account not a particular instance, and you control that address until you choose to explicitly release it.
- **User Data Scripts**
  - "User Data Scripts" in EC2 instances are used to perform common automated configuration tasks and even run scripts after the instance starts. These scripts run as the root user, and can be used to install software or download files from an S3 bucket.

### 1.3 VPC
- **AWS Global Infrastructure**
  - AWS Global Infrastructure refers to the layout of AWS regions and availability zones around the world. A region is a geographical area, each consisting of two or more availability zones (AZs) which are engineered to be isolated from failures in other AZs.
- **Shared Responsibility Model**
  - The shared responsibility model defines what AWS secures and what the customer is responsible for. AWS manages the security of the cloud, meaning the physical infrastructure, hardware, and managed services.
- **Well Architected Framework**
  - AWS Well-Architected Framework is a set of strategic guidelines provided by Amazon Web Services. It is designed to provide high-performing and resilient systems while maintaining cost efficiency.
- **CIDR Blocks**
  - "CIDR" stands for Classless Inter-Domain Routing. In AWS VPC, a CIDR block is the IP address block from which private IPv4 addresses and public IPv4 addresses are allocated when you create a VPC.
- **Subnets**
  - Subnets divide a VPC's IP address range into smaller segments, each tied to a specific availability zone. Resources in a subnet inherit its routing configuration, which determines whether they can reach the internet or stay private.
- **Private Subnet**
  - Private subnets in AWS are isolated network segments within your VPC that do not have direct access to the internet. You can use private subnets to run services and applications that should not be directly accessible from the outside world, but still need to communicate with other resources within your VPC.
- **Public Subnet**
  - A public subnet has a route to an Internet Gateway, making resources inside it reachable from the internet when they have a public IP. Load balancers and bastion hosts are commonly placed in public subnets.

### 1.4 IAM
- **Purchasing Options**
  - EC2 offers several purchasing models to balance cost and flexibility. On-Demand instances are billed per second with no commitment.
- **Route Tables**
  - A Route Table in AWS VPC is a set of rules, called routes, that are used to determine where network traffic is directed. Each subnet in your VPC must be associated with a route table, which controls the traffic for the subnet.
- **Security Groups**
  - Security groups act as virtual firewalls for EC2 instances and other resources. They control inbound and outbound traffic using rules based on protocol, port, and source or destination.
- **Internet Gateway**
  - An Internet Gateway is a horizontally scaled, redundant component that connects a VPC to the internet. Attaching one to a VPC and adding a route in a public subnet's route table enables resources with public IPs to send and receive internet traffic.
- **NAT Gateway**
  - A NAT Gateway allows resources in a private subnet to initiate outbound connections to the internet without being directly reachable from it. It is placed in a public subnet and translates the private IP addresses of outgoing traffic to its own public IP.
- **Policies**
  - IAM policies are JSON documents that define permissions. A policy specifies which actions are allowed or denied on which resources, and under what conditions.
- **Users / User Groups**
  - IAM users represent individual people or applications that need programmatic or console access to AWS. User groups let you apply the same set of policies to multiple users at once, simplifying access management.
- **Roles**
  - IAM Roles in AWS are a form of secure access control that do not directly associate with specific users or groups. Instead, trusted entities such as AWS users, applications or services (like EC2) can take on roles to obtain temporary security credentials for making AWS API requests.
- **Identity-based**
  - Identity-based policies are attached to IAM identities: users, groups, or roles. They define what actions that identity is allowed to perform across AWS services and resources.
- **Resource-based**
  - Resource-based policies are attached directly to the AWS resources that receive the permissions. The policy then specifies what actions are allowed or denied on that particular resource.

### 1.5 Auto-Scaling
- **AMIs**
  - Amazon Machine Images (AMIs) are pre-configured templates for EC2 instances. When you launch an instance in EC2, you start with an AMI.
- **Launch Templates**
  - "Launch Templates" in AWS Auto Scaling are configurations that an Auto Scaling group uses to launch EC2 instances. They store the configuration information necessary to launch an instance, which includes the ID of the Amazon Machine Image (AMI), the instance type, a key pair, security groups, and the storage configuration.
- **Auto-Scaling Groups**
  - An Auto Scaling group manages a collection of EC2 instances as a unit. You define a minimum, maximum, and desired capacity, and the group maintains that count by launching or terminating instances as needed.

---

## 2. Intermediate

### 2.1 S3
- **Instance Profiles**
  - Instance profiles are AWS IAM entities that you can use to grant permissions to applications running on your EC2 instances. They effectively allow your instances to make secure API requests.
- **Assuming Roles**
  - Assuming a role means temporarily taking on a different set of permissions defined by that role. This is done using the STS AssumeRole API call, which returns short-lived credentials.
- **Buckets / Objects**
  - In AWS S3, a "bucket" is a container for data. It is used to store objects.

### 2.2 SES
- **Sandbox / Sending Limits**
  - In AWS SES, when your account is in the sandbox (default mode for all new accounts), you can only send emails to verified email addresses and the maximum send rate is 1 email per second. The maximum sending quota is 200 messages per 24-hour period.
- **Identity Verification**
  - Amazon Simple Email Service (SES) requires users to verify their identities to ensure they own the email addresses or domains they plan to use as 'From', 'Source', 'Sender', or 'Return-Path' addresses. The verification process prevents unauthorized use of identities.
- **DKIM Setup**
  - DKIM (DomainKeys Identified Mail) adds a cryptographic signature to outgoing emails that recipients can verify. Setting up DKIM in SES involves publishing DNS records with a public key that SES uses to sign your messages.
- **Feedback Handling**
  - SES can receive delivery notifications, bounces, and complaint feedback from recipient mail servers. These events are delivered via SNS or SQS and should be processed to remove invalid addresses and maintain a clean sending list.
- **Configuration Sets**
  - Configuration sets in SES are groups of rules applied to outgoing emails. They enable tracking of events like sends, bounces, complaints, and clicks by routing data to CloudWatch, SNS, Kinesis, or S3.
- **Sender Reputation**
  - Sender reputation in Amazon Web Services (AWS) Simple Email Service (SES) is essentially a measure of your sending practices and how they align with the expectations of ISPs and email recipients. This reputation is determined by factors such as your email bounce rate, complaints, content quality, email volume, consistency of email sending, etc.
- **Dedicated IP**
  - "Dedicated IP" in AWS SES (Simple Email Service) refers to a unique IP address that can be used exclusively by a single AWS SES customer for sending emails. When you choose to use a dedicated IP, you get full control over the reputation of that IP address, which is beneficial when sending large volume of emails.

### 2.3 Route53
- **Hosted Zones**
  - Route53 routing policies determine how DNS queries are answered when multiple records exist. Simple routing returns a single value.
- **Routing Policies**
  - Route53 routing policies determine how DNS queries are answered when multiple records exist. Simple routing returns a single value.
- **Health Checks**
  - Route53 health checks monitor the availability of endpoints by sending periodic requests and checking the response. If an endpoint fails its health check, Route53 can stop routing traffic to it, which is central to failover routing policies.

### 2.4 Storage Types
- **Scaling Policies**
  - Scaling policies determine when and how an Auto Scaling group changes its capacity. Target tracking policies adjust instance count to keep a metric like CPU utilization at a target value.
- **Elastic Load Balancers**
  - Elastic Load Balancing distributes incoming traffic across multiple EC2 instances or targets. AWS offers three types: Application Load Balancer for HTTP/HTTPS traffic with content-based routing, Network Load Balancer for high-performance TCP/UDP routing, and Gateway Load Balancer for traffic inspection appliances.
- **Bucket / Object Lifecycle**
  - AWS S3 Lifecycle is a feature within the AWS S3 resources that allows users to manage their objects so that they are automatically transferred to different storage classes or expire at the end of their lifetimes. It facilitates transitioning objects between different storage classes at set times or according to specified conditions, and can also automate the cleanup of expired objects to help reduce storage consumed by obsolete data.
- **Standard**
  - Amazon S3 Standard storage is designed for general-purpose storage of frequently accessed data. It provides low latency and high throughput, making it suitable for a wide variety of use cases, including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics.
- **S3-IA**
  - Amazon S3 Infrequent Access (S3 IA) is a storage class in Amazon S3 designed for data that is accessed less frequently, but requires rapid access when needed. S3 IA offers the high durability, high throughput, and low latency of Amazon S3 Standard, with a lower cost per GB for storage and a per GB retrieval fee.
- **Glacier**
  - AWS Glacier is a secure, durable, and extremely low-cost storage service for data archiving and long-term backup. It is designed to reliably store data for as long as you need.

### 2.5 Cloudwatch
- **Metrics**
  - In Amazon CloudWatch, metrics are fundamental concepts that you work with. A metric is the fundamental concept in CloudWatch and represents a time-ordered set of data points that are published to CloudWatch.
- **Events**
  - CloudWatch Events (now part of EventBridge) lets you respond to changes in your AWS environment by routing events to targets like Lambda functions, SQS queues, or SNS topics. You can trigger actions on a schedule using cron expressions or react to events like an EC2 instance stopping or an S3 object being created.
- **Logs**
  - AWS CloudWatch Logs service allows you to monitor, store, and access your log files from Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS CloudTrail, and other sources. It centralizes the logs from all your systems, applications, and AWS services that you use, into a single, highly scalable service.

### 2.6 RDS
- **DB Instances**
  - The term "DB Instance" is used within the context of Amazon's Relational Database Service (RDS). A DB Instance is essentially an isolated database environment in the cloud, run within Amazon RDS.
- **Storage Types**
  - RDS supports three storage types. General Purpose SSD (gp2/gp3) is the default for most workloads, balancing cost and performance.
- **Backup / Restore**
  - RDS performs automated backups of the database and transaction logs within a configurable retention window of up to 35 days. You can restore to any point in time within that window.
- **General Purpose**
  - General Purpose SSD storage in RDS uses gp2 or gp3 volumes and is suitable for most database workloads. gp3 lets you provision IOPS and throughput independently from storage size, offering better cost control.
- **Provisioned IOPS**
  - "Provisioned IOPS" is a storage option available in Amazon Web Services' (AWS) Elastic Block Store (EBS). This option is designed to deliver fast, predictable, and consistent I/O performance.

### 2.7 DynamoDB
- **Tables / Items / Attributes**
  - In Amazon DynamoDB, tables are a collection of items. An item is a group of attributes that is identified by a primary key.
- **Primary Keys / Secondary Indexes**
  - Every DynamoDB table requires a primary key, which uniquely identifies each item. A simple primary key uses just a partition key; a composite primary key uses a partition key and a sort key together.
- **Data Modeling**
  - Data modeling in DynamoDB requires a different approach than relational databases. Because DynamoDB does not support joins, related data is often stored together in a single table using a single-table design pattern.
- **Streams**
  - DynamoDB Streams captures a time-ordered sequence of item-level changes in a table. Each stream record contains information about what changed, including the old and new item state.
- **Capacity Settings**
  - DynamoDB offers two capacity modes. Provisioned mode requires you to specify read and write capacity units in advance, and you can enable Auto Scaling to adjust them automatically.
- **Limits**
  - DynamoDB has several limits to be aware of. Item size is capped at 400KB.
- **DynamoDB Local**
  - DynamoDB Local is a downloadable version of Amazon DynamoDB that lets you write and test applications without accessing the real AWS services. It mimics the actual DynamoDB service.

---

## 3. Advanced

### 3.1 ElastiCache
- **Quotas**
  - AWS ElastiCache quotas define the limit on the maximum number of clusters, nodes, parameter groups, and subnet groups you can create in an AWS account. These quotas vary by region and can be increased upon request to the AWS Service team.

### 3.2 ECR
- **Backup / Restore**
  - DynamoDB supports on-demand backups that create full snapshots of a table at any point in time, stored without affecting table performance. Point-in-time recovery (PITR) lets you restore a table to any second within the last 35 days.

### 3.3 Cloudfront
- **Magnetic**
  - "Magnetic" in AWS refers to Magnetic storage, also known as Amazon EBS (Elastic Block Store) Magnetic volumes. These storage types are designed for workloads where data is accessed infrequently, and sceneries where the lowest storage cost is important.
- **Distributions**
  - A CloudFront distribution is the configuration that defines how content is delivered. It specifies the origin (where CloudFront fetches content), cache behaviors, supported protocols, and geographic restrictions.
- **Policies**
  - CloudFront policies control what gets cached and how. Cache policies define which headers, cookies, and query strings CloudFront includes in the cache key and forwards to the origin.
- **Invalidations**
  - Invalidations in AWS CloudFront is a concept where you remove files (objects) from CloudFront cache before it hits the expiration period. AWS CloudFront, like any other CDN, stores copies of your website’s static files in its cache until and unless it reaches its TTL (time to live) duration.

### 3.4 ECS
- **Services**
  - AWS ECS Services are defined as a set of part or all of your task definitions that run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster. If any of your tasks should fail or stop for any reason, the Amazon ECS service scheduler launches another instance of your task definition to replace it and maintain the desired count of tasks, ensuring the service's reliability and availability.

### 3.5 EKS
- **EKS**
  - EKS (Elastic Kubernetes Service) is a managed Kubernetes service that runs the Kubernetes control plane on AWS. It handles upgrades, patching, and high availability of the control plane, while you manage the worker nodes or use Fargate for serverless pods.

### 3.6 Lambda
- **Clusters / ECS Container Agents**
  - In AWS, an ECS Cluster is a logical grouping of tasks or services. If you run tasks or create services, you do it inside a cluster, so it's a vital building block of the Amazon ECS infrastructure.
- **Tasks**
  - Tasks in Amazon ECS are the instantiation of a task definition within a cluster. They can be thought of as the running instance of the definition, the same way an object is an instance of a class in object-oriented programming.
- **Launch Config / Autoscaling Groups**
  - Launch Configuration is a template that an Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances such as the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping.
- **Fargate**
  - Fargate is a technology used for the deployment of containers in Amazon's Elastic Container Service (ECS). This technology completely removes the need to manage the EC2 instances for your infrastructure; therefore, you would not have to be concerned about selecting the right type of EC2 instances, deciding when to scale your clusters, or optimizing cluster packing.
- **Creating / Invoking Functions**
  - A Lambda function is created by uploading code and specifying a runtime, handler, and execution role. Functions can be invoked synchronously (waiting for a response), asynchronously (fire and forget), or through event source mappings that poll queues and streams.
- **Layers**
  - Lambda layers are archives containing libraries, dependencies, or custom runtimes that can be shared across multiple functions. Instead of bundling dependencies in each deployment package, you attach a layer and Lambda makes its contents available to the function at runtime.
- **Custom Runtimes**
  - Lambda provides managed runtimes for languages like Python, Node.js, Java, and Go. For unsupported languages or custom configurations, you can provide a custom runtime using the Lambda Runtime API.
- **Versioning / Aliases**
  - Lambda supports versioning, which lets you publish immutable snapshots of a function. Each version has its own ARN and configuration.
- **Event Bridge / Scheduled Execution**
  - EventBridge (formerly CloudWatch Events) is a serverless event bus that connects Lambda to AWS services and custom applications. You can configure rules to invoke Lambda functions on a schedule using cron or rate expressions, or in response to events from AWS services like S3, EC2, or CodePipeline.
- **Cold Start and Limitations**
  - A cold start happens when Lambda initializes a new execution environment for a function that has not been run recently. During initialization, the runtime and your code are loaded, which adds latency to the first invocation.
- **API Gateway**
  - API Gateway is a fully managed service for creating, deploying, and securing APIs at scale. It supports REST, HTTP, and WebSocket APIs and integrates directly with Lambda, making it a common entry point for serverless backends.
- **Lambda@Edge**
  - Lambda Edge is a feature of AWS Lambda that allows you to run coding functions at AWS edge locations, closest to your customers. This can result in lower latency response times and better customer experiences.

---

## 4. Optional / Specialized Topics

- Elastic IP
- User Data Scripts
- Subnets
- Private Subnet
- Public Subnet
- NAT Gateway
- Policies
- Users / User Groups
- Roles
- Identity-based
- Resource-based
- Configuration Sets
- Sender Reputation
- Dedicated IP
- S3-IA
- Glacier
- Provisioned IOPS
- Capacity Settings
- Limits
- DynamoDB Local
- Creating / Invoking Functions
- Layers
- Custom Runtimes
- Versioning / Aliases
- Event Bridge / Scheduled Execution

---

## 5. References

- [AWS Roadmap](https://roadmap.sh/aws)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer

### Related Skills
- Computer Science
- Cloudflare
- Linux