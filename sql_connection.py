import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ramv1357",
  database ="pythonmysqlmovieticketsys"
)



def select_movies():
    mycursor = mydb.cursor()
    mycursor.execute("Select * from Movies")
    myresult = mycursor.fetchall()

    for movie in myresult:
        print("Id:"+str(movie[0]) +" , title:"+ movie[1])


select_movies()