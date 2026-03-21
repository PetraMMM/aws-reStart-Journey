
# Working with Amazon S3 for Secure Media Collaboration

## Project Overview

In this lab, I successfully designed and deployed a secure file-sharing and notification system using **Amazon Simple Storage Service (Amazon S3)**. The solution enables a media company (an external user, `mediacouser`) to upload and update product images for a café, while ensuring automated security alerts. The core focus was on implementing access control and an automated email notification to immediately alert administrators of any bucket modifications.

<img width="500" height="340" alt="image" src="https://github.com/user-attachments/assets/6447d956-1ea3-4949-bc58-3f2a3bf35c62" />

## Objectives Accomplished

I have accomplished the following technical objectives:

* **S3 CLI Administration:** I utilized the **s3api** and **s3** AWS CLI commands to programmatically create and fully configure the S3 bucket.
* **Permissions Validation:** I validated **IAM permissions** for the external `mediacouser`, ensuring they possessed the appropriate, minimum necessary 'write' privileges to manage the bucket contents securely.

<img width="500" height="340" alt="image" src="https://github.com/user-attachments/assets/ac1cf1d7-9ba0-425f-b423-d6944457e0ca" />
<img width="500" height="340" alt="image" src="https://github.com/user-attachments/assets/2295fdcb-dbc4-4ea0-abd5-d56a1af727e7" />


* **Notification Automation:** I successfully implemented **Amazon S3 Event Notifications**, configuring the bucket to automatically trigger an email alert when contents are added, modified, or removed.

## Solution Flow

1.  **Secure Upload:** The media company (signed in as `mediacouser`) uploads or modifies product images in the S3 bucket via the AWS Console or CLI.
2.  **Automated Trigger:** When Amazon S3 detects this change, it instantly publishes a notification to a dedicated **Amazon SNS (Simple Notification Service)** topic.
3.  **Admin Alert:** The café administrator, subscribed to the SNS topic, immediately receives an email detail describing the changes made, ensuring visibility and accountability.

<img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/1e7b6740-a849-4988-b8e3-c4869aa6882c" />


**Learning Outcomes:** This project provided practical experience in leveraging the **AWS CLI** for S3 management, understanding **IAM security** integration, and automating cloud workflows by linking **S3 and SNS**.
