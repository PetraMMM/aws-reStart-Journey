# Automated Storage Management & Data Recovery

> **The Goal:** I wanted to move away from manual backups and set up a reliable, automated system for managing data on AWS. I focused on protecting EBS volumes and ensuring data redundancy using S3.

---
<img width="400" height="290" alt="image" src="https://github.com/user-attachments/assets/839fdf02-001b-4dd6-ae17-adb15ef48079" />

### What I Accomplished

*   **Used Snapshot Management**  
    I used the **AWS CLI** to create point-in-time backups (snapshots) of my EBS volumes. This ensures that if anything goes wrong with a server, the data is safe and recoverable.

<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/ebfe99cf-2eb9-4be6-a032-3c080ec9d413" />


*   **Automated Maintenance with Python**  
    To keep things clean and cost-efficient, I configured a **scheduler to run Python scripts**. This automation automatically deletes older snapshots, so I only keep the backups I actually need.

<img width="800" height="355" alt="image" src="https://github.com/user-attachments/assets/980d919e-4d2e-4c47-b91c-8217e8f832e1" />


*   **Cloud Data Syncing**  
    I tackled a challenge to sync local directories from an EBS volume directly to an **Amazon S3 bucket**. I used the `s3 sync` command, which is much faster than manual copying because it only uploads new or changed files.

*   **Built-in Data Protection**  
    I enabled **S3 Versioning**, which allowed me to easily retrieve files that were accidentally deleted or overwritten, providing an extra layer of "undo" for the project.

<img width="800" height="190" alt="image" src="https://github.com/user-attachments/assets/9f7d563f-31f3-456d-a660-f58166999268" />


---

### My Environment Setup
For this project, I managed a **VPC** with two specific EC2 instances:
1.  **Command Host:** My central "control tower" for administering all AWS resources.
2.  **Processor:** The worker instance where the actual data lived.

### Key Takeaway
This project taught me that **automation is key** to professional cloud management. Instead of clicking buttons, I learned how to use scripts and the CLI to make storage reliable and self-sustaining.
