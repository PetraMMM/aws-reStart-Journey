# Working with Amazon EBS Storage

> **The Goal:** I wanted to understand how to manage high-performance block storage in the cloud. In this project, I handled the entire lifecycle of an Amazon EBS volume—from creation to backup and recovery.

---

<img width="420" height="90" alt="image" src="https://github.com/user-attachments/assets/56605e85-b90e-4e7d-ada2-4fb53e5a20fa" />


###  What I Accomplished

*   **Provisioned Block Storage**  
    I started by creating a custom **Amazon EBS volume**. I learned how to choose the right size and type to match the performance needs of a cloud application.

*   **Connected Storage to Compute**  
    I successfully **attached and mounted** the EBS volume to a running EC2 instance. This involved not just the AWS Console/CLI steps, but also working within the Linux terminal to create a filesystem so the instance could actually use the space.

*   **Data Protection & Backups**  
    I took a **snapshot** of my volume. This taught me how to create point-in-time backups that are stored durably in S3, ensuring that my data is safe even if the original volume is deleted.

*   **Rapid Recovery & Scaling**  
    I proved my backup worked by **creating a brand new EBS volume from my snapshot**. This is a key skill for migrating data between zones or recovering from a system failure.

---

###  Key Takeaway
This project gave me practical experience in managing persistent storage. I now know how to scale capacity on the fly and ensure that critical data is backed up and ready to be restored in seconds.
