from customtkinter import*
from tkinter import filedialog
from PIL import Image
from Extra import Extra
from Database import Database

class Folders():
    def __init__(self,extra: Extra,db: Database):
        self.img0 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
        self.img1 = CTkImage(Image.open("Icons\\plus.png"),size=(20,20))
        self.img2 = CTkImage(Image.open("Icons\\delete.png"),size=(20,20))

        self.Extra = extra
        self.Database = db
    
    def folders(self,frame,button,app):
        self.App =app
        
        self.folders_page = CTkFrame(frame,height= 330,width= 300,fg_color="#510723",corner_radius= 6)
        
        if self.folders_page in self.Extra.frames_b:
            pass
        else:
            self.Extra.frames_b.append(self.folders_page)
            
        self.Extra.configure_frames(self.folders_page, self.Extra.frames_b)
        self.folders_page.place(x= 60,y= 150)
        
        fd_img = CTkLabel(self.folders_page,height= 30,width=30,text= '',fg_color="#510723",image= self.img0,corner_radius= 5)
        fd_img.place(x= 30,y= 10)
                
        fd_label = CTkLabel(self.folders_page,text="Folders",font=("TImes",16),height= 30,width=170,fg_color="#0967CC",corner_radius= 4)
        fd_label.place(x= 70,y= 10)
        
        add = CTkButton(self.folders_page,height= 30,width=25,text= '',fg_color="#510723",hover_color="#510723",image= self.img1,corner_radius= 4,border_color="#0967CC",border_width=0,command= self.new_folder)
        add.place(x= 245,y =10)
        add.bind('<Enter>',lambda Event: self.Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,add))

        back2 = CTkButton(self.folders_page,text= "Back",font=("TImes",14),height= 28,width=150,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,command= lambda: self.Extra.back(self.folders_page,button))
        back2.place(x=75,y=295)
        back2.bind('<Enter>',lambda Event: self.Extra.highlight(Event,back2))
        back2.bind('<Leave>',lambda Event: self.Extra.unhighlight(Event,back2))

        self.load_folders()

    def load_folders(self):
        fd_frame = CTkScrollableFrame(self.folders_page,width=300,height=230,fg_color="#510723",corner_radius= 6,orientation="vertical")
        fd_frame.place(x=0,y=40)

        global Y
        Y = 0
        for i in self.Extra.Folders:
            values = str(i).split("=")
            id = values[0]
            name = values[1]
            fd = CTkFrame(fd_frame,height=35,width=220,fg_color="#770B33",border_color="#0967CC",border_width=0)
            fd.grid(column= 0,row= Y,padx= 30,pady= 2)
            
            lb = CTkLabel(fd,text=values[1],font=("TImes",16),fg_color="#770B33")
            lb.place(x=15,y=2)

            fd.bind('<Enter>',lambda Event, fd=fd: self.Extra.highlight(Event,fd))
            fd.bind('<Leave>',lambda Event, fd=fd: self.Extra.unhighlight(Event,fd))
            fd.bind('<Button-1>',lambda Event, id=id, name=name: self.Database.del_folder(Event,id,name,self))

            lb.bind('<Enter>',lambda Event, fd=fd: self.Extra.highlight(Event,fd))
            lb.bind('<Leave>',lambda Event, fd=fd: self.Extra.unhighlight(Event,fd))
            lb.bind('<Button-1>',lambda Event, id=id, name=name: self.Database.del_folder(Event,id,name,self))

            Y = Y + 1
    
    def hover_in(self,Event,frame,button):
        frame.configure(border_width = 2)

    def hover_out(self,Event,frame,button):
        frame.configure(border_width = 0)

    def new_folder(self):
        lc = filedialog.askdirectory()
        
        if lc != "":
            values = lc.split("""/""") 
            self.Database.add_folder(values[len(values)-1],lc)
            self.App.update()
            self.load_folders()



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