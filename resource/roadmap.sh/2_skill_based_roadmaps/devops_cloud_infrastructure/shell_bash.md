# Shell & Bash

## Metadata
- Type: Skill
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/shell-bash
- Related Roles:
  - Backend Developer
  - Fullstack Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **CLI vs GUI**
  - A Command Line Interface (CLI) is a text-based interface used to interact with a computer system by typing commands. A Graphical User Interface (GUI), on the other hand, utilizes visual elements such as windows, icons, and menus to enable users to interact with the system using a mouse, touchpad, or touchscreen.
- **What is Bash?**
  - Bash, short for Bourne Again Shell, is a command-line interpreter and a shell scripting language. It's essentially a program that allows users to interact with the operating system by typing commands.
- **What is scripting?**
  - Scripting is the process of writing a series of commands that are executed in a specific order by a program or scripting engine. These commands, often written in a simple, human-readable language, automate tasks, control software applications, or interact with operating systems.
- **dash**
  - dash (Debian Almquist Shell) is a Unix shell that is smaller, faster, and requires fewer resources compared to Bash. It's often used as the default /bin/sh on Debian-based systems and is designed to be POSIX-compliant, focusing on speed and efficiency in script execution.
- **zsh**
  - Zsh, also known as the Z shell, is a Unix shell that can be used as an interactive login shell and as a shell script command interpreter. It's designed to be highly customizable and offers features like improved tab completion, shared command history across multiple terminal windows, and powerful theming options.

### 1.2 Popular Shells
- **bash**
  - Bash, short for Bourne Again Shell, is a command-line interpreter and a shell scripting language. It's a program that allows users to interact with the operating system by typing commands.
- **fish**
  - fish is a user-friendly command-line shell for UNIX-like operating systems. It focuses on providing a more interactive and discoverable experience compared to traditional shells like Bash or Zsh.
- **cmd**
  - cmd, also known as the Command Prompt, is the default command-line interpreter on Windows operating systems. It allows users to interact with the operating system by entering text-based commands.
- **tcsh**
  - tcsh is an enhanced version of the C shell (csh), a Unix shell program. It's designed as an interactive login shell and a shell script command processor.
- **PowerShell**
  - PowerShell is a cross-platform task automation and configuration management framework, consisting of a command-line shell and associated scripting language. It's built on the .NET Common Language Runtime (CLR) and accepts and returns .NET objects, which allows for more complex and structured data manipulation compared to traditional text-based shells.
- **ksh**
  - ksh, or the Korn shell, is an interactive command language and scripting language. It's designed to be backward-compatible with the Bourne shell (sh) while incorporating many features from other shells like csh.

### 1.3 Setting Up Bash
- **Setting Up Bash**
  - Setting up Bash involves configuring your shell environment to suit your preferences and workflow. This includes customizing the appearance of your command prompt, defining aliases for frequently used commands, setting environment variables to control program behavior, and creating custom functions to automate tasks.

### 1.4 Files & Directories
- **pwd**
  - pwd (print working directory) is a command-line utility that displays the absolute path of the current directory you are working in. It essentially tells you where you are located within the file system hierarchy from the root directory.
- **cp**
  - The cp command in Unix-like operating systems is used to copy files and directories from one location to another. It creates an exact duplicate of the source file or directory at the specified destination, leaving the original intact.
- **echo**
  - echo is a fundamental command-line utility used to display lines of text. It essentially prints its arguments to standard output, which is typically your terminal screen.
- **mv**
  - The mv command in Unix-like operating systems is used to move or rename files and directories. It allows you to relocate files from one directory to another, effectively changing their location within the file system.
- **cat**
  - cat is a command-line utility that is primarily used to display the contents of one or more files on the standard output (usually your terminal screen). It can also be used to concatenate files, meaning to combine them into a single output stream.
- **touch**
  - The touch command is a fundamental utility used to update the access and modification times of files and directories. If a file doesn't exist, touch creates an empty file with the specified name.
- **find**
  - The find command is a powerful utility used to locate files and directories within a file system hierarchy. It allows you to search based on various criteria, such as name, size, modification time, permissions, and file type.
- **rm**
  - The rm command in Unix-like operating systems is used to remove files or directories. It permanently deletes the specified files, so caution is advised when using it.
- **ls**
  - ls is a command-line utility used to list files and directories within a specified directory. By default, it displays the contents of the current working directory.
- **cd**
  - cd is a fundamental command used to change the current working directory in a shell environment. It allows you to navigate through the file system, moving from one directory to another.
- **mkdir**
  - mkdir is a command-line utility used to create new directories (folders) in a file system. It allows users to organize files by grouping them into logical structures.
- **rmdir**
  - rmdir is a command-line utility used to remove empty directories. It's a straightforward tool that helps in cleaning up directory structures by deleting directories that no longer contain any files or subdirectories.

### 1.5 Tab Completion
- **stdin, stdout, stderr**
  - In computing, standard streams are preconnected input and output communication channels between a computer program and its environment. Specifically, stdin (standard input) is the channel through which a program receives input, typically from the keyboard or another program.
- **Output redirection**
  - Output redirection in shell scripting allows you to control where the output of a command is sent. Instead of displaying on the terminal, you can redirect it to a file, either overwriting the file or appending to it.

### 1.6 Repeat Commands
- **Repeat Commands**
  - In the shell, you can easily access and reuse previously executed commands. The most common way to do this is using the up and down arrow keys to navigate through your command history.

### 1.7 Help Commands
- **Help Commands**
  - Help commands in a shell environment provide users with information about available commands, their syntax, and options. They are essential tools for understanding how to use commands effectively and discovering new functionalities within the shell.

### 1.8 Bash Alias
- **Bash Alias**
  - A Bash alias is a shortcut or a custom name you assign to a command or a sequence of commands. Instead of typing a long command every time, you can create an alias that represents it.

### 1.9 Stop Execution
- **grep**
  - grep is a command-line utility used for searching plain-text data sets for lines matching a regular expression. It outputs the lines that contain the specified pattern, making it a powerful tool for filtering and locating specific information within files or streams of data.
- **Navigate between dirs**
  - Navigating between directories in a shell environment involves moving from one location in the file system to another. This is primarily achieved using the cd (change directory) command, which allows users to specify the destination directory, whether it's a relative path from the current location or an absolute path from the root directory.
- **cut, paste**
  - cut and paste are command-line utilities used for manipulating text files. cut extracts specific sections (columns) from each line of a file based on delimiters or character positions.
- **wc**
  - wc is a command-line utility that displays the number of lines, words, and bytes (or characters) in a file. It's a simple yet powerful tool for quickly getting a summary of the size and content of text files.

---

## 2. Intermediate

### 2.1 Redirects & Pipelines
- **Pipes**
  - Pipes in shell scripting are a form of redirection that allows you to send the output of one command as the input to another command. This creates a chain of commands where the data flows from one process to the next, enabling you to perform complex data manipulation and filtering concisely and efficiently.
- **Command substitution**
  - Command substitution allows you to use the output of a command as an argument to another command. It essentially captures the standard output of a command and inserts it into the command line of another command, enabling you to dynamically generate arguments or values based on the results of other commands.
- **Input redirection**
  - Input redirection enables a command to obtain its input from a source other than the standard input (typically the keyboard). Instead of typing input directly, a command can read data from a file or another command's output.
- **Process substitution**
  - Process substitution allows you to treat the output of a process as if it were a file. It provides a way to pass the output of one command as input to another command, without using temporary files or named pipes.
- **Error redirection**
  - Error redirection in shell scripting involves capturing and managing error messages generated by commands. By default, standard error (stderr) is displayed on the terminal.

### 2.2 Basic Editor Ops.
- **less, more**
  - less and more are command-line utilities used to view the contents of text files, one screen at a time. They allow users to navigate through the file, search for specific patterns, and perform other basic text manipulation tasks directly from the terminal.
- **head, tail**
  - head and tail are command-line utilities used to display the beginning or end of a file, respectively. head shows the first few lines of a file, while tail shows the last few lines.
- **find**
  - find is a command-line utility for searching files and directories within a specified directory hierarchy. It allows you to locate files based on various criteria, such as name, type, size, modification time, permissions, and more.
- **join, split**
  - join and split are command-line utilities used for manipulating text files. join combines lines from two files based on a common field, creating a new file with the merged data.
- **tr**
  - The tr command in Unix-like operating systems is a command-line utility that translates or deletes characters. It reads standard input, performs the specified transformations, and writes the result to standard output.
- **sed**
  - sed (Stream EDitor) is a powerful command-line utility used for text transformation. It operates on a stream of text, performing operations like searching, replacing, deleting, and inserting text based on patterns or line numbers.
- **sort**
  - sort is a command-line utility that arranges lines of text in a specific order. It can sort alphabetically, numerically, by month, or even based on custom criteria.
- **uniq**
  - uniq is a command-line utility that filters adjacent matching lines from an input file (or standard input) and writes a single copy of the matching line to the output. It's primarily used to remove duplicate lines, but it requires that the duplicates be next to each other to be effective.
- **nl**
  - nl is a command-line utility that numbers the lines of a file or standard input. It reads lines, adds line numbers, and writes the result to standard output.
- **awk**
  - awk is a powerful text processing tool in Unix-like operating systems. It scans input files line by line, searching for lines that match a specified pattern.
- **[...]**
  - Square brackets [] in shell wildcards define a character class, matching any single character within the brackets. This allows you to specify a range or set of characters to match in a filename or string.
- **{...}**
  - Curly braces {} are used for multiple matches. Each string can be an exact name, or a wildcard.

### 2.3 Text Editors
- **Nano**
  - Nano is a simple, beginner-friendly text editor for Unix-like operating systems. It's designed to be easy to use, with a straightforward interface that displays command shortcuts at the bottom of the screen.
- **Emacs**
  - Emacs is a highly customizable and extensible text editor, known for its powerful features and extensive ecosystem of extensions. It's more than just a text editor; it's often described as an operating system within an operating system due to its ability to handle tasks like file management, email, and even web browsing, all within its environment.
- **Vim**
  - Vim is a highly configurable text editor built to enable efficient text editing. It's an improved version of the vi editor distributed with most UNIX systems.
- **Vi**
  - Vi is a powerful text editor that's been a standard part of Unix-like systems for decades. It operates in different modes, primarily command mode for issuing instructions and insert mode for typing text.

### 2.4 Bash Script Anatomy
- **Bash Script Anatomy**
  - A Bash script is essentially a plain text file containing a series of commands that the Bash interpreter executes sequentially. It typically starts with a shebang line specifying the interpreter to use, followed by comments explaining the script's purpose, and then the actual commands that perform the desired actions, including variable assignments, control structures (like loops and conditional statements), and function definitions.

### 2.5 Running Shell Scripts
- **Environment vs Shell vars.**
  - Environment variables are a set of dynamic named values that can affect the way running processes will behave on a computer. They are part of the environment in which a process runs.
- **Create, Print, Modify**
  - Variables in shell scripting are named storage locations that hold data. You can create a variable by assigning a value to a name.
- **Running with Bash**
  - Running a shell script with Bash involves explicitly invoking the Bash interpreter to execute the commands within the script. This is typically done by using the bash command followed by the script's filename as an argument.
- **Direct Execution**
  - Direct execution involves running a shell script by specifying its path directly to the shell. This method requires the script to have execute permissions set.
- **Running with Source**
  - Sourcing a shell script executes the commands within the script in the current shell environment, rather than in a subshell. This means that any variables, functions, or aliases defined or modified within the script will directly affect the shell you're currently working in.

### 2.6 Bash Data Types
- **Strings**
  - In Bash, strings are sequences of characters. They can be enclosed in single quotes ('...') or double quotes ("...").
- **Arrays**
  - Arrays are ordered collections of elements, where each element can be accessed using an index. They allow you to store multiple values under a single variable name, making it easier to manage and manipulate related data.
- **Numeric**
  - Bash, by default, treats all variables as strings. However, Bash can perform arithmetic operations on variables that contain numeric values.
- **Associative Arrays**
  - Associative arrays, also known as dictionaries or hash maps in other programming languages, are data structures that store key-value pairs. Unlike regular arrays which use numerical indexes to access elements, associative arrays use strings (or other data types in some languages) as keys.

### 2.7 Input/Output
- **Read user input**
  - Reading user input in a shell script allows the script to interact with the person running it. This is achieved by pausing the script's execution and waiting for the user to type something and press Enter.
- **Here documents**
  - Here documents (or "heredocs") are a way to redirect multiple lines of input to a command. Instead of typing input directly into the terminal or reading from a file, you can embed the input directly within your script.
- **printf formatting**
  - printf is a command-line utility used to format and print text in a specific way. It allows you to control the appearance of output by using format specifiers, which define how different types of data (strings, numbers, etc.) should be displayed.
- **Here strings**
  - Here strings provide a way to pass strings to commands as standard input. They are a simplified form of here documents, designed for single-line input.
- **Arithmetic expansion**
  - Arithmetic expansion allows you to perform mathematical calculations directly within your shell scripts. It uses the $((...)) syntax to evaluate expressions, treating the contents inside the parentheses as an arithmetic expression.
- **expr**
  - expr is a command-line utility used to evaluate expressions. It can perform arithmetic operations, string manipulations, and logical comparisons.
- **bc**
  - bc is a command-line utility for arbitrary-precision arithmetic. It allows you to perform calculations with numbers of any size and with a specified level of decimal precision, making it suitable for tasks where standard shell arithmetic is insufficient.

### 2.8 Comments
- **$1, $2, $3**
  - Positional parameters in shell scripting are variables that hold the command-line arguments passed to a script. These parameters are represented by special variables like $1, $2, $3, and so on, where each number corresponds to the order in which the argument was provided when the script was executed.
- **$0**
  - In shell scripting, $0 is a special variable that holds the name of the script being executed. It essentially represents the command used to invoke the script.

### 2.9 Bash Operators
- **Variable Scopes**
  - Variable scope determines the region of a program where a declared variable can be accessed. It defines the visibility and lifetime of a variable.
- **Variables best practices**
  - Using variables effectively in shell scripts involves following certain guidelines to improve readability, maintainability, and prevent errors. This includes choosing descriptive names, initializing variables before use, using appropriate scoping, and quoting variables to avoid unexpected behavior due to word splitting and globbing.
- **Special variables**
  - Special variables in shell scripting are predefined variables that automatically hold specific values related to the shell's operation or the script's execution environment. These variables provide access to information like the script's name, the number of arguments passed to it, the exit status of the last command, and process IDs.
- **Arithmetic**
  - Arithmetic operators in Bash are symbols used to perform mathematical calculations within shell scripts. These operators allow you to add, subtract, multiply, divide, and find the remainder of numbers directly within your scripts, enabling you to perform calculations and manipulate numerical data.
- **Comparison**
  - Comparison operators in Bash are used to compare values, typically numbers or strings. These operators allow you to create conditional statements within your scripts, enabling different code blocks to execute based on whether a comparison is true or false.

### 2.10 String Manipulation
- **String length**
  - Determining the length of a string is a common task in scripting. It involves finding the number of characters present in a given string, which can be useful for validation, formatting, or other string processing operations.
- **Pattern replacement**
  - Pattern replacement in shell scripting involves finding specific patterns within strings and substituting them with other strings. This is a fundamental text processing technique used to modify and transform data, allowing for tasks like cleaning up input, standardizing formats, or extracting relevant information.
- **Substring extraction**
  - Substring extraction involves selecting a portion of a string based on its position within the string. This is done by specifying the starting point and the length of the desired substring.
- **let**
  - The let command in Bash is used to perform arithmetic operations. It allows you to evaluate arithmetic expressions and assign the result to a variable.
- **awk**
  - Awk is a powerful text processing tool that can also perform numeric calculations. It reads input line by line and executes a set of instructions for each line.

### 2.11 Script Arguments
- **$***
  - $ is a special variable in shell scripting that expands to all the positional parameters (arguments) passed to a script or function. It represents all the arguments as a single string, with each argument separated by the first character of the IFS (Internal Field Separator) variable, which defaults to a space, tab, and newline.
- **$#**
  - $# is a special variable in shell scripting that represents the number of arguments passed to a script when it is executed. It's a simple integer value that allows you to determine how many inputs the user provided when running your script, enabling you to write logic that handles different scenarios based on the number of arguments.
- **$@**
  - $@ is a special variable in shell scripting that expands to all the positional parameters (arguments) passed to a script. Each argument is treated as a separate word, even if it contains spaces, ensuring that the script receives and processes each argument individually.
- **shift**
  - The shift command in shell scripting renames the command-line arguments. Specifically, it moves each argument one position to the left.

### 2.12 Exit Codes
- **Logical**
  - Logical operators in Bash are used to combine or modify conditional expressions. They allow you to create more complex tests within your scripts, enabling you to execute commands based on multiple conditions being true or false.
- **File test**
  - File test operators in Bash are used to check the type and attributes of files. These operators allow you to determine if a file exists, if it's a regular file or a directory, if it's readable, writable, or executable, and other file-related properties.
- **String operators**
  - String operators in Bash are symbols or keywords used to perform operations on strings, such as checking if a string is empty, comparing strings, extracting substrings, or determining the length of a string. These operators are essential for manipulating and evaluating string values within shell scripts, enabling conditional logic and data processing based on string content.
- **exit**
  - Exit codes are numerical values returned by a program or script upon completion. These codes signal whether the execution was successful or if any errors occurred.
- **$?**
  - Exit codes are numerical values returned by a program or script upon completion, signaling whether it executed successfully or encountered an error. The special variable $?
- **Success vs failure**
  - Exit codes are numerical values returned by a program or script upon completion, signaling whether it executed successfully or encountered an error. A zero (0) exit code typically indicates success, while any non-zero value signifies failure, with different non-zero codes often representing specific types of errors.

---

## 3. Advanced

### 3.1 File Permissions
- **rwx**
  - In Unix-like operating systems, file permissions control who can access and modify files and directories. The "rwx" notation represents the three fundamental permission types: "r" for read, allowing users to view the contents of a file or list the contents of a directory; "w" for write, allowing users to modify a file or create/delete files within a directory; and "x" for execute, allowing users to run a file as a program or enter a directory.
- **chmod**
  - chmod is a command-line utility used to change the access permissions of files or directories. These permissions determine who can read, write, or execute a file.
- **chown**
  - chown is a command-line utility used to change the ownership of files or directories. It allows you to modify the user and/or group associated with a file, effectively controlling who has access and what they can do with it.
- **chgrp**
  - chgrp is a command-line utility used to change the group ownership of a file or directory. It allows you to specify a new group that should be associated with the file, controlling which users have specific access rights based on group membership.

### 3.2 Conditionals
- **if**
  - The if statement in shell scripting allows you to execute different blocks of code based on whether a certain condition is true or false. It's a fundamental control flow mechanism that enables scripts to make decisions and behave differently depending on the input or state of the system.
- **case**
  - Case statements provide a way to execute different blocks of code based on the value of a variable or expression. They offer a structured alternative to multiple if-elif-else statements, making code more readable and maintainable when dealing with several possible conditions.

### 3.3 Loops
- **for**
  - A "for" loop is a control flow statement that allows you to repeatedly execute a block of code a specific number of times or for each item in a list. It's a fundamental programming construct used to automate repetitive tasks and iterate over collections of data.
- **until**
  - An until loop in shell scripting repeatedly executes a block of code as long as a specified condition is false. The loop continues to iterate until the condition becomes true, at which point the loop terminates.
- **while**
  - A while loop in shell scripting repeatedly executes a block of code as long as a specified condition remains true. It's a fundamental control flow statement that allows you to automate repetitive tasks based on a dynamic condition that can change during the loop's execution.
- **break, continue**
  - break and continue are control flow statements used within loops to alter their execution. The break statement immediately terminates the loop, transferring control to the next statement after the loop.
- **set -x**
  - set -x is a debugging tool used in shell scripts to trace the execution of commands. When enabled, the shell will print each command to standard error (stderr) before it is executed, preceded by a + symbol.
- **bash -n**
  - The bash -n option is a debugging tool that allows you to perform a syntax check on your Bash script without actually executing it. This is useful for identifying errors like typos, missing keywords, or incorrect syntax before running the script and potentially causing unintended consequences.
- **shellcheck**
  - Shellcheck is a static analysis tool for shell scripts. It helps identify and fix common syntax errors, semantic issues, and stylistic problems in your Bash/Shell scripts before you even run them.

### 3.4 Functions
- **Case conversion**
  - Case conversion involves changing the case of characters within a string. This typically means converting lowercase letters to uppercase, uppercase letters to lowercase, or applying title case (where the first letter of each word is capitalized).
- **Function Scopes**
  - Function scope determines the visibility and accessibility of variables within a function. In shell scripting, variables can have either global or local scope.
- **Recursive Functions**
  - Recursive functions are functions that call themselves within their own definition. This allows a function to repeat a process until a specific condition is met, breaking down a complex problem into smaller, self-similar subproblems.

### 3.5 Debugging
- **Bash Debug**
  - The Bash Debug extension for VS Code, powered by bashdb, allows you to debug Bash scripts directly within the VS Code editor. It provides features like breakpoints, stepping through code, inspecting variables, and evaluating expressions, making it easier to identify and fix errors in your Bash scripts.

### 3.6 Error Handling
- **set -e**
  - set -e is a shell command that instructs the shell to exit immediately if a command exits with a non-zero status. This is a way to ensure that your script stops executing as soon as an error occurs, preventing subsequent commands from running based on potentially incorrect or incomplete results.
- **set -o**
  - The set -o command in shell scripting is used to modify shell options, which control the behavior of the shell. These options can affect how the shell interprets commands, handles errors, and performs other tasks.
- **set -u**
  - The set -u command in shell scripting treats unset variables as an error. When this option is enabled, the script will exit immediately if it tries to use a variable that has not been assigned a value.
- **Error logging**
  - Error logging is the process of recording errors that occur during the execution of a script or program. This involves capturing information about the error, such as the type of error, the time it occurred, and the location in the code where it happened.
- **trap**
  - trap is a shell command used to specify actions to be taken upon receiving signals. Signals are notifications sent to a process to indicate an event, such as termination, interruption, or an error.
- **curl**
  - curl is a command-line tool used to transfer data with URLs. It supports various protocols like HTTP, HTTPS, FTP, and more, allowing you to download files, send data to servers, and interact with APIs directly from the command line.

### 3.7 Regular Expressions
- **Basic regex syntax**
  - Regular expressions (regex) are sequences of characters that define a search pattern. They are used to match, locate, and manipulate text based on patterns.
- **Extended regex**
  - Extended regular expressions (EREs) are a more powerful and flexible version of basic regular expressions. They offer additional metacharacters and features that simplify pattern matching and make complex searches easier to express.

### 3.8 Process Management
- **nohup**
  - nohup is a command-line utility used to run a command immune to hangups, with output redirected to a file. This allows a process to continue running in the background even after the user who started the process logs out or closes the terminal.
- **jobs**
  - In a shell environment, a job represents a process or a group of processes that are running in the background or foreground. The jobs command provides a way to list the currently active jobs, check their status (running, stopped, terminated), and manage them, such as bringing them to the foreground or terminating them.
- **disown**
  - disown is a shell built-in command used to remove jobs from the shell's job control. When you start a process in the background (using &), the shell keeps track of it.
- **fg, bg**
  - fg and bg are shell commands used to manage processes. bg moves a process to the background, allowing you to continue using the terminal while the process runs.
- **Process substitution**
  - Process substitution allows you to treat the output of a process as if it were a file. It achieves this by creating a temporary file (or using a pipe in some systems) and connecting the standard output of a command to it.
- **ps**
  - ps is a command-line utility that displays information about active processes running on a Linux or Unix-like operating system. It provides a snapshot of the current processes, including their process IDs (PIDs), resource usage, and other relevant details.
- **free**
  - free is a command-line utility used to display the amount of free and used physical and swap memory in a system. It provides a snapshot of the memory usage at a given point in time, showing total memory, used memory, free memory, shared memory, buffer/cache memory, and available memory.
- **top, htop**
  - top and htop are command-line utilities used for real-time system monitoring. They display a dynamic, ordered list of processes running on a system, along with information about CPU usage, memory consumption, and other system resources.
- **df, du**
  - df (disk free) and du (disk usage) are command-line utilities used to monitor disk space on Unix-like operating systems. df provides a summary of available and used disk space on mounted file systems, while du estimates the file space usage of files and directories.
- **ping**
  - Ping is a command-line utility used to test the reachability of a host on an Internet Protocol (IP) network. It works by sending Internet Control Message Protocol (ICMP) "echo request" packets to the target host and waiting for ICMP "echo reply" packets.
- **wget**
  - wget is a command-line utility used to retrieve files from the internet. It supports downloading files using HTTP, HTTPS, and FTP protocols.
- **scp**
  - scp, short for secure copy, is a command-line utility that allows you to securely transfer files between a local host and a remote host or between two remote hosts. It uses the SSH protocol for data transfer, ensuring that the data is encrypted during transmission, thus protecting it from eavesdropping.
- **ssh**
  - SSH (Secure Shell) is a cryptographic network protocol that enables secure communication between two computers over an insecure network. It's commonly used for remote command-line access, remote execution of commands, and secure file transfer.
- **rsync**
  - rsync is a command-line utility for efficiently transferring and synchronizing files between a computer and an external hard drive or across networked computers. It minimizes data transfer by only copying the differences between the source and destination, making it faster than simple copy commands, especially for large files or directories.

### 3.9 Package Management
- **uptime**
  - Uptime is a command-line utility that displays how long the system has been running. It provides a concise summary of the current time, how long the system has been up, the number of users currently logged in, and the system's load average over the past 1, 5, and 15 minutes.
- **iostat, vmstat**
  - iostat and vmstat are command-line utilities used for system monitoring. iostat reports CPU utilization and disk I/O statistics, providing insights into storage device performance.
- **ifconfig, ip**
  - ifconfig and ip are command-line utilities used to configure and manage network interfaces on Unix-like operating systems. They allow you to view, configure, and control network interfaces, including assigning IP addresses, setting network masks, and enabling or disabling interfaces.
- **netstat, ss**
  - netstat and ss are command-line tools used to display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. They provide insights into the network activity of a system, allowing users to diagnose network issues, monitor connections, and understand network traffic patterns.
- **brew**
  - Homebrew is a package manager for macOS (and Linux). It simplifies the installation of software on these operating systems by automating the process of downloading, compiling, and installing software packages from the command line.
- **apt**
  - apt (Advanced Package Tool) is a command-line package management system used primarily on Debian-based Linux distributions like Ubuntu. It simplifies the process of installing, updating, removing, and managing software packages by retrieving them from configured repositories and handling dependencies automatically.
- **dnf**
  - dnf is a package manager for RPM-based Linux distributions, serving as the successor to YUM (Yellowdog Updater, Modified). It is used to install, update, and remove software packages, as well as manage dependencies.
- **yum**
  - yum (Yellowdog Updater, Modified) is a command-line package management tool for systems using the RPM Package Manager. It automates the process of installing, updating, removing, and searching for software packages and their dependencies from configured repositories.
- **tar**
  - tar (Tape Archive) is a command-line utility in Unix-like operating systems used for archiving and extracting files. It combines multiple files into a single archive file, often referred to as a "tarball." While tar itself doesn't compress the archive, it's commonly used in conjunction with compression tools like gzip or bzip2 to create compressed archives (e.g., .tar.gz or .tar.bz2 files), reducing file size for storage or distribution.
- **gzip, gunzip**
  - gzip is a command-line utility used to compress files, reducing their size and making them easier to store or transmit. The compressed files typically have a .gz extension.
- **zip, unzip**
  - zip and unzip are command-line utilities used for compressing and decompressing files and directories. zip packages files into a single archive, reducing their size and making them easier to share or store.
- **bzip2, xz**
  - bzip2 and xz are command-line tools used for file compression in Unix-like operating systems. They reduce the size of files, making them easier to store and transfer.
- **cron, crontab**
  - cron is a time-based job scheduler in Unix-like operating systems. It allows users to schedule tasks (commands or scripts) to run automatically at specific times, dates, or intervals.
- **at**
  - The at command in Unix-like operating systems is used to schedule commands to be executed at a specific time. It allows you to specify a time and date, and then provide a command that will be run automatically at that designated time.
- **systemd timers**
  - Systemd timers are a systemd feature that allows you to schedule tasks to run at specific times or intervals, similar to cron. They provide a more flexible and powerful alternative to cron, offering features like dependency management, event-based activation, and integration with systemd's logging and service management capabilities.

---

## 4. Optional / Specialized Topics

- zsh
- PowerShell
- ksh
- cat
- touch
- find
- rm
- ls
- cd
- mkdir
- rmdir
- Error redirection
- tr
- sed
- sort
- uniq
- nl
- awk
- [...]
- {...}
- Running with Source
- Arithmetic expansion
- expr
- bc
- Comparison

---

## 5. References

- [Shell & Bash Roadmap](https://roadmap.sh/shell-bash)

---

## 6. Related Roles / Topics

### Related Roles
- Backend Developer
- Fullstack Developer
- DevOps Engineer

### Related Skills
- System Design
- Node.js