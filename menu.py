import sql_connection



def mostrar_menu():
    print("\n\033[35mSystem for cinemas administration\033[0m \n")
    print("\033[34mPlease select one of the options\033[0m \n")
    print("Options \n")
    print("A) Billboards \n")
    print("B) Cinemas \n")
    print("C) Cities \n")
    print("D) Movies \n")
    print("E) States \n")
    print("F) Tickets \n")
    print("G) Exit \n")
    opccion = input()

    return opccion



def menu_billboards():
    print("\n Billboard Menu \n")
    print("A) Check all the billboards \n")
    print("B) Check billboards by cinema \n")
    print("C) Enter new billboard \n")
    print("D) Update billboard \n")
    print("D) Delete billboard \n ")

    option = input()

    if(option == "A"):
        sql_connection.select_all_billdoards()
    elif (option == "B"):
        cinemaName= input("Write the name of the cinema:")
        print("Billboard of cinema:" + str(cinemaName))
        sql_connection.select_billboards_by_cinema(cinemaName)
    elif (option == "C"):
        movieName = input("Write the name of the movie:")
        cinemaName = input("Write the name of the cinema:")
        hourStart = input("Write the hour it starts:")
        rate= input("Write the rate of the movie:")
        price= float(input("Wtrite the price of the tickets:"))
        sql_connection.enter_billboard(movieName,cinemaName,hourStart,rate,price)





def menu_cinemas():
    print("Cinemas menu")

def menu_cities():
    print("Cities menu")

def menu_movies():
    print("Movies menu")

def menu_states():
    print("\n States Menu \n")
    print("A) Check all the states \n")
    print("B) Enter new state \n")
    print("C) Update state \n")
    print("D) Delete state \n ")

    option = input()

    if(option == "A"):
        sql_connection.select_all_states()


def menu_tickets():
    print("Menu tickets")



valMostrarMenu = True

while valMostrarMenu:
    opccionUsuario = mostrar_menu()

    if opccionUsuario == 'A' or opccionUsuario == 'a':
        menu_billboards()
    elif opccionUsuario == 'B' or opccionUsuario == 'b':
        menu_cinemas()
    elif opccionUsuario == 'C' or opccionUsuario == 'c':
        menu_cities()
    elif opccionUsuario == 'D' or opccionUsuario == 'd':
        menu_movies()
    elif opccionUsuario == 'E' or opccionUsuario == 'e':
        menu_states()
    elif opccionUsuario == 'F' or opccionUsuario == 'f':
        menu_tickets()
    elif opccionUsuario == "G" or opccionUsuario == "g":
        print("Good bye")
        valMostrarMenu = False
    else:
        print("Choose a valid option")