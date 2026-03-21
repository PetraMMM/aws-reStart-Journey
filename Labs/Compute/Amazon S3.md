
# AWS Lab: Automating Amazon S3 for Secure Media Collaboration

## Project Overview

In this lab, I successfully created and configured an **Amazon Simple Storage Service (Amazon S3)** solution designed to facilitate secure file sharing and automated change notifications. I established a process for a media company (acting as an external user, `mediacouser`) to upload product images for a café. The core achievement was integrating security and automation: I implemented fine-grained access control and an automated email notification system to immediately alert administrators whenever the bucket contents are modified.

## Objectives Accomplished

I have accomplished the following technical objectives:

* **S3 API Mastery:** I utilized the **s3api** and **s3** AWS CLI (Command Line Interface) commands to create and fully configure the target S3 bucket programmatically.
* **Security Verification:** I validated the **IAM permissions** for the external `mediacouser` to ensure they had appropriate 'write' permissions to modify the bucket contents.
* **Event Automation:** I successfully configured **Amazon S3 Event Notifications** to automatically trigger an email alert when the bucket is modified.

## Project Architecture and Workflow

The following diagram illustrates the solution's component architecture and the data flow I implemented:

![Amazon S3 File Sharing Solution Architecture and Flow](https://raw.githubusercontent.com/your-username/your-repository/main/architecture-diagram.png)

### Deployed Workflow:

1.  **Media Upload:** An external user at the media company signs in to the AWS Management Console (or uses the AWS CLI) as `mediacouser`.
2.  **S3 Action:** Based on pre-verified IAM permissions, the user uploads new product pictures or updates existing ones in the S3 bucket.
3.  **Automated Trigger:** When Amazon S3 detects this change, it immediately publishes an event notification to a dedicated **Amazon SNS (Simple Notification Service)** topic named `s3NotificationTopic`.
4.  **Admin Alert:** The café administrator, who is subscribed to the `s3NotificationTopic`, receives an automated email message containing details about the modifications made to the bucket.

## Implementation Details

### Step 1: Programmatic S3 Bucket Management

I used the **AWS CLI** to create and configure the S3 bucket. This included using advanced `s3api` commands to refine bucket settings that are not available in standard `s3` commands.

```bash
# Example: Creating the bucket (ensure the name is globally unique)
aws s3api create-bucket --bucket cafe-media-assets --region us-west-2
