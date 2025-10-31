# Technology Stack Selection

| Layer | Choice | Rationale |
| ----- | ------ | --------- |
| Application Language | **Python 3.11** | Mature ecosystem for data ingestion, scheduling, and async messaging; first-class support for FastAPI and Celery; strong typing via Pydantic. |
| Web Framework | **FastAPI** | High-performance async APIs, auto-generated OpenAPI docs, native dependency injection, excellent developer ergonomics for microservices. |
| Background Workers | **Celery 5 (with Flower)** | Battle-tested task queue with scheduling via Celery Beat, supports Redis broker/backends, and integrates well with FastAPI. |
| Primary Database | **PostgreSQL 15 (AWS RDS)** | Reliable relational store with advanced JSON support for raw payloads, robust indexing, and LISTEN/NOTIFY support for lightweight eventing. |
| Message Broker / Queue | **Redis 7 (AWS ElastiCache)** | Low-latency broker for Celery, simple operations, and managed service availability in AWS. |
| Object Storage | **Amazon S3** | Durable storage for raw ingestion payloads and generated reports. |
| Caching Layer | **Redis** | Shared with Celery broker to reduce operational surface area. |
| SMS Provider | **Twilio Programmable SMS** | Global reach, webhook support for delivery receipts, strong tooling and analytics. |
| Email Provider | **SendGrid** | Optional email channel with reliable deliverability and API-first design. |
| Infrastructure-as-Code | **Terraform** | Multi-environment management, module reuse, strong AWS support, integrates with CI/CD pipelines. |
| Container Runtime | **Docker + AWS ECS Fargate** | Serverless containers with managed scaling, no node maintenance, integrates with AWS networking and IAM. |
| Monitoring | **Prometheus + Grafana (via AWS Managed Prometheus/Grafana)** | Standard metrics stack with alerting and dashboards. |
| Logging | **OpenTelemetry + Loki** | Structured logging pipeline with vendor-neutral instrumentation. |

## Additional Notes
* Use Poetry for dependency management to ensure reproducible builds.
* Apply Ruff + MyPy in CI to enforce code quality.
* Secrets are managed via AWS SSM Parameter Store with secure parameter paths per environment.
