import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, mobile) VALUES (%s, %s, %s)"
val = ("Bhaskar", "50 Lake Gardens", 8)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")