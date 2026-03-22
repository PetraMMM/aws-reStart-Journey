
# AWS Challenge: Serverless Word Count with AWS Lambda

## Project Overview

In this challenge, I successfully designed, developed, and deployed a serverless solution using **AWS Lambda** to automate text analysis. The primary goal was to create a Python-based Lambda function that automatically counts the words in any text file uploaded to a specific **Amazon S3** bucket. The solution then leverages **Amazon Simple Notification Service (Amazon SNS)** to immediately deliver the results via email to an administrator.

## Objectives Accomplished

I achieved all specified objectives for this challenge:

* **Serverless Function Development:** I developed a robust **Python** Lambda function within the AWS Management Console to accurately count words in a text file.
* **Event-Driven Trigger:** I configured an **Amazon S3 bucket** to automatically invoke the Lambda function upon the successful upload of a text file.
* **SNS Integration:** I created and configured an **Amazon SNS Topic** to send an email notification containing the word count results to a subscribed administrator.

## Technical Walkthrough

### 1. Resource Provisioning (S3 & SNS)

My first step was to set up the necessary infrastructure:
* **S3 Bucket:** I created a dedicated S3 bucket to serve as the upload point for the text files.

<img width="350" height="180" alt="image" src="https://github.com/user-attachments/assets/dfaf51e7-ef59-4b91-a337-a8b8971731ec" />

  
* **SNS Topic:** I established an Amazon SNS topic named `WordCountResultTopic`. I created an email subscription for this topic and successfully confirmed the subscription to ensure receipt of notifications.

  <img width="350" height="180" alt="image" src="https://github.com/user-attachments/assets/e700dc81-01b7-4c02-9333-53bd7f866bdc" />


### 2. Lambda Function Development & IAM

I developed the core logic in Python 3 using the AWS Management Console's built-in code editor. The function utilizes the **Boto3 SDK** to interact with S3.

**Key Coding Logic:**
1.  **Event Parsing:** Extract the S3 bucket name and the object key (file name) from the incoming S3 event data.
2.  **S3 Download:** Use the Boto3 S3 client to download the text content from the uploaded file directly into memory.
3.  **Word Count:** Read the file content and apply standard Python string manipulation (`.split()`) to count the words accurately.
4.  **SNS Publish:** Utilize the Boto3 SNS client to publish a formatted message to the `WordCountResultTopic`. The message includes the file name and the exact word count.

For permissions, I adhered to the lab constraints and utilized a pre-existing **IAM (Identity and Access Management) role** that provided the necessary standard permissions for Lambda basic execution, Amazon SNS full access, and Amazon S3 full access.

### 3. S3 Event Trigger Configuration

I navigated back to the S3 bucket properties and configured an **Event Notification**. I specifically created a trigger to invoke my Lambda function for any `ObjectCreated` event, targeting objects with the `.txt` suffix.

### 4. End-to-End Testing

To verify the entire pipeline, I created several sample text files (e.g., `test1.txt` with "Hello, this is my first test file for Lambda.") and uploaded them to the S3 bucket.

Upon upload, the following automated sequence occurred successfully:
* S3 triggered the Lambda function.
* Lambda executed the word count logic.
* Lambda published the result to the SNS topic.
* I received an email within seconds confirming the exact word count for the specific file uploaded.

---
**Learning Outcomes:** This challenge provided practical, hands-on experience in constructing an event-driven serverless architecture, connecting multiple AWS services (S3, Lambda, SNS), and managing IAM permissions for seamless service integration.
