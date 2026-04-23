# AWS Identity and Access Management (IAM) Implementation

## Project Overview
In this project, I implemented and tested role-based access control using **AWS Identity and Access Management (IAM)**. Securing access to cloud resources is critical to prevent unauthorized exploitation. My objective was to enforce the principle of least privilege by configuring users, user groups, and specific IAM policies to ensure individuals only had access to the AWS services they strictly needed.

<img width="500" height="230" alt="image" src="https://github.com/user-attachments/assets/48126150-1adb-4241-8373-a25e9aa8a042" />


## Key Implementations
To establish a secure access framework, I successfully completed the following tasks:
* **Enforced Password Policies:** I created and applied a custom IAM password policy to ensure strong authentication standards across the AWS account.

<img width="500" height="340" alt="image" src="https://github.com/user-attachments/assets/6b7b0cf8-3117-4bee-99a3-a8eec403a6c8" />


* **Managed Users & Groups:** I explored, categorized, and assigned IAM users into specific user groups based on their required operational capabilities.
* **Inspected & Applied IAM Policies:** I analyzed the JSON-based IAM policies attached to these groups to understand exactly what permissions were being granted or explicitly denied.
* **Custom Access Routing:** I located and utilized the dedicated IAM sign-in URL to securely route users into the environment.

## Security Validation & Testing
To verify that the IAM policies were working exactly as intended, I conducted hands-on testing by logging in via the IAM sign-in URL as three different users with distinct permission sets. I validated the following:

* **User-1 (Storage Focus):** I verified that this user could successfully view Amazon S3 buckets, but their access was strictly denied when attempting to view or interact with Amazon EC2 instances.

<img width="500" height="168" alt="image" src="https://github.com/user-attachments/assets/52ff0fe5-82e7-4946-92ed-5bd4ac24709d" />


* **User-2 (Compute Read-Only Focus):** I confirmed this user could view EC2 instances but lacked the administrative permissions to alter them (e.g., they could not stop an instance). Additionally, they were completely denied access to view S3 buckets.
* **User-3 (Compute Admin Focus):** I verified that this user had elevated compute permissions, allowing them to successfully view EC2 instances and execute administrative commands, such as stopping a running instance.

<img width="530" height="165" alt="image" src="https://github.com/user-attachments/assets/5028e3c2-956e-42af-b2bb-698765b88b0d" />


## Technologies & Services Used
* **Security & Identity:** AWS Identity and Access Management (IAM)
* **Compute:** Amazon EC2
* **Storage:** Amazon S3
* **Concepts:** Principle of Least Privilege, Role-Based Access Control, Password Policies

## Conclusion
Through this project I enhanced my understanding of cloud security fundamentals. By testing the effects of different policies on service access, I demonstrated how to effectively secure an AWS environment, and segment user permissions.
