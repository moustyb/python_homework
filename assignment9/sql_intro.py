import sqlite3

def main():
    conn = None
    try:
        # Connect to the database. If '../db/magazines.db' doesn't exist, SQLite creates it.
        conn = sqlite3.connect("../db/magazines.db")
        print("✅ Successfully connected to magazines.db")
        
        # NOTE: As you proceed to Tasks 2-4, every SQL statement (CREATE, INSERT, SELECT, etc.)
        # must be wrapped in its own try/except block as required by the assignment.
        # Example structure for later:
        # try:
        #     conn.execute("YOUR SQL HERE")
        # except sqlite3.IntegrityError as e:
        #     print(f"Constraint error: {e}")
        # except sqlite3.Error as e:
        #     print(f"SQL error: {e}")

    except sqlite3.Error as e:
        print(f"❌ SQLite error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        # Explicitly close the connection as requested
        if conn:
            conn.close()
            print("🔌 Database connection closed.")

if __name__ == "__main__":
    main()
