
# AWS Challenge Lab: Amazon S3 

## Project Overview

In this hands-on challenge lab, I successfully created and configured an **Amazon Simple Storage Service (Amazon S3)** bucket. I performed routine, essential cloud storage tasks, focusing on object lifecycle management and security access controls. The project culminated in deploying a sample web asset and verifying its availability through both a standard web browser and the AWS Command Line Interface (AWS CLI).

## Objectives Completed

By the end of this challenge, I had achieved the following milestones:

* **S3 Bucket Creation:** I successfully created a globally unique S3 bucket (demo-pm3) to host static content.
* **Object Upload:** I uploaded a picture into the newly created bucket.
* **Public Access Configuration:** I configured the bucket permissions and object policies to allow the object to be accessed publicly via a standard web browser.
* **CLI Verification:** I listed the contents of the S3 bucket using the AWS CLI, confirming the successful upload and verifying the setup programmatically.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/111562dd-64e5-4968-aee3-a94162de4f4b" />


## Technical Walkthrough

### 1. Creating the S3 Bucket

My first step was to log into the AWS Management Console and navigate to the S3 service. I created a new bucket with a unique name, adhering to AWS naming conventions. During the creation process, I ensured that "Block All Public Access" was *not* fully enabled, which was a necessary prerequisite for the public accessibility testing later in the lab.

![AWS Console showing bucket creation in progress](https://via.placeholder.com/600x400.png?text=Placeholder:S3+Bucket+Creation+Console)

### 2. Uploading the Object

Once the bucket was active, I navigated into it and initiated an upload. I chose a simple file (e.g., `sample_web_page.html`) to serve as our target object. The upload process was quick, and the file was visible in the bucket objects list.

### 3. Enabling Public Access

This was the core challenge of the lab. To make the object publicly viewable through a browser, I had to configure two layers of security permissions:

1.  **Bucket-level Permissions:** I updated the bucket's "Block public access" settings to allow specific public permissions.
2.  **Object-level Access Control (ACL):** I directly modified the Access Control List (ACL) of the `sample_web_page.html` object, explicitly granting "Read" permissions to everyone.

This configuration is critical for static website hosting scenarios.

### 4. Verification

#### Web Browser Access

To verify the public access, I navigated to the "Properties" tab of the uploaded file in the AWS Console. I copied the unique **Object URL** (e.g., `https://my-unique-bucket-name.s3.amazonaws.com/sample_web_page.html`).

I then opened a new private (incognito) browser window and pasted the URL. The `sample_web_page.html` content loaded successfully, confirming that the public access configuration was working as intended.

#### AWS CLI Verification

The final step was to verify the setup from the command line. Using a terminal configured with AWS CLI access, I executed the following command:

```bash
aws s3 ls s3://my-unique-bucket-name
