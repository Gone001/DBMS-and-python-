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
df = pd.read_sql("SELECT c.City, SUM(o.Amount)  FROM customers c JOIN orders o ON c.CustomerID = o.CustomerID Where Status ='Delivered' GROUP BY c.City ORDER BY SUM(o.Amount) DESC ", conn)
print(df.head())
df=pd.read_sql("SELECT * FROM products",conn)
stock = df.groupby("Category")["StockLeft"].sum().sort_values(ascending=False)

print(stock)
print(stock.head(3))

plt.figure(figsize=(6, 4))

plt.bar(stock.index, stock.values, color="#d97706")

plt.title("Units in Stock by Category")

plt.xlabel("Category")

plt.ylabel("Units")

plt.tight_layout()


plt.savefig("Stockleft_by_category.png")
plt.show()




conn.close()