import sqlite3
import os
from pathlib import Path
from Extra import*
from tkinter import messagebox
from MusicPage import*
from VideoPage import*

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
        db.execute('INSERT INTO Storage(Path) VALUES(?)',["Always ask"])
        
        db.commit() 

    def get_folder():
        Extra.Folders.clear()
        folder = db.execute('SELECT* FROM Folders;')
        for i in folder:
            value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
            Extra.Folders.append(value)

        Extra.Folders.sort()

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
        update = "UPDATE Storage set Path = '"+ location +"' WHERE id = 1"
        db.execute(update)
        db.commit()
    
    def del_folder(Event,folder_id,folder_name,folder_class):
        prompt = messagebox.askyesno("Delete Folder",f"Are you sure you want to delete {folder_name} folder")
        if prompt:
            Extra.notify(f"Deleting {folder_name} from Folders...")
            db.execute(f"DELETE FROM Folders WHERE id={folder_id}")
            db.commit()

            Database.get_folder()
            folder_class.load_folders()
            Database.load_songs()
            Extra.undo_noyify()

    def add_folder(folder_name,folder_path):
        Extra.notify(f"Adding {folder_name} to Folders...")
        db.execute("INSERT INTO Folders(Name,Path) VALUES(?,?)",(folder_name,folder_path))
        db.commit()

        Database.get_folder()
        Database.load_songs()
        Extra.undo_noyify()

    def close():
        db.close()

    def load_songs():
        Extra.All_songs.clear()
        Extra.All_videos.clear()

        for i in Extra.Folders:
            values = i.split("=")
            for x in os.listdir(values[2]):
                if x.endswith(".mp3"):
                    Extra.All_songs.append(f"{x}={values[2]}\{x}")
                
                if x.endswith(".mp4"):
                    Extra.All_videos.append(f"{x}={values[2]}\{x}")
        
        Extra.All_songs.sort()
        Extra.All_videos.sort()

        try:
            Music.show_all_songs()
        except:
                pass
        
        Video.get_thumbnails()
        try:
            Video.show_all_videos()
        except:
                pass

Database.get_folder()
Database.get_recent()
Database.get_favourites()
Database.load_songs()
    