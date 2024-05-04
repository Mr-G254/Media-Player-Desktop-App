from customtkinter import*
from Extra import Extra
from PIL import Image
import webbrowser
import pyperclip as clipboard
from tkinter import filedialog
from Database import Database
from AudioControls import AudioControls

class Settings():
    def __init__(self,extra: Extra,db: Database,audioctrl: AudioControls):

        self.img1 = CTkImage(Image.open("Icons\setting.png"),size=(64,64))
        self.img3 = CTkImage(Image.open("Icons\github.png"),size=(24,24))
        self.img4 = CTkImage(Image.open("Icons\linkedin.png"),size=(24,24))
        self.img5 = CTkImage(Image.open("Icons\gmail.png"),size=(24,24))
        self.img6 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
        self.img7 = CTkImage(Image.open("Icons\\reject.png"),size=(21,21))

        self.Extra = extra
        self.Database = db
        self.Audioctrl = audioctrl
    
    def settings(self,frame,app,b,c,search):
        self.Audioctrl.Normal_mode()

        self.App = app
        self.Search = search
        self.icona = b
        self.iconb = c
        
        self.settings_page = CTkFrame(frame,height= 385,width= 965,fg_color="#781F15",corner_radius= 6)
        
        if self.settings_page in self.Extra.frames_a:

            pass
        else:
            self.Extra.frames_a.append(self.settings_page)
          
        
        self.dnd_frame = CTkFrame(self.settings_page,width=340,height=175,fg_color="#641E16",corner_radius=10)
        self.dnd_frame.place(x=5,y=10)

        dnd_frtext = CTkLabel(self.dnd_frame,text= 'Downloads',width=320,font=("TImes",17),fg_color="#641E16")
        dnd_frtext.place(x=10,y=5)

        dnd = CTkFrame(self.dnd_frame,height= 55,width= 320,fg_color="#510723",corner_radius= 5)
        dnd.place(x=10,y= 35)
        
        dnd_text = CTkLabel(dnd,text= 'Always ask where to save downloads',font=("TImes",15),fg_color="#510723")
        dnd_text.place(x=5,y=12)
        
        self.switch_btn = CTkSegmentedButton(dnd,values=["Yes","No  "],width=75,height=25,corner_radius=5,command=self.ask_location)
        self.switch_btn.place(x=240, y=12)
        
        loc = CTkFrame(self.dnd_frame,height= 35,width= 320,fg_color="#510723",corner_radius= 5)
        loc.place(x=10,y= 100)
        
        loc_img = CTkLabel(loc,text='',fg_color="#510723",height=32,width=32,image=self.img6)
        loc_img.place(x=3,y=2)
        
        self.loc_text = CTkLabel(loc,font=("TImes",15),fg_color="#510723",height=30,width=295,anchor=W)
        self.loc_text.place(x=35,y=2)
        
        self.browse = CTkButton(self.dnd_frame,text= "Browse",font=("TImes",14),height= 27,width=120,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,command= self.set_loc)
        self.browse.bind('<Enter>',lambda Event: self.Extra.highlight(Event,self.browse))
        self.browse.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,self.browse))
        
        if self.Database.get_location() == "Always ask":
            self.switch_btn.set("Yes")
            self.ask_location("Yes")
        else:
            self.switch_btn.set("No  ")
            self.ask_location("No  ")
        
        self.dev_frame = CTkFrame(self.settings_page,width=340,height=130,fg_color="#641E16",corner_radius=10)
        self.dev_frame.place(x=5,y=190)

        dev_label = CTkLabel(self.dev_frame,text="Developer",font=("TImes",17),height=20,width=330)
        dev_label.place(x=5,y=5)

       
        git_button = CTkButton(self.dev_frame,text= "GitHub   ",compound=LEFT,font=("TImes",15),height= 40,width=250,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,image= self.img3,command= lambda: [app.update(), webbrowser.open("https://github.com/Mr-G254",new= 2)])
        git_button.place(x= 45,y= 33)
        git_button.bind('<Enter>',lambda Event: self.Extra.highlight(Event,git_button))
        git_button.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,git_button))
        
        lin_button = CTkButton(self.dev_frame,text= "Linkedin",compound=LEFT,font=("TImes",15),height= 40,width=122,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,image= self.img4,command= lambda: [app.update(), webbrowser.open("https://www.linkedin.com/in/ezekiel-gikuhi-6a0757259/",new= 2)])
        lin_button.place(x= 45,y= 80)
        lin_button.bind('<Enter>',lambda Event: self.Extra.highlight(Event,lin_button))
        lin_button.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,lin_button))
        
        gm_button = CTkButton(self.dev_frame,text= "Gmail   ",compound=LEFT,font=("TImes",15),height= 40,width=122,fg_color="#510723",corner_radius= 4,border_color="#0967CC",border_width=0,image= self.img5,command= lambda: self.copy_email(app))
        gm_button.place(x= 173,y= 80)
        gm_button.bind('<Enter>',lambda Event: self.Extra.highlight(Event,gm_button))
        gm_button.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,gm_button))

        self.ver_frame = CTkFrame(self.settings_page,width=340,height=60,fg_color="#641E16",corner_radius=10)
        self.ver_frame.place(x=5,y=325)

        dev_label = CTkLabel(self.ver_frame,text="Version: 2.0.0",font=("TImes",17),fg_color="#510723",height=40,width=320,corner_radius=8)
        dev_label.place(x=10,y=10)
        
    def copy_email(self,app):
        clipboard.copy("gikuhiezekiel@gmail.com")
        self.Extra.notify(app,"The email address has been copied to the clipboard")
        
    def ask_location(self,value):
        if value=="Yes":
            self.Database.update_location("Always ask")
            self.browse.place_forget()
            self.loc_text.configure(text=':  Always Ask')
            
        elif value=="No  ":
            self.browse.place(x=210,y=140)
            if self.Database.get_location() == "Always ask":
                self.set_loc()
            else:
                self.loc_text.configure(text=f':  {self.Database.get_location()}')
            
    def set_loc(self):
        file = str(filedialog.askdirectory())
        if file=='':
            if self.Database.get_location() != "Always ask":
                self.loc_text.configure(text=f':  {self.Database.get_location()}')
            else:
                self.ask_location("Yes")
                self.switch_btn.set("Yes")

        else:
            self.Database.update_location(file)
            self.loc_text.configure(text = f":  {file}")

    def display(self):
        self.Extra.configure_frames(self.settings_page, self.Extra.frames_a)  
        self.settings_page.place(x= 60,y= 105)

        self.Search.unbind('<KeyRelease>')
        self.icona.place_forget()
        self.iconb.configure(image=self.img1)
        self.iconb.place(x= 5,y= 5)

            


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