import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

df = pd.read_csv("data/customers.csv")


# Create output folder

os.makedirs(
    "outputs/charts",
    exist_ok=True
)


print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# ---------------------------------------------------------
# BASIC DATA INFORMATION
# ---------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nCustomer Gender:")
print(df["Gender"].value_counts())

print("\nPreferred Categories:")
print(df["Preferred_Category"].value_counts())

print("\nLocations:")
print(df["Location"].value_counts())


# ---------------------------------------------------------
# CHART 1 - AGE DISTRIBUTION
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Age"],
    bins=20,
    kde=True
)

plt.title("Customer Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/age_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 2 - INCOME DISTRIBUTION
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Income"],
    bins=25,
    kde=True
)

plt.title("Customer Income Distribution")

plt.xlabel("Income")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/income_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 3 - TOTAL SPENDING
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Total_Spend"],
    bins=25,
    kde=True
)

plt.title("Customer Spending Distribution")

plt.xlabel("Total Spend")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/spending_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 4 - INCOME VS SPENDING
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Income",
    y="Total_Spend"
)

plt.title("Income vs Total Spending")

plt.xlabel("Income")

plt.ylabel("Total Spend")

plt.tight_layout()

plt.savefig(
    "outputs/charts/income_vs_spending.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 5 - PURCHASE FREQUENCY
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Frequency"],
    bins=20,
    kde=True
)

plt.title("Customer Purchase Frequency")

plt.xlabel("Number of Purchases")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "outputs/charts/purchase_frequency.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 6 - PREFERRED CATEGORY
# ---------------------------------------------------------

category_counts = (
    df["Preferred_Category"]
    .value_counts()
)

plt.figure(figsize=(10, 6))

category_counts.plot(
    kind="bar"
)

plt.title(
    "Customer Preferred Product Categories"
)

plt.xlabel(
    "Product Category"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/preferred_categories.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 7 - GENDER DISTRIBUTION
# ---------------------------------------------------------

gender_counts = (
    df["Gender"]
    .value_counts()
)

plt.figure(figsize=(8, 6))

gender_counts.plot(
    kind="bar"
)

plt.title(
    "Customer Gender Distribution"
)

plt.xlabel(
    "Gender"
)

plt.ylabel(
    "Number of Customers"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/gender_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 8 - LOCATION DISTRIBUTION
# ---------------------------------------------------------

location_counts = (
    df["Location"]
    .value_counts()
)

plt.figure(figsize=(10, 6))

location_counts.plot(
    kind="bar"
)

plt.title(
    "Customers by Location"
)

plt.xlabel(
    "Location"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/location_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# CHART 9 - CORRELATION HEATMAP
# ---------------------------------------------------------

numeric_df = df.select_dtypes(
    include="number"
)

correlation = numeric_df.corr()

plt.figure(
    figsize=(10, 8)
)

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title(
    "Customer Data Correlation Matrix"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/correlation_heatmap.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# FINISHED
# ---------------------------------------------------------

print("\n" + "=" * 60)

print("EDA COMPLETED SUCCESSFULLY!")

print("=" * 60)

print("\nCharts have been saved in:")

print("outputs/charts/")