import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ramv1357",
  database ="pythonmysqlmovieticketsys"
)



def select_all_movies():
    mycursor = mydb.cursor()
    mycursor.execute("Select * from Movies")
    myresult = mycursor.fetchall()

    for movie in myresult:
        print("Id:"+str(movie[0]) +" , title:"+ movie[1])


def select_all_billdoards():
    mycursor = mydb.cursor()
    mycursor.execute("Select * from Billboards inner join Movies "+
                     "on Billboards.Id_Cinema = Movies.Id inner join "+
                     "Cinemas on Billboards.Id_Cinema = Cinemas.Id ")
    myresult = mycursor.fetchall()
    for billboard in myresult:
        print("Id:"+billboard[0])

def select_all_cities():
    mycursor = mydb.cursor()
    mycursor.execute("select * from Cities")
    myresults = mycursor.fetchall()
    for city in myresults:
        print("Id:"+city[0])

def select_all_states():
    mycursor = mydb.cursor()
    mycursor.execute("select * from States")
    myresutls = mycursor.fetchall()
    for state in myresutls:
        print("Id:"+str(state[0])+" name:"+state[1])

def select_billboards_by_cinema():
    pass

def enter_billboard(movieName,cinemaName,hourStart,rate,price):
    idMovie = 0
    idCinema = 0
    idBillboard =0
    mycursor = mydb.cursor()
    mycursor.execute("select * from movies where Title ='" + movieName+"'")
    idMovie = mycursor.fetchone()[0]

    
    mycursor.execute("select * from cinemas where Name = '" +cinemaName+"'")
    idCinema = mycursor.fetchone()[0]

    mycursor.execute("select count(id) from billboards")
    idBillboard = mycursor.fetchone()[0] + 1
    
    insertQuery = "insert into billboards (Id,Id_Movie,Id_Cinema,Hour_Start,Rate,Price) values(%s,%s,%s,%s,%s,%s)"

    
    val =(idBillboard,idMovie,idCinema,hourStart,rate,price)
    mycursor.execute(insertQuery,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
