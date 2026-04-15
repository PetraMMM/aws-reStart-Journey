# Next-Generation 3D E-Commerce Architecture

## Project Overview
We designed this cloud-native, highly available architecture to solve a specific challenge: delivering heavy 3D assets (like furniture and high-fidelity gadgets) to millions of global users without compromising performance. 

By using a robust AWS stack—specifically Amazon CloudFront, S3, and Amazon Aurora—we built a system that ensures a secure, fast rendering experience that scales automatically with global demand.

---

## Architectural Component Breakdown
We carefully selected each service to ensure the platform remains performant and secure under heavy loads.

| Service | Purpose | Rationale |
| :--- | :--- | :--- |
| Route 53 | DNS Management | We utilized latency-based routing to ensure users connect to the fastest available endpoint. |
| AWS IAM | Access Control | We implemented the Principle of Least Privilege, allowing our EC2 and Lambda functions to securely access resources using Roles instead of insecure permanent credentials. |
| AWS WAF | Security Shield | We integrated WAF with CloudFront to block SQL injections and bots at the "edge" before they reach our backend. |
| CloudFront | Content Delivery (CDN) | This was essential for caching heavy 3D models (.glb/.usdz) at edge locations to provide a smooth user experience. |
| Amazon S3 | Object Storage | We chose S3 for its industry-leading durability for 3D assets, integrated with CloudFront for secure delivery. |
| ALB (Application Load Balancer) | Traffic Distribution | We used an Application Load Balancer to automatically distribute incoming traffic across EC2 instances to prevent bottlenecks. |
| EC2  Auto Scaling Group | Backend Compute | We utilized Auto Scaling Groups to allow the platform to grow or shrink based on real-time CPU/Memory demand. |
| AWS Lambda | Serverless Compute | We used Lambda for event-driven tasks (like order processing or image resizing) to save costs and avoid managing servers. |
| Amazon Aurora | Relational Database | We chose Aurora to handle critical transaction and user data with automated failover and high performance. |
| DynamoDB | NoSQL Database | We implemented DynamoDB for the product catalog to provide millisecond response times during high-speed searches. |
| VPC Endpoints | Private Fast-Lanes | We routed S3 and DynamoDB traffic over the private AWS backbone, bypassing the expensive public internet. |

---

<img width="750" height="755" alt="image" src="https://github.com/user-attachments/assets/2cb0ef40-3723-49f2-820d-31c8cce9cb26" />



## Meeting Key Requirements

### 1. High Availability (24/7 Uptime)
* **Multi-AZ Deployment:** We spread the architecture across two Availability Zones. If one data center fails, the Elastic Load Balancer and Route 53 automatically reroute traffic to the healthy zone.
* **Database Redundancy:** We configured Amazon Aurora to maintain a synchronized "Standby" copy in a different zone to prevent data loss during an outage.

### 2. Scalability 
* **Elasticity:** We set up the Auto Scaling Group (ASG) to monitor traffic spikes. During high-demand product launches, the system automatically launches new EC2 instances and terminates them when traffic subsides.
* **Serverless Scaling:** We utilized DynamoDB and Lambda because they scale nearly infinitely without manual intervention.

### 3. Performance 
* **Edge Caching:** By using Amazon CloudFront, we ensured 3D models are stored miles away from the user rather than thousands of miles away at the origin, eliminating lag.
* **VPC Endpoints:** We used Private Endpoints for S3 and DynamoDB to keep data traffic within the AWS backbone, avoiding the slower public internet.

### 4. Security
* **Defense in Depth:** We utilized a Public/Private Subnet strategy. We hid the database and application servers in Private Subnets, making them unreachable from the public internet.
* **IAM Roles:** we assigned strict "Least Privilege" roles to services so they only have the minimum permissions needed to function.
* **WAF:** We configured AWS WAF to act as a bouncer, filtering malicious requests before they ever enter the network.

### 5. Cost Optimization 
* **S3 Intelligent-Tiering:** We enabled this to automatically move older 3D assets to cheaper storage classes when they are no longer frequently accessed.
* **Event-Driven Processing:** By using AWS Lambda for tasks like 3D model processing, we avoided the cost of keeping an EC2 instance running 24/7. We only pay for the exact seconds the code executes.
* **Resource Monitoring:** We used AWS Trusted Advisor and CloudWatch to find and terminate idle resources, allowing us to downsize and save budget.

---

## Networking & Traffic Flow
We structured the data flow to be as efficient as possible:

1. **Entry:** A user queries Route 53, which points to CloudFront.
2. **Inspection:** AWS WAF inspects the request at the CloudFront edge.
3. **Handoff:** The request enters the VPC via the Internet Gateway and hits the ALB.
4. **Processing:** The ALB sends the request to an EC2 instance in a Private Subnet.
5. **Data Retrieval:** The EC2 fetches 3D metadata from DynamoDB and user data from Aurora (using local Read Replicas for speed).
6. **Asset Delivery:** Heavy 3D files are fetched from S3 via a VPC Endpoint, remaining entirely off the public internet.

---

## Design Trade-offs & Challenges
* **Consistency vs. Speed:** We chose Amazon Aurora over a single-node RDS instance. While Aurora is slightly more expensive, we decided the trade-off was necessary to prevent a single point of failure.
* **Database Complexity:** We managed multiple database types (Relational for orders, NoSQL for catalogs). This added complexity but prevented the bottleneck effect that occurs when a single database tries to handle all data types.
* **Redundancy vs. Cost:** We implemented a Multi-AZ VPC which is more complex than a "Monolith," but we determined it was the only way to ensure the reliability required for a global startup.
