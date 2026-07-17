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


# this is the cursor object that will be used to execte the queries

cursor =conn.cursor()
cursor.execute("select FullName,City from customers")
row=cursor.fetchall()
print(row[:5])

for name,city in cursor.fetchall():
    print(name,"live in city",city)

print("type",type(row).__name__, "|How many : ",len(row))
cursor.close()
conn.close()

print("Connected" if conn.is_connected() else "Disconnected")
