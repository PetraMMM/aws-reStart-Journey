
# AWS CloudTrail: Security Auditing & Incident Response

## Project Overview
In this project, I acted as a Cloud Security Engineer tasked with investigating a security breach for a business's primary web application (the Café website hosted on Amazon EC2). My objective was to implement tracking mechanisms, identify how the environment was compromised, pinpoint the culprit, and secure the infrastructure against future attacks.

<img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/2077ede7-a059-4cbe-bb1c-b68e940e3b23" />


## The Scenario
The company's leadership team discovered that their website had been hacked. They needed a way to track infrastructure changes and determine exactly who made them. I stepped in to trace the unauthorized modifications—specifically, changes made to the EC2 security groups—and remediate the vulnerabilities.

## My Approach & Technical Implementation

### 1. Enabling Continuous Auditing (AWS CloudTrail)
I started by configuring an **AWS CloudTrail trail** to monitor and record all API activity and administrative actions taken within the AWS account. This provided the foundational audit logs needed to reconstruct the events leading up to the breach.

### 2. Initial Log Analysis (AWS CLI & Linux)
Once the trail was active and logging the hacker's movements, I downloaded the CloudTrail logs. I utilized the **AWS CLI** and Linux command-line utilities (such as `grep`) to parse through the raw JSON log files. This initial triage helped me confirm that an unauthorized security group modification was the entry point for the attack.

### 3. Advanced Threat Hunting (Amazon Athena)
To perform a more robust and structured investigation, I integrated CloudTrail with **Amazon Athena**. I imported the log data into Athena and executed SQL queries to filter the massive dataset. This allowed me to rapidly isolate the specific IAM user and IP address responsible for the unauthorized security group changes.

### 4. Incident Response & Remediation
After identifying the compromised user account (the "culprit"), I immediately took action to contain the threat:
* I revoked the malicious user's access via **AWS IAM**.
* I reverted the unauthorized Security Group changes to lock down access to the EC2 Linux instance.
* I implemented stricter IAM policies and security best practices to harden the AWS account and prevent future breaches.

## Technologies Used
* **Security & Auditing:** AWS CloudTrail, AWS Identity and Access Management (IAM)
* **Data Querying & Analysis:** Amazon Athena, SQL
* **Compute & Networking:** Amazon EC2, Security Groups
* **Tools:** AWS CLI, Linux Command Line (`grep`)

## Conclusion
This project gave me invaluable hands-on experience in cloud incident response. I successfully demonstrated how to track API calls, analyze audit logs using both command-line tools and SQL-based querying, and effectively remediate security vulnerabilities within an AWS environment.
