# Infrastructure Automation with AWS CloudFormation

## Overview
In this project I gained experience with Infrastructure as Code (IaC) using **AWS CloudFormation**. 

Deploying cloud infrastructure in a consistent and reliable manner is difficult, as it often relies on manual, documented procedures, where human error or undocumented shortcuts can occur. To solve this, I used AWS CloudFormation to define my cloud infrastructure within a template, allowing for automated, repeatable, and reliable deployments.

## What I Accomplished
During this project, I successfully demonstrated the ability to:
* **Deploy an Initial Stack:** I deployed an initial AWS CloudFormation stack that automatically provisioned a custom Virtual Private Cloud (VPC) and a Security Group.

<img width="520" height="335" alt="image" src="https://github.com/user-attachments/assets/08e7a310-611a-4b6f-83e6-0d1a1ceab77a" />


* **Update and Configure Resources:** I expanded my infrastructure by editing the active CloudFormation template to include new resources. Specifically, I configured and deployed an **Amazon S3 bucket** and an **Amazon EC2 instance**.
* **Manage the Infrastructure Lifecycle:** I learned how to safely tear down environments by terminating the CloudFormation stack, which automatically and cleanly deletes all associated resources to prevent orphaned infrastructure and unexpected costs.

## Technologies Used
* **AWS CloudFormation** (Infrastructure as Code)
* **Amazon VPC** (Networking)
* **Amazon EC2** (Compute)
* **Amazon S3** (Storage)
* **AWS Security Groups** (Firewalls)

## Key Takeaways
This project showed  how to automate infrastructure by using templates (deploying templates, updating and deleting).
