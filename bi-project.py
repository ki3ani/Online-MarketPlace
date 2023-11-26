import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the sales dataset
df_sales = pd.read_csv(('C:/Users/Admin/Online-MarketPlace/data/amazon.csv'))

# Load the customer behavior dataset
df_customer_behavior = pd.read_csv('C:/Users/Admin/Online-MarketPlace/data/customer-behavior.csv')


# Display the first few rows of each dataset
print("Sales Dataset:")
print(df_sales.head())
print("\nCustomer Behavior Dataset:")
print(df_customer_behavior.head())

# Measure of Frequency - Countplot for product categories
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=df_sales)
plt.title('Count of Products in Each Category')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.show()

# Measure of Central Tendency - Distribution of discounted prices
plt.figure(figsize=(10, 6))
sns.histplot(df_sales['discounted_price'], bins=30, kde=True)
plt.title('Distribution of Discounted Prices')
plt.xlabel('Discounted Price')
plt.ylabel('Frequency')
plt.show()

# Measure of Distribution - Distribution of discount percentages
plt.figure(figsize=(10, 6))
sns.histplot(df_sales['discount_percentage'], bins=20, kde=True)
plt.title('Distribution of Discount Percentages')
plt.xlabel('Discount Percentage')
plt.ylabel('Frequency')
plt.show()

# Measure of Relationship - Scatter plot of discounted price vs. rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='discounted_price', y='rating', data=df_sales)
plt.title('Scatter Plot of Discounted Price vs. Rating')
plt.xlabel('Discounted Price')
plt.ylabel('Rating')
plt.show()

# Measures of Relationship
plt.figure(figsize=(12, 6))
sns.regplot(x='actual_price', y='discounted_price', data=df_sales)
plt.title('Scatter Plot with Regression Line')
plt.show()

# Correlation Matrix (Measures of Relationship for numerical columns)
correlation_matrix = df_sales.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Sales Dataset')
plt.show()


# Measure of Frequency - Countplot for gender
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=df_customer_behavior)
plt.title('Count of Respondents in Each Gender Category')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Measure of Central Tendency - Distribution of age
plt.figure(figsize=(10, 6))
sns.histplot(df_customer_behavior['age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Measure of Distribution - Distribution of purchase frequencies
plt.figure(figsize=(10, 6))
sns.histplot(df_customer_behavior['Purchase_Frequency'], bins=15, kde=True)
plt.title('Distribution of Purchase Frequencies')
plt.xlabel('Purchase Frequency')
plt.ylabel('Frequency')
plt.show()

# Measure of Relationship - Scatter plot of browsing frequency vs. shopping satisfaction
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Browsing_Frequency', y='Shopping_Satisfaction', data=df_customer_behavior)
plt.title('Scatter Plot of Browsing Frequency vs. Shopping Satisfaction')
plt.xlabel('Browsing Frequency')
plt.ylabel('Shopping Satisfaction')
plt.show()