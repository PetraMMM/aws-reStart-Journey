# AWS Monitoring and Compliance Infrastructure

## Project Overview
In this project, I designed and implemented a comprehensive monitoring and compliance tracking solution for AWS applications and infrastructure. I built a system capable of collecting statistics for long-term analysis, reacting quickly to system changes or outages, and continuously reporting on infrastructure compliance against organizational standards.

## Key Implementations & Achievements
To achieve a fully monitored and compliant environment, I successfully completed the following objectives:

* **Automated Agent Deployment:** I utilized the **AWS Systems Manager (SSM) Run Command** to remotely and efficiently install the CloudWatch agent across my Amazon EC2 instances without needing manual SSH access.

<img width="507" height="325" alt="image" src="https://github.com/user-attachments/assets/e2ba5271-fb5f-4c7f-b707-89f9381eef67" />


* **Centralized Log Management:** I configured the CloudWatch agent to stream application logs directly into **Amazon CloudWatch Logs**, enabling centralized troubleshooting and analysis.
* **System Resource Monitoring:** I set up **Amazon CloudWatch Metrics** to track performance metrics (such as memory and disk usage) that are not captured by default EC2 monitoring.
* **Real-Time Alerting:** I engineered automated, real-time notifications using **Amazon CloudWatch Events** (EventBridge) to immediately alert on critical state changes within the infrastructure.
* **Continuous Compliance Auditing:** I deployed **AWS Config** to continuously monitor, record, and evaluate the configurations of my AWS resources, ensuring they strictly adhere to defined organizational security and compliance standards.

<img width="500" height="360" alt="image" src="https://github.com/user-attachments/assets/23b6dbf2-d2f5-431d-acbe-a9432e9772d3" />


## Technologies & AWS Services Used
* **Compute:** Amazon EC2
* **Operations & Management:** AWS Systems Manager (Run Command)
* **Observability:** Amazon CloudWatch (Logs, Metrics, Events)
* **Security & Compliance:** AWS Config

## Conclusion
Through this project, I gained practical experience in establishing a robust observability framework in the cloud. 
