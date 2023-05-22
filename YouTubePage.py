from customtkinter import*
from Extra import*
from PIL import Image
from AudioControls import AudioControls
from youtube_search import YoutubeSearch
import urllib.request

class You_Tube():
    img0 = CTkImage(Image.open("Icons\\youtube_bg.png"),size=(64,64))

    def youtube(frame,app,b,c,search,clear_btn):
        AudioControls.Youtube_mode()

        global Search
        Search = search
        Search.unbind('<KeyRelease>')
        Search.bind('<KeyRelease>',lambda Event: You_Tube.check_search(Event))
        Search.bind('<Return>',lambda Event: You_Tube.search_youtube_video(Event))

        global Clear_btn
        Clear_btn = clear_btn
        Clear_btn.configure(command= Search.delete(0,END))

        global App
        App = app

        Extra.close_small_frames()
        b.place_forget()
        c.configure(image=You_Tube.img0)
        c.place(x= 5,y= 5)

        if Extra.Youtube_frame != '':
            Extra.configure_frames(Extra.Youtube_frame, Extra.frames_a)
            Extra.Youtube_frame.place(x= 55,y= 105)
        else:

            global Youtube_page
            Youtube_page = CTkFrame(frame,height= 500,width= 970,fg_color="#781F15",corner_radius= 6)
            Extra.Youtube_frame = Youtube_page
            
            if Youtube_page in Extra.frames_a:
                pass
            else:
                Extra.frames_a.append(Youtube_page)
                
            Extra.configure_frames(Youtube_page, Extra.frames_a)
            Youtube_page.place(x= 55,y= 105)
            Extra.notify("Press Enter to search")
# "#641E16"
            global Yt_frame
            Yt_frame = CTkScrollableFrame(Youtube_page,height=480,width=950,fg_color="#781F15")
            Yt_frame.place(x=0,y=0)


    def check_search(Event):
        if len(Search.get()) > 0:
            Clear_btn.place(x = 520,y=2)
        else:
            Clear_btn.place_forget()

    def search_youtube_video(Event):
        if len(Search.get()) > 0:
            video_search = YoutubeSearch(Search.get(), max_results=20).to_dict()

            X = 0
            Y = 0
            for i in video_search:
                imgurl = i['thumbnails'][0]
                urllib.request.urlretrieve(imgurl,"image.png")

                img = CTkImage(Image.open("image.png"),size=(370,200))

                # if X == 2:
                #     X = 0
                #     Y = Y + 1

                vid_frame = CTkFrame(Yt_frame,height=200,width=940,corner_radius=6,fg_color="#510723",border_color="#0967CC",border_width=0)
                vid_frame.grid(column= 0,row= Y,pady=5,padx=5)
                vid_frame.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                vid_frame.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
                # vid_frame.bind('<Button-1>',lambda Event, path=path, name=name:Video.play_video(Event,path,name))

                thumbn_label = CTkLabel(vid_frame,text='',image=img)
                thumbn_label.place(x=0,y=0)
                thumbn_label.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                thumbn_label.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
                # thumbn_label.bind('<Button-1>',lambda Event, path=path,name=name:Video.play_video(Event,path,name))

                vid_name = CTkLabel(vid_frame,text=str(i['title']),font=("TImes bold",18),width=200,height=40,fg_color="#510723",anchor=W,wraplength=550)
                vid_name.place(x=375,y=10)
                vid_name.bind('<Enter>',lambda Event, vid_frame=vid_frame: Extra.highlight(Event,vid_frame))
                vid_name.bind('<Leave>',lambda Event, vid_frame=vid_frame: Extra.unhighlight(Event,vid_frame))
                # vid_name.bind('<Button-1>',lambda Event, path=path, name=name:Video.play_video(Event,path,name))

                views = CTkLabel(vid_frame,text=str(i['views']),font=("TImes",17),width=100,fg_color="#510723",anchor=W)
                views.place(x=375,y=50)

                time = CTkLabel(vid_frame,text=str(i['publish_time']),font=("TImes",16),width=50,fg_color="#510723",anchor=W)
                time.place(x=375,y=70)

                dur = CTkLabel(vid_frame,text=str(i['duration']),font=("TImes",16),width=50,fg_color="#510723",anchor=W)
                dur.place(x=375,y=170)

                # X = X + 1
                Y = Y + 1
                App.update()

