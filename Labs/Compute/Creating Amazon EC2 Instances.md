Creating Amazon EC2 Instances

This repository contains the documentation and architectural overview for the AWS Lab: Creating Amazon EC2 Instances. 

1. Overview

This lab demonstrates the different methods available for provisioning compute resources on AWS. The project involves building a secure two-tier architecture where a Bastion Host is launched manually to act as a gateway, which is then used to programmatically launch a Web Server using the AWS Command Line Interface (AWS CLI).


<img width="245" height="180" alt="image" src="https://github.com/user-attachments/assets/3105c6f9-7717-4c59-b6fe-5a632ec34587" />



The final architecture includes a Bastion Host in a public subnet and a Web Server provisioned via CLI.

2. Objectives

Launch EC2 via Console: Provision a Linux instance using the AWS Management Console.

Secure Connectivity: Use EC2 Instance Connect for browser-based SSH access.




Automated Provisioning: Use the AWS CLI from within an active instance to launch a secondary web server instance.

3. Environment & Tools

Cloud Provider: Amazon Web Services (AWS)

Services: Amazon EC2, VPC, IAM

Connectivity: EC2 Instance Connect

Interface: AWS Management Console & AWS CLI

Operating System: Amazon Linux 2023

4. Methodology

Task 1: Launching the Bastion Host

Configured an EC2 instance via the AWS Console with the following parameters:

Subnet: Public

Security Group: Allowed SSH (Port 22)

IAM Role: Attached a role with permissions to describe and run EC2 instances.

<img width="524" height="274" alt="image" src="https://github.com/user-attachments/assets/f9cf4ab2-30ce-4e06-add3-9f43cf4582d3" />

Task 2: Logging in to the Bastion Host

Used EC2 Instance Connect to establish a secure terminal session directly from the browser.

Task 3: Launching the Web Server via CLI

<img width="778" height="223" alt="image" src="https://github.com/user-attachments/assets/0e4532ef-ce3b-424e-b929-25c1e2ce5349" />

Task 4: Testing the Web Server

Verified the instance was "Running" in the console and confirmed the web server was serving traffic by accessing its public IP.

<img width="376" height="193" alt="image" src="https://github.com/user-attachments/assets/01e401a2-561f-4d95-b3b8-e4b74df2adad" />


<img width="382" height="160" alt="image" src="https://github.com/user-attachments/assets/36259e0b-4e80-4afb-939d-19bbdf2649b2" />


Connectivity: Verified that the Web Server was reachable, confirming correct Security Group application.


Developed as part of AWS Technical Training.
