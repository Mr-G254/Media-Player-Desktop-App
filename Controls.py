from customtkinter import*
from Extra import*
import audioplayer

class Controls():

    def controls(Home_class):
        global Home
        Home = Home_class

        controlframe = CTkFrame(Home_class.frame,fg_color="#510723",height= 100,width=990,corner_radius= 6)
        controlframe.place(x=5,y=495)

        p_label = CTkLabel(controlframe,text="00:00",fg_color="#510723",height=20,width=55,anchor=CENTER)
        p_label.place(x=5,y=3)

        progressbar = CTkSlider(controlframe,from_=0,to=865,progress_color="#770B33",fg_color=['gray86', 'gray17'], orientation="horizontal",width=865)
        progressbar.set(865)
        progressbar.place(x= 60,y= 5)

        global r_label
        r_label = CTkLabel(controlframe,text="00:00",fg_color="#510723",height=20,width=40,anchor=CENTER)
        r_label.place(x=935,y=3)

        msclabel = CTkLabel(controlframe,height= 70,width= 70,image= Home_class.img1,text = '',fg_color=['gray86', 'gray17'],corner_radius= 4,anchor= CENTER)
        msclabel.place(x= 5,y= 25)

        song_frame = CTkFrame(controlframe,height= 40,width= 300,fg_color="#510723")
        song_frame.place(x=85,y=25)

        global song_name
        song_name = CTkLabel(song_frame,height= 40,width= 100,text = '',fg_color="#510723",font=("TImes",16),anchor= W)
        song_name.place(x=0,y=0)

        previous_btn = CTkButton(controlframe,text= "",image= Home_class.img16,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        previous_btn.place(x=415,y=41)
        previous_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,previous_btn))
        previous_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,previous_btn))

        global play_btn
        play_btn = CTkButton(controlframe,text= "",image= Home_class.img17,height= 64,width=64,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        play_btn.place(x=462,y=25)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        next_btn = CTkButton(controlframe,text= "",image= Home_class.img19,height= 35,width=35,fg_color="#510723",hover_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        next_btn.place(x=540,y=41)
        next_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,next_btn))
        next_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,next_btn))

        global fav_btn
        fav_btn = CTkButton(controlframe,text= "",image= Home_class.img21,height= 30,width=30,fg_color="#510723",corner_radius= 4,border_color="#510723",hover_color="#510723",border_width=0,command=lambda:[Home_class.fav_song(fav_btn)])
        fav_btn.place(x=930,y=35)
        fav_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,fav_btn))
        fav_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,fav_btn))

    def play_song(Event,file_path,file_name):
        song_name.configure(text=file_name)
        play_btn.configure(image= Home.img18)

        global song
        song = audioplayer.AudioPlayer(file_path)
        song.play(loop=False, block=False)

        play_btn.configure(command= Controls.pause)

    def pause():
        song.pause()
        play_btn.configure(command= Controls.resume)
        play_btn.configure(image= Home.img17)

    def resume():
        song.resume()
        play_btn.configure(command= Controls.pause)
        play_btn.configure(image= Home.img18)