from customtkinter import*

class Extra():  
    def __init__(self):
        self.Home_frame = ''

        self.buttons_a = [] #Buttons in the menu except Folder and settings button
        self.buttons_b = [] #Folder and settings button
        self.buttons_c = [] #Buttons in the home page(playlist, recent and favourites)
        
        self.frames_a = []
        self.frames_b = [] #Folder and Settings frame

        self.Folders = []

        self.Playlist = []
        self.current_playlist_songs = []
        self.current_playlist_songs_edit = []
        self.playlist_frames = []
        self.songs_added = []

        self.Recent = []
        self.Recent_frames = []

        self.Favourites = []
        self.Favourites_frames = []
        
        self.All_songs = []
        self.song_frames = []

        self.All_videos = []
        self.video_thumbnails = []

        self.Music_frame = ''
        self.Music_scrollframe = ''
        self.Video_frame = ''
        self.Youtube_frame = ''
    
    def highlight(self,Event,widget):
        widget.configure(border_width=2)
        
    def unhighlight(self,Event,widget):
        widget.configure(border_width=0)

    def highlightControls(self,Event,widget,icon):
        widget.configure(image = icon)
        
    def unhighlightControls(self,Event,widget,icon):
        widget.configure(image = icon)
        
    def notify(self,information):
        H= len(information)*10
        X= 515 - (H/2)
        
        self.toast = CTkLabel(self.Home_frame,text= information,font=("TImes",16),height= 35,width=H,fg_color="#641E16",corner_radius= 4)
        self.toast.place(x=X,y=10)

    def undo_noyify(self):
        try:
            self.toast.destroy()
        except:
            pass
        
    def configure_buttons(self,button,list):
        button.configure(fg_color= "#0967CC",state= DISABLED)
        for i in list:
            if i != button:
                i.configure(state= NORMAL,fg_color="#510723")
            
    def configure_frames(self,frame,list):
        for i in list:
            if i != frame:
                i.place_forget()
                
    def back(self,frame,button):
        frame.place_forget()
        button.configure(state= NORMAL,fg_color="#510723")

    def close_small_frames(self):
        for i in self.frames_b:
            i.place_forget()

        for i in self.buttons_b:
            i.configure(state= NORMAL,fg_color="#510723")

    def destroy(self,frame):
        frame.destroy()
        


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