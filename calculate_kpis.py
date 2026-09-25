import pandas as pd

df = pd.read_csv("cleaned_business_data.csv")

# Business scenario: a small retail store selling Electronics, Furniture,
# and Stationery, wanting to track overall health, customer loyalty,
# category performance, and payment trends.

# KPI 1: Total Revenue
total_revenue = df['TotalPrice'].sum()

# KPI 2: Average Order Value (AOV)
aov = df['TotalPrice'].mean()

# KPI 3: Repeat Customer Rate (% of orders from returning customers)
repeat_orders = (df['CustomerType'] == 'Returning').sum()
repeat_customer_rate = (repeat_orders / len(df)) * 100

# KPI 4: Top Category Revenue Share (%)
by_category = df.groupby('Category')['TotalPrice'].sum().sort_values(ascending=False)
top_category = by_category.index[0]
top_category_share = (by_category.iloc[0] / total_revenue) * 100

# KPI 5: Digital Payment Adoption Rate (% of orders paid via Card or UPI, not Cash)
digital_orders = df['PaymentMethod'].isin(['Card', 'UPI']).sum()
digital_payment_rate = (digital_orders / len(df)) * 100

print("KPI 1 - Total Revenue: $", round(total_revenue, 2))
print("KPI 2 - Average Order Value: $", round(aov, 2))
print("KPI 3 - Repeat Customer Rate:", round(repeat_customer_rate, 1), "%")
print(f"KPI 4 - Top Category Revenue Share ({top_category}):", round(top_category_share, 1), "%")
print("KPI 5 - Digital Payment Adoption Rate:", round(digital_payment_rate, 1), "%")

# supporting breakdowns for the charts
by_category.to_csv("kpi_category_breakdown.csv")
df.groupby('PaymentMethod')['TotalPrice'].sum().to_csv("kpi_payment_breakdown.csv")
df.groupby('CustomerType')['TotalPrice'].sum().to_csv("kpi_customertype_breakdown.csv")

kpi_summary = pd.DataFrame({
    "KPI": ["Total Revenue", "Average Order Value", "Repeat Customer Rate",
            f"Top Category Share ({top_category})", "Digital Payment Adoption Rate"],
    "Value": [round(total_revenue, 2), round(aov, 2), round(repeat_customer_rate, 1),
              round(top_category_share, 1), round(digital_payment_rate, 1)],
    "Unit": ["$", "$", "%", "%", "%"]
})
kpi_summary.to_csv("kpi_summary.csv", index=False)
print("\nSaved kpi_summary.csv and breakdown files")
