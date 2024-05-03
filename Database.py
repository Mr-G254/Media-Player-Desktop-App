import sqlite3
import os
from pathlib import Path
from Extra import Extra
from tkinter import messagebox
from MusicPage import Music
from VideoPage import Video
from pydub import AudioSegment

class Database():
    def __init__(self,extra: Extra,msc: Music,vid: Video):
        if "App.db" in os.listdir():
            self.db = sqlite3.connect("App.db")
        else:
            self.db = sqlite3.connect("App.db")

            self.db.execute("CREATE TABLE Folders(id integer PRIMARY KEY,Name text,Path text)")

            music = str(Path.home())+"\Music"
            videos = str(Path.home())+"\Videos"

            self.db.execute('INSERT INTO Folders(Name,Path) VALUES(?,?)',("Music",music))
            self.db.execute('INSERT INTO Folders(Name,Path) VALUES(?,?)',("Videos",videos))

            self.db.execute("CREATE TABLE Recent(id integer PRIMARY KEY,Name text,Path text);")
            self.db.execute("CREATE TABLE Favourites(id integer PRIMARY KEY,Name text,Path text);")
            self.db.execute("CREATE TABLE Playlist(id integer PRIMARY KEY,Name text,Path text);")

            self.db.execute("CREATE TABLE Storage(id integer PRIMARY KEY,Path text);")
            self.db.execute('INSERT INTO Storage(Path) VALUES(?)',["Always ask"])
            
            self.db.commit() 

        self.Extra = extra
        self.Music = msc
        self.Video = vid

        self.get_folder()
        self.get_recent()
        self.get_favourites()
        self.get_playlist()
        self.load_songs()

    def get_folder(self):
        self.Extra.Folders.clear()
        folder = self.db.execute('SELECT* FROM Folders;')
        for i in folder:
            if os.path.exists(str(i[2])):
                value = str(i[0]) + "=" + str(i[1]) + "=" + str(i[2])
                self.Extra.Folders.append(value)

        self.Extra.Folders.sort()

    def get_recent(self):
        self.Extra.Recent.clear()
        recent = self.db.execute('SELECT* FROM Recent;')
        for i in recent:
            if os.path.exists(str(i[2])):
                value = str(i[1]) + "=" + str(i[2])
                self.Extra.Recent.append(value)

    def upload_recent(self):
        self.db.execute("DROP TABLE Recent;")
        self.db.execute("CREATE TABLE Recent(id integer PRIMARY KEY,Name text,Path text);")

        for i in self.Extra.Recent:
            value = i.split("=")
            name = value[0]
            path = value[1]
            self.db.execute('INSERT INTO Recent(Name,Path) VALUES(?,?)',(name,path))
        
        self.db.commit()

    def add_favourites(self,song_name,song_path,home):
        self.Home = home

        self.db.execute("INSERT INTO Favourites(Name,Path) VALUES(?,?)",(song_name,song_path))
        self.db.commit()

        self.get_favourites()

    def del_favourites(self,song_name,home):

        self.db.execute(f"DELETE FROM Favourites WHERE Name= '{song_name}'")
        self.db.commit()

        self.get_favourites()

    def get_favourites(self,):
        self.Extra.Favourites.clear()
        favourites = self.db.execute('SELECT* FROM Favourites;')
        for i in favourites:
            if os.path.exists(str(i[2])):
                value = str(i[1]) + "=" + str(i[2])
                self.Extra.Favourites.append(value)
        
        try:
            self.Home.configure_fav_page()
        except:
            pass


    def get_location(self):
        location = self.db.execute('SELECT* FROM Storage;')
        for i in location:
            value = i
        return value[1]
    
    def update_location(self,location):
        update = "UPDATE Storage set Path = '"+ location +"' WHERE id = 1"
        self.db.execute(update)
        self.db.commit()
    
    def del_folder(self,Event,folder_id,folder_name,folder_class):
        prompt = messagebox.askyesno("Delete Folder",f"Are you sure you want to delete {folder_name} folder")
        if prompt:
            self.Extra.notify(f"Deleting {folder_name} from Folders...")
            self.db.execute(f"DELETE FROM Folders WHERE id={folder_id}")
            self.db.commit()

            self.get_folder()
            folder_class.load_folders()
            self.load_songs()
            self.Extra.undo_noyify()

    def add_folder(self,folder_name,folder_path):
        self.Extra.notify(f"Adding {folder_name} to Folders...")
        self.db.execute("INSERT INTO Folders(Name,Path) VALUES(?,?)",(folder_name,folder_path))
        self.db.commit()

        self.get_folder()
        self.load_songs()
        self.Extra.undo_noyify()

    def load_songs(self):
        self.Extra.All_songs.clear()
        self.Extra.All_videos.clear()

        for i in self.Extra.Folders:
            values = i.split("=")
            for x in os.listdir(values[2]):
                if x.endswith(".mp3"):
                    self.Extra.All_songs.append(f"{x}={values[2]}\{x}")
                
                if x.endswith(".mp4"):
                    self.Extra.All_videos.append(f"{x}={values[2]}\{x}")

                # if x.endswith(".m4a"):
                #     print(os.path.isfile(f"{values[2]}/{x}"))
                #     song = AudioSegment.from_file(f"{values[2]}\{x}", format="m4a")
                #     nm = x.split(".")
                #     song.export(f"{values[2]}/{str(nm[0:len(nm)-1].strip("[").strip("]").strip("'"))}.mp3",format="mp3")

                #     self.Extra.All_songs.append(f"{x.split(".")[0]}.mp3={values[2]}\{x.split(".")[0]}.mp3")
        
        self.Extra.All_songs.sort()
        self.Extra.All_videos.sort()

        try:
             self.Music.show_all_songs()
        except:
                pass
        
        self.Video.get_thumbnails()
        try:
             self.Video.show_all_videos()
        except:
                pass
        
    def get_playlist(self):
        self.Extra.Playlist.clear()
        for i in self.db.execute("SELECT name FROM sqlite_master WHERE type='table'"):
            tables = i[0].split("=")
            if len(tables) > 1:
                self.Extra.Playlist.append(tables[0])

        self.Extra.Playlist.sort()

    def create_playlist(self,playlist_name):
        name = f"{str(playlist_name).capitalize()}=playlist"
        self.db.execute(f"CREATE TABLE '{name}'(id integer PRIMARY KEY,Name text,Path text);")
        self.db.commit()
        self.get_playlist()

    def add_song_to_playlist(self,name,path,playlist):
        self.db.execute(f"INSERT INTO '{playlist}=playlist'(Name,Path) VALUES(?,?)",(name,path))
        self.db.commit()

    def add_songs_to_playlist(self,playlist_name):
        for i in self.Extra.songs_added:
            value = i.split("=")
            name = value[0]
            path = value[1]
            self.db.execute(f"INSERT INTO '{playlist_name}=playlist'(Name,Path) VALUES(?,?)",(name,path))
        
        self.db.commit()
        self.Extra.songs_added.clear()
        self.get_playlist_songs(playlist_name)
    
    def del_song_from_playlist(self,name,playlist_name):
        self.db.execute(f"DELETE FROM '{playlist_name}=playlist' WHERE Name='{name}'")
        self.db.commit()
        self.get_playlist_songs(playlist_name)

    def get_playlist_songs(self,playlist_name):
        self.Extra.current_playlist_songs.clear()
        self.Extra.current_playlist_songs_edit.clear()
        for i in self.db.execute(f"SELECT * from '{playlist_name}=playlist';"):
            if os.path.exists(str(i[2])):
                self.Extra.current_playlist_songs.append(f"{i[1]}={i[2]}")
                self.Extra.current_playlist_songs_edit.append(f"{i[1]}")

    def check_if_song_exist(self,name,playlist):
        exist = False
        for i in self.db.execute(f"SELECT Name FROM '{playlist}=playlist' WHERE Name='{name}'"):
            exist = True

        return exist
    
    def delete_playlist(self,playlist_name):
        self.db.execute(f"DROP TABLE '{playlist_name}=playlist'")
        self.db.commit

        self.get_playlist()
    
    def close(self):
        self.db.close()


    


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