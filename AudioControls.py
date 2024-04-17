from Controls import*
from customtkinter import*
from pygame import mixer,USEREVENT,event
from Extra import Extra
from mutagen.mp4 import MP4

class AudioControls(Control):
    def __init__(self,extra: Extra):
        self.favourite = False
        self.vol_on = True
        self.Id = ""
        self.Index = 0

        # init()
        mixer.init()
        mixer.music.set_volume(0.5)
        self.current_song_path = ""
        self.current_song_name = ""
        self.song_value = ""

        self.duration = 0
        self.current_time = 0
        self.added_time = 0

        self.Extra = extra

    def controls(self,home,app,database):
        self.Home = home

        self.App = app

        self.Database = database

        self.controlframe = CTkFrame(self.Home.frame,fg_color="#510723",height= 100,width=1020,corner_radius= 6)
        self.controlframe.place(x=5,y=495)

        self.progressbar = CTkSlider(self.controlframe,from_=0,to=1000,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=1000,state = 'disabled',command=self.move_progress)
        self.progressbar.set(1000)
        self.progressbar.place(x= 10,y= 5)

        self.r_label = CTkLabel(self.controlframe,text="00:00",fg_color="#510723",height=20,width=40,anchor=CENTER)
        self.r_label.place(x=970,y=25)

        self.msclabel = CTkLabel(self.controlframe,height= 70,width= 70,image= self.img5,text = '',fg_color=['gray86', 'gray17'],corner_radius= 4,anchor= CENTER)
        self.msclabel.place(x= 5,y= 25)

        self.song_frame = CTkFrame(self.controlframe,height= 40,width= 300,fg_color="#510723")
        self.song_frame.place(x=85,y=25)

        self.song_name = CTkLabel(self.song_frame,height= 40,width= 100,text = '',fg_color="#510723",font=("TImes",16),anchor= W)
        self.song_name.place(x=0,y=0)

        self.previous_btn = CTkButton(self.controlframe,text= "",image= self.img6,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.previous_btn.place(x=415,y=41)
        self.previous_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.previous_btn))
        self.previous_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.previous_btn))

        self.play_btn = CTkButton(self.controlframe,text= "",image= self.img7,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.play_btn.place(x=462,y=25)
        self.play_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.play_btn))
        self.play_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.play_btn))

        self.next_btn = CTkButton(self.controlframe,text= "",image= self.img9,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.next_btn.place(x=540,y=41)
        self.next_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.next_btn))
        self.next_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.next_btn))

        self.vol_btn = CTkButton(self.controlframe,text= "",image= self.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=self.switch_vol)
        self.vol_btn.place(x=830,y=55)

        self.vol_bar = CTkSlider(self.controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=self.set_vol)
        self.vol_bar.set(50)
        self.vol_bar.place(x= 860,y= 65)

        self.fav_btn = CTkButton(self.controlframe,text= "",image= self.img1,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=self.fav_song)
        self.fav_btn.place(x=975,y=55)
       

    def select_song(self,Event,file_path,file_name,id):
        self.Id = id
 
        # try:
        self.play_song(file_path,file_name)
        # except Exception as e:
        #     messagebox.showerror("Error",e)

    def play_song(self,file_path,file_name):
        self.song_value = f"{file_name}.mp3={file_path}"
        self.current_time = 0
        self.added_time = 0    

        try:
            index = self.Extra.All_songs.index(self.song_value)
            self.select_frame(index,self.Extra.song_frames)
        except:
            pass

        self.song_name.configure(text=file_name)

        self.current_song_path = file_path
        self.current_song_name = file_name
        try:
            length = mixer.Sound(self.current_song_path).get_length()
        except:
            length = MP4(self.current_song_path).info.length

        self.duration = length

        song = f"{file_name}={file_path}"
        if self.Id != "Recent":
            self.add_to_recent(song)

        if song in self.Extra.Favourites:
            if self.Id == "Favourites":
                index = self.Extra.Favourites.index(song)
                self.Index = index
                self.select_frame(index,self.Extra.Favourites_frames)

            self.fav_btn.configure(image=self.img2)
            self.favourite = True
        else:
            self.fav_btn.configure(image=self.img1)
            self.favourite = False

        if self.Id == "Recent":
            index = self.Extra.Recent.index(song)
            self.Index = index
            self.select_frame(index,self.Extra.Recent_frames)
        
        elif self.Id == "Playlist":
            index = self.Extra.current_playlist_songs_edit.index(f"{song.split('=')[0]}.mp3")
            self.Index = index
            self.select_frame(index,self.Extra.playlist_frames)

        self.play_btn.configure(image= self.img8)
        self.progressbar.configure(state = 'normal')
        mixer.music.load(self.current_song_path)
        mixer.music.play()

        self.MUSIC_END = USEREVENT + 1
        mixer.music.set_endevent(self.MUSIC_END)

        self.previous_btn.configure(command=self.previous_song)
        self.play_btn.configure(command= self.pause)
        self.next_btn.configure(command=self.next_song)
        self.update_progress()
    
    def get_index(self,song,list):
        for i in range(len(list)):
            if i == song:
                return i


    def pause(self):
        mixer.music.pause()

        self.play_btn.configure(command= self.resume)
        self.play_btn.configure(image= self.img7)

    def resume(self):
        mixer.music.unpause()

        self.play_btn.configure(command= self.pause)
        self.play_btn.configure(image= self.img8)
    
    def update_progress(self):
        while mixer.music.get_busy():
            self.current_time = mixer.music.get_pos()/1000
            time = self.current_time + self.added_time
            if time < 0:
                time = 0
                self.current_time = 0
                self.added_time = 0

            self.r_label.configure(text = self.audio_duration(time))
            self.progressbar.set(int(((time/self.duration)*1000)))
            self.App.update()

        if mixer.music.get_busy() == False:
            self.App.after(500,self.update_progress)

        for i in event.get():
            if i.type == self.MUSIC_END:
                self.end_song()

    def move_progress(self,value):
        self.current_time = mixer.music.get_pos()/1000
        x = (self.current_time/self.duration)* 1000
        self.added_time = (value - x)*(self.duration/1000)
        
        try:
            if self.added_time < 0:
                mixer.music.play()
                mixer.music.set_pos((self.current_time + self.added_time))

            else:
                mixer.music.set_pos(self.added_time)

        except :
            mixer.music.load(self.current_song_path)
            mixer.music.play()
            mixer.music.set_pos((self.current_time + self.added_time))

    def next_song(self):
        self.play_btn.configure(image= self.img8)

        if self.Id == "Songs":
            index = self.Extra.All_songs.index(self.song_value)
            if index != len(self.Extra.All_songs)-1:
                index = index + 1
            else:
                index = 0
            
            name = self.Extra.All_songs[index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            self.play_song(path,name)

        elif self.Id == "Favourites":
            self.select_next_song(self.Extra.Favourites)
            
        elif self.Id == "Recent":
            self.select_next_song(self.Extra.Recent)
        
        elif self.Id == "Playlist":
            self.select_next_song(self.Extra.current_playlist_songs)
            
    def select_next_song(self,song_list):
        if self.Index != len(song_list)-1:
                self.Index = self.Index + 1
        else:
            self.Index = 0
        
        name = song_list[self.Index]
        value = name.split('=')
        name = value[0].replace('.mp3','')
        path = value[1]

        self.play_song(path,name)


    def previous_song(self):
        if self.Id == "Songs":
            index = self.Extra.All_songs.index(self.song_value)
            if index != 0:
                index = index - 1
            else:
                index = len(self.Extra.All_songs)-1

            name = self.Extra.All_songs[index]
            value = name.split('=')
            name = value[0].replace('.mp3','')
            path = value[1]

            self.play_song(path,name)
        elif self.Id == "Favourites":
            self.select_previous_song(self.Extra.Favourites)
           
        elif self.Id == "Recent":
            self.select_previous_song(self.Extra.Recent)

        elif self.Id == "Playlist":
            self.select_previous_song(self.Extra.current_playlist_songs)

    def select_previous_song(self,song_list):
        if self.Index != 0:
                self.Index = self.Index - 1
        else:
            self.Index = len(song_list)-1
        
        name = song_list[self.Index]
        value = name.split('=')
        name = value[0].replace('.mp3','')
        path = value[1]

        self.play_song(path,name)

    def end_song(self):
        self.play_btn.configure(image= self.img8)
        self.next_song()

    def select_frame(self,index,frames):
        for i in frames:
            for x in i.winfo_children():
                x.configure(text_color = "white")

        frame = frames[index]
        for i in frame.winfo_children():
            i.configure(text_color = "#0967CC")

    def fav_song(self):
        if self.favourite == True:
            self.Database.del_favourites(self.current_song_name,self.Home)
            self.fav_btn.configure(image= self.img1)
            self.favourite = False
        else:
            self.Database.add_favourites(self.current_song_name,self.current_song_path,self.Home)
            self.fav_btn.configure(image= self.img2)
            self.favourite = True

    def switch_vol(self):
        if self.vol_on == True:
            self.configure(image= self.img4)
            self.vol_on = False
            mixer.music.set_volume(0)
        else:
            self.vol_btn.configure(image= self.img3)
            self.vol_on = True
            value = self.vol_bar.get()
            mixer.music.set_volume((value/100))

    def set_vol(self,value):
        if self.vol_on:
            mixer.music.set_volume((value/100))

    def add_to_recent(self,song):
        if song in self.Extra.Recent:
            index = self.Extra.Recent.index(song)
            self.Extra.Recent.pop(index)

        if len(self.Extra.Recent) > 9:
            self.Extra.Recent.pop(9)
        
        self.Extra.Recent.insert(0,song)
        self.Home.configure_rec_page()
    
    def stop(self):
        mixer.music.stop()

    def Youtube_mode(self):
        self.controlframe.place_forget()

    def Normal_mode(self):
        self.controlframe.place(x=5,y=495)



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