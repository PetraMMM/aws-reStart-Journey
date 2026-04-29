# Infrastructure Automation with AWS CloudFormation

## Overview
In this project, I gained hands-on experience with **Infrastructure as Code (IaC)** using **AWS CloudFormation**. 

Historically, deploying cloud infrastructure in a consistent and reliable manner is difficult—it often relies on manual, documented procedures where human error or undocumented shortcuts can occur. Additionally, manual deployments make out-of-hours scheduling challenging. To solve this, I used AWS CloudFormation to define my cloud infrastructure within a declarative template, allowing for automated, repeatable, and reliable deployments.

This was a highly interactive project that required me to consult AWS documentation extensively to discover how to properly define, format, and configure various AWS resources within a CloudFormation template.

## What I Accomplished
During this project, I successfully demonstrated the ability to:
* **Deploy a Foundational Stack:** I deployed an initial AWS CloudFormation stack that automatically provisioned a custom Virtual Private Cloud (VPC) and a Security Group.
* **Update and Configure Resources:** I expanded my infrastructure by editing the active CloudFormation template to include new resources. Specifically, I configured and deployed an **Amazon S3 bucket** and an **Amazon EC2 instance**.
* **Manage the Infrastructure Lifecycle:** I learned how to safely tear down environments by terminating the CloudFormation stack, which automatically and cleanly deletes all associated resources to prevent orphaned infrastructure and unexpected costs.

## Technologies Used
* **AWS CloudFormation** (Infrastructure as Code)
* **Amazon VPC** (Networking)
* **Amazon EC2** (Compute)
* **Amazon S3** (Storage)
* **AWS Security Groups** (Firewalls)

## Key Takeaways
This project reinforced the power of automating infrastructure. By defining my environment as code, I can now deploy entire architectures reliably without manual intervention, update them safely, and tear them down quickly when they are no longer needed.
