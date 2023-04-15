from customtkinter import*
from Extra import*
from PIL import Image
import webbrowser
import pyperclip as clipboard
from pathlib import Path
from tkinter import filedialog

class Settings():
    # from MediaPlayer import HomeUI
    img1 = CTkImage(Image.open("Icons\setting.png"),size=(24,24))
    img2 = CTkImage(Image.open("Icons\dev.png"),size=(128,128))
    img3 = CTkImage(Image.open("Icons\github.png"),size=(24,24))
    img4 = CTkImage(Image.open("Icons\linkedin.png"),size=(24,24))
    img5 = CTkImage(Image.open("Icons\gmail.png"),size=(24,24))
    img6 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
    
    def settings(frame,button,app):
        
        global settings_page
        settings_page = CTkFrame(frame,height= 330,width= 600,fg_color="#510723",corner_radius= 6)
        
        if settings_page in Extra.frames_b:
            pass
        else:
            Extra.frames_b.append(settings_page)
          
        Extra.configure_frames(settings_page, Extra.frames_b)  
        settings_page.place(x= 60,y= 150)
        
        st_img = CTkLabel(settings_page,height= 30,width=30,text= '',fg_color="#510723",image= Settings.img1,corner_radius= 5)
        st_img.place(x= 175,y= 10)
                
        st_label = CTkLabel(settings_page,text="Settings",font=("TImes",16),height= 30,width=170,fg_color="#0967CC",corner_radius= 4)
        st_label.place(x= 215,y= 10)
        
        dnd = CTkFrame(settings_page,height= 55,width= 330,fg_color="#770B33",corner_radius= 5)
        dnd.place(x=10,y= 50)
        
        dnd_text = CTkLabel(dnd,text= 'Always ask where to save downloads',font=("TImes",15),fg_color="#770B33")
        dnd_text.place(x=10,y=12)
        
        global switch_btn
        switch_btn = CTkSegmentedButton(dnd,values=["Yes","No  "],width=75,height=25,corner_radius=5,command=Settings.select_loc)
        switch_btn.place(x=250, y=12)
        
        loc = CTkFrame(settings_page,height= 35,width= 330,fg_color="#770B33",corner_radius= 5)
        loc.place(x=10,y= 110)
        
        loc_img = CTkLabel(loc,text='',fg_color="#770B33",height=32,width=32,image=Settings.img6)
        loc_img.place(x=3,y=2)
        
        global loc_text
        loc_text = CTkLabel(loc,text=':  Always Ask',font=("TImes",15),fg_color="#770B33",height=30,width=295,anchor=W)
        loc_text.place(x=35,y=2)
        
        global browse
        browse = CTkButton(settings_page,text= "Browse",font=("TImes",14),height= 27,width=120,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,command= Settings.get_loc)
        browse.bind('<Enter>',lambda Event: Extra.highlight(Event,browse))
        browse.bind('<Leave>',lambda Event: Extra.unhighlight(Event,browse))
        
        switch_btn.set("Yes")
        Settings.select_loc("Yes")
 
        dev_image = CTkLabel(settings_page,height= 130,width= 200,text= '',fg_color="#510723",image= Settings.img2,corner_radius= 4)
        dev_image.place(x= 390,y= 53)
        
        git_button = CTkButton(settings_page,text= "GitHub   ",compound=LEFT,font=("TImes",15),height= 40,width=200,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,image= Settings.img3,command= lambda: [app.update(), webbrowser.open("https://github.com/Mr-G254",new= 2)])
        git_button.place(x= 390,y= 188)
        git_button.bind('<Enter>',lambda Event: Extra.highlight(Event,git_button))
        git_button.bind('<Leave>',lambda Event: Extra.unhighlight(Event,git_button))
        
        lin_button = CTkButton(settings_page,text= "Linkedin",compound=LEFT,font=("TImes",15),height= 40,width=200,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,image= Settings.img4,command= lambda: [app.update(), webbrowser.open("https://www.linkedin.com/in/ezekiel-gikuhi-6a0757259/",new= 2)])
        lin_button.place(x= 390,y= 233)
        lin_button.bind('<Enter>',lambda Event: Extra.highlight(Event,lin_button))
        lin_button.bind('<Leave>',lambda Event: Extra.unhighlight(Event,lin_button))
        
        gm_button = CTkButton(settings_page,text= "Gmail   ",compound=LEFT,font=("TImes",15),height= 40,width=200,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,image= Settings.img5,command= lambda: Settings.copy_email(app))
        gm_button.place(x= 390,y= 278)
        gm_button.bind('<Enter>',lambda Event: Extra.highlight(Event,gm_button))
        gm_button.bind('<Leave>',lambda Event: Extra.unhighlight(Event,gm_button))
        
        back = CTkButton(settings_page,text= "Back",font=("TImes",14),height= 28,width=150,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,command= lambda: Extra.back(settings_page,button))
        back.place(x=225,y=291)
        back.bind('<Enter>',lambda Event: Extra.highlight(Event,back))
        back.bind('<Leave>',lambda Event: Extra.unhighlight(Event,back))
        
    def copy_email(app):
        clipboard.copy("gikuhiezekiel@gmail.com")
        Extra.notify(app,"The email address has been copied to the clipboard")
        
    def select_loc(value):
        if value=="Yes":
            loc_text.configure(text = ":  Always ask")
            browse.place_forget()
        elif value=="No  ":
            loc_text.configure(text = f":  {Path.home()}\Downloads")
            browse.place(x=220,y=150)
            
    def get_loc():
        file = str(filedialog.askdirectory())
        if file=='':
            Settings.get_loc()
        else:
            loc_text.configure(text = f":  {file}")
            
        