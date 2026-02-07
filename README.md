 Intelligent Cloud Auto Recovery System

 Overview
This project implements an intelligent self-healing cloud infrastructure
using AWS services. It automatically detects EC2 instance failures and
triggers recovery actions without human intervention.

 Architecture
- Amazon EC2 – Compute instance
- Amazon CloudWatch – Health monitoring
- AWS Lambda – Automated recovery logic
- Amazon DynamoDB – Failure tracking (planned enhancement)
- Amazon SNS – Alerting (optional)

 Recovery Workflow
1. CloudWatch monitors EC2 health
2. Alarm triggers on failure
3. Lambda function executes recovery
4. EC2 instance is rebooted or restarted

 Key Features
- Event-driven architecture
- Automated fault recovery
- Cloud-native design
- Free-tier friendly implementation

 Skills Demonstrated
AWS EC2, CloudWatch, Lambda, IAM, Cloud Automation, Monitoring
