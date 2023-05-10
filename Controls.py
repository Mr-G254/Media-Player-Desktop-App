from customtkinter import*
from PIL import Image
from Extra import*
from pygame import mixer,USEREVENT,event,init

class Controls():
    img1 = CTkImage(Image.open("Icons\hearta.png"),size=(24,24))
    img2 = CTkImage(Image.open("Icons\heartb.png"),size=(24,24))
    img3 = CTkImage(Image.open("Icons\\volume.png"),size=(26,26))
    img4 = CTkImage(Image.open("Icons\\volume-mute.png"),size=(26,26))
    img5 = CTkImage(Image.open("Icons\music.png"),size=(24,24))
    img6 = CTkImage(Image.open("Icons\previous-button.png"),size=(32,32))
    img7 = CTkImage(Image.open("Icons\play.png"),size=(64,64))
    img8 = CTkImage(Image.open("Icons\pause.png"),size=(62,62))
    img9 = CTkImage(Image.open("Icons\\next-button.png"),size=(32,32))

    favourite = False
    vol_on = True

    init()
    mixer.init()
    mixer.music.set_volume(0.5)
    current_song = ""
    song_value = ""

    duration = 0
    current_time = 0
    added_time = 0

    def controls(frame,app):
        global App
        App = app

        controlframe = CTkFrame(frame,fg_color="#510723",height= 100,width=1020,corner_radius= 6)
        controlframe.place(x=5,y=495)

        global progressbar
        progressbar = CTkSlider(controlframe,from_=0,to=1000,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=1000,state = 'disabled',command=Controls.move_progress)
        progressbar.set(1000)
        progressbar.place(x= 10,y= 5)

        global r_label
        r_label = CTkLabel(controlframe,text="00:00",fg_color="#510723",height=20,width=40,anchor=CENTER)
        r_label.place(x=970,y=25)

        msclabel = CTkLabel(controlframe,height= 70,width= 70,image= Controls.img5,text = '',fg_color=['gray86', 'gray17'],corner_radius= 4,anchor= CENTER)
        msclabel.place(x= 5,y= 25)

        song_frame = CTkFrame(controlframe,height= 40,width= 300,fg_color="#510723")
        song_frame.place(x=85,y=25)

        global song_name
        song_name = CTkLabel(song_frame,height= 40,width= 100,text = '',fg_color="#510723",font=("TImes",16),anchor= W)
        song_name.place(x=0,y=0)

        previous_btn = CTkButton(controlframe,text= "",image= Controls.img6,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=Controls.previous_song)
        previous_btn.place(x=415,y=41)
        previous_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,previous_btn))
        previous_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,previous_btn))

        global play_btn
        play_btn = CTkButton(controlframe,text= "",image= Controls.img7,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        play_btn.place(x=462,y=25)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        next_btn = CTkButton(controlframe,text= "",image= Controls.img9,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=Controls.next_song)
        next_btn.place(x=540,y=41)
        next_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,next_btn))
        next_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,next_btn))

        global vol_btn
        vol_btn = CTkButton(controlframe,text= "",image= Controls.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=Controls.switch_vol)
        vol_btn.place(x=830,y=55)

        global vol_bar
        vol_bar = CTkSlider(controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=Controls.set_vol)
        vol_bar.set(50)
        vol_bar.place(x= 860,y= 65)

        global fav_btn
        fav_btn = CTkButton(controlframe,text= "",image= Controls.img1,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=Controls.fav_song)
        fav_btn.place(x=975,y=55)
       

    def select_song(Event,file_path,file_name):
        Controls.play_song(file_path,file_name)

    def play_song(file_path,file_name):
        Controls.song_value = f"{file_name}.mp3={file_path}"
        Controls.current_time = 0
        Controls.added_time = 0

        index = Extra.All_songs.index(Controls.song_value)
        Controls.select_frame(index)

        song_name.configure(text=file_name)

        Controls.current_song = file_path
        length = mixer.Sound(Controls.current_song).get_length()
        Controls.duration = length

        play_btn.configure(image= Controls.img8)
        progressbar.configure(state = 'normal')
        mixer.music.load(Controls.current_song)
        mixer.music.play()

        global MUSIC_END
        MUSIC_END = USEREVENT + 1
        mixer.music.set_endevent(MUSIC_END)

        play_btn.configure(command= Controls.pause)
        Controls.update_progress()

    def pause():
        mixer.music.pause()

        play_btn.configure(command= Controls.resume)
        play_btn.configure(image= Controls.img7)

    def resume():
        mixer.music.unpause()

        play_btn.configure(command= Controls.pause)
        play_btn.configure(image= Controls.img8)

    def audio_duration(length):
        hours = int(length // 3600)  
        length %= 3600
        mins = int(length // 60)  
        length %= 60
        seconds = int(length)  

        if hours == 0:
            return(f"{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")
        else:
            return(f"{str(hours).rjust(2,'0')}:{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")
    
    def update_progress():
        while mixer.music.get_busy():
            Controls.current_time = mixer.music.get_pos()/1000
            time = Controls.current_time + Controls.added_time
            if time < 0:
                time = 0
                Controls.current_time = 0
                Controls.added_time = 0

            r_label.configure(text = Controls.audio_duration(time))
            progressbar.set(int(((time/Controls.duration)*1000)))
            App.update()

        if mixer.music.get_busy() == False:
            App.after(500,Controls.update_progress)

        for i in event.get():
            if i.type == MUSIC_END:
                Controls.end_song()

    def move_progress(value):
        Controls.current_time = mixer.music.get_pos()/1000
        x = (Controls.current_time/Controls.duration)* 1000
        Controls.added_time = (value - x)*(Controls.duration/1000)
        
        try:
            if Controls.added_time < 0:
                mixer.music.play()
                mixer.music.set_pos((Controls.current_time + Controls.added_time))

            else:
                mixer.music.set_pos(Controls.added_time)

        except :
            mixer.music.load(Controls.current_song)
            mixer.music.play()
            mixer.music.set_pos((Controls.current_time + Controls.added_time))

    def next_song():
        play_btn.configure(image= Controls.img8)
        index = Extra.All_songs.index(Controls.song_value)
        if index != len(Extra.All_songs)-1:
            Controls.select_frame(index+1)
           
            name = Extra.All_songs[index+1]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            Controls.play_song(path,name)

    def previous_song():
        index = Extra.All_songs.index(Controls.song_value)
        if index != 0:
            name = Extra.All_songs[index-1]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            Controls.play_song(path,name)

    def end_song():
        play_btn.configure(image= Controls.img8)
        Controls.next_song()

    def select_frame(index):
        for i in Extra.song_frames:
            for x in i.winfo_children():
                x.configure(text_color = "white")

        frame = Extra.song_frames[index]
        for i in frame.winfo_children():
            i.configure(text_color = "#0967CC")

    def fav_song():
        if Controls.favourite == True:
            fav_btn.configure(image= Controls.img1)
            Controls.favourite = False
        else:
            fav_btn.configure(image= Controls.img2)
            Controls.favourite = True

    def switch_vol():
        if Controls.vol_on == True:
            vol_btn.configure(image= Controls.img4)
            Controls.vol_on = False
            mixer.music.set_volume(0)
        else:
            vol_btn.configure(image= Controls.img3)
            Controls.vol_on = True
            value = vol_bar.get()
            mixer.music.set_volume((value/100))

    def set_vol(value):
        if Controls.vol_on:
            mixer.music.set_volume((value/100))