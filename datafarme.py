import os
import pandas as pd
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("database_host"),
    user=os.getenv("user"),
    password=os.getenv("db_password"),
    database=os.getenv("db_name")
)

print("Successfully Connected" if conn.is_connected() else "Connection Failed")

df = pd.read_sql(
    "SELECT * FROM customers",
    conn
)

print(df.head())

conn.close()