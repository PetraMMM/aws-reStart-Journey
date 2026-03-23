
<img width="1567" height="749" alt="image" src="https://github.com/user-attachments/assets/4563563d-8963-4d10-a4cf-2e25e9bea212" />

## The Quiet Kettle Static Website Project

## Project Overview

Welcome to "The Quiet Kettle," a static e-commerce website designed for a boutique tea shop. This project represents the successful development and cloud deployment of a clean, minimalist, and inviting online presence, focusing on creating a serene experience for users.

This project was a collaborative group effort.

## Site Structure

The website consists of 5 main pages, all accessible via the global navigation menu:

* **Home:** (Visualized in the header) Introduces the brand, features a curated image/banner, a newsletter signup section, and highlights "Our Monthly Arrivals."
* **Shop:** The main catalog page showcasing the full range of available teas.
* **About:** The story and mission behind The Quiet Kettle.
* **Contact:** How to get in touch with us.
* **Login:** A portal for existing customers.

## Technology Stack

* **Development:** All HTML and CSS code was authored using **Visual Studio Code**.

   ![Screen shots of the bucket](https://github.com/PetraMMM/aws-reStart-Journey/blob/main/Projects/Static%20Website%20/Screenshots/CreatingBucket.md)

* **Deployment:** The project is a purely static website. It is **hosted as a static website on an Amazon S3** (Simple Storage Service) bucket. The Bucket was created in the AWS Management Console.  The Bucket´s name was "the-quiet-kettle". We have enabled public access and bucket policies, uploaded files (html files for each page and pictures)  and we hosted the web page at ```
[http://the-quiet-kettle.s3-website-us-west-2.amazonaws.com/login.html]```.

 ![Screen shots of the bucket](https://github.com/PetraMMM/aws-reStart-Journey/blob/main/Projects/Static%20Website%20/Screenshots/CreatingBucket.md)
* **Assets:** Original product photography of the teas and other media were integrated directly into the HTML structure.

## Deployment Screenshot

![The Quiet Kettle Screenshots](https://github.com/PetraMMM/aws-reStart-Journey/blob/main/Projects/Static%20Website%20/Screenshots/FinalWebPages.md)



## Challenges & Solutions

A significant challenge we faced during the final deployment was a missing product image from one of the pages. Upon investigation within the AWS console, we discovered that the specific image file had not been included in our initial bulk upload bundle with the HTML files.

**Solution:**

We successfully resolved this by locating the correct image asset and uploading it separately and directly into the designated folder structure within the Amazon S3 bucket. This verified that the issue was not with the HTML code's reference path, but strictly a deployment asset transfer error. The website now displays correctly all pages.

## Group Contributors

We would like to thank all the group members who contributed to this project's success.
