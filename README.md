# Project Title: Lumiere Financiers Revenue Integrity Suite
> An automated data engineering pipeline designed to identify, quantify, and reconcile revenue leakages across legacy and modern payment gateways

---
## The Business Case
* **Business Context** Lumiere Financiers is a legacy wealth management firm founded in the early 2000s. After decades of sustained growth, the firm's infrastructure evolved into a complex hybrid of internal databases and modern API-driven payment gateways. This fragmentation led to synchronization errors across Lumiere's three core service tiers: Basic (Retail), Pro (Wealth), and Premium (Private Client). Facing a projected $10M revenue leakage, Lumiere sought a data-driven strategy to justify full Cloud Migration.

* Product Scope: Managed Tiers
> The pipeline reconciles transaction data across three wealth management offerings:
* Basic: Entry-level automated portfolio tracking ($15.99/mo)
* Pro: Active Management with advisor access ($19.99/mo)
* Premium: Full-service Private Client Management ($29.99/mo)

* **Technical Challenge** Handling 1.5M+ records with inconsistent data types and integrity issues across multiple systems

## The Tech Stack
* **1. Infrastructure:** Docker & Docker Compose
* **2. Data Generation:** Python (Data Generation: Faker library for high-cardinality synthetic data)
* **3. DataBase:** DuckDB (Local Development) / BigQuery (Planned Cloud Migration)
* **4. Transformation:** dbt (Data Build Tool)
* **5. Environment:** GitHub Codespaces (Cloud-based development), VSCode
* **6. Version Control:** Git (Feature branching workflow)

## Technical Architecture
* **1. Generation:** Python script (fintech_audit.py) creates 1.5M rows of subscription data with intentional payment leaks
* **2. Loading:** DuckDB ingests the raw data via dbt seeds
* **3. Transformation:** 
    * stg_subscriptions: Cleans the raw data and maps prices to tiers (Basic, Pro, and Premium), stages calculations for downstream models
    * fct_gateway_audit: Audits payment gateways to pinpoint leakages
    * fct_gateway_performance_audit: Identifies payment gateways for Cloud Migration
    * fct_retention_audit: Churn rates for active vs inactive users (Users without log-in presence for over 30 days)
    * fct_revenue_leakage: Aggregates revenues to identify loss from each Plan
    * fct_tenure_risk_audit: Summarizes failure rates by Tenure

## Key Achievements So Far:
* **1.** Built a Medallion Architecture (Staging -> Marts) to clean and model raw financial data
* **2.** Identifies a 60% failure rate in Legacy Internal Systems compared to a 23% rate in modern gateways
* **3.** Engineered Fact Models to provide real-time visibility into transaction health