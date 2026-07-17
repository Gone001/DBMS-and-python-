import os 
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
conn=mysql.connector.connect(
   host = os.getenv("database_host"),
   user = os.getenv("user"),
   password = os.getenv("db_password"),
   database = os.getenv("db_name")
)  

print("Successfully Connected" if conn.is_connected() else "Connection failed")

cursor =conn.cursor()
'''
query = input("Enter SQL Query: ")
if not query:
    """insert into orders(OrderID , CustomerID , ProductID ,Quantity ,Amount , OrderDate ,Status) values(1021,15,103,8,1000,'2026-06-01','Pending'
    )

    """
'''
product_id = 5
new_price = 899
query = input("Enter SQL Query: ")
if not query:
    """
     UPDATE products SET Price = %s WHERE ProductID = %s
    """
cursor.execute(query,(new_price, product_id)
)

conn.commit()

print(f"{cursor.rowcount} row(s) updated.")
cursor.execute("SELECT * FROM products")
rows=cursor.fetchall()
if len(rows) <=0:
        print(f"No Record for order :")
else: 
    for pid,name,category,price,stock in rows:
      print(pid,name,category,price,stock)

