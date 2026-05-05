---
title: "Building a Medallion Architecture on Databricks (AWS)"
date: 2025-01-15
categories: [Databricks, Architecture]
---

The Medallion Architecture has become the de facto standard for organizing data in a lakehouse. In this post, we explore how to implement Bronze, Silver, and Gold layers on Databricks running on AWS.

## Why Medallion?

The three-layer approach provides clear separation of concerns:

- **Bronze**: Raw ingestion, append-only, schema-on-read
- **Silver**: Cleansed, conformed, business-ready entities
- **Gold**: Aggregated, curated datasets for analytics and reporting

## Implementation on Databricks + AWS

Using Delta Live Tables (DLT), we can declaratively define each layer with built-in data quality expectations and lineage tracking.

```python
@dlt.table(name="bronze_transactions")
def bronze_transactions():
    return spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "json") \
        .load("s3://raw-bucket/transactions/")
```

Stay tuned for the full implementation guide.
