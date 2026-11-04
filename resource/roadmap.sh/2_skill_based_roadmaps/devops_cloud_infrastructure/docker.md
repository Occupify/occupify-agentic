# Docker

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/docker
- Related Roles:
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What are Containers?**
  - Containers are lightweight, portable, and isolated software environments that package applications with their dependencies for consistent execution across different platforms. They streamline development, deployment, and management while ensuring applications run reliably regardless of underlying infrastructure.
- **Why do we need Containers?**
  - Containers solve environment inconsistency issues when working in teams by standardizing runtime environments. Before containers, significant time was lost configuring local environments to run projects shared by teammates, leading to "works on my machine" problems.
- **Bare Metal vs VMs vs Containers**
  - Bare metal runs applications directly on hardware with maximum performance but limited flexibility. VMs use hypervisors to run multiple OS instances with strong isolation but higher overhead.
- **Docker and OCI**
  - The Open Container Initiative (OCI) is a Linux Foundation project which aims at creating industry standards for container formats and runtimes. Its primary goal is to ensure the compatibility and interoperability of container environments through defined technical specifications.
- **Package Managers**
  - Package managers are tools used to install, update, and manage software packages on Linux systems. Since most Docker images are based on Linux distributions, understanding package managers like apt (Debian/Ubuntu), yum/dnf (RHEL/CentOS/Fedora), and apk (Alpine Linux) is essential for building Docker images.

### 1.2 Underlying Technologies
- **Users / Groups Permissions**
  - Linux users, groups, and file permissions control access to files and resources on the system. In Docker, understanding these concepts is important because containers run processes as specific users, and the permissions model determines what files a containerized application can read, write, or execute.
- **Shell Commands**
  - Shell commands are the fundamental way to interact with Linux-based systems that Docker containers typically run on. Understanding commands like ls, cd, cp, mv, rm, chmod, chown, ps, top, grep, find, and cat is essential for working inside containers, writing Dockerfiles, and debugging running containers.
- **Shell Scripting**
  - Shell scripting involves writing scripts using shell languages like Bash to automate tasks and workflows. In the context of Docker, shell scripts are commonly used in Dockerfiles as part of RUN instructions to set up the container environment, install packages, or configure applications.
- **Namespaces**
  - Docker namespaces are a Linux kernel feature that creates isolated environments for containers by providing separate instances of global system resources. Docker uses PID, NET, MNT, UTS, IPC, and USER namespaces to ensure each container believes it has its own unique resources, enabling lightweight, portable, and secure containerization.
- **cgroups**
  - cgroups (control groups) are Linux kernel features that limit and manage system resources like CPU, memory, and I/O for process groups. Docker uses cgroups to enforce resource constraints on containers, ensuring predictable performance and preventing containers from consuming excessive system resources.
- **Union Filesystems**
  - Union filesystems (UnionFS) create virtual, layered file structures by overlaying multiple directories without modifying originals. Docker uses this to manage storage efficiently by minimizing duplication and reducing image sizes through layered filesystem approach that keeps directory contents separate while mounted together.

### 1.3 Installation / Setup
- **Docker Desktop (Win/Mac/Linux)**
  - Docker Desktop is a comprehensive development environment for Windows, macOS, and Linux with a GUI. It includes Docker Engine, CLI, Buildx, Extensions, Compose, Kubernetes, and credentials helper, providing everything needed for container development on desktop platforms.
- **Docker Engine ( Linux )**
  - Docker Engine is the core open-source containerization runtime that creates and manages containers, builds images, and provides the Docker API. It runs on Linux, Windows, and macOS, serving as the foundation for Docker Desktop and standalone Docker installations on servers.

### 1.4 Basics of Docker
- **Basics of Docker**
  - Docker is a platform that simplifies building, packaging, and deploying applications in lightweight, portable containers. Key components include Dockerfiles (build instructions), Images (snapshots), and Containers (running instances).

---

## 2. Intermediate

### 2.1 Data Persistence
- **Ephemeral Container Filesystem**
  - By default, the storage within a Docker container is ephemeral, meaning that any data changes or modifications made inside a container will only persist until the container is stopped and removed. Once the container is stopped and removed, all the associated data will be lost.
- **Volume Mounts**
  - Volume mounts are a way to map a folder or file on the host system to a folder or file inside a container. This allows the data to persist outside the container even when the container is removed.

### 2.2 Using 3rd Party Container Images
- **Programming Languages**
  - Having proficiency in at least one programming language is essential before working with Docker, as containers are ultimately used to package and run applications. Whether you work with Python, JavaScript, Go, Java, or any other language, understanding how your application is built, its dependencies, and its runtime requirements directly informs how you write Dockerfiles and structure container images.
- **Application Architecture**
  - Application architecture in containerized environments focuses on designing applications to leverage containerization benefits. This includes microservices patterns, service decomposition, inter-service communication, data persistence strategies, and designing for scalability and fault tolerance in distributed systems.
- **Databases**
  - Running your database in a Docker container can help streamline your development process and ease deployment. Docker Hub provides numerous pre-made images for popular databases such as MySQL, PostgreSQL, and MongoDB.
- **Command Line Utilities**
  - Docker images can include command line utilities or standalone applications that we can run inside containers.

### 2.3 Container Registries
- **Dockerhub**
  - Docker Hub is a cloud-based registry service that serves as the primary public repository for Docker container images. It allows users to store, share, and distribute Docker images, offering both free public repositories and paid private ones and integrates seamlessly with Docker CLI, enabling easy pushing and pulling of images.
- **Runtime Configuration Options**
  - Docker runtime configuration options give you powerful control over your containers' environments. By tweaking resource limits, network settings, security profiles, and logging drivers, you can optimize performance and enhance security.

### 2.4 Running Containers
- **Bind Mounts**
  - Bind mounts have limited functionality compared to volumes. When you use a bind mount, a file or directory on the host machine is mounted into a container.
- **docker run**
  - The docker run command creates and starts a new container from a specified image. It combines docker create and docker start operations, offering a range of options to customize the container's runtime environment.
- **docker compose**
  - Docker Compose is a tool for defining and running multi-container applications using a YAML file (docker-compose.yml). It describes application services, networks, and volumes, enabling you to create, manage, and run entire containerized applications with single commands for simplified orchestration.

### 2.5 Building Container Images
- **Dockerfiles**
  - A Dockerfile is a text document that contains a list of instructions used by the Docker engine to build an image. Each instruction in the Dockerfile adds a new layer to the image.
- **Efficient Layer Caching**
  - When building container images, Docker caches the newly created layers. These layers can then be used later on when building other images, reducing the build time and minimizing bandwidth usage.
- **Image Size and Security**
  - Reducing Docker image size is crucial for optimizing storage, transfer speeds, and deployment times. Key strategies include using minimal base images like Alpine Linux, leveraging multi-stage builds to exclude unnecessary build tools, removing unnecessary files and packages, and minimizing the number of layers by combining commands.

### 2.6 Container Security
- **Runtime Security**
  - Runtime security in Docker focuses on ensuring the safety and integrity of containers during their execution, safeguarding against vulnerabilities and malicious activities that could arise while the containerized application is running. This involves monitoring container behavior for anomalies, implementing access controls to limit permissions, and employing tools to detect and respond to suspicious activity in real time.
- **Image Security**
  - Image security is a crucial aspect of deploying Docker containers in your environment. Ensuring the images you use are secure, up to date, and free of vulnerabilities is essential.
- **Nomad**
  - Nomad is a cluster manager and scheduler that enables you to deploy, manage and scale your containerized applications. It automatically handles node failures, resource allocation, and container orchestration.
- **Docker Swarm**
  - Docker Swarm is Docker’s native container orchestration tool that allows users to deploy, manage, and scale containers across a cluster of Docker hosts. By transforming a group of Docker nodes into a single, unified cluster, Swarm provides high availability, load balancing, and automated container scheduling using simple declarative commands.

---

## 3. Advanced

### 3.1 Docker CLI
- **Image Tagging Best Practices**
  - Docker image tagging best practices center on creating clear, consistent, and informative labels. Adopt semantic versioning for releases, avoid the ambiguous "latest" tag in production, and include relevant metadata like build dates or Git commit hashes.
- **Others (ghcr, ecr, gcr, acr, etc)**
  - Container images can be stored in many different registries, not just Dockerhub. Most major cloud platforms now provide container registries such as "Artifact Registry" on Google Cloud Platform, Elastic Container Registry on AWS and Azure Container Registry on Microsoft Azure.
- **Images**
  - Docker images are lightweight, standalone packages containing everything needed to run software: application code, runtime, libraries, and system tools. Built in layers for efficient storage, they serve as blueprints for containers and can be shared through registries like Docker Hub for consistent deployment across environments.
- **Containers**
  - Containers are isolated, lightweight environments that run applications using a shared operating system kernel, ensuring consistency and portability across different computing environments. They encapsulate everything needed to run an application, such as code, dependencies, and configurations, making it easy to move and run the containerized application anywhere.
- **Volumes**
  - Docker volumes are persistent storage solutions used to manage and store data outside the container's filesystem, ensuring data remains intact even if the container is deleted or recreated. They are ideal for storing application data, logs, and configuration files that need to persist across container restarts and updates.
- **Networks**
  - Docker networks enable containers to communicate with each other and with external systems, providing the necessary connectivity for microservices architectures. By default, Docker offers several network types such as bridge, host, and overlay, each suited for different use cases like isolated environments, high-performance scenarios, or multi-host communication.

### 3.2 Networking
- **Networking**
  - Understand fundamental concepts, architectures, and implementation practices of Networking.

### 3.3 Developer Experience
- **Hot Reloading**
  - Even though we can speed up the image building with layer caching enable, we don't want to have to rebuild our container image with every code change. Instead, we want the state of our application in the container to reflect changes immediately.
- **Debuggers**
  - In order to make developing with containers competitive with developing locally, we need the ability to run and attach to debuggers inside the container.
- **Tests**
  - We want to run tests in an environment as similar as possible to production, so it only makes sense to do so inside of our containers! This can include unit tests, integration tests, and end-to-end tests, all run within Docker containers to simulate real-world scenarios while avoiding interference from external dependencies.
- **Continuous Integration**
  - Continuous integration is the idea of executing some actions (for example build, test, etc...) automatically as you push code to your version control system.

### 3.4 Deploying Containers
- **PaaS Options**
  - Platform-as-a-Service (PaaS) options for deploying containers provide a simplified and managed environment where developers can build, deploy, and scale containerized applications without worrying about the underlying infrastructure. Popular PaaS offerings include Google Cloud Run, Azure App Service, AWS Elastic Beanstalk, and Heroku, which abstract away container orchestration complexities while offering automated scaling, easy integration with CI/CD pipelines, and monitoring capabilities.
- **Kubernetes**
  - Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications. It provides a robust framework for handling complex container workloads by organizing containers into logical units called pods, managing service discovery, load balancing, and scaling through declarative configurations.

---

## 4. Optional / Specialized Topics

- Package Managers
- cgroups
- Union Filesystems
- Volumes
- Networks

---

## 5. References

- [Docker Roadmap](https://roadmap.sh/docker)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer

### Related Skills
- Kubernetes
- Linux
- AWS