# Customer Segmentation Using Machine Learning

## Project Overview

Customer segmentation is the process of dividing customers into groups based on similar characteristics, purchasing behavior, and preferences.

This project uses Machine Learning clustering techniques to identify meaningful customer segments and provide business recommendations for targeted marketing.

## Objectives

- Analyze customer demographics.
- Analyze purchasing behavior.
- Identify groups of similar customers.
- Apply K-Means clustering.
- Determine the optimal number of clusters.
- Visualize customer segments.
- Generate business insights.
- Support targeted marketing strategies.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering
- PCA
- Power BI

## Dataset Features

The dataset contains:

- Customer ID
- Age
- Gender
- Income
- Total Purchases
- Total Spend
- Average Order Value
- Recency
- Frequency
- Location
- Preferred Category

## Project Workflow

1. Dataset Generation
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Feature Scaling
6. Elbow Method
7. Silhouette Score Analysis
8. K-Means Clustering
9. PCA Visualization
10. Customer Segment Analysis
11. Business Insights
12. Power BI Dashboard

## Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised machine learning algorithm that groups data points into clusters based on similarity.

The algorithm works by:

1. Selecting the number of clusters.
2. Initializing cluster centroids.
3. Assigning customers to the nearest centroid.
4. Updating centroid positions.
5. Repeating the process until convergence.

## Feature Scaling

StandardScaler is used before clustering because the dataset contains features with different numerical ranges.

## Evaluation

Two techniques are used:

### Elbow Method

The Elbow Method analyzes clustering inertia for different numbers of clusters.

### Silhouette Score

Silhouette Score measures how well each customer fits within its assigned cluster.

A higher score generally indicates better-separated clusters.

## Business Insights

The project identifies customer groups such as:

### High-Value Customers

Customers with relatively high spending and purchasing activity.

Recommended strategies:

- Loyalty programs
- Premium offers
- Personalized recommendations
- Exclusive discounts

### Regular Customers

Customers who purchase consistently.

Recommended strategies:

- Membership programs
- Product recommendations
- Bundle offers
- Loyalty rewards

### Occasional Customers

Customers with relatively low purchasing activity.

Recommended strategies:

- Promotional offers
- Discount coupons
- Product recommendations
- Repeat-purchase campaigns

### At-Risk Customers

Customers who have not purchased recently.

Recommended strategies:

- Re-engagement campaigns
- Win-back offers
- Personalized reminders
- Limited-time discounts

## Project Output

The project generates:

- Clean customer dataset
- Customer segmentation dataset
- Cluster summary
- Segment summary
- Business insights
- EDA charts
- Elbow Method chart
- Silhouette Score chart
- Customer cluster visualization
- Income vs spending visualization

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt 

Run the complete project:

python main.py



## Author

Sarthak Bhangade

B.Tech Artificial Intelligence & Data Science
Sanjivani University
