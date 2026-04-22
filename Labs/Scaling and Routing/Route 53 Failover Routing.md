# Amazon Route 53 Failover Routing 

## Project Overview
In this project, I configured a highly available, disaster-resilient architecture for a web application using **Amazon Route 53 Failover Routing**. The goal of this project was to ensure that if my primary web server goes down, application traffic is automatically and seamlessly routed to a backup server in a different Availability Zone, minimizing downtime and ensuring a reliable user experience.

## Infrastructure Setup
The foundational environment for this project consists of:
* **Two Amazon EC2 Instances:** Both instances are fully configured with a LAMP (Linux, Apache, MySQL, PHP) stack and host a custom café website.
* **Multiple Availability Zone Deployment:** To ensure high availability, the EC2 instances are deployed in two separate Availability Zones (e.g., `us-west-2a` and `us-west-2b`). 

## What I Implemented
To achieve automated failover and monitoring, I successfully configured the following AWS components:

### 1. Route 53 Health Checks & Alerts
I created a Route 53 health check to continuously monitor the HTTP endpoint of the primary EC2 instance. I integrated this health check with an alarm system so that if the primary instance becomes unresponsive or unhealthy, I immediately receive an email notification alerting me to the outage.

### 2. Failover Routing
I configured DNS records in Amazon Route 53 using a failover routing policy:
* **Primary Record:** Points to the IP address of "Café Instance 1" in Availability Zone 1. Under normal conditions, all user traffic is directed here.
* **Secondary (Failover) Record:** Points to the IP address of "Café Instance 2" in Availability Zone 2. 
* **The Failover Mechanism:** Route 53 actively evaluates the health check of the primary instance. If the primary instance fails, Route 53 automatically updates the DNS routing to send all incoming user requests to the secondary instance until the primary server recovers.

## Objectives Achieved
By the end of this project, I successfully demonstrated my ability to:
- [x] Configure a **Route 53 health check** that triggers email alerts when an HTTP endpoint becomes unhealthy.
- [x] Implement **Failover Routing in Route 53** to maintain continuous application uptime across multiple Availability Zones.

## Technologies Used
* **Amazon Route 53** (DNS Management, Health Checks, Failover Routing)
* **Amazon EC2** (Web Servers)
* **Amazon SNS** (Email Alert Notifications)


---
*This project demonstrates my practical experience with AWS networking, high availability architecture, and automated disaster recovery configurations.*
