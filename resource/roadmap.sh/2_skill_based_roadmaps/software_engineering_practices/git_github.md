# Git & GitHub

## Metadata
- Type: Skill
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/git-github
- Related Roles:
  - Frontend Developer
  - Backend Developer
  - DevOps Engineer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Learn the Basics
- **What is Version Control?**
  - Version control is a system that tracks changes to files over time, so developers can see who changed what and revert to earlier versions when needed. It keeps a history of every modification, letting multiple people work on the same project without overwriting each other's work.
- **Why use Version Control?**
  - Version control lets developers track every change made to a codebase and roll back to a previous state if something breaks. It removes the need for manual backups like renamed folders or zipped copies of a project.
- **Git vs Other VCS**
  - Git is a distributed version control system, meaning every developer has a full copy of the project history on their own machine, not just the latest snapshot. Older systems like Subversion (SVN) or CVS are centralized, so they depend on a single server for most operations and require a network connection to commit changes.
- **Installing Git Locally**
  - Installing Git locally means setting up the Git command-line tool on a personal machine so it can track and manage code changes. The installation process differs by operating system: Windows users typically download an installer from the official Git website, macOS users can install it through Homebrew or Xcode command line tools, and Linux users install it through their package manager.
- **git init**
  - The git init command creates a new Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.
- **git config**
  - git config sets configuration values that control how Git behaves, such as the user's name, email, and default editor. These settings can apply at different levels: system-wide, per user, or per repository.
- **Local vs Global Config**
  - Git configuration can be set at the local level, which applies only to the current repository, or at the global level, which applies to every repository for that user. Local settings are stored inside a repository's .git/config file and override global ones when both exist.

### 1.2 What is a Repository
- **Working Directory**
  - The working directory is the actual folder on disk where a developer edits files. It reflects the current state of the project, including any changes that have not yet been staged or committed.
- **Staging Area**
  - The staging area, also called the index, is where changes are prepared before being committed. Running git add moves specific changes from the working directory into the staging area, letting developers choose exactly what to include in the next commit.
- **Committing Changes**
  - Committing saves a snapshot of the staged changes to the repository's history, along with a message describing what was changed and why. Each commit gets a unique hash that identifies it and allows Git to track the exact state of the project at that point.
- **Managing Remotes**
  - Managing remotes involves adding, renaming, or removing the remote repositories a local project is connected to. The command git remote add <name> <url> links a new remote, git remote rename changes its label, and git remote remove deletes the connection entirely.
- **Cloning Repositories**
  - Cloning a repository in Git and GitHub involves creating a local copy of a remote repository on your computer. This allows you to work on the project locally, commit changes, and later push those changes back to the remote repository.

### 1.3 Branching Basics
- **Creating Branch**
  - Creating a branch in Git is a fundamental part of working with version control, allowing you to work on different features or fixes without affecting the main codebase. You can create branches either through the terminal or github interface
- **Renaming Branch**
  - Renaming a branch in Git means changing the name of a branch to something different while preserving its history and the commits it contains. The branch itself remains the same in terms of the code and history it tracks, but the reference (the name by which you refer to it) is updated

### 1.4 GitHub Essentials
- **Deleting Branch**
  - Deleting a Git branch means removing a line of development from your Git repository. A branch in Git is essentially a pointer to a specific commit, representing an independent line of development.
- **Checkout Branch**
  - In Git, to "checkout" from a branch means to switch your working directory to that branch, making it the active branch. This updates your files to match the state of that branch and allows you to work on it.
- **Merging Basics**
  - A merge in Git is the process of combining changes from one branch into another. When you want to integrate updates from one branch (the source) into another branch (the target), you need to perform a merge.
- **Creating Account**
  - To get started with GitHub, you'll need to create a free personal account on GitHub.com and verify your email address. Every person who uses GitHub.com signs in to a personal account.
- **GitHub Interface**
  - The GitHub interface is the web-based dashboard used to navigate repositories, pull requests, issues, and account settings. It includes a repository view showing files and commit history, a notifications tab, and organization or team pages for shared projects.
- **Profile Readme**
  - A profile README is a special repository named after a GitHub username that displays custom content directly on the user's profile page. It uses standard Markdown, so developers can add text, images, badges, and links to showcase skills, projects, or contact information.
- **Private vs Public**
  - A public repository is visible to anyone on GitHub and can be cloned or viewed by other users, while a private repository restricts access to the owner and any collaborators explicitly invited. Public repositories are common for open source projects that want community contributions, while private repositories suit proprietary code or work in progress.

### 1.5 Git Remotes
- **.gitignore**
  - Ignored files are tracked in a special file named .gitignore that is checked in at the root of your repository. There is no explicit git ignore command: instead the .gitignore file must be edited and committed by hand when you have new files that you wish to ignore.
- **Viewing Commit History**
  - Viewing commit history shows the sequence of commits made to a repository, typically through the git log command. Each entry includes the commit hash, author, date, and message, giving a record of how the project evolved.
- **Pushing / Pulling Changes**
  - When you pull changes in Git, you're fetching and integrating changes from a remote repository into your local repository. This operation updates your local branch with the latest changes from the remote branch.
- **Fetch without Merge**
  - git fetch downloads new commits, branches, and tags from a remote repository without merging them into the local branch. It updates the remote-tracking branches, like origin/main, so the developer can inspect incoming changes before deciding to merge or rebase them.

### 1.6 Merge Strategies
- **Setting up Profile**
  - Setting up a GitHub profile involves adding a profile picture, bio, location, and links to personal or professional sites. A well-configured profile helps other developers and potential employers understand who is behind the code.
- **Creating Repositories**
  - Creating a Git repository means setting up a system to track changes in your project's files over time. This is crucial for version control, allowing you to manage, review, and collaborate on code efficiently.
- **Forking vs Cloning**
  - Forking creates a personal copy of someone else's repository under the user's own GitHub account, allowing changes without affecting the original project. Cloning downloads a copy of a repository, whether it's the original or a fork, to a local machine for editing.
- **Fast-Forward vs Non-FF**
  - A fast-forward merge happens when the target branch has no new commits since the feature branch was created, so Git simply moves the branch pointer forward without creating a new commit. A non-fast-forward merge occurs when both branches have diverged, requiring Git to create a dedicated merge commit that ties the two histories together.
- **Handling Conflicts**
  - When multiple developers work on the same project simultaneously, conflicts can arise during the merging process. This occurs when changes made by different individuals overlap or contradict each other in a specific code file.
- **Rebase**
  - Rebasing in Git is a powerful and potentially complex feature used to reorganize or modify a series of commits. The primary purpose of rebasing is to create a cleaner, more linear project history by moving or combining changes from one branch into another.
- **Squash**
  - Squashing in Git, refers to the process of combining multiple commits into a single commit. This is often done to create a cleaner and more concise commit history, especially before merging a feature branch into the main branch.
- **Cherry Picking Commits**
  - Cherry-picking in Git allows you to apply a specific commit from one branch to another, without merging the entire branch. This is useful when you want to bring in a specific feature or fix from one branch to another without incorporating all the changes from the source branch.
- **Commit Messages**
  - A Git commit message is a brief explanation of the changes introduced in a particular commit. It helps others (and your future self) understand the purpose of the changes and the context behind them.

### 1.7 Collaboration on GitHub
- **Issues**
  - Issues are used to track bugs, feature requests, or tasks related to a repository. Each issue has a title, description, and optional labels, assignees, and milestones, and it can be commented on to discuss the problem or proposed solution.
- **Pull Requests**
  - A pull request is a proposal to merge a set of changes from one branch into another. In a pull request, collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase.
- **PR from a Fork**
  - A pull request from a fork lets a contributor propose changes to a repository they don't have write access to. The contributor forks the repository, makes changes on their own copy, and opens a pull request comparing their fork's branch against the original repository.
- **Collaborators**
  - Collaborators in GitHub are users who have been granted direct access to a repository by the repository owner or organization administrators. Collaborators can perform actions like pushing commits, creating branches, and managing issues or pull requests, depending on the permissions granted to them.
- **Labelling Issues / PRs**
  - Labels are colored tags applied to issues and pull requests to categorize them by type, priority, or status. Common examples include "bug," "enhancement," or "help wanted," and repositories can define custom labels to match their workflow.
- **Saved Replies**
  - Saved replies let users store commonly used comment templates that can be inserted into issues or pull requests with a click. This is useful for repetitive responses, like closing an issue with a standard message or thanking a contributor for their submission.
- **Mentions**
  - Mentions on GitHub allow you to notify specific users or teams about comments, issues, pull requests, or other activities. This feature improves collaboration by encouraging participation and discussion among team members, increasing visibility of important topics, and streamlining communication within your repository.
- **Reactions**
  - Reactions in GitHub are a way for users to express their feelings or opinions about issues, pull requests, comments, and other discussions without adding additional comments. They are similar to "likes" or "emojis" on social media platforms, providing a quick and non-verbal way to engage with content.

### 1.8 Documentation
- **Branch Naming**
  - Branch naming conventions give structure to how branches are labeled, often including a prefix like feature/, bugfix/, or hotfix/ followed by a short description. Consistent naming makes it easy to identify a branch's purpose at a glance and helps automate workflows that trigger based on branch name patterns.
- **PR Guidelines**
  - Pull request guidelines are the conventions a project sets for how contributions should be submitted, often documented in a CONTRIBUTING.md file. They typically cover expectations like keeping pull requests focused on a single change, writing a clear description, and linking related issues.
- **Code Reviews**
  - A code review is the process of examining proposed changes in a pull request before they get merged, checking for bugs, style issues, or design concerns. Reviewers can leave comments on specific lines, approve the changes, or request modifications before approval.
- **Markdown**
  - Markdown is a lightweight markup language used to format text with plain, readable syntax, like using asterisks for bold or a hash symbol for headings. GitHub renders Markdown automatically in README files, issues, pull requests, and comments, converting the plain text syntax into styled output.
- **Project Readme**
  - A README is the first file most people see when visiting a repository, typically explaining what the project does, how to install it, and how to use it. It's written in Markdown and rendered automatically on the repository's main page.
- **GitHub Wikis**
  - A GitHub wiki is a separate space attached to a repository for writing longer-form documentation, tutorials, or notes that don't belong in the main README. Wikis support Markdown and have their own version history, similar to the main repository.
- **CITATION files**
  - You can add a CITATION.cff file to the root of a repository to let others know how you would like them to cite your work. The citation file format is plain text with human- and machine-readable citation information.

### 1.9 Git Stash Basics
- **GitHub Discussions**
  - GitHub Discussions is a forum-style feature for conversations that don't fit the structure of an issue, such as general questions, ideas, or announcements. Unlike issues, discussions aren't meant to track specific tasks and can be organized into categories like Q&A or ideas.

### 1.10 GitHub Projects
- **Contribution Guidelines**
  - Contribution guidelines are essential for collaborative projects on GitHub as they help streamline collaboration, set expectations for contributions, and maintain the project's quality and consistency.
- **Clean Git History**
  - A clean Git history means commits are logically organized, well described, and free of unnecessary noise like "fix typo" or "WIP" messages. Techniques like squashing commits, rebasing, and writing clear commit messages all contribute to keeping history readable.
- **Project Planning**
  - Project planning in GitHub Projects involves setting up boards, defining custom fields, and organizing tasks into a workflow that reflects how a team operates. This can include setting milestones, prioritizing issues, and assigning work to specific people or iterations.
- **Kanban Boards**
  - A Kanban board is a visual layout that organizes tasks into columns representing different stages, such as "To Do," "In Progress," and "Done." Items move across columns as their status changes, giving a clear picture of the team's workflow at a glance. GitHub Projects supports this board view natively, letting issues and pull requests be dragged between columns.

---

## 2. Intermediate

### 2.1 Working in a Team
- **GitHub Organizations**
  - A GitHub organization is a shared account used by companies or groups to manage multiple repositories, members, and teams under one umbrella. It allows centralized billing, permission management, and visibility settings across all repositories owned by the organization.
- **Collaborators / Members**
  - In GitHub, collaborators and members refer to individuals who contribute to or have access to your repository. Collaborators are users who have been granted permission to contribute code, make changes, and push updates to your repository, whereas members are the owners of a repository, including organization owners who have full control over their team's repositories.
- **Teams within Organization**
  - Teams within a GitHub organization group members together to manage permissions more efficiently across multiple repositories. Instead of granting access to each person individually, an admin assigns access to a team, and every member inherits those permissions.

### 2.2 History
- **Linear vs Non-Linear**
  - A linear history means commits follow a single, straight sequence with no branching or merging, often achieved through rebasing instead of merging. A non-linear history includes branches that diverge and later merge back together, creating a more complex graph of commits.
- **HEAD**
  - The HEAD file is at the core of how Git knows the SHA-1 of the last commit when running commands like git branch <branch>. It serves as a symbolic reference, pointing to the current branch.
- **Detached HEAD**
  - A detached HEAD state occurs when HEAD points directly to a specific commit instead of a branch, typically after checking out a commit hash or tag. Any new commits made in this state aren't attached to a branch, so they can be lost once another branch is checked out unless a new branch is created to save them.
- **git log options**
  - git log accepts many options to customize how commit history is displayed, such as --oneline for a condensed view or --graph to visualize branching and merging. Filters like --author or --since narrow results to specific contributors or time ranges.

### 2.3 Undoing Changes
- **git revert**
  - git revert creates a new commit that undoes the changes made by a previous commit, without altering existing history. This makes it a safe way to undo changes on a branch that others have already pulled, since it doesn't rewrite any commits.
- **git reset**
  - Git reset is a command that allows you to "undo" or reset your current branch to a previous state by moving its HEAD pointer, effectively discarding changes made since then. When using git reset, it's essential to specify one of the three modes: soft, hard, or mixed.
- **--soft**
  - git reset --soft moves the branch pointer to a specified commit while leaving the staging area and working directory untouched. This means all changes from the undone commits remain staged, ready to be recommitted differently.
- **--hard**
  - git reset --hard moves the branch pointer to a specified commit and resets both the staging area and working directory to match it exactly. Any changes in commits after that point, as well as any uncommitted work, get permanently discarded.
- **--mixed**
  - When using mixed mode, the HEAD pointer is moved to the specified commit. However, files in your working directory remain as they were before the reset.
- **commit-msg**
  - The commit-msg hook is a client-side hook that runs after you enter a commit message, but before the commit is finalized in your repository. It's typically used to validate or modify the commit message before it's recorded in the Git history.
- **post-checkout**
  - Git post-checkout hooks are scripts that run automatically after a successful git checkout operation. These hooks provide a way to customize Git's behavior and perform specific actions when switching branches or updating the working directory.

### 2.4 Viewing Diffs
- **Roadmaps**
  - GitHub Roadmaps are a feature that helps you visualize and organize plans for your projects, allowing you to create a high-level view of milestones and goals, and collaborate on planning and tracking progress with team members.
- **Automations**
  - To add automation to your GitHub project, use built-in workflows that can trigger actions such as setting fields on item changes or archiving items meeting specific criteria, and also configure automatic item addition from repositories based on matching criteria.
- **Between Commits**
  - To compare two specific commits in your Git history, use git diff followed by the hashes of the commits. This will show you the changes made between those two points, including added, modified, and deleted lines.
- **Between Branches**
  - When comparing the differences between two branches, such as a feature branch and its upstream parent branch, use git diff <branch1>..<branch2>. This command displays the changes made on the feature branch relative to the parent branch.
- **Staged Changes**
  - To view the changes you've staged with git add, but not yet committed, use git diff --cached. This command compares the staged files against their original versions in the repository.
- **Unstaged Changes**
  - For changes that are not yet staged with git add, such as untracked new files or modified existing ones , use git diff. This command compares your working directory (your current changes) against the staging area (changes already staged with git add).

### 2.5 Rewriting History
- **git commit --amend**
  - git commit --amend is a command used to modify the most recent commit in your repository's history by updating its message, adding or removing files, or changing the commit's metadata. This allows you to correct mistakes or improve the commit's description after it has been made.
- **git rebase**
  - Git rebase is a powerful command in Git that allows you to integrate changes from one branch into another. Unlike git merge, which creates a new commit to combine the histories of two branches, git rebase moves or applies commits from one branch on top of another, effectively re-writing the commit history.
- **git filter-branch**
  - git filter-branch rewrites a large portion of a repository's history, often used to remove sensitive files or restructure the project after the fact. It applies a filter across many or all commits, such as deleting a specific file from every point in history.
- **git push --force**
  - git push --force overwrites the remote branch's history with the local branch's history, even if they've diverged. This is necessary after rewriting local commits, like through a rebase, since a normal push would be rejected due to mismatched history.
- **post-update**
  - Git post-update hooks are scripts that run automatically after a successful push to a repository. These hooks are executed on the remote repository and are typically used for server-side tasks such as updating other services, triggering continuous integration processes, or notifying team members about changes.
- **pre-commit**
  - The pre-commit hook runs before a commit is finalized, giving a chance to inspect the staged changes and abort the commit if something is wrong. It's frequently used to run linters, formatters, or tests against the code being committed.

### 2.6 Submodules
- **Adding / Updating**
  - To add a submodule to a repository, use git submodule add https://github.com/user/submodule-repo.git, which is the typical format for specifying the URL of the submodule repository. This creates a new folder for the submodule and checks it out at the specified revision.
- **What and Why use?**
  - Submodules let a project reference another Git repository at a specific commit, rather than copying its code directly into the main project. This is useful when multiple projects depend on the same shared library and need to track updates to it independently.

### 2.7 Git Patch
- **Git Patch**
  - In Git, a patch is a file that contains a set of changes made to a project's codebase. It's essentially a diff (difference) file that shows the modifications between two versions of a commit or a branch.

### 2.8 Tagging
- **Managing Tags**
  - Managing tags involves creating, listing, and deleting tags within a repository. The command git tag <name> creates a lightweight tag, while git tag -a <name> -m "message" creates an annotated one with extra details.
- **Pushing Tags**
  - Pushing tags in Git is the process of sharing your local tags with a remote repository. Tags in Git are used to mark specific points in the repository's history, typically to signify a release or a milestone.
- **Checkout Tags**
  - Tags in Git are typically used to mark specific points in history, such as a release version. Checking out a tag means switching your working directory to the state of the repository at the point in time when that tag was created.
- **GitHub Releases**
  - A GitHub release packages a specific tag along with release notes, binaries, or other downloadable assets. It gives users a clear, versioned snapshot of the project they can download without cloning the entire repository.
- **What are these?**
  - GitHub Actions lets developers automate tasks that happen in response to events in a repository, such as pushing code or opening a pull request. Instead of manually running tests or deployments, a workflow file defines what should happen automatically when a specific trigger occurs.

### 2.9 Git hooks
- **What and Why?**
  - Git hooks let developers automate tasks or enforce rules at key points in the Git workflow, such as validating a commit message or running a linter before code gets committed. They exist because manually remembering to run checks before every commit or push is error-prone and easy to skip.
- **Client vs Server Hooks**
  - Like many other Version Control Systems, Git has a way to fire off custom scripts when certain important actions occur. There are two groups of these hooks: client-side and server-side.
- **pre-push**
  - The pre-push hook runs before commits are pushed to a remote repository, allowing checks to run on the commits about to be shared. It's often used to run a test suite or verify that the branch is up to date before allowing the push to proceed.

### 2.10 GitHub Actions
- **YAML Syntax**
  - GitHub Actions workflows are written in YAML, a human-readable format that uses indentation to represent structure instead of brackets or tags. A workflow file defines keys like on for triggers, jobs for the tasks to run, and steps for individual commands within each job.
- **Workflow Triggers**
  - Workflow triggers are events that initiate a GitHub Actions workflow. They can be scheduled, triggered by code changes, or manually initiated.
- **Scheduled Worfklows**
  - Scheduled workflows run automatically at specified times using cron syntax under the schedule trigger in a workflow file. This is useful for recurring tasks like nightly builds, periodic cleanup jobs, or fetching data on a regular interval.
- **Workflow Runners**
  - Workflow runners are the environments where GitHub Actions workflows are executed. They are hosted on GitHub-hosted virtual machines (GHVMs) or self-hosted runners.
- **Workflow Context**
  - Workflow context in GitHub Actions refers to the environment and variables that are available to a workflow. It includes information about the workflow's execution, such as the event that triggered it, the repository, and the workflow itself.
- **Usecases**
  - Common use cases for GitHub Actions include running automated tests on every pull request, building and deploying applications, publishing packages, and sending notifications. It can also automate repository maintenance tasks, like labeling issues or closing stale pull requests.
- **Workflow Expressions**
  - Understand fundamental concepts, architectures, and implementation practices of Workflow Expressions.

### 2.11 GitHub CLI
- **Installation and Setup**
  - Installing GitHub CLI involves downloading the gh tool through a package manager like Homebrew, apt, or winget, depending on the operating system. After installation, running gh auth login connects the tool to a GitHub account through browser or token-based authentication.
- **Repository management**
  - GitHub CLI supports repository management commands like gh repo create, gh repo clone, and gh repo view, letting developers manage repositories without leaving the terminal. These commands mirror actions normally done through the GitHub website, such as creating a new repo or checking its details.
- **Issue Management**
  - GitHub CLI allows creating, listing, and closing issues directly from the terminal using commands like gh issue create and gh issue list. Filters can narrow results by label, assignee, or state, similar to searching issues on the website.
- **Pull Requests**
  - GitHub CLI supports the full pull request workflow from the terminal, including creating one with gh pr create, reviewing changes with gh pr diff, and merging with gh pr merge. This lets developers open and manage pull requests without leaving their code editor or terminal session.
- **Git Reflog**
  - Git reflog is a powerful tool in Git that keeps a record of all the changes made to the branches and commits in your repository, including actions that are not part of the regular commit history, such as resetting branches or checking out commits. It's particularly useful for recovering lost commits or understanding the history of changes in your repository, even if those changes are not reflected in the normal commit history.Reflog stands for "reference log." It records when the tip of branches or other references (like HEAD) is updated in your repository.
- **Git Bisect**
  - Git Bisect is an interactive tool used to identify which commit in your project's history introduced a bug or regression. You start by identifying two commits: one where the issue isn't present (the "good" commit) and another where it is (the "bad" commit).
- **Git Worktree**
  - Git worktree allows multiple branches to be checked out simultaneously in separate directories, all linked to the same repository. Running git worktree add <path> <branch> creates a new working directory for a specific branch without needing to clone the repository again.
- **Git Attributes**
  - Git attributes are settings stored in the .gitattributes file, controlling how Git handles files in your repository. They can influence filtering (e.g., ignoring specific files), conversion (formatting or transforming files during Git operations), and formatting (applying consistent styles).

### 2.12 GitHub API
- **Git LFS**
  - Git Large File Storage (LFS) is an extension that helps manage large files by tracking metadata, not storing entire files. It allows storing and tracking binary assets like images, videos, audio files separately from your regular Git repository.
- **REST API**
  - The GitHub REST API is a set of APIs that provide access to various GitHub features, such as user data, repository information, and commit history. It allows developers to interact with the GitHub platform programmatically.
- **GraphQL API**
  - The GitHub GraphQL API is a set of APIs that provides access to various GitHub features, such as user data, repository information, and commit history. It allows developers to interact with the GitHub platform programmatically using GraphQL queries.

### 2.13 Creating Apps
- **Use in Automation**
  - GitHub CLI can be used inside scripts or CI/CD pipelines to automate tasks like creating releases, commenting on issues, or triggering workflows. Because it supports authentication via tokens, it can run in non-interactive environments without manual login.
- **GitHub Apps**
  - A GitHub App is a way to integrate with the GitHub platform programmatically, using either the REST API or GraphQL API. It allows developers to create custom integrations that can automate tasks, provide real-time notifications, and build custom workflows.
- **OAuth Apps**
  - GitHub OAuth Apps allow developers to integrate with GitHub using OAuth 2.0 authentication. They enable secure, token-based access to specific GitHub resources like repositories, issues, and pull requests.

### 2.14 Webhooks
- **Secrets and Env Vars**
  - Secrets store sensitive values like API keys or passwords securely, configured in a repository's settings and referenced in workflows without exposing their actual values in logs. Environment variables, defined with the env key, hold configuration values that steps in a workflow can access during execution.
- **Caching Dependencies**
  - Caching dependencies in GitHub Actions stores files like package manager directories between workflow runs, avoiding the need to reinstall them from scratch every time. The actions/cache action saves and restores these files based on a key, often derived from a lockfile's hash.
- **Storing Artifacts**
  - Artifacts are files produced during a workflow run, like build outputs or test reports, that can be saved and downloaded after the workflow finishes. The actions/upload-artifact action stores these files, and actions/download-artifact retrieves them in a later job or for manual inspection.
- **Workflow Status**
  - Workflow status indicates whether a GitHub Actions run succeeded, failed, or is still in progress, shown directly on commits, pull requests, and the Actions tab. Status checks can be configured as required, blocking a pull request from merging until the workflow passes.
- **Marketplace Actions**
  - Marketplace Actions are pre-built, reusable workflow steps published by GitHub and the community that can be added to any workflow. Instead of writing custom scripts for common tasks like checking out code or setting up a programming language, a workflow can reference an action like actions/checkout or actions/setup-node.
- **Deploying Static Websites**
  - Deploying static websites on GitHub Pages involves uploading and serving website content that is generated beforehand, without dynamic functionality. This approach allows for fast deployment, low maintenance, and improved security.

---

## 3. Advanced

### 3.1 GitHub Copilot
- **GitHub Copilot**
  - GitHub Copilot is an AI-powered code-completion tool that helps developers write code faster and with less errors. It uses a combination of machine learning algorithms and access to GitHub's vast repository of open-source code to provide context-aware suggestions for coding tasks.

### 3.2 GitHub Gists
- **GitHub Gists**
  - A GitHub Gist is a small code or text snippet that can be shared with others. It is a simple way to share code, configuration files, or other snippets of text without creating a full-fledged repository.

### 3.3 GitHub Models
- **GitHub Models**
  - GitHub Models is a feature that allows developers to search, explore, and use pre-trained AI models from various sources. This platform provides a way to discover and experiment with these models, making it easier to integrate AI capabilities into software projects.

### 3.4 GitHub Packages
- **GitHub Packages**
  - GitHub Packages is a package hosting service that lets developers publish and manage packages, like npm, Docker, or Maven artifacts, directly within GitHub. It integrates with existing repository permissions, so access to a package can follow the same rules as the repository it's tied to.

### 3.5 GitHub Pages
- **Custom Domains**
  - On GitHub Pages, users can customize their site's URL by connecting a custom domain to their repository. This feature allows users to use their own domain name instead of the default GitHub.io subdomain, giving their site a more professional and personalized look.
- **Static Site Generators**
  - GitHub offers a set of static site generators (SSGs) that allow users to create and deploy websites directly from their GitHub repositories. These SSGs include Jekyll, Hugo, and Middleman, among others.

### 3.6 GitHub Marketplace
- **GitHub Marketplace**
  - GitHub Marketplace is a platform that allows developers to discover, install, and manage third-party tools and services directly within their GitHub environment. These tools can provide a range of features, such as code analysis, project management, or collaboration, making it easier for developers to work efficiently and effectively.

### 3.7 GitHub Codespaces
- **GitHub Codespaces**
  - GitHub Codespaces provides a cloud-based development environment that can be launched directly from a repository, complete with a configured editor and terminal. It uses a configuration file, typically a devcontainer.json, to define the environment's tools, extensions, and dependencies.

### 3.8 GitHub Education
- **Student Developer Pack**
  - The GitHub Student Developer Pack is a collection of developer tools and resources that are offered free or at a discounted price to students through the GitHub Education program. This pack includes access to GitHub, GitHub Desktop, GitHub Classroom, GitHub Student Developer Kit, and other benefits.
- **GitHub Classroom**
  - GitHub Classroom is an integrated feature within GitHub that allows educators to create and assign homework assignments, projects, or quizzes directly to students. This feature streamlines the process of teaching and learning by making it easy for instructors to share code, provide feedback, and track student progress all in one place.
- **Campus Program**
  - The GitHub Campus Program offers GitHub Enterprise Cloud and GitHub Enterprise Server free-of-charge for schools that want to make the most of GitHub for their community. This program provides access to a comprehensive set of developer tools, as well as resources and support to help students and educators build projects, collaborate, and develop skills in software development.

### 3.9 GitHub Security
- **GitHub Security**
  - GitHub Security covers the built-in tools that help identify and fix vulnerabilities in a repository, such as dependency scanning, secret scanning, and code scanning. These features can flag outdated dependencies with known vulnerabilities or detect accidentally committed secrets like API keys.

### 3.10 GitHub Sponsors
- **GitHub Sponsors**
  - GitHub Sponsors lets developers and organizations receive financial support directly from users who want to fund their open source work. Sponsors can choose a one-time or recurring monthly contribution, and maintainers can offer different sponsorship tiers with specific perks.

---

## 4. Optional / Specialized Topics

- git init
- git config
- Local vs Global Config
- Cloning Repositories
- GitHub Interface
- Profile Readme
- Private vs Public
- Handling Conflicts
- Rebase
- Squash
- Cherry Picking Commits
- Commit Messages
- Labelling Issues / PRs
- Saved Replies
- Mentions
- Reactions
- Project Readme
- GitHub Wikis
- CITATION files
- --mixed
- commit-msg
- post-checkout
- Staged Changes
- Unstaged Changes
- post-update

---

## 5. References

- [Git & GitHub Roadmap](https://roadmap.sh/git-github)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- Backend Developer
- DevOps Engineer
- Fullstack Developer

### Related Skills
- Computer Science
- Linux