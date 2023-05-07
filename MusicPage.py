from customtkinter import*
from PIL import Image
from Extra import*
from Controls import*
from pygame import mixer
from mutagen.mp3 import MP3

class Music():
    img0 = CTkImage(Image.open("Icons\music_bg.png"),size=(64,64))


    def music(frame,app,a,b,c):
        global App
        App = app

        Extra.close_small_frames()
        a.place_forget()
        b.place_forget()
        c.configure(image=Music.img0)
        c.place(x= 5,y= 5)
        App.update()


        global music_page
        music_page = CTkFrame(frame,height= 385,width= 965,fg_color="#641E16",corner_radius= 6)
        
        if music_page in Extra.frames_a:
            pass
        else:
            Extra.frames_a.append(music_page)
            
        Extra.configure_frames(music_page, Extra.frames_a)
        music_page.place(x= 60,y= 105)

        Music.show_all_songs()

    def show_all_songs():
        music_frame = CTkScrollableFrame(music_page,height= 380,width= 945,fg_color="#641E16",corner_radius= 6)
        music_frame.place(x=0,y=0)

        Y = 0
        x = 0
        for i in Extra.All_songs:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc = CTkFrame(music_frame,height=35,width=940,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc.grid(column= 0,row= Y,padx= 0,pady= 0)
            msc.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            msc.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            msc.bind('<Button-1>',lambda Event, path=path, name=name: Controls.select_song(Event,path,name))
            
            lb = CTkLabel(msc,text=name,font=("TImes",16),fg_color="#510723")
            lb.place(x=15,y=2)
            lb.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            lb.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            lb.bind('<Button-1>',lambda Event, path=path, name=name: Controls.select_song(Event,path,name))

            dur = MP3(path).info.length
            dur_label = CTkLabel(msc,text=Controls.audio_duration(dur),font=("TImes",16),fg_color="#510723")
            dur_label.place(x=600,y=2)

            if x==1:
                msc.configure(fg_color="#641E16")
                lb.configure(fg_color="#641E16")
                dur_label.configure(fg_color="#641E16")

                x = 0
            else:
                x = 1

            Y = Y + 1
