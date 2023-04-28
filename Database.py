import sqlite3
import os
from pathlib import Path
from Extra import*
from tkinter import messagebox

class Database():
    global db
    if "App.db" in os.listdir():
        db = sqlite3.connect("App.db")
    else:
        db = sqlite3.connect("App.db")

        db.execute("CREATE TABLE Folders(id integer PRIMARY KEY,Name text,Path text)")

        Music = str(Path.home())+"\Music"
        Videos = str(Path.home())+"\Videos"

        db.execute('INSERT INTO Folders(Name,Path) VALUES(?,?)',("Music",Music))
        db.execute('INSERT INTO Folders(Name,Path) VALUES(?,?)',("Videos",Videos))

        db.execute("CREATE TABLE Recent(id integer PRIMARY KEY,Name text,Path text);")
        db.execute("CREATE TABLE Favourites(id integer,Name text,Path text);")

        db.execute("CREATE TABLE Storage(id integer PRIMARY KEY,Path text);")
        db.execute('INSERT INTO Storage(Path) VALUES(?)',("Always ask"))
        
        db.commit() 

    def get_folder():
        Extra.Folders.clear()
        folder = db.execute('SELECT* FROM Folders;')
        for i in folder:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Folders.append(value)

    def get_recent():
        Extra.Recent.clear()
        recent = db.execute('SELECT* FROM Recent;')
        for i in recent:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Recent.append(value)

    def get_favourites():
        Extra.Recent.clear()
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
    
    def del_folder(folder_id,folder_name):
        prompt = messagebox.askyesno("Delete Folder",f"Are you sure you want to delete {folder_name} folder")
        if prompt:
            db.execute(f"DELETE FROM Folders WHERE id={folder_id}")
            db.commit()

            Database.get_folder()

    def close():
        db.close()

Database.get_folder()
Database.get_recent()
Database.get_favourites()
    