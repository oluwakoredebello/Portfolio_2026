# 📊 Lumiere Financiers - Revenue Integrity Data Pipeline
![Build Status](https://img.shields.io/badge/Status-Active_Development-green)
![Tech](https://img.shields.io/badge/Stack-Python%20%7C%20DuckDB%20%7C%20dbt-blue)

> A production-style data engineering pipeline designed to simulate, ingest, and audit revenue leakages across legacy and modern payment gateways

---
## 🧠 Business Context
Lumiere Financiers is a legacy wealth management firm founded in the early 2000s. Overtime, the firm's infrastructure evolved into a complex hybrid of internal databases and modern API-driven payment gateways. This fragmentation led to synchronization errors across Lumiere's three core service tiers: Basic (Retail), Pro (Wealth), and Premium (Private Client), leading to unchecked revenue losses.

This project simulates that environment, processing **1.5 million records**, and answers a core business question:
> Which payment gateways and customer segments are responsible for the losses, and where should Lumiere prioritize its modernization efforts?

## 🏗️ Architecture Overview
Python (Synthetic Data Generation) -> DuckDB (In-Process OLAP) -> dbt (Medallion Architecture) -> Orchestration (Docker & Docker Compose)

The entire pipeline is containerized using Docker to ensure reproducibility across environments.

## ⚙️ The Tech Stack
* **Data Generation:** Python (Faker, random)
* **Batch Processing:** Generator-based ingestion
* **DataBase:** DuckDB (Local Development)
* **Transformation:** dbt (tests,  models, docs)
* **Version Control:** Git (feature branch workflow)
* **Infrastructure:** Docker & Docker Compose
* **Cloud Target (Planned):** BigQuery

## 🔁 Pipeline Breakdown
* **Generation:** Python script (fintech_audit.py) creates 1.5M rows of subscription data with intentional payment leaks
* **Loading:** DuckDB ingests the raw data via dbt seeds
* **Transformation:** 
    * stg_subscriptions: Standardizes schema and maps prices to tiers (Basic, Pro, and Premium), stages calculations for downstream models
    * fct_gateway_audit: Audits payment gateways to pinpoint leakages
    * fct_gateway_performance_audit: Identifies payment gateways for Cloud Migration
    * fct_retention_audit: Churn rates for active vs inactive users (Users without log-in presence for over 30 days)
    * fct_revenue_leakage: Aggregates revenues to identify loss from each Plan
    * fct_tenure_risk_audit: Summarizes failure rates by Tenure
* **Data Quality**: dbt tests enforce:
    * Not-null constraints
    * Accepted values for plans and statuses
    * Revenue integrity checks

## Key Achievements So Far
**1.** Built a Medallion Architecture (Staging -> Marts) to clean and model raw financial data

**2.** Identified a ~60% failure rate in Legacy Internal Systems compared to a 23% rate in modern gateways

**3.** Engineered Fact Models to provide real-time visibility into transaction health

**4** Results support prioritizing gateway modernization over customer repricing

## 🛠️ How to Run
To execute the full pipeline (Ingestion + Transformation + Testing), run:

```bash
# Clone the repository
git clone https://github.com/oluwakoredebello/Portfolio_2026

# Build and run the containers
docker-compose up --build

```