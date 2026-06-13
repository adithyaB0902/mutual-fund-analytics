# 📊 Mutual Fund Analytics Platform

## Bluestock Internship Capstone Project

A comprehensive end-to-end Mutual Fund Analytics Platform developed during the Bluestock Internship. The project combines Data Engineering, Exploratory Data Analysis (EDA), Financial Performance Analytics, Advanced Risk Analytics, Investor Behavior Analysis, and Interactive Power BI Dashboards to generate actionable insights from mutual fund industry data.

---

# 👨‍💻 Author

**Adithya B**

Vel Tech High Tech Engineering College

Bluestock Internship Capstone Project

Internship Duration: **01 June 2026 – 12 June 2026**

---

# 🎯 Project Objectives

- Build a complete ETL pipeline for mutual fund datasets.
- Perform Exploratory Data Analysis (EDA).
- Evaluate mutual fund performance using financial metrics.
- Analyze investment risk and downside exposure.
- Study investor demographics and behavior.
- Develop a fund recommendation system.
- Create interactive Power BI dashboards.
- Generate business insights for investment decision-making.

---

# 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SciPy

### Dashboard
- Power BI Desktop

### Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# 📂 Datasets Used

| Dataset | Description |
|----------|-------------|
| fund_master.csv | Mutual fund scheme information |
| nav_history.csv | Daily NAV values |
| aum_history.csv | Assets Under Management history |
| sip_inflows.csv | Monthly SIP statistics |
| category_inflows.csv | Category-wise inflows |
| industry_folios.csv | Industry folio growth |
| investor_transactions.csv | Investor transaction records |
| portfolio_holdings.csv | Portfolio sector allocations |

---

# 📁 Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── Day1_Data_Quality.ipynb
│   ├── Day2_ETL.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   ├── Dashboard.pdf
│   ├── fund_scorecard.csv
│   ├── alpha_beta.csv
│   ├── tracking_error.csv
│   ├── var_cvar_report.csv
│   └── charts/
│
├── presentation/
│   └── Bluestock_MF_Presentation.pptx
│
├── recommender.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# 🚀 Day-by-Day Project Execution

## Day 1 – Data Collection & Quality Assessment

### Tasks Completed
- Imported all datasets
- Examined schema structures
- Checked missing values
- Identified duplicate records
- Validated data types
- Created data dictionary

### Deliverables
- Data Quality Report
- Data Dictionary

### Key Findings
- No major missing values
- Consistent schema across datasets
- Over 46,000 NAV records available

---

## Day 2 – ETL Pipeline Development

### Tasks Completed
- Data cleaning
- Data transformation
- Standardization of formats
- Dataset validation
- Processed dataset generation

### Deliverables
- ETL Notebook
- Cleaned datasets
- Processed CSV files

### Workflow

```text
Raw Data
    ↓
Cleaning
    ↓
Transformation
    ↓
Validation
    ↓
Processed Data
```

---

## Day 3 – Exploratory Data Analysis (EDA)

### Analyses Performed
- NAV Trend Analysis
- AUM Growth Analysis
- SIP Inflow Trend Analysis
- Category Inflow Heatmap
- Investor Demographics Analysis
- Geographic Distribution Analysis
- Folio Growth Analysis
- NAV Correlation Matrix
- Sector Allocation Analysis

### Key Findings
- SIP inflows reached ₹31,002 Cr
- Folio count nearly doubled
- Equity funds attracted the highest inflows
- Technology and Financial sectors dominated allocations

### Deliverables
- EDA_Analysis.ipynb
- 15+ Visualizations

---

## Day 4 – Performance Analytics

### Metrics Computed

#### Return Metrics
- Daily Returns
- CAGR

#### Risk Metrics
- Sharpe Ratio
- Sortino Ratio

#### Market Metrics
- Alpha
- Beta

#### Downside Risk
- Maximum Drawdown

### Additional Analysis
- Fund Scorecard
- Benchmark Comparison
- Tracking Error

### Deliverables
- Performance_Analytics.ipynb
- fund_scorecard.csv
- alpha_beta.csv

### Key Findings
- Small-cap funds generated the highest CAGR
- Several funds achieved Sharpe Ratios greater than 1
- Positive Alpha observed in top-performing funds

---

## Day 5 – Power BI Dashboard Development

### Dashboard Pages

### Page 1 – Industry Overview
- KPI Cards
- Industry AUM Trend
- AUM by Fund House

### Page 2 – Fund Performance
- Return vs Risk Scatter Plot
- Fund Scorecard
- NAV Comparison

### Page 3 – Investor Analytics
- State-wise Investments
- Age Group Analysis
- Transaction Trends

### Page 4 – SIP & Market Trends
- SIP Growth Trend
- Category Heatmap
- Top Categories by Inflow

### Deliverables
- bluestock_mf_dashboard.pbix
- Dashboard PDF
- Dashboard Screenshots

---

## Day 6 – Advanced Analytics

### Risk Analytics
- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio

### Investor Analytics
- Cohort Analysis
- SIP Continuity Analysis

### Recommendation System
- Low Risk Fund Recommendations
- Moderate Risk Fund Recommendations
- High Risk Fund Recommendations

### Portfolio Analytics
- HHI Sector Concentration Analysis

### Deliverables
- Advanced_Analytics.ipynb
- var_cvar_report.csv
- recommender.py

### Key Findings
- Several funds showed high downside risk
- Most investors were classified as At-Risk
- Portfolio concentration varied significantly across funds

---

## Day 7 – Final Packaging & Documentation

### Tasks Completed
- Final Report Creation
- PowerPoint Presentation
- Dashboard Documentation
- GitHub Repository Preparation
- README Documentation

### Deliverables
- Final_Report.pdf
- Bluestock_MF_Presentation.pptx
- README.md
- GitHub Release v1.0

---

# 📊 Key Business Insights

### Industry Insights
- SIP inflows reached record levels.
- Mutual fund participation continues to increase.
- Industry AUM demonstrated consistent growth.

### Fund Insights
- Small-cap funds delivered the strongest returns.
- Risk-adjusted rankings differed from return-based rankings.
- Diversified portfolios showed better downside protection.

### Investor Insights
- 2024 investor cohort contributed the largest investment volume.
- Most investors were classified as At-Risk in SIP continuity analysis.
- Urban investors contributed the majority of investments.

### Portfolio Insights
- Technology and Financial Services sectors dominated allocations.
- Several funds exhibited concentration risk.

---

# 📈 Dashboard Features

### Interactive Filters
- Fund House
- Category
- Plan Type
- State
- Age Group
- City Tier

### Visualizations
- KPI Cards
- Heatmaps
- Scatter Plots
- Trend Lines
- Donut Charts
- Risk Analytics Charts

---

# 🔮 Future Enhancements

### Machine Learning
- Fund Recommendation Models
- Investor Churn Prediction
- SIP Discontinuation Forecasting

### Real-Time Analytics
- Live NAV APIs
- Real-Time Dashboard Updates
- Automated Reporting

### Cloud Deployment
- Azure
- AWS
- Power BI Service

---

# 🏆 Project Outcomes

✅ Complete ETL Pipeline Developed

✅ Comprehensive EDA Performed

✅ Financial Performance Metrics Implemented

✅ Advanced Risk Analytics Completed

✅ Investor Recommendation System Built

✅ Interactive Power BI Dashboard Developed

✅ Business Intelligence Insights Generated

✅ End-to-End Mutual Fund Analytics Solution Delivered

---

# 📜 License

This project was developed for educational and internship purposes as part of the Bluestock Internship Program.

---
# Bonus Financial Analytics

## Monte Carlo Simulation

A 5-year Monte Carlo simulation was performed using historical daily returns to project future NAV growth under uncertainty.

Outputs:
- Monte Carlo Projection Chart
- Confidence Band Visualization

## Markowitz Portfolio Optimization

Modern Portfolio Theory (MPT) was applied to identify the optimal allocation among selected mutual funds.

Outputs:
- Efficient Frontier
- Optimal Portfolio Allocation
- Sharpe-Maximizing Portfolio


```