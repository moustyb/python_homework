import sqlite3

# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders.

# Open the database
conn = sqlite3.connect("db/lesson.db")
cursor = conn.cursor()

# The SQL statement
query = """
SELECT 
    o.order_id, 
    SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

# Issue the SQL statement
cursor.execute(query)
results = cursor.fetchall()

# Print out the result
print("Task 1: Total price of the first 5 orders")
for row in results:
    print(f"Order ID: {row[0]}, Total Price: {row[1]}")

# Close the database
conn.close()
