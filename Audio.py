from Controls import*
from customtkinter import*
import vlc
# from pygame import mixer,USEREVENT,event

class Audio(Control):
    favourite = False
    vol_on = True
    Id = ""
    Index = 0
    vid_name = ''
    playing = True
    vol_on = True
    video_length = 0

    

    def controls(home,app,database):
        global Home
        Home = home

        global App
        App = app

        global Database
        Database = database

        global controlframe
        controlframe = CTkFrame(Home.frame,fg_color="#510723",height= 100,width=1020,corner_radius= 6)
        controlframe.place(x=5,y=495)

        global progressbar
        progressbar = CTkSlider(controlframe,from_=0,to=1000,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=1000,state = 'disabled',command=AudioControls.move_progress)
        progressbar.set(1000)
        progressbar.place(x= 10,y= 5)

        global r_label
        r_label = CTkLabel(controlframe,text="00:00",fg_color="#510723",height=20,width=40,anchor=CENTER)
        r_label.place(x=970,y=25)

        msclabel = CTkLabel(controlframe,height= 70,width= 70,image= AudioControls.img5,text = '',fg_color=['gray86', 'gray17'],corner_radius= 4,anchor= CENTER)
        msclabel.place(x= 5,y= 25)

        song_frame = CTkFrame(controlframe,height= 40,width= 300,fg_color="#510723")
        song_frame.place(x=85,y=25)

        global song_name
        song_name = CTkLabel(song_frame,height= 40,width= 100,text = '',fg_color="#510723",font=("TImes",16),anchor= W)
        song_name.place(x=0,y=0)

        global previous_btn
        previous_btn = CTkButton(controlframe,text= "",image= AudioControls.img6,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        previous_btn.place(x=415,y=41)
        previous_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,previous_btn))
        previous_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,previous_btn))

        global play_btn
        play_btn = CTkButton(controlframe,text= "",image= AudioControls.img7,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        play_btn.place(x=462,y=25)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        global next_btn
        next_btn = CTkButton(controlframe,text= "",image= AudioControls.img9,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        next_btn.place(x=540,y=41)
        next_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,next_btn))
        next_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,next_btn))

        global vol_btn
        vol_btn = CTkButton(controlframe,text= "",image= AudioControls.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=AudioControls.switch_vol)
        vol_btn.place(x=830,y=55)

        global vol_bar
        vol_bar = CTkSlider(controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=AudioControls.set_vol)
        vol_bar.set(50)
        vol_bar.place(x= 860,y= 65)

        global fav_btn
        fav_btn = CTkButton(controlframe,text= "",image= AudioControls.img1,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=AudioControls.fav_song)
        fav_btn.place(x=975,y=55)
       

    def select_song(Event,file_path,file_name,id):
        AudioControls.Id = id
 
        # try:
        AudioControls.play_song(file_path,file_name)
        # except Exception as e:
        #     messagebox.showerror("Error",e)

    def play_video(file_path,name,frame):
        global media_player

        media_player = vlc.MediaPlayer() 
        media = vlc.Media(file_path)
        media_player.set_media(media)
            
        media_player.set_hwnd(frame.winfo_id())
        media_player.play()

        Audio.vid_name = name
        Audio.playing = True

    def resume_or_play():
        if media_player.is_playing():
            play_btn.configure(image = Audio.img12)
            try:
                media_player.set_pause(1)
            except Exception as e:
                messagebox.showerror("Error",e)

            Audio.playing = False
        else:
            play_btn.configure(image = Audio.img13)
            try:
                media_player.set_pause(0)
            except Exception as e:
                messagebox.showerror("Error",e)

            Audio.playing = True
            # Audio.update_progress()

    def set_volume(value):
        if Audio.vol_on:
            media_player.audio_set_volume(int(value))

    def switch_vol():
        if Audio.vol_on == True:
            vol_btn.configure(image= Audio.img4)
            Audio.vol_on = False
            media_player.audio_set_volume(0)
        else:
            vol_btn.configure(image= Audio.img3)
            Audio.vol_on = True
            value = vol_bar.get()
            media_player.audio_set_volume(int(value))

    def update_progress():
        while media_player.is_playing():
            if Audio.video_length == 0:
                Audio.video_length = media_player.get_length()
            
            value = media_player.get_position()*prog_width
            progressbar.set(value)
            currtime_label.configure(text = Audio.audio_duration((media_player.get_time()/1000)))
            rem = Audio.video_length - media_player.get_time()
            if rem > -1:
                remtime_label.configure(text = Audio.audio_duration((rem/1000)))
            App.update()

        if not media_player.is_playing():
            App.after(500,Audio.update_progress)

    def move_forward():
        time = media_player.get_time() + 15000
        media_player.set_time(time)

    def move_backward():
        time = media_player.get_time() - 15000
        media_player.set_time(time)

   

    def move_video_progress(value):
        if Audio.video_length > 0:
            position = (value/1000)
            media_player.set_position(position)