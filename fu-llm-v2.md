# README: GenAI-Based Trade File Generation Platform

## Overview
This project uses Generative AI (LLMs) to automatically create trade settlement instruction files based on:
- User inputs (like settlement amount, date, etc.)
- Past trade data (stored in DB2)
- Existing Excel file templates

The system is designed in a microservices architecture for scalability, modularity, and production readiness.

---

## Use Case Summary

### Problem Statement
Traditionally, users manually upload trade settlement instruction files based on repetitive historical trades with only minor variations like amounts or dates. This manual preparation is error-prone, time-consuming, and non-scalable.

### Solution
Using Generative AI and microservices, this platform enables:
- Smart prediction and generation of new trade files by learning from historical uploaded trades.
- Dynamic input adjustments (e.g., settlement amount, currency, settlement dates) by users.
- Automated creation of ready-to-upload Excel files using standard templates.

### Business Benefits
- **Efficiency Boost**: 80%+ reduction in manual effort and faster file generation.
- **Error Reduction**: Minimize human errors in formatting and trade instructions.
- **User Satisfaction**: Instant file generation enhances client and operations team experience.
- **Compliance & Auditability**: Every file generation is tracked and logged.
- **Scalability**: Can handle hundreds of trade instructions with minimal resource increase.
- **Cost Savings**: Reduced operational costs by minimizing manual labor and rework.
- **Competitive Advantage**: Faster client onboarding and settlements drive business growth.

---

## Microservices Architecture

**Service Name** | **Responsibility** | **Tech Stack**
:---|:---|:---
File Parser Service | Parses uploaded Excel files and extracts metadata | Python (FastAPI) / Java (Spring Boot)
Prompt Builder Service | Dynamically builds a prompt for the LLM based on past trades and user inputs | Python (Flask/FastAPI)
LLM Interaction Service | Handles communication with LLMs (e.g., OpenAI, Bedrock) | Python (FastAPI)
Excel Generator Service | Generates Excel files using LLM output and templates | Python (FastAPI)
Storage Service | Stores generated Excel files securely in cloud storage (e.g., AWS S3, Azure Blob) | Java (Spring Boot) / Node.js
Authentication Service | Manages user authentication and token validation | Keycloak / OAuth2 / Custom Auth Service
Monitoring & Audit Service | Tracks API usage, logs events, monitors LLM costs and failures | Prometheus + Grafana / Custom APIs

---

## Service-to-Service Call Flow

1. User uploads trade request or fills form via Frontend.
2. API Gateway routes requests.
3. Authentication Service validates user identity.
4. Fetch Past Trades from DB2.
5. Prompt Builder Service generates a contextual LLM prompt using past trade details and user input.
6. LLM Interaction Service sends the prompt to the LLM model and receives structured trade data.
7. Excel Generator Service creates the Excel file from LLM response and template.
8. Storage Service uploads the file to cloud storage and returns a download link.
9. Frontend shows the file to the user or triggers download.

---

## Database

DB2 is used to store past trade details.
(Optional) A Vector Database like Pinecone, FAISS, or Weaviate can be introduced later for better semantic search on past trades.

Example DB2 Table Schema:

| Column | Example Value |
|:---|:---|
| trade_id | 12345 |
| client_name | ABC Corp |
| currency | USD |
| settlement_method | DVP |
| past_settlement_amount | 1,000,000 |
| past_settlement_date | 2024-04-01 |
| template_type | Standard |
| other_fields_json | { "fieldA": "valueA" } |

---

## Security

- OAuth2 / JWT authentication across all APIs.
- Secure file uploads and downloads (pre-signed S3 URLs).
- Encrypted database fields for sensitive trade data.

---

## Monitoring

- API response times
- LLM API usage and cost monitoring
- File generation success/failure tracking
- Retry mechanisms for LLM and Storage failures

Tools: Prometheus, Grafana, ELK Stack (Elasticsearch + Logstash + Kibana).

---

## Deployment Options

- Docker containerized microservices.
- AWS ECS + S3 + API Gateway (Recommended)
- Azure Kubernetes Service (AKS) + Azure Blob Storage.
- On-prem deployment with Docker Compose / Kubernetes (Minikube or Openshift).

---

## Future Enhancements

- Add Semantic Search over past trades using OpenAI Embedding API + VectorDB.
- Introduce Background Job Processing (e.g., with Kafka/SQS for async LLM calls).
- Implement Role-Based Access Control (RBAC).
- Add Audit Trail for trade file generation and downloads.

---

## Quick Summary

Your DB2 becomes the "Memory Layer" for now. Focus on DB2 fetch, prompt generation, LLM integration, Excel creation, and secure download handling.

