# Movietowne Listing Platform

This repository contains the scaffolding for the Movietowne listing platform, including service modules, documentation, infrastructure-as-code, and CI configuration.

## Repository Layout

- `docs/` – Architecture and technology stack documentation.
- `src/movietowne_listing/` – Python packages for ingestion, scheduling, messaging, and admin services.
- `infra/terraform/` – Terraform configuration for dev, staging, and production environments.
- `.github/workflows/` – Continuous integration pipelines.
- `.env.example` – Sample environment configuration.
- `pyproject.toml` – Project dependencies and tooling managed via Poetry.

## Getting Started

1. Install Poetry and Python 3.11.
2. Copy `.env.example` to `.env` and update environment-specific values.
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Run service locally (example for ingestion API):
   ```bash
   poetry run uvicorn movietowne_listing.ingestion.service:app --reload
   ```

## Continuous Integration

CI runs linting (Ruff), type checking (MyPy), and unit tests (Pytest) via GitHub Actions. The workflow file is located at `.github/workflows/ci.yml`.

## Infrastructure

Terraform modules under `infra/terraform` define AWS infrastructure for dev, staging, and production environments. Refer to `infra/terraform/README.md` for deployment guidance.
