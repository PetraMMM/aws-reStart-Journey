
# Launching the Café & Bakery Website on AWS

> **Summary:** I moved the Café & Bakery’s website to the cloud using AWS. My goal was to create a fast, reliable, and automated hosting solution using the command line.


---

<img width="383" height="183" alt="image" src="https://github.com/user-attachments/assets/7a93d13c-4bf6-46d8-9b85-4e5e41a1715f" />

### What I Accomplished

*   **Built the Infrastructure**  
    I created an **Amazon S3 bucket pmat256** to act as the primary storage and hosting engine for the website.

    <img width="397" height="103" alt="image" src="https://github.com/user-attachments/assets/fba5c924-5ee5-4d91-8a7c-bc1e02c70d56" />
<img width="384" height="175" alt="image" src="https://github.com/user-attachments/assets/fb4fca12-7501-40da-b9bc-f1b38b599867" />
<img width="395" height="138" alt="image" src="https://github.com/user-attachments/assets/e4720980-ea83-4bb4-8dfd-8541203dff03" />

    
*   **Managed Access & Security**  
    I set up a dedicated **IAM user** with full S3 access, ensuring I had the exact permissions needed to manage the project securely.
    
*   **Launched the Site via CLI**  
    Instead of manual uploads, I used the **AWS CLI** from an EC2 instance to push the website files directly to the bucket, turning it into a live static host.
    
    <img width="395" height="307" alt="image" src="https://github.com/user-attachments/assets/fbd3f867-ed5e-4496-a9e9-49522735d03b" />


---

### Key Takeaway
This project showed me how to manage web assets efficiently using professional developer tools.
