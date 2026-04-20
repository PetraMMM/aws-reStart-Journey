# AWS Cloud Development: Python & Security Labs

## Project Overview
This repository contains a collection of projects I completed during the AWS re/Start program. These labs were developed within the AWS Cloud9 IDE, focusing on using Python to solve business logic problems and implementing robust security configurations to protect cloud infrastructure.

## What I Have Accomplished

### 1. Caesar Cipher Encryption Tool
I developed a Python application that simulates a classic Caesar Cipher to encrypt and decrypt messages. This project was centered on string manipulation and algorithmic logic.
* **Logic Development:** I built functions to shift characters through the alphabet based on a user-defined key.
* **User Experience:** I implemented interactive prompts to allow users to enter secret messages and choose between encryption or decryption modes.
* **Data Processing:** I ensured the script could handle various character types while maintaining the integrity of the original message structure.

### 2. JSON Data & File Handling
I created a script to process and format complex data structures, specifically working with JSON files—a critical skill for interacting with AWS APIs.
* **Data Parsing:** I used the `json` library to import data from external files into Python dictionaries and lists.
* **Readable Output:** I implemented the `pprint` (pretty-print) module to transform raw, dense JSON strings into human-readable formats for debugging and reporting.
* **File Integration:** I practiced reading from and writing to files within the Cloud9 environment, ensuring proper data persistence.

### 3. Restricted Access Management (Simulated Business Scenario)
Beyond pure coding, I designed a security solution for a stock exchange to restrict engineer access based on the "Principle of Least Privilege."
* **IAM Policy Engineering:** I analyzed and wrote IAM policies to define exactly what actions support engineers could take on Amazon EC2 and Amazon RDS instances.
* **Security Architecture:** I mapped out the transition from broad administrative access to role-based access control (RBAC), significantly reducing the system's attack surface.
* **Validation:** I implemented and verified these security controls in a live AWS Management Console environment to ensure compliance with the AWS Shared Responsibility Model.

## Technical Skills & Competencies
Through these Cloud9-based projects, I have demonstrated the following skills:
* **Python Programming:** Proficient in using loops, conditional logic, and built-in libraries to solve data-driven problems.
* **Cloud Security:** Deep understanding of Identity and Access Management (IAM), including roles, groups, and granular JSON policies.
* **DevOps Foundation:** Experience using a cloud-based IDE (Cloud9) to write, test, and debug code that interacts with infrastructure.
* **Problem Solving:** Translating complex business requirements (like secure financial transactions or encrypted communication) into functional technical solutions.

## Tools & AWS Services Used
* **AWS Cloud9:** The primary IDE used for coding and environment management.
* **AWS IAM:** Used to engineer security boundaries and access controls.
* **Amazon EC2 & RDS:** The target services for my security implementation labs.
* **Python 3:** The core language for my programming and automation scripts.

## Summary
These projects represent my growth as a Cloud Associate. By working within the AWS ecosystem, I have learned not just how to write code, but how to write secure, compliant, and efficient code that meets the needs of modern enterprise environments.
