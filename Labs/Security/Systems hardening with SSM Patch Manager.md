# Systems Hardening with AWS Systems Manager (Patch Manager)

## Project Overview
In enterprise environments with hundreds or thousands of servers, keeping operating systems and applications consistently up-to-date is a massive logistical challenge. In this project, I engineered a scalable, automated solution to maintain strict security policies and software baselines across a mixed-OS fleet of servers. 

Using **Patch Manager**, a capability of AWS Systems Manager, I automated the process of scanning, deploying, and verifying critical OS updates across both Windows and Linux Amazon EC2 instances to ensure infrastructure compliance and system hardening.

## Key Implementations & Achievements
To achieve a secure and compliant environment, I successfully completed the following tasks:

* **Automated Linux Patching:** I leveraged AWS-managed default patch baselines to automatically scan and apply necessary security updates to a fleet of Amazon Linux EC2 instances.
* **Custom Windows Patch Baselines:** I designed and created a custom patch baseline tailored specifically for the Windows Server environment, defining exact rules for auto-approving patches based on classification and severity.
* **Targeted Rollouts via Patch Groups:** I utilized AWS tags to organize my infrastructure into logical **Patch Groups**. This allowed me to safely target specific groups of Windows instances to receive the custom patch baseline without disrupting other environments.
* **Compliance Verification:** After executing the patching operations, I used Systems Manager to audit the fleet, successfully verifying patch compliance and confirming that no instances were missing critical security updates.

<img width="500" height="240" alt="image" src="https://github.com/user-attachments/assets/07b58e53-6808-4cef-83b7-2652d273ba75" />


## Technologies & Services Used
* **Operations & Automation:** AWS Systems Manager (Patch Manager, Run Command)
* **Compute:** Amazon EC2 (Windows Server, Linux)
* **Security Concepts:** Systems Hardening, Patch Management, Compliance Auditing, Fleet Management

## Conclusion
This project provided me with practical experience in automated cloud infrastructure management. I learned how to establish secure patching baselines, orchestrate updates across a diverse fleet of servers, and guarantee that organizational compliance standards are strictly met.
