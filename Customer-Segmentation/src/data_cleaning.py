import os
import numpy as np
import pandas as pd


# ---------------------------------------------------------
# CUSTOMER DATA GENERATION
# ---------------------------------------------------------

np.random.seed(42)

number_of_customers = 1000

customer_ids = [
    f"CUST{str(i).zfill(4)}"
    for i in range(1, number_of_customers + 1)
]

age = np.random.randint(18, 65, number_of_customers)

gender = np.random.choice(
    ["Male", "Female"],
    number_of_customers,
    p=[0.52, 0.48]
)

income = np.random.randint(
    20000,
    150001,
    number_of_customers
)

total_purchases = np.random.randint(
    1,
    51,
    number_of_customers
)

avg_order_value = np.round(
    np.random.uniform(200, 3000, number_of_customers),
    2
)

total_spend = np.round(
    total_purchases * avg_order_value,
    2
)

frequency = total_purchases

recency = np.random.randint(
    1,
    181,
    number_of_customers
)

location = np.random.choice(
    [
        "Maharashtra",
        "Gujarat",
        "Karnataka",
        "Delhi",
        "Tamil Nadu",
        "Rajasthan"
    ],
    number_of_customers
)

preferred_category = np.random.choice(
    [
        "Electronics",
        "Fashion",
        "Groceries",
        "Beauty",
        "Home",
        "Sports"
    ],
    number_of_customers
)


df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": age,
    "Gender": gender,
    "Income": income,
    "Total_Purchases": total_purchases,
    "Total_Spend": total_spend,
    "Avg_Order_Value": avg_order_value,
    "Recency": recency,
    "Frequency": frequency,
    "Location": location,
    "Preferred_Category": preferred_category
})


# ---------------------------------------------------------
# ADD SOME MISSING VALUES
# ---------------------------------------------------------

missing_indices = np.random.choice(
    df.index,
    size=20,
    replace=False
)

df.loc[missing_indices[:10], "Income"] = np.nan
df.loc[missing_indices[10:], "Age"] = np.nan


# ---------------------------------------------------------
# SAVE RAW DATA
# ---------------------------------------------------------

os.makedirs("data", exist_ok=True)

raw_file = "data/customers_raw.csv"

df.to_csv(
    raw_file,
    index=False
)


# ---------------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------------

print("\nRaw Dataset Shape:")
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# Fill numerical missing values with median

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Income"] = df["Income"].fillna(
    df["Income"].median()
)


# Remove duplicate rows

df = df.drop_duplicates()


# Make sure numerical columns are correct

numeric_columns = [
    "Age",
    "Income",
    "Total_Purchases",
    "Total_Spend",
    "Avg_Order_Value",
    "Recency",
    "Frequency"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# Remove any remaining invalid rows

df = df.dropna(
    subset=numeric_columns
)


# ---------------------------------------------------------
# SAVE CLEAN DATASET
# ---------------------------------------------------------

clean_file = "data/customers.csv"

df.to_csv(
    clean_file,
    index=False
)


# ---------------------------------------------------------
# FINAL INFORMATION
# ---------------------------------------------------------

print("\nDataset after cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFirst 5 Records:")
print(df.head())

print("\nCustomer dataset successfully created!")

print(f"\nSaved to: {clean_file}")