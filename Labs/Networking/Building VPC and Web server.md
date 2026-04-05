
# Building a VPC and Launching a Web Server

In this project, I moved beyond default settings to build a custom, logically isolated virtual network on AWS. I manually configured the networking environment to host a functional web server, ensuring I had full control over connectivity and security.

---

## Project Overview

I designed and implemented a Virtual Private Cloud (VPC) to provide a secure foundation for cloud resources. The process involved defining the network boundaries, setting up connectivity, and deploying a live EC2 instance to act as a web server.

<img width="400" height="180" alt="image" src="https://github.com/user-attachments/assets/942a82f1-8bcf-4d37-b99e-e59c684fbf10" />


### Key Tasks Performed:

* **VPC Creation:** I established a custom **Virtual Private Cloud (VPC)**, defining a specific IP address range to isolate my resources from other users.
* **Subnet Design:** I created **subnets** within the VPC to organize the network and prepare it for hosting resources in specific Availability Zones.
* **Security Configuration:** I built and configured a **Security Group**, acting as a virtual firewall. I specifically wrote rules to control which traffic (such as HTTP or SSH) was allowed to reach my instance.

<img width="400" height="180" alt="image" src="https://github.com/user-attachments/assets/f0b6be45-7602-4ed5-b746-8822326727f6" />


* **Web Server Deployment:** I launched an **Amazon EC2 instance** into the newly created VPC, ensuring it was correctly associated with the custom subnet and security group.

<img width="400" height="215" alt="image" src="https://github.com/user-attachments/assets/44ac7684-12a2-409a-a705-e7b886593047" />


---

## Objectives Achieved

* **Network Infrastructure:** Gained a fundamental understanding of how to build a cloud network from scratch.
* **Resource Isolation:** Successfully launched compute resources into a private, controlled environment rather than a default shared network.
* **Traffic Management:** Applied the "Principle of Least Privilege" by configuring security group rules that only allow necessary traffic to the web server.

---

## Technical Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Networking:** Amazon VPC, Subnets, IP Addressing
* **Security:** Security Groups (Stateful Inspection)
* **Compute:** Amazon EC2 (Linux-based Web Server)

---

## Conclusion

This project provided me with practical experience in the building blocks of AWS networking. By manually creating the VPC and security layers, I learned exactly how data flows from the internet to a web server and how to protect those resources from unauthorized access.
