from customtkinter import*
from tkinter import*
from PIL import Image
from Extra import Extra
from moviepy.editor import VideoFileClip
from PIL import Image
from VideoControls  import VideoControls
from AudioControls import AudioControls

class Video():
    def __init__(self,extra: Extra,videoctrl: VideoControls,audioctrl: AudioControls):
        
        self.img0 = CTkImage(Image.open("Icons\\video_bg.png"),size=(64,64))
        self.search_results = []
        self.vid_window = ''

        self.Extra = extra
        self.VideoControls = videoctrl
        self.AudioControls = audioctrl

    def video(self,frame,app,b,c,search,clear_btn):
        self.AudioControls.Normal_mode()
        
        self.Search = search
        self.Clear_btn = clear_btn
        self.App = app
        self.icona = b
        self.iconb = c
        
        self.App.update()

        self.video_page = CTkFrame(frame,height= 385,width= 965,fg_color="#781F15",corner_radius= 6)
        self.Extra.Video_frame = self.video_page
        
        if self.video_page in self.Extra.frames_a:
            pass
        else:
            self.Extra.frames_a.append(self.video_page)

        self.show_all_videos()

    def show_all_videos(self):
        video_frame = CTkScrollableFrame(self.video_page,height= 380,width= 945,fg_color="#781F15",corner_radius= 6)
        video_frame.place(x=0,y=0)

        X= 0
        Y= 0
        for i in self.Extra.All_videos:
            value = i.split("=")
            name = value[0].replace('.mp4','')
            path = value[1]

            index = self.Extra.All_videos.index(i)
            image = self.Extra.video_thumbnails[index]
            img = CTkImage(Image.open(image),size=(312,160))

            if X == 3:
                X = 0
                Y = Y + 1

            vid_frame = CTkFrame(video_frame,height=200,width=313,corner_radius=6,fg_color="#510723",border_color="#0967CC",border_width=0)
            vid_frame.grid(column= X,row= Y,pady=5,padx=1)
            vid_frame.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
            vid_frame.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))
            vid_frame.bind('<Button-1>',lambda Event, path=path, name=name:self.play_video(Event,path,name))

            thumbn_label = CTkLabel(vid_frame,text='',image=img)
            thumbn_label.place(x=0,y=0)
            thumbn_label.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
            thumbn_label.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))
            thumbn_label.bind('<Button-1>',lambda Event, path=path,name=name:self.play_video(Event,path,name))

            frame = CTkFrame(vid_frame,width=290,height=27,fg_color="#510723")
            frame.place(x=10,y=170)

            vid_name = CTkLabel(frame,text=name,font=("TImes",17),width=300,fg_color="#510723",anchor=W)
            vid_name.place(x=0,y=0)
            vid_name.bind('<Enter>',lambda Event, vid_frame=vid_frame: self.Extra.highlight(Event,vid_frame))
            vid_name.bind('<Leave>',lambda Event, vid_frame=vid_frame: self.Extra.unhighlight(Event,vid_frame))
            vid_name.bind('<Button-1>',lambda Event, path=path, name=name:self.play_video(Event,path,name))

            X = X + 1
            self.App.update()
        
        self.search_frame = CTkScrollableFrame(self.video_page,height=200,width=590,corner_radius= 5,fg_color=['gray86', 'gray17'])

    def get_thumbnails(self):
        self.Extra.video_thumbnails.clear()
        no = 0
        if not os.path.exists(f"{os.getcwd()}/Thumbnails"):
            os.makedirs(f"{os.getcwd()}/Thumbnails")

        for i in self.Extra.All_videos:
            value = i.split("=")
            path = value[1]

            clip = VideoFileClip(path)
            thumbnail = f"{os.getcwd()}/Thumbnails/pic{no}.png"
            clip.save_frame(thumbnail,3)

            try:
                self.App.update()
            except:
                pass

            self.Extra.video_thumbnails.append(thumbnail)
            no = no + 1
        
    def play_video(self,Event,file_path,name):
        if self.vid_window !='':
            self.on_closing()

        self.App.iconify()
        video_window =CTkToplevel()
        self.vid_window = video_window
        video_window.state('zoomed')
        video_window.title(name)
        video_window.minsize(900,500)
        video_window.protocol("WM_DELETE_WINDOW",self.on_closing)

        frame = CTkFrame(video_window,fg_color="black",height=video_window.winfo_height(),width=video_window.winfo_width())
        frame.place(x=0,y=0)

        self.VideoControls.play_video(file_path,name,frame)
        self.VideoControls.controls(frame,self.App,video_window)
        
    def search_video(self,Event):    
        self.search_results.clear()

        Y2 = 0
        for i in self.Extra.All_videos:
            if self.Search.get().lower() in i.split(".")[0].lower() and self.Search.get() != "":
                self.search_results.append(i)
        
        if len(self.Search.get()) > 0:
            if self.search_frame.winfo_ismapped():
                for i in self.search_frame.winfo_children():
                    i.destroy()
            
            if len(self.search_results) < 1:
                self.search_frame.place_forget()
            else:
                self.search_frame.place(x=100,y=0)

            self.Clear_btn.place(x = 520,y=2)
        else:
            self.Clear_btn.place_forget()
            self.search_frame.place_forget()
           
            
        for i in self.search_results:
            value = i.split("=")
            name = value[0].replace('.mp4','')
            path = value[1]
            msc2 = CTkFrame(self.search_frame,height=35,width=588,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc2.grid(column= 0,row= Y2,padx= 2,pady= 2)
            msc2.bind('<Enter>',lambda Event, msc2=msc2: self.Extra.highlight(Event,msc2))
            msc2.bind('<Leave>',lambda Event, msc2=msc2: self.Extra.unhighlight(Event,msc2))
            msc2.bind('<Button-1>',lambda Event, path=path, name=name: self.play_video(Event,path,name))
            
            lb2 = CTkLabel(msc2,text=name,font=("TImes",16),fg_color="#510723")
            lb2.place(x=15,y=2)
            lb2.bind('<Enter>',lambda Event, msc2=msc2: self.Extra.highlight(Event,msc2))
            lb2.bind('<Leave>',lambda Event, msc2=msc2: self.Extra.unhighlight(Event,msc2))
            lb2.bind('<Button-1>',lambda Event, path=path, name=name: self.play_video(Event,path,name))

            Y2 = Y2 + 1
   
    def clear_entry(self):
        self.Search.delete(0,END)
        self.search_frame.place_forget()
        self.Clear_btn.place_forget()

    def display(self):
        self.Extra.configure_frames(self.Extra.Video_frame, self.Extra.frames_a)
        self.Extra.Video_frame.place(x= 60,y= 105)

        self.Search.unbind('<KeyRelease>')
        self.Search.bind('<KeyRelease>',lambda Event: self.search_video(Event))
        self.Clear_btn.configure(command= self.clear_entry)

        self.Extra.close_small_frames()
        self.icona.place_forget()
        self.iconb.configure(image=self.img0)
        self.iconb.place(x= 5,y= 5)

    def on_closing(self):
        print("ye")
        self.VideoControls.stop_video()
        self.vid_window.destroy()
        self.VideoControls.is_maxsize = True
        self.App.deiconify()
        


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