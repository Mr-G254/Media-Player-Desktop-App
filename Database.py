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
        db.execute("CREATE TABLE Favourites(id integer PRIMARY KEY,Name text,Path text);")
        db.execute("CREATE TABLE Playlist(id integer PRIMARY KEY,Name text,Path text);")

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
            value = str(i[1]) + "=" + str(i[2])
            Extra.Recent.append(value)

    def upload_recent():
        db.execute("DROP TABLE Recent;")
        db.execute("CREATE TABLE Recent(id integer PRIMARY KEY,Name text,Path text);")

        for i in Extra.Recent:
            value = i.split("=")
            name = value[0]
            path = value[1]
            db.execute('INSERT INTO Recent(Name,Path) VALUES(?,?)',(name,path))
        
        db.commit()

    def add_favourites(song_name,song_path,home):
        global Home
        Home = home

        db.execute("INSERT INTO Favourites(Name,Path) VALUES(?,?)",(song_name,song_path))
        db.commit()

        Database.get_favourites()

    def del_favourites(song_name,home):
        global Home
        Home = home

        db.execute(f"DELETE FROM Favourites WHERE Name= '{song_name}'")
        db.commit()

        Database.get_favourites()

    def get_favourites():
        Extra.Favourites.clear()
        favourites = db.execute('SELECT* FROM Favourites;')
        for i in favourites:
            value = str(i[1]) + "=" + str(i[2])
            Extra.Favourites.append(value)
        
        try:
            Home.configure_fav_page()
        except:
            pass


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

    def load_songs():
        Extra.All_songs.clear()
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
        
    def get_playlist():
        Extra.Playlist.clear()
        for i in db.execute("SELECT name FROM sqlite_master WHERE type='table'"):
            tables = i[0].split("=")
            if len(tables) > 1:
                Extra.Playlist.append(tables[0])

        Extra.Playlist.sort()

    def create_playlist(playlist_name):
        name = f"{str(playlist_name).capitalize()}=playlist"
        db.execute(f"CREATE TABLE '{name}'(id integer PRIMARY KEY,Name text,Path text);")
        db.commit()
        Database.get_playlist()

    def add_song_to_playlist(name,path,playlist):
        db.execute(f"INSERT INTO '{playlist}=playlist'(Name,Path) VALUES(?,?)",(name,path))
        db.commit()

    def add_songs_to_playlist(playlist_name):
        for i in Extra.songs_added:
            value = i.split("=")
            name = value[0]
            path = value[1]
            db.execute(f"INSERT INTO '{playlist_name}=playlist'(Name,Path) VALUES(?,?)",(name,path))
        
        db.commit()
        Extra.songs_added.clear()
        Database.get_playlist_songs(playlist_name)
    
    def del_song_from_playlist(name,playlist_name):
        db.execute(f"DELETE FROM '{playlist_name}=playlist' WHERE Name='{name}'")
        db.commit()
        Database.get_playlist_songs(playlist_name)

    def get_playlist_songs(playlist_name):
        Extra.current_playlist_songs.clear()
        Extra.current_playlist_songs_edit.clear()
        for i in db.execute(f"SELECT * from '{playlist_name}=playlist';"):
            Extra.current_playlist_songs.append(f"{i[1]}={i[2]}")
            Extra.current_playlist_songs_edit.append(f"{i[1]}")

    def check_if_song_exist(name,playlist):
        exist = False
        for i in db.execute(f"SELECT Name FROM '{playlist}=playlist' WHERE Name='{name}'"):
            exist = True

        return exist
    
    def delete_playlist(playlist_name):
        db.execute(f"DROP TABLE '{playlist_name}=playlist'")
        db.commit

        Database.get_playlist()
    
    def close():
        db.close()

Database.get_folder()
Database.get_recent()
Database.get_favourites()
Database.get_playlist()
Database.load_songs()
    


# Art by:

#     ...     ..      ..                                      ....        .   
#   x*8888x.:*8888: -"888:                                 .x88" `^x~  xH(`   
#  X   48888X `8888H  8888             .u    .            X888   x8 ` 8888h   
# X8x.  8888X  8888X  !888>          .d88B :@8c          88888  888.  %8888   
# X8888 X8888  88888   "*8%-        ="8888f8888r        <8888X X8888   X8?    
# '*888!X8888> X8888  xH8>            4888>'88"         X8888> 488888>"8888x  
#   `?8 `8888  X888X X888>            4888> '           X8888>  888888 '8888L 
#   -^  '888"  X888  8888>            4888>             ?8888X   ?8888>'8888X 
#    dx '88~x. !88~  8888>      .    .d888L .+      .    8888X h  8888 '8888~ 
#  .8888Xf.888x:!    X888X.:  .@8c   ^"8888*"     .@8c    ?888  -:8*"  <888"  
# :""888":~"888"     `888*"  '%888"     "Y"      '%888"    `*88.      :88%    
#     "~'    "~        ""      ^*                  ^*         ^"~====""`      