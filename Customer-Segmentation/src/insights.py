import pandas as pd


# =========================================================
# 1. LOAD CLUSTERED DATA
# =========================================================

df = pd.read_csv(
    "outputs/customer_segments.csv"
)


print("=" * 70)
print("CUSTOMER SEGMENT ANALYSIS")
print("=" * 70)


# =========================================================
# 2. CREATE CLUSTER SUMMARY
# =========================================================

features = [
    "Age",
    "Income",
    "Total_Purchases",
    "Total_Spend",
    "Avg_Order_Value",
    "Recency",
    "Frequency"
]

summary = (
    df
    .groupby("Cluster")[features]
    .mean()
    .round(2)
)


print("\nCluster Summary:")
print(summary)


# =========================================================
# 3. IDENTIFY CLUSTERS
# =========================================================

high_spending_cluster = (
    summary["Total_Spend"]
    .idxmax()
)

high_frequency_cluster = (
    summary["Frequency"]
    .idxmax()
)

low_frequency_cluster = (
    summary["Frequency"]
    .idxmin()
)

high_recency_cluster = (
    summary["Recency"]
    .idxmax()
)


# =========================================================
# 4. ASSIGN BUSINESS SEGMENT NAMES
# =========================================================

segment_names = {}


for cluster in summary.index:

    # High spending + high frequency
    if (
        cluster == high_spending_cluster
        and cluster == high_frequency_cluster
    ):

        segment_names[
            cluster
        ] = "High-Value Customers"


    # Lower purchase frequency
    elif cluster == low_frequency_cluster:

        segment_names[
            cluster
        ] = "Occasional Customers"


    # Customers who have not purchased recently
    elif cluster == high_recency_cluster:

        segment_names[
            cluster
        ] = "At-Risk Customers"


    else:

        segment_names[
            cluster
        ] = "Regular Customers"


# =========================================================
# 5. APPLY SEGMENT NAMES
# =========================================================

df["Segment"] = (
    df["Cluster"]
    .map(segment_names)
)


# =========================================================
# 6. CREATE SEGMENT SUMMARY
# =========================================================

segment_summary = (
    df
    .groupby("Segment")
    .agg(

        Customers=(
            "Customer_ID",
            "count"
        ),

        Average_Age=(
            "Age",
            "mean"
        ),

        Average_Income=(
            "Income",
            "mean"
        ),

        Average_Purchases=(
            "Total_Purchases",
            "mean"
        ),

        Average_Spend=(
            "Total_Spend",
            "mean"
        ),

        Average_Order_Value=(
            "Avg_Order_Value",
            "mean"
        ),

        Average_Recency=(
            "Recency",
            "mean"
        ),

        Average_Frequency=(
            "Frequency",
            "mean"
        )
    )
    .round(2)
)


# =========================================================
# 7. PRINT FINAL SEGMENTS
# =========================================================

print("\n" + "=" * 70)

print("CUSTOMER SEGMENTS")

print("=" * 70)

print(
    "\n"
)

print(
    segment_summary
)


# =========================================================
# 8. SAVE FINAL DATASET
# =========================================================

df.to_csv(
    "outputs/customer_segments.csv",
    index=False
)


# =========================================================
# 9. SAVE SEGMENT SUMMARY
# =========================================================

segment_summary.to_csv(
    "outputs/segment_summary.csv"
)


# =========================================================
# 10. CREATE BUSINESS INSIGHTS FILE
# =========================================================

with open(
    "outputs/business_insights.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "CUSTOMER SEGMENTATION - BUSINESS INSIGHTS\n"
    )

    file.write(
        "==========================================\n\n"
    )

    file.write(
        f"Total Customers: {len(df)}\n"
    )

    file.write(
        f"Number of Segments: "
        f"{len(segment_summary)}\n\n"
    )


    # -----------------------------------------------------
    # INDIVIDUAL SEGMENT INSIGHTS
    # -----------------------------------------------------

    for segment in segment_summary.index:

        row = segment_summary.loc[
            segment
        ]


        file.write(
            "\n"
        )

        file.write(
            f"SEGMENT: {segment}\n"
        )

        file.write(
            "-" * 55 + "\n"
        )

        file.write(
            f"Number of Customers: "
            f"{int(row['Customers'])}\n"
        )

        file.write(
            f"Average Age: "
            f"{row['Average_Age']:.2f}\n"
        )

        file.write(
            f"Average Income: "
            f"{row['Average_Income']:.2f}\n"
        )

        file.write(
            f"Average Purchases: "
            f"{row['Average_Purchases']:.2f}\n"
        )

        file.write(
            f"Average Spending: "
            f"{row['Average_Spend']:.2f}\n"
        )

        file.write(
            f"Average Order Value: "
            f"{row['Average_Order_Value']:.2f}\n"
        )

        file.write(
            f"Average Recency: "
            f"{row['Average_Recency']:.2f} days\n"
        )

        file.write(
            f"Average Frequency: "
            f"{row['Average_Frequency']:.2f}\n"
        )


        # -------------------------------------------------
        # BUSINESS STRATEGIES
        # -------------------------------------------------

        if segment == "High-Value Customers":

            file.write(
                "\nRecommended Business Strategy:\n"
            )

            file.write(
                "- Introduce loyalty and VIP programs.\n"
            )

            file.write(
                "- Offer premium products.\n"
            )

            file.write(
                "- Provide personalized recommendations.\n"
            )

            file.write(
                "- Give exclusive offers and early access.\n"
            )


        elif segment == "Occasional Customers":

            file.write(
                "\nRecommended Business Strategy:\n"
            )

            file.write(
                "- Provide discount coupons.\n"
            )

            file.write(
                "- Encourage repeat purchases.\n"
            )

            file.write(
                "- Send personalized product recommendations.\n"
            )

            file.write(
                "- Use promotional campaigns.\n"
            )


        elif segment == "At-Risk Customers":

            file.write(
                "\nRecommended Business Strategy:\n"
            )

            file.write(
                "- Launch re-engagement campaigns.\n"
            )

            file.write(
                "- Send win-back offers.\n"
            )

            file.write(
                "- Provide limited-time discounts.\n"
            )

            file.write(
                "- Send personalized reminders.\n"
            )


        else:

            file.write(
                "\nRecommended Business Strategy:\n"
            )

            file.write(
                "- Encourage loyalty membership.\n"
            )

            file.write(
                "- Offer bundle discounts.\n"
            )

            file.write(
                "- Recommend related products.\n"
            )

            file.write(
                "- Increase purchase frequency.\n"
            )


# =========================================================
# 11. FINAL MESSAGE
# =========================================================

print("\n" + "=" * 70)

print(
    "BUSINESS INSIGHTS GENERATED SUCCESSFULLY!"
)

print("=" * 70)

print("\nGenerated files:")

print(
    "outputs/customer_segments.csv"
)

print(
    "outputs/segment_summary.csv"
)

print(
    "outputs/business_insights.txt"
)