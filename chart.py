import os
import pandas as pd
import matplotlib.pyplot as plt
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
df = pd.read_sql("SELECT Category, StockLeft FROM products", conn)
stock = df.groupby("Category")["StockLeft"].sum().sort_values(ascending=False)

print(stock)

plt.figure(figsize=(6, 4))

plt.bar(stock.index, stock.values, color="#d97706")

plt.title("Units in Stock by Category")

plt.xlabel("Category")

plt.ylabel("Units")

plt.tight_layout()

plt.savefig("step09_stock.png")

plt.show()



conn.close()