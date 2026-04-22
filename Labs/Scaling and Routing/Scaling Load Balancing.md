# Scaling and Load Balancing AWS Architecture

## Project Overview
In this project, I designed and implemented a highly available, fault-tolerant, and dynamically scalable infrastructure on AWS. By leveraging **Elastic Load Balancing (ELB)** and **Amazon EC2 Auto Scaling**, I built an environment capable of automatically adjusting its compute capacity based on traffic demands while efficiently distributing incoming traffic across multiple instances. 

This architecture ensures that the application remains highly available during traffic spikes and cost-optimized during downtimes, all without requiring manual intervention.


<img width="450" height="300" alt="image" src="https://github.com/user-attachments/assets/db8d8017-35cb-47be-b18b-7f406bc8be92" />
<img width="450" height="300" alt="image" src="https://github.com/user-attachments/assets/367d8150-b2fc-49ec-928e-33a92de28543" />


## What I Implemented

To achieve a resilient and self-healing infrastructure, I successfully completed the following tasks:

* **Custom AMI Creation:** I created an Amazon Machine Image (AMI) from a pre-configured EC2 instance. This AMI image served as the reliable baseline for all newly provisioned servers.
* **Elastic Load Balancing (ELB):** I deployed a load balancer to automatically distribute incoming application traffic evenly across my fleet of EC2 instances, preventing any single instance from becoming a bottleneck.
* **Auto Scaling Configuration:** I created a **Launch Template** linked to my custom AMI and established an **Auto Scaling group**. This allowed the infrastructure to automatically scale out (add instances) or scale in (remove instances) based on real-time conditions.

<img width="517" height="109" alt="image" src="https://github.com/user-attachments/assets/743af2f3-2505-4294-974f-39a367cb6aa0" />


* **Secure Network Placement:** For enhanced security, I configured the Auto Scaling group to strictly provision new EC2 instances within **private subnets**, shielding them from direct internet access while still receiving traffic via the load balancer.
* **CloudWatch Monitoring & Alarms:** I utilized **Amazon CloudWatch** to monitor the performance of the infrastructure. I set up alarms based on specific metrics (such as CPU utilization) to automatically trigger the Auto Scaling policies.

<img width="500" height="270" alt="image" src="https://github.com/user-attachments/assets/506c0c67-634d-4b8d-ae29-b8a8fd0c2810" />



## Technologies & Services Used
* **Compute:** Amazon EC2, Amazon Machine Images (AMI)
* **Scaling & Traffic Routing:** Amazon EC2 Auto Scaling, Elastic Load Balancing (ELB), Launch Templates
* **Networking & Security:** Amazon VPC (Private & Public Subnets)
* **Monitoring:** Amazon CloudWatch (Metrics & Alarms)

## Conclusion
Through this project, I gained hands-on experience in building cloud-native, elastic architectures. I learned how to configure environments, that automatically respond to changes in demand, ensuring stable application performance, fault tolerance, and optimized cloud usage costs.
