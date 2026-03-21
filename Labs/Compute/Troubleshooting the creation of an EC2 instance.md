
# AWS Challenge: Troubleshooting Amazon EC2

## Project Overview

In this activity, I gained practical experience in launching and configuring Amazon Elastic Compute Cloud (Amazon EC2) instances using the AWS Command Line Interface (AWS CLI). The primary objective was to deploy a fully functional "LAMP stack" (Linux, Apache, MySQL/MariaDB, and PHP) on a single EC2 machine to host the Café Web Application. This common architectural pattern provides a solid foundation for websites with database backends.

<img width="361" height="179" alt="image" src="https://github.com/user-attachments/assets/8296e416-2c2d-4d97-912b-5b8ca46f092e" />

## Key Actions Taken

I have accomplished the following technical steps using the AWS CLI:

* **EC2 Instance Launch via CLI:** I successfully used AWS CLI commands to request the launch of an EC2 instance, specifying the desired AMI, instance type, key pair, and security group.
* **User Data Script Automation:** I referenced and executed a specific **user data script** during the instance launch process. This script was critical for automate the configuration, including:
    * Updating the operating system.
    * Installing and configuring the Apache web server.
    * Installing and configuring the MariaDB relational database.
    * Installing the PHP runtime.
* **Application Deployment:** The user data script also handled the final deployment stages by downloading the Café Web Application files and executing the necessary database configuration scripts on the newly installed LAMP stack.

## Result

Upon successful execution, the automated deployment process resulted in a live EC2 instance hosting the complete Café Web Application. This activity solidified my understanding of using the AWS CLI for infrastructure provisioning and highlighted the power of automated user data scripts for consistent and repeatable application deployment.

<img width="2644" height="1295" alt="image" src="https://github.com/user-attachments/assets/ec4a5473-af36-41a1-99b6-0ae08eebe05a" />
