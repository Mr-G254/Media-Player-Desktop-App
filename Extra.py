from customtkinter import*

class Extra():  
    Home_frame = ''

    buttons_a = [] #Buttons in the menu except Folder and settings button
    buttons_b = [] #Folder and settings button
    buttons_c = [] #Buttons in the home page(playlist, recent and favourites)
    
    frames_a = []
    frames_b = [] #Folder and Settings frame

    Folders = []

    Playlist = []
    current_playlist_songs = []
    current_playlist_songs_edit = []
    playlist_frames = []
    songs_added = []

    Recent = []
    Recent_frames = []

    Favourites = []
    Favourites_frames = []
    
    All_songs = []
    song_frames = []

    All_videos = []
    video_thumbnails = []

    Music_frame = ''
    Music_scrollframe = ''
    Video_frame = ''
    Youtube_frame = ''
    
    def highlight(Event,widget):
        widget.configure(border_width=2)
        
    def unhighlight(Event,widget):
        widget.configure(border_width=0)
        
    def notify(information):
        H= len(information)*10
        X= 515 - (H/2)
        
        global toast
        toast = CTkLabel(Extra.Home_frame,text= information,font=("TImes",16),height= 35,width=H,fg_color="#641E16",corner_radius= 4)
        toast.place(x=X,y=10)

    def undo_noyify():
        try:
            toast.destroy()
        except:
            pass
        
    def configure_buttons(button,list):
        button.configure(fg_color= "#0967CC",state= DISABLED)
        for i in list:
            if i != button:
                i.configure(state= NORMAL,fg_color="#510723")
            
    def configure_frames(frame,list):
        for i in list:
            if i != frame:
                i.place_forget()
                
    def back(frame,button):
        frame.place_forget()
        button.configure(state= NORMAL,fg_color="#510723")

    def close_small_frames():
        for i in Extra.frames_b:
            i.place_forget()

        for i in Extra.buttons_b:
            i.configure(state= NORMAL,fg_color="#510723")

    def destroy(frame):
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