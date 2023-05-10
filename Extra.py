from customtkinter import*

class Extra():  
    Home_frame = ''

    buttons_a = [] #Buttons in the menu except Folder and settings button
    buttons_b = [] #Folder and settings button
    buttons_c = [] #Buttons in the home page(playlist, recent and favourites)
    
    frames_a = []
    frames_b = [] #Folder and Settings frame

    Folders = []
    Recent = []
    Favourites = []

    All_songs = []
    song_frames = []

    All_videos = []
    video_thumbnails = []

    Music_frame = ''
    Music_scrollframe = ''
    Video_frame = ''
    
    def highlight(Event,widget):
        widget.configure(border_width=2)
        
    def unhighlight(Event,widget):
        widget.configure(border_width=0)
        
    def notify(information):
        H= len(information)*10
        X= 515 - (H/2)
        
        global toast
        toast = CTkLabel(Extra.Home_frame,text= information,font=("TImes",16),height= 35,width=H,fg_color="#770B33",corner_radius= 4)
        toast.place(x=X,y=20)

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
        