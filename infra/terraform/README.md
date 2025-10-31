# Terraform Infrastructure

This directory contains Terraform configuration for provisioning Movietowne Listing environments in AWS. The layout separates reusable modules from environment-specific stacks.

## Structure

- `modules/`
  - `network/` – Creates VPC, subnets, security groups, and networking primitives shared across services.
  - `services/` – Provisions ECS clusters, task definitions, and supporting resources for ingestion, scheduling, messaging, and admin services.
- `environments/`
  - `dev/`
  - `staging/`
  - `prod/`

Each environment composes modules with environment-specific variables.

## Usage

1. Ensure Terraform >= 1.6.0 is installed and AWS credentials are available.
2. Initialize the desired environment directory, e.g.:
   ```bash
   cd infra/terraform/environments/dev
   terraform init
   ```
3. Review and customize `variables.tf` files before applying changes.
4. Plan and apply:
   ```bash
   terraform plan -var-file=dev.tfvars
   terraform apply -var-file=dev.tfvars
   ```

State is expected to be stored remotely in AWS S3 with DynamoDB state locking; configure backend settings in `backend.tf`.
