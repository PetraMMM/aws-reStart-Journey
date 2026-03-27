### AWS Challenge Lab: Building and Querying an AWS RDS Database Server

#### Project Overview

In this hands-on challenge lab, I successfully reinforced my understanding of leveraging AWS-managed database instances to solve relational database needs. The core focus was on **Amazon Relational Database Service (Amazon RDS)**, an AWS service that simplifies setting up, operating, and scaling a relational database in the cloud. By utilizing Amazon RDS, I experienced firsthand how it provides cost-efficient, resizable capacity while automating time-consuming database administration tasks.

While Amazon RDS supports multiple database engines, including Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, and MariaDB, this lab provided me with specific, job-ready competencies centered around creation and querying.

#### Objectives Accomplished

I have accomplished the following technical objectives during this challenge:

* **RDS Instance Creation:** I successfully navigated the AWS Management Console to provision a new, fully operational **Amazon RDS instance**. This involved configuring essential parameters such as the database engine (MySQL), instance class, storage type, and security settings to create a robust database backend.
* **Database Interaction via Query Editor:** Once the RDS instance was active, I utilized the built-in **Amazon RDS Query Editor** within the AWS console. This powerful, integrated tool allowed me to directly connect to the database, run SQL queries, and validate data without needing to install or configure external database client software.
* **Linux/EC2 Server Administration:** I executed essential system administration tasks directly on the Amazon Linux EC2 instance. This included installing the necessary database server packages (`sudo yum install`), managing database services (`systemctl start`/`status`), and identifying connectivity issues related to the MariaDB socket file.
* **Database User Security and Authentication:** I successfully navigated common authentication hurdles on a fresh database installation. I identified and resolved **Access Denied ERROR 1045 (28000)** for the `root` user, demonstrating my ability to manage user credentials and secure access.
* **Relational Schema and Table Design:** I designed and created a fully operational relational database (`StudentDB`) containing two different tables (`RESTART` and `CLOUD_PRACTITIONER`). In this process, I mastered essential technical skills including:
    * Implementing robust **AUTO_INCREMENT PRIMARY KEYs** (for automatically generating unique number IDs) and advanced **Composite PRIMARY KEYs** (combining IDs and dates).
    * Selecting correct SQL date/time data types (`DATE` and `DATETIME`) and using their specific standard input formats.
    * Avoiding robust identifier names to prevent terminal-specific character errors in Putty.
* **Advanced Data Population and Modification:** I populated my database with complex sample data, mastering the correct use of single quotes for text strings and datetimes. I successfully executed SQL DML queries to create multiple empty sets in one action, and to update specific existing records based on unique identifiers (like `StudentID`).
* **Performing INNER JOIN Queries:** I executed the core relational database operation—an **INNER JOIN**—between my two custom tables (`RESTART` and `CLOUD_PRACTITIONER`). This allowed me to efficiently link and display matching records (`Student Name`, `Student ID`, and `Certification Date`) from both sets of data.

#### Learning Outcomes

This project provided practical experience in deploying and managing cloud-based relational databases. Key takeaways include understanding how AWS manages the underlying infrastructure and how to efficiently interact with an RDS instance to create tables, insert data, and execute complex SQL queries, laying a strong foundation for cloud-native application development.
