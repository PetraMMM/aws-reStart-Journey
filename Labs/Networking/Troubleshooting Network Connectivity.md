# Troubleshooting Network Connectivity for a Cloud-Based Web Server

This project highlights my ability to act as a Cloud Support Engineer, diagnosing and resolving real-world connectivity issues. I was tasked with investigating why a customer’s Apache web server was unreachable via both the browser and ping commands despite being active.

---


<img width="400" height="160" alt="image" src="https://github.com/user-attachments/assets/66b3c54b-71f3-449d-84eb-378e1283df42" />


## Project Overview

In this scenario, I received an escalation from a customer who had successfully launched an Apache server on an EC2 instance but faced two major hurdles:
1. They could not **ping** the server.
2. They received a **connection error** when trying to access the server's IP address in a web browser.

I took a systematic approach to identify whether the blockage was occurring at the network level (VPC), the security level (Security Groups/NACLs), or the instance level itself.

### Key Tasks Performed:

* **Scenario Analysis:** I reviewed the customer's infrastructure to map out the traffic path from the public internet to the EC2 instance.
* **Security Group Audit:** I inspected the **Security Groups** and found that inbound rules for **HTTP (Port 80)** were missing.
* **Route Table Verification:** I verified that the instance was in a public subnet with a valid path to an **Internet Gateway (IGW)**.
* **Problem Resolution:** I modified the security rules to allow traffic on the necessary ports.

<img width="400" height="150" alt="image" src="https://github.com/user-attachments/assets/5e229026-a73b-4ef9-9914-58368b76f6f5" />


* **Verification:** I performed final testing by successfully pinging the instance and loading the Apache test page via the public IP.

---

## Objectives Achieved

* **Technical Troubleshooting:** Applied a logical "bottom-up" troubleshooting method to isolate network failures.
* **Protocol Knowledge:** Demonstrated understanding of **HTTP (TCP Port 80)** for web traffic and "ping"  for network diagnostics.
* **Security Policy Management:** Correctly implemented security rules to allow legitimate traffic while maintaining the principle of least privilege.

---

## Technical Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Web Server:** Apache (HTTPD)
* **Networking & Security:** Amazon VPC, Security Groups, TCP/IP
* **Compute:** Amazon EC2

---

## Conclusion

This project reinforced the importance of security group configuration in cloud environment. By analyzing the symptoms provided by the customer, I was able to pinpoint exactly where the communication was breaking down and restore service, ensuring the web server was both secure and accessible.
