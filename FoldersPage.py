from customtkinter import*
from tkinter import filedialog
from PIL import Image
from Extra import*
from Database import*

class Folders():
    img0 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
    img1 = CTkImage(Image.open("Icons\\plus.png"),size=(20,20))
    img2 = CTkImage(Image.open("Icons\\delete.png"),size=(20,20))
    
    def folders(frame,button,app):
        global App
        App =app
        
        global folders_page
        folders_page = CTkFrame(frame,height= 330,width= 300,fg_color="#510723",corner_radius= 6)
        
        if folders_page in Extra.frames_b:
            pass
        else:
            Extra.frames_b.append(folders_page)
            
        Extra.configure_frames(folders_page, Extra.frames_b)
        folders_page.place(x= 60,y= 150)
        
        fd_img = CTkLabel(folders_page,height= 30,width=30,text= '',fg_color="#510723",image= Folders.img0,corner_radius= 5)
        fd_img.place(x= 30,y= 10)
                
        fd_label = CTkLabel(folders_page,text="Folders",font=("TImes",16),height= 30,width=170,fg_color="#0967CC",corner_radius= 4)
        fd_label.place(x= 70,y= 10)
        
        add = CTkButton(folders_page,height= 30,width=25,text= '',fg_color="#510723",hover_color="#510723",image= Folders.img1,corner_radius= 4,border_color="#0967CC",border_width=0,command= Folders.new_folder)
        add.place(x= 245,y =10)
        add.bind('<Enter>',lambda Event: Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: Extra.unhighlight(Event,add))

        back2 = CTkButton(folders_page,text= "Back",font=("TImes",14),height= 28,width=150,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,command= lambda: Extra.back(folders_page,button))
        back2.place(x=75,y=295)
        back2.bind('<Enter>',lambda Event: Extra.highlight(Event,back2))
        back2.bind('<Leave>',lambda Event: Extra.unhighlight(Event,back2))

        Folders.load_folders()

    def load_folders():
        fd_frame = CTkScrollableFrame(folders_page,width=300,height=230,fg_color="#510723",corner_radius= 6,orientation="vertical")
        fd_frame.place(x=0,y=40)

        global Y
        Y = 0
        for i in Extra.Folders:
            values = str(i).split("=")
            id = values[0]
            name = values[1]
            fd = CTkFrame(fd_frame,height=35,width=220,fg_color="#770B33",border_color="#0967CC",border_width=0)
            fd.grid(column= 0,row= Y,padx= 30,pady= 2)
            
            lb = CTkLabel(fd,text=values[1],font=("TImes",16),fg_color="#770B33")
            lb.place(x=15,y=2)

            fd.bind('<Enter>',lambda Event, fd=fd: Extra.highlight(Event,fd))
            fd.bind('<Leave>',lambda Event, fd=fd: Extra.unhighlight(Event,fd))
            fd.bind('<Button-1>',lambda Event, id=id, name=name: Database.del_folder(Event,id,name,Folders))

            lb.bind('<Enter>',lambda Event, fd=fd: Extra.highlight(Event,fd))
            lb.bind('<Leave>',lambda Event, fd=fd: Extra.unhighlight(Event,fd))
            lb.bind('<Button-1>',lambda Event, id=id, name=name: Database.del_folder(Event,id,name,Folders))

            Y = Y + 1
    
    def hover_in(Event,frame,button):
        frame.configure(border_width = 2)

    def hover_out(Event,frame,button):
        frame.configure(border_width = 0)

    def new_folder():
        lc = filedialog.askdirectory()
        
        if lc != "":
            values = lc.split("""/""") 
            Database.add_folder(values[len(values)-1],lc)
            App.update()
            Folders.load_folders()



