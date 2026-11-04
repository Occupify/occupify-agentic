# Kubernetes

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/kubernetes
- Related Roles:
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **Overview of Kubernetes**
  - Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem.
- **Why use Kubernetes?**
  - Kubernetes (k8s) is needed because it provides a powerful and flexible platform for deploying and managing containerized applications at scale. It allows for easy scalability, high resilience, application portability, automation of many tasks, and standardization of the container platform.
- **Key Concepts and Terminologies**
  - Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Here are some important concepts and terminologies in Kubernetes:
- **Kubernetes Alternatives**
  - Kubernetes is a popular open-source container orchestration tool that is widely used for managing and deploying containerized applications. While there are other container orchestration tools available, such as Docker Swarm, Mesos, and Nomad, there are some key differences between Kubernetes and these other tools and some of them are mentioned below:

### 1.2 Containers
- **Containers**
  - Kubernetes is built on containers, so before learning Kubernetes you should be comfortable running and building containers from scratch.

### 1.3 Setting up Kubernetes
- **Deploying your First Application**
  - To deploy your first application in Kubernetes, you need to create a deployment and service manifest in YAML files, apply the manifests to your Kubernetes cluster using the kubectl apply command, verify that your application's pods are running with kubectl get pods, and test the service with kubectl get services and accessing the service using a web browser or a tool like cURL. There are also various tools and platforms available that can simplify application deployment in Kubernetes, such as Helm charts and Kubernetes operators.
- **Choosing a Managed Provider**
  - A managed provider is a cloud-based service that provides a managed Kubernetes environment. This means that the provider handles the underlying infrastructure, such as servers, storage, and networking, as well as the installation, configuration, and maintenance of the Kubernetes cluster.
- **Installing a Local Cluster**
  - To install and configure a Kubernetes cluster on CentOS 7 or Ubuntu, you would need to setup the prerequisites and requirements for setting up a Kubernetes cluster after which you would be installing the Kubernetes components, including Kubeadm, Kubelet, and Kubectl and then you'll need to connect the master and the worker nodes. Once the connection is established you can check it by deploying application on the cluster.

### 1.4 Running Applications
- **Pods**
  - In Kubernetes, a pod is the smallest deployable unit that represents a single instance of a running process in a cluster. A pod can contain one or more containers that share the same network namespace and can access the same storage volumes.
- **ReplicaSets**
  - A ReplicaSet is a controller that ensures a specified number of replicas (identical copies) of a pod are running in a cluster at all times. ReplicaSets help to ensure high availability and scalability by automatically scaling the number of pod replicas up or down in response to changes in demand or hardware failures.
- **Deployments**
  - A Deployment is a resource object for managing Pods and ReplicaSets via a declarative configuration, which define a desired state that describes the application workload life cycle, number of pods, deployment strategies, container images, and more. The Deployment Controller works to ensure the actual state matches desired state, such as by replacing a failed pod.
- **StatefulSets**
  - It is a controller that manages the deployment and scaling of a set of stateful pods that require stable network identities and stable storage volumes. StatefulSets are used to run stateful applications such as databases, where the order and uniqueness of each pod is important.
- **Jobs**
  - a Job is a controller that manages the execution of a finite task or batch job. Jobs are used to run short-lived tasks, such as batch processing, data analysis, or backups, that run to completion and then terminate.

---

## 2. Intermediate

### 2.1 Services and Networking
- **External Access to Services**
  - External access to Kubernetes (k8s) Services allows external clients to access pods and services running in the cluster. There are multiple ways to enable external access to Services in k8s, including NodePorts, LoadBalancers, and Ingress.
- **Load Balancing**
  - Load balancing in distributes network traffic across multiple pods or nodes using a Service object. A Service provides a stable network endpoint for a set of pods, allowing other pods or external clients to access them through a single IP address and DNS name.
- **Networking & Pod-to-Pod Communication**
  - Kubernetes networking enables pods to communicate with each other across the cluster, regardless of which node they are running on. Every pod is assigned its own IP address, and Kubernetes follows a flat network model where all pods can directly communicate with each other without Network Address Translation (NAT).
- **Gateway API**
  - Understand fundamental concepts, architectures, and implementation practices of Gateway API.

### 2.2 Configuration Management
- **Injecting Pod Config with ConfigMaps**
  - ConfigMaps are a way to store configuration data that can be used by applications running in the cluster. A Config Map is a key-value store that can hold configuration data such as database URLs, credentials, API keys, or any other application configuration data that can be used by the application.
- **Using Secrets for Sensitive Data**
  - Kubernetes secrets store sensitive data such as passwords, tokens, and API keys in a secure manner. They can be created manually or automatically, and stored in etcd.

### 2.3 Resource Management
- **Setting Resource Requests and Limits**
  - Resource requests and limits in Kubernetes specify the minimum and maximum amount of CPU and memory a container requires to run. Resource requests are used for scheduling containers on nodes with sufficient resources, while limits enforce resource quotas and prevent containers from consuming too much.
- **Assigning Quotas to Namespaces**
  - Assigning quotas to namespaces is a way to limit resource usage for specific groups of resources in Kubernetes. Quotas can be set for CPU, memory, and other resources, as well as for the number of objects in a namespace.

### 2.4 Security
- **Role Based Access Control (RBAC)**
  - Role-Based Access Control (RBAC) is a method of controlling access to Kubernetes resources based on the roles assigned to users or groups. RBAC involves creating roles and binding them to users or groups to control access to Kubernetes resources.
- **Network Security**
  - Network security in Kubernetes involves securing network communication between different components within the cluster and with external networks. This can be achieved through various mechanisms such as Network Policies, Encryption, Authentication, Authorization, and Firewall rules.
- **Container and Pod Security**
  - Kubernetes (k8s) can secure containers and pods through measures like using trusted container images, limiting container privileges, enforcing pod-level security policies, implementing network security measures, using access controls with RBAC, and managing sensitive information with Secrets and ConfigMaps. These practices help organizations reduce the risk of security incidents in their k8s clusters.

### 2.5 Monitoring and Logging
- **Metrics**
  - Metrics to monitor include CPU usage, memory usage, network usage, disk usage, API server metrics, pod and container metrics, and cluster-level metrics. These metrics provide insights into the performance and health of the cluster, nodes, and applications running on the cluster.
- **Traces**
  - Tracing in Kubernetes involves monitoring the flow of requests through different components of the system, using tools such as Jaeger or Zipkin. OpenTracing and OpenCensus provide a consistent way of capturing traces across different components and applications running on the cluster.
- **Resource Health**
  - Resource health monitoring in Kubernetes involves monitoring the health and availability of resources such as pods, nodes, and containers. It helps administrators identify and troubleshoot issues that may affect the system's performance and availability using tools such as Kubernetes Dashboard, Prometheus, or Grafana.
- **Observability Engines**
  - Observability in Kubernetes (k8s) refers to the ability to gain insight into the inner workings of your cluster, applications, and services running on top of it. An observability engine in k8s is a tool or platform that facilitates the collection, analysis, and visualization of data from various sources in your k8s environment.

### 2.6 Autoscaling
- **Horizontal Pod Autoscaler (HPA)**
  - It is a feature in Kubernetes that automatically scales the number of replicas of a pod based on the current demand for the workload it is running. The HPA controller monitors the CPU utilization or other metrics of the pod and adjusts the number of replicas of the pod to meet the specified target.
- **Vertical Pod Autoscaler (VPA)**
  - Vertical Pod Autoscaler (VPA) is a Kubernetes feature that automates the process of adjusting resource limits for containers in pods. Unlike Horizontal Pod Autoscaler (HPA), which scales the number of replicas of a pod, VPA scales the resources allocated to a pod's containers.
- **Cluster Autoscaling**
  - Autoscaling in Kubernetes involves adjusting the resources allocated to a deployment or set of pods based on demand. It includes Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA), which increase or decrease replicas or adjust resource requests and limits, respectively.
- **Should you manage your own Cluster?**
  - To create your own Kubernetes cluster, you need to choose a cloud provider or set up your own infrastructure, install Kubernetes on your infrastructure, configure your cluster by setting up networking, storage, and security, deploy your applications using Kubernetes manifests, and monitor and manage your cluster using tools like Kubernetes Dashboard, kubectl, and Prometheus. This process can be complex and time-consuming, but it gives you complete control over your infrastructure and allows for customization to meet your specific needs.

---

## 3. Advanced

### 3.1 Scheduling
- **Logs**
  - Logs are generated by containerized applications running on nodes within the cluster. You can access these logs using the kubectl logs command followed by the name of the pod.
- **Basics**
  - Scheduling involves assigning pods to worker nodes based on criteria such as resource availability, labels, affinity/anti-affinity rules, taints, and tolerations. Pods are the smallest deployable units in k8s, consisting of one or more containers that share the same network namespace.
- **Taints and Tolerations**
  - Taints and tolerations are used in Kubernetes to restrict or allow pods to be scheduled on certain nodes based on labels. A taint is a label that is applied to a node to indicate certain limitations or requirements.
- **Topology Spread Constraints**
  - Topology spread constraints ensure even distribution of pods across a cluster's topology. Constraints define rules for the number of pods of a certain type that can run on a given level, such as nodes, zones, or racks.
- **Evictions**
  - Evictions terminate or delete running pods from a node due to reasons like resource constraints or pod failures. They can be initiated by the system or administrators manually through the API.

### 3.2 Storage and Volumes
- **Monitoring & Optimizing Resource Usage**
  - Monitoring and optimizing resource usage in Kubernetes helps ensure workloads run efficiently while minimizing waste and avoiding performance issues. By observing CPU, memory, and storage consumption at the node, pod, and container levels, teams can identify bottlenecks, detect underutilized resources, and make informed scaling decisions.
- **CSI Drivers**
  - CSI (Container Storage Interface) drivers in Kubernetes provide a standard way for storage providers to integrate with Kubernetes and offer persistent storage for containerized applications. They operate as separate containerized processes and communicate with Kubernetes through a well-defined API.

### 3.3 Deployment Patterns
- **Pod Priorities**
  - Pod priorities in Kubernetes determine the order in which pods are scheduled on nodes when there are competing demands for resources. Each pod is assigned a numeric priority value, with higher values indicating higher priority.
- **Stateful Applications**
  - In Kubernetes, storage is a key component for stateful applications, as these applications require persistent data storage that is available across multiple replicas of the application. Kubernetes provides several options for storage, including volumes, persistent volumes, and storage classes.
- **CI / CD Integration**
  - In CI/CD pattern, the build, test, and deployment of applications to Kubernetes are fully automated. The CI pipeline creates the container image, runs tests, and pushes it to a registry.
- **GitOps**
  - GitOps is a set of practices for managing infrastructure and applications using Git repositories as the source of truth for declarative configuration. In Kubernetes, GitOps involves using Git as the single source of truth for both the desired and actual state of the system, automating deployment and management tasks, and often using it in conjunction with Continuous Delivery (CD) practices.
- **Helm Charts**
  - Helm is a Kubernetes package manager that simplifies the deployment and management of complex applications through the use of reusable and versioned Helm charts. These charts are composed of YAML files that describe related sets of Kubernetes resources and can be customized using values files and templating with Go templates.
- **Canary Deployments**
  - Canary Deployments is a technique used in Kubernetes to gradually roll out new versions of an application by directing a small percentage of users or traffic to the new version while the majority continue using the old version. This approach allows for testing the new version under real-world conditions before fully committing to the update.
- **Creating Custom Controllers**
  - Custom controllers in Kubernetes automate the management of custom resources that are not natively supported by Kubernetes. They are implemented as Kubernetes controllers that watch custom resources and react to changes in their state.
- **Custom Schedulers and Extenders**
  - Custom Scheduler Extenders in Kubernetes enhance the scheduling capabilities of Kubernetes by allowing users to define their own scheduling logic based on custom metrics and constraints. They are implemented as custom Kubernetes controllers that run alongside the Kubernetes scheduler.
- **Blue-Green Deployments**
  - It is a deployment strategy used in Kubernetes for deploying new versions of an application by running two identical production environments, one with the current version (blue) and the other with the new version (green). After the green environment is fully tested, traffic is routed from the blue environment to the green environment, providing a seamless transition for users and avoiding any downtime or disruption.

### 3.4 Advanced Topics
- **Rolling Updates / Rollbacks**
  - Rolling updates and rollbacks are methods for updating applications without downtime. A rolling update gradually replaces old versions of an application with new ones, ensuring that some instances of the application are always available.
- **Custom Resource Definitions (CRDs)**
  - Custom Resource Definitions (CRDs) in Kubernetes extend the Kubernetes API by defining new resource types specific to an organization's needs. CRDs create custom resources that can manage a wide variety of resources, such as applications, databases, storage, and networking.
- **Kubernetes Extensions and APIs**
  - Kubernetes (k8s) extensions and APIs are used to customize the behavior of Kubernetes and add new capabilities to the system. Kubernetes extensions, including Custom Resource Definitions (CRDs), Custom Controllers, Custom Scheduler Extenders, and Custom Metrics APIs, enhance Kubernetes functionality.
- **Installing the Control Plane**
  - The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment's replicas field is unsatisfied). Control plane components can be run on any machine in the cluster.
- **Adding and Managing Worker Nodes**
  - Kubernetes runs your workload by placing containers into Pods to run on Nodes. A node may be a virtual or physical machine, depending on the cluster.
- **Multi-Cluster Management**
  - Multi-Cluster Management in Kubernetes (k8s) refers to the ability to manage multiple Kubernetes clusters using a single control plane. This approach allows administrators to centrally manage and orchestrate resources across multiple clusters, regardless of where they are located, without having to switch between multiple management consoles or tools.

---

## 4. Optional / Specialized Topics

- Jobs
- Evictions
- Helm Charts
- Canary Deployments
- Creating Custom Controllers
- Custom Schedulers and Extenders
- Blue-Green Deployments
- Adding and Managing Worker Nodes
- Multi-Cluster Management

---

## 5. References

- [Kubernetes Roadmap](https://roadmap.sh/kubernetes)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer

### Related Skills
- Docker
- Cloudflare