# AWS Lab: Building and Interacting with a High-Availability RDS Database Server via a Web App

## Project Overview

In this hands-on challenge lab, I successfully reinforced my understanding of leveraging AWS-managed database instances to solve relational database needs. The core focus was on **Amazon Relational Database Service (Amazon RDS)**, an AWS service that simplifies setting up, operating, and scaling a relational database in the cloud. By utilizing Amazon RDS, I experienced firsthand how it provides cost-efficient, resizable capacity while automating time-consuming database administration tasks.

While Amazon RDS supports multiple database engines, including Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, and MariaDB, this lab provided me with specific, job-ready competencies centered around high availability, security configuration, and application integration.

<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/9a33469b-1660-4cf7-bf48-f8b5624aca75" />
<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/8c76d074-b0ec-4c69-879e-11977e451fd8" />


## Objectives Accomplished

I have accomplished the following technical objectives during this challenge:

* **Launching a High-Availability RDS Instance:** I successfully navigated the AWS Management Console to provision a new, fully operational **Amazon RDS DB instance**. Crucially, I configured this instance for **high availability**, implementing features like Multi-AZ deployment to ensure database resilience and minimize downtime in a production-like environment. This involved configuring essential parameters such as the database engine (MySQL), instance class, storage type, and redundancy settings.
* **Configuring Security for Application Connectivity:** Once the RDS instance was active, I performed the necessary steps to allow a web server to connect securely. This involved modifying the database's **VPC Security Group** rules to authorize inbound traffic on the MySQL port (3306) specifically from the security group associated with the web server, demonstrating my understanding of secure network configuration between AWS tiers.

<img width="500" height="260" alt="image" src="https://github.com/user-attachments/assets/e984129f-186e-4795-b43a-124a9a92ba31" />


* **Integrating a Web Application with the Database:** Once connectivity was established, I utilized a pre-configured **web application** running on an EC2 instance. I successfully opened the application in a web browser and interacted directly with the live RDS database, performing standard database operations (like creating tables or inserting data) through the app's interface, verifying the end-to-end integration.

## Learning Outcomes

This project provided practical experience in deploying and managing resilient, cloud-based relational databases. Key takeaways include understanding how AWS RDS automates administrative burdens, mastering the configuration for high availability and robust network security between application and database tiers, and gaining confidence in integrating active web applications with cloud-managed database solutions.
