import sqlite3
import os

class Database():
    if "App.db" in os.listdir():
        db = sqlite3.connect("App.db")
    else:
        db = sqlite3.connect("App.db")
        db.execute("CREATE TABLE Folders(Name text,Path text);")
        db.execute("CREATE TABLE Recent(Name text,Path text);")
        db.execute("CREATE TABLE Favourites(Name text,Path text);")
        db.execute("CREATE TABLE Storage(Path text);")
        db.execute("INSERT INTO Storage(Path) / VALUES(""Any"");")

    # db = sqlite3.connect("App.db")