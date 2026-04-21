
# AWS Systems Manager: Centralized Operations and Automation

In this project, I utilized AWS Systems Manager to centralize operational data and automate tasks across my AWS resources. I managed Amazon EC2 instances at scale, demonstrating how to streamline configurations and enhance security.

## Project Objectives
After completing this project, I am able to use Systems Manager to:
* Verify configurations and permissions across resources.
* Run tasks on multiple servers simultaneously.
* Update application settings or configurations remotely.
* Access the command line on an instance securely without SSH keys.

## Key Capabilities Implemented

### Fleet Management and Verification
I ensured that all managed instances were correctly configured and reporting to the Systems Manager dashboard. This involved verifying that instances possessed the necessary IAM permissions and that the SSM Agent was functioning correctly.

### Automation via Run Command
I used the Run Command feature to perform bulk operations. Instead of logging into each server individually, I executed scripts across multiple EC2 instances at once, allowing for efficient software updates and configuration management.

<img width="500" height="190" alt="image" src="https://github.com/user-attachments/assets/5a636e54-8bab-48e3-833c-214d8e6fada8" />


### Configuration Management
I managed application settings and environment configurations remotely. This allowed me to maintain consistency across my fleet and ensure that all servers were aligned with the required operational state.

### Secure Access with Session Manager
I utilized Session Manager to access the command line of my instances. This improved security by removing the need to open inbound SSH ports or manage SSH keys, while providing a full audit trail of session activity.

## Conclusion
By implementing AWS Systems Manager, I have demonstrated how to automate routine maintenance and management tasks. This approach reduces the risk of manual errors and provides a centralized, secure way to manage infrastructure at scale.

## Tools Used
* AWS Systems Manager (Run Command, Session Manager, Fleet Manager)
* Amazon EC2
* AWS Identity and Access Management (IAM)
