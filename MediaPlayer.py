from tkinter import ttk,Button
from customtkinter import*
from PIL import ImageTk,Image
from Extra import*
from Database import*
from VideoPage import*
from SettingsPage import*
from FoldersPage import*
from MusicPage import*
from AudioControls import*

app = CTk()
app.title("Media Player")
app.geometry("1030x600+100+50")
app.lift()
app.resizable(False,False)

class HomeUI():
    size = "min"
    
    img0 = CTkImage(Image.open("Icons\menu.png"),size=(32,32))
    img1 = CTkImage(Image.open("Icons\music.png"),size=(24,24))
    img2 = CTkImage(Image.open('Icons\\video.png'),size=(24,24))
    img3 = CTkImage(Image.open("Icons\setting.png"),size=(24,24))
    img4 = CTkImage(Image.open("Icons\youtube.png"),size=(24,24))
    img5 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
    img6 = CTkImage(Image.open("Icons\cancel.png"),size=(24,24))
    img7 = CTkImage(Image.open("Icons\\recent.png"),size=(20,20))
    img8 = CTkImage(Image.open("Icons\playlist.png"),size=(20,20))
    img9 = CTkImage(Image.open("Icons\heart.png"),size=(20,20))
    img10 = CTkImage(Image.open("Icons\house.png"),size=(100,100))
    img11 = CTkImage(Image.open("Icons\close.png"),size=(24,24))
    img12 = CTkImage(Image.open("Icons\search.png"),size=(20,20))
    img13 = CTkImage(Image.open("Icons\\recent_bg.png"),size=(64,64))
    img14 = CTkImage(Image.open("Icons\playlist_bg.png"),size=(64,64))
    img15 = CTkImage(Image.open("Icons\heart_bg.png"),size=(64,64))
    img16 = CTkImage(Image.open("Icons\\reject.png"),size=(21,21))
    #781F15 
    #641E16
    frame = CTkFrame(app,height= 600,width=1030,fg_color="#781F15")
    Extra.Home_frame = frame
    frame.place(x= 0,y= 0)
       
    def home():
        global name
        name = CTkLabel(HomeUI.frame,height= 100,width= 135,fg_color="#510723",text="",font=("TImes",15),corner_radius= 6)
        name.place(x= 5,y= 5)

        global name2
        name2 = CTkLabel(HomeUI.frame,height= 100,width= 135,fg_color="#510723",text="",font=("TImes",15),corner_radius= 6)
        
        search_frame = CTkFrame(HomeUI.frame,height= 39,width= 555,fg_color=['gray86', 'gray17'],corner_radius= 5)
        search_frame.place(x=172,y= 60)

        global search
        search = CTkEntry(search_frame,height= 35,width= 550,font=("TImes",14),corner_radius= 5,border_color="#0967CC",fg_color=['gray86', 'gray17'],border_width=0)
        search.place(x= 2,y= 2)
        search.bind('<FocusIn>',lambda Event: Extra.highlight(Event,search))
        search.bind('<FocusOut>',lambda Event: Extra.unhighlight(Event,search))

        global clear_btn
        clear_btn = CTkButton(search_frame,text= "",image= HomeUI.img16,height= 35,width=25,fg_color=['gray86', 'gray17'],corner_radius= 4,hover=False)
        
        search_btn = CTkLabel(HomeUI.frame,text= "",image= HomeUI.img12,height= 38,width=38,fg_color="#641E16",corner_radius= 4)
        search_btn.place(x=730,y= 60)
        
        global home_tab
        home_tab = CTkTabview(HomeUI.frame,height=380,width=690,fg_color="#641E16")
        home_tab.place(x=120,y=105)

        home_tab.add("Recent")
        home_tab.add("Playlist")
        home_tab.add("Favourites")
        HomeUI.configure_fav_page()

        home_tab.set("Recent")

        global topbar
        topbar = CTkFrame(HomeUI.frame,height= 40,width= 466,corner_radius= 5,border_color="#0967CC",border_width=2)
        topbar.place(x= 232,y= 105)
        
        recent = CTkButton(topbar,text="Recents",image= HomeUI.img7,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(recent, Extra.buttons_c),HomeUI.recent_page()])
        recent.place(x= 5,y=5)
        Extra.buttons_c.append(recent)
        
        playlist = CTkButton(topbar,text="Playlist",image= HomeUI.img8,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(playlist, Extra.buttons_c),HomeUI.playlist_page()])
        playlist.place(x= 158,y= 5)
        Extra.buttons_c.append(playlist)
        
        favourites = CTkButton(topbar,text="Favourites",image= HomeUI.img9,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(favourites, Extra.buttons_c),HomeUI.fav_page()])
        favourites.place(x= 311,y= 5)
        Extra.buttons_c.append(favourites)

        global pic
        pic = CTkLabel(HomeUI.frame,height= 120,width= 200,fg_color="#510723",text="",font=("TImes",15),image= HomeUI.img10,compound= LEFT,corner_radius= 6)
        pic.place(x= 826,y= 5)
        
        recent.invoke()

        AudioControls.controls(HomeUI,app,Database)
        HomeUI.menu()
        
    def menu():
        menuframe = CTkFrame(HomeUI.frame,height= 250,width=50,fg_color="#510723",corner_radius= 6)
        menuframe.place(x=5,y=150)
        
        menubtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img0,text = '',corner_radius= 4,fg_color="#510723",anchor= CENTER,command= lambda: [Extra.configure_buttons(menubtn, Extra.buttons_a),HomeUI.home_action()])
        menubtn.place(x= 3,y= 3)
        menubtn.configure(fg_color= "#0967CC",state= DISABLED)
        Extra.buttons_a.append(menubtn)
        
        mscbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img1,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [Extra.configure_buttons(mscbtn, Extra.buttons_a),Music.music(HomeUI.frame,app,pic,name2,search,clear_btn)])
        mscbtn.place(x= 3,y= 48)
        Extra.buttons_a.append(mscbtn)
        
        vdbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img2,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [Extra.configure_buttons(vdbtn, Extra.buttons_a),Video.video(HomeUI.frame,app,pic,name2,search,clear_btn)])
        vdbtn.place(x= 3,y= 88)
        Extra.buttons_a.append(vdbtn)
        
        ytbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img4,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [Extra.configure_buttons(ytbtn, Extra.buttons_a)])
        ytbtn.place(x= 3,y= 128)
        Extra.buttons_a.append(ytbtn)
        
        sep = ttk.Separator(menuframe,orient= HORIZONTAL)
        sep.place(x= 10,y= 166,height=1,width=30)
        
        global fdbtn
        fdbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img5,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [Extra.configure_buttons(fdbtn, Extra.buttons_b),Folders.folders(HomeUI.frame,fdbtn,app)])
        fdbtn.place(x= 3,y= 173)
        Extra.buttons_b.append(fdbtn)
        
        global stbtn
        stbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img3,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER,command= lambda: [Extra.configure_buttons(stbtn, Extra.buttons_b),Settings.settings(HomeUI.frame,stbtn,app)])
        stbtn.place(x= 3,y= 213)
        Extra.buttons_b.append(stbtn)  
        
        ext = CTkButton(HomeUI.frame,text= "",image= HomeUI.img11,height= 40,width=50,fg_color="#510723",corner_radius= 5,border_color="#0967CC",border_width=0,command= lambda:[(Database.close(),app.destroy())])
        ext.place(x=5,y=405)
        ext.bind('<Enter>',lambda Event: Extra.highlight(Event,ext))
        ext.bind('<Leave>',lambda Event: Extra.unhighlight(Event,ext))  

    def home_action():
        for i in Extra.frames_a:
            i.place_forget()

        pic.place(x= 826,y= 5)
        name2.place_forget()
        search.unbind('<KeyRelease>')
        
    def recent_page():
        name.configure(image= HomeUI.img13)
        home_tab.set("Recent")
        
    def playlist_page():
        name.configure(image= HomeUI.img14)
        home_tab.set("Playlist")
        
    def fav_page():
        name.configure(image= HomeUI.img15)
        home_tab.set("Favourites")

    def configure_fav_page():
        fav_frame = CTkScrollableFrame(home_tab.tab("Favourites"),height=355,width=655,fg_color="#641E16")
        fav_frame.place(x=0,y=0)

        Y3=0
        for i in Extra.E_favourites:
            value = i.split("=")
            name = value[0].replace('.mp3','')
            path = value[1]
            msc3 = CTkFrame(fav_frame,height=35,width=655,fg_color="#510723",border_color="#0967CC",border_width=0)
            msc3.grid(column= 0,row= Y3,padx= 2,pady= 2)
            msc3.bind('<Enter>',lambda Event, msc3=msc3: Extra.highlight(Event,msc3))
            msc3.bind('<Leave>',lambda Event, msc3=msc3: Extra.unhighlight(Event,msc3))
            msc3.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name,"Favourites"))
            Extra.Favourites_frames.append(msc3)
            
            lb3 = CTkLabel(msc3,text=name,font=("TImes",16),fg_color="#510723")
            lb3.place(x=15,y=2)
            lb3.bind('<Enter>',lambda Event, msc3=msc3: Extra.highlight(Event,msc3))
            lb3.bind('<Leave>',lambda Event, msc3=msc3: Extra.unhighlight(Event,msc3))
            lb3.bind('<Button-1>',lambda Event, path=path, name=name: AudioControls.select_song(Event,path,name,"Favourites"))

            Y3 = Y3 + 1
              
HomeUI.home()

app.mainloop()