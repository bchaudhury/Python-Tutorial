import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)