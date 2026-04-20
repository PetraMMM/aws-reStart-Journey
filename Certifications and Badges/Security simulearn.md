# AWS Security Project: Restricted Access for Support Engineers

## Project Description
In this project, I addressed a simulated business scenario for a stock exchange. The organization needed to enhance its security controls by ensuring that support engineers had access only to the specific actions required for their roles. I was responsible for designing and building a secure access management solution that prevents unauthorized changes while allowing engineers to perform their daily duties efficiently.

## What I Have Accomplished
I have successfully designed, implemented, and validated a security architecture within a live AWS environment. My work included the following:

* **Identity Architecture:** I analyzed the differences between IAM users, roles, and groups to determine the best structure for the support team. I created a hierarchical access model that simplifies management while maintaining high security.
* **Granular Policy Engineering:** I broke down the structure of IAM policies to understand how Version, Statement, Effect, Action, and Resource components interact. I wrote and applied JSON-based policies to enforce the Principle of Least Privilege.
* **Shared Responsibility Implementation:** I evaluated the AWS Shared Responsibility Model to ensure that my configurations met compliance standards and that I was properly managing the security configurations "in" the cloud.
* **Environment Validation:** I deployed and tested these permissions in a live AWS Management Console, specifically managing access to Amazon EC2 instances and Amazon RDS databases.
* **Soft Skill Development:** I used generative AI simulation tools to consult with fictional customers, translating business requirements into technical security specifications.

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
