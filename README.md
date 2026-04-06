# AWS Property Maintenance Request System

## Overview
A cloud-based web application for submitting and tracking property 
maintenance requests.
The system is deployed on AWS and demonstrates a production-style 
architecture using load balancing, compute, and managed database services.

## Business Use Case
Property management teams require a reliable and centralized system to 
handle tenant maintenance requests.
This application provides a structured workflow for submission, storage, 
and review of service requests while leveraging scalable cloud 
infrastructure.

## Features
- Submit maintenance requests through a web interface
- Validate required input fields
- Store requests in a relational database
- View and manage requests in a dashboard
- Track request details and status

## Technology Stack

Application
- Python
- Flask
- SQLAlchemy

Cloud Infrastructure
- Amazon EC2
- Application Load Balancer (ALB)
- Amazon RDS (MySQL)
- Amazon CloudWatch

## Architecture
User requests are routed through an Application Load Balancer to a Flask 
application running on EC2.
The application processes and stores data in an RDS MySQL database.

## Deployment Details
- Application runs on port 5001
- ALB distributes traffic to EC2 instance
- Health checks configured for application endpoint
- Security groups restrict direct access to the instance
- Database is deployed in a private network layer

## Monitoring
- CloudWatch alarms configured for CPU usage
- Billing alerts enabled
- Centralized monitoring of application health

## Outcome
The system demonstrates the ability to design, deploy, and troubleshoot a 
multi-tier AWS application, including networking, load balancing, and 
database integration.

## Future Improvements
- User authentication and role-based access
- REST API implementation
- Domain integration using Route 53
- Production deployment with Gunicorn
- Containerization using Docker
