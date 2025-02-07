import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhas@123abc#"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")