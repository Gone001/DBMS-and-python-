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

conn.close()

print("Connected" if conn.is_connected() else "Disconnected")
