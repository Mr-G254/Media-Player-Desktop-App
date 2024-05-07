from Controls import*
from customtkinter import*
from pygame import mixer,USEREVENT,event
from Extra import Extra
from mutagen.mp4 import MP4
from random import randint

class AudioControls(Control):
    def __init__(self,extra: Extra):
        self.favourite = False
        self.vol_on = True
        self.Id = ""
        self.Index = 0
        self.on_start = True

        mixer.init()
        mixer.music.set_volume(0.5)
        self.current_song_path = ""
        self.current_song_name = ""
        self.song_value = ""
        self.shuffle = False
        # self.current_song_list = []

        self.duration = 0
        self.current_time = 0
        self.added_time = 0

        self.Extra = extra

        self.loop = False
        self.shuffle = False
        self.loop_end = False

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

        self.song_frame = CTkFrame(self.controlframe,height= 35,width= 300,fg_color="#510723")
        self.song_frame.place(x=85,y=25)

        self.song_name = CTkLabel(self.song_frame,height= 35,width= 100,text = '',fg_color="#510723",font=("TImes",16),anchor= W)
        self.song_name.place(x=0,y=0)

        self.shuffle_btn = CTkButton(self.controlframe,text= "",image= self.img16a,height= 25,width=25,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.shuffle_songs)
        self.shuffle_btn.place(x=380,y=50)

        self.previous_btn = CTkButton(self.controlframe,text= "",image= self.img6a,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.previous_btn.place(x=415,y=41)
        self.previous_btn.bind('<Enter>',lambda Event: self.Extra.highlightControls(Event,self.previous_btn,self.img6b))
        self.previous_btn.bind('<Leave>',lambda Event: self.Extra.unhighlightControls(Event,self.previous_btn,self.img6a))

        self.play_btn = CTkButton(self.controlframe,text= "",image= self.img7a,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.play_btn.place(x=462,y=25)

        self.iconNorm = self.img7a
        self.iconHighlight = self.img7b
        self.play_btn.bind('<Enter>',lambda Event: self.Extra.highlightControls(Event,self.play_btn,self.iconHighlight))
        self.play_btn.bind('<Leave>',lambda Event: self.Extra.unhighlightControls(Event,self.play_btn,self.iconNorm))

        self.next_btn = CTkButton(self.controlframe,text= "",image= self.img9a,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        self.next_btn.place(x=535,y=41)
        self.next_btn.bind('<Enter>',lambda Event: self.Extra.highlightControls(Event,self.next_btn,self.img9b))
        self.next_btn.bind('<Leave>',lambda Event: self.Extra.unhighlightControls(Event,self.next_btn,self.img9a))

        self.loop_btn = CTkButton(self.controlframe,text= "",image= self.img17a,height= 25,width=25,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.loop_songs)
        self.loop_btn.place(x=585,y=50)

        self.vol_btn = CTkButton(self.controlframe,text= "",image= self.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=self.switch_vol)
        self.vol_btn.place(x=830,y=55)

        self.vol_bar = CTkSlider(self.controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=self.set_vol)
        self.vol_bar.set(50)
        self.vol_bar.place(x= 860,y= 65)

        self.fav_btn = CTkButton(self.controlframe,text= "",image= self.img1,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=self.fav_song)
        self.fav_btn.place(x=975,y=55)

        try:
            self.restore_last_song()
        except:
            pass

    def restore_last_song(self):
        try:
            song = self.Extra.Recent[0]
        except:
            song = self.Extra.All_songs[0]

        values = song.split("=")
        name = values[0].split(".")[0]
        path = values[1]
        self.Id = "Songs"
        
        self.song_name.configure(text=name)
        self.play_btn.configure(command=lambda: self.play_song(path,name))
       

    def select_song(self,Event,file_path,file_name,id):
        self.Id = id
 
        self.play_song(file_path,file_name)


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
                self.current_song_list = self.Extra.Favourites
                self.current_played_song_list = self.Extra.Favourites_played_songs
                index = self.Extra.Favourites.index(song)
                self.Index = index
                self.select_frame(index,self.Extra.Favourites_frames)

            self.fav_btn.configure(image=self.img2)
            self.favourite = True
        else:
            self.fav_btn.configure(image=self.img1)
            self.favourite = False

        if self.Id == "Recent":
            self.current_song_list = self.Extra.Recent
            self.current_played_song_list = self.Extra.Recent_played_songs
            index = self.Extra.Recent.index(song)
            self.Index = index
            self.select_frame(index,self.Extra.Recent_frames)
        
        elif self.Id == "Playlist":
            self.current_song_list = self.Extra.Playlist
            self.current_played_song_list = self.Extra.current_playlist_played_songs
            index = self.Extra.current_playlist_songs_edit.index(f"{song.split('=')[0]}.mp3")
            self.Index = index
            self.select_frame(index,self.Extra.playlist_frames)

        elif self.Id == "Songs":
            self.current_song_list = self.Extra.All_songs
            self.current_played_song_list = self.Extra.All_songs_played

        if f"{self.current_song_name}.mp3={self.current_song_path}" not in self.current_played_song_list:
            self.current_played_song_list.append(f"{self.current_song_name}.mp3={self.current_song_path}")

        self.iconNorm = self.img8a
        self.iconHighlight = self.img8b
        self.play_btn.configure(image= self.iconNorm)
        self.progressbar.configure(state = 'normal')
        mixer.music.unload()
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

        self.iconNorm = self.img7a
        self.iconHighlight = self.img7b
        self.play_btn.configure(command= self.resume)

        if self.loop_end:
            self.play_btn.configure(image= self.iconNorm)
        else:
            self.play_btn.configure(image= self.iconHighlight)

    def resume(self):
        if self.loop_end:
            self.play_song(self.current_song_path,self.current_song_name)
        else:
            mixer.music.unpause()

            self.iconNorm = self.img8a
            self.iconHighlight = self.img8b
            self.play_btn.configure(image= self.iconHighlight)
            self.play_btn.configure(command= self.pause)
            self.play_btn.configure(image= self.iconHighlight)
            
    
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

        if self.Id == "Songs":
            self.current_song_list = self.Extra.All_songs
            self.current_played_song_list = self.Extra.All_songs_played

            index = 0
            if self.shuffle:
                index = self.get_random_index()
            else:
                try:
                    index = self.Extra.All_songs.index(self.song_value)
                except:
                    for i in self.Extra.All_songs:
                        if i.startswith(self.song_value.split("=")[0].split(".")[0]):
                            index = self.current_song_list.index(i)
                            break

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
            self.current_song_list = self.Extra.Favourites
            self.current_played_song_list = self.Extra.Favourites_played_songs
            self.select_next_song(self.Extra.Favourites)
            
        elif self.Id == "Recent":
            self.current_song_list = self.Extra.Recent
            self.current_played_song_list = self.Extra.Recent_played_songs
            self.select_next_song(self.Extra.Recent)
        
        elif self.Id == "Playlist":
            self.current_song_list = self.Extra.current_playlist_songs
            self.current_played_song_list = self.Extra.current_playlist_played_songs
            self.select_next_song(self.Extra.current_playlist_songs)
            
    def select_next_song(self,song_list):
        if self.shuffle:
            self.Index = self.get_random_index()
        else:
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
            self.current_song_list = self.Extra.All_songs
            self.current_played_song_list = self.Extra.All_songs_played

            if self.shuffle:
                indx = self.current_played_song_list.index(f"{self.current_song_name}.mp3={self.current_song_path}")

                if indx > 0:
                    song = self.current_played_song_list[indx - 1]
                    index = self.Extra.All_songs.index(song)
                else:
                    index = self.get_random_index()

            else:
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
            self.current_song_list = self.Extra.Favourites
            self.current_played_song_list = self.Extra.Favourites_played_songs
            self.select_previous_song(self.Extra.Favourites)
           
        elif self.Id == "Recent":
            self.current_song_list = self.Extra.Recent
            self.current_played_song_list = self.Extra.Recent_played_songs
            self.select_previous_song(self.Extra.Recent)

        elif self.Id == "Playlist":
            self.current_song_list = self.Extra.current_playlist_songs
            self.current_played_song_list = self.Extra.current_playlist_played_songs
            self.select_previous_song(self.Extra.current_playlist_songs)

    def select_previous_song(self,song_list):
        self.current_song_list = song_list

        if self.shuffle:
            indx = self.current_played_song_list.index(f"{self.current_song_name}.mp3={self.current_song_path}")

            if indx > 0:
                song = self.current_played_song_list[indx - 1]

                try:
                    self.Index = self.current_song_list.index(song)
                except:

                    for i in self.current_song_list:
                        if i.startswith(song.split("=")[0].split(".")[0]):
                            self.Index = self.current_song_list.index(i)
                            break

            else:
                self.Index = self.get_random_index()
        else:
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
        self.iconNorm = self.img8a
        self.iconHighlight = self.img8b
        self.play_btn.configure(image= self.iconNorm)

        if self.shuffle:
            index = self.get_random_index()
        
        else:
            try:
                index = self.current_song_list.index(self.song_value)
            except:
                for i in self.current_song_list:
                    if i.startswith(self.song_value.split("=")[0].split(".")[0]):
                        index = self.current_song_list.index(i)
                        break

        if index == len(self.current_song_list)-1:
            if self.loop == True:
                self.loop_end = False
                self.next_song()
            else:
                self.loop_end = True
                self.pause()
        
        else:
            self.loop_end = False
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

            if len(self.current_song_name) > 0:
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

    def loop_songs(self):
        if self.loop:
            self.loop = False
            self.loop_btn.configure(image=self.img17a)
        else:
            self.loop = True
            self.loop_btn.configure(image=self.img17b)

    def shuffle_songs(self):
        if self.shuffle == False:
            self.shuffle = True
            self.shuffle_btn.configure(image= self.img16b)
        else:
            self.shuffle = False
            self.shuffle_btn.configure(image= self.img16a)
            self.current_played_song_list.clear()

    def get_random_index(self):
        index = 0
        if len(self.current_song_list) == len(self.current_played_song_list):
            self.current_played_song_list.clear()

            if self.loop == False:
                index = len(self.current_song_list) - 1
            else:
                self.get_random_index()

        else:
            index = randint(0,len(self.current_song_list)-1)

            while self.current_song_list[index] in self.current_played_song_list:
                index = randint(0,len(self.current_song_list)-1)
            
            # self.current_played_song_list.append(self.current_song_list[index])

        return index





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