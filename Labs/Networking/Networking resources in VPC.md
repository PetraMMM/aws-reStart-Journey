
# Building and Configuring a Routable AWS VPC

In this project, I took on the role of a Cloud Support Engineer to help a customer who was struggling with a common yet critical cloud challenge: a VPC with no external connectivity. I built a complete networking stack from scratch to ensure that resources within the VPC could successfully "ping" the outside world.

---

## Project Overview

The customer had a vision for their network but was missing the "glue" that connects a private cloud to the internet. I systematically provisioned and linked every essential networking component, moving from an isolated environment to a fully routable network.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/d0121a79-3c7f-43b5-a818-21365b2035fb" />


### Key Tasks Performed:

* **VPC Infrastructure:** I created a custom **Virtual Private Cloud (VPC)** to serve as the logically isolated home for all resources.
* **Internet Gateway (IGW) Attachment:** I provisioned an **Internet Gateway** and attached it to the VPC, providing the necessary "doorway" for traffic to enter and exit.
* **Route Table Configuration:** I created and configured a **Route Table** with a default route (`0.0.0.0/0`) pointing to the Internet Gateway, ensuring the network knew how to find the public internet.
* **Layered Security:**
    * **Network ACLs (NACLs):** I configured a Network Access Control List to act as a stateless firewall for the subnet.
    * **Security Groups:** I set up a stateful firewall for the **EC2 instance**, specifically allowing **ICMP traffic** to enable the ping command.
* **Testing & Validation:** I launched an EC2 instance and used the command line to successfully **ping an external address**, proving the network was fully routable.

---

## Objectives Achieved

* **End-to-End Connectivity:** Mastered the specific order of operations required to make a VPC "internet-aware."
* **Diagnostic Mastery:** Successfully addressed the customer's core requirement—enabling ICMP (Ping) functionality—which required aligning Route Tables, IGWs, and Security Groups.
* **Console Proficiency:** Gained deep familiarity with the AWS Management Console’s networking and VPC dashboards.

---

## Technical Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Networking:** Amazon VPC, Internet Gateway (IGW), Route Tables
* **Security:** Security Groups (Layer 4), Network ACLs (Layer 3), ICMP Protocol
* **Compute:** Amazon EC2

---

## Conclusion

This project allowed me to solve a fundamental connectivity puzzle. By building the network piece-by-piece, I demonstrated that "just needing to ping" actually requires a perfectly synchronized set of resources—from the gateway and routes to the specific ICMP rules in the security layer.
