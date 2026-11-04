# Terraform

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/terraform
- Related Roles:
  - DevOps Engineer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is Terraform?**
  - Terraform is a powerful tool designed by HashiCorp that helps you set up, manage, and update infrastructure safely and efficiently across various cloud providers. Think of it as a way to define your cloud resources—like servers, storage, and networks—using a simple code format.
- **Usecases and Benefits**
  - Terraform is used to automate the provisioning of cloud resources, manage multi-cloud environments from a single workflow, and enforce consistent infrastructure configurations across teams. Key benefits include reproducibility, reduced human error, faster deployments, and a full audit trail of infrastructure changes through version control.
- **Installing Terraform**
  - To install Terraform, you need to download the appropriate package for your operating system from the official Terraform website. After downloading, unzip the package and move the executable to a directory included in your system's PATH.
- **CaC vs IaC**
  - Configuration as Code (CaC) refers to managing the configuration of existing systems, such as installing software or setting up services on a server. Infrastructure as Code (IaC) refers to provisioning the underlying infrastructure itself, like virtual machines, networks, and storage.
- **What is Infrastructure as Code?**
  - Infrastructure as Code (IaC) is a practice in DevOps and cloud computing that involves managing and provisioning computing infrastructure through machine-readable configuration files, rather than through physical hardware configuration or interactive configuration tools. This approach allows for version control, automation, and consistency in infrastructure deployment, making it easier to manage, scale, and replicate environments while reducing the risk of human error.

### 1.2 Hashicorp Config. Language (HCL)
- **What is HCL?**
  - HCL (HashiCorp Configuration Language) is a structured configuration language designed to be easy for people to read and write. Terraform uses HCL in .tf files to describe infrastructure through blocks, arguments, and expressions.
- **Basic Syntax**
  - The Basic Syntax of HashiCorp Configuration Language (HCL) includes defining blocks, attributes, and expressions. Blocks are fundamental units like resource, module, and provider, identified by keywords and enclosed in curly braces.

### 1.3 Providers
- **Terraform Registry**
  - The Terraform Registry is a centralized repository for discovering, sharing, and using Terraform modules and providers. It allows users to browse and download pre-built configurations, enabling quick integration of best practices.
- **Configuring Providers**
  - Configuring providers in Terraform involves specifying the required provider in the provider block within your Terraform configuration files. This block includes settings such as authentication credentials, region, and other provider-specific parameters.
- **Versions**
  - Specifying provider versions in Terraform ensures consistent and predictable behavior across different environments. Instead of using the version meta-argument within the provider block, which was deprecated and removed in Terraform 0.13, provider version constraints should now be defined in the requiredproviders block.

### 1.4 Project Initialization
- **Input Variables**
  - Terraform input variables are parameters for modules, declared using variable blocks. They support multiple data types, default values, and descriptions.

### 1.5 Resources
- **Resource Behavior**
  - When Terraform applies a configuration, it determines what actions to take for each resource based on the difference between the desired state and the current state. Resources can be created, updated in place, destroyed and recreated, or left unchanged depending on what changed in the configuration.
- **Resource Lifecycle**
  - The lifecycle meta-argument controls how Terraform manages a resource across plan and apply operations. Common settings include createbeforedestroy, which ensures a replacement resource is created before the old one is removed, preventdestroy, which blocks accidental deletion, and ignorechanges, which tells Terraform to ignore drift on specific attributes.
- **depends_on**
  - The depends\on meta-argument in Terraform is used to explicitly declare dependencies between resources, ensuring that one or more resources are created or destroyed only after the specified dependent resources have been successfully applied. This is crucial for managing resource dependencies that are not automatically detected by Terraform’s implicit dependency analysis.
- **count**
  - The count meta-argument creates multiple instances of a resource or module from a single block. It accepts a whole number, and each instance is identified by an index starting at zero.
- **Meta Arguments**
  - Meta-arguments are special arguments available on any resource block that change how Terraform handles that resource. They are not specific to a provider and are built into Terraform itself.
- **Versioning**
  - State files can be versioned using backends that support versioning, such as S3 with versioning enabled. Keeping a history of state versions allows you to roll back to a previous state if a bad apply corrupts or loses data.
- **Sensitive Data**
  - Terraform state may contain sensitive data such as passwords, private keys, and tokens returned by provider APIs. State files should be stored securely, with access restricted to authorized users and systems.

### 1.6 Outputs
- **Output Syntax**
  - An output block requires a value argument that specifies what to expose. Optional arguments include description for documentation, sensitive to redact the value, and dependson to declare explicit dependencies.
- **Sensitive Outputs**
  - Marking an output as sensitive tells Terraform to redact its value from CLI output and logs. The value is still stored in state and can be accessed programmatically.
- **Preconditions**
  - Terraform preconditions are declarative checks within resource or data blocks that validate configuration or state before Terraform attempts to create or modify resources. They use condition arguments to specify logical tests and errormessage arguments for custom failure notifications.

### 1.7 Variables
- **Type Constraints**
  - Terraform variable type constraints specify allowed data types for input variables. They include primitive types (string, number, bool), complex types (list, set, map, object), and any for unspecified types.
- **Environment Variables**
  - Environment variables can be used to customize various aspects of Terraform. You can set these variables to change the default behaviour of terraform such as increase verbosity, update log file path, set workspace, etc.
- **Variable Definition File**
  - A Terraform variables.tf file centralizes input variable declarations for a module or configuration. It typically contains multiple variable blocks, each defining a single input variable with its name, type constraint, optional default value, and description.
- **Validation Rules**
  - Validation rules can be used to specify custom validations to a variable. The motive of adding validation rules is to make the variable comply with the rules.
- **Local Values**
  - Local values can be understood as a name assigned to any expression to use it multiple times directly by the name in your terraform module. Local values are referred to as locals and can be declared using the locals block.
- **Splitting State Files**
  - Large Terraform configurations can be split into multiple state files by organizing resources into separate workspaces or root modules. This reduces the blast radius of plan and apply operations, speeds up plans, and makes it easier for teams to work independently on different parts of the infrastructure.

---

## 2. Intermediate

### 2.1 Format & Validate
- **terraform fmt**
  - terraform fmt rewrites Terraform configuration files to the canonical format and style defined by HashiCorp. It adjusts indentation, alignment, and spacing.
- **terraform validate**
  - The validate command helps you make sure your Terraform code is syntactically correct before you deploy. This helps you to prevent misconfiguration due to missing attributes or incorrect dependencies, saving time, improving efficiency, and reducing cost.
- **TFLint**
  - TFLint is a Terraform linter that goes beyond the checks provided by terraform validate. It detects errors specific to provider APIs, such as invalid instance types or unsupported regions, and can enforce custom coding rules through plugins.

### 2.2 State
- **Remote State**
  - Remote state stores the Terraform state file in a shared, remote backend such as S3, Azure Blob Storage, or Terraform Cloud. This allows multiple team members to work with the same state and prevents conflicts from concurrent operations.
- **State Locking**
  - State locking prevents two Terraform operations from modifying state at the same time. When supported by the backend, Terraform acquires a lock before writing to state and releases it when the operation completes.
- **Import Existing Resources**
  - terraform import brings existing infrastructure resources under Terraform management by adding them to the state file. After importing, the configuration must be written manually to match the imported resource.

### 2.3 Best Practices for State
- **for_each**
  - The foreach meta-argument creates one instance of a resource or module for each item in a map or set of strings. Each instance is keyed by the map key or set value, making it easier to manage and reference individual items than with count.
- **provider**
  - The provider meta-argument assigns a specific provider configuration to a resource when multiple configurations of the same provider exist. This is common when managing resources across multiple regions or accounts within the same Terraform workspace.
- **lifecycle**
  - The lifecycle block inside a resource configures how Terraform handles creation, updates, and deletion of that resource. It supports arguments like createbeforedestroy, preventdestroy, ignorechanges, and replacetriggeredby.

### 2.4 Inspect / Modify State
- **graph**
  - terraform graph outputs a visual representation of the dependency graph for the current configuration or plan. The output is in DOT format, which can be rendered with tools like Graphviz.
- **list**
  - terraform state list prints the addresses of all resources tracked in the current state. It is a quick way to see what Terraform is managing and to find the exact resource address needed for other state subcommands.
- **output**
  - terraform output displays the values of outputs defined in the configuration. Without arguments it shows all outputs; a specific output name can be passed to retrieve a single value.
- **-replace option in apply**
  - The -replace flag on terraform apply forces Terraform to destroy and recreate a specific resource even if no configuration changes would normally trigger replacement. It is used to resolve issues with a corrupted or degraded resource that needs to be rebuilt.
- **show**
  - terraform show displays a human-readable representation of the current state or a saved plan file. It is useful for reviewing what Terraform currently knows about managed resources without running a full plan.
- **rm**
  - terraform state rm removes one or more resources from the state file without destroying the actual infrastructure. This is used when you want Terraform to stop managing a resource, for example before importing it into a different workspace or before deleting it manually.
- **state pull / push**
  - terraform state pull downloads the current remote state and prints it to stdout. terraform state push uploads a local state file to the configured backend, overwriting the remote state.

### 2.5 Deployment
- **terraform plan**
  - terraform plan computes the difference between the current state and the desired configuration and displays the actions Terraform would take. It does not make any changes to infrastructure.
- **terraform apply**
  - terraform apply is the command used to implement the changes defined in your Terraform configuration files. It creates, updates, or deletes the specified infrastructure resources to match the desired state.

### 2.6 Clean Up
- **terraform destroy**
  - terraform destroy removes all resources managed by the current configuration. It is the equivalent of running terraform apply with every resource marked for deletion.

### 2.7 Modules
- **mv**
  - terraform state mv moves a resource address from one location to another within the state file. It is used when refactoring configurations, such as renaming a resource or moving it into a module, without triggering a destroy and recreate cycle.
- **Root vs Child Modules**
  - The root module is the working directory where Terraform is invoked. Child modules are called from the root module or from other modules using a module block.
- **Published Modules Usage**
  - Published modules are pre-built, versioned modules available on the Terraform Registry. They can be referenced directly in a module block using a registry source address and version constraint.
- **Creating Local Modules**
  - Local modules are directories containing Terraform configuration files that are referenced using a relative file path in a module block. They allow you to break a large configuration into smaller, self-contained units.
- **state replace-provider**
  - terraform state replace-provider updates all resource entries in the state that reference one provider to reference a different provider. This is used when migrating resources to a forked or renamed provider without destroying and recreating them.
- **state force-unlock**
  - terraform state force-unlock manually releases a state lock that was not properly released after an interrupted operation. It requires the lock ID, which is displayed in the error message shown when a lock conflict is detected.

### 2.8 Provisioners
- **When to Use?**
  - Provisioners are appropriate when no provider resource or data source can accomplish the required task and the action must happen at resource creation or destruction time. Common use cases include running initialization scripts on a new server or notifying an external system after a resource is created.
- **Creation / Destroy Time**
  - Provisioners run either at creation time, after the resource is created, or at destroy time, before the resource is deleted. Creation-time provisioners bootstrap resources, while destroy-time provisioners handle cleanup tasks.
- **file provisioner**
  - The file provisioner copies files or directories from the machine running Terraform to a newly created remote resource. It requires a connection block specifying how to reach the remote machine, typically over SSH or WinRM.
- **local-exec provisioner**
  - The local-exec provisioner runs a command on the machine executing Terraform, not on the remote resource. It is used for tasks like triggering an external API, running a local script, or writing data to a file.
- **remote-exec provisioner**
  - The remote-exec provisioner runs commands on the remote resource after it is created. It connects over SSH or WinRM and executes a list of inline commands or a script file.
- **Custom Provisioners**
  - Custom provisioners can be implemented using external programs that follow the Terraform provisioner plugin protocol. They allow teams to integrate specialized tooling into the Terraform lifecycle without relying on the built-in provisioner types.

### 2.9 Data Sources
- **Inputs / Outputs**
  - Modules accept input values through declared variables and expose results through declared outputs. The calling module passes values for each required variable and can reference the module's outputs using the module.<name>.<output> syntax.
- **Modules Best Practices**
  - Modules should be focused on a single concern and avoid hardcoding values that callers need to control. Always declare types for input variables and provide descriptions.

---

## 3. Advanced

### 3.1 Template Files
- **Template Files**
  - Template files use the templatefile function to render a file with variable substitutions at plan time. The function takes a file path and a map of values and returns the rendered string.

### 3.2 Workspaces
- **Workspaces**
  - Workspaces allow multiple state files to exist for the same configuration, enabling the same code to manage separate environments such as development, staging, and production. The terraform workspace commands create, switch, and list workspaces.

### 3.3 CI / CD Integration
- **GitHub Actions**
  - GitHub Actions can run Terraform commands as part of a workflow triggered by pull requests or pushes. Workflows are defined in YAML files and can use community actions from the GitHub Marketplace or call the Terraform CLI directly.
- **Circle CI**
  - CircleCI can execute Terraform pipelines using orbs or custom job configurations. Jobs are defined in a .circleci/config.yml file and run in containers with the Terraform binary installed.
- **GitLab CI**
  - GitLab CI runs Terraform pipelines using .gitlab-ci.yml configuration files. GitLab provides a native Terraform integration with merge request widgets that display plan output directly in the code review interface.
- **Jenkins**
  - Jenkins can orchestrate Terraform workflows using Pipeline scripts written in Groovy. The Terraform binary is installed on agents or provided via a tool configuration.

### 3.4 Testing
- **Unit Testing**
  - Unit tests for Terraform validate individual modules in isolation, checking that inputs produce the expected plan output without provisioning real resources. The native terraform test command introduced in Terraform 1.6 supports this by running configurations in a controlled context.
- **Contract Testing**
  - Contract testing verifies that the inputs and outputs of a module conform to a defined interface. It ensures that a module behaves predictably when called with specific values and that its outputs meet the expectations of callers.
- **Integration Testing**
  - Integration tests provision real infrastructure and verify that resources are created correctly and work together as expected. They are slower and more expensive than unit tests but catch issues that static analysis cannot detect.
- **End to End Testing**
  - End-to-end tests validate an entire infrastructure stack by provisioning it, running checks against live endpoints or resources, and then tearing it down. These tests are the most comprehensive but also the slowest and most costly.
- **Testing Modules**
  - Testing modules involves validating their logic, variable handling, and output values in isolation before they are used in a larger configuration. The terraform test command can apply a module with test-specific variable values and assert expected output values.

### 3.5 Scaling Terraform
- **Splitting Large State**
  - Large state files slow down plans and increase the risk of conflicts. Splitting infrastructure into smaller, independently managed configurations with their own state files reduces plan times and limits the impact of a failed apply.
- **Parallelism**
  - Terraform applies resource changes in parallel by default, up to a configurable limit controlled by the -parallelism flag. Increasing parallelism can speed up large deployments but may hit API rate limits.
- **Deployment Workflow**
  - A consistent deployment workflow defines how infrastructure changes move from development to production. Common patterns include environment promotion, where changes are applied to lower environments first, and GitOps, where the desired state is tracked in a Git repository and applied automatically.
- **Terragrunt**
  - Terragrunt is a thin wrapper around Terraform that adds support for keeping configurations DRY, managing dependencies between modules, and running commands across multiple modules at once. It uses terragrunt.hcl files to define module sources, variable inputs, and backend configuration.
- **Infracost**
  - Infracost is a cost estimation tool that integrates with Terraform to show the monthly cloud cost impact of planned infrastructure changes. It parses a Terraform plan and calculates costs based on provider pricing data.
- **Version Management**
  - Managing Terraform and provider versions across a team requires consistent tooling. tfenv is a popular version manager for Terraform that allows switching between installed versions based on a .terraform-version file.

### 3.6 Security
- **Secret Management**
  - Secrets such as API keys, passwords, and certificates should never be stored in Terraform configuration files or committed to version control. Common approaches include injecting secrets via environment variables, using a secrets manager like HashiCorp Vault or AWS Secrets Manager as a data source, or using a backend that encrypts sensitive state values.
- **Compliance / Sentinel**
  - Sentinel is a policy as code framework built into Terraform Cloud and Enterprise. It allows teams to define rules that restrict what infrastructure can be provisioned, enforce tagging standards, or require cost approval before applying.
- **Terrascan**
  - Terrascan is an open-source static analysis tool that scans Terraform configurations for security and compliance violations before deployment. It checks against a library of built-in policies covering common cloud security standards and supports custom rules.
- **Checkov**
  - Checkov is a static analysis tool for infrastructure as code that scans Terraform, CloudFormation, Kubernetes, and other formats for security and compliance issues. It includes hundreds of built-in checks covering major cloud providers and supports custom policies written in Python or YAML.

### 3.7 HCP
- **Trivy**
  - Trivy is a security scanner that can analyze Terraform configurations for misconfigurations in addition to scanning container images and filesystems. It checks infrastructure code against a set of built-in rules and reports issues by severity.
- **KICS**
  - KICS (Keeping Infrastructure as Code Secure) is an open-source tool from Checkmarx that scans IaC files including Terraform for security vulnerabilities, compliance issues, and misconfigurations. It covers a broad set of cloud platforms and IaC formats and supports custom queries written in the Open Policy Agent Rego language.
- **What and when to use HCP?**
  - HCP Terraform is appropriate when a team wants the benefits of Terraform Cloud, such as remote runs, state management, and policy enforcement, without managing infrastructure for it. It suits teams that are scaling beyond local Terraform workflows and need collaboration features, audit logs, and a managed backend.
- **Enterprise Features**
  - HCP Terraform Enterprise features include audit logging, single sign-on, self-hosted deployment options, Sentinel policy enforcement, team and organization management, and private module registries. These features are aimed at large organizations that need governance controls and compliance capabilities beyond what the free tier provides.
- **Authentication**
  - HCP Terraform authenticates users and services through API tokens. User tokens are generated in the account settings and used for CLI access.
- **Workspaces**
  - HCP Terraform workspaces are managed environments that store state, run history, and variable values for a specific configuration. Each workspace is linked to a version control repository or configured for CLI-driven runs.
- **VCS Integration**
  - HCP Terraform integrates with version control systems including GitHub, GitLab, Bitbucket, and Azure DevOps. Linking a workspace to a VCS repository triggers speculative plans on pull requests and applies on merges to the configured branch.
- **Run Tasks**
  - Run Tasks are integrations that execute external services at specific points in the Terraform run lifecycle, such as after a plan or before an apply. They can be used to trigger security scans, cost checks, or custom validation logic.

---

## 4. Optional / Specialized Topics

- What is Infrastructure as Code?
- Meta Arguments
- Versioning
- Sensitive Data
- Local Values
- Splitting State Files
- show
- rm
- state pull / push
- state replace-provider
- state force-unlock
- remote-exec provisioner
- Custom Provisioners
- Testing Modules
- Infracost
- Version Management
- Authentication
- Workspaces
- VCS Integration
- Run Tasks

---

## 5. References

- [Terraform Roadmap](https://roadmap.sh/terraform)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer

### Related Skills
- AWS
- Git & GitHub
- Cloudflare