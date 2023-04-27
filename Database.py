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
        Downloads = str(Path.home())+"\Downloads"
        db.execute('INSERT INTO Folders(id,Name,Path)'
                   'VALUES(?,?,?)',(0,"Music",Downloads))

        db.execute("CREATE TABLE Recent(id integer,Name text,Path text);")
        db.execute("CREATE TABLE Favourites(id integer,Name text,Path text);")

        db.execute("CREATE TABLE Storage(id integer,Path text);")
        db.execute('INSERT INTO Storage(id,Path)'
                   'VALUES(?,?)',(0,"Any"))
        db.commit() 


    def get_folder():
        folder = db.execute("SELECT* FROM Folders;")
        for i in folder:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Folders.append(value)
            print(value)

    def get_recent():
        recent = db.execute("SELECT* FROM Recent;")
        for i in recent:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Recent.append(value)

    def get_favourites():
        favourites = db.execute("SELECT* FROM Favourites;")
        for i in favourites:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Favourites.append(value)

    def close():
        db.close()

Database.get_folder()
Database.get_recent()
Database.get_favourites()
    