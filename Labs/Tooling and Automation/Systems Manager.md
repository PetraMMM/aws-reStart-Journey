# AWS Systems Manager: Centralized Operations & Automation

In this project, I utilized **AWS Systems Manager** to centralize operational data and automate management tasks across Amazon EC2 instances. 

## Project Objectives
I successfully completed the following objectives during this implementation:
* **Verify configurations and permissions:** Ensured instances were correctly configured with the necessary IAM roles to communicate with the Systems Manager service.
* **Run tasks on multiple servers:** Used **Run Command** to execute scripts and administrative tasks across a fleet of instances simultaneously.
* **Update application settings:** Streamlined the process of updating configurations across my environment without manual intervention.
* **Access the command line:** Utilized **Session Manager** to gain secure, browser-based shell access to instances without opening port 22.

---

## Capabilities Implemented

### 1. Verification & Compliance
I verified that the SSM Agent was active and that the instances possessed the appropriate permissions. This allowed for seamless communication between the AWS console and the remote resources.

### 2. Automation at Scale
Instead of logging into servers individually, I used Systems Manager to:
* Execute shell scripts across multiple instances.
* Install and update software packages.
* Verify the status of services across the entire fleet.

<img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/a0025429-f3c1-46fa-8b76-c7d8a36cfef2" />


### 3. Secure Session Management
I replaced traditional SSH methods with **Session Manager**. This allowed me to:
* Access the command line directly from the AWS Console.
* Improve security by closing inbound SSH ports on Security Groups.

<img width="455" height="360" alt="image" src="https://github.com/user-attachments/assets/1028e705-b719-465f-8dca-0c408514d679" />


---

## Conclusion
This project demonstrated how to effectively use AWS Systems Manager to simplify cloud operations. By automating repetitive tasks and centralizing resource management, I improved operational efficiency and strengthened infrastructure security.

**Key Tools Used:** 
* AWS Systems Manager (Run Command, Session Manager)
* Amazon EC2
* IAM (Identity and Access Management)
