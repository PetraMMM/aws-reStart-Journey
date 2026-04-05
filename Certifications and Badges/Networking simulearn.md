# AWS Networking Design: Routing and Database Connectivity

In this project, I moved beyond theoretical networking to build and validate a functional connection between a Web Tier and a Database Tier within an AWS VPC. I focused on the precise configuration of Route Tables and Security Groups to ensure secure, cross-subnet communication.

---

## Project Overview

The goal of this lab was to establish a secure "Internal-only" connection between two different parts of a network. I managed the flow of traffic from the public internet to a web server, and then from that web server to a private database server.

<img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/53a2a837-1b8e-4c2f-a788-5f0668e7319c" />


### Key Tasks Performed:

*   **VPC Architecture Exploration:** I analyzed the core components of the Virtual Private Cloud (VPC) to understand how subnets isolate different types of resources.
*   **Routing Configuration:** 
    *   I configured **Route Tables** attached to specific subnets to manage how data moves internally.
    *   I established a route to direct internet-bound traffic to an **Internet Gateway (IGW)**, allowing the web tier to be reachable from the outside world.

<img width="400" height="180" alt="image" src="https://github.com/user-attachments/assets/9d98d7fd-a9df-4f6d-be68-6e07f96b00cd" />

   
*   **Security Group (DIY Goal):**
    *   I modified the **DbServerSecurityGroup** to allow inbound traffic on **Port 3306** (MySQL/Aurora).
    *   I specifically configured the rules so that the Database server would only accept requests coming from the **WebServerSecurityGroup**, implementing a "Least Privilege" security model.

<img width="400" height="180" alt="image" src="https://github.com/user-attachments/assets/5bb9e8e8-d543-44f3-93ae-2e224fc2a72b" />


*   **Connection Validation:** I verified that the Web Server (on the `10.10.0.0/24` subnet) could successfully communicate with the DB Server (on the `10.10.2.0/24` subnet) over the required TCP port.

---

## Objectives Achieved

*   **Traffic Steering:** Mastered the ability to use Route Tables to define specific paths for both internal and internet-bound data.
*   **Tiered Security:** Successfully implemented a two-tier architecture where the database is shielded from the internet and only accessible by the web server.
*   **Database Connectivity:** Gained hands-on experience opening specific ports (3306) for standard database protocols (MySQL/Aurora).

---

## Technical Stack

*   **Cloud Provider:** Amazon Web Services (AWS)
*   **Networking:** VPC, Subnets (10.10.0.0/24 & 10.10.2.0/24), Route Tables, Internet Gateway
*   **Security:** Security Groups (Stateful), Inbound/Outbound Rules
*   **Protocols:** TCP, MySQL/Aurora (Port 3306)

---

## Conclusion

By completing this project, I demonstrated the ability to bridge the gap between two isolated subnets. This exercise reinforced the importance of "chained" security groups—where one security group acts as the authorized source for another—ensuring that sensitive data remains protected even within the internal network.
