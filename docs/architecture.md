# Movietowne Listing Platform Architecture

## Overview
The Movietowne Listing platform coordinates ingestion of third-party movie schedules, processes and enriches them, and delivers timely notifications to subscribers while providing operators with administrative tooling. The system is organized around four primary layers:

1. **Content Ingestion** – Connectors pull listings from cinemas and distributors, normalize metadata, and publish canonical events.
2. **Scheduling & Orchestration** – Pipelines validate, enrich, and deduplicate screenings, coordinating asynchronous jobs.
3. **Messaging & Delivery** – Subscribers receive SMS alerts and optional email notifications based on personalized preferences.
4. **Admin & Insights** – Staff manage listings, monitor health, and tune messaging policies through a web console.

## High-Level Component Diagram
```
+----------------+       +------------------------+       +------------------+
| External       |       | Content Ingestion      |       | Scheduling &     |
| Providers      |-----> |  - Source connectors   |-----> | Orchestration    |
| (APIs, feeds)  |       |  - Normalization jobs  |       |  - Celery beats  |
+----------------+       |  - Storage adapters    |       |  - Orchestrators |
                         +------------------------+       |  - Event store   |
                                                          +---------+--------+
                                                                    |
                                                                    v
                                                          +------------------+
                                                          | Messaging        |
                                                          |  - Trigger rules |
                                                          |  - SMS/email svc |
                                                          +---------+--------+
                                                                    |
                                                                    v
                                                          +------------------+
                                                          | Admin Console    |
                                                          |  - FastAPI admin |
                                                          |  - Reporting     |
                                                          +------------------+
```

## Core Services

### 1. Content Ingestion Service
* Polls or receives webhooks from cinema and distributor APIs.
* Uses pluggable connectors to support heterogeneous formats (JSON, XML, CSV).
* Normalizes listings to a canonical schema and stores raw payloads for auditing.
* Publishes normalized events to the event bus (PostgreSQL + LISTEN/NOTIFY and Celery queues).

### 2. Scheduling & Orchestration Service
* Subscribes to ingestion events, deduplicates by venue/movie/time, and enriches with metadata (ratings, runtimes).
* Maintains future screenings in PostgreSQL with time-zone aware scheduling.
* Uses Celery Beat to drive periodic tasks (cleanup, refresh, notification generation).
* Generates messaging jobs stored in Redis-backed Celery queues.

### 3. Messaging Service
* Applies subscriber rules to determine who should be notified of new or updated screenings.
* Uses Twilio SMS and optional SendGrid email integrations.
* Tracks delivery receipts and retries transient failures.
* Persists communication history for compliance and analytics.

### 4. Admin & Insights Service
* FastAPI + React admin portal provides CRUD tooling for venues, movies, campaigns, and user management.
* Provides dashboards for ingestion health, queue depth, and delivery success metrics.
* Supports feature flags and A/B experiments via configuration toggles stored in PostgreSQL.

## Cross-Cutting Concerns
* **Security** – All services authenticate via JWT issued by an internal auth service backed by PostgreSQL.
* **Observability** – OpenTelemetry traces, Prometheus metrics, and structured JSON logging aggregated in Loki.
* **Configuration** – Centralized via environment variables loaded by Pydantic settings; secrets stored in AWS SSM Parameter Store.
* **Infrastructure** – Deployed on AWS using ECS Fargate per service, RDS for PostgreSQL, Elasticache for Redis, S3 for raw payload archives.

## Data Flow
1. Ingestion service pulls listings every 15 minutes (configurable) via Celery Beat schedule.
2. Raw payloads stored in S3, normalized events written to `ingested_listings` table and queued to Celery `ingestion_events` queue.
3. Scheduling service consumes events, enriches data, and updates `screenings` table. It schedules messaging jobs by pushing to `notification_jobs` queue.
4. Messaging service reads jobs, fetches subscriber preferences, and sends SMS via Twilio. Delivery results persisted to `message_deliveries`.
5. Admin console reads aggregated data from PostgreSQL, provides management operations via REST APIs, and surfaces observability metrics.

## Scalability Considerations
* Services are containerized and independently scalable.
* Celery workers can be scaled horizontally per workload (ingestion, scheduling, messaging).
* Read-heavy admin dashboards can leverage read replicas.
* Twilio webhooks handled by dedicated messaging worker instances.

## Disaster Recovery
* Automated PostgreSQL snapshots with point-in-time recovery.
* S3 versioning for raw payload archive.
* Immutable infrastructure deployments via Terraform and GitOps workflows.

