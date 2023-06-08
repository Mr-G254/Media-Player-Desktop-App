from customtkinter import *
from tkinter import messagebox
from PIL import Image
from Extra import *

class Playlist():
    img0 = CTkImage(Image.open("Icons\plus.png"),size=(20,20))
    img1 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(100,100))
    img2 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(22,22))
    img3 = CTkImage(Image.open("Icons\\reject.png"),size=(20,20))

    frame = ''

    def get_database(database,app):
        global Database
        Database = database

        global App
        App =app

    def configure_playlist_page(master):
        Playlist.frame = master
        add = CTkButton(Playlist.frame,image=Playlist.img0,compound=LEFT,text='New Playlist',font=('Times',14),width=120,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: Playlist.add_song_to_playlist_window("Create a new playlist",App.winfo_x(),App.winfo_y(),""))
        add.place(x=20,y=2)
        add.bind('<Enter>',lambda Event: Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: Extra.unhighlight(Event,add))

        global play_frame
        play_frame = CTkScrollableFrame(master,height=295,width=155,fg_color="#641E16")
        play_frame.place(x=0,y=35)

        Playlist.show_playlists()

        play_label = CTkLabel(master,text='  My Playlist',image=Playlist.img2,compound=LEFT,font=('Times',15),width=250,height=28,corner_radius=4,fg_color="#770B33",anchor=CENTER,)
        play_label.place(x=295,y=2)

        song_frame = CTkScrollableFrame(master,height=295,width=480,fg_color="#641E16")
        song_frame.place(x=175,y=35)

    def show_playlists():
        Y = 0
        for i in Extra.Playlist:
            name = i

            playlist = CTkFrame(play_frame,width=150,height=155,corner_radius=8,fg_color="#510723",border_color="#0967CC",border_width=0)
            playlist.grid(column=0,row=Y,pady=5)
            playlist.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            playlist.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            img_label = CTkLabel(playlist,text='',image=Playlist.img1,width=144,height=120,corner_radius=8,fg_color="#770B33")
            img_label.place(x=3,y=3)
            img_label.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            img_label.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            frame = CTkFrame(playlist,width=130,height=20,fg_color="#510723")
            frame.place(x=5,y=130)
            frame.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            frame.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            play_name = CTkLabel(frame,width=130,height=20,text=name,fg_color="#510723",font=("Times",15))
            play_name.place(x=0,y=0)
            play_name.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            play_name.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            Y = Y + 1

    def add_song_to_playlist_window(song_title,x_cord,y_cord,path):
        cord_x = x_cord + 215
        cord_y = y_cord + 140

        global window
        window = CTkToplevel()
        window.geometry(f"600x320+{str(cord_x)}+{str(cord_y)}")
        if path:
            window.title("Select Playlist (Double click to add song to playlist)")
        else:
            window.title("New Playlist")

        window.resizable(False,False)
        window.attributes("-topmost",True)
        window.grab_set()

        frame = CTkFrame(window,width=600,height=320,fg_color="#641E16")
        frame.place(x=0,y=0)

        H = (len(song_title)*6) + 60
        X = (300-(H/2))
        if X < 5:
            X = 5

        title_label = CTkLabel(frame,text=song_title,height=30,width=H,corner_radius=6,fg_color="#770B33",font=("Times",16))
        title_label.place(x=X,y=5)

        entry_frame = CTkFrame(frame,height=30,width=222,corner_radius=6,fg_color="#770B33",border_color="#0967CC",border_width=0)

        cancel_btn = CTkButton(frame,text="",image=Playlist.img3,width=26,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: [window.grab_release(),window.destroy()])
        cancel_btn.place(x=5,y=45)
        cancel_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,cancel_btn))
        cancel_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,cancel_btn))

        add = CTkButton(frame,text='New Playlist',font=('Times',14),width=186,height=28,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0,command=lambda: entry_frame.place(x=5,y=77))
        add.place(x=41,y=45)
        add.bind('<Enter>',lambda Event: Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: Extra.unhighlight(Event,add))

        label = CTkLabel(entry_frame,text='Name',height=30,font=('Times',14),fg_color="#770B33")
        label.place(x=5,y=0)

        global entry
        entry = CTkEntry(entry_frame,height=27,width=140,font=('Times',14),corner_radius=5,fg_color=['gray86', 'gray17'],border_width=0)
        entry.place(x=47,y=2)

        add2 = CTkButton(entry_frame,image=Playlist.img0,text="",width=22,height=30,corner_radius=4,fg_color="#770B33",hover_color="#770B33",command= lambda: Playlist.add_playlist())
        add2.place(x=187,y=0)

        global playlist_frame
        playlist_frame = CTkScrollableFrame(frame,width=535,height=200,fg_color="#641E16")
        playlist_frame.place(x=40,y=110)

        Playlist.show_playlist_toplevel(song_title,path)

    def show_playlist_toplevel(song,path):
        X = 0
        Y = 0
        for i in Extra.Playlist:
            name = i

            playlist = CTkFrame(playlist_frame,width=150,height=155,corner_radius=8,fg_color="#510723",border_color="#0967CC",border_width=0)
            playlist.grid(column=X,row=Y,padx=10,pady=5)
            playlist.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            playlist.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            img_label = CTkLabel(playlist,text='',image=Playlist.img1,width=144,height=120,corner_radius=8,fg_color="#770B33")
            img_label.place(x=3,y=3)
            img_label.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            img_label.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            frame = CTkFrame(playlist,width=130,height=20,fg_color="#510723")
            frame.place(x=5,y=130)
            frame.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            frame.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            play_name = CTkLabel(frame,width=130,height=20,text=name,fg_color="#510723",font=("Times",15))
            play_name.place(x=0,y=0)
            play_name.bind('<Enter>',lambda Event, playlist=playlist: Extra.highlight(Event,playlist))
            play_name.bind('<Leave>',lambda Event, playlist=playlist: Extra.unhighlight(Event,playlist))

            if path:
                playlist.bind('<Double-Button-1>',lambda Event: Playlist.add_song_to_playlist(Event,song,path,name))
                img_label.bind('<Double-Button-1>',lambda Event: Playlist.add_song_to_playlist(Event,song,path,name))
                frame.bind('<Double-Button-1>',lambda Event: Playlist.add_song_to_playlist(Event,song,path,name))
                play_name.bind('<Double-Button-1>',lambda Event: Playlist.add_song_to_playlist(Event,song,path,name))

            if X == 2:
                X = 0 
                Y = Y + 1
            else:
                X = X + 1

    def add_playlist():
        playlist = str(entry.get())
        if playlist and playlist.capitalize() not in Extra.Playlist:

            Database.create_playlist(playlist)
            Playlist.update_playlist_page()
            Playlist.show_playlist_toplevel("","")
            entry.delete(0,END)
        else:
            messagebox.showinfo("Can't create playlist",f"The playlist '{playlist.capitalize()}' already exists",parent=window)
            entry.delete(0,END)

    def add_song_to_playlist(Event,name,path,playlist):
        Database.add_song_to_playlist(name,path,playlist)
        messagebox.showinfo("Song added to playlist successfully",f"{name} has been successfully added to '{playlist}' playlist",parent=window)
        window.grab_release()
        window.destroy()


    def update_playlist_page():
        if Playlist.frame:
            Playlist.show_playlists()
        
