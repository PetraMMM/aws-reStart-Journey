# AWS SimuLearn Project: Serverless File Sharing for a Pet Modeling Agency

## Project Overview

In this hands-on AWS SimuLearn project, I stepped into the role of a cloud solution architect to tackle a real-world business challenge for a fictional pet modeling agency. The agency needed a robust, scalable method to share files seamlessly across its various branch offices *without* the overhead of managing physical storage infrastructure. This assignment required analyzing different AWS storage options and designing a solution that met their needs before transitioning to a live environment to build and validate the proposed architecture.

## objectives & Key Accomplishments

Through this project, I successfully achieved the following technical and analytical objectives:

* **Storage Evaluation:** Evaluated multiple AWS storage services, weighing factors like access patterns, performance, cost, and manageability to identify the optimal solution for shared file access.
* **Deep Dive into Amazon EFS:** Thoroughly analyzed the key features and benefits of **Amazon Elastic File System (Amazon EFS)**, understanding its elastic nature, concurrent access capabilities, and durability guarantees.
* **Scenario-Based Application:** Applied **Amazon EFS** as the core solution to address the agency's specific centralized file-sharing requirement.
* **Configuration:** Implemented and configured Amazon EFS access points and mount targets to enable centralized and secure storage access from multiple **Amazon EC2** instances.

## Solution Architecture & Build

After designing the solution, I transitioned to a live AWS Management Console environment to build and validate the architecture through structured, step-by-step guidance.

**Key Technical Steps Completed:**

1.  **IAM & Security:** Identified and configured necessary **IAM permissions** and security groups to ensure secure communication between services.
2.  **EC2 Provisioning:** I launched and configured several **Amazon EC2** Linux instances to simulate the agency's different branch offices or servers needing access to the shared files.
3.  **Amazon EFS Deployment:** I successfully created a new Amazon Elastic File System and configured its mount targets within the same Virtual Private Cloud (VPC) as the EC2 instances.
4.  **Verification & Mounting:** Finally, I successfully mounted the Amazon EFS file system onto each EC2 instance and verified that files created on one instance were immediately accessible and modifiable from the other instances, demonstrating a robust and truly shared storage solution.

## How it works (SimuLearn Component)

This project unique utilized **AWS SimuLearn**, which is powered by generative AI. I gained practical experience by having life-like conversations with AI-generated customers to gather requirements and present my design.

* **Generative AI Conversations:** Engaged in iterative dialogues to improve soft skills like communication and problem-solving.

## Final Result

By integrating both the soft-skill simulation and the hard-skill technical build, I successfully deployed a working, scalable, serverless file-sharing solution for the pet modeling agency, confirming that Amazon EFS provides the perfect balance of ease of use, concurrent access, and scalability for this real-world scenario.
