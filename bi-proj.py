import pandas as pd
from scipy.stats import zscore
import numpy as np


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