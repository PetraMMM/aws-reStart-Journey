
# AWS Lab: Automating Amazon S3 for Secure Media Collaboration

## Project Overview

In this lab, I successfully designed and deployed a secure file-sharing and notification system using **Amazon Simple Storage Service (Amazon S3)**. The solution enables a media company (an external user, `mediacouser`) to upload and update product images for a café, while ensuring automated security alerts. The core focus was on implementing fine-grained access control and an automated email notification pipeline to immediately alert administrators of any bucket modifications.

## Objectives Accomplished

I have accomplished the following technical objectives:

* **S3 CLI Administration:** I utilized the **s3api** and **s3** AWS CLI commands to programmatically create and fully configure the S3 bucket.
* **Permissions Validation:** I validated **IAM permissions** for the external `mediacouser`, ensuring they possessed the appropriate, minimum necessary 'write' privileges to manage the bucket contents securely.
* **Notification Automation:** I successfully implemented **Amazon S3 Event Notifications**, configuring the bucket to automatically trigger an email alert when contents are added, modified, or removed.

## Solution Flow

I implemented an automated pipeline that connects multiple AWS services:
1.  **Secure Upload:** The media company (signed in as `mediacouser`) uploads or modifies product images in the S3 bucket via the AWS Console or CLI.
2.  **Automated Trigger:** When Amazon S3 detects this change, it instantly publishes a notification to a dedicated **Amazon SNS (Simple Notification Service)** topic.
3.  **Admin Alert:** The café administrator, subscribed to the SNS topic, immediately receives an email detail describing the changes made, ensuring visibility and accountability.

**Learning Outcomes:** This project provided practical experience in leveraging the **AWS CLI** for S3 management, understanding **IAM security** integration, and automating cloud workflows by linking **S3 and SNS**.
