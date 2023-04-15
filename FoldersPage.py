from customtkinter import*
from PIL import Image
from Extra import*

class Folders():
    img0 = CTkImage(Image.open("Icons\\folder.png"),size=(24,24))
    img1 = CTkImage(Image.open("Icons\\plus.png"),size=(20,20))
    
    def folders(frame,button,app):
        
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
        
        # global add
        add = CTkButton(folders_page,height= 30,width=25,text= '',fg_color="#510723",image= Folders.img1,corner_radius= 4,border_color="#0967CC",border_width=0)
        add.place(x= 245,y =10)
        add.bind('<Enter>',lambda Event: Extra.highlight(Event,add))
        add.bind('<Leave>',lambda Event: Extra.unhighlight(Event,add))
        
        # global back2
        back2 = CTkButton(folders_page,text= "Back",font=("TImes",14),height= 28,width=150,fg_color="#770B33",corner_radius= 4,border_color="#0967CC",border_width=0,command= lambda: Extra.back(folders_page,button))
        back2.place(x=75,y=295)
        back2.bind('<Enter>',lambda Event: Extra.highlight(Event,back2))
        back2.bind('<Leave>',lambda Event: Extra.unhighlight(Event,back2))
