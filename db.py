import pandas as pd
import sqlite3

# Step 1: Read the CSV file
df = pd.read_csv("amazon.csv")

# Step 2: Create the database
conn = sqlite3.connect("amazon.db")

# Step 3: Save the DataFrame as a table in the database
df.to_sql("amazon_products", conn, if_exists="replace", index=False)

# Step 4: Close the connection
conn.close()

print("amazon.db created successfully.")
