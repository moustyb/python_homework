import sqlite3
import pandas as pd

# Connect to the lesson database 
# (Using ../ to go up one folder from assignment9 to find the db folder)
conn = sqlite3.connect("../db/lesson.db")

# ==========================================
# Task 5: Read Data into a DataFrame
# ==========================================

# 1. Retrieve data from a JOIN of line_items and products tables
query = """
SELECT 
    li.line_item_id, 
    li.quantity, 
    p.product_id, 
    p.name AS product_name, 
    p.price
FROM line_items AS li
JOIN products AS p ON li.product_id = p.product_id
"""

# Read the SQL query results directly into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print the first 5 lines of the resulting DataFrame
print("--- First 5 lines of initial DataFrame ---")
print(df.head())
print("\n")

# 2. Add a column called "total" (quantity times price)
df['total'] = df['quantity'] * df['price']

# Print out the first 5 lines to verify the new column
print("--- First 5 lines after adding 'total' column ---")
print(df.head())
print("\n")

# 3. Group by product_id and aggregate
# Use 'count' for line_item_id, 'sum' for total, 'first' for product_name
summary_df = df.groupby('product_id').agg(
    order_count=('line_item_id', 'count'),
    total_revenue=('total', 'sum'),
    product_name=('product_name', 'first')
).reset_index()

# Print out the first 5 lines of the grouped DataFrame
print("--- First 5 lines of grouped DataFrame ---")
print(summary_df.head())
print("\n")

# 4. Sort the DataFrame by the product_name column
summary_df = summary_df.sort_values(by='product_name')

# 5. Write this DataFrame to a file order_summary.csv in the assignment9 directory
# index=False prevents pandas from writing row numbers into the CSV
summary_df.to_csv('order_summary.csv', index=False)
print("Successfully wrote summary data to order_summary.csv")

# Close the database connection
conn.close()
