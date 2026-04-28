# AWS Resource Management and Automation via Tagging

## Overview
In this project, I explored and implemented automated infrastructure management using **AWS Resource Tagging**. By using the AWS Command Line Interface (CLI) and JMESPath query syntax, I successfully demonstrated how metadata tags can be used to organize, filter, and automate lifecycle actions across a fleet of Amazon EC2 instances. 

---

<img width="500" height="210" alt="image" src="https://github.com/user-attachments/assets/dd1d3ca9-bc3b-47aa-97ca-9b084b0ff1f2" />


## The Environment
The cloud architecture for this hands-on project was deployed within a custom **Lab VPC** containing both public and private subnets. The computing environment consisted of:
* A central **CommandHost** EC2 Linux instance, pre-configured with the AWS CLI.
* A fleet of **8 Amazon EC2 Linux instances** simulating a company's workload.

To manage these resources, I utilized a strict tagging schema across the fleet:
* **Project:** Identifies the workload (`ERPSystem`).
* **Version:** Tracks the deployment version (initialized at `1.0`).
* **Environment:** Defines the release stage (`development`, `staging`, or `production`).

---

## Objectives Achieved
Through this project, I successfully demonstrated the ability to:
* **Apply and modify tags** on existing AWS resources programmatically.
* **Query and filter resources** based on specific tag values using advanced CLI parameters.
* **Automate lifecycle actions** (such as stopping and starting instances) to simulate cost-saving measures for non-production environments.
* **Enforce tagging compliance** by identifying and terminating resources that fail to meet corporate tagging standards.

---


## Technologies and Tools Used
* **Amazon Web Services (AWS):** EC2, VPC
* **AWS CLI:** Primary interface for resource manipulation and automation.
* **JMESPath:** Used for parsing and filtering complex JSON data structures returned by the AWS API.
* **Bash Scripting:** Utilized for executing batch commands and state management.
