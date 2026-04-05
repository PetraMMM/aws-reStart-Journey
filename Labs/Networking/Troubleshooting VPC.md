# Troubleshooting a VPC: Network Analysis & Configuration

This project documents my process of diagnosing and resolving connectivity issues within a multi-VPC AWS environment. I focused on using **VPC Flow Logs** and **Amazon S3** to identify bottlenecks and misconfigurations in network traffic.

---

## Project Overview

In this lab, I managed an environment featuring two separate VPCs, EC2 instances, and various networking components. The primary goal was to restore seamless communication between resources by systematically identifying and fixing configuration errors.

I followed a structured methodology to move from a state of total connectivity loss to a fully functional, monitored network.

<img width="800" height="415" alt="image" src="https://github.com/user-attachments/assets/0f4a8377-4903-42d1-a22d-959cb1df9791" />


### Key Tasks Performed:

*   **Storage Provisioning:** I created a dedicated **Amazon S3 bucket** to act as the centralized repository for network telemetry.
*   **Traffic Capture:** I configured **VPC Flow Logs** to capture all IP traffic (accepted and rejected) flowing through the network interfaces within the VPC.
*   **Network Troubleshooting:** I identified and resolved VPC configuration issues to restore access to the resources, ensuring that routing and security rules were correctly aligned.
*   **Log Analysis:** I downloaded and parsed the flow log data to verify successful traffic flow and ensure the troubleshooting steps were effective.

---

## Objectives Achieved

*   **VPC Flow Log Implementation:** Gained hands-on experience in setting up logging at the VPC level to monitor network health.
*   **Connectivity Troubleshooting:** Successfully diagnosed why specific EC2 instances could not communicate, focusing on route tables and security policies.
*   **Data Analysis:** Analyzed raw flow log fields (source/destination IP, port, protocol, and action) to distinguish between successful connections and blocked requests.

---

## Technical Stack

*   **Cloud Provider:** Amazon Web Services (AWS)
*   **Networking:** Amazon VPC, VPC Flow Logs, Security Groups, Network ACLs
*   **Storage:** Amazon S3
*   **Compute:** Amazon EC2

---

## Conclusion

Through this project, I strengthened my understanding of how to isolate network failures in a cloud environment. By using VPC Flow Logs, I moved beyond guesswork to make data-driven decisions that restored connectivity while maintaining a secure posture.
