from customtkinter import*
from PIL import Image
from Extra import*

class Music():
    img0 = CTkImage(Image.open("Icons\music_bg.png"),size=(64,64))


    def music(frame,app,a,b,c):
        Extra.close_small_frames()
        a.place_forget()
        b.place_forget()
        c.configure(image=Music.img0)
        c.place(x= 5,y= 5)


        global music_page
        music_page = CTkScrollableFrame(frame,height= 370,width= 915,fg_color="#641E16",corner_radius= 6)
        
        if music_page in Extra.frames_a:
            pass
        else:
            Extra.frames_a.append(music_page)
            
        Extra.configure_frames(music_page, Extra.frames_a)
        music_page.place(x= 60,y= 110)

        Y = 0
        x = 0
        for i in Extra.All_songs:
            value = i.split("=")
            msc = CTkFrame(music_page,height=35,width=900,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc.grid(column= 0,row= Y,padx= 0,pady= 0)
            msc.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            msc.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            
            lb = CTkLabel(msc,text=value[0].replace('.mp3',''),font=("TImes",16),fg_color="#510723")
            lb.place(x=15,y=2)
            lb.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            lb.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))

            if x==1:
                msc.configure(fg_color="#641E16")
                lb.configure(fg_color="#641E16")

                x = 0
            else:
                x = 1

            Y = Y + 1