Lab Report: Deploying and Managing Amazon EC2 Instances

Project Overview

In this hands-on lab, I gained experience with Amazon Elastic Compute Cloud (EC2). I focused on the full lifecycle of a virtual server—from initial configuration and security to vertical scaling and safe termination. My goal was to deploy a functional web server while implementing industry best practices for security and resource management.

Key Technical Steps I Performed

1. Provisioning & Security 

I launched a Linux-based EC2 instance by selecting a high-performance Amazon Machine Image (AMI) and a cost-effective t-series Instance Type.

Termination Protection: I enabled this essential safeguard to prevent accidental deletion of production workloads.

Network Architecture: I assigned specific Network Settings to ensure the instance was correctly placed within its VPC and subnet.

<img width="465" height="165" alt="image" src="https://github.com/user-attachments/assets/300afdec-b740-421a-98bb-1b9d318a15ed" />

At first I have not specified any inbound rules, which made the instance not reachable and therefore it showed following message.

<img width="208" height="179" alt="image" src="https://github.com/user-attachments/assets/2784804a-531e-4ea9-9f4f-afba1a09fc38" />


2. Security & Public Accessibility

To make the web server reachable, I modified the Security Group rules. Since AWS follows a "default-deny" security posture, I explicitly added:

Inbound Rule: Allowed HTTP access (Port 80) from any source (0.0.0.0/0).

Verification: This enabled the server to serve live content to the public internet.

3. Monitoring & Performance Checks

I utilized the AWS Management Console to monitor the instance’s health. By observing status checks and system metrics, I ensured the virtual hardware and the software layer were performing optimally without errors.

4. Vertical Scaling (Resizing)

I demonstrated the elasticity of the cloud by performing a vertical scale:

Instance Transformation: I stopped the instance to change its Instance Type, increasing CPU and RAM.

Storage Modification: I updated the Elastic Block Store (EBS) volume to increase total storage capacity.

Takeaway: This proved how easily resources can be adjusted based on real-time traffic demands without migrating to new hardware.

5. Lifecycle Management & Cleanup

I concluded the lab by testing the Termination Protection I enabled earlier. After confirming that the system successfully blocked an accidental deletion attempt, I manually disabled the protection and Terminated the instance to clean up the cloud resources efficiently.

Summary of Skills Learned

Skill Category

Tools & Concepts

Cloud Infrastructure

AWS EC2, AMI Selection, Scaling

Security

Security Groups, Key Pairs, Termination Protection

Storage

Amazon EBS (Elastic Block Store)

Ops & Management

Instance Lifecycle, Resource Monitoring

This lab was completed as part of my continuous learning journey in AWS Cloud Architecture.


















<img width="229" height="63" alt="image" src="https://github.com/user-attachments/assets/48b82efb-01d7-483c-be97-8990f517dc08" />




<img width="440" height="231" alt="image" src="https://github.com/user-attachments/assets/ca79fb08-d9f2-43bc-b87b-931ed74047c5" />

