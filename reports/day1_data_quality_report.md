# Day 1 Data Quality Report

## Dataset Overview

Total Datasets Loaded: 10

## Fund Master Dataset

Total Schemes: 40

Columns:
- amfi_code
- fund_house
- scheme_name
- category
- sub_category
- plan
- launch_date
- benchmark
- expense_ratio_pct
- exit_load_pct
- min_sip_amount
- min_lumpsum_amount
- fund_manager
- risk_category
- sebi_category_code

## NAV History Dataset

Contains historical NAV records for all schemes.

## AMFI Validation

Codes in Fund Master: 40

Codes in NAV History: 40

Missing Codes: 0

Result:
All AMFI codes from Fund Master are present in NAV History.

## Data Quality Status

✓ Data ingestion successful

✓ All datasets loaded successfully

✓ AMFI validation passed

✓ Ready for transformation and analysis
