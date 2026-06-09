import sqlite3
import os

# ==========================================
# Task 1: Create a New SQLite Database
# ==========================================
db_path = "../db/magazines.db"

# Ensure the db directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

try:
    conn = sqlite3.connect(db_path)
    print("Successfully connected to magazines.db")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit()

# ==========================================
# Task 2: Define Database Structure
# ==========================================
try:
    cursor = conn.cursor()
    
    # Create publishers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)
    
    # Create magazines table (One-to-many with publishers)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        )
    """)
    
    # Create subscribers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)
    
    # Create subscriptions table (Many-to-many join table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        )
    """)
    
    conn.commit()
    print("Tables created successfully.")
except sqlite3.Error as e:
    print(f"Error creating tables: {e}")

# ==========================================
# Task 3: Populate Tables with Data
# ==========================================
# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = 1")

def add_publisher(name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        # Publisher already exists, fetch its ID
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Error adding publisher: {e}")
        return None

def add_magazine(name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        cursor.execute("SELECT id FROM magazines WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Error adding magazine: {e}")
        return None

def add_subscriber(name, address):
    try:
        # Check for duplication of both name and address
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        existing = cursor.fetchone()
        if existing:
            return existing[0] # Return existing ID to prevent duplication
        
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")
        return None

def add_subscription(subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) 
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")
        return None

# Populate with at least 3 entries each
print("\nPopulating tables...")
pub1 = add_publisher("Tech Media Corp")
pub2 = add_publisher("Lifestyle Publishing")
pub3 = add_publisher("Science Weekly Inc")

mag1 = add_magazine("Python Monthly", pub1)
mag2 = add_magazine("Home & Garden", pub2)
mag3 = add_magazine("Space Discoveries", pub3)

sub1 = add_subscriber("Alice Smith", "123 Main St, NY")
sub2 = add_subscriber("Bob Jones", "456 Oak Ave, CA")
sub3 = add_subscriber("Alice Smith", "123 Main St, NY") # Duplicate test (should be ignored)
sub4 = add_subscriber("Charlie Brown", "789 Pine Rd, TX")

add_subscription(sub1, mag1, "2027-12-31")
add_subscription(sub2, mag2, "2026-06-30")
add_subscription(sub4, mag3, "2028-01-15")
add_subscription(sub1, mag3, "2027-12-31") # Alice gets a second magazine

print("Data populated successfully (duplicates prevented).")

# ==========================================
# Task 4: Write SQL Queries
# ==========================================
print("\n--- Task 4 Queries ---")

# Query 1: Retrieve all information from the subscribers table
print("\n1. All Subscribers:")
try:
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Query error: {e}")

# Query 2: Retrieve all magazines sorted by name
print("\n2. All Magazines (Sorted by Name):")
try:
    cursor.execute("SELECT * FROM magazines ORDER BY name ASC")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Query error: {e}")

# Query 3: Find magazines for a particular publisher (requires JOIN)
publisher_to_find = "Tech Media Corp"
print(f"\n3. Magazines published by '{publisher_to_find}':")
try:
    cursor.execute("""
        SELECT magazines.name 
        FROM magazines 
        JOIN publishers ON magazines.publisher_id = publishers.id 
        WHERE publishers.name = ?
    """, (publisher_to_find,))
    for row in cursor.fetchall():
        print(row[0])
except sqlite3.Error as e:
    print(f"Query error: {e}")

# Close the connection
conn.close()
print("\nDatabase connection closed.")
