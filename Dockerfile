# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Installing my dbt libraries
RUN pip install --no-cache-dir \
    dbt-core==1.7.18 \
    dbt-duckdb==1.7.4 \
    mashumaro==3.12

# Copying project files into container
COPY . /app

CMD ["tail", "-f", "/dev/null"]