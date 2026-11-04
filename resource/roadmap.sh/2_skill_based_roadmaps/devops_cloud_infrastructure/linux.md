# Linux

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/linux
- Related Roles:
  - DevOps Engineer
  - Backend Developer
  - Cyber Security Specialist

---

## 1. Beginner

### 1.1 Navigation Basics
- **Basic Commands**
  - Linux Navigation Basics is about using simple commands to move around and manage files on your computer. For example, cd lets you go into different folders, ls shows you what files and folders are inside, and pwd tells you where you are currently.
- **Moving Files / Directories**
  - In Linux, moving files is an essential task that you will need to perform quite frequently. The mv command, short for move, is used to move files and directories from one location to another.
- **Creating & Deleting Files / Dirs**
  - Linux file creation uses touch for empty files, echo "text" > filename for text files, or cat > filename for interactive input. Commands like mkdir create directories.
- **Directory Hierarchy Overview**
  - In Linux, understanding the directory hierarchy is crucial for efficient navigation and file management. A Linux system's directory structure, also known as the Filesystem Hierarchy Standard (FHS), is a defined tree structure that helps to prevent files from being scattered all over the system and instead organise them in a logical and easy-to-navigate manner.

### 1.2 Editing Files
- **Vim**
  - Vim (Vi Improved) is a powerful and flexible text editor used in Unix-like systems. It builds on the original Vi editor with additional features and improvements, including multi-level undo, syntax highlighting, and an extensive set of commands for text manipulation.
- **Nano**
  - Nano is a popular, user-friendly text editor used for creating and editing files directly within the Linux command line interface (CLI). It is an alternative to editors like Vi and Emacs and is considered more straightforward for beginners due to its simple and intuitive interface.

### 1.3 Shell and Other Basics
- **Command Path**
  - The command path is a variable that is used by the shell to determine where to look for the executable files to run. Linux commands are nothing but programs residing in particular directories.
- **Environment Variables**
  - Environment variables are dynamic named values that can affect the behavior of running processes in a shell. They exist in every shell session.
- **Command Help**
  - Linux command help provides documentation and usage information for shell commands. Use man command for detailed manuals, help command for shell built-ins, command --help for quick options, and tldr command for practical examples.
- **Redirects**
  - Redirects change where a command's input comes from or where its output goes, instead of the default terminal screen. The > operator sends output to a file, overwriting it, while >> appends to the end of a file instead.
- **Super User**
  - The super user, commonly referred to as root, is the account with unrestricted access to every file, process, and setting on a Linux system. Regular users run commands with sudo to temporarily gain root privileges for a single command, rather than logging in as root directly.
- **stdout / stdin / stderr**
  - Linux processes use three standard data streams: STDIN (input), STDOUT (output), and STDERR (error messages). STDOUT handles normal command output while STDERR specifically handles error messages.
- **paste**
  - In Linux, paste is a powerful text processing utility that is primarily used for merging lines from multiple files. It allows users to combine data by columns rather than rows, adding immense flexibility to textual data manipulation.

### 1.4 Working with Files
- **File Permissions**
  - File permissions control who can read, write, or execute a file, split into three categories: owner, group, and others. Each category can have any combination of read (r), write (w), and execute (x) permissions, often represented as a numeric value like 755.
- **Archiving and Compressing**
  - Archiving bundles multiple files into a single file, typically using tar, while compressing reduces that file's size using tools like gzip or bzip2. A common pattern combines both steps at once, such as tar -czvf archive.tar.gz folder/, which archives and compresses a folder in one command.
- **Copying and Renaming**
  - Essential Linux file operations use cp to copy files and mv to move/rename them. The cp command copies files from source to destination, while mv moves or renames files/directories.
- **Soft Links / Hard Links**
  - Linux supports two types of file links. Hard links share the same inode and data as the original file - if the original is deleted, data remains accessible.

### 1.5 Text Processing
- **cut**
  - The cut command is a text processing utility that allows you to cut out sections of each line from a file or output, and display it on the standard output (usually, the terminal). It's commonly used in scripts and pipelines, especially for file operations and text manipulation.
- **sort**
  - Linux provides a variety of tools for processing and manipulating text files, one of which is the sort command. The sort command in Linux is used to sort the contents of a text file, line by line.
- **head**
  - The head command in Linux is a text processing utility that allows a user to output the first part (or the "head") of files. It is commonly used for previewing the start of a file without loading the entire document into memory, which can act as an efficient way of quickly examining the data in very large files.
- **tr**
  - The tr command in Linux is a command-line utility that translates or substitutes characters. It reads from the standard input and writes to the standard output.
- **tail**
  - The tail command in Linux is a utility used in text processing. Fundamentally, it's used to output the last part of the files.
- **join**
  - join is a powerful text processing command in Linux. It lets you combine lines of two files on a common field, which works similar to the 'Join' operation in SQL.
- **split**
  - Linux provides an extensive set of tools for manipulating text data. One of such utilities is the split command that is used, as the name suggests, to split large files into smaller files.
- **pipe**
  - The pipe (|) is a powerful feature in Linux used to connect two or more commands together. This mechanism allows output of one command to be "piped" as input to another.
- **tee**
  - The tee command reads from standard input and writes to both standard output and files simultaneously, like a T-splitter in plumbing. It enables users to view results in the terminal while saving output to files concurrently.
- **nl**
  - The nl command numbers lines in text files, providing an overview of line locations. By default, it numbers only non-empty lines, but this behavior can be modified.
- **wc**
  - The wc command is a commonly used tool in Unix or Linux that allows users to count the number of bytes, characters, words, and lines in a file or in data piped from standard input. The name wc stands for 'word count', but it can do much more than just count words.
- **expand**
  - The expand command converts tabs to spaces in text files, useful for consistent formatting across different systems and editors. Default conversion is 8 spaces per tab.
- **unexpand**
  - The unexpand command converts spaces to tabs in text files, making documents more coherent and neat. Commonly used in programming scripts where tab indentation is preferred.
- **uniq**
  - uniq is an extremely useful command-line program for text processing. It aids in the examination and manipulation of text files by comparing or filtering out repeated lines that are adjacent.
- **grep**
  - GREP (Global Regular Expression Print) is a powerful text search utility that finds and filters text matching specific patterns in files. It searches line by line and prints matching lines to the screen.
- **awk**
  - AWK is a powerful text-processing language for Unix-like systems, named after its creators Aho, Weinberger, and Kernighan. It reads files line by line, identifies patterns, and executes actions on matches.

---

## 2. Intermediate

### 2.1 Server Review
- **Uptime and Load**
  - The uptime command shows system running time and load averages for 1, 5, and 15-minute intervals. Load average indicates computational work and processes waiting for CPU time.
- **Authentication Logs**
  - Authentication logs in Linux record all auth-related events like logins, password changes, and sudo commands. Located at /var/log/auth.log (Debian) or /var/log/secure (RHEL/CentOS), these logs help detect brute force attacks and unauthorized access attempts.
- **Services Running**
  - Linux servers run various services including web, database, DNS, and mail servers. System administrators use tools like systemctl, service, netstat, ss, and lsof to manage and monitor services.
- **Available Memory / Disk**
  - Linux provides tools like free, vmstat, and top to monitor system memory usage and performance. The free -h command shows total, used, free, shared, buffer/cache, and available memory in human-readable format.

### 2.2 Process Management
- **Background / Foreground Processes**
  - Linux processes run in foreground (taking direct user input) or background (running independently). Send processes to background with & or bg command.
- **Listing / Finding Processes**
  - Linux processes can be monitored using the proc virtual filesystem and commands like ps, top, and htop. Use ps -ef for process snapshots, top/htop for real-time views.
- **Process Signals**
  - Process signals are communication mechanisms in Linux that notify processes of synchronous or asynchronous events. Common signals include SIGINT, SIGSTOP, SIGKILL for interrupting, pausing, or terminating processes.
- **Killing Processes**
  - The kill command terminates processes manually by sending specific signals to Process IDs (PIDs). Used when processes behave unexpectedly due to system bugs or accidental initiation.
- **Process Priorities**
  - Linux assigns priority levels to processes for efficient resource utilization and execution timing. Priority values ("nice" values) range from -20 (highest) to +19 (lowest priority).
- **Process Forking**
  - Process forking uses the fork() system call to create child processes from parent processes, enabling concurrent execution. Child processes are nearly perfect copies of parents with different PIDs.

### 2.3 User Management
- **Create / Delete / Update**
  - Linux user management involves creating, updating, and deleting user accounts for system security and resource utilization. Key commands: useradd/adduser (create users), usermod (update user details like home directory/shell), userdel (delete users).
- **Users and Groups**
  - Linux user groups simplify system administration by managing collections of users with shared access rights to files and directories. Each user belongs to one or more groups, enabling privilege management without full superuser access.

### 2.4 Service Management (systemd)
- **Managing Permissions**
  - Linux permissions control file and directory access for users, groups, and others with read, write, and execute types. Commands include chmod (change permissions), chown (change owner), and chgrp (change group).
- **Creating New Services**
  - Creating Linux services involves setting up background applications using systemd service files. Services run continuously performing essential tasks like web servers, databases, and mail servers.
- **Checking Service Logs**
  - Systemd captures output from all managed services and stores it in the journal, a binary log managed by journald. You can view logs for a specific service using journalctl -u service-name.
- **Starting / Stopping Services**
  - Linux service management controls system services like firewall, network, and database using systemctl commands. Basic operations: sudo systemctl start servicename (start), sudo systemctl stop servicename (stop), sudo systemctl restart servicename (restart).
- **Checking Service Status**
  - systemctl status service-name gives a real-time snapshot of a service: whether it's active, inactive, or failed; its process ID; recent log lines; and any error messages from the last run. For a quick boolean check, systemctl is-active and systemctl is-enabled return simple values suitable for use in scripts.

### 2.5 Package Management
- **Package Repositories**
  - Repositories are storage locations containing collections of software packages for Linux distributions. They store thousands of compiled packages specific to each distribution (.deb for Debian/Ubuntu, .rpm for Fedora/CentOS).
- **Finding & Installing Packages**
  - Linux package managers like apt, yum, and dnf automate software installation, upgrading, configuring, and removal. Debian-based systems: sudo apt-get update && sudo apt-get install package-name.
- **Listing Installed Packages**
  - Linux distributions use different package managers: apt (Debian-based), dnf (Fedora), zypper (OpenSUSE), pacman (Arch). Listing installed packages helps with auditing software and deployment automation.
- **Install / Remove / Upgrade Packages**
  - Linux package management handles installing, removing, and upgrading pre-compiled software modules. Different distributions use specific package managers: apt (Debian/Ubuntu), yum/dnf (Fedora/RHEL/CentOS), zypper (SUSE).
- **Snap**
  - Snap is a modern Linux package management system by Canonical providing self-contained packages with all dependencies included. Snaps run consistently across different Linux distributions, install from Snapcraft store, and update automatically.

### 2.6 Disks and Filesystems
- **Inodes**
  - An inode (index node) is a data structure in Linux filesystems that stores metadata about files and directories except their names and actual data. Contains file size, owner, permissions, timestamps, and more.
- **Filesystems**
  - Filesystems define how files are stored and organized on Linux storage disks, ensuring data integrity, reliability, and efficient access. Linux supports various types like EXT4, XFS, BTRFS with different performance and recovery capabilities.
- **Swap**
  - Swap space extends physical memory by using disk storage when RAM is full. Inactive memory pages move to swap, freeing RAM but with performance impact due to slower disk access.
- **Mounts**
  - Mounting in Linux attaches filesystems to specific directories (mount points) in the directory tree, allowing the OS to access data on storage devices. The mount command performs this operation.
- **Adding Disks**
  - Adding disks in Linux involves partitioning, creating filesystems, and mounting. Use lsblk to list devices, fdisk /dev/sdX to create partitions, mkfs.ext4 /dev/sdX1 to create filesystems, and mount /dev/sdX1 /mount/point to mount.
- **LVM**
  - LVM provides logical volume management through device mapper framework, offering flexible disk management with resizing, mirroring, and moving capabilities. Three levels: Physical Volumes (PVs - actual disks), Volume Groups (VGs - storage pools), and Logical Volumes (LVs - carved portions).

---

## 3. Advanced

### 3.1 Booting Linux
- **Logs**
  - Linux maintains logs documenting system activities, errors, and kernel messages. Boot logs record all operations during system startup for troubleshooting.
- **Boot Loaders**
  - Boot loaders load the OS kernel into memory when systems start. Common Linux boot loaders include GRUB (modern, feature-rich with graphical interface) and LILO (older, broader hardware support).

### 3.2 Networking
- **TCP/IP Stack**
  - TCP/IP (Transmission Control Protocol/Internet Protocol) forms the backbone of internet communication, allowing computers to connect and transfer data. It comprises four layers: Network Interface, Internet, Transport, and Application.
- **Subnetting**
  - Subnetting divides networks into smaller subnets to improve performance and security in Linux networking. It organizes IP addresses within IP addressing schemes, preventing conflicts and efficiently utilizing address ranges.
- **Ethernet & arp/rarp**
  - Three crucial Linux networking components: Ethernet enables LAN device communication, ARP (Address Resolution Protocol) translates IP addresses to MAC addresses for direct network communication, and RARP (Reverse ARP) converts MAC addresses to IP addresses when devices know their MAC but need their IP. Essential for diagnosing and managing Linux networking issues.
- **DHCP**
  - DHCP (Dynamic Host Configuration Protocol) automatically allocates IP addresses and network configuration to clients, ensuring unique addresses for each machine. In Linux, install with sudo apt-get install isc-dhcp-server and configure via /etc/dhcp/dhcpd.conf.
- **IP Routing**
  - IP routing in Linux involves configuring routing tables and network routes for packet forwarding across networks. The kernel handles route selection to send packets to their destinations.
- **DNS Resolution**
  - DNS (Domain Name System) converts hostnames to IP addresses, enabling users to access websites without remembering numeric addresses. Linux systems use /etc/resolv.conf to configure DNS resolution.
- **Netfilter**
  - Netfilter is a Linux kernel framework for manipulating and filtering network packets with hooks at various stages (pre-routing, input, forward, output, post-routing). Used for firewalls and NAT management with iptables configuration.
- **SSH**
  - SSH (Secure Shell) is a cryptographic network protocol providing secure remote access, command execution, and data communication between networked computers. Replaces insecure protocols like Telnet with confidentiality, integrity, and security.
- **File Transfer**
  - Linux file transfer involves copying or moving files between systems over networks. Command-line tools support protocols like FTP, HTTP, SCP, SFTP, and NFS.

### 3.3 Shell Programming
- **Literals**
  - Shell literals are fixed values in source code including string literals (enclosed in quotes), numeric literals (sequences of digits), and boolean literals (1=true, 0=false). String examples: 'Hello, world!' or "Hello, world!".
- **Variables**
  - Shell variables store system or user-defined data that can change during script execution. Two categories exist: System Variables (PATH, HOME, PWD) created by Linux, and User-Defined Variables created by users.
- **Loops**
  - Shell loops automate repetitive tasks with three types: for (iterates over lists), while (executes while condition true), until (runs until condition true). Example: for i in 1 2 3; do echo "$i"; done outputs each number.
- **Conditionals**
  - Shell conditionals allow scripts to make decisions based on conditions using if, elif, and else statements. These control process flow by evaluating string variables, arithmetic tests, or process status.
- **Debugging**
  - Shell script debugging in Linux uses tools like bash's -x option for execution traces, trap, set commands, and external tools like shellcheck. Use #!/bin/bash -x in scripts or bash -x script.sh from command line for tracing.

### 3.4 Troubleshooting
- **ICMP**
  - Internet Control Message Protocol (ICMP) is a supportive protocol used by network devices to communicate error messages and operational information. Essential for Linux network troubleshooting, ICMP enables tools like ping and traceroute to diagnose network connectivity and routing issues.
- **traceroute**
  - Traceroute is a Linux network diagnostic tool that displays the path packets take from your system to a destination. It identifies routing problems, measures latency, and reveals network structure as packets traverse the internet.
- **netstat**
  - Netstat is a command-line tool for network troubleshooting and performance measurement in Linux. It provides network statistics, open ports, routing table information, and protocol details.
- **Packet Analysis**
  - Packet analysis is a key Linux network troubleshooting skill involving capturing and analyzing network traffic to identify performance issues, connectivity problems, and security vulnerabilities. Tools like tcpdump and Wireshark provide packet-level details for network diagnostics.

### 3.5 Containerization
- **ping**
  - The ping command is essential for Linux network troubleshooting, checking connectivity between your host and target machines. It sends ICMP ECHO\REQUEST packets and listens for ECHO\RESPONSE returns, providing insights into connection health and speed.
- **ulimits**
  - Ulimits (user limits) are Linux kernel features that restrict resources like file handles and memory that processes can consume. In containerization, ulimits prevent rogue processes from exhausting server resources and creating denial-of-service situations.
- **cgroups**
  - Cgroups (control groups) are a Linux kernel feature that organizes processes into hierarchical groups and limits their resource usage (CPU, memory, disk I/O). Essential for containerization, cgroups prevent containers from monopolizing host resources, ensuring system stability and performance.
- **Container Runtime**
  - Container runtime is software responsible for running containers in Linux, providing image transport, storage, execution, and network interactions. Popular options include Docker (comprehensive ecosystem), Containerd (lightweight standalone), and CRI-O (Kubernetes-optimized).
- **Docker**
  - Docker is an open-source containerization platform that uses OS-level virtualization to package applications with dependencies into lightweight containers. In Linux, Docker containers share the kernel and use features like namespaces and cgroups for isolation.

---

## 4. Optional / Specialized Topics

- Super User
- stdout / stdin / stderr
- paste
- tail
- join
- split
- pipe
- tee
- nl
- wc
- expand
- unexpand
- uniq
- grep
- awk
- Process Priorities
- Process Forking
- Checking Service Status
- Snap
- Adding Disks
- LVM
- IP Routing
- DNS Resolution
- Netfilter
- SSH

---

## 5. References

- [Linux Roadmap](https://roadmap.sh/linux)

---

## 6. Related Roles / Topics

### Related Roles
- DevOps Engineer
- Backend Developer
- Cyber Security Specialist

### Related Skills
- Docker