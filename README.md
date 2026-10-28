# AutoHeal Demo ETL Service

This is a demonstration ETL data pipeline designed for validating the **AutoHeal Agent** (autonomous self-healing data engineering system).

## Intentional Bug
In `etl/pipeline.py`, the function `calculate_revenue()` accesses `df['total_price']`, which does not exist in `data/sales.csv` (the valid column is `price`).
When run on GitHub Actions, the pipeline fails with `KeyError: 'total_price'`.

AutoHeal Agent detects this failure, performs Root Cause Analysis, self-corrects the code, verifies the fix in an isolated sandbox, and automatically submits a Draft Pull Request.
