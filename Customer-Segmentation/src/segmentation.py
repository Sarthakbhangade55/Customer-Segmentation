import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA


# =========================================================
# 1. LOAD DATASET
# =========================================================

df = pd.read_csv("data/customers.csv")

print("=" * 70)
print("CUSTOMER SEGMENTATION USING K-MEANS")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)


# =========================================================
# 2. SELECT FEATURES
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

X = df[features].copy()

print("\nFeatures used for clustering:")
print(features)


# =========================================================
# 3. STANDARDIZE FEATURES
# =========================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeature scaling completed.")


# =========================================================
# 4. ELBOW METHOD
# =========================================================

print("\nCalculating Elbow Method...")

inertia = []

k_values = range(2, 11)

for k in k_values:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertia.append(
        model.inertia_
    )


# Create Elbow Chart

plt.figure(figsize=(10, 6))

plt.plot(
    list(k_values),
    inertia,
    marker="o"
)

plt.title(
    "Elbow Method for Optimal Number of Clusters"
)

plt.xlabel(
    "Number of Clusters"
)

plt.ylabel(
    "Inertia"
)

plt.xticks(
    list(k_values)
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/elbow_method.png",
    dpi=300
)

plt.close()

print(
    "Elbow Method chart saved."
)


# =========================================================
# 5. SILHOUETTE SCORE
# =========================================================

print("\nCalculating Silhouette Scores...")

silhouette_scores = []

for k in k_values:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(
        X_scaled
    )

    score = silhouette_score(
        X_scaled,
        labels
    )

    silhouette_scores.append(
        score
    )


# Create Silhouette Chart

plt.figure(figsize=(10, 6))

plt.plot(
    list(k_values),
    silhouette_scores,
    marker="o"
)

plt.title(
    "Silhouette Score Analysis"
)

plt.xlabel(
    "Number of Clusters"
)

plt.ylabel(
    "Silhouette Score"
)

plt.xticks(
    list(k_values)
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/silhouette_scores.png",
    dpi=300
)

plt.close()


# =========================================================
# 6. FIND BEST NUMBER OF CLUSTERS
# =========================================================

best_k = list(k_values)[
    np.argmax(silhouette_scores)
]

best_score = max(
    silhouette_scores
)

print("\n" + "=" * 70)

print(
    f"Best Number of Clusters: {best_k}"
)

print(
    f"Best Silhouette Score: {best_score:.4f}"
)

print("=" * 70)


# =========================================================
# 7. APPLY K-MEANS
# =========================================================

print("\nTraining K-Means model...")

kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(
    X_scaled
)

print(
    "K-Means clustering completed."
)


# =========================================================
# 8. CLUSTER SUMMARY
# =========================================================

cluster_summary = (
    df
    .groupby("Cluster")[features]
    .mean()
    .round(2)
)

print("\nCluster Summary:")

print(
    cluster_summary
)


# =========================================================
# 9. CUSTOMER COUNT PER CLUSTER
# =========================================================

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .sort_index()
)

print("\nCustomers in Each Cluster:")

print(
    cluster_counts
)


# =========================================================
# 10. PCA FOR 2D VISUALIZATION
# =========================================================

print("\nCreating PCA visualization...")

pca = PCA(
    n_components=2
)

X_pca = pca.fit_transform(
    X_scaled
)

pca_df = pd.DataFrame(
    X_pca,
    columns=[
        "PCA1",
        "PCA2"
    ]
)

pca_df["Cluster"] = (
    df["Cluster"]
)


# =========================================================
# 11. CLUSTER VISUALIZATION
# =========================================================

plt.figure(
    figsize=(10, 7)
)

sns.scatterplot(
    data=pca_df,
    x="PCA1",
    y="PCA2",
    hue="Cluster",
    palette="viridis",
    s=70
)

plt.title(
    "Customer Segmentation using K-Means"
)

plt.xlabel(
    "Principal Component 1"
)

plt.ylabel(
    "Principal Component 2"
)

plt.legend(
    title="Cluster"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/customer_clusters.png",
    dpi=300
)

plt.close()


# =========================================================
# 12. INCOME VS SPENDING
# =========================================================

plt.figure(
    figsize=(10, 7)
)

sns.scatterplot(
    data=df,
    x="Income",
    y="Total_Spend",
    hue="Cluster",
    palette="viridis",
    s=70
)

plt.title(
    "Customer Segments: Income vs Total Spending"
)

plt.xlabel(
    "Income"
)

plt.ylabel(
    "Total Spend"
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/income_spending_clusters.png",
    dpi=300
)

plt.close()


# =========================================================
# 13. CLUSTER DISTRIBUTION
# =========================================================

plt.figure(
    figsize=(10, 6)
)

cluster_counts.plot(
    kind="bar"
)

plt.title(
    "Number of Customers in Each Cluster"
)

plt.xlabel(
    "Cluster"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/cluster_distribution.png",
    dpi=300
)

plt.close()


# =========================================================
# 14. SAVE RESULTS
# =========================================================

os.makedirs(
    "outputs",
    exist_ok=True
)

df.to_csv(
    "outputs/customer_segments.csv",
    index=False
)

cluster_summary.to_csv(
    "outputs/cluster_summary.csv"
)


# =========================================================
# 15. SAVE MODEL RESULTS
# =========================================================

with open(
    "outputs/model_results.txt",
    "w"
) as file:

    file.write(
        "CUSTOMER SEGMENTATION MODEL RESULTS\n"
    )

    file.write(
        "====================================\n\n"
    )

    file.write(
        f"Number of Customers: {len(df)}\n"
    )

    file.write(
        f"Number of Features: {len(features)}\n"
    )

    file.write(
        f"Best Number of Clusters: {best_k}\n"
    )

    file.write(
        f"Best Silhouette Score: {best_score:.4f}\n\n"
    )

    file.write(
        "Features Used:\n"
    )

    for feature in features:

        file.write(
            f"- {feature}\n"
        )

    file.write(
        "\nCluster Summary:\n\n"
    )

    file.write(
        cluster_summary.to_string()
    )


# =========================================================
# FINISHED
# =========================================================

print("\n" + "=" * 70)

print(
    "CUSTOMER SEGMENTATION COMPLETED SUCCESSFULLY!"
)

print("=" * 70)

print("\nGenerated files:")

print(
    "outputs/customer_segments.csv"
)

print(
    "outputs/cluster_summary.csv"
)

print(
    "outputs/model_results.txt"
)

print(
    "outputs/charts/elbow_method.png"
)

print(
    "outputs/charts/silhouette_scores.png"
)

print(
    "outputs/charts/customer_clusters.png"
)

print(
    "outputs/charts/income_spending_clusters.png"
)

print(
    "outputs/charts/cluster_distribution.png"
)