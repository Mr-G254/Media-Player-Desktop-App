from customtkinter import*
from tkinter import messagebox
from Extra import*
from PIL import Image
from AudioControls import AudioControls
from VideoControls import VideoControls
from youtube_search import YoutubeSearch
import urllib.request
import webbrowser
from Downloader import *

class You_Tube():
    Keywords = ''
    vid_window=''
    img0 = CTkImage(Image.open("Icons\\youtube_bg.png"),size=(64,64))

    def youtube(frame,app,b,c,search,clear_btn):
        AudioControls.Youtube_mode()

        global Search
        Search = search
        Search.unbind('<KeyRelease>')
        Search.bind('<KeyRelease>',lambda Event: You_Tube.check_search(Event))
        Search.bind('<Return>',lambda Event: You_Tube.search_youtube_video(Event,Search.get()))

        global Clear_btn
        Clear_btn = clear_btn
        Clear_btn.configure(command=lambda: [Search.delete(0,END),Clear_btn.place_forget()])

        global App
        App = app

        global Frame
        Frame = frame
        
        Extra.close_small_frames()
        b.place_forget()
        c.configure(image=You_Tube.img0)
        c.place(x= 5,y= 5)
        App.update()

        if Extra.Youtube_frame != '':
            Extra.configure_frames(Extra.Youtube_frame, Extra.frames_a)
            Extra.Youtube_frame.place(x= 60,y= 105)
        else:

            global Youtube_page
            Youtube_page = CTkFrame(Frame,height= 500,width= 970,fg_color="#781F15",corner_radius= 6)
            Extra.Youtube_frame = Youtube_page
            
            if Youtube_page in Extra.frames_a:
                pass
            else:
                Extra.frames_a.append(Youtube_page)
                
            Extra.configure_frames(Youtube_page, Extra.frames_a)
            Youtube_page.place(x= 60,y= 105)
            Extra.notify("Press Enter to search")

            global Yt_frame
            Yt_frame = CTkScrollableFrame(Youtube_page,height=490,width=945,fg_color="#781F15")
            Yt_frame.place(x=0,y=0)

            You_Tube.search_yt_video("Technology")    

    def check_search(Event):
        if len(Search.get()) > 0:
            Clear_btn.place(x = 520,y=2)
        else:
            Clear_btn.place_forget()

    def search_youtube_video(Event,keywords):
        You_Tube.search_yt_video(keywords)

    def search_yt_video(keywords):
        You_Tube.Keywords = keywords
        try:
            if len(keywords) > 0:
                video_search = YoutubeSearch(keywords, max_results=20).to_dict()
                X = 0
                Y = 0
                for i in video_search:
                    imgurl = i['thumbnails'][0]
                    urllib.request.urlretrieve(imgurl,"image.png")

                    img = CTkImage(Image.open("image.png"),size=(370,200))

                    vid_frame = CTkFrame(Yt_frame,height=200,width=940,corner_radius=6,fg_color="#510723",border_color="#0967CC",border_width=0)
                    vid_frame.grid(column= 0,row= Y,pady=5,padx=1)
                    vid_frame.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    vid_frame.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))

                    thumbn_label = CTkLabel(vid_frame,text='',image=img)
                    thumbn_label.place(x=0,y=0)
                    thumbn_label.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    thumbn_label.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))

                    title = str(i['title'])
                    vid_name = CTkLabel(vid_frame,text=title,font=("TImes",19),width=200,height=40,fg_color="#510723",anchor=W,justify='left',wraplength=550)
                    vid_name.place(x=375,y=10)
                    vid_name.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    vid_name.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))

                    views = CTkLabel(vid_frame,text=str(i['views']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    views.place(x=375,y=170)
                    App.update()

                    time = CTkLabel(vid_frame,text=str(i['publish_time']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    time.place(x=(views.winfo_width()+380),y=170)
                    App.update()

                    dur = CTkLabel(vid_frame,text=str(i['duration']),font=("TImes",16),height=22,fg_color="#770B33",corner_radius= 4,anchor=W)
                    dur.place(x=(views.winfo_width()+time.winfo_width()+385),y=170)

                    id = i['id']
                    play_vid = CTkButton(vid_frame,height=30,width=150,text="  Play video",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command=lambda id=id: You_Tube.play_video(id))
                    play_vid.place(x=780,y=90)
                    play_vid.bind('<Enter>',lambda Event, play_vid=play_vid: Extra.highlight(Event,play_vid))
                    play_vid.bind('<Leave>',lambda Event, play_vid=play_vid: Extra.unhighlight(Event,play_vid))
                    play_vid.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    play_vid.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))

                    download_vid = CTkButton(vid_frame,height=30,width=150,text="  Download video",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command= lambda title=title, id=id:[Downloader.download_video(Frame,title,f"https://www.youtube.com/watch?v={id}"),You_Tube.show_downloads()])
                    download_vid.place(x=780,y=125)
                    download_vid.bind('<Enter>',lambda Event, download_vid=download_vid: Extra.highlight(Event,download_vid))
                    download_vid.bind('<Leave>',lambda Event, download_vid=download_vid: Extra.unhighlight(Event,download_vid))
                    download_vid.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    download_vid.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))

                    download_aud = CTkButton(vid_frame,height=30,width=150,text="  Download audio",font=("Times",17),fg_color="#641E16",border_color="#0967CC",border_width=0,corner_radius= 4,anchor=W,command= lambda title=title, id=id:[Downloader.download_audio(Frame,title,f"https://www.youtube.com/watch?v={id}"),You_Tube.show_downloads()])
                    download_aud.place(x=780,y=160)
                    download_aud.bind('<Enter>',lambda Event, download_aud=download_aud: Extra.highlight(Event,download_aud))
                    download_aud.bind('<Leave>',lambda Event, download_aud=download_aud: Extra.unhighlight(Event,download_aud))
                    download_aud.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                    download_aud.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
            

                    Y = Y + 1
                    App.update()
        except Exception as e:
            messagebox.showerror("An error occurred",e)

    def play_video(id):
       webbrowser.open(f"https://www.youtube.com/watch?v={id}")

    def on_closing():
        VideoControls.stop_video()
        You_Tube.vid_window.destroy()
        VideoControls.is_maxsize = True
        App.deiconify()

    def show_downloads():
        Yt_frame.configure(height=445)