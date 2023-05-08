from customtkinter import*
from PIL import Image
from Extra import*

class Video():
    img0 = CTkImage(Image.open("Icons\\video_bg.png"),size=(64,64))

    def video(frame,app,a,b,c):
        Extra.close_small_frames()
        a.place_forget()
        b.place_forget()
        c.configure(image=Video.img0)
        c.place(x= 5,y= 5)
        app.update()


        global video_page
        video_page = CTkFrame(frame,height= 385,width= 965,fg_color="#641E16",corner_radius= 6)
        
        if video_page in Extra.frames_a:
            pass
        else:
            Extra.frames_a.append(video_page)
            
        Extra.configure_frames(video_page, Extra.frames_a)
        video_page.place(x= 60,y= 105)