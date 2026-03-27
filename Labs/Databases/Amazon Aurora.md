# AWS Hands-On Lab: Building and Querying an Amazon Aurora Database Instance

## Project Overview

In this hands-on project, I successfully completed a practical introduction to **Amazon Aurora**, an AWS-managed, high-performance relational database built for the cloud. This lab provided a comprehensive, step-by-step approach to creating a database instance and then connecting to it using an application server.

I gained practical, job-ready competencies spanning the entire process of setting up and querying an Aurora instance. The project involved not only the database configuration but also the essential network and security steps required to allow an application server (running on an EC2 instance) to communicate securely with the database backend.

## Objectives Accomplished

I have accomplished the following technical objectives during this project:

* **Amazon Aurora Instance Creation:** I successfully navigated the AWS Management Console to provision a new, fully operational **Amazon Aurora database instance**. This involved configuring essential parameters such as the database engine (MySQL compatibility), instance class, storage type, and security settings to create a robust and resilient database environment.

<img width="500" height="160" alt="image" src="https://github.com/user-attachments/assets/85542572-c6cf-4d74-8537-c51f90504d01" />

* **Connecting to an Application Server (EC2):** Once the Aurora instance was active, I utilized a pre-created **Amazon Elastic Compute Cloud (Amazon EC2) instance** as my application server. I successfully connected to this instance via SSH to perform subsequent database configurations.
* **Configuring the EC2-to-Aurora Connection:** I performed the necessary steps to allow the EC2 instance to connect securely to the Aurora instance. This involved modifying the database's **VPC Security Group** rules to authorize inbound traffic on the MySQL port (3306) specifically from the EC2 instance's private IP address.
* **Database Interaction and Querying:** Once connectivity was established, I utilized the command-line tools on the EC2 instance to connect directly to the Aurora endpoint. I successfully executed multiple SQL queries to verify the connection and interact with the database, demonstrating my ability to perform standard database administration and data retrieval tasks.

<img width="780" height="150" alt="image" src="https://github.com/user-attachments/assets/2fb3adcc-eeb1-432f-bfe6-d0c7f4965a12" />


## Learning Outcomes

This project provided practical experience in deploying and managing advanced, cloud-native relational database. Key takeaways include understanding how to leverage the specialized features of Amazon Aurora, mastering secure network configuration between EC2 and RDS instances, and gaining confidence in using standard command-line tools to query database instances.

