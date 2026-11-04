# Network Engineer

## Metadata
- Type: Role
- Domain: DevOps & Cloud Infrastructure
- Source: roadmap.sh
- Source URL: https://roadmap.sh/network-engineer
- Related Roles:
  - MLOps Engineer
  - Cyber Security Specialist
  - Frontend Developer

---

## 1. Beginner

### 1.1 Introduction
- **How does the Internet Work?**
  - The Internet is a massive global network of interconnected computers and devices that communicate by sending data to each other using a shared set of rules. When you visit a website, your device sends a request that travels through multiple routers and networks until it reaches the server hosting that site, which then sends the data back to your screen.
- **Client**
  - A client is any device or software application that sends requests to a server to access resources or services. In everyday terms, your web browser acts as a client when it asks a web server to load a page.
- **Host**
  - A host is any device connected to a network that has an IP address and can send or receive data. This includes computers, servers, printers, smartphones, and any other networked device.
- **Frame**
  - A frame is a unit of data transmission at the Data Link layer of the OSI model. It wraps raw bits into a structured format that includes source and destination MAC addresses, the data payload, and error-checking information.
- **Latency**
  - Latency is the time it takes for a data packet to travel from its source to its destination, usually measured in milliseconds. Low latency means data arrives quickly, which is critical for real-time applications like video calls and online gaming.
- **Server**
  - A server is a computer or software system that listens for requests from clients and responds by providing resources, data, or services. Servers can host websites, store files, manage emails, or run applications that many users access simultaneously.
- **Package**
  - In networking, a package (or packet) is a small chunk of data broken off from a larger message for transmission across a network. Each packet travels independently through the network and is reassembled at the destination.
- **Bandwidth**
  - Bandwidth refers to the maximum amount of data that can be transmitted over a network connection in a given amount of time, typically measured in bits per second (bps). Higher bandwidth means more data can flow simultaneously, which generally results in faster network performance.
- **Throughput**
  - Throughput is the actual amount of data successfully transferred over a network in a given period of time, as opposed to the theoretical maximum that bandwidth represents. While bandwidth is the capacity of a network link, throughput reflects real-world performance after accounting for packet loss, latency, and protocol overhead.
- **Protocol**
  - A protocol is a set of rules that defines how data is formatted, transmitted, and received between devices on a network. Protocols ensure that different systems, regardless of manufacturer or operating system, can predictably communicate with each other.
- **Socket**
  - A socket is the combination of an IP address and a port number, forming a unique endpoint for network communication. When two devices establish a connection, each end uses a socket to send and receive data, creating a two-way communication channel.
- **Port**
  - A port is a numerical identifier used to direct network traffic to a specific application or service running on a device. While an IP address identifies the device, the port number identifies which program on that device should handle the incoming data.
- **IP Address**
  - An IP address is a numerical label assigned to each device on a network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host and providing its location in the network for routing purposes.
- **CCNP**
  - CCNP (Cisco Certified Network Professional) is an intermediate-level professional certification that validates a candidate's ability to plan, implement, verify, and troubleshoot local and wide-area enterprise networks. It focuses on advanced core technologies, including routing, switching, security, automation, and programmable network solutions.
- **CompTIA Network+**
  - The CompTIA Network+ is a highly sought-after certification for IT professionals who aim to build a solid foundation in networking concepts and practices. This certification is vendor-neutral, meaning that it covers a broad range of knowledge that can be applied to various network technologies, products, and solutions.
- **CCNA**
  - The Cisco Certified Network Associate (CCNA) certification is an entry-level certification for IT professionals who want to specialize in networking, specifically within the realm of Cisco products. This certification validates an individual's ability to install, configure, operate, and troubleshoot medium-sized routed and switched networks.
- **CompTIA Security+**
  - CompTIA Security+ is a global certification that establishes the baseline knowledge required to perform core security functions and pursue an IT security career. It covers foundational principles of network security, including threat identification, risk management, cryptography, and identity and access management.
- **Cloud Certifications**
  - Cloud certifications are professional credentials that validate an individual's ability to design, deploy, and manage scalable infrastructure and services on platforms like AWS, Microsoft Azure, and Google Cloud. These programs cover essential technical competencies, including virtual networking, identity and access management, storage solutions, and security configurations within public and hybrid cloud environments.

### 1.2 What are Networks?
- **LAN**
  - A LAN, or Local Area Network, is a network that connects devices within a limited geographic area, such as a home, office, or building. LANs typically use Ethernet cables or Wi-Fi to link computers, printers, and other devices, allowing them to share files and resources at high speeds.
- **MAN**
  - A MAN, or Metropolitan Area Network, is a network that covers a geographic area roughly the size of a city or a large campus. It is larger than a LAN but smaller than a WAN, often used by organizations or service providers to connect multiple buildings or locations within the same metropolitan region.
- **PAN**
  - A PAN, or Personal Area Network, is a small network designed for communication between devices in proximity to a single person, typically within a range of a few meters. Examples include connecting a smartphone to wireless earbuds via Bluetooth or linking a laptop to a smartwatch.
- **VPN**
  - A VPN, or Virtual Private Network, creates an encrypted tunnel between a device and a remote network over the public Internet, allowing secure communication as if the device were directly connected to that network. Organizations use VPNs to let remote employees securely access internal resources, while individuals use them for privacy and to bypass geographic content restrictions.
- **Transmission Media Types**
  - Transmission media refers to the physical or wireless channels through which data travels between devices. Wired media includes twisted pair cables (like Ethernet), coaxial cables, and fiber optic cables, each with different speeds, ranges, and interference characteristics.
- **WAN**
  - A WAN, or Wide Area Network, is a network that spans a large geographic area, often connecting multiple LANs across cities, countries, or continents. The Internet itself is the largest example of a WAN.
- **WLAN**
  - A WLAN, or Wireless Local Area Network, is a type of LAN that uses wireless radio signals instead of cables to connect devices. It is the technology behind Wi-Fi networks found in homes, offices, and public spaces.
- **SAN**
  - A SAN, or Storage Area Network, is a specialized high-speed network that provides block-level access to shared storage devices such as disk arrays and tape libraries. Unlike a regular network where files are shared, a SAN makes storage appear as locally attached to the servers that use it, enabling fast and reliable data access.
- **Cloud**
  - In networking, the cloud refers to a model of delivering computing resources, such as servers, storage, databases, and networking, over the Internet on a pay-as-you-go basis. Rather than owning and maintaining physical infrastructure, organizations can provision and scale resources through cloud providers like AWS, Azure, or Google Cloud.
- **Client-Server Network**
  - A client-server network is a model where one or more central servers provide resources or services, and multiple client devices request and consume those resources. The server manages shared resources such as files, databases, or applications, while clients interact with them through the network.
- **Mac Address**
  - A MAC address, or Media Access Control address, is a unique hardware identifier assigned to a network interface card (NIC) by its manufacturer. It operates at the Data Link layer and is used to identify devices within the same local network segment.
- **ARP**
  - ARP, or Address Resolution Protocol, is used to map an IP address to a physical MAC address on a local network. When a device wants to communicate with another device on the same network, it uses ARP to discover which MAC address corresponds to a known IP address.
- **TCP**
  - TCP (Transmission Control Protocol) sets up a connection between two devices before sending any data, then makes sure every piece of data arrives in order and without errors. It splits data into segments, numbers them, and asks for retransmission if a segment gets lost or corrupted.
- **UDP**
  - UDP (User Datagram Protocol) sends data without setting up a connection first and without checking whether it arrives. It skips the overhead of acknowledgments and retransmissions, which makes it faster than TCP but less reliable.
- **ICMP**
  - ICMP (Internet Control Message Protocol) carries diagnostic and error messages between devices on a network, rather than application data. Routers and hosts use it to report problems like an unreachable destination or an expired packet, and tools like ping and traceroute rely on it directly.

### 1.3 Network Devices
- **Routers**
  - A router is a network device that forwards data packets between different networks, directing traffic based on IP addresses. It determines the best path for data to travel from source to destination, making routing decisions using routing tables and protocols.
- **Switches**
  - A switch is a network device that connects multiple devices within the same local network and forwards data based on MAC addresses. Unlike a hub, a switch sends data only to the specific device it is intended for, making communication more efficient and reducing unnecessary network traffic.
- **Hub**
  - A hub is a basic network device that connects multiple devices in a LAN and broadcasts incoming data to all connected ports, regardless of the intended recipient. This makes hubs simple but inefficient, as all devices receive all traffic, even if it is not meant for them.
- **Access Points**
  - A wireless access point (AP) is a device that creates a wireless local area network, typically in an office or large building, by connecting to a wired router or switch and broadcasting a Wi-Fi signal. Multiple access points can be deployed across a large area to extend wireless coverage and allow devices to roam seamlessly.
- **Modems**
  - A modem (modulator-demodulator) is a device that converts digital data from a computer into a format suitable for transmission over a communication medium such as telephone lines or cable, and vice versa. It serves as the bridge between your local network and your Internet Service Provider's infrastructure.
- **Peer-to-Peer Network**
  - A peer-to-peer (P2P) network is one where each device, or peer, can act as both a client and a server, sharing resources directly with other devices without a central server. This model is simpler and cheaper to set up than a client-server network, making it common in small home networks or applications like file sharing.
- **HTTP / HTTPS**
  - HTTP (HyperText Transfer Protocol) is the foundation of data communication on the web, defining how messages are formatted and transmitted between browsers and servers. HTTPS is the secure version of HTTP, adding an SSL/TLS encryption layer to protect data from being intercepted during transmission.
- **SSL / TLS**
  - SSL (Secure Sockets Layer) and its successor TLS (Transport Layer Security) are cryptographic protocols designed to provide secure communication over a network. They work by encrypting the data exchanged between a client and a server, verifying the identity of the parties involved through digital certificates.
- **FTP / SFTP**
  - FTP (File Transfer Protocol) is a standard protocol used to transfer files between a client and a server over a network. It operates over two channels (one for commands and one for data), but transmits information in plain text, making it insecure.
- **SSH**
  - SSH, or Secure Shell, is a network protocol that provides a secure, encrypted channel for remotely accessing and managing devices over an unsecured network. It replaces older, insecure protocols like Telnet by encrypting all communication between the client and the server.
- **NTP**
  - NTP, or Network Time Protocol, is used to synchronize the clocks of computers and network devices over a network. Accurate timekeeping is essential for logging events, coordinating distributed systems, and ensuring security certificates work correctly.
- **SNTP**
  - SNTP, or Simple Network Time Protocol, is a simplified version of NTP used to synchronize device clocks over a network. It is less precise than full NTP but requires fewer resources, making it suitable for devices that do not need highly accurate timekeeping.
- **DHCP**
  - DHCP, or Dynamic Host Configuration Protocol, is a network management protocol that automatically assigns IP addresses and other network configuration parameters to devices when they join a network. Without DHCP, administrators would need to manually configure the IP address, subnet mask, gateway, and DNS settings on every device.
- **SMTP / IMAP**
  - SMTP (Simple Mail Transfer Protocol) is the protocol used to send emails from a client to a server or between mail servers. IMAP (Internet Message Access Protocol) is used by email clients to retrieve and manage messages stored on a mail server, allowing access from multiple devices while keeping messages synchronized.
- **DNS**
  - DNS, or Domain Name System, is the system that translates human-readable domain names like www.example.com into IP addresses that computers use to identify each other on the network. Without DNS, users would need to memorize IP addresses to visit websites or access online services.
- **WebSocket**
  - WebSocket is a communication protocol that provides a persistent, full-duplex connection between a client and a server over a single TCP connection. Unlike traditional HTTP requests where the client must initiate every interaction, WebSockets allow for continuous, real-time data exchange in both directions once the initial handshake is complete.

### 1.4 OSI Model
- **Physical**
  - The Physical layer is the first and lowest layer of the OSI model, responsible for the actual transmission of raw bits over a physical medium such as copper cables, fiber optics, or radio waves. It defines the electrical, mechanical, and timing specifications for hardware components like network cables, connectors, and network interface cards.
- **Transport**
  - The Transport layer is the fourth layer of the OSI model, responsible for end-to-end communication, data flow control, and error recovery between applications on different hosts. It breaks data into segments, ensures they are delivered reliably and in order, and manages retransmission if packets are lost.
- **Data Link**
  - The Data Link layer is the second layer of the OSI model, responsible for node-to-node data transfer and error detection within a single network segment. It organizes raw bits from the Physical layer into frames and uses MAC addresses to identify devices on the local network.
- **Network**
  - The Network layer is the third layer of the OSI model, responsible for logical addressing and routing data packets between devices across different networks. It uses IP addresses to determine the best path for data to travel from source to destination.
- **Cloudflare**
  - Cloudflare's DNS resolver, known by its address 1.1.1.1, is a public DNS service focused on speed and privacy. It is consistently ranked among the fastest DNS resolvers in the world and does not log user queries for advertising purposes.
- **Google**
  - Google Public DNS is a global Domain Name System (DNS) resolution service that translates human-readable domain names into numerical IP addresses. It functions as a recursive name server, allowing users and network devices to perform lookups more efficiently by leveraging Google's massive infrastructure for faster responses and enhanced security.
- **OpenDNS**
  - OpenDNS is a cloud-based DNS service operated by Cisco that provides fast DNS resolution along with additional security and filtering features. It can block access to malicious websites, phishing domains, and unwanted content categories before a connection is ever established.
- **Quad9**
  - Quad9 is a free, public DNS resolver that focuses on security by blocking access to known malicious domains at the DNS level. It uses threat intelligence from multiple cybersecurity partners to identify and block harmful websites before a connection is made, without logging personally identifiable information.

### 1.5 TCP/IP Model
- **Session**
  - The Session layer is the fifth layer of the OSI model, responsible for establishing, managing, and terminating communication sessions between applications. It handles synchronization and dialog control, ensuring that data exchanges are organized and that sessions can be paused and resumed if needed.
- **Presentation**
  - The Presentation layer is the sixth layer of the OSI model, responsible for translating data between the format used by the application and the format used for network transmission. It handles tasks such as data encryption and decryption, compression, and character encoding.
- **Application**
  - The Application layer is the seventh and topmost layer of the OSI model, where end-user software interacts with the network. It provides network services directly to applications, enabling functions like web browsing, email, file transfer, and domain name resolution.
- **Network Access**
  - The Network Access layer is the lowest layer of the TCP/IP model, combining the functions of the OSI Physical and Data Link layers. It handles how data is physically transmitted over the network medium, including framing, MAC addressing, and hardware-level error detection.
- **Internet**
  - The Internet layer of the TCP/IP model corresponds to the Network layer of the OSI model and is responsible for logical addressing and routing packets across networks. The primary protocol at this layer is IP (Internet Protocol), which assigns addresses to packets and determines how they are routed toward their destination.
- **Transport**
  - The Transport layer of the TCP/IP model is responsible for end-to-end communication between applications on different hosts. It uses TCP for reliable, ordered delivery and UDP for faster, connectionless communication where some data loss is acceptable.

### 1.6 Network Design Principles
- **Two-Tier**
  - The two-tier architecture, also called the collapsed core design, organizes a network into two layers: the distribution layer and the access layer. The distribution layer handles routing, policy enforcement, and inter-VLAN communication, while the access layer connects end devices like computers, phones, and printers to the network.
- **Three-Tier**
  - The three-tier architecture organizes a network into three distinct layers: the core, distribution, and access layers. The core layer provides high-speed backbone connectivity between distribution blocks and is optimized purely for fast packet forwarding with no policy enforcement.
- **Spine-Leaf**
  - Spine-leaf is a two-tier data center network architecture designed to provide consistent, low-latency connectivity between servers and storage in modern data centers. Every leaf switch connects to every spine switch, and no leaf connects directly to another leaf.
- **Design Best Practices**
  - Network design best practices are a set of proven principles that engineers follow to build networks that are reliable, secure, and maintainable over time. Key practices include designing for redundancy at every layer to eliminate single points of failure, keeping the design as simple as possible since complexity increases the chance of misconfiguration and makes troubleshooting harder, segmenting the network using VLANs and subnets to limit broadcast domains and contain security incidents, documenting everything from IP address assignments to device configurations, and designing with scalability in mind so the network can grow without requiring a fundamental redesign.

### 1.7 Network Simulators
- **Cisco Packet Tracer**
  - Cisco Packet Tracer is a visual simulation and modeling tool that allows users to design, configure, and troubleshoot network topologies without the need for physical hardware. It provides a drag-and-drop interface where you can place virtual routers, switches, and end devices, and then execute Cisco IOS commands to test network connectivity and protocols.
- **GNS3**
  - GNS3 is a graphical network simulation software that allows users to design, configure, and test complex network topologies in a virtual environment. It works by combining real Cisco IOS images or open-source network operating systems with virtual machines to emulate hardware behavior, enabling engineers to build lab environments without the need for physical equipment.
- **EVE-NG**
  - EVE-NG (Emulated Virtual Environment - Next Generation) is a multi-vendor network emulation platform that allows users to create virtual network topologies. It runs as a virtual machine on a server, enabling engineers to drag and drop various virtual appliances, such as routers, switches, and firewalls, into a workspace to simulate complex enterprise environments.

### 1.8 Linux for Networking
- **Shell & Scripting**
  - The shell is the command-line interface used to interact with a Linux system, while scripting is the practice of combining shell commands into reusable files called scripts. For network engineers, shell scripting helps automate repetitive tasks such as backing up device configurations, parsing log files, running diagnostic checks across multiple devices, and generating reports.
- **Static vs Dynamic NAT**
  - Static NAT creates a permanent, one-to-one mapping between a specific private IP address and a specific public IP address, ensuring that a device always appears on the Internet with the same public IP. It is commonly used for servers that need to be consistently reachable from outside the network, such as web servers or mail servers hosted internally.
- **PAT/NAT Overload**
  - PAT, or Port Address Translation, also called NAT Overload, is the most common form of NAT used in home and enterprise networks. It allows many devices with private IP addresses to share a single public IP address simultaneously by tracking each connection using a unique combination of the public IP address and a port number.
- **NAT64**
  - NAT64 is a transition mechanism that allows IPv6-only devices to communicate with IPv4-only servers and services by translating between the two address formats at the network boundary. As the Internet continues its gradual migration from IPv4 to IPv6, NAT64 bridges the gap during the transition period, ensuring that devices operating exclusively on IPv6 networks are not cut off from the large portion of the Internet that still runs on IPv4.

### 1.9 IP Addressing
- **IPv4 vs IPv6**
  - IPv4 is the original version of the Internet Protocol, using 32-bit addresses written in dotted decimal notation (e.g., 192.168.1.1), allowing for about 4.3 billion unique addresses. IPv6 was introduced to solve the problem of IPv4 address exhaustion, using 128-bit addresses written in hexadecimal (e.g., 2001:0db8::1), providing an astronomically larger address space.
- **Public vs Private Addresses**
  - Public IP addresses are globally unique addresses assigned by Internet Service Providers and are reachable over the Internet. Private IP addresses are reserved for use within local networks and are not routable on the public Internet (ranges like 192.168.x.x, 10.x.x.x, and 172.16.x.x are commonly used internally).
- **IP vs MAC vs ARP**
  - An IP address is a logical address used to identify a device across networks and is assigned by software, while a MAC address is a physical address burned into the network interface hardware, used for communication within a local network segment. ARP (Address Resolution Protocol) bridges the two by resolving a known IP address to its corresponding MAC address so that data can be delivered on the local network.
- **NAT vs PAT**
  - NAT, or Network Address Translation, is a method used by routers to map private IP addresses on a local network to a single public IP address before traffic leaves for the Internet. This allows many devices to share one public IP, which helps conserve the limited pool of available IPv4 addresses.

---

## 2. Intermediate

### 2.1 Subnetting
- **Subnet Masks**
  - A subnet mask is a 32-bit number used alongside an IP address to determine which portion of the address identifies the network and which portion identifies the individual host. It works by applying a bitwise AND operation with the IP address to extract the network address.
- **CIDR**
  - CIDR, or Classless Inter-Domain Routing, is a method of allocating IP addresses and routing that replaced the older class-based system. Instead of fixed classes (A, B, C), CIDR uses a slash notation (e.g., 192.168.1.0/24) to indicate how many bits are used for the network portion of the address.
- **VLSM**
  - VLSM, or Variable Length Subnet Masking, is a technique that allows a network to be divided into subnets of different sizes by using different subnet masks within the same network. Unlike fixed-length subnetting, where all subnets are the same size, VLSM lets you allocate address space more efficiently based on the actual needs of each subnet.
- **Supernetting**
  - Supernetting, also known as route aggregation or summarization, is the process of combining multiple smaller network routes into a single, larger route advertisement. This reduces the size of routing tables and simplifies routing by representing several contiguous subnets as one summary route.

### 2.2 Routing
- **Static vs Dynamic Routing**
  - Static routing involves manually configuring fixed routes in a router's routing table, which do not change unless an administrator updates them. It is simple and predictable, but does not adapt automatically to network changes or failures.
- **Default Gateway**
  - A default gateway is the IP address of the router that a device uses to send traffic destined for networks outside its own local subnet. When a device does not have a specific route for a destination, it forwards the packet to the default gateway, which then handles the routing decision.
- **RIP**
  - RIP, or Routing Information Protocol, is one of the oldest dynamic routing protocols, using a distance-vector algorithm to determine the best path based on hop count —the number of routers a packet must pass through to reach its destination. It has a maximum hop count of 15, making it unsuitable for large networks.
- **OSPF**
  - OSPF, or Open Shortest Path First, is a link-state interior gateway routing protocol used within a single autonomous system or organization. It works by having each router build a complete map of the network topology and then calculate the shortest path to every destination using Dijkstra's algorithm.
- **EIGRP**
  - EIGRP, or Enhanced Interior Gateway Routing Protocol, is an advanced distance-vector routing protocol developed by Cisco that combines features of both distance-vector and link-state protocols. It uses a composite metric based on bandwidth, delay, load, and reliability to calculate the best route and converges faster than traditional distance-vector protocols.
- **BGP**
  - BGP, or Border Gateway Protocol, is the routing protocol that powers the Internet by exchanging routing information between autonomous systems, i.e., the large networks operated by ISPs, corporations, and other organizations. It is a path-vector protocol that makes routing decisions based on network policies, path attributes, and rules rather than simply the shortest path.
- **MPLS**
  - MPLS, or Multiprotocol Label Switching, is a technique for speeding up network traffic by using short labels to direct packets along predetermined paths rather than making complex routing decisions at each hop. When a packet enters an MPLS network, it is assigned a label, and subsequent routers forward it based on that label without needing to inspect the IP header.

### 2.3 Switching
- **VLANs**
  - A VLAN, or Virtual Local Area Network, is a logical subdivision of a physical network that groups devices together regardless of their physical location. VLANs allow network administrators to segment traffic, improve security, and reduce broadcast domains without needing separate physical switches.
- **STP**
  - STP, or Spanning Tree Protocol, is a network protocol that prevents loops in Ethernet networks by creating a logical tree topology from a physically redundant network. Without STP, multiple paths between switches could cause broadcast storms that would bring a network down.
- **Link Aggregation**
  - Link aggregation is a technique that combines multiple physical network connections between two devices into a single logical link, increasing bandwidth and providing redundancy. If one physical link fails, the others continue to carry traffic without interruption.
- **MAC Address Tables**
  - A MAC address table, also called a CAM (Content Addressable Memory) table, is a database maintained by a network switch that maps MAC addresses to the specific ports those devices are connected to. When a frame arrives, the switch looks up the destination MAC address in this table to determine which port to forward the frame to.
- **SD-WAN**
  - SD-WAN, or Software-Defined Wide Area Network, is a technology that uses software to centrally manage and optimize how traffic is routed across multiple WAN connections, such as MPLS, broadband Internet, and 4G/5G links, based on real-time conditions and application requirements. Instead of rigidly sending all traffic through a single expensive MPLS circuit, SD-WAN can intelligently distribute traffic across the best available link at any given moment, improving performance and reducing costs.
- **VRFs**
  - VRF, or Virtual Routing and Forwarding, is a technology that allows a single physical router to run multiple independent routing tables at the same time. Each VRF acts like a completely separate virtual router, meaning traffic in one VRF is fully isolated from traffic in another, even if they share the same physical hardware.
- **VXLAN**
  - VXLAN, or Virtual Extensible LAN, is a network virtualization technology that extends Layer 2 networks over a Layer 3 infrastructure by encapsulating Ethernet frames inside UDP packets. It was created to overcome the scalability limitations of traditional VLANs, which support a maximum of 4,096 network segments, by supporting up to 16 million virtual network identifiers.

### 2.4 Tunneling & VPNs
- **WiFi Standards**
  - Wi-Fi standards are a series of specifications developed by the IEEE under the 802.11 family that define how wireless networks operate. Each generation, from 802.11b and 802.11g through to 802.11ac (Wi-Fi 5) and 802.11ax (Wi-Fi 6), brings improvements in speed, range, efficiency, and the ability to handle more simultaneous connections.
- **IPSec vs SSL VPN**
  - IPSec (Internet Protocol Security) VPNs operate at the network layer, encrypting all IP traffic between two endpoints and are commonly used for site-to-site connections between networks. SSL/TLS VPNs operate at the application layer, typically accessible through a web browser or lightweight client, and are better suited for remote individual user access.
- **Site-to-Site vs Remote Access**
  - Site-to-site VPNs connect two entire networks together — such as a branch office to a headquarters — over an encrypted tunnel, allowing devices on both networks to communicate as if they were on the same LAN. Remote access VPNs allow individual users to securely connect to a corporate network from any location, typically using a VPN client on their device.
- **MLPS VPN**
  - MPLS VPN is a technique that uses Multiprotocol Label Switching to create private, isolated network connections over a shared provider backbone. Service providers use it to offer private WAN connectivity to enterprise customers, where each customer's traffic is logically separated from others, even though it travels across the same physical infrastructure.
- **GRE/IPSec Tunnels**
  - GRE, or Generic Routing Encapsulation, is a tunneling protocol that wraps packets from one protocol inside packets of another, allowing traffic to be carried across networks that would not normally support it. On its own, GRE provides no encryption, so it is commonly combined with IPSec, which adds authentication and encryption to secure the tunnel.

### 2.5 Wireless Networking
- **Access Points**
  - A wireless access point (AP) is a networking device that creates a Wi-Fi network by broadcasting a wireless signal and acting as a bridge between wireless clients and the wired network infrastructure. APs connect to the network via an Ethernet uplink to a switch and allow devices like laptops, phones, and tablets to join the network without a physical cable.
- **Bluetooth**
  - Bluetooth is a short-range wireless communication standard used to connect devices over distances typically up to 10 meters. It operates in the 2.4 GHz frequency band and is designed for low-power, point-to-point or small-group connections between devices like phones, headsets, keyboards, and IoT sensors.
- **Mobile Networks**
  - Mobile networks are wireless communication systems that provide connectivity to devices over large geographic areas through a network of cell towers and base stations. They have evolved through generations, from 2G and 3G through 4G to 5G, each offering faster speeds, lower latency, and greater capacity.
- **Roaming & Band Steering**
  - Roaming is the process by which a wireless client seamlessly transitions from one access point to another as it moves through a space, without dropping its network connection. In enterprise environments, fast roaming protocols like 802.11r (Fast BSS Transition) allow clients to re-authenticate quickly as they move between APs, which is critical for real-time applications like voice and video.
- **Channel Planning**
  - Channel planning is the process of assigning specific radio frequency channels to access points in a way that minimizes interference between them. In the 2.4 GHz band, only three non-overlapping channels (1, 6, and 11) are available, making careful planning essential in dense deployments.
- **Controllers**
  - A wireless controller is a centralized device or software platform that manages multiple access points across a network from a single point of administration. Instead of configuring each AP individually, a controller lets engineers push configurations, monitor performance, manage roaming, and enforce security policies across the entire wireless infrastructure at once.
- **AP Placement & Coverage**
  - AP placement is the process of determining the optimal physical location for access points to ensure complete wireless coverage across a space without dead zones or excessive overlap. Signal strength degrades with distance and is affected by physical obstacles like walls, floors, glass, and metal, so engineers must account for building materials and layout when planning deployments.
- **NFC**
  - NFC, or Near Field Communication, is a short-range wireless communication technology that allows two devices to exchange small amounts of data when brought within a few centimeters of each other. It operates at 13.56 MHz and is most commonly used for contactless payments, access control cards, and quick device pairing.
- **Zigbee & Z-Wave**
  - Zigbee and Z-Wave are low-power, short-range wireless communication protocols designed primarily for IoT and smart home devices such as sensors, lights, locks, and thermostats. Both operate on mesh network topologies where devices can relay signals through each other to extend range, making them well suited for environments with many small, battery-powered devices spread across a space.

### 2.6 Packet Analysis
- **Wireless Security**
  - Wireless security refers to the measures taken to protect wireless networks from unauthorized access, eavesdropping, and attacks. Because wireless signals travel through the air and can be intercepted by anyone within range, securing Wi-Fi networks requires encryption, strong authentication, and proper configuration.
- **Hotspot and Tethering**
  - A hotspot is a physical location or device that provides wireless Internet access to other devices, typically by sharing a cellular data connection. Tethering is the act of connecting a device, such as a laptop, to a smartphone's mobile data connection via Wi-Fi, USB, or Bluetooth to access the Internet.
- **Wireless Site Surveys**
  - A wireless site survey is the process of systematically assessing a physical environment before and after a wireless network deployment to determine optimal AP placement, identify sources of interference, and validate coverage. A passive survey involves walking the space with a Wi-Fi analyzer tool to measure existing signal strength and interference without connecting to any network.
- **LoRaWAN**
  - LoRaWAN, or Long Range Wide Area Network, is a wireless communication protocol designed for IoT devices that need to transmit small amounts of data over very long distances while consuming minimal power. It operates in unlicensed sub-GHz radio bands and can achieve ranges of several kilometers in open environments, making it suitable for applications like smart meters, agricultural sensors, asset tracking, and environmental monitoring.
- **Satellite**
  - Satellite networking uses orbiting satellites to provide wireless connectivity to locations where terrestrial infrastructure is unavailable or impractical, such as remote areas, ships, and aircraft. Traditional geostationary (GEO) satellites orbit at approximately 36,000 km altitude, introducing significant latency (around 600ms round trip) that makes them unsuitable for real-time applications.

### 2.7 High Availability
- **Load Balancer**
  - A load balancer is a device or software that distributes incoming network traffic across multiple servers to prevent any single server from becoming overwhelmed. By spreading the workload, load balancers improve application availability, responsiveness, and fault tolerance.
- **WPA vs WPS**
  - WPA (Wi-Fi Protected Access) is a security protocol designed to protect wireless networks through encryption and authentication, with WPA2 and WPA3 being the current standards offering strong AES-based encryption. WPS (Wi-Fi Protected Setup) is a feature designed to simplify the process of connecting devices to a Wi-Fi network, typically using a PIN or button press.
- **HSRP**
  - HSRP, or Hot Standby Router Protocol, is a Cisco proprietary protocol that provides gateway redundancy by allowing two or more routers to work together as a single virtual router. One router acts as the active gateway handling all traffic, while one or more standby routers monitor it and take over automatically if the active router fails.
- **VRRP**
  - VRRP, or Virtual Router Redundancy Protocol, is an open standard protocol that provides the same gateway redundancy function as HSRP but works across equipment from any vendor. A group of routers share a virtual IP address, with one elected as the master and the others as backups ready to take over if the master becomes unavailable.
- **GLBP**
  - GLBP, or Gateway Load Balancing Protocol, is a Cisco proprietary protocol that goes beyond simple redundancy by also distributing traffic across multiple routers simultaneously. Unlike HSRP and VRRP, where only one router actively handles traffic at a time, GLBP allows all routers in the group to forward traffic, improving both availability and bandwidth utilization.

### 2.8 Traffic Management
- **Round Robin**
  - Round Robin is one of the simplest load balancing algorithms, where incoming requests are distributed sequentially to each server in the pool, one after another, cycling back to the first when the end is reached. It assumes all servers have roughly equal capacity and is easy to implement.
- **Least Connections**
  - The Least Connections algorithm is a load-balancing method that routes each new request to the server with the fewest active connections at that moment. This approach is more adaptive than Round Robin because it accounts for varying request durations and server load.
- **Failover**
  - Failover is the process by which a system automatically switches to a backup server, network path, or resource when the primary one becomes unavailable due to failure or maintenance. The goal is to minimize downtime and ensure continuity of service without requiring manual intervention.
- **Traffic shaping**
  - Traffic shaping is a QoS technique used to control the rate at which data is transmitted on a network, smoothing out bursts and enforcing bandwidth limits for specific types of traffic. By delaying or queuing packets that exceed a defined rate, traffic shaping ensures that no single application or user monopolizes network resources.
- **Packet prioritization**
  - Packet prioritization is the process of classifying network traffic and assigning different levels of importance to different types of packets so that critical traffic is processed and delivered first. Real-time traffic, like VoIP and video conferencing, is given higher priority than background activities like file downloads or software updates.
- **QoS (Quality of Service)**
  - QoS, or Quality of Service, refers to a set of techniques used to manage network traffic and ensure that critical applications receive the bandwidth, low latency, and reliability they need. Without QoS, all traffic is treated equally, which can cause voice calls to break up or video to buffer when the network is congested.

### 2.9 Firewalls
- **Packet Filtering**
  - Packet filtering is the most basic type of firewall technique, where each packet is inspected individually against a set of rules based on attributes like source IP, destination IP, port numbers, and protocol. If a packet matches an allow rule, it passes through; if it matches a deny rule or no rule at all, it is dropped.

### 2.10 Network Attacks
- **DoS & DDoS**
  - A DoS (Denial of Service) attack is an attempt to make a network resource or service unavailable by overwhelming it with a flood of illegitimate traffic or requests. A DDoS (Distributed Denial of Service) attack is the same concept but launched from many different sources simultaneously — often thousands of compromised machines in a botnet — making it much harder to block.
- **Stateful Inspection**
  - Stateful inspection, also known as dynamic packet filtering, is a firewall technique that tracks the state of active network connections and makes filtering decisions based on context, not just individual packets. By maintaining a state table of established connections, a stateful firewall can allow response packets that belong to a legitimate session while blocking unsolicited incoming traffic.

### 2.11 Encryption Basics
- **Next-Generation**
  - A Next-Generation Firewall (NGFW) is an advanced firewall that goes beyond traditional packet filtering and stateful inspection to include deep packet inspection, application awareness, intrusion prevention, and user identity tracking. NGFWs can identify and control traffic based on the specific application being used, regardless of port or protocol, and can detect and block sophisticated threats in real time.

### 2.12 IDS / IPS
- **Proxy**
  - A proxy firewall operates at the application layer and acts as an intermediary between internal clients and external servers, inspecting the full content of network requests and responses. Instead of allowing direct connections, all traffic is routed through the proxy, which can apply content filtering, authentication, and logging.

---

## 3. Advanced

### 3.1 ACLs
- **Circuit Level Gateway**
  - A circuit-level gateway is a type of firewall that operates at the session layer and monitors TCP handshakes to verify that a connection is legitimate before allowing data to flow. Unlike application-layer proxies, it does not inspect the content of the data itself — only the connection establishment.

### 3.2 Zero Trust Architecture
- **Web Application**
  - A Web Application Firewall (WAF) is a specialized security tool designed to filter, monitor, and block HTTP/HTTPS traffic to and from web applications. It protects against common web-based attacks such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF) by inspecting application-layer traffic against a set of rules or policies.

### 3.3 Troubleshooting
- **Methdologies**
  - A troubleshooting methodology is a structured approach to diagnosing network problems that prevents guesswork and reduces time to resolution. The most common approaches are bottom-up (starting at the Physical layer and working up through the OSI model), top-down (starting at the Application layer and working down), and divide and conquer (starting at a middle layer based on available evidence).
- **Common Networks Issues**
  - Common network issues are recurring problems that network engineers encounter regularly across different environments and infrastructures. These include IP address conflicts where two devices share the same address, DNS resolution failures where domain names cannot be translated to IP addresses, default gateway misconfigurations that prevent traffic from leaving the local network, duplex and speed mismatches between connected devices causing performance degradation, VLAN misconfigurations that isolate devices unintentionally, routing loops where packets cycle endlessly between routers, and high latency or packet loss caused by congestion, faulty hardware, or misconfigured QoS policies.
- **ping**
  - ping is one of the most basic and widely used network diagnostic tools, sending ICMP Echo Request packets to a target host and measuring whether a response is received and how long it takes. It is typically the first tool used when troubleshooting connectivity, quickly confirming whether a device is reachable on the network.
- **nslookup**
  - nslookup is a command-line tool used to query DNS servers and retrieve information about domain name resolution. It allows a network engineer to check what IP address a domain resolves to, which DNS server is being used, and whether DNS records such as A, MX, or CNAME entries are correctly configured.
- **netstat**
  - netstat, short for network statistics, is a command-line tool that displays active network connections, listening ports, routing tables, and network interface statistics on a device. It is useful for identifying which services are listening on which ports, spotting unexpected or unauthorized connections, and understanding the current state of network activity on a machine.
- **speedtest**
  - A speedtest is a diagnostic tool that measures the actual throughput of a network connection by downloading and uploading data to a remote server and reporting the results in megabits per second. It is used to verify that a connection is delivering the bandwidth expected from an ISP or internal network link, and to identify discrepancies between advertised and real-world speeds.
- **traceroute / tracert**
  - traceroute (on Linux and macOS) and tracert (on Windows) are diagnostic tools that map the path packets take from a source device to a destination, showing each hop along the route and the latency at each one. By sending packets with incrementally increasing TTL (Time to Live) values, they reveal every router the traffic passes through on its way to the target.

### 3.4 Cloud Networking Basics
- **ipconfig / ifconfig**
  - ipconfig (on Windows) and ifconfig (on Linux and macOS) are command-line tools used to view and manage the network configuration of a device's interfaces. They display information such as the assigned IP address, subnet mask, default gateway, and MAC address for each network adapter.
- **AWS**
  - AWS (Amazon Web Services) offers a comprehensive set of networking services that allow engineers to build and manage network infrastructure entirely in the cloud. Core networking components include VPC (Virtual Private Cloud) for creating isolated virtual networks, subnets for segmenting those networks, Security Groups and Network ACLs for controlling traffic, Route Tables for directing traffic between subnets and to the Internet, and Internet Gateways for enabling public connectivity.
- **Azure**
  - Microsoft Azure provides a full suite of networking services built around the concept of Virtual Networks (VNets), which are the foundational isolated network environments where Azure resources are deployed. Key networking services include VNet Peering for connecting virtual networks together, Azure VPN Gateway for site-to-site and point-to-site VPN connections, ExpressRoute for dedicated private connectivity between on-premises networks and Azure, Azure Firewall for centralized network security, Network Security Groups (NSGs) for controlling inbound and outbound traffic, and Azure Load Balancer and Application Gateway for distributing traffic across services.
- **GCP**
  - Google Cloud Platform (GCP) takes a unique approach to networking with its globally distributed Virtual Private Cloud (VPC), which, unlike AWS and Azure, operates as a single global resource rather than being tied to a specific region. Key networking services include Cloud Router for dynamic routing between on-premises and GCP networks using BGP, Cloud VPN and Cloud Interconnect for hybrid connectivity, Cloud Load Balancing for distributing traffic globally across regions, Firewall Rules for controlling traffic at the network level, and Cloud DNS for scalable domain name resolution.
- **Cloud Network Types**
  - Cloud providers offer several types of virtual network constructs that mirror traditional networking concepts but operate in software. The most fundamental is the Virtual Private Cloud (VPC), a logically isolated section of the cloud where resources are deployed.
- **Virtual Networks**
  - A virtual network in cloud computing is a software-defined network that replicates the functionality of a physical network entirely in software, allowing cloud resources to communicate with each other, with on-premises systems, and with the Internet. Virtual networks are defined through configuration rather than physical cabling, making them fast to create, easy to modify, and infinitely scalable.

### 3.5 APIs for Networking
- **Cloud Routing**
  - Cloud routing refers to how traffic is directed between subnets, virtual networks, on-premises environments, and the Internet within a cloud platform. Each cloud provider uses route tables (collections of rules that determine where traffic destined for specific IP ranges should be sent) to control the flow of packets through the virtual network.
- **Load Balancing**
  - Cloud load balancing distributes incoming network traffic across multiple backend resources, such as virtual machines, containers, or serverless functions, to ensure no single resource is overwhelmed and that applications remain available even if individual components fail. Unlike hardware load balancers in traditional data centers, cloud load balancers are fully managed services that scale automatically with traffic and require no physical maintenance.
- **Cloud VPN**
  - A Cloud VPN is a managed service offered by cloud providers that creates encrypted IPSec tunnels between a cloud virtual network and an on-premises network or another cloud environment over the public Internet. It allows organizations to securely extend their private network into the cloud without needing a dedicated physical connection, making it a cost-effective option for hybrid connectivity.
- **Security Groups**
  - Security groups are virtual firewalls applied at the resource level in cloud environments, controlling which traffic is allowed to reach individual instances, containers, or services based on rules that specify protocol, port range, and source or destination IP address. Unlike traditional network firewalls that sit at the perimeter, security groups travel with the resource and enforce rules wherever that resource is deployed within the cloud.
- **NETCONF**
  - NETCONF, or Network Configuration Protocol, is a network management protocol designed specifically for configuring and retrieving the state of network devices. It uses XML to encode data and runs over SSH, providing a structured, transactional approach to device management that is far more reliable than screen-scraping CLI output.
- **Netmiko**
  - Netmiko is an open-source Python library that simplifies SSH connections to network devices from multiple vendors, including Cisco, Juniper, Aruba, and many others. It handles the complexity of establishing SSH sessions, sending commands, and capturing output in a consistent way regardless of the underlying device type, eliminating the need to write custom connection code for each vendor.
- **NAPALM**
  - NAPALM, which stands for Network Automation and Programmability Abstraction Layer with Multivendor support, is an open-source Python library that provides a unified API for interacting with network devices from different vendors in a vendor-agnostic way. While Netmiko focuses on sending CLI commands and capturing output, NAPALM works at a higher level of abstraction.
- **YANG**
  - YANG is a data modeling language used to define the structure, syntax, and semantics of the data that network devices exchange through management protocols like NETCONF and RESTCONF. It describes exactly what configuration and operational data a device supports in a way that both humans and machines can understand.
- **RESTCONF**
  - RESTCONF is a network management protocol that exposes the same YANG-modeled data as NETCONF but through a RESTful HTTP/HTTPS interface, making it more accessible to developers and tools already familiar with web APIs. Instead of XML over SSH, RESTCONF uses HTTP methods like GET, POST, PUT, PATCH, and DELETE, and supports both JSON and XML as data formats.
- **Python for Networking**
  - Python has become the dominant programming language in network engineering due to its simplicity, readability, and the rich ecosystem of libraries built specifically for interacting with network devices and infrastructure. Network engineers use Python to write scripts that automate configuration changes, parse device output, interact with APIs, process network data, and build custom tools.

### 3.6 Network Automation
- **Wireshark**
  - Wireshark is an open-source network protocol analyzer that captures and displays the data traveling across a network in real time. Engineers use it to inspect individual packets, decode protocols, diagnose connectivity problems, and investigate security incidents at a granular level.
- **Nmap**
  - Nmap (Network Mapper) is a free, open-source tool used to discover hosts and services on a network by sending packets and analyzing the responses. It can identify active devices, open ports, running services, operating systems, and potential vulnerabilities across a network.
- **Ansible**
  - Ansible is an open-source automation tool that uses simple, human-readable YAML files called playbooks to automate the configuration and management of servers, network devices, and cloud infrastructure. Unlike some automation tools, Ansible is agentless — it communicates with devices directly over SSH or APIs without requiring any software to be installed on the target device first.
- **Terraform**
  - Terraform is an open-source Infrastructure as Code tool developed by HashiCorp that allows engineers to define and provision infrastructure — including network resources — using a declarative configuration language called HCL (HashiCorp Configuration Language). Instead of manually creating networks, subnets, firewall rules, and load balancers through a cloud console, Terraform lets you describe the desired state of your infrastructure in code and then automatically creates or modifies resources to match that state.

### 3.7 Infrastructure as Code
- **NetFlow / sFlow**
  - NetFlow is a Cisco-developed protocol that collects and exports metadata about IP traffic flows passing through a network device, providing visibility into who is communicating with whom, how much data is being exchanged, and what protocols are in use. sFlow is a similar, vendor-neutral sampling-based protocol that works across a broader range of hardware.

### 3.8 Observability
- **SNMP**
  - SNMP, or Simple Network Management Protocol, is a widely used protocol for monitoring and managing network devices such as routers, switches, servers, and printers. It allows a central management system to query devices for performance data — like CPU usage, interface statistics, and error counts — and can also receive unsolicited alerts called traps when certain conditions occur.
- **Prometheus**
  - Prometheus is an open-source monitoring and alerting toolkit originally built at SoundCloud and now widely adopted across the industry. It collects metrics by scraping data from configured targets at regular intervals, stores them in a time-series database, and provides a powerful query language called PromQL to analyze and visualize the data.
- **Grafana**
  - Grafana is an open-source data visualization and dashboarding platform that connects to a wide range of data sources, including Prometheus, InfluxDB, Elasticsearch, and SNMP collectors, and displays the data in customizable, real-time dashboards. In network engineering, it is commonly used to visualize metrics like interface traffic, packet loss, latency, and device health collected from monitoring tools.
- **Datadog**
  - Datadog is a cloud-based observability platform that provides monitoring, logging, and security capabilities across infrastructure, applications, and networks in a single unified interface. It collects metrics, traces, and logs from servers, containers, cloud services, and network devices, correlating them to give a complete picture of system health.
- **Dynatrace**
  - Dynatrace is an AI-powered observability platform that automatically discovers, maps, and monitors the full technology stack, from infrastructure and networks to applications and user experience. Its standout feature is the Davis AI engine, which automatically detects anomalies, determines root causes, and reduces alert noise by correlating data across the entire environment.

---

## 4. Optional / Specialized Topics

- Latency
- Server
- Package
- Bandwidth
- Throughput
- Protocol
- Socket
- Port
- IP Address
- CCNP
- CompTIA Network+
- CCNA
- CompTIA Security+
- Cloud Certifications
- Transmission Media Types
- WAN
- WLAN
- SAN
- Cloud
- Client-Server Network
- Mac Address
- ARP
- TCP
- UDP
- ICMP

---

## 5. References

- [Network Engineer Roadmap](https://roadmap.sh/network-engineer)

---

## 6. Related Roles / Topics

### Related Roles
- MLOps Engineer
- Cyber Security Specialist
- Frontend Developer

### Related Skills
- Devops Beginner
- Terraform
- Linux
- Shell & Bash
- System Design