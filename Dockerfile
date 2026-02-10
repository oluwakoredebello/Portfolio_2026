FROM python:3.12-slim

# install uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# copy dependency files
COPY pyproject.toml uv.lock ./


RUN uv pip install --system -r pyproject.toml

COPY . .


CMD ["python", "fintech_audit.py"]