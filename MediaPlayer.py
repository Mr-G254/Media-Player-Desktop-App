from tkinter import ttk,Button
from customtkinter import*
from PIL import ImageTk,Image
from SettingsPage import Settings
from FoldersPage import Folders
from Extra import*
from tkhtmlview import HTMLLabel

app = CTk()
app.title("Media Player")
app.geometry("1000x600+100+50")
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
    img10 = CTkImage(Image.open("Icons\house.png"),size=(128,128))
    img11 = CTkImage(Image.open("Icons\close.png"),size=(24,24))
    img12 = CTkImage(Image.open("Icons\search.png"),size=(20,20))
    img13 = CTkImage(Image.open("Icons\\recent_bg.png"),size=(64,64))
    img14 = CTkImage(Image.open("Icons\playlist_bg.png"),size=(64,64))
    img15 = CTkImage(Image.open("Icons\heart_bg.png"),size=(64,64))
    img16 = CTkImage(Image.open("Icons\previous-button.png"),size=(32,32))
    img17 = CTkImage(Image.open("Icons\play.png"),size=(64,64))
    img18 = CTkImage(Image.open("Icons\pause.png"),size=(64,64))
    img19 = CTkImage(Image.open("Icons\\next-button.png"),size=(32,32))
    
    frame = CTkFrame(app,height= 600,width=1000,fg_color="#641E16")
    frame.place(x= 0,y= 0)
       
    def home():
        global name
        name = CTkLabel(HomeUI.frame,height= 100,width= 135,fg_color="#510723",text="",font=("TImes",15),corner_radius= 6)
        name.place(x= 5,y= 5)
        
        topbar = CTkFrame(HomeUI.frame,height= 40,width= 466,corner_radius= 5,border_color="#0967CC",border_width=2)
        topbar.place(x= 217,y= 15)
        
        recent = CTkButton(topbar,text="Recents",image= HomeUI.img7,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(recent, Extra.buttons_c),HomeUI.recent_page()])
        recent.place(x= 5,y=5)
        Extra.buttons_c.append(recent)
        
        playlist = CTkButton(topbar,text="Playlist",image= HomeUI.img8,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(playlist, Extra.buttons_c),HomeUI.playlist_page()])
        playlist.place(x= 158,y= 5)
        Extra.buttons_c.append(playlist)
        
        favourites = CTkButton(topbar,text="Favourites",image= HomeUI.img9,compound= LEFT,font=("TImes",15),fg_color="#510723",width= 150,height=30,corner_radius= 4,command= lambda: [Extra.configure_buttons(favourites, Extra.buttons_c),HomeUI.fav_page()])
        favourites.place(x= 311,y= 5)
        Extra.buttons_c.append(favourites)
        
        recent.invoke()
        
        search = CTkEntry(HomeUI.frame,height= 35,width= 550,font=("TImes",14),corner_radius= 5,border_color="#0967CC",fg_color=['gray86', 'gray17'],border_width=0)
        search.place(x= 147,y= 60)
        search.bind('<FocusIn>',lambda Event: Extra.highlight(Event,search))
        search.bind('<FocusOut>',lambda Event: Extra.unhighlight(Event,search))
        
        search_btn = CTkButton(HomeUI.frame,text= "",image= HomeUI.img12,height= 35,width=50,fg_color=['gray86', 'gray17'],corner_radius= 4,border_color="#0967CC",border_width=0)
        search_btn.place(x=703,y= 60)
        search_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,search_btn))
        search_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,search_btn))
        
        pic = CTkLabel(HomeUI.frame,height= 140,width= 235,fg_color="#510723",text="",font=("TImes",15),image= HomeUI.img10,compound= LEFT,corner_radius= 6)
        pic.place(x= 761,y= 5)
        
        controlframe = CTkFrame(HomeUI.frame,fg_color="#510723",height= 100,width=990,corner_radius= 6)
        controlframe.place(x=5,y=495)

        p_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20)
        p_label.place(x=5,y=5)

        progressbar = CTkProgressBar(controlframe, orientation="horizontal",width=865,height=5)
        progressbar.place(x= 60,y= 12)

        r_label = CTkLabel(controlframe,text="00:00:00",fg_color="#510723",height=20)
        r_label.place(x=935,y=5)

        msclabel = CTkLabel(controlframe,height= 70,width= 70,image= HomeUI.img1,text = '',fg_color=['gray86', 'gray17'],corner_radius= 4,anchor= CENTER)
        msclabel.place(x= 5,y= 25)

        previous_btn = CTkButton(controlframe,text= "",image= HomeUI.img16,height= 35,width=35,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        previous_btn.place(x=415,y=36)
        previous_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,previous_btn))
        previous_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,previous_btn))

        play_btn = CTkButton(controlframe,text= "",image= HomeUI.img17,height= 64,width=64,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        play_btn.place(x=462,y=20)
        play_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,play_btn))
        play_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,play_btn))

        next_btn = CTkButton(controlframe,text= "",image= HomeUI.img19,height= 35,width=35,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0)
        next_btn.place(x=540,y=36)
        next_btn.bind('<Enter>',lambda Event: Extra.highlight(Event,next_btn))
        next_btn.bind('<Leave>',lambda Event: Extra.unhighlight(Event,next_btn))

        HomeUI.menu()
        
    def menu():
        menuframe = CTkFrame(HomeUI.frame,height= 250,width=50,fg_color="#510723",corner_radius= 6)
        menuframe.place(x=5,y=150)
        
        menubtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img0,text = '',corner_radius= 4,fg_color="#510723",anchor= CENTER)
        menubtn.place(x= 3,y= 3)
        menubtn.configure(fg_color= "#0967CC",state= DISABLED)
        Extra.buttons_a.append(menubtn)
        
        mscbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img1,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER)
        mscbtn.place(x= 3,y= 48)
        Extra.buttons_a.append(mscbtn)
        
        vdbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img2,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER)
        vdbtn.place(x= 3,y= 88)
        Extra.buttons_a.append(vdbtn)
        
        ytbtn = CTkButton(menuframe,height= 35,width= 45,image= HomeUI.img4,text = '',fg_color="#510723",corner_radius= 4,anchor= CENTER)
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
        
        ext = CTkButton(HomeUI.frame,text= "",image= HomeUI.img11,height= 40,width=50,fg_color="#510723",corner_radius= 5,border_color="#0967CC",border_width=0,command= lambda: app.destroy())
        ext.place(x=5,y=405)
        ext.bind('<Enter>',lambda Event: Extra.highlight(Event,ext))
        ext.bind('<Leave>',lambda Event: Extra.unhighlight(Event,ext))  
        
    def recent_page():
        name.configure(image= HomeUI.img13)
        
    def playlist_page():
        name.configure(image= HomeUI.img14)
        
    def fav_page():
        name.configure(image= HomeUI.img15)
              
HomeUI.home()

app.mainloop()