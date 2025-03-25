import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ramv1357"
)

print(mydb)