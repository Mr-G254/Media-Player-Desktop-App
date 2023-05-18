from customtkinter import*
from tkinter import*
from PIL import Image
from Extra import*
from moviepy.editor import VideoFileClip
import tkVideoPlayer
import vlc
import os
from PIL import Image
from VideoControls  import*

class Video():
    img0 = CTkImage(Image.open("Icons\\video_bg.png"),size=(64,64))
    search_results = []
    vid_window = ''

    def video(frame,app,a,b,c,search,clear_btn):
        global Search
        Search = search
        Search.unbind('<KeyRelease>')
        Search.bind('<KeyRelease>',lambda Event: Video.search_video(Event))

        global Clear_btn
        Clear_btn = clear_btn
        Clear_btn.configure(command= Video.clear_entry)

        global App
        App = app

        Extra.close_small_frames()
        a.place_forget()
        b.place_forget()
        c.configure(image=Video.img0)
        c.place(x= 5,y= 5)
        App.update()

        if Extra.Video_frame != '':
            Extra.configure_frames(Extra.Video_frame, Extra.frames_a)
            Extra.Video_frame.place(x= 55,y= 105)
        else:

            global video_page
            video_page = CTkFrame(frame,height= 385,width= 965,fg_color="#641E16",corner_radius= 6)
            Extra.Video_frame = video_page
            
            if video_page in Extra.frames_a:
                pass
            else:
                Extra.frames_a.append(video_page)
                
            Extra.configure_frames(video_page, Extra.frames_a)
            video_page.place(x= 55,y= 105)

            Video.show_all_videos()

    def show_all_videos():
        video_frame = CTkScrollableFrame(video_page,height= 380,width= 945,fg_color="#641E16",corner_radius= 6)
        video_frame.place(x=0,y=0)

        X= 0
        Y= 0
        for i in Extra.All_videos:
            value = i.split("=")
            name = value[0].replace('.mp4','')
            path = value[1]

            index = Extra.All_videos.index(i)
            image = Extra.video_thumbnails[index]
            img = CTkImage(Image.open(image),size=(312,160))

            if X == 3:
                X = 0
                Y = Y + 1

            vid_frame = CTkFrame(video_frame,height=200,width=313,corner_radius=6,fg_color="#510723",border_color="#0967CC",border_width=0)
            vid_frame.grid(column= X,row= Y,pady=5,padx=1)
            vid_frame.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
            vid_frame.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
            vid_frame.bind('<Button-1>',lambda Event, path=path, name=name:Video.play_video(Event,path,name))

            thumbn_label = CTkLabel(vid_frame,text='',image=img)
            thumbn_label.place(x=0,y=0)
            thumbn_label.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
            thumbn_label.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
            thumbn_label.bind('<Button-1>',lambda Event, path=path,name=name:Video.play_video(Event,path,name))

            vid_name = CTkLabel(vid_frame,text=name,font=("TImes",17),width=200,fg_color="#510723",anchor=W)
            vid_name.place(x=10,y=170)
            vid_name.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
            vid_name.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
            vid_name.bind('<Button-1>',lambda Event, path=path, name=name:Video.play_video(Event,path,name))

            X = X + 1
        
        global search_frame
        search_frame = CTkScrollableFrame(video_page,height=200,width=590,corner_radius= 5,fg_color=['gray86', 'gray17'])

    def get_thumbnails():
        Extra.video_thumbnails.clear()
        no = 0
        if not os.path.exists(f"{os.getcwd()}/Thumbnails"):
            os.makedirs(f"{os.getcwd()}/Thumbnails")

        for i in Extra.All_videos:
            value = i.split("=")
            path = value[1]

            clip = VideoFileClip(path)
            thumbnail = f"{os.getcwd()}/Thumbnails/pic{no}.png"
            clip.save_frame(thumbnail,3)

            try:
                App.update()
            except:
                pass

            Extra.video_thumbnails.append(thumbnail)
            no = no + 1
        
    def play_video(Event,file_path,name):
        if Video.vid_window !='':
            Video.on_closing()

        App.iconify()
        video_window =CTkToplevel()
        Video.vid_window = video_window
        video_window.state('zoomed')
        video_window.title(name)
        video_window.minsize(900,500)
        video_window.protocol("WM_DELETE_WINDOW",Video.on_closing)

        frame = CTkFrame(video_window,fg_color="black",height=video_window.winfo_height(),width=video_window.winfo_width())
        frame.place(x=0,y=0)

        VideoControls.play_video(file_path,name,frame)
        VideoControls.controls(frame,App,video_window)
        
    def search_video(Event):    
        Video.search_results.clear()

        if len(Search.get()) > 0:
            Clear_btn.place(x = 520,y=2)
        else:
            Clear_btn.place_forget()

        if search_frame.winfo_ismapped():
            for i in search_frame.winfo_children():
                i.destroy()
        else:
            search_frame.place(x=100,y=0)

        Y2 = 0
        for i in Extra.All_videos:
            if i.lower().startswith(Search.get().lower()):
                Video.search_results.append(i)
           
            
        for i in Video.search_results:
            value = i.split("=")
            name = value[0].replace('.mp4','')
            path = value[1]
            msc2 = CTkFrame(search_frame,height=35,width=588,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc2.grid(column= 0,row= Y2,padx= 2,pady= 2)
            msc2.bind('<Enter>',lambda Event, msc2=msc2: Extra.highlight(Event,msc2))
            msc2.bind('<Leave>',lambda Event, msc2=msc2: Extra.unhighlight(Event,msc2))
            msc2.bind('<Button-1>',lambda Event, path=path, name=name: Video.play_video(Event,path,name))
            
            lb2 = CTkLabel(msc2,text=name,font=("TImes",16),fg_color="#510723")
            lb2.place(x=15,y=2)
            lb2.bind('<Enter>',lambda Event, msc2=msc2: Extra.highlight(Event,msc2))
            lb2.bind('<Leave>',lambda Event, msc2=msc2: Extra.unhighlight(Event,msc2))
            lb2.bind('<Button-1>',lambda Event, path=path, name=name: Video.play_video(Event,path,name))

            Y2 = Y2 + 1
   
    def clear_entry():
        Search.delete(0,END)
        search_frame.place_forget()
        Clear_btn.place_forget()

    def on_closing():
        VideoControls.stop_video()
        Video.vid_window.destroy()
        VideoControls.is_maxsize = True