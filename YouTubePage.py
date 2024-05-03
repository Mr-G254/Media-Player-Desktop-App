from customtkinter import*
from tkinter import messagebox
from Extra import Extra
from PIL import Image
from AudioControls import AudioControls
from youtube_search import YoutubeSearch
import urllib.request
import webbrowser
from Downloader import Downloader
import threading

class You_Tube():
    def __init__(self,extra: Extra,audioctrl: AudioControls,download: Downloader):
    
        self.Keywords = ''
        self.vid_window=''
        self.img0 = CTkImage(Image.open("Icons\\youtube_bg.png"),size=(64,64))

        self.Extra = extra
        self.AudioControls = audioctrl
        self.Downloader = download

    def youtube(self,frame,app,b,c,search,clear_btn):
        self.AudioControls.Youtube_mode()

        self.Search = search
        self.Search.unbind('<KeyRelease>')
        self.Search.bind('<KeyRelease>',lambda Event: self.check_search(Event))
        self.Search.bind('<Return>',lambda Event: self.search_youtube_video(Event,self.Search.get()))

        self.Clear_btn = clear_btn
        self.Clear_btn.configure(command=lambda: [self.Search.delete(0,END),self.Clear_btn.place_forget()])

        self.App = app

        self.Frame = frame
        
        self.Extra.close_small_frames()
        b.place_forget()
        c.configure(image=self.img0)
        c.place(x= 5,y= 5)
        self.App.update()

        if self.Extra.Youtube_frame != '':
            self.Extra.configure_frames(self.Extra.Youtube_frame, self.Extra.frames_a)
            self.Extra.Youtube_frame.place(x= 60,y= 105)
        else:

            self.Youtube_page = CTkFrame(self.Frame,height= 500,width= 970,fg_color="#781F15",corner_radius= 6)
            self.Extra.Youtube_frame = self.Youtube_page
            
            if self.Youtube_page in self.Extra.frames_a:
                pass
            else:
                self.Extra.frames_a.append(self.Youtube_page)
                
            self.Extra.configure_frames(self.Youtube_page, self.Extra.frames_a)
            self.Youtube_page.place(x= 60,y= 105)
            self.Extra.notify("Press Enter to search")

            self.Yt_frame = CTkScrollableFrame(self.Youtube_page,height=490,width=945,fg_color="#781F15")
            self.Yt_frame.place(x=0,y=0)

            thread = threading.Thread(target=self.search_yt_video,args=("Technology",),daemon=True)
            thread.start()

    def check_search(self,Event):
        if len(self.Search.get()) > 0:
            self.Clear_btn.place(x = 520,y=2)
        else:
            self.Clear_btn.place_forget()

    def search_youtube_video(self,Event,keywords):
        self.search_yt_video(keywords)

    def search_yt_video(self,keywords):
        self.Keywords = keywords
        try:
            if len(keywords) > 0:
                video_search = YoutubeSearch(keywords, max_results=20).to_dict()
                X = 0
                Y = 0
                for i in video_search:
                    imgurl = i['thumbnails'][0]
                    urllib.request.urlretrieve(imgurl,"image.png")

                    img = CTkImage(Image.open("image.png"),size=(370,200))

                    vid_frame = CTkFrame(self.Yt_frame,height=200,width=940,corner_radius=6,fg_color="#510723",border_color="#0967CC",border_width=0)
                    vid_frame.grid(column= 0,row= Y,pady=5,padx=1)
                    vid_frame.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    vid_frame.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))

                    thumbn_label = CTkLabel(vid_frame,text='',image=img)
                    thumbn_label.place(x=0,y=0)
                    thumbn_label.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    thumbn_label.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))

                    title = str(i['title'])
                    vid_name = CTkLabel(vid_frame,text=title,font=("TImes",19),width=200,height=40,fg_color="#510723",anchor=W,justify='left',wraplength=550)
                    vid_name.place(x=375,y=10)
                    vid_name.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    vid_name.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))

                    views = CTkLabel(vid_frame,text=str(i['views']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    views.place(x=375,y=170)
                    self.App.update()

                    time = CTkLabel(vid_frame,text=str(i['publish_time']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    time.place(x=(views.winfo_width()+380),y=170)
                    self.App.update()

                    dur = CTkLabel(vid_frame,text=str(i['duration']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    dur.place(x=(views.winfo_width()+time.winfo_width()+385),y=170)

                    id = i['id']
                    play_vid = CTkButton(vid_frame,height=30,width=150,text="  Play video",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command=lambda id=id: self.play_video(id))
                    play_vid.place(x=780,y=90)
                    play_vid.bind('<Enter>',lambda Event, play_vid=play_vid: self.Extra.highlight(Event,play_vid))
                    play_vid.bind('<Leave>',lambda Event, play_vid=play_vid: self.Extra.unhighlight(Event,play_vid))
                    play_vid.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    play_vid.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))

                    download_vid = CTkButton(vid_frame,height=30,width=150,text="  Download video",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command= lambda title=title, id=id:[self.Downloader.download_video(self.Frame,title,f"https://www.youtube.com/watch?v={id}"),self.show_downloads()])
                    download_vid.place(x=780,y=125)
                    download_vid.bind('<Enter>',lambda Event, download_vid=download_vid: self.Extra.highlight(Event,download_vid))
                    download_vid.bind('<Leave>',lambda Event, download_vid=download_vid: self.Extra.unhighlight(Event,download_vid))
                    download_vid.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    download_vid.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))

                    download_aud = CTkButton(vid_frame,height=30,width=150,text="  Download audio",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command= lambda title=title, id=id:[self.Downloader.download_audio(self.Frame,title,f"https://www.youtube.com/watch?v={id}"),self.show_downloads()])
                    download_aud.place(x=780,y=160)
                    download_aud.bind('<Enter>',lambda Event, download_aud=download_aud: self.Extra.highlight(Event,download_aud))
                    download_aud.bind('<Leave>',lambda Event, download_aud=download_aud: self.Extra.unhighlight(Event,download_aud))
                    download_aud.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
                    download_aud.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))
            

                    Y = Y + 1
                    self.App.update()
        except Exception as e:
            messagebox.showerror("An error occurred",e)

    def play_video(self,id):
       webbrowser.open(f"https://www.youtube.com/watch?v={id}")

    def on_closing(self):
        self.VideooControls.stop_video()
        self.vid_window.destroy()
        self.VideooControls.is_maxsize = True
        self.App.deiconify()

    def show_downloads(self):
        self.Yt_frame.configure(height=445)



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