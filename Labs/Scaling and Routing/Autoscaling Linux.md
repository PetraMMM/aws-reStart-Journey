# AWS Auto Scaling and Load Balancing Architecture (Linux)

## Project Overview
In this project, I engineered a highly available, dynamically scaling web server infrastructure on AWS. Using the **AWS Command Line Interface (AWS CLI)**, I provisioned the foundational compute resources and created a custom Amazon Machine Image (AMI). I then utilized **Amazon EC2 Auto Scaling** and an **Elastic Load Balancer (ELB)** to build an architecture capable of automatically adjusting to variable traffic loads across multiple Availability Zones.

## Key Achievements & Implementation Details
Throughout this project, I successfully completed the following objectives:

* **CLI-Driven Provisioning:** I created the initial Amazon EC2 instance entirely via the AWS CLI, demonstrating programmatic control over AWS resources.
* **Custom AMI Creation:** I generated a custom Amazon Machine Image (AMI) from my configured EC2 web server using the CLI. This served as the reliable, reusable baseline for my scaling group.
* **Launch Templates & Configurations:** I designed an Amazon EC2 launch template and an Auto Scaling launch configuration to standardize the rapid deployment of new instances.
* **Dynamic Auto Scaling:** I configured an Auto Scaling group equipped with specific scaling policies. This enables the infrastructure to automatically **scale out** (provision new servers) during high traffic spikes and **scale in** (terminate unneeded servers) during low demand, optimizing both performance and cost.
* **Load Distribution:** I deployed an Elastic Load Balancer to evenly distribute incoming user traffic across the auto-scaled EC2 instances spanning multiple Availability Zones, ensuring fault tolerance and high availability.

## Technologies Used
* **AWS Command Line Interface (CLI)**
* **Amazon EC2** (Linux Web Servers)
* **Amazon Machine Images (AMI)**
* **Amazon EC2 Auto Scaling** (Groups, Launch Templates, Scaling Policies)
* **Elastic Load Balancing (ELB)**

## Conclusion
This project solidified my practical experience with AWS command-line management and automated scaling mechanisms. I am now fully capable of designing robust environments that autonomously respond to variable loads, ensuring consistent application uptime and infrastructure cost efficiency.
