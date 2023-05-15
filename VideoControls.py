from Controls import*
from customtkinter import*
import vlc

class VideoControls(Control):
    vid_name = ''
    playing = True
    vol_on = True
    video_length = 0
    def controls(frame,app,window):
        global App
        App = app

        global Frame
        Frame = frame

        Height = window.winfo_height()
        Width = window.winfo_width()
        frame_width = Width - 10

        Y= Height-100

        controlframe = CTkFrame(window,fg_color="#510723",height= 100,width=Width,corner_radius= 6)
        controlframe.place(x=0,y=Y)

        global progressbar
        progressbar = CTkSlider(controlframe,from_=0,to=frame_width-20,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=Width-30)
        progressbar.set(Width-30)
        progressbar.place(x= 10,y= 5)

        global currtime_label
        currtime_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=W)
        currtime_label.place(x=10,y=25)

        global remtime_label
        remtime_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=E)
        remtime_label.place(x=Width-85,y=25)

        video_frame = CTkFrame(controlframe,height= 40,width= 0.25*Width,fg_color="#510723")
        video_frame.place(x=10,y=55)

        global video_name
        video_name = CTkLabel(video_frame,height= 50,width= 0.25*Width,text = VideoControls.vid_name,fg_color="#510723",font=("TImes",22),anchor= W)
        video_name.place(x=0,y=0)

        previous_btn = CTkButton(controlframe,text= "",image= VideoControls.img6,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        previous_btn.place(x=(0.5*frame_width)-85,y=41)
        previous_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,previous_btn))
        previous_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,previous_btn))

        global play_btn
        play_btn = CTkButton(controlframe,text= "",image= VideoControls.img7,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=VideoControls.resume_or_play)
        play_btn.place(x=(0.5*frame_width)-38,y=25)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        next_btn = CTkButton(controlframe,text= "",image= VideoControls.img9,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        next_btn.place(x=(0.5*frame_width)+40,y=41)
        next_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,next_btn))
        next_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,next_btn))

        global vol_btn
        vol_btn = CTkButton(controlframe,text= "",image= VideoControls.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=VideoControls.switch_vol)
        vol_btn.place(x=Width-145,y=55)

        global vol_bar
        vol_bar = CTkSlider(controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=VideoControls.set_volume)
        vol_bar.set(50)
        vol_bar.place(x= Width-115,y= 65)

        if VideoControls.playing:
            play_btn.configure(image = VideoControls.img8)
        else:
            play_btn.configure(image = VideoControls.img7)

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
        print(VideoControls.video_length)

    def resume_or_play():
        if media_player.is_playing():
            play_btn.configure(image = VideoControls.img7)
            media_player.set_pause(1)
            VideoControls.playing = False
        else:
            play_btn.configure(image = VideoControls.img8)
            media_player.set_pause(0)
            VideoControls.playing = True

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
            
            value = media_player.get_position()*1000
            progressbar.set(value)
            currtime_label.configure(text = VideoControls.audio_duration((media_player.get_time()/1000)))
            rem = VideoControls.video_length - media_player.get_time()
            if rem > -1:
                remtime_label.configure(text = VideoControls.audio_duration((rem/1000)))
            App.update()

        if not media_player.is_playing():
            App.after(500,VideoControls.update_progress)