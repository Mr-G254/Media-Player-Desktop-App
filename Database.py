import sqlite3
import os
from pathlib import Path
from Extra import*

class Database():
    global db
    if "App.db" in os.listdir():
        db = sqlite3.connect("App.db")
    else:
        db = sqlite3.connect("App.db")
        db.execute("CREATE TABLE Folders(id integer,Name text,Path text)")
        Music = str(Path.home())+"\Music"
        db.execute('INSERT INTO Folders(id,Name,Path) VALUES(?,?,?)',(0,"Music",Music))

        db.execute("CREATE TABLE Recent(id integer,Name text,Path text);")
        db.execute("CREATE TABLE Favourites(id integer,Name text,Path text);")

        db.execute("CREATE TABLE Storage(id integer,Path text);")
        db.execute('INSERT INTO Storage(id,Path) VALUES(?,?)',(0,"Always ask"))
        
        db.commit() 

    def get_folder():
        folder = db.execute('SELECT* FROM Folders;')
        for i in folder:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Folders.append(value)

    def get_recent():
        recent = db.execute('SELECT* FROM Recent;')
        for i in recent:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Recent.append(value)

    def get_favourites():
        favourites = db.execute('SELECT* FROM Favourites;')
        for i in favourites:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Favourites.append(value)

    def get_location():
        location = db.execute('SELECT* FROM Storage;')
        for i in location:
            value = i
        return value[1]
    
    def update_location(location):
        update = "UPDATE Storage set Path = '"+ location +"' WHERE id = 0"
        db.execute(update)
        db.commit()

    def close():
        db.close()

Database.get_folder()
Database.get_recent()
Database.get_favourites()
    