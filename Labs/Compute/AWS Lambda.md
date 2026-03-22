
# AWS Lab: Deploying a Serverless Sales Analysis Reporting Solution

## Project Overview

In this lab, I successfully deployed and configured a comprehensive serverless computing solution powered by **AWS Lambda**. The system automatically generates a daily sales analysis report by extracting data from a live database and delivering the results via email. 

## System Architecture and Workflow

The following diagram illustrates the architecture of the sales analysis report solution and the automated sequence of events:

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/960f54bb-0154-41fb-a50b-81868eba9a0f" />


### Automated Workflow:

1.  **Scheduled Trigger:** An **Amazon CloudWatch Events** rule initiates the workflow every Monday through Saturday at 8 PM.
2.  **Report Orchestration:** The CloudWatch event triggers the main `salesAnalysisReport` Lambda function.
3.  **Data Extraction:** The orchestrator function invokes a second, specialized Lambda function, `salesAnalysisReportDataExtractor`.
4.  **Database Query:** The data extractor function runs an analytical query against the cafe database (`cafe_db`) hosted on an **Amazon EC2** LAMP instance. Connection details are securely retrieved from **AWS Systems Manager Parameter Store**.
5.  **Report Formatting & Delivery:** The query results are returned to the main function, which formats the report and publishes the message to an **Amazon SNS (Simple Notification Service)** topic (`salesAnalysisReportTopic`).
6.  **Email Notification:** The SNS topic delivers the finalized sales report via email to the administrator.

   <img width="350" height="300" alt="image" src="https://github.com/user-attachments/assets/a56ea567-f091-420e-9812-37cb0b02dda5" />


## Objectives Accomplished

I successfully completed the following technical objectives during this deployment:

* **IAM Permissions Management:** I identified and configured the necessary **AWS Identity and Access Management (IAM)** policy permissions required for Lambda functions to securely interact with other AWS resources (CloudWatch, SNS).
* **Lambda Layers:** I created and implemented a **Lambda layer** to manage an external library dependency, ensuring the data extractor function had the necessary tools to connect to the MySQL database.
* **Serverless Function Deployment:** I deployed the Python-based Lambda functions for both data extraction and report orchestration.
* **Scheduled Automation:** I deployed and tested the **CloudWatch Events** trigger, verifying that the scheduled invocation and cross-function calls executed correctly.
* **Troubleshooting with CloudWatch Logs:** I utilized **Amazon CloudWatch Logs** to monitor execution and troubleshoot any issues encountered during the testing of the Lambda functions.

  <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/dce3d02a-8cc5-4209-af49-70bb424be7dc" />


## Learning Outcomes

This project provided me with practical, hands-on experience in building a real-world serverless application. Key takeaways include managing IAM permissions for secure service integration, automating tasks using CloudWatch events, leveraging Lambda layers for dependency management, and using CloudWatch Logs.
