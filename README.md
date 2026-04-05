# AWS Property Maintenance Request System

## Overview
A property management web application that allows tenants to submit maintenance issues and allows staff to review submitted requests in a dashboard.

## Business Use Case
Property management teams often need a simple internal system to track tenant maintenance issues such as plumbing, HVAC, electrical, leaks, and appliance problems. This application provides a lightweight request intake workflow and dashboard view.

## Features
- Submit maintenance requests
- Validate required form fields
- Persist requests in a database
- View submitted requests in a dashboard
- Track request status

## Technology Stack
- Python
- Flask
- SQLAlchemy
- SQLite for local development
- MySQL-compatible support for AWS RDS deployment

## Architecture Approach
This application is designed with environment-based database configuration:
- Local development uses SQLite
- AWS deployment uses MySQL on Amazon RDS

The same application code is reused across both environments.

## Local Run Instructions
1. Create and activate a virtual environment
2. Install dependencies from `app/requirements.txt`
3. Run `python app/app.py`
4. Open `http://127.0.0.1:5051`

## Planned AWS Deployment
- VPC
- Public and private subnets
- Security groups
- Amazon RDS MySQL
- Amazon EC2 for app hosting
- Application Load Balancer

## Why This Project Matters
This project demonstrates:
- full-stack application flow
- database-backed persistence
- validation and error handling
- environment-based configuration
- cloud-ready application design

## Future Improvements
- request status update workflow
- authentication
- filtering and search
- CI/CD pipeline
- Terraform deployment
- HTTPS with ACM and Route 53