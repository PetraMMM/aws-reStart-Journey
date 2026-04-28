# Cloud Cost Optimization: Right-Sizing AWS Resources

## Overview
In this project my task was to optimize the cloud computing resources for a live web application (the Café app) to reduce AWS service costs. 

Following a successful migration of the application's database to Amazon RDS, the primary web server was left over-provisioned. I identified key opportunities to right-size the environment, including downsizing compute power to align with the application's new architecture.

## Objectives Achieved
Through this activity, I successfully demonstrated my ability to:
* **Optimize an Amazon EC2 instance** to reduce ongoing operational storage and compute costs.
* **Right-size infrastructure** based on updated application requirements.
* **Use the AWS Pricing Calculator** to forecast and estimate AWS service expenses accurately.

## Project Execution & Business Value

### 1. Storage Optimization (Cleanup)
Because the database was successfully migrated to a managed Amazon RDS instance in a previous phase, the local database software running on the web server was obsolete. I uninstalled this local database from the EC2 instance, which immediately decreased the instance's storage requirements and eliminated unnecessary EBS volume costs.

### 2. Compute Optimization (Downsizing)
With the heavy database processes no longer consuming CPU and memory on the web server, the original instance size was overpowered for simply serving web traffic. To maximize cost-efficiency, I downsized the instance type to a `t3.micro`. This adjustment cut hourly compute costs while maintaining the performance necessary for the web application to run smoothly.

## Conclusion
By actively monitoring resource utilization and adjusting infrastructure to match actual demand, I ensured that the business only pays for what it truly needs without sacrificing application performance.
