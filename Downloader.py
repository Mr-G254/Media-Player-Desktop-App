from customtkinter import *
from tkinter import messagebox,filedialog
from PIL import Image
from Extra import Extra
from Database import Database
from pytube import YouTube,request
import threading
from pydub import AudioSegment
from time import sleep

class Downloader():
    def __init__(self,extra: Extra,db: Database):
        
        self.img0 = CTkImage(Image.open("Icons\download.png"),size=(25,25))
        self.img1 = CTkImage(Image.open("Icons\check-mark.png"),size=(19,19))

        self.is_downloading = False
        self.pending = 0

        self.Database = db
        self.Extra = extra

    def show_status(self,frame,title,url,id):
        try:
            self.hide_status()
        except:
            pass

        self.is_downloading = True

        global dndbtn
        dndbtn = CTkFrame(frame,height= 35,width= 320,fg_color="#641E16",corner_radius= 5,border_color="#0967CC",border_width=0)
        if self.pending == 0:
            dndbtn.place(x= 5,y= 562)

        dndbtn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,dndbtn))
        dndbtn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,dndbtn))

        dndlabel = CTkLabel(dndbtn,height=25,width=25,image= self.img0,text = '',fg_color="#641E16")
        dndlabel.place(x=6,y=6)
        dndlabel.bind('<Enter>',lambda Event: self.Extra.highlight(Event,dndbtn))
        dndlabel.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,dndbtn))
        
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

        thread = threading.Thread(target= self.download,args=(id,url,title, self.Database.get_location()),daemon=True)
        thread.start()

    def hide_status(self):
        dndbtn.destroy()

    def download_audio(self,frame,title,url):
        if not self.is_downloading:
            self.show_status(frame,title,url,140)

    def download_video(self,frame,title,url):
        if not self.is_downloading:
            self.show_status(frame,title,url,22)

    def download(self,id,url,title,location):
        request.default_range_size=1024000
        yt = YouTube(url)
        yt.register_on_progress_callback(self.show_progress)
        yt.register_on_complete_callback(self.download_commplete)
        stream = yt.streams.get_by_itag(id)
        global file_size
        file_size = stream.filesize

        if location == "Always ask":
            storage_location = filedialog.askdirectory(title="Choose where we should save downloads")

        else:
            storage_location = location

        if storage_location:
            title = title.replace("|","")
            title = title.replace("*"," ")
            try:
                if id == 140:
                    print(f"{storage_location}/{str(title)}.m4a")
                    stream.download(output_path=storage_location,filename=f"{str(title)}.m4a",max_retries=3)
                else:
                    stream.download(output_path=storage_location,filename=f"{title}.mp4",max_retries=3)
                
                song = AudioSegment.from_file(f"{storage_location}/{str(title)}.m4a", format="m4a")
                song.export(f"{storage_location}/{str(title)}.mp3",format="mp3")
            except Exception as e:
                messagebox.showerror("Error",e)
                self.is_downloading = False
                self.hide_status()

    def show_progress(self,stream,chunk,bytes_remaining):
        percent = 100-((bytes_remaining/file_size)*100)
        prog_text.configure(text = f"{int(percent)}%")
        progress_bar.configure(width = ((percent/100)*280))
    
    def download_commplete(self,stream,file_path):
        self.is_downloading = False
        prog_text.place(x=285,y=4)
        prog_text.configure(text="",image=self.img1)



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