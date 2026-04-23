# Data Protection Using AWS Encryption

## Project Overview
In this project I implemented cryptographic data protection on an AWS file server. Understanding that cryptography is essential for keeping communicated information confidential and ensuring data integrity, my goal was to practically apply encryption and decryption techniques in a cloud environment. 

I configured a file server hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance and utilized the **AWS Key Management Service (AWS KMS)** alongside the **AWS Encryption CLI** to securely encrypt and decrypt local files, ensuring they remain unreadable to unauthorized users.

## Key Implementations & Achievements
To secure data protection, I successfully completed the following tasks:

* **Symmetric Key Generation:** I generated and managed a secure cryptographic encryption key using **AWS KMS** to serve as the foundation.

<img width="500" height="206" alt="image" src="https://github.com/user-attachments/assets/a00f6916-fe5f-4921-9c39-ea34bb080eaa" />


* **Tool Provisioning:** I installed and configured the **AWS Encryption CLI** on my EC2 instance, enabling streamlined encryption and decryption directly from the command line.
* **Plaintext Encryption:** I created standard, unencrypted text files and successfully transformed them into unreadable ciphertext using my centralized KMS key.
* **Decryption:** I reversed the process, successfully decrypting the secure ciphertext back into its original, readable plaintext format using the proper key authentication.
* **Data Verification:** I validated the integrity and confidentiality of the data at each step, verifying that the encrypted files were completely inaccessible without the proper decryption protocols.

<img width="820" height="385" alt="image" src="https://github.com/user-attachments/assets/1beda894-6fdd-4564-a79c-33853d56d2a0" />


## Technologies & Services Used
* **Compute & Storage:** Amazon EC2 (Linux File Server)
* **Security & Cryptography:** AWS Key Management Service (KMS)
* **Command Line Tools:** AWS Encryption CLI
* **Concepts:** Data Confidentiality, Cryptography, Plaintext vs. Ciphertext Transformation

## Conclusion
This project provided me with practical experience in cloud data security. I learned to provision cryptographic keys, utilize AWS encryption tooling, and securely protect sensitive data at rest.
