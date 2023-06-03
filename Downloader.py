from customtkinter import *
from PIL import Image
from Extra import *

class Downloader():
    img0 = CTkImage(Image.open("Icons\download.png"),size=(25,25))

    is_downloading = False

    def show_status(frame,title):
        global dndbtn
        dndbtn = CTkFrame(frame,height= 35,width= 320,fg_color="#641E16",corner_radius= 5,border_color="#0967CC",border_width=0)
        dndbtn.place(x= 5,y= 562)
        dndbtn.bind('<Enter>',lambda Event: Extra.highlight(Event,dndbtn))
        dndbtn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,dndbtn))

        dndlabel = CTkLabel(dndbtn,height=25,width=25,image= Downloader.img0,text = '',fg_color="#641E16")
        dndlabel.place(x=6,y=6)
        dndlabel.bind('<Enter>',lambda Event: Extra.highlight(Event,dndbtn))
        dndlabel.bind('<Leave>',lambda Event: Extra.unhighlight(Event,dndbtn))
        
        txt_frame = CTkFrame(dndbtn,width=240,height=20,fg_color="#510723",corner_radius= 4)
        txt_frame.place(x=35,y=4)

        dndtext = CTkLabel(txt_frame,text=title,fg_color="#510723",font=("TImes",13),corner_radius= 4,anchor=W,height=20,width=250)
        dndtext.place(x=3,y=0)

        prog_text = CTkLabel(dndbtn,text="0%",fg_color="#510723",font=("TImes",13),corner_radius= 4,height=20)
        prog_text.place(x=280,y=4)

        progress = CTkFrame(dndbtn,fg_color="#0967CC",corner_radius=4,height=3,width=0)#280
        progress.place(x=35,y=27)

    def hide_status():
        dndbtn.destroy()

    def download_audio(frame,title,url):
        Downloader.show_status(frame,title)

    def download_video(frame,title,url):
        Downloader.show_status(frame,title)