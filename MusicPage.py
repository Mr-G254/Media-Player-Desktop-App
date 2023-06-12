from customtkinter import*
from PIL import Image
from Extra import*
from AudioControls import AudioControls
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from Playlist import*

class Music():
    img0 = CTkImage(Image.open("Icons\music_bg.png"),size=(64,64))
    img1 = CTkImage(Image.open("Icons\playlist.png"),size=(18,18))

    search_results = []

    def music(frame,app,b,c,search,clear_btn):
        AudioControls.Normal_mode()

        global App
        App = app
        
        global Search
        Search = search
        Search.unbind('<KeyRelease>')
        Search.bind('<KeyRelease>',lambda Event: Music.search_song(Event))

        global Clear_btn
        Clear_btn = clear_btn
        Clear_btn.configure(command= Music.clear_entry)

        Extra.close_small_frames()
        b.place_forget()
        c.configure(image=Music.img0)
        c.place(x= 5,y= 5)
        App.update()

        if Extra.Music_frame != '':
            Extra.configure_frames(Extra.Music_frame, Extra.frames_a)
            Extra.Music_frame.place(x= 60,y= 105)
        else:
            global music_page
            music_page = CTkFrame(frame,height= 385,width= 965,fg_color="#781F15",corner_radius= 6)
            Extra.Music_frame = music_page
            
            if music_page in Extra.frames_a:
                pass
            else:
                Extra.frames_a.append(music_page)
                
            Extra.configure_frames(music_page, Extra.frames_a)
            music_page.place(x= 60,y= 105)

            
            Music.show_all_songs()

    def show_all_songs():
        music_frame = CTkScrollableFrame(music_page,height= 380,width= 945,fg_color="#781F15",corner_radius= 6)
        music_frame.place(x=0,y=0)

        Extra.song_frames.clear()

        Y = 0
        x = 0
        for i in Extra.All_songs:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc = CTkFrame(music_frame,height=35,width=940,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc.grid(column= 0,row= Y,padx= 0,pady= 0)
            msc.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            msc.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            msc.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name,"Songs"))

            Extra.song_frames.append(msc)
            
            lb = CTkLabel(msc,text=name,font=("TImes",16),fg_color="#510723")
            lb.place(x=15,y=2)
            lb.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            lb.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            lb.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name,"Songs"))

            try:
                dur = MP3(path).info.length
            except:
                dur = MP4(path).info.length

            dur_label = CTkLabel(msc,text=AudioControls.audio_duration(dur),font=("TImes",16),fg_color="#510723")
            dur_label.place(x=600,y=2)
            dur_label.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            dur_label.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))
            dur_label.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name,"Songs"))

            playlist = CTkButton(msc,fg_color="#510723",hover_color="#510723",width=19,height=19,text="",image=Music.img1,command=lambda name=name, path=path: Playlist.add_song_to_playlist_window(name,App.winfo_x(),App.winfo_y(),path))
            playlist.place(x=900,y=6)
            playlist.bind('<Enter>',lambda Event, msc=msc: Extra.highlight(Event,msc))
            playlist.bind('<Leave>',lambda Event, msc=msc: Extra.unhighlight(Event,msc))

            if x==1:
                msc.configure(fg_color="#641E16")
                lb.configure(fg_color="#641E16")
                dur_label.configure(fg_color="#641E16")
                playlist.configure(fg_color="#641E16",hover_color="#641E16")

                x = 0
            else:
                x = 1

            Y = Y + 1
            App.update()

        global search_frame
        search_frame = CTkScrollableFrame(music_page,height=200,width=590,corner_radius= 5,fg_color=['gray86', 'gray17'])


    def search_song(Event):
        Music.search_results.clear()

        Y2 = 0
        for i in Extra.All_songs:
            if i.lower().startswith(Search.get().lower()) and Search.get() != "":
                Music.search_results.append(i)
        
        if len(Search.get()) > 0:
            if search_frame.winfo_ismapped():
                for i in search_frame.winfo_children():
                    i.destroy()
            
            if len(Music.search_results) < 1:
                search_frame.place_forget()
            else:
                search_frame.place(x=100,y=0)

            Clear_btn.place(x = 520,y=2)
        else:
            Clear_btn.place_forget()
            search_frame.place_forget()

        for i in Music.search_results:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc2 = CTkFrame(search_frame,height=35,width=588,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc2.grid(column= 0,row= Y2,padx= 2,pady= 2)
            msc2.bind('<Enter>',lambda Event, msc2=msc2: Extra.highlight(Event,msc2))
            msc2.bind('<Leave>',lambda Event, msc2=msc2: Extra.unhighlight(Event,msc2))
            msc2.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name))
            
            lb2 = CTkLabel(msc2,text=name,font=("TImes",16),fg_color="#510723")
            lb2.place(x=15,y=2)
            lb2.bind('<Enter>',lambda Event, msc2=msc2: Extra.highlight(Event,msc2))
            lb2.bind('<Leave>',lambda Event, msc2=msc2: Extra.unhighlight(Event,msc2))
            lb2.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name))

            Y2 = Y2 + 1

    def clear_entry():
        Search.delete(0,END)
        search_frame.place_forget()
        Clear_btn.place_forget()



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