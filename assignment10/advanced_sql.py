import sqlite3

# Connect to the database
conn = sqlite3.connect("db/lesson.db")
cursor = conn.cursor()

# Enable foreign keys as required for Task 3
conn.execute("PRAGMA foreign_keys = 1")

# ==========================================
# Task 1: Complex JOINs with Aggregation
# ==========================================
# Find the total price of each of the first 5 orders.
query_task1 = """
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

cursor.execute(query_task1)
results1 = cursor.fetchall()

print("--- Task 1: Total price of the first 5 orders ---")
for row in results1:
    print(f"Order ID: {row[0]}, Total Price: {row[1]}")
print("\n")


# ==========================================
# Task 2: Understanding Subqueries
# ==========================================
# For each customer, find the average price of their orders.
query_task2 = """
SELECT 
    c.name AS customer_name,
    AVG(subq.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS subq ON c.customer_id = subq.customer_id_b
GROUP BY c.customer_id, c.name;
"""

cursor.execute(query_task2)
results2 = cursor.fetchall()

print("--- Task 2: Average order price per customer ---")
for row in results2:
    # Handle cases where a customer might have no orders (average will be None)
    avg_price = row[1] if row[1] is not None else 0.0
    print(f"Customer: {row[0]}, Average Total Price: {avg_price}")
print("\n")


# ==========================================
# Task 3: An Insert Transaction Based on Data
# ==========================================
# Create a new order for "Perez and Sons" by "Miranda Harris" 
# for 10 of each of the 5 least expensive products.

print("--- Task 3: New Order Transaction ---")

# 1. Retrieve customer_id
cursor.execute("SELECT customer_id FROM customers WHERE name = 'Perez and Sons'")
customer_id = cursor.fetchone()[0]

# 2. Retrieve employee_id
cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
employee_id = cursor.fetchone()[0]

# 3. Retrieve product_ids of the 5 least expensive products
cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
product_ids = [row[0] for row in cursor.fetchall()]

# 4. Create the order record and get the new order_id using RETURNING
# Note: 'order_date' is included as it is standard in this schema. 
cursor.execute("""
    INSERT INTO orders (customer_id, employee_id, order_date) 
    VALUES (?, ?, date('now')) 
    RETURNING order_id
""", (customer_id, employee_id))

new_order_id = cursor.fetchone()[0]

# 5. Create the 5 line_item records within the same transaction
for pid in product_ids:
    cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, 10)
    """, (new_order_id, pid))

# 6. Commit the transaction to save all changes
conn.commit()
print(f"Successfully created Order ID: {new_order_id}")

# 7. Print out the list of line_item_ids, quantity, and product name for the new order
cursor.execute("""
    SELECT li.line_item_id, li.quantity, p.name
    FROM line_items AS li
    JOIN products AS p ON li.product_id = p.product_id
    WHERE li.order_id = ?
""", (new_order_id,))

task3_results = cursor.fetchall()
for row in task3_results:
    print(f"Line Item ID: {row[0]}, Quantity: {row[1]}, Product: {row[2]}")
print("\n")


# ==========================================
# Task 4: Aggregation with HAVING
# ==========================================
# Find all employees associated with more than 5 orders.
query_task4 = """
SELECT 
    e.employee_id, 
    e.first_name, 
    e.last_name, 
    COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query_task4)
results4 = cursor.fetchall()

print("--- Task 4: Employees with more than 5 orders ---")
for row in results4:
    print(f"Employee ID: {row[0]}, Name: {row[1]} {row[2]}, Order Count: {row[3]}")
print("\n")

# Close the database connection
conn.close()
print("Database connection closed.")
