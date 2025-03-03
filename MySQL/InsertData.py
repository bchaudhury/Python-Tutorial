import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO supplier (name, address, mobile) VALUES (%s, %s, %s)"
val = ("Zomato", "India", 9999900000)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")