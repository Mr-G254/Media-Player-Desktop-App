from customtkinter import *
from tkinter import messagebox
from PIL import Image
from Extra import Extra
from AudioControls import AudioControls

class Playlist():
    def __init__(self,extra: Extra,audioctrl: AudioControls):
        self.img0 = CTkImage(Image.open("Icons\plus.png"),size=(20,20))
        self.img1 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(100,100))
        self.img2 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(22,22))
        self.img3 = CTkImage(Image.open("Icons\\reject.png"),size=(20,20))
        self.img4 = CTkImage(Image.open("Icons\delete.png"),size=(20,20))

        self.frame = ''
        self.current_playlist = ''
        self.playlist_labels = []
        self.Extra = extra
        self.AudioControls = audioctrl

    def get_database(self,database,app):
        self.Database = database

        self.App =app

    def configure_playlist_page(self,master):
        self.frame = master
        add_playlist = CTkButton(self.frame,image=self.img0,compound=LEFT,text='New Playlist',font=('Times',14),width=120,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: self.add_song_to_playlist_window("Create a new playlist",self.App.winfo_x(),self.App.winfo_y(),""))
        add_playlist.place(x=20,y=2)
        add_playlist.bind('<Enter>',lambda Event: self.Extra.highlight(Event,add_playlist))
        add_playlist.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,add_playlist))

        self.play_frame = CTkScrollableFrame(master,height=285,width=155,fg_color="#641E16")
        self.play_frame.place(x=0,y=35)

        self.add_songs = CTkButton(self.frame,image=self.img0,compound=LEFT,text='',width=26,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0)
        self.add_songs.place(x=258,y=2)
        self.add_songs.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.add_songs))
        self.add_songs.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.add_songs))

        self.play_label = CTkLabel(master,text='',image=self.img2,compound=LEFT,font=('Times',15),width=250,height=28,corner_radius=4,fg_color="#770B33",anchor=CENTER,)
        self.play_label.place(x=295,y=2)

        self.del_playlist = CTkButton(self.frame,image=self.img4,compound=LEFT,text='',width=26,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0)
        self.del_playlist.place(x=550,y=2)
        self.del_playlist.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.del_playlist))
        self.del_playlist.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.del_playlist))

        self.song_frame = CTkScrollableFrame(self.frame,height=285,width=475,fg_color="#641E16")
        self.song_frame.place(x=175,y=35)

        self.show_playlists()

    def show_playlists(self):
        self.playlist_labels.clear()
        Y = 0
        for i in self.Extra.Playlist:
            name = i

            playlist = CTkFrame(self.play_frame,width=150,height=155,corner_radius=8,fg_color="#510723",border_color="#0967CC",border_width=0)
            playlist.grid(column=0,row=Y,pady=5)
            playlist.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            playlist.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))
            playlist.bind('<Button-1>',lambda Event, name=name, Y=Y: [self.select_playlist(Y),self.fetch_current_playlist_songs(Event,name)])

            img_label = CTkLabel(playlist,text='',image=self.img1,width=144,height=120,corner_radius=8,fg_color="#770B33")
            img_label.place(x=3,y=3)
            img_label.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            img_label.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))
            img_label.bind('<Button-1>',lambda Event, name=name, Y=Y: [self.select_playlist(Y),self.fetch_current_playlist_songs(Event,name)])

            frame = CTkFrame(playlist,width=130,height=20,fg_color="#510723",corner_radius=5)
            frame.place(x=5,y=130)
            frame.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            frame.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))
            frame.bind('<Button-1>',lambda Event, name=name, Y=Y: [self.select_playlist(Y),self.fetch_current_playlist_songs(Event,name)])

            play_name = CTkLabel(frame,height=20,text=name,fg_color="#510723",font=("Times",16),corner_radius=5)
            play_name.place(x=0,y=0)
            play_name.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            play_name.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))
            play_name.bind('<Button-1>',lambda Event, name=name, Y=Y: [self.select_playlist(Y),self.fetch_current_playlist_songs(Event,name)])
            self.playlist_labels.append(play_name)

            if Y == 0:
                self.select_playlist(Y)
                self.fetch_current_playlist(name)

            Y = Y + 1

    def add_song_to_playlist_window(self,song_title,x_cord,y_cord,path):
        cord_x = x_cord + 215
        cord_y = y_cord + 140

        self.window = CTkToplevel()
        self.window.geometry(f"600x320+{str(cord_x)}+{str(cord_y)}")
        if path:
            self.window.title("Select Playlist (Double click to add song to playlist)")
        else:
            self.window.title("New Playlist")

        self.window.resizable(False,False)
        self.window.attributes("-topmost",True)
        self.window.grab_set()

        frame = CTkFrame(self.window,width=600,height=320,fg_color="#641E16")
        frame.place(x=0,y=0)

        H = (len(song_title)*6) + 60
        X = (300-(H/2))
        if X < 5:
            X = 5

        title_label = CTkLabel(frame,text=song_title,height=30,width=H,corner_radius=6,fg_color="#770B33",font=("Times",16))
        title_label.place(x=X,y=5)

        entry_frame = CTkFrame(frame,height=30,width=222,corner_radius=6,fg_color="#770B33",border_color="#0967CC",border_width=0)

        cancel_btn = CTkButton(frame,text="",image=self.img3,width=26,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: [self.window.grab_release(),self.window.destroy()])
        cancel_btn.place(x=5,y=45)
        cancel_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,cancel_btn))
        cancel_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,cancel_btn))

        add = CTkButton(frame,text='New Playlist',font=('Times',14),width=186,height=28,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: entry_frame.place(x=5,y=77))
        add.place(x=41,y=45)
        add.bind('<Enter>',lambda Event: self.Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,add))

        label = CTkLabel(entry_frame,text='Name',height=30,font=('Times',14),fg_color="#770B33")
        label.place(x=5,y=0)

        self.entry = CTkEntry(entry_frame,height=27,width=140,font=('Times',14),corner_radius=5,fg_color=['gray86', 'gray17'],border_width=0)
        self.entry.place(x=47,y=2)

        add2 = CTkButton(entry_frame,image=self.img0,text="",width=22,height=30,corner_radius=4,fg_color="#770B33",hover_color="#770B33",command= lambda: self.add_playlist())
        add2.place(x=187,y=0)

        self.playlist_frame = CTkScrollableFrame(frame,width=535,height=200,fg_color="#641E16")
        self.playlist_frame.place(x=40,y=110)

        self.show_playlist_toplevel(song_title,path)

    def show_playlist_toplevel(self,song,path):
        X = 0
        Y = 0
        for i in self.Extra.Playlist:
            name = i

            playlist = CTkFrame(self.playlist_frame,width=150,height=155,corner_radius=8,fg_color="#510723",border_color="#0967CC",border_width=0)
            playlist.grid(column=X,row=Y,padx=10,pady=5)
            playlist.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            playlist.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))

            img_label = CTkLabel(playlist,text='',image=self.img1,width=144,height=120,corner_radius=8,fg_color="#770B33")
            img_label.place(x=3,y=3)
            img_label.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            img_label.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))

            frame = CTkFrame(playlist,width=130,height=20,fg_color="#510723")
            frame.place(x=5,y=130)
            frame.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            frame.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))

            play_name = CTkLabel(frame,width=130,height=20,text=name,fg_color="#510723",font=("Times",15))
            play_name.place(x=0,y=0)
            play_name.bind('<Enter>',lambda Event, playlist=playlist: self.Extra.highlight(Event,playlist))
            play_name.bind('<Leave>',lambda Event, playlist=playlist: self.Extra.unhighlight(Event,playlist))

            if path:
                playlist.bind('<Double-Button-1>',lambda Event, song=song, path=path, name=name: self.add_song_to_playlist(Event,song,path,name))
                img_label.bind('<Double-Button-1>',lambda Event, song=song, path=path, name=name: self.add_song_to_playlist(Event,song,path,name))
                frame.bind('<Double-Button-1>',lambda Event, song=song, path=path, name=name: self.add_song_to_playlist(Event,song,path,name))
                play_name.bind('<Double-Button-1>',lambda Event, song=song, path=path, name=name: self.add_song_to_playlist(Event,song,path,name))

            if X == 2:
                X = 0 
                Y = Y + 1
            else:
                X = X + 1

    def select_playlist(self,index):
        for i in range(len(self.playlist_labels)):
            if i == index:
                self.playlist_labels[i].configure(fg_color="#770B33")
            else:
                self.playlist_labels[i].configure(fg_color="#510723")

    def add_playlist(self):
        playlist = str(self.entry.get())

        if playlist and playlist.capitalize() not in self.Extra.Playlist:

            self.Database.create_playlist(playlist)
            self.update_playlist_page()
            self.show_playlist_toplevel("","")
            self.entry.delete(0,END)
        else:
            messagebox.showinfo("Can't create playlist",f"The playlist '{playlist.capitalize()}' already exists",parent=self.window)
            self.entry.delete(0,END)

    def add_song_to_playlist(self,Event,name,path,playlist):
        exist = self.Database.check_if_song_exist(name,playlist)
        if exist:
            messagebox.showerror("Song can't be added more than once",f"'{name}' already exists in the playlist",parent=self.window)
        else:
            self.Database.add_song_to_playlist(name,path,playlist)
            messagebox.showinfo("Song added to playlist successfully",f"'{name}' has been successfully added to '{playlist}' playlist",parent=self.window)
            self.window.grab_release()
            self.window.destroy()


    def update_playlist_page(self):
        if self.frame:
            self.show_playlists()
        
    def fetch_current_playlist_songs(self,Event,playlist_name):
        self.fetch_current_playlist(playlist_name)

    def fetch_current_playlist(self,playlist_name):
        self.current_playlist = playlist_name
        for i in self.song_frame.winfo_children():
            i.destroy()

        self.add_songs.configure(command=lambda: self.add_songs_to_playlist(playlist_name))
        self.play_label.configure(text=f"  {playlist_name}")
        self.del_playlist.configure(command=lambda: self.delete_playlist(playlist_name))
        self.Database.get_playlist_songs(playlist_name)

        Y5=0
        self.Extra.playlist_frames.clear()
        for i in self.Extra.current_playlist_songs:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc4 = CTkFrame(self.song_frame,height=35,width=470,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc4.grid(column= 0,row= Y5,padx= 2,pady= 2)
            msc4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
            msc4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))
            msc4.bind('<Button-1>',lambda Event, path=path, name=name: self.AudioControls.select_song(Event,path,name,"Playlist"))
            self.Extra.playlist_frames.append(msc4)
            
            lb4 = CTkLabel(msc4,text=name,font=("TImes",15),fg_color="#510723")
            lb4.place(x=15,y=2)
            lb4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
            lb4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))
            lb4.bind('<Button-1>',lambda Event, path=path, name=name: self.AudioControls.select_song(Event,path,name,"Playlist"))

            del_song = CTkButton(msc4,image=self.img4,compound=LEFT,text='',width=26,height=28,corner_radius=4,fg_color="#510723",hover_color="#510723",command=lambda name=name: self.del_song_from_playlist(name,playlist_name))
            del_song.place(x=440,y=2)

            Y5 = Y5 + 1

    def add_songs_to_playlist(self,playlist_name):
        self.frame = CTkFrame(self.frame,height=330,width=680,fg_color="#641E16")
        self.frame.place(x=0,y=2)

        self.done_btn = CTkButton(self.frame,text="Done (0)",font=("Times",15),width=75,height=28,corner_radius=4,fg_color="#510723",command=lambda: self.done(playlist_name))
        self.done_btn.place(x=555,y=10)

        cancel_btn = CTkButton(self.frame,text="",image=self.img3,width=26,height=26,corner_radius=4,fg_color="#510723",command=lambda: self.frame.destroy())
        cancel_btn.place(x=635,y=10)

        label = CTkLabel(self.frame,text=f"  Add songs to '{playlist_name}' playlist  ",height=30,font=("Times",16),fg_color="#770B33",corner_radius=5)
        label.place(x=5,y=10)

        song_frame2 = CTkScrollableFrame(self.frame,height=280,width=655,fg_color="#641E16")
        song_frame2.place(x=0,y=45)

        Y6 = 0
        for i in self.Extra.All_songs:
            if str(i).split("=")[0] not in self.Extra.current_playlist_songs_edit:
                value = i.split("=")
                name = value[0].replace('.mp3','')
                path = value[1]
                msc4 = CTkFrame(song_frame2,height=35,width=650,fg_color="#510723",border_color="#0967CC",border_width=0)
                msc4.grid(column= 0,row= Y6,padx= 2,pady= 2)
                msc4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
                msc4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))
                
                lb4 = CTkLabel(msc4,text=name,font=("TImes",15),fg_color="#510723")
                lb4.place(x=15,y=2)
                lb4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
                lb4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))

                check = CTkCheckBox(msc4,text="",fg_color="#510723",width=25,height=25)
                check.place(x=616,y=5)
                check.configure(command=lambda check=check, name=name, path=path: self.checkbox(check,name,path))

                Y6 = Y6 + 1

    def del_song_from_playlist(self,name,playlist_name):
        ask = messagebox.askyesno("Delete song from playlist",f"Are you sure you want to delete '{name}' from '{playlist_name}' playlist")
        if ask:
            self.Database.del_song_from_playlist(f"{name}.mp3",playlist_name)
            self.fetch_current_playlist(playlist_name)

    def checkbox(self,checkbox,name,path):
        if checkbox.get():
            self.Extra.songs_added.append(f"{name}.mp3={path}")
        else:
            index = self.Extra.songs_added.index(f"{name}.mp3={path}")
            self.Extra.songs_added.pop(index)

        self.done_btn.configure(text=f"Done ({str(len(Extra.songs_added))})")

    def done(self,playlist_name):
        self.Database.add_songs_to_playlist(playlist_name)
        self.frame.destroy()
        self.fetch_current_playlist(playlist_name)

    def delete_playlist(self,playlist_name):
        if messagebox.askyesno("Deleting playlist",f"Are you sure you want to delete '{playlist_name}' playlist"):
            self.Database.delete_playlist(playlist_name)
            self.configure_playlist_page(self.frame)

            self.play_label.configure(text="")
            for i in self.song_frame.winfo_children():
                i.destroy()



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