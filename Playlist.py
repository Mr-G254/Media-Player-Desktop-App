from customtkinter import *
from PIL import Image
from Extra import *

class Playlist:
    img0 = CTkImage(Image.open("Icons\plus.png"),size=(20,20))
    img1 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(100,100))
    img2 = CTkImage(Image.open("Icons\playlist_thumbnail.png"),size=(22,22))
    img3 = CTkImage(Image.open("Icons\\reject.png"),size=(20,20))


    def configure_playlist_page(master):
        add = CTkButton(master,image=Playlist.img0,compound=LEFT,text='New Playlist',font=('Times',14),width=120,height=26,corner_radius=4,fg_color="#770B33",hover_color="#770B33",border_color="#0967CC",border_width=0)
        add.place(x=20,y=2)
        add.bind('<Enter>',lambda Event: Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: Extra.unhighlight(Event,add))

        play_frame = CTkScrollableFrame(master,height=295,width=155,fg_color="#641E16")
        play_frame.place(x=0,y=35)

        Y = 0
        for i in Extra.Playlist:
            name = i.split("=")[0]

            playlist = CTkFrame(play_frame,width=150,height=155,corner_radius=8,fg_color="#510723",border_color="#0967CC",border_width=0)
            playlist.grid(column=0,row=Y)
            playlist.bind('<Enter>',lambda Event: Extra.highlight(Event,playlist))
            playlist.bind('<Leave>',lambda Event: Extra.unhighlight(Event,playlist))

            img_label = CTkLabel(playlist,text='',image=Playlist.img1,width=144,height=120,corner_radius=8,fg_color="#770B33")
            img_label.place(x=3,y=3)
            img_label.bind('<Enter>',lambda Event: Extra.highlight(Event,playlist))
            img_label.bind('<Leave>',lambda Event: Extra.unhighlight(Event,playlist))

            frame = CTkFrame(playlist,width=130,height=20,fg_color="#510723")
            frame.place(x=5,y=130)

            play_name = CTkLabel(frame,width=130,height=20,text=name,fg_color="#510723",font=("Times",13))
            play_name.place(x=0,y=0)

            Y = Y + 1

        play_label = CTkLabel(master,text='  My Playlist',image=Playlist.img2,compound=LEFT,font=('Times',15),width=250,height=28,corner_radius=4,fg_color="#770B33",anchor=CENTER,)
        play_label.place(x=295,y=2)

        song_frame = CTkScrollableFrame(master,height=295,width=480,fg_color="#641E16")
        song_frame.place(x=175,y=35)

    def add_song_to_playlist(song_title,x_cord,y_cord):
        cord_x = x_cord + 215
        cord_y = y_cord + 140

        window = CTkToplevel()
        window.geometry(f"600x320+{str(cord_x)}+{str(cord_y)}")
        window.title("Select Playlist")
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

        entry = CTkEntry(entry_frame,height=27,width=140,font=('Times',14),corner_radius=5,fg_color=['gray86', 'gray17'],border_width=0)
        entry.place(x=47,y=2)

        add2 = CTkButton(entry_frame,image=Playlist.img0,text="",width=22,height=30,corner_radius=4,fg_color="#770B33",hover_color="#770B33")
        add2.place(x=187,y=0)

        playlist_frame = CTkScrollableFrame(frame,width=575,height=200,fg_color="#641E16")
        playlist_frame.place(x=0,y=110)
        
