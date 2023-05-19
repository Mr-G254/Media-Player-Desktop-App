from Controls import*
from customtkinter import*
from pygame import mixer,USEREVENT,event,init
# from Database import 

class AudioControls(Control):
    favourite = False
    vol_on = True
    Id = ""
    Index = 0

    # init()
    mixer.init()
    mixer.music.set_volume(0.5)
    current_song_path = ""
    current_song_name = ""
    song_value = ""

    duration = 0
    current_time = 0
    added_time = 0

    def controls(home,app,database):
        global Home
        Home = home

        global App
        App = app

        global Database
        Database = database

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
        AudioControls.play_song(file_path,file_name)

    def play_song(file_path,file_name):
        AudioControls.song_value = f"{file_name}.mp3={file_path}"
        AudioControls.current_time = 0
        AudioControls.added_time = 0    

        try:
            index = Extra.All_songs.index(AudioControls.song_value)
            AudioControls.select_frame(index,Extra.song_frames)
        except:
            pass

        song_name.configure(text=file_name)

        AudioControls.current_song_path = file_path
        AudioControls.current_song_name = file_name
        length = mixer.Sound(AudioControls.current_song_path).get_length()
        AudioControls.duration = length

        
        song = f"{file_name}={file_path}"
        if song in Extra.E_favourites:
            if AudioControls.Id == "Favourites":
                index = Extra.E_favourites.index(song)
                AudioControls.Index = index
                AudioControls.select_frame(index,Extra.Favourites_frames)

            fav_btn.configure(image=AudioControls.img2)
            AudioControls.favourite = True
        else:
            fav_btn.configure(image=AudioControls.img1)
            AudioControls.favourite = False

        play_btn.configure(image= AudioControls.img8)
        progressbar.configure(state = 'normal')
        mixer.music.load(AudioControls.current_song_path)
        mixer.music.play()

        global MUSIC_END
        MUSIC_END = USEREVENT + 1
        mixer.music.set_endevent(MUSIC_END)

        previous_btn.configure(command=AudioControls.previous_song)
        play_btn.configure(command= AudioControls.pause)
        next_btn.configure(command=AudioControls.next_song)
        AudioControls.update_progress()
    
    def get_index(song,list):
        for i in range(len(list)):
            if i == song:
                return i


    def pause():
        mixer.music.pause()

        play_btn.configure(command= AudioControls.resume)
        play_btn.configure(image= AudioControls.img7)

    def resume():
        mixer.music.unpause()

        play_btn.configure(command= AudioControls.pause)
        play_btn.configure(image= AudioControls.img8)
    
    def update_progress():
        while mixer.music.get_busy():
            AudioControls.current_time = mixer.music.get_pos()/1000
            time = AudioControls.current_time + AudioControls.added_time
            if time < 0:
                time = 0
                AudioControls.current_time = 0
                AudioControls.added_time = 0

            r_label.configure(text = AudioControls.audio_duration(time))
            progressbar.set(int(((time/AudioControls.duration)*1000)))
            App.update()

        if mixer.music.get_busy() == False:
            App.after(500,AudioControls.update_progress)

        for i in event.get():
            if i.type == MUSIC_END:
                AudioControls.end_song()

    def move_progress(value):
        AudioControls.current_time = mixer.music.get_pos()/1000
        x = (AudioControls.current_time/AudioControls.duration)* 1000
        AudioControls.added_time = (value - x)*(AudioControls.duration/1000)
        
        try:
            if AudioControls.added_time < 0:
                mixer.music.play()
                mixer.music.set_pos((AudioControls.current_time + AudioControls.added_time))

            else:
                mixer.music.set_pos(AudioControls.added_time)

        except :
            mixer.music.load(AudioControls.current_song_path)
            mixer.music.play()
            mixer.music.set_pos((AudioControls.current_time + AudioControls.added_time))

    def next_song():
        play_btn.configure(image= AudioControls.img8)

        if AudioControls.Id == "Songs":
            index = Extra.All_songs.index(AudioControls.song_value)
            if index != len(Extra.All_songs)-1:
                index = index + 1
            else:
                index = 0
            
            name = Extra.All_songs[index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            AudioControls.play_song(path,name)

        elif AudioControls.Id == "Favourites":
            
            if AudioControls.Index != len(Extra.E_favourites)-1:
                AudioControls.Index = AudioControls.Index + 1
            else:
                AudioControls.Index = 0
            
            name = Extra.E_favourites[AudioControls.Index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            AudioControls.play_song(path,name)

    def previous_song():
        if AudioControls.Id == "Songs":
            index = Extra.All_songs.index(AudioControls.song_value)
            if index != 0:
                index = index - 1
            else:
                index = len(Extra.All_songs)-1

            name = Extra.All_songs[index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            AudioControls.play_song(path,name)
        elif AudioControls.Id == "Favourites":
            if AudioControls.Index != 0:
                AudioControls.Index = AudioControls.Index - 1
            else:
                AudioControls.Index = len(Extra.E_favourites)-1
            
            name = Extra.E_favourites[AudioControls.Index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            AudioControls.play_song(path,name)

    def end_song():
        play_btn.configure(image= AudioControls.img8)
        AudioControls.next_song()

    def select_frame(index,frames):
        for i in frames:
            for x in i.winfo_children():
                x.configure(text_color = "white")

        frame = frames[index]
        for i in frame.winfo_children():
            i.configure(text_color = "#0967CC")

    def fav_song():
        if AudioControls.favourite == True:
            Database.del_favourites(AudioControls.current_song_name,Home)
            fav_btn.configure(image= AudioControls.img1)
            AudioControls.favourite = False
        else:
            Database.add_favourites(AudioControls.current_song_name,AudioControls.current_song_path,Home)
            fav_btn.configure(image= AudioControls.img2)
            AudioControls.favourite = True

    def switch_vol():
        if AudioControls.vol_on == True:
            vol_btn.configure(image= AudioControls.img4)
            AudioControls.vol_on = False
            mixer.music.set_volume(0)
        else:
            vol_btn.configure(image= AudioControls.img3)
            AudioControls.vol_on = True
            value = vol_bar.get()
            mixer.music.set_volume((value/100))

    def set_vol(value):
        if AudioControls.vol_on:
            mixer.music.set_volume((value/100))