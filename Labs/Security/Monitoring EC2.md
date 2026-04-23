# AWS EC2 Monitoring and Alerting System

## Project Overview
In this project, I implemented a monitoring and alerting system for an Amazon EC2 instance to ensure system performance and security. Logging and monitoring are critical for identifying performance bottlenecks and detecting security red flags, such as unauthorized access or malware infections.

To demonstrate this, I configured an automated alerting pipeline using **Amazon CloudWatch** and **Amazon Simple Notification Service (SNS)**. I then simulated a security incident by running a stress test on the server, which successfully triggered the alarm and sent an automated incident response email. 

## Objectives Achieved
During this project, I successfully completed the following tasks:
* **Created an Amazon SNS Topic & Subscription:** Configured an email-based notification system to alert administrators of critical system events.
* **Configured a CloudWatch Alarm:** Set up a performance threshold alarm that continuously monitors the CPU Utilization of my EC2 instance.
* **Simulated a Cyberattack (Stress Test):** Logged into the EC2 instance via the command line and executed a stress test, forcing the server to 100% CPU capacity to mimic a malware infection or resource hijacking.
* **Validated the Alerting Pipeline:** Confirmed the successful delivery of the SNS email alert the moment the CPU threshold was breached.
* **Built a CloudWatch Dashboard:** Created a centralized, visual dashboard to monitor real-time metrics and system health at a glance.

## Implementation Steps

### 1. Alerting Infrastructure (Amazon SNS)
I started by creating an SNS topic dedicated to system alerts. I subscribed my email address to this topic so that any critical performance anomalies would be pushed directly to my inbox in real-time.

### 2. Performance Monitoring (Amazon CloudWatch)
I created a CloudWatch Alarm tied specifically to the EC2 instance's `CPUUtilization` metric. I configured the alarm to trigger a state change (and publish a message to my SNS topic) if the CPU usage exceeded a designated safe threshold.

### 3. Incident Simulation & Validation
To test the resilience and responsiveness of my alerting system, I accessed the EC2 Linux instance and ran a stress-testing command. This rapidly consumed the server's compute resources, pushing CPU utilization to 100%. Within minutes, CloudWatch detected the anomaly, shifted the alarm to the `ALARM` state, and successfully triggered the SNS email notification to my inbox.

### 4. Visualizing Data
Finally, I built a custom **CloudWatch Dashboard**. This provided a single pane of glass to view the CPU utilization graphs, making it easier to track performance trends and quickly identify when the baseline was exceeded during the stress test.

## Technologies & Services Used
* **Compute:** Amazon EC2 (Linux)
* **Monitoring:** Amazon CloudWatch (Metrics, Alarms, Dashboards)
* **Messaging & Alerting:** Amazon SNS (Simple Notification Service)
* **System Administration:** Linux command-line utilities (Stress testing)

## Conclusion
This project gave me experience in proactive cloud security and monitoring. 
