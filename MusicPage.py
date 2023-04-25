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
