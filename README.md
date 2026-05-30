# Dockerized Jenkins Setup

## Overview

This project provides a production-style Dockerized Jenkins platform with distributed build agent architecture, Jenkins Configuration as Code (JCasC), and Pipeline-as-Code implementation.

The platform is designed to simulate modern enterprise CI/CD infrastructure practices while remaining lightweight enough for local development and learning.

The setup includes:

* Dockerized Jenkins Controller
* Dedicated Docker Build Agent
* Jenkins Configuration as Code (JCasC)
* Pipeline-as-Code using Jenkinsfile
* Docker Compose orchestration
* WebSocket-based inbound agent communication
* Automated local environment setup
* Persistent Jenkins storage
* Git-integrated CI/CD workflows

---

# Architecture

```text
                    +----------------------+
                    | Jenkins Controller   |
                    | (JCasC Managed)      |
                    +----------+-----------+
                               |
                               |
                    WebSocket Agent Connection
                               |
                               v
                    +----------------------+
                    | Jenkins Docker Agent |
                    | CI/CD Runtime        |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Docker Engine        |
                    +----------------------+
```

---

# Tech Stack

| Technology                    | Purpose                       |
| ----------------------------- | ----------------------------- |
| Jenkins LTS                   | CI/CD Automation              |
| Docker                        | Containerization              |
| Docker Compose                | Multi-container orchestration |
| Jenkins Configuration as Code | Jenkins automation            |
| Jenkins Inbound Agent         | Distributed builds            |
| Git                           | Source control integration    |
| Python 3.11                   | Automation tooling            |
| pyenv                         | Python version management     |
| WebSocket Agents              | Secure agent communication    |

---

# Key Features

* Production-style Jenkins controller-agent architecture
* Dockerized CI/CD runtime
* Distributed build execution
* Jenkins Configuration as Code (JCasC)
* Pipeline-as-Code implementation
* Docker Compose orchestration
* Automated plugin installation
* Secure Jenkins authentication
* Persistent Jenkins storage
* Git-integrated CI/CD workflows
* Local development automation

---

# Why Distributed Agent Architecture?

Initially, the Jenkins controller was directly connected to the Docker socket.

While functional for local testing, this approach is not considered production-friendly because:

* Controller gains elevated Docker host access
* Security boundaries are reduced
* Build workloads impact controller stability
* Scaling becomes difficult

The architecture was upgraded to use dedicated Docker build agents instead.

Benefits:

* Better runtime isolation
* Improved security boundaries
* Production-aligned CI/CD design
* Scalable build execution model
* Cleaner separation of orchestration and execution

---

# Project Structure

```text
dockerized-jenkins-setup/
│
├── docker/
│   └── Dockerfile
│
├── docker-agent/
│   └── Dockerfile
│
├── jenkins_config/
│   └── casc.yaml
│
├── jenkins_plugins/
│   └── plugins.txt
│
├── pipelines/
│
├── scripts/
│   └── start_local_env.py
│
├── screenshots/
│
├── Jenkinsfile
├── docker-compose.yml
├── requirements.txt
├── .python-version
├── .env
└── README.md
```

---

# Jenkins Components

## Jenkins Controller

Responsible for:

* Pipeline orchestration
* Build scheduling
* Agent management
* UI access
* Jenkins configuration management

The controller does NOT directly execute Docker workloads.

---

## Docker Build Agent

Responsible for:

* Pipeline execution
* Docker builds
* Runtime CI/CD tasks
* Git operations
* Compose execution

The build agent connects to the controller using WebSocket-based inbound communication.

---

# Jenkins Configuration as Code (JCasC)

Jenkins is configured using YAML-based configuration management instead of manual UI configuration.

Benefits:

* Reproducible setup
* Infrastructure-as-Code practices
* Git-managed configuration
* Automated Jenkins provisioning
* Reduced manual configuration drift

Configuration file:

```text
jenkins_config/casc.yaml
```

---

# Pipeline-as-Code

CI/CD workflows are managed using Jenkinsfile.

Current pipeline stages:

* Environment validation
* Docker validation
* Compose validation
* Image build validation
* Runtime verification

Pipeline execution occurs on the dedicated Docker agent.

---

# Prerequisites

Install the following before running locally:

* Git
* Docker Desktop
* Python 3.11
* pyenv
* VS Code (recommended)

---

# Docker Installation

Install Docker Desktop:

https://www.docker.com/products/docker-desktop/

Verify installation:

```bash
docker --version
docker compose version
```

---

# Python Setup

## Install Python 3.11

```bash
pyenv install 3.11
```

## Set local Python version

Inside repository:

```bash
pyenv local 3.11
```

Verify:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

---

# Local Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/<your-github-username>/dockerized-jenkins-setup.git
```

Move into repository:

```bash
cd dockerized-jenkins-setup
```

---

## 2. Configure Environment Variables

Create local `.env` file:

```env
JENKINS_PORT=8081
JENKINS_ADMIN_ID=admin
JENKINS_ADMIN_PASSWORD=admin
JENKINS_AGENT_SECRET=<your-agent-secret>
```

---

## 3. Start Jenkins Platform

```bash
python scripts/start_local_env.py
```

The automation script performs:

* Virtual environment creation
* Dependency installation
* Docker validation
* Jenkins image build
* Agent image build
* Container startup
* Runtime validation

---

# Access Jenkins UI

Open browser:

```text
http://localhost:8081
```

Default credentials:

| Username | Password |
| -------- | -------- |
| admin    | admin    |

---

# Jenkins Agent Setup

A Jenkins inbound agent must be configured manually during initial setup.

## Steps

1. Open Jenkins UI
2. Navigate to:

   * Manage Jenkins
   * Nodes
3. Create new node:

   * Name: docker-agent
   * Type: Permanent Agent
4. Configure:

   * Label: docker-agent
   * Remote Root Directory: /home/jenkins
   * Launch Method: Launch agent by connecting it to the controller
5. Copy generated agent secret
6. Add secret to local `.env`
7. Restart containers

---

# Running Pipelines

The project uses Pipeline-as-Code via SCM integration.

Pipeline source:

```text
Jenkinsfile
```

Pipeline execution target:

```groovy
agent {
    label 'docker-agent'
}
```

This ensures all CI/CD workloads execute on the dedicated Docker agent.

---

# Useful Commands

## Stop Environment

```bash
docker compose down
```

---

## Remove Environment Completely

```bash
docker compose down -v
```

---

## Rebuild Images

```bash
docker compose build --no-cache
```

---

## Start Environment

```bash
docker compose up -d
```

---

## View Running Containers

```bash
docker ps
```

---

## View Jenkins Logs

```bash
docker logs -f jenkins-server
```

---

## View Agent Logs

```bash
docker logs -f jenkins-docker-agent
```

---

# Security Notes

The following practices are intentionally implemented:

* Secrets stored in local `.env`
* `.env` excluded from Git tracking
* Controller-agent runtime separation
* WebSocket-based inbound agents
* No hardcoded credentials in repository

---

# Current Limitations

This project is designed for local development and learning purposes.

Some production-grade capabilities are intentionally simplified.

Examples:

* Local Docker socket usage
* Static agent configuration
* Local secret management
* Single-node Jenkins controller

---

# Future Improvements

Planned production-grade enhancements:

## CI/CD Enhancements

* GitHub Webhook automation
* Dynamic Docker agents
* Multi-agent scaling
* Shared Jenkins libraries

## Infrastructure Enhancements

* Kubernetes-based agents
* Terraform integration
* Helm deployment support
* NGINX reverse proxy

## Security Enhancements

* Vault integration
* Jenkins credentials management
* Rootless container runtime
* Docker socket proxy

## Observability

* Prometheus monitoring
* Grafana dashboards
* Jenkins metrics export
* Centralized logging

## Platform Integrations

* Airflow CI/CD deployment
* Spark workload integration
* Databricks automation pipelines
* AWS deployment workflows

---

# Learning Objectives

This project demonstrates:

* Jenkins distributed architecture
* CI/CD platform engineering
* Pipeline-as-Code
* Dockerized build environments
* Jenkins Configuration as Code
* Controller-agent separation
* Docker runtime integration
* Secure CI/CD design concepts
* Infrastructure automation practices

---

# Author

Chinmay Karnekar

Databricks Platform Engineer | AWS Cloud & Platform Engineering
