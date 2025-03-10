import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Insert some data
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
connection.commit()

# Query the data
cursor.execute("SELECT * FROM users")

# Fetch rows one by one
row = cursor.fetchone()
while row:
    print(row)  # Outputs each row as a tuple, e.g., (1, 'Alice')
    row = cursor.fetchone()

# Clean up
cursor.close()
connection.close()
