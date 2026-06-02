# Day 2 Summary – Data Cleaning & SQLite Database

## Objectives Completed

* Cleaned NAV history dataset
* Cleaned investor transactions dataset
* Cleaned scheme performance dataset
* Generated 10 processed CSV files
* Designed star schema
* Implemented SQLite database
* Loaded all datasets using SQLAlchemy
* Verified row counts
* Created analytical SQL queries
* Created data dictionary

## Database Tables

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

## Validation Results

| Table             |  Rows |
| ----------------- | ----: |
| dim_fund          |    40 |
| fact_nav          | 45913 |
| fact_transactions | 32778 |
| fact_performance  |    40 |
| fact_aum          |    90 |

## Outcome

Day 2 requirements completed successfully.
