from customtkinter import*
from tkinter import*
from PIL import Image
from Extra import*
from moviepy.editor import VideoFileClip
import tkVideoPlayer
import vlc
import os
from PIL import Image
from Controls  import VideoControls

class Video():
    img0 = CTkImage(Image.open("Icons\\video_bg.png"),size=(64,64))

    def video(frame,app,a,b,c,search,clear_btn):
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
        App.iconify()
        video_window =CTkToplevel()
        video_window.state('zoomed')
        video_window.title(name)
        video_window.resizable(False,False)

        frame = CTkFrame(video_window,fg_color="black",height=video_window.winfo_height(),width=video_window.winfo_width())
        frame.place(x=0,y=0)

        # media_player = vlc.MediaPlayer() 
        # media = vlc.Media(file_path)
        # media_player.set_media(media)
        # media_player.set_hwnd(frame.winfo_id())
        # media_player.play()

        VideoControls.play_video(file_path,name,frame)
        VideoControls.controls(frame,App,video_window)
        
                

