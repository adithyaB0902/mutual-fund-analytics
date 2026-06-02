-- 1. Top 5 Fund Houses by AUM

SELECT fund_house,
MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;

-- 2. Average NAV by Month

SELECT substr(nav_date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. Transaction Volume by State

SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 4. Total SIP Amount

SELECT SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP';

-- 5. Funds with Expense Ratio Below 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 5 Funds by 5-Year Return

SELECT scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average Return by Fund House

SELECT fund_house,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return DESC;

-- 8. Transactions by KYC Status

SELECT kyc_status,
COUNT(*) AS cnt
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Highest NAV Funds

SELECT amfi_code,
MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 10;

-- 10. Average AUM Across Fund Houses

SELECT AVG(aum_crore)
FROM fact_aum;
