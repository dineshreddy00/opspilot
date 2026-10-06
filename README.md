# OpsPilot

OpsPilot is a beginner-friendly DevOps automation project designed to demonstrate how a Python application can be containerised and prepared for a modern DevOps workflow.

## Project Overview

The goal of OpsPilot is to practise and demonstrate important DevOps concepts including:

* Linux
* Git and GitHub
* Python application deployment
* Docker containerisation
* CI/CD concepts
* Jenkins
* Infrastructure as Code with Terraform
* Application and system monitoring
* Automation using shell scripts

## Project Structure

```text
opspilot/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docker/
├── docs/
├── jenkins/
├── monitoring/
├── scripts/
├── terraform/
├── Dockerfile
├── .gitignore
└── README.md
```

## Technologies

* Python
* Linux
* Git
* GitHub
* Docker
* Jenkins
* Terraform
* Shell Scripting
* Monitoring

## Application

The application is written in Python.

Dependencies are maintained in:

```text
app/requirements.txt
```

The application can be containerised using the project Dockerfile.

## Docker

Build the Docker image:

```bash
docker build -t opspilot .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name opspilot opspilot
```

Check running containers:

```bash
docker ps
```

Stop the container:

```bash
docker stop opspilot
```

## Git Workflow

The project uses Git for version control and GitHub for remote source-code management.

Basic workflow:

```bash
git add .
git commit -m "Describe your changes"
git push
```

## DevOps Workflow

The intended workflow is:

```text
Developer
   ↓
Git
   ↓
GitHub
   ↓
Jenkins
   ↓
Build
   ↓
Docker
   ↓
Deployment
   ↓
Monitoring
```

## Learning Objectives

This project is being developed to gain practical experience with real-world Junior DevOps responsibilities such as:

* Managing Linux environments
* Working with Git repositories
* Building Docker images
* Running containerised applications
* Understanding CI/CD pipelines
* Working with Jenkins
* Using Terraform for infrastructure automation
* Creating automation scripts
* Understanding application monitoring

## Future Improvements

Planned improvements include:

* Complete Jenkins CI/CD pipeline
* AWS deployment
* Terraform infrastructure
* Automated Docker builds
* Application monitoring
* Health checks
* Deployment automation
* Better documentation

## Author

**Dinesh Reddy**

B.Tech Computer Engineering (AI)

Aspiring DevOps / Cloud Engineer
# opspilot
End-to-end DevOps and cloud deployment platform
