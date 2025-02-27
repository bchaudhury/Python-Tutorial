import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE supplier ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")