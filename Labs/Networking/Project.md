# Troubleshooting AWS VPC Connectivity & Flow Logs

## Project Overview
In this project, I acted as a Cloud Support Engineer to diagnose and resolve a series of networking hurdles within a multi-VPC environment. The goal was to restore full connectivity between two isolated VPCs using a systematic, step-by-step troubleshooting approach.

I worked through an environment containing multiple Amazon EC2 instances, VPC Peering connections, and various security layers. By identifying misconfigurations at both the instance and subnet levels, I successfully restored the intended traffic flow.

---

## Skills & Technologies Used
*   **Networking:** Amazon VPC, Subnets, Route Tables, VPC Peering.
*   **Security:** Security Groups (Stateful), Network Access Control Lists (NACLs - Stateless).
*   **Monitoring:** VPC Flow Logs, Amazon CloudWatch.
*   **Tools:** ICMP/Ping, SSH, AWS Management Console.

---

## The 4-Step Troubleshooting Process
Following the project roadmap (Circles #1–4), I resolved the following issues:

### 1. Identifying the "Black Hole" (Initial Testing)
I began by attempting to communicate between instances across the VPC Peering connection. Initial tests failed. I verified that while the **VPC Peering** was active, the **Route Tables** were missing the necessary entries to direct traffic to the peered CIDR block. I manually updated the routes to bridge the two networks.

### 2. Resolving Security Group Blocks
Once routing was established, traffic still wasn't reaching the target instances. I audited the **Security Groups** and found that the inbound rules were too restrictive. I modified the rules to allow specific traffic (HTTP/ICMP) from the source VPC’s CIDR range, ensuring "Stateful" tracking was handled correctly.

### 3. Fixing Stateless NACL Errors
After fixing the Security Groups, I encountered a more subtle issue: traffic would reach the subnet but wouldn't return. I identified a misconfiguration in the **Network ACLs (NACLs)**. Since NACLs are **stateless**, I had to ensure that both:
*   **Inbound Rules** allowed the traffic in.
*   **Outbound Rules** allowed the ephemeral return traffic back out.

### 4. Final Validation via VPC Flow Logs
To confirm the environment was healthy and secure, I analyzed **VPC Flow Logs**. 
*   I filtered for `REJECT` packets to ensure no unintentional blocking was occurring.
*   I verified `ACCEPT` traffic to confirm that my fixes in steps 1-3 were successfully allowing the required data packets to reach their destination.

---

## Key Takeaways
*   **Layered Defense:** I learned that a "Passed" check at the Security Group level doesn't mean the traffic is safe; NACLs act as a second, stateless gatekeeper.
*   **Visibility is King:** Using VPC Flow Logs turned "guessing" into "diagnosing." It provided clear evidence of where a packet was dropped.
*   **Routing Logic:** I reinforced my understanding that VPC Peering is only half the battle—proper Route Table entries are the "glue" that makes it work.

---

## Conclusion
By the end of this lab, I had transformed a fragmented network into a cohesive, secure, and monitored infrastructure. This project sharpened my ability to debug complex AWS networking issues in a high-pressure environment.
