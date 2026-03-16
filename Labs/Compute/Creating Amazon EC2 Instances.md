Lab: Creating Amazon EC2 Instances

This repository contains the documentation and architectural overview for the AWS Lab: Creating Amazon EC2 Instances. 

1. Overview

This lab demonstrates the different methods available for provisioning compute resources on AWS. The project involves building a secure two-tier architecture where a Bastion Host is launched manually to act as a gateway, which is then used to programmatically launch a Web Server using the AWS Command Line Interface (AWS CLI).

Architecture Diagram



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

Task 2: Logging in to the Bastion Host

Used EC2 Instance Connect to establish a secure terminal session directly from the browser, avoiding the need for local .pem keys.

Task 3: Launching the Web Server via CLI

Once inside the Bastion Host, the environment was verified, and the following CLI command structure was used to launch the second instance:

aws ec2 run-instances \
    --image-id ami-xxxxxxxxxxxxxxxxx \
    --count 1 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-xxxxxxxxxxxxxxxxx \
    --user-data file://user-data.sh


Task 4: Testing the Web Server

Verified the instance was "Running" in the console and confirmed the web server was serving traffic by accessing its public IP.

5. Results & Findings

Seamless Integration: The Bastion Host successfully inherited IAM permissions to execute CLI commands.

Efficiency: CLI provisioning proved faster for repeatable infrastructure tasks compared to the Console.

Connectivity: Verified that the Web Server was reachable, confirming correct Security Group application.

6. Challenges & Solutions

Issue: AWS CLI permissions error.

Solution: Verified the IAM Instance Profile was correctly attached to the Bastion Host.

Issue: Port 80 (HTTP) was closed.

Solution: Updated the Security Group rules via the console to allow inbound web traffic.

7. Conclusion

This lab successfully illustrated the hybrid workflow of manual setup and CLI-driven automation. By using a bastion host, we maintained a high security posture while demonstrating the power of the AWS CLI for scaling infrastructure.

Developed as part of AWS Technical Training.
