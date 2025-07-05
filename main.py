import pandas as pd
import numpy as np
import os
from datetime import datetime

# Create the output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

#  1: Load raw sales data from CSV
df = pd.read_csv('data/sales_data.csv')
print("Raw Data:\n", df)


#  1.5: Check for duplicate 'Order ID's and print them
duplicate_orders = df[df.duplicated(subset=['Order ID'], keep=False)]
if not duplicate_orders.empty:
    print("\n ⚠️ Duplicate Order IDs Found:\n", duplicate_orders)
else:
    print("\n ✅ No Duplicate Order IDs found.")

# Drop duplicate orders, keeping only the first occurrence
df = df.drop_duplicates(subset=['Order ID'], keep='first')


#  2: Handle missing values
# Fill missing 'Quantity' and 'Price' values with their respective column means
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
df['Price'] = df['Price'].fillna(df['Price'].mean())

# Fill missing 'Order ID' values with the string 'NaN'
df['Order ID'] = df['Order ID'].fillna('NaN')


#  3: Convert 'Date' to a consistent YYYY-MM-DD format
def parse_dates(date_str):
    for fmt in ('%Y/%m/%d', '%d-%m-%Y', '%Y-%m-%d'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    return pd.NaT  # Return Not-a-Time if no format matches

df['Date'] = df['Date'].apply(parse_dates)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')  # Format all dates as strings in YYYY-MM-DD

#  4: Calculate total sales for each order
df['Total Sales'] = df['Quantity'] * df['Price']

# Optional: Validate total sales using NumPy for comparison
total_sales_np = np.array(df['Quantity']) * np.array(df['Price'])
df['Total Sales (numpy)'] = total_sales_np

#  5: Aggregate total sales by region
sales_by_region = df.groupby('Region')['Total Sales'].sum().reset_index()

#  6: Export cleaned data and summary to CSV files
df.to_csv('output/clean_sales_data.csv', index=False)
sales_by_region.to_csv('output/sales_by_region.csv', index=False)

# Display outputs
print("\nCleaned Data:\n", df)
print("\nSales by Region:\n", sales_by_region)
