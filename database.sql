create database if not exists  PythonMySqlMovieTicketSys;
use PythonMySqlMovieTicketSys;
create table if not exists Movies (Id INT, Title TEXT, Director TEXT,Year TEXT, Studio TEXT, constraint pk_movie primary key (Id)); 
create table if not exists States (Id INT, Name TEXT, constraint primary key pk_state (ID) );
create table if not exists Cities (Id INT, Id_State INT,Name TEXT, constraint primary key pk_city (Id), 
constraint foreign key fk_city_state (Id) references States(Id) );
create table if not exists Cinemas (Id INT, Name TEXT,Open_Hour INT, Close_hour INT,Id_City INT,
constraint primary key pk_cinema (Id),
constraint foreign key fk_cinema_city (Id_City) references Cities(Id));
create table if not exists Billboards (Id INT,Id_Movie INT,Id_Cinema INT, Hour_Start TEXT, Rate TEXT,Price FLOAT,
constraint primary key pk_billboard (Id),
constraint foreign key fk_billboard_movie (Id_Movie) references Movies(Id),
constraint foreign key fk_billboard_cinema (Id_Cinema) references Cinemas(Id));
create table if not exists Tickets (Id INT,Number_Tickets INT, Id_Billboard INT, Total_Price FLOAT,
constraint primary key pk_ticket (Id),
constraint foreign key fk_tickets_billboard (Id_Billboard) references Billboards(Id));