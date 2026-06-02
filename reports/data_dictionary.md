# Data Dictionary

## 01_fund_master.csv

| Column             | Type    | Description                 |
| ------------------ | ------- | --------------------------- |
| amfi_code          | Integer | Unique AMFI scheme code     |
| fund_house         | Text    | Asset Management Company    |
| scheme_name        | Text    | Name of mutual fund scheme  |
| category           | Text    | Fund category               |
| sub_category       | Text    | Sub-category of scheme      |
| plan               | Text    | Direct / Regular plan       |
| launch_date        | Date    | Scheme launch date          |
| benchmark          | Text    | Benchmark index             |
| expense_ratio_pct  | Float   | Annual expense ratio        |
| exit_load_pct      | Float   | Exit load percentage        |
| min_sip_amount     | Float   | Minimum SIP amount          |
| min_lumpsum_amount | Float   | Minimum lump sum investment |
| fund_manager       | Text    | Fund manager                |
| risk_category      | Text    | Risk classification         |
| sebi_category_code | Text    | SEBI category identifier    |

## 02_nav_history.csv

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | Integer | Scheme code     |
| date      | Date    | NAV date        |
| nav       | Float   | Net Asset Value |

## 03_aum_by_fund_house.csv

| Column         | Type    | Description       |
| -------------- | ------- | ----------------- |
| date           | Date    | Reporting date    |
| fund_house     | Text    | Fund house        |
| aum_lakh_crore | Float   | AUM in lakh crore |
| aum_crore      | Float   | AUM in crore      |
| num_schemes    | Integer | Number of schemes |

## 07_scheme_performance.csv

Contains fund return metrics, risk measures, ratings and expense ratios.

## 08_investor_transactions.csv

Contains investor transactions, SIPs, redemptions, KYC status and demographic information.
