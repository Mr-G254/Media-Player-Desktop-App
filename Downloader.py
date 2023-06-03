from customtkinter import *
from tkinter import messagebox
from PIL import Image
from Extra import *
from pytube import YouTube,request
import threading

class Downloader():
    img0 = CTkImage(Image.open("Icons\download.png"),size=(25,25))
    img1 = CTkImage(Image.open("Icons\check-mark.png"),size=(20,20))

    is_downloading = False
    pending = 0

    def show_status(frame,title,url,id):
        Downloader.is_downloading = True

        global dndbtn
        dndbtn = CTkFrame(frame,height= 35,width= 320,fg_color="#641E16",corner_radius= 5,border_color="#0967CC",border_width=0)
        if Downloader.pending == 0:
            dndbtn.place(x= 5,y= 562)
        # else:
        #     X = (Downloader.pending * 325) + 5
        #     dndbtn.place(x= X,y= 562)

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

        global prog_text
        prog_text = CTkLabel(dndbtn,text="0%",fg_color="#510723",font=("TImes",13),corner_radius= 4,height=20)
        prog_text.place(x=280,y=4)

        global progress_bar
        progress_bar = CTkFrame(dndbtn,fg_color="#0967CC",corner_radius=4,height=3,width=0)#280
        progress_bar.place(x=35,y=27)

        thread = threading.Thread(target= Downloader.download,args=(id,url,title),daemon=True)
        thread.start()

    def hide_status():
        dndbtn.destroy()

    def download_audio(frame,title,url):
        Downloader.show_status(frame,title,url,251)
        # Downloader.pending = Downloader.pending + 1

    def download_video(frame,title,url):
        Downloader.show_status(frame,title,url,22)
        # Downloader.pending = Downloader.pending + 1

    def download(id,url,title):
        request.default_range_size=1024000
        yt = YouTube(url)
        yt.register_on_progress_callback(Downloader.show_progress)
        yt.register_on_complete_callback(Downloader.download_commplete)
        stream = yt.streams.get_by_itag(id)
        global file_size
        file_size = stream.filesize

        try:
            if id == 251:
                stream.download(output_path="C:/Users/user/Downloads",filename=f"{str(title)}.mp3",max_retries=3)
            else:
                stream.download(output_path="C:/",filename=f"{title}.mp4",max_retries=3)
        except Exception as e:
            messagebox.showerror("Error",e)
            Downloader.is_downloading = False
            Downloader.hide_status()

    def show_progress(stream,chunk,bytes_remaining):
        percent = 100-((bytes_remaining/file_size)*100)
        prog_text.configure(text = f"{int(percent)}%")
        progress_bar.configure(width = ((percent/100)*280))
    
    def download_commplete(stream,file_path):
        Downloader.is_downloading = False
        prog_text.configure(text="",image=Downloader.img1)


