import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv(
    "outputs/customer_segments.csv"
)

os.makedirs(
    "outputs/charts",
    exist_ok=True
)


print("=" * 70)
print("FINAL CUSTOMER SEGMENT VISUALIZATION")
print("=" * 70)


# =========================================================
# 1. CUSTOMER COUNT BY SEGMENT
# =========================================================

segment_counts = (
    df["Segment"]
    .value_counts()
)


plt.figure(
    figsize=(10, 6)
)

segment_counts.plot(
    kind="bar"
)

plt.title(
    "Number of Customers by Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/final_segment_count.png",
    dpi=300
)

plt.close()


# =========================================================
# 2. AVERAGE SPENDING BY SEGMENT
# =========================================================

spending = (
    df
    .groupby("Segment")["Total_Spend"]
    .mean()
    .sort_values(
        ascending=False
    )
)


plt.figure(
    figsize=(10, 6)
)

spending.plot(
    kind="bar"
)

plt.title(
    "Average Spending by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Average Total Spend"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/final_average_spending.png",
    dpi=300
)

plt.close()


# =========================================================
# 3. AVERAGE PURCHASE FREQUENCY
# =========================================================

frequency = (
    df
    .groupby("Segment")["Frequency"]
    .mean()
    .sort_values(
        ascending=False
    )
)


plt.figure(
    figsize=(10, 6)
)

frequency.plot(
    kind="bar"
)

plt.title(
    "Average Purchase Frequency by Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Average Purchase Frequency"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/final_purchase_frequency.png",
    dpi=300
)

plt.close()


# =========================================================
# 4. INCOME VS SPENDING BY SEGMENT
# =========================================================

plt.figure(
    figsize=(10, 7)
)

sns.scatterplot(
    data=df,
    x="Income",
    y="Total_Spend",
    hue="Segment",
    s=80
)

plt.title(
    "Income vs Spending by Customer Segment"
)

plt.xlabel(
    "Income"
)

plt.ylabel(
    "Total Spend"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/final_income_spending.png",
    dpi=300
)

plt.close()


# =========================================================
# 5. AGE VS SPENDING
# =========================================================

plt.figure(
    figsize=(10, 7)
)

sns.scatterplot(
    data=df,
    x="Age",
    y="Total_Spend",
    hue="Segment",
    s=80
)

plt.title(
    "Age vs Spending by Customer Segment"
)

plt.xlabel(
    "Age"
)

plt.ylabel(
    "Total Spend"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/final_age_spending.png",
    dpi=300
)

plt.close()


# =========================================================
# 6. SEGMENT SUMMARY
# =========================================================

summary = (
    df
    .groupby("Segment")
    .agg(
        Customers=("Customer_ID", "count"),
        Average_Age=("Age", "mean"),
        Average_Income=("Income", "mean"),
        Average_Spend=("Total_Spend", "mean"),
        Average_Purchases=("Total_Purchases", "mean"),
        Average_Frequency=("Frequency", "mean"),
        Average_Recency=("Recency", "mean")
    )
    .round(2)
)


print("\nFinal Segment Summary:")

print(
    summary
)


summary.to_csv(
    "outputs/final_segment_summary.csv"
)


# =========================================================
# COMPLETE
# =========================================================

print("\n" + "=" * 70)

print(
    "FINAL VISUALIZATIONS CREATED SUCCESSFULLY!"
)

print("=" * 70)

print("\nCharts created:")

print(
    "final_segment_count.png"
)

print(
    "final_average_spending.png"
)

print(
    "final_purchase_frequency.png"
)

print(
    "final_income_spending.png"
)

print(
    "final_age_spending.png"
)

print(
    "\nFinal summary:"
)

print(
    "outputs/final_segment_summary.csv"
)