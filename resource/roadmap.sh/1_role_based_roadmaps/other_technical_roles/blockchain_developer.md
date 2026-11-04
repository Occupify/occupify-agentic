# Blockchain Developer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/blockchain
- Related Roles:
  - Software Architect
  - Frontend Developer
  - Backend Developer

---

## 1. Beginner

### 1.1 Introduction
- **Blockchain Structure**
  - A blockchain is essentially a distributed, immutable ledger composed of blocks chained together chronologically. Each block contains a batch of transactions, a timestamp, and a cryptographic hash of the previous block.
- **Applications and Uses**
  - Blockchain technology enables secure and transparent record-keeping across various sectors. It's used to track goods as they move through supply chains, ensuring authenticity and reducing fraud.
- **What is Blockchain**
  - A blockchain is essentially a digital ledger of transactions that is duplicated and distributed across a network of computers. Each transaction, or group of transactions, is recorded in a "block," and these blocks are linked together in a chronological chain.
- **Decentralization**
  - Decentralization means power and control are distributed, rather than held by a single entity. Imagine a group of friends managing a shared bank account; no single person can make changes without the others knowing and agreeing.
- **Why it matters?**
  - Blockchain technology provides a secure and transparent way to record and share information across a network. It works by grouping data into blocks, which are then cryptographically linked together in a chain.
- **Decentralization vs Trust**
  - Decentralization refers to the distribution of power and control away from a central authority. Trust, in this context, is the reliance on a third party or system to act honestly and reliably.
- **Cryptography & Hashing**
  - Cryptography is the art of secure communication. It involves techniques for encrypting messages, making them unreadable to anyone except the intended recipient who possesses the key to decrypt them.
- **EVM-Based**
  - The Ethereum Virtual Machine (EVM) is a dedicated software virtual stack that executes smart contract bytecode and is integrated into each Ethereum node. Simply said, EVM is a software framework that allows developers to construct Ethereum-based decentralized applications (DApps).
- **Blockchain Networks**
  - Blockchain networks are the underlying infrastructure that allows blockchains to operate. They are essentially distributed ledgers shared among multiple participants.

### 1.2 Understanding Blockchain
- **Basic Blockchain Operations**
  - Basic blockchain operations encompass the fundamental actions that allow a blockchain network to function. These operations include creating new blocks, adding transactions to blocks, verifying transactions, distributing the blockchain across the network, and reaching consensus on the state of the blockchain.
- **Ethereum**
  - Ethereum is an open-source, decentralized blockchain platform that establishes a peer-to-peer network for securely executing and verifying application code, referred to as smart contracts. It enables participants to transact with each other without a trusted central authority.
- **Polygon**
  - Polygon is a framework for building and connecting Ethereum-compatible blockchain networks. It aims to aggregate scalable solutions on Ethereum, supporting a multi-chain Ethereum ecosystem.
- **BNB Chain**
  - BNB Chain is a blockchain network created by Binance. It's designed for fast and low-cost transactions, and it supports smart contracts and decentralized applications (dApps).
- **Gnosis Chain**
  - Gnosis Chain is a blockchain that's compatible with the Ethereum Virtual Machine (EVM). This means it can run smart contracts and applications designed for Ethereum with relatively few changes.
- **Avalanche**
  - Avalanche is a high-throughput, open-source platform for launching decentralized finance (DeFi) applications and enterprise blockchain deployments in one interoperable, highly scalable ecosystem. It distinguishes itself through its unique consensus mechanism, which allows for faster transaction finality compared to many other blockchain networks.
- **Fantom**
  - Fantom is a directed acyclic graph (DAG) smart contract platform that provides decentralized, scalable, and secure services. It's designed to overcome the limitations of older blockchain technologies, particularly in terms of transaction speed and cost.
- **Moonbeam / Moonriver**
  - Moonbeam and Moonriver are developer-friendly blockchain environments designed to be compatible with Ethereum's tooling and ecosystem. Moonbeam operates as a smart contract parachain on the Polkadot network, while Moonriver serves as its "canary network" on Kusama, providing a real-world testing ground for new code.
- **BFT**
  - Byzantine Fault Tolerance (BFT) is a system's ability to function correctly even when some of its components fail or act maliciously by providing incorrect information. It addresses scenarios where nodes in a distributed network can exhibit arbitrary behavior, including lying, forging data, or simply not responding.
- **PoH**
  - Proof of History (PoH) is a consensus mechanism that creates a historical record to prove that an event occurred at a specific moment in time. It uses a verifiable delay function (VDF) to generate a sequence of computations that are difficult to parallelize, meaning they must be executed in a specific order.
- **PoS**
  - Proof of Stake (PoS) is a type of consensus mechanism used by blockchains to achieve agreement on the state of the network. In PoS systems, validators are chosen to create new blocks based on the number of tokens they "stake" or hold in the network.
- **PoW**
  - Proof-of-Work is a mechanism used to confirm transactions and add new blocks to a blockchain. It involves solving a complex computational puzzle, requiring significant processing power and time.
- **Consensus Protocols**
  - Consensus protocols are mechanisms that allow a distributed network of computers to agree on a single, consistent state of data. They ensure that all participants in the network can trust the information being shared, even when some participants might be unreliable or malicious.

### 1.3 Types of Blockchains
- **Mining & Incentive Models**
  - Mining, in the context of blockchain, is the process of validating new transactions and adding them to the blockchain. This is achieved by solving complex computational problems.
- **Blockchain Forking**
  - Blockchain forking happens when a blockchain diverges into two or more separate chains. This typically occurs when there's a change to the blockchain's protocol or software, and not all nodes agree on or adopt the new rules.
- **Cryptocurrencies**
  - Cryptocurrencies are digital or virtual currencies that use cryptography for security. They operate independently of a central bank and are often decentralized, meaning no single entity controls them.
- **Cryptowallets**
  - Cryptowallets are tools that allow users to manage, store, and transact with cryptocurrencies. They don't actually hold the cryptocurrency itself; instead, they store the private keys needed to access and control your digital assets on the blockchain.
- **Blockchain Interoperability**
  - Blockchain interoperability refers to the ability of different blockchains to communicate, share data, and transact with each other. It allows for the transfer of assets and information between otherwise isolated blockchain networks, creating a more connected and collaborative blockchain ecosystem.
- **Everscale**
  - Everscale is a layer-1 PoS blockchain network of the 5th generation. It is one of the most technologically advanced blockchain networks, and that is not a marketing exaggeration.
- **Gosh**
  - Gosh is a development platform that is purpose-built for securing the software supply chain and extracting the value locked in projects. It is the first blockchain-based platform for software development, which allows developers and businesses to create products in a familiar, straightforward, and safe way.
- **TON**
  - TON (The Open Network) is a fast and scalable layer-1 blockchain architecture designed for high transaction throughput and user accessibility. It aims to provide a platform for decentralized applications, instant payments, and secure communication.
- **Venom**
  - Venom Network is a next-generation, scalable Layer 0 blockchain designed for enterprise and Web3 use, featuring advanced dynamic sharding, Proof-of-Stake (PoS), and a unique architecture for high transaction speeds (150k+ TPS) and security, allowing for parallel processing of tasks like CBDCs, RWA tokenization, and dApps. It combines Layer 0 interoperability with Layer 1 execution, offering a hybrid approach for regulated environments
- **TVM-Based**
  - TVM-based blockchains execute smart contracts on a stack-based virtual machine rather than the Ethereum Virtual Machine. The most prominent example is the TON blockchain, whose Telegram Virtual Machine (TVM) uses its own bytecode and design, trading Ethereum-tooling compatibility for performance and unique contract capabilities.
- **L2 Blockchains**
  - Layer 2 blockchains are built on top of an existing blockchain (Layer 1) to improve scalability and efficiency. They handle transactions off-chain, reducing the burden on the main chain and allowing for faster and cheaper transactions.
- **Arbitrum**
  - Arbitrum is a Layer-2 scaling solution designed to improve the speed and reduce the costs of transactions on the Ethereum blockchain. It operates by executing transactions off-chain and then posting the results back to the main Ethereum chain, leveraging optimistic rollups to achieve higher throughput and lower gas fees compared to directly interacting with Ethereum.
- **Optimism**
  - Optimism is a Layer 2 scaling solution for Ethereum. It aims to improve transaction speeds and reduce costs on the Ethereum network by processing transactions off-chain and then bundling them back onto the main chain in a more efficient manner.
- **Storage**
  - Decentralized storage in blockchain involves distributing data across a network of computers instead of relying on a single, central server. Each computer in the network holds a piece of the overall data, making it more resistant to censorship, single points of failure, and data loss.
- **UTXO-Based**
  - UTXO-based blockchains utilize the Unspent Transaction Output (UTXO) model. In this model, each transaction consumes previous transaction outputs (UTXOs) as inputs and creates new UTXOs as outputs.
- **Bitcoin**
  - Bitcoin is a decentralized digital currency, meaning it operates without a central bank or single administrator. Transactions are verified by network nodes through cryptography and recorded in a public, distributed ledger called a blockchain.
- **Cardano**
  - Cardano is a third-generation, open-source, decentralized public blockchain and cryptocurrency project. It uses a proof-of-stake consensus mechanism called Ouroboros, designed to be more energy-efficient and scalable than proof-of-work systems.
- **Environmental Considerations**
  - Blockchain technology, particularly certain types like those using Proof-of-Work, can consume significant amounts of energy. This energy consumption stems from the computational power required to validate transactions and secure the network.

### 1.4 Smart Contracts
- **Solana**
  - Solana is a high-performance, open-source blockchain platform designed for speed and scalability. It aims to provide fast transaction speeds and low transaction costs, making it suitable for decentralized applications (dApps) and decentralized finance (DeFi) projects.
- **Solidity**
  - Solidity is a programming language specifically designed for writing smart contracts that run on the Ethereum blockchain. It's a high-level, contract-oriented language whose syntax is similar to JavaScript, C++, and Python, making it relatively accessible to developers familiar with these languages.
- **Vyper**
  - Vyper is a contract-oriented, Pythonic programming language that targets the Ethereum Virtual Machine (EVM). It's designed with security as a primary focus, aiming to make it harder to write insecure smart contracts.
- **Rust**
  - Rust is a multi-paradigm, high-level programming language focused on safety, speed, and concurrency. It achieves memory safety without garbage collection, making it suitable for systems programming and resource-constrained environments.
- **Unit Tests**
  - Unit tests are a way to check if individual parts of a program, like functions or modules, work correctly in isolation. They involve writing specific test cases that provide inputs to these parts and then verifying that the outputs match what's expected.
- **Integration Tests**
  - Integration tests verify that different units or components of an application work correctly together. They focus on testing the interactions between these components to ensure that data is passed correctly and that the overall system functions as expected when the parts are combined.
- **Code Coverage**
  - Code coverage is a metric that measures the extent to which the source code of a program is executed when a test suite is run. It helps identify areas of the code that are not being tested, potentially revealing bugs or vulnerabilities that might otherwise go unnoticed.
- **Deployment**
  - Smart contract deployment is the process of taking a smart contract, written in a language like Solidity, and making it live and executable on a blockchain network. This involves compiling the code into bytecode, paying a transaction fee (gas) to the network, and storing the contract's bytecode and initial state on the blockchain.
- **Monitoring**
  - Smart contract monitoring involves continuously observing and analyzing the activity and state of deployed smart contracts. This process helps identify potential issues, vulnerabilities, or unexpected behavior in real-time.
- **Upgrades**
  - Smart contract upgrades involve modifying or replacing existing smart contracts deployed on a blockchain. Since blockchains are immutable, directly altering a deployed contract is impossible.
- **ERC Tokens**
  - ERC tokens are a set of standards for creating tokens on the Ethereum blockchain. These standards define a common set of rules that tokens must follow, ensuring they can interact seamlessly with other applications and wallets within the Ethereum ecosystem.
- **Remix**
  - An integrated development environment is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.
- **Hardhat**
  - Hardhat is a development environment designed for Ethereum software. It helps developers manage and automate the tasks that are inherent to building smart contracts and decentralized applications (dApps), such as compiling, testing, debugging, and deploying smart contracts.
- **Brownie**
  - Brownie is a Python-based development and testing framework for smart contracts targeting the Ethereum Virtual Machine (EVM). It simplifies the process of writing, deploying, testing, and interacting with smart contracts by providing a suite of tools and libraries tailored for Python developers.
- **Truffle**
  - Truffle is a development environment, testing framework, and asset pipeline for blockchains using the Ethereum Virtual Machine (EVM). It provides tools for compiling, testing, and deploying smart contracts, making it easier for developers to build decentralized applications (dApps).
- **Foundry**
  - Foundry is a fast, portable, and modular toolkit for Ethereum application development. It's primarily used for writing, testing, and deploying smart contracts.
- **OpenZeppelin**
  - OpenZeppelin is a library of secure, reusable smart contracts for Ethereum and other blockchain platforms. It provides implementations of common standards like ERC-20 and ERC-721, as well as security tools and best practices to help developers build decentralized applications (dApps) safely and efficiently.
- **Go**
  - Go, often referred to as Golang, is a programming language known for its simplicity, efficiency, and strong support for concurrency. It's designed to be easy to learn and use, while also providing the performance needed for complex systems.
- **Base**
  - Base is an Ethereum Layer 2 (L2) blockchain developed by Coinbase. It's designed to offer a secure, low-cost, and developer-friendly environment for building decentralized applications (dApps).
- **Starknet**
  - Starknet is a permissionless, decentralized Layer 2 (L2) scaling solution that operates on top of Ethereum. It uses a technology called STARKs (Succinct Transparent ARguments of Knowledge) to bundle multiple transactions together and process them off-chain, before submitting a single proof of validity back to the Ethereum mainnet.
- **VS Code**
  - VS Code (Visual Studio Code) is a free and popular source code editor developed by Microsoft. It's used by developers for writing, debugging, and managing code across various programming languages.

---

## 2. Intermediate

### 2.1 Security
- **Crypto Wallets**
  - Crypto wallets are tools that allow users to manage and interact with their cryptocurrencies. They don't actually store the crypto themselves; instead, they store the private keys needed to access and control your digital assets on the blockchain.
- **Crypto Faucets**
  - Crypto faucets are websites or apps that distribute small amounts of cryptocurrency as a reward for completing simple tasks. These tasks can include things like solving captchas, watching ads, or playing games.
- **Decentralized Storage**
  - Decentralized storage is where data is stored on a decentralized network across multiple locations by users or groups who are incentivized to join, store, and keep data accessible. The servers used are hosted by people, rather than a single company.
- **Practices**
  - Security practices are the established methods, procedures, and guidelines implemented to protect systems, data, and assets from unauthorized access, use, disclosure, disruption, modification, or destruction. These practices encompass a wide range of measures, including access controls, encryption, vulnerability management, incident response, and security awareness training, all designed to minimize risks and maintain confidentiality, integrity, and availability.
- **Slither**
  - Slither is a static analysis tool for Solidity smart contracts. It analyzes code without executing it, identifying potential vulnerabilities, bugs, and code inefficiencies.
- **Diligent Fuzzing**
  - Manticore is a symbolic execution tool used for analyzing smart contracts and binary programs. It works by exploring all possible execution paths of a program, identifying potential vulnerabilities like integer overflows, underflows, and other security flaws.
- **Echidna**
  - Echidna is a Haskell program designed for fuzzing/property-based testing of Ethereum smart contracts. It generates random sequences of calls to the contract and checks if certain user-defined properties hold true after each sequence.
- **Git**
  - Git is a distributed version control system that tracks changes to files in a project over time. It allows multiple developers to collaborate on the same codebase simultaneously, managing different versions and merging changes efficiently.
- **GitHub**
  - GitHub is a web-based platform that provides hosting for software development and version control using Git. It allows developers to collaborate on projects, track changes to code, and manage different versions of their work.
- **GitLab**
  - GitLab is a web-based DevOps platform that provides a Git repository manager offering features like issue tracking, CI/CD pipelines, and more. It allows developers to collaboratively work on code, manage projects, and automate the software development lifecycle from planning to deployment.
- **Bitbucket**
  - Bitbucket is a web-based version control repository hosting service owned by Atlassian, the same company that makes Jira and Confluence. It's primarily used for source code management and collaborative development, allowing teams to store, track, and manage changes to their code.

### 2.2 Supporting Languages
- **Fuzz Testing & Static Analysis**
  - Fuzz testing involves providing invalid, unexpected, or random data as input to a program to identify potential vulnerabilities and bugs. Static analysis, on the other hand, examines the source code of a program without actually executing it, looking for potential errors, security flaws, and coding standard violations.
- **Common Threat Vectors**
  - Smart contracts, while powerful, are susceptible to various vulnerabilities that attackers can exploit. These weaknesses, known as threat vectors, can lead to loss of funds, data manipulation, or denial of service.
- **Source of Randomness Attacks**
  - The security of cryptographic systems depends on some secret data that is known to authorized persons but unknown and unpredictable to others. To achieve this unpredictability, some randomization is typically employed.
- **JavaScript**
  - JavaScript is a programming language that makes websites interactive. It's what allows buttons to work, animations to play, and data to be updated without reloading the page.
- **Python**
  - Python is a versatile and widely-used programming language known for its clear syntax and extensive libraries. It's a great choice for building decentralized applications (dApps) because it simplifies complex tasks like interacting with blockchain networks, handling data, and creating smart contracts.

### 2.3 Oracles
- **Hybrid Smart Contracts**
  - Hybrid smart contracts combine the benefits of blockchain-based smart contracts with external data and computation. They leverage on-chain code for core logic and security, while using off-chain oracles to access real-world information and perform complex computations that are impractical or impossible to execute directly on the blockchain.
- **Chainlink**
  - Chainlink is a decentralized oracle network that provides real-world data to smart contracts on a blockchain. It acts as a bridge, securely connecting blockchains to external data sources, APIs, and payment systems.
- **Oracle Networks**
  - Oracle networks are groups of independent oracles that work together to provide data to a blockchain. Instead of relying on a single source of information, these networks aggregate data from multiple oracles, enhancing reliability and security.

### 2.4 Frontend Frameworks
- **React**
  - React is a JavaScript library for building user interfaces. It allows developers to create reusable UI components and efficiently update and render them based on data changes.

### 2.5 Client Libraries
- **Angular**
  - Angular is a TypeScript-based, open-source web application framework led by the Angular Team at Google. It provides a structured way to build dynamic web applications, using components, templates, and dependency injection.
- **Vue**
  - Vue.js is a progressive JavaScript framework used for building user interfaces and single-page applications. It focuses on the view layer, making it easy to integrate into existing projects or build complex applications from scratch.
- **web3.js**
  - web3.js is a collection of JavaScript libraries that allows you to interact with a local or remote Ethereum node using HTTP, WebSocket, or IPC. It provides a set of functions to interact with smart contracts on the Ethereum blockchain, send transactions, read blockchain data, and manage Ethereum accounts.
- **Moralis**
  - Moralis is a development platform that simplifies the process of building decentralized applications (dApps). It provides a suite of tools and infrastructure, including a managed backend, authentication, and real-time data synchronization, allowing developers to focus on the front-end user experience and smart contract logic rather than managing complex server-side infrastructure.

### 2.6 dApps
- **Testing**
  - Testing decentralized applications (dApps) involves verifying that the smart contracts and user interfaces function correctly and securely. This process ensures that the dApp behaves as expected under various conditions, including normal usage, edge cases, and potential attacks.
- **Deployment**
  - Deployment refers to the process of making a decentralized application (dApp) accessible and functional for users. This involves taking the code, smart contracts, and user interface components and placing them on the appropriate networks and servers so that users can interact with the dApp.
- **Maintenance**
  - dApps can be harder to maintain because the code and data published to the blockchain is harder to modify. It’s hard for developers to make updates to their dapps (or the underlying data stored by a dapp) once they are deployed, even if bugs or security risks are identified in an old version.
- **Architecture**
  - Traditional web applications typically rely on a centralized server to handle data storage, logic, and user authentication. In contrast, decentralized applications (dApps) shift these responsibilities to a decentralized network, often a blockchain.
- **Security**
  - Decentralized applications (dApps) face unique security risks because they run on a blockchain and interact with smart contracts. Common vulnerabilities include flaws in smart contract code that can be exploited to drain funds, front-running where malicious actors take advantage of pending transactions, and phishing attacks targeting users' private keys.
- **State & Payment Channels**
  - State channels and payment channels are techniques used to improve the scalability and efficiency of blockchain transactions. They allow participants to conduct multiple transactions off-chain, only interacting with the main blockchain to open and close the channel.

---

## 3. Advanced

### 3.1 Client Nodes
- **ethers.js**
  - Ethers.js is a JavaScript library that simplifies interacting with the Ethereum blockchain and its ecosystem. It provides a complete and well-tested set of tools for developers to create and deploy smart contracts, send transactions, and interact with blockchain data.
- **Geth**
  - Geth, short for Go Ethereum, is a command-line interface for running a full Ethereum node implemented in the Go programming language. It allows you to interact with the Ethereum blockchain, mine Ether, create and deploy smart contracts, and inspect block and transaction data.
- **Besu**
  - Besu is an open-source Ethereum client designed for both public and private blockchain networks. It allows users to connect to and interact with Ethereum-based blockchains, executing smart contracts and participating in network consensus.

### 3.2 Building for Scale
- **Optimistic Rollups & Fraud Proofs**
  - Optimistic rollups are a layer-2 scaling solution for blockchains that bundle multiple transactions together and post them to the main chain as a single transaction. The "optimistic" part means that these bundled transactions are assumed to be valid unless proven otherwise.
- **Zk Rollups & Zero Knowledge Proof**
  - Zero-knowledge proofs (ZKPs) are a cryptographic method where one party (the prover) can prove to another party (the verifier) that a statement is true, without revealing any information beyond the validity of the statement itself. ZK-rollups leverage this technology to bundle multiple transactions into a single batch, which is then verified using a ZKP on the main blockchain.
- **Validium**
  - Validium is a type of layer-2 scaling solution for blockchains that processes transactions off-chain and posts only validity proofs on the main chain. Unlike other scaling solutions, Validium uses external data availability, meaning the transaction data is not stored on the main chain or by the validators of the layer-2 network itself, but by a separate entity.
- **Plasma**
  - Plasma is a framework for building scalable decentralized applications (dApps) on top of a parent blockchain, like Ethereum. It essentially creates "child chains" that operate independently but are anchored to the main chain for security.
- **Sidechains**
  - Sidechains are separate blockchains that are linked to a main blockchain (often called the "mainchain" or "parent chain"). They operate independently but can communicate with the mainchain, allowing assets and data to be transferred between them.
- **Ethereum 2.0**
  - Ethereum 2.0, also known as Serenity, represents a major upgrade to the Ethereum blockchain. It transitions the network from a Proof-of-Work (PoW) consensus mechanism to a Proof-of-Stake (PoS) system called Casper, aiming to improve scalability, security, and sustainability.
- **On-Chain Scaling**
  - On-chain scaling refers to methods of increasing a blockchain's transaction processing capacity directly within the blockchain's own architecture. This involves modifications to the blockchain's core rules, such as increasing the block size or changing the consensus mechanism, to allow for more transactions to be processed in a given time period.

### 3.3 Applicability
- **Defi**
  - Decentralized Finance (DeFi) refers to financial services built on blockchain technology, primarily using smart contracts. These services aim to replicate traditional financial systems like lending, borrowing, trading, and insurance, but in a decentralized and often permissionless manner.
- **DAOs**
  - DAOs, or Decentralized Autonomous Organizations, are essentially internet-native organizations governed by rules encoded as computer programs (smart contracts) on a blockchain. These rules dictate how the organization operates, and decisions are made through proposals and voting by DAO members, often using tokens that represent ownership or voting rights.
- **NFTs**
  - NFTs, or Non-Fungible Tokens, are unique digital assets that represent ownership of items. These items can be anything digital, like artwork, music, or virtual real estate, or even real-world assets.
- **Nethermind**
  - Nethermind is a software client for the Ethereum blockchain, written in C#/.NET. It allows developers to interact with the Ethereum network, execute smart contracts, and build decentralized applications (dApps).
- **Substrate**
  - Substrate is a modular framework for building blockchains. It provides a set of pre-built components and libraries that developers can use to create custom blockchains tailored to specific needs, rather than building everything from scratch.

### 3.4 Node as a Service
- **Payments**
  - Payments within decentralized applications (dApps) involve using cryptocurrencies or tokens to exchange value directly between users or between users and the dApp itself, without relying on traditional intermediaries like banks. This enables faster, more transparent, and often cheaper transactions compared to conventional payment systems.
- **Insurance**
  - Insurance dApps can streamline and automate various insurance processes. For example, claims processing can be automated using smart contracts that trigger payouts when specific conditions are met, verified by oracles providing external data.
- **Alchemy**
  - Alchemy is a platform that provides developers with the infrastructure and tools needed to build and scale decentralized applications (dApps). It simplifies the process of interacting with blockchain networks by offering reliable and scalable APIs, enhanced monitoring, and developer tools that abstract away the complexities of running and maintaining blockchain nodes.
- **Infura**
  - Infura provides a suite of tools and infrastructure that allows developers to easily connect to the Ethereum and IPFS networks. It essentially acts as a gateway, handling the complexities of running and maintaining blockchain nodes.
- **Pokt Network**
  - Moralis is a development platform that simplifies the process of building decentralized applications (dApps). It provides a set of tools and infrastructure that handle the backend complexities, allowing developers to focus on the frontend user experience and smart contract logic.
- **Quicknode**
  - QuickNode is a platform that provides infrastructure and tools for developers to build and run blockchain applications. It simplifies the process of connecting to blockchain networks by offering pre-configured nodes and APIs, eliminating the need for developers to set up and manage their own blockchain infrastructure.

---

## 4. Optional / Specialized Topics

- Solana
- Everscale
- Gosh
- TON
- Venom
- TVM-Based
- Vyper
- Rust
- Hardhat
- Brownie
- Truffle
- Diligent Fuzzing
- Echidna
- GitLab
- Bitbucket
- Payments
- Insurance
- Python
- Go
- Angular
- Vue
- web3.js
- Moralis
- VS Code

---

## 5. References

- [Blockchain Developer Roadmap](https://roadmap.sh/blockchain)

---

## 6. Related Roles / Topics

### Related Roles
- Software Architect
- Frontend Developer
- Backend Developer

### Related Skills
- Computer Science
- Linux
- Node.js