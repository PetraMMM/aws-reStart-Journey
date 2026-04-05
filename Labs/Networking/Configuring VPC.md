
# Configuring a Secure AWS VPC Architecture

In this project, I built a custom, logically isolated virtual network on AWS from the ground up. The goal was to design a network that balances security with connectivity, ensuring that private resources remain protected while allowing necessary communication with the internet.

---

## Project Overview

I provisioned a complete Virtual Private Cloud (VPC) environment, including both public and private subnets. This architecture follows cloud best practices by placing sensitive resources in a private area and using a "Bastion Host" (jump server) as a secure gateway for administrative access.

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/bcadf86e-3fb1-4f76-9933-8e70e88c7239" />


### Key Tasks Performed:

* **VPC Foundation:** I created a custom VPC and carved out specific IP address ranges by designing both **public and private subnets**.
* **Connectivity Routing:** I deployed an **Internet Gateway (IGW)** to allow public access and a **NAT Gateway** to allow private instances to download updates without being exposed to the open internet.
* **Route Table Management:** I configured and associated separate route tables for each subnet to ensure traffic was correctly directed to either the IGW or the NAT Gateway.
* **Secure Access Bridge:** I launched a **Bastion Host** in the public subnet and used it as a secure "jumping point" to log in to an EC2 instance located in the private subnet.

---

## Objectives Achieved

* **Network Segmentation:** Successfully separated public-facing resources from private backend resources.
* **Traffic Control:** Mastered the use of route tables to manage how data enters and exits the VPC.
* **Secure Administration:** Implemented a Bastion Server architecture, demonstrating how to manage private cloud resources without assigning them public IP addresses.

---

## Technical Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Networking:** Amazon VPC, Subnets, Internet Gateway, NAT Gateway, Route Tables
* **Compute:** Amazon EC2 (Public Bastion & Private Instance)
* **Security:** Key Pairs, Security Groups

---

## Conclusion

This project allowed me to gain a deep understanding of how virtual networking functions in a cloud environment. By building this architecture, I learned how to ensure that a private database or application server can stay "hidden" from the internet while still receiving necessary updates and remaining accessible to authorized administrators.
