from Controls import*
from customtkinter import*
import vlc
import pafy

class VideoControls(Control):
    vid_name = ''
    playing = True
    vol_on = True
    video_length = 0
    is_maxsize = True

    def controls(frame,app,window):
        global App
        App = app

        global Frame
        Frame = frame

        global Window
        Window = window
        
        global Height
        Height = window.winfo_height()

        global Width
        Width = window.winfo_width()

        global frame_width
        frame_width = Width - 10

        global prog_width
        prog_width = frame_width-20

        global controlframe
        controlframe = CTkFrame(window,fg_color="#510723",height= 80,width=Width,corner_radius= 6)
        controlframe.place(x=0,y=Height-80)

        global progressbar
        progressbar = CTkSlider(controlframe,from_=0,to=frame_width-20,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=Width-30,command=VideoControls.move_video_progress)
        progressbar.set(Width-30)
        progressbar.place(x= 5,y= 5)

        global resize
        resize = CTkButton(controlframe,text='',image=VideoControls.img15,height=25,width=25,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=VideoControls.minimize)
        resize.place(x=Width-30,y=0)

        global currtime_label
        currtime_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=W)
        currtime_label.place(x=5,y=25)

        global remtime_label
        remtime_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=E)
        remtime_label.place(x=Width-90,y=25)

        global video_frame
        video_frame = CTkFrame(controlframe,height= 40,width= 0.25*Width,fg_color="#510723")
        video_frame.place(x=5,y=40)

        global video_name
        video_name = CTkLabel(video_frame,height= 50,width= 0.25*Width,text = VideoControls.vid_name,fg_color="#510723",font=("TImes",22),anchor= W)
        video_name.place(x=0,y=0)

        global backward_btn
        backward_btn = CTkButton(controlframe,text= "",image= VideoControls.img10,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=VideoControls.move_backward)
        backward_btn.place(x=(0.5*frame_width)-75,y=36)
        backward_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,backward_btn))
        backward_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,backward_btn))

        global play_btn
        play_btn = CTkButton(controlframe,text= "",image= VideoControls.img12,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=VideoControls.resume_or_play)
        play_btn.place(x=(0.5*frame_width)-38,y=20)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        global forward_btn
        forward_btn = CTkButton(controlframe,text= "",image= VideoControls.img11,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=VideoControls.move_forward)
        forward_btn.place(x=(0.5*frame_width)+26,y=36)
        forward_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,forward_btn))
        forward_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,forward_btn))

        global vol_btn
        vol_btn = CTkButton(controlframe,text= "",image= VideoControls.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=VideoControls.switch_vol)
        vol_btn.place(x=Width-145,y=40)

        global vol_bar
        vol_bar = CTkSlider(controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=VideoControls.set_volume)
        vol_bar.set(50)
        vol_bar.place(x= Width-115,y= 50)

        if VideoControls.playing:
            play_btn.configure(image = VideoControls.img13)
        else:
            play_btn.configure(image = VideoControls.img12)

        App.update()

        Window.bind('<Configure>',lambda Event: VideoControls.reconfigure_widgets(Event))
        Window.bind('<space>',VideoControls.spacebar)
        Window.bind('<Right>',VideoControls.right_arrow)
        Window.bind('<Left>',VideoControls.left_arrow)
        VideoControls.update_progress()

    def play_video(file_path,name,frame):
        global media_player

        media_player = vlc.MediaPlayer() 
        media = vlc.Media(file_path)
        media_player.set_media(media)
            
        media_player.set_hwnd(frame.winfo_id())
        media_player.play()

        VideoControls.vid_name = name
        VideoControls.playing = True

    def resume_or_play():
        if media_player.is_playing():
            play_btn.configure(image = VideoControls.img12)
            media_player.set_pause(1)
            VideoControls.playing = False
        else:
            play_btn.configure(image = VideoControls.img13)
            media_player.set_pause(0)
            VideoControls.playing = True
            VideoControls.update_progress()

    def set_volume(value):
        if VideoControls.vol_on:
            media_player.audio_set_volume(int(value))

    def switch_vol():
        if VideoControls.vol_on == True:
            vol_btn.configure(image= VideoControls.img4)
            VideoControls.vol_on = False
            media_player.audio_set_volume(0)
        else:
            vol_btn.configure(image= VideoControls.img3)
            VideoControls.vol_on = True
            value = vol_bar.get()
            media_player.audio_set_volume(int(value))

    def update_progress():
        while media_player.is_playing():
            if VideoControls.video_length == 0:
                VideoControls.video_length = media_player.get_length()
            
            value = media_player.get_position()*prog_width
            progressbar.set(value)
            currtime_label.configure(text = VideoControls.audio_duration((media_player.get_time()/1000)))
            rem = VideoControls.video_length - media_player.get_time()
            if rem > -1:
                remtime_label.configure(text = VideoControls.audio_duration((rem/1000)))
            App.update()

        # if not media_player.is_playing():
        #     App.after(500,VideoControls.update_progress)

    def move_forward():
        time = media_player.get_time() + 15000
        media_player.set_time(time)

    def move_backward():
        time = media_player.get_time() - 15000
        media_player.set_time(time)

    def minimize():
        controlframe.place(x=0,y=Height-25)
        resize.configure(image=VideoControls.img14,command=VideoControls.maximize)
        VideoControls.is_maxsize = False

    def maximize():
        App.update()
        controlframe.place(x=0,y=Height-80)
        resize.configure(image=VideoControls.img15,command=VideoControls.minimize)
        VideoControls.is_maxsize = True

    def move_video_progress(value):
        if VideoControls.video_length > 0:
            position = (value/prog_width)
            media_player.set_position(position)

    def reconfigure_widgets(Event):
        App.update()
        Height = Window.winfo_height()
        Width = Window.winfo_width()
        frame_width = Width - 10
        prog_width = frame_width-20

        Frame.configure(height=Height,width=Width)

        controlframe.configure(width=Width)
        if VideoControls.is_maxsize:
            controlframe.place(x=0,y=Height-80)
        else:
            controlframe.place(x=0,y=Height-25)

        progressbar.configure(from_=0,to=Width-30,width=Width-30)

        resize.place(x=Width-30,y=0)

        remtime_label.place(x=Width-90,y=25)

        video_frame.configure(width= 0.25*Width)
        video_name.configure(width= 0.25*Width)

        backward_btn.place(x=(0.5*frame_width)-75,y=36)     
        play_btn.place(x=(0.5*frame_width)-38,y=20)
        forward_btn.place(x=(0.5*frame_width)+26,y=36)

        vol_btn.place(x=Width-145,y=40)
        vol_bar.place(x= Width-115,y= 50)
        App.update()

    def spacebar(Event):
        try:
            VideoControls.resume_or_play()
        except:
            pass

    def right_arrow(Event):
        VideoControls.move_forward()

    def left_arrow(Event):
        VideoControls.move_backward()
    
    def stop_video():
        Window.unbind_all()
        media_player.stop()