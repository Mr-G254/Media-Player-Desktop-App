from tkinter import ttk
from customtkinter import*
from PIL import Image
from Extra import Extra
from Database import Database
from VideoPage import Video
from SettingsPage import Settings
from FoldersPage import Folders
from MusicPage import Music
from YouTubePage import You_Tube
from AudioControls import AudioControls
from Playlist import Playlist
from Downloader import Downloader
from VideoControls import VideoControls


class HomeUI():
    def __init__(self):
        self.app = CTk()
        self.app.title("Media Player")
        self.app.geometry("1030x600+100+50")
        self.app.lift()
        self.app.resizable(False,False)
        self.size = "min"

        
        self.Extra = Extra()
        self.Audioctrl = AudioControls(self.Extra)
        self.Playlist = Playlist(self.Extra,self.Audioctrl)
        self.Videoctrl = VideoControls(self.Extra)
        self.Music = Music(self.Extra,self.Playlist,self.Audioctrl)
        self.Video = Video(self.Extra,self.Videoctrl,self.Audioctrl)
        self.Database = Database(self.Extra,self.Music,self.Video)
        self.Settings = Settings(self.Extra,self.Database)
        self.Folders = Folders(self.Extra,self.Database)
        self.Downloader = Downloader(self.Extra,self.Database)
        self.You_Tube = You_Tube(self.Extra,self.Audioctrl,self.Downloader)        
        
        self.img0 = CTkImage(Image.open("Icons\\menu.png"),size=(32,32))
        self.img1 = CTkImage(Image.open("Icons\\music.png"),size=(24,24))
        self.img2 = CTkImage(Image.open('Icons\\video.png'),size=(24,24))
        self.img3 = CTkImage(Image.open("Icons\\setting.png"),size=(24,24))
        self.img4 = CTkImage(Image.open("Icons\\youtube.png"),size=(24,24))
        self.img5 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
        self.img6 = CTkImage(Image.open("Icons\\cancel.png"),size=(24,24))
        self.img7 = CTkImage(Image.open("Icons\\recent.png"),size=(20,20))
        self.img8 = CTkImage(Image.open("Icons\\playlist.png"),size=(20,20))
        self.img9 = CTkImage(Image.open("Icons\\heart.png"),size=(20,20))
        self.img10 = CTkImage(Image.open("Icons\\house.png"),size=(100,100))
        self.img11 = CTkImage(Image.open("Icons\\close.png"),size=(24,24))
        self.img12 = CTkImage(Image.open("Icons\\search.png"),size=(20,20))
        self.img13 = CTkImage(Image.open("Icons\\recent_bg.png"),size=(64,64))
        self.img14 = CTkImage(Image.open("Icons\\playlist_bg.png"),size=(64,64))
        self.img15 = CTkImage(Image.open("Icons\\heart_bg.png"),size=(64,64))
        self.img16 = CTkImage(Image.open("Icons\\reject.png"),size=(21,21))

        self.frame = CTkFrame(self.app,height= 600,width=1030,fg_color="#781F15")
        self.Extra.Home_frame = self.frame
        self.frame.place(x= 0,y= 0)

        self.home()
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing_app)
        self.app.mainloop()

       
    def home(self):
        self.name = CTkLabel(self.frame,height= 100,width= 135,fg_color="#510723",text="",font=("TImes",15),corner_radius= 6)
        self.name.place(x= 5,y= 5)

        self.name2 = CTkLabel(self.frame,height= 100,width= 135,fg_color="#510723",text="",font=("TImes",15),corner_radius= 6)
        
        self.search_frame = CTkFrame(self.frame,height= 39,width= 555,fg_color=['gray86', 'gray17'],corner_radius= 5)
        self.search_frame.place(x=172,y= 60)

        self.search = CTkEntry(self.search_frame,height= 35,width= 550,font=("TImes",17),corner_radius= 5,border_color="#0967CC",fg_color=['gray86', 'gray17'],border_width=0)
        self.search.place(x= 2,y= 2)
        self.search.bind('<FocusIn>',lambda Event: self.Extra.highlight(Event,self.search))
        self.search.bind('<FocusOut>',lambda Event: self.Extra.unhighlight(Event,self.search))

        self.clear_btn = CTkButton(self.search_frame,text= "",image= self.img16,height= 35,width=25,fg_color=['gray86', 'gray17'],corner_radius= 4,hover=False)
        
        self.search_btn = CTkLabel(self.frame,text= "",image= self.img12,height= 38,width=38,fg_color="#641E16",corner_radius= 5)
        self.search_btn.place(x=730,y= 60)
        
        self.home_tab = CTkTabview(self.frame,height=380,width=690,fg_color="#641E16")
        self.home_tab.place(x=120,y=105)

        self.home_tab.add("Recent")
        self.home_tab.add("Playlist")
        self.home_tab.add("Favourites")

        self.configure_fav_page()
        self.configure_rec_page()

        self.Playlist.get_database(self.Database,self.app)
        self.Playlist.configure_playlist_page(self.home_tab.tab("Playlist"))

        self.topbar = CTkFrame(self.frame,height= 40,width= 466,corner_radius= 5,border_color="#0967CC",border_width=2)
        self.topbar.place(x= 232,y= 105)
        
        self.recent = CTkButton(self.topbar,text="Recents",image= self.img7,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [self.Extra.configure_buttons(self.recent, self.Extra.buttons_c),self.recent_page()])
        self.recent.place(x= 5,y=5)
        self.Extra.buttons_c.append(self.recent)
        
        self.playlist = CTkButton(self.topbar,text="Playlist",image= self.img8,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [self.Extra.configure_buttons(self.playlist, self.Extra.buttons_c),self.playlist_page()])
        self.playlist.place(x= 158,y= 5)
        self.Extra.buttons_c.append(self.playlist)
        
        self.favourites = CTkButton(self.topbar,text="Favourites",image= self.img9,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [self.Extra.configure_buttons(self.favourites, self.Extra.buttons_c),self.fav_page()])
        self.favourites.place(x= 311,y= 5)
        self.Extra.buttons_c.append(self.favourites)

        self.pic = CTkLabel(self.frame,height= 120,width= 200,fg_color="#510723",text="",font=("TImes",15),image= self.img10,compound= LEFT,corner_radius= 6)
        self.pic.place(x= 826,y= 5)
        
        self.recent.invoke()

        self.menu()
        self.Audioctrl.controls(self,self.app,self.Database)
        
    def menu(self):
        menuframe = CTkFrame(self.frame,height= 250,width=50,fg_color="#510723",corner_radius= 6)
        menuframe.place(x=8,y=150)
        
        menubtn = CTkButton(menuframe,height= 35,width= 45,image= self.img0,text = '',corner_radius= 4,fg_color="#510723",anchor= CENTER,command= lambda: [self.Extra.configure_buttons(menubtn, self.Extra.buttons_a),self.home_action()])
        menubtn.place(x= 3,y= 3)
        menubtn.configure(fg_color= "#0967CC",state= DISABLED)
        self.Extra.buttons_a.append(menubtn)
        
        mscbtn = CTkButton(menuframe,height= 35,width= 45,image= self.img1,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [self.Extra.configure_buttons(mscbtn, self.Extra.buttons_a),self.Music.music(self.frame,self.app,self.pic,self.name2,self.search,self.clear_btn)])
        mscbtn.place(x= 3,y= 48)
        self.Extra.buttons_a.append(mscbtn)
        
        vdbtn = CTkButton(menuframe,height= 35,width= 45,image= self.img2,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [self.Extra.configure_buttons(vdbtn, self.Extra.buttons_a),self.Video.video(self.frame,self.app,self.pic,self.name2,self.search,self.clear_btn)])
        vdbtn.place(x= 3,y= 88)
        self.Extra.buttons_a.append(vdbtn)
        
        ytbtn = CTkButton(menuframe,height= 35,width= 45,image= self.img4,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [self.Extra.configure_buttons(ytbtn, self.Extra.buttons_a),self.You_Tube.youtube(self.frame,self.app,self.pic,self.name2,self.search,self.clear_btn)])
        ytbtn.place(x= 3,y= 128)
        self.Extra.buttons_a.append(ytbtn)
        
        sep = ttk.Separator(menuframe,orient= HORIZONTAL)
        sep.place(x= 10,y= 166,height=1,width=30)
        
        self.fdbtn = CTkButton(menuframe,height= 35,width= 45,image= self.img5,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [self.Extra.configure_buttons(self.fdbtn, self.Extra.buttons_b),self.Folders.folders(self.frame,self.fdbtn,self.app)])
        self.fdbtn.place(x= 3,y= 173)
        self.Extra.buttons_b.append(self.fdbtn)
        
        self.stbtn = CTkButton(menuframe,height= 35,width= 45,image= self.img3,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [self.Extra.configure_buttons(self.stbtn, self.Extra.buttons_b),self.Settings.settings(self.frame,self.stbtn,self.app)])
        self.stbtn.place(x= 3,y= 213)
        self.Extra.buttons_b.append(self.stbtn)  
        
        ext = CTkButton(self.frame,text= "",image= self.img11,height= 40,width=50,fg_color="#510723",corner_radius= 5,border_color="#0967CC",border_width=0,command= self.on_closing_app)
        ext.place(x=8,y=405)
        ext.bind('<Enter>',lambda Event: self.Extra.highlight(Event,ext))
        ext.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,ext)) 

    def home_action(self):
        for i in self.Extra.frames_a:
            i.place_forget()

        self.pic.place(x= 826,y= 5)
        self.name2.place_forget()
        self.search.unbind('<KeyRelease>')
        
    def recent_page(self):
        self.name.configure(image= self.img13)
        self.home_tab.set("Recent")
        
    def playlist_page(self):
        self.name.configure(image= self.img14)
        self.home_tab.set("Playlist")
        
    def fav_page(self):
        self.name.configure(image= self.img15)
        self.home_tab.set("Favourites")

    def configure_fav_page(self):
        fav_frame = CTkScrollableFrame(self.home_tab.tab("Favourites"),height=330,width=655,fg_color="#641E16")
        fav_frame.place(x=0,y=0)

        Y3=0
        self.Extra.Favourites_frames.clear()
        for i in self.Extra.Favourites:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc3 = CTkFrame(fav_frame,height=35,width=650,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc3.grid(column= 0,row= Y3,padx= 2,pady= 2)
            msc3.bind('<Enter>',lambda Event, msc3=msc3: self.Extra.highlight(Event,msc3))
            msc3.bind('<Leave>',lambda Event, msc3=msc3: self.Extra.unhighlight(Event,msc3))
            msc3.bind('<Button-1>',lambda Event, path=path, name=name: self.Audioctrl.select_song(Event,path,name,"Favourites"))
            self.Extra.Favourites_frames.append(msc3)
            
            lb3 = CTkLabel(msc3,text=name,font=("TImes",16),fg_color="#510723")
            lb3.place(x=15,y=2)
            lb3.bind('<Enter>',lambda Event, msc3=msc3: self.Extra.highlight(Event,msc3))
            lb3.bind('<Leave>',lambda Event, msc3=msc3: self.Extra.unhighlight(Event,msc3))
            lb3.bind('<Button-1>',lambda Event, path=path, name=name: self.Audioctrl.select_song(Event,path,name,"Favourites"))

            Y3 = Y3 + 1

    def configure_rec_page(self):
        rec_frame = CTkScrollableFrame(self.home_tab.tab("Recent"),height=330,width=655,fg_color="#641E16")
        rec_frame.place(x=0,y=0)

        Y4=0
        self.Extra.Recent_frames.clear()
        for i in self.Extra.Recent:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc4 = CTkFrame(rec_frame,height=35,width=650,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc4.grid(column= 0,row= Y4,padx= 2,pady= 2)
            msc4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
            msc4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))
            msc4.bind('<Button-1>',lambda Event, path=path, name=name: self.Audioctrl.select_song(Event,path,name,"Recent"))
            self.Extra.Recent_frames.append(msc4)
            
            lb4 = CTkLabel(msc4,text=name,font=("TImes",16),fg_color="#510723")
            lb4.place(x=15,y=2)
            lb4.bind('<Enter>',lambda Event, msc4=msc4: self.Extra.highlight(Event,msc4))
            lb4.bind('<Leave>',lambda Event, msc4=msc4: self.Extra.unhighlight(Event,msc4))
            lb4.bind('<Button-1>',lambda Event, path=path, name=name: self.Audioctrl.select_song(Event,path,name,"Recent"))

            Y4 = Y4 + 1
    
    def on_closing_app(self):
        self.Database.upload_recent()
        self.Database.close()
        self.Audioctrl.stop()
        self.app.destroy()
              

App = HomeUI()
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