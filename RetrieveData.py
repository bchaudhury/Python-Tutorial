import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE address ='Highway 21'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)