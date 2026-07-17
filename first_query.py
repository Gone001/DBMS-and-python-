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
'''city="jammu"
cursor.execute(
    "SELECT FullName FROM customers WHERE City = %s",
    (city,)
)

rows=cursor.fetchall()
for row in rows:
    print(row)
print(len(rows),"customers in ",city)
'''
'''
cursor.execute(
    "SELECT o.CustomerID, c.FullName ,o.Status FROM orders o JOIN customers c ON o.CustomerID = c.CustomerID WHERE o.OrderID = 1017; "    
)
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
'''

order=int(input("Enter the order ID : ") or 1017)
'''
cursor.execute(
    "SELECT o.CustomerID, c.FullName ,o.Status FROM orders o JOIN customers c ON o.CustomerID = c.CustomerID WHERE o.OrderID = %s ",
    (order,) 
)
'''
query = input("Enter SQL Query: ")
if not query:
    query = """
    SELECT o.CustomerID, c.FullName, o.Status
    FROM orders o
    JOIN customers c
    ON o.CustomerID = c.CustomerID
    WHERE o.OrderID = %s
    """
cursor.execute(query ,(order,))
rows=cursor.fetchall()

if len(rows) <=0:
        print(f"No Record for order : {order}")
else: 
    for row in rows:
      print(row)

   
cursor.close()
conn.close()
