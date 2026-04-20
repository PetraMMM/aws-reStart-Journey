# AWS Security Project: Restricted Access for Support Engineers

## Project Description
In this project, I addressed a simulated business scenario for a stock exchange. The organization needed to enhance its security controls by ensuring that support engineers had access only to the specific actions required for their roles. 

<img width="380" height="260" alt="image" src="https://github.com/user-attachments/assets/6135f6e4-75f6-45eb-b052-7bcd658c014e" />


## What I Have Accomplished
I have successfully designed, implemented, and validated a security architecture within a live AWS environment. My work included the following:

* **Identity Architecture:** I analyzed the differences between IAM users, roles, and groups to determine the best structure for the support team. I created a hierarchical access model that simplifies management while maintaining high security.
* **Environment Validation:** I deployed and tested the permissions in a live AWS Management Console. I have logged in as a support-engineer-1 user and I tried to terminate the EC2 Instance. That action failed, as this role did not have the permission to terminate the instance.

<img width="800" height="250" alt="image" src="https://github.com/user-attachments/assets/84df0046-6cfe-4d0b-a356-4d0732596cc7" />



## Technical Objectives and Skills
Through this project, I have demonstrated the following competencies:

* **Access Management:** Implementing secure access controls to protect sensitive financial infrastructure.
* **Policy Analysis:** Evaluating and troubleshooting complex IAM policies to ensure correct permission boundaries.
* **Security Best Practices:** Applying IAM best practices, such as using groups for permissions and avoiding the use of root accounts for daily tasks.
* **Cloud Compliance:** Explaining how AWS compliance programs and the Shared Responsibility Model protect organizational data.

## AWS Services Used
* **AWS Identity and Access Management (IAM):** To create users, groups, roles, and fine-grained permission policies.
* **Amazon Elastic Compute Cloud (EC2):** To manage and secure compute resources used by the engineering team.
* **Amazon Relational Database Service (RDS):** To implement data-layer security and restrict access to backend financial databases.

## Summary of Results
I successfully transformed a business security requirement into a functional technical solution. By restricting engineer access to only the necessary API calls for EC2 and RDS, I reduced the risk of accidental or malicious configuration changes. This project confirms my ability to use professional AWS tools to build secure, scalable, and compliant cloud infrastructures.
