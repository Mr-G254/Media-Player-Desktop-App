from Controls import*
from customtkinter import*
import vlc
from tkinter import messagebox
from Extra import Extra

class VideoControls(Control):
    def __init__(self,extra: Extra):
        self.vid_name = ''
        self.playing = True
        self.vol_on = True
        self.video_length = 0
        self.is_maxsize = True

        self.Extra = extra

    def controls(self,frame,app,window):
        self.App = app

        self.Frame = frame

        self.Window = window
        
        self.Height = window.winfo_screenheight()

        self.Width = window.winfo_screenwidth()

        self.frame_width = self.Width - 10

        self.prog_width = self.frame_width-20

        self.controlframe = CTkFrame(window,fg_color="#510723",height= 90,width=self.Width,corner_radius= 6)
        self.controlframe.place(x=0,y=self.Height-105)

        self.progressbar = CTkSlider(self.controlframe,from_=0,to=self.frame_width-20,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=self.Width-30,command=self.move_video_progress)
        self.progressbar.set(self.Width-30)
        self.progressbar.place(x= 5,y= 5)

        self.resize = CTkButton(self.controlframe,text='',image=self.img15,height=25,width=25,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.minimize)
        self.resize.place(x=self.Width-30,y=0)

        self.currtime_label = CTkLabel(self.controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=W)
        self.currtime_label.place(x=5,y=25)

        self.remtime_label = CTkLabel(self.controlframe,text="00:00:00",fg_color="#510723",height=20,width=60,anchor=E)
        self.remtime_label.place(x=self.Width-90,y=25)

        self.video_frame = CTkFrame(self.controlframe,height= 40,width= 0.25*self.Width,fg_color="#510723")
        self.video_frame.place(x=5,y=40)

        self.video_name = CTkLabel(self.video_frame,height= 50,width= 0.25*self.Width,text = self.vid_name,fg_color="#510723",font=("TImes",22),anchor= W)
        self.video_name.place(x=0,y=0)

        self.backward_btn = CTkButton(self.controlframe,text= "",image= self.img10,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.move_backward)
        self.backward_btn.place(x=(0.5*self.frame_width)-75,y=36)
        # self.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.backward_btn))
        self.backward_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.backward_btn))

        self.play_btn = CTkButton(self.controlframe,text= "",image= self.img12,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.resume_or_play)
        self.play_btn.place(x=(0.5*self.frame_width)-38,y=20)
        self.play_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.play_btn))
        self.play_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.play_btn))

        self.forward_btn = CTkButton(self.controlframe,text= "",image= self.img11,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command=self.move_forward)
        self.forward_btn.place(x=(0.5*self.frame_width)+26,y=36)
        self.forward_btn.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.forward_btn))
        self.forward_btn.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.forward_btn))

        self.vol_btn = CTkButton(self.controlframe,text= "",image= self.img3,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=self.switch_vol)
        self.vol_btn.place(x=self.Width-145,y=40)

        self.vol_bar = CTkSlider(self.controlframe,from_=0,to=100,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=100,command=self.set_volume)
        self.vol_bar.set(50)
        self.vol_bar.place(x= self.Width-115,y= 50)

        if self.playing:
            self.play_btn.configure(image = self.img13)
        else:
            self.play_btn.configure(image = self.img12)

        self.App.update()

        # Window.bind('<Configure>',lambda Event: self.reconfigure_widgets(Event))
        # self.Window.resizable(False,False)
        self.Window.bind('<space>',self.spacebar)
        self.Window.bind('<Right>',self.right_arrow)
        self.Window.bind('<Left>',self.left_arrow)
        self.update_progress()

    def play_video(self,file_path,name,frame):

        self.media_player = vlc.MediaPlayer() 
        self.media = vlc.Media(file_path)
        self.media_player.set_media(self.media)
            
        self.media_player.set_hwnd(frame.winfo_id())
        self.media_player.play()

        self.vid_name = name
        self.playing = True

    def resume_or_play(self):
        if self.media_player.is_playing():
            self.play_btn.configure(image = self.img12)
            try:
                self.media_player.set_pause(1)
            except Exception as e:
                messagebox.showerror("Error",e)

            self.playing = False
        else:
            self.play_btn.configure(image = self.img13)
            try:
                self.media_player.set_pause(0)
            except Exception as e:
                messagebox.showerror("Error",e)

            self.playing = True
            # self.update_progress()

    def set_volume(self,value):
        if self.vol_on:
            self.media_player.audio_set_volume(int(value))

    def switch_vol(self):
        if self.vol_on == True:
            self.vol_btn.configure(image= self.img4)
            self.vol_on = False
            self.media_player.audio_set_volume(0)
        else:
            self.vol_btn.configure(image= self.img3)
            self.vol_on = True
            value = self.vol_bar.get()
            self.media_player.audio_set_volume(int(value))

    def update_progress(self):
        while self.media_player.is_playing():
            if self.video_length == 0:
                self.video_length = self.media_player.get_length()
            
            value = self.media_player.get_position()*self.prog_width
            self.progressbar.set(value)
            self.currtime_label.configure(text = self.audio_duration((self.media_player.get_time()/1000)))
            rem = self.video_length - self.media_player.get_time()
            if rem > -1:
                self.remtime_label.configure(text = self.audio_duration((rem/1000)))
            self.App.update()

        if not self.media_player.is_playing():
            self.App.after(500,self.update_progress)

    def move_forward(self):
        time = self.media_player.get_time() + 15000
        self.media_player.set_time(time)

    def move_backward(self):
        time = self.media_player.get_time() - 15000
        self.media_player.set_time(time)

    def minimize(self):
        self.controlframe.place(x=0,y=self.Height-50)
        self.resize.configure(image=self.img14,command=self.maximize)
        self.is_maxsize = False

    def maximize(self):
        self.App.update()
        self.controlframe.place(x=0,y=self.Height-105)
        self.resize.configure(image=self.img15,command=self.minimize)
        self.is_maxsize = True

    def move_video_progress(self,value):
        if self.video_length > 0:
            position = (value/self.prog_width)
            self.media_player.set_position(position)

    def reconfigure_widgets(self,Event):
        self.App.update()
        Height = self.Window.winfo_screenheight()
        Width = self.Window.winfo_screenwidth()
        frame_width = Width - 10
        self.prog_width = frame_width-20

        self.Frame.configure(height=Height,width=Width)

        self.controlframe.configure(width=Width)
        if self.is_maxsize:
            self.controlframe.place(x=0,y=Height-80)
        else:
            self.controlframe.place(x=0,y=Height-25)

        self.progressbar.configure(from_=0,to=Width-30,width=Width-30)

        self.resize.place(x=Width-30,y=0)

        self.remtime_label.place(x=Width-90,y=25)

        self.video_frame.configure(width= 0.25*Width)
        self.video_name.configure(width= 0.25*Width)

        self.backward_btn.place(x=(0.5*frame_width)-75,y=36)     
        self.play_btn.place(x=(0.5*frame_width)-38,y=20)
        self.forward_btn.place(x=(0.5*frame_width)+26,y=36)

        self.vol_btn.place(x=Width-145,y=40)
        self.vol_bar.place(x= Width-115,y= 50)
        self.App.update()

    def spacebar(self,Event):
        try:
            self.resume_or_play()
        except:
            pass

    def right_arrow(self,Event):
        self.move_forward()

    def left_arrow(self,Event):
        self.move_backward()
    
    def stop_video(self):
        self.media_player.stop()



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