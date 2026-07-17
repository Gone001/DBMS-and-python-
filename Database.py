import mysql.connector
print(mysql.connector.__version__)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gone@123",
    database="quickcart"
)

print("Connected Successfully")
cursor = conn.cursor()
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

print(rows)