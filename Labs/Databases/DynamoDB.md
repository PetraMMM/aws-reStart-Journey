# Hands-On Introduction to Amazon DynamoDB: Building a Music Library

## Project Overview

In this project, I successfully completed a practical, hands-on introduction to **Amazon DynamoDB**, a fast, fully managed, and flexible NoSQL database service offered by AWS. This experience reinforced my understanding of DynamoDB's capabilities as both a **document** and **key-value** data model, designed for applications requiring consistent, single-digit millisecond latency at any scale.

During this lab, I deployed and managed a DynamoDB table specifically configured to store and retrieve information for a **music library**. I gained practical, job-ready competencies across the entire database lifecycle, spanning creation, data entry, querying, and deletion.

## Objectives Accomplished

I have accomplished the following technical objectives during this project:

* **DynamoDB Table Creation:** I successfully navigated the AWS Management Console to provision a new **Amazon DynamoDB table** named Music for my music library. This involved defining the vital schema elements: the **Partition Key** (to uniquely partition the data) and the optional **Sort Key** (to further organize and sort data within each partition).

<img width="500" height="420" alt="image" src="https://github.com/user-attachments/assets/00681604-2d85-43ec-ac19-059dc4aa9871" />


* **Data Entry and Item Creation:** Once the table was active, I manually populated the database with multiple sample **items**. This process demonstrated how flexible the DynamoDB NoSQL model is, allowing each item (representing a song) to have different attributes beyond the required primary keys.
* **Querying the NoSQL Table:** I utilized the integrated tools in the AWS console to execute powerful **queries** against the music library. This allowed me to practice efficiently retrieving specific items based on their primary keys, as well as applying specific **filters** to refine the results—crucial skills for optimizing data retrieval in NoSQL environments.

<img width="500" height="279" alt="image" src="https://github.com/user-attachments/assets/4d09ff99-6ac6-4221-ab68-c9758199240d" />


* **Database Cleanup and Deletion:** After verifying the table and the results of my queries, I performed essential database cleanup by successfully **deleting** the Amazon DynamoDB table. This action reinforces proper resource management and highlights how quickly fully managed AWS services can be spun down when they are no longer needed.

## Learning Outcomes

This project provided practical experience in deploying and managing cloud-native, serverless NoSQL databases. Key takeaways include a foundational understanding of how AWS DynamoDB differs from traditional relational databases, mastering core CRUD (Create, Read, Update, Delete) operations, and gaining confidence in efficiently interacting with the AWS Console to build and test NoSQL data models.
