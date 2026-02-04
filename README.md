# Project Title: Automated Revenue Leakage Audit Pipeline 
> An end-to-end data engineering pipeline built to detect payment discrepancies in 1,000,000+ subscription records.

---

## The Tech Stack
* **1. Infrastructure:** Docker & Docker Compose
* **2. Data Generation:** Python (Faker library for high-cardinality synthetic data)
* **3. Data Warehouse:** DuckDB - (in Process)
* **4. Transformation:** dbt (Data Build Tool)

## The Architecture
* **1. Generation:** Python script creates 1M rows of subscription data with intentional payment leaks.
* **2. Loading:** DuckDB ingests the raw data via dbt seeds
* **3. Transformation:** 
    * stg_subscriptions: Cleans the data and maps prices to tiers (Basic/Pro/Enterprise)
    * fct_revenue_leakage: Aggregates revenues to identify loss