
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

<img width="400" height="180" alt="image" src="https://github.com/user-attachments/assets/c4d9324e-f1f8-47d0-a6cf-472456d9bf7d" />


* **Layered Security:**
    * **Network ACLs (NACLs):** I configured a Network Access Control List to act as a stateless firewall for the subnet.
      
      <img width="400" height="220" alt="image" src="https://github.com/user-attachments/assets/52b6ba8d-b3d7-4c3d-ae4c-afae5cce0edb" />

    * **Security Groups:** I set up a stateful firewall for the **EC2 instance**.

      <img width="400" height="260" alt="image" src="https://github.com/user-attachments/assets/f73f50b5-eeba-41b5-b25a-994b34eb923d" />

      
* **Testing & Validation:** I launched an EC2 instance and used the command line to successfully **ping an external address**, proving the network was fully routable.

<img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/6a79f8a7-a1d4-49d1-abad-1d909e5ccaf6" />


---

## Objectives Achieved

* **End-to-End Connectivity:** Managed the specific order of operations required to make a VPC "internet-aware."
* **Diagnostic:** Successfully addressed the customer's core requirement—enabling ICMP (Ping) functionality—which required aligning Route Tables, IGWs, and Security Groups.
* **Console Proficiency:** Gained familiarity with the AWS Management Console’s networking and VPC dashboards.

---

## Technical Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Networking:** Amazon VPC, Internet Gateway (IGW), Route Tables
* **Security:** Security Groups, Network ACLs
* **Compute:** Amazon EC2

---

## Conclusion

This project allowed me to solve a connectivity puzzle. By building the network piece-by-piece, I demonstrated that "just needing to ping" actually requires a perfectly synchronized set of resources from the Internet gateway, route tables, Security groups and NACLs.
