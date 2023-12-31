import pandas as pd
from scipy.stats import zscore
import numpy as np
import scipy.stats as stats
from scipy.stats import kruskal
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity


# Define the file paths for the datasets
file_paths = {
    'order_items': 'data/olist_order_items_dataset.csv',
    'products': 'data/olist_products_dataset.csv',
    'customers': 'data/olist_customers_dataset.csv',
    'order-reviews': 'data/olist_order_reviews_dataset.csv',
    'orders': 'data/olist_orders_dataset.csv',
    'order-payments': 'data/olist_order_payments_dataset.csv',

}

# Function to load datasets
def load_datasets(file_paths):
    data = {}
    for name, path in file_paths.items():
        data[name] = pd.read_csv(path)
    return data

# Load the datasets
loaded_data = load_datasets(file_paths)

# Accessing individual DataFrames
order_items_df = loaded_data['order_items']
products_df = loaded_data['products']
customers_df = loaded_data['customers']
order_reviews_df = loaded_data['order-reviews']
orders_df = loaded_data['orders']
order_payments_df = loaded_data['order-payments']

# Display basic info about the loaded datasets
for name, df in loaded_data.items():
    print(f"--- {name} ---")
    print(df.head())
    print(df.info())
    print("---------------")


# Data preprocessing and cleaning
for name, df in loaded_data.items():
    # Handle missing values
    if df.isnull().sum().any():
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        object_columns = df.select_dtypes(include=['object']).columns
        df[object_columns] = df[object_columns].fillna(df[object_columns].mode().iloc[0])

    # Remove duplicates
    df.drop_duplicates(inplace=True)


# Outlier detection and removal using Z-score
for name, df in loaded_data.items():
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        df = df[(np.abs(zscore(df[col])) < 3)]

# Normalization
for name, df in loaded_data.items():
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())


# Merge 'order_items' and 'orders' on 'order_id'
merged_df = pd.merge(loaded_data['order_items'], loaded_data['orders'], on='order_id')

# Merge the resulting DataFrame with 'customers' on 'customer_id'
final_df = pd.merge(merged_df, loaded_data['customers'], on='customer_id')

# Feature engineering
order_items_df['total_cost'] = order_items_df['price'] + order_items_df['freight_value']


# Encoding categorical variables
for name, df in loaded_data.items():
    object_columns = df.select_dtypes(include=['object']).columns
    for col in object_columns:
        df[col] = df[col].astype('category').cat.codes

# Merge 'order_items' and 'orders' on 'order_id'
merged_df = pd.merge(loaded_data['order_items'], loaded_data['orders'], on='order_id')

# Merge the resulting DataFrame with 'customers' on 'customer_id'
final_df = pd.merge(merged_df, loaded_data['customers'], on='customer_id')


# Define a threshold for the minimum number of purchases
min_product_purchases = 10
min_customer_purchases = 10

# Filter out products that have been bought less than min_product_purchases times
product_counts = final_df['product_id'].value_counts()
popular_products = product_counts[product_counts >= min_product_purchases].index
final_df = final_df[final_df['product_id'].isin(popular_products)]

# Filter out customers who have bought less than min_customer_purchases times
customer_counts = final_df['customer_unique_id'].value_counts()
active_customers = customer_counts[customer_counts >= min_customer_purchases].index
final_df = final_df[final_df['customer_unique_id'].isin(active_customers)]

# Create user-item matrix
user_item_matrix = final_df.pivot_table(index='customer_unique_id', columns='product_id', values='total_cost')

# Fill missing values with 0
user_item_matrix.fillna(0, inplace=True)

# Print the user-item matrix
print(user_item_matrix)



# Fill missing values with 0
user_item_matrix.fillna(0, inplace=True)

# Print the user-item matrix
print(user_item_matrix)

# Print the first 5 rows of each DataFrame
for name, df in loaded_data.items():
    print(f"--- First 5 rows of {name} ---")
    print(df.head())
    print("\n")

# Print the summary statistics of each DataFrame
for name, df in loaded_data.items():
    print(f"--- Summary statistics of {name} ---")
    print(df.describe())
    print("\n")

# Print the number of missing values in each DataFrame
for name, df in loaded_data.items():
    print(f"--- Missing values in {name} ---")
    print(df.isnull().sum())
    print("\n")

# Frequency: count the number of purchases for each product
product_frequency = final_df['product_id'].value_counts()

# Central tendency: calculate the mean and median total cost
mean_cost = final_df['total_cost'].mean()
median_cost = final_df['total_cost'].median()

# Distribution: calculate the standard deviation of the total cost
std_dev_cost = final_df['total_cost'].std()

# Relationship: calculate the correlation between total cost and product_id
# Note: this requires product_id to be a numeric type. If it's a categorical type, you'll need to convert it to numeric.
correlation = final_df['total_cost'].corr(final_df['product_id'])

print(f"Product Frequency:\n{product_frequency}\n")
print(f"Mean Total Cost: {mean_cost}")
print(f"Median Total Cost: {median_cost}")
print(f"Standard Deviation of Total Cost: {std_dev_cost}")
print(f"Correlation between Total Cost and Product ID: {correlation}")



# Select specific product_ids
product_ids = [1633, 27232, 6138]  # replace with your chosen product_ids

# Select the total cost data for these products
product1 = final_df[final_df['product_id'] == product_ids[0]]['total_cost']
product2 = final_df[final_df['product_id'] == product_ids[1]]['total_cost']
product3 = final_df[final_df['product_id'] == product_ids[2]]['total_cost']

# Perform ANOVA
f_val, p_val = stats.f_oneway(product1, product2, product3)

print(f"F-value: {f_val}")
print(f"P-value: {p_val}")


# Create a contingency table
contingency_table = pd.crosstab(final_df['product_id'], final_df['customer_unique_id'])

# Perform Chi-square test
chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p_val}")


# Correlation with price
correlation_price = final_df['total_cost'].corr(final_df['price'])
print(f"Correlation with Price: {correlation_price}")

# Correlation with freight_value
correlation_freight = final_df['total_cost'].corr(final_df['freight_value'])
print(f"Correlation with Freight Value: {correlation_freight}")


# Perform Kruskal-Wallis H test
h_val, p_val = stats.kruskal(product1, product2, product3)

print(f"H-value: {h_val}")
print(f"P-value: {p_val}")


# Prepare data
data = pd.concat([product1, product2, product3])
groups = ['product1']*len(product1) + ['product2']*len(product2) + ['product3']*len(product3)
df = pd.DataFrame({'values': data, 'groups': groups})

# Perform Dunn's test
posthoc = sp.posthoc_dunn(df, val_col='values', group_col='groups', p_adjust='bonferroni')

print(posthoc)

# Histogram for 'total_cost'
plt.figure(figsize=(10, 6))
plt.hist(final_df['total_cost'], bins=30, edgecolor='black')
plt.title('Total Cost Distribution')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.show()

# Boxplot for 'total_cost'
plt.figure(figsize=(10, 6))
sns.boxplot(final_df['total_cost'])
plt.title('Total Cost Boxplot')
plt.show()

# Scatter plot for 'total_cost' vs 'price'
plt.figure(figsize=(10, 6))
plt.scatter(final_df['total_cost'], final_df['price'])
plt.title('Total Cost vs Price')
plt.xlabel('Total Cost')
plt.ylabel('Price')
plt.show()

# Scatter plot for 'total_cost' vs 'freight_value'
plt.figure(figsize=(10, 6))
plt.scatter(final_df['total_cost'], final_df['freight_value'])
plt.title('Total Cost vs Freight Value')
plt.xlabel('Total Cost')
plt.ylabel('Freight Value')
plt.show()

# Heatmap for the correlation matrix of the DataFrame
plt.figure(figsize=(10, 6))
sns.heatmap(final_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()


print(final_df.columns)



# Check for missing values
missing_values = final_df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Impute missing values
for column in final_df.columns:
    if final_df[column].dtype == 'object':  # Categorical data
        final_df[column] = final_df[column].fillna(final_df[column].mode()[0])
    else:  # Numerical data
        final_df[column] = final_df[column].fillna(final_df[column].median())

# Confirm that there are no more missing values
print("\nMissing values after imputation:\n", final_df.isnull().sum())

# Data transformation
numerical_cols = final_df.select_dtypes(include=[np.number]).columns
final_df[numerical_cols] = final_df[numerical_cols].apply(zscore)

# Print the first 5 rows of the DataFrame to confirm transformations
print("\nFirst 5 rows after transformations:\n", final_df.head())


# Create user-item interaction matrix
interaction_matrix = final_df.pivot_table(index='customer_id', columns='product_id', values='order_item_id', fill_value=0, aggfunc='count')


# Print unique customer IDs
print(interaction_matrix.index.unique())



# Calculate item-item similarity matrix
item_similarity = cosine_similarity(interaction_matrix.T)
item_similarity = pd.DataFrame(item_similarity, index=interaction_matrix.columns, columns=interaction_matrix.columns)

# Function to get the most similar items
def get_similar_items(product_id, n=5):
    similar_items = item_similarity[product_id].sort_values(ascending=False)[:n+1]
    similar_items = similar_items.index[similar_items.index != product_id]  # Exclude the item itself
    return similar_items

# Function to recommend items for a user
def recommend_items(user_id, n=5):
    if user_id not in interaction_matrix.index:
        print(f"No data available for user ID: {user_id}")
        return []
    user_items = interaction_matrix.loc[user_id]
    not_interacted_items = user_items[user_items == 0].index
    item_scores = item_similarity[not_interacted_items].sum(axis=1)
    recommended_items = item_scores.nlargest(n)
    return recommended_items.index


# Get recommendations for a specific user
recommended_items = recommend_items(-1.9176302812675063)
print(f"Recommended items for user '-1.9176302812675063': {recommended_items}")



