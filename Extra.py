from customtkinter import*

class Extra():
    buttons_a = []
    buttons_b = []
    
    frames_a = []
    frames_b = []
    
    def highlight(Event,x):
        x.configure(border_width=2)
        
    def unhighlight(Event,x):
        x.configure(border_width=0)
        
    def notify(app,information):
        H= len(information)*10
        X= 500 - (H/2)
        
        toast = CTkLabel(app,text= information,font=("TImes",16),height= 35,width=H,fg_color="#770B33",corner_radius= 4)
        toast.place(x=X,y=550)
        
        app.update()
        app.after(1200,toast.place_forget())
        
    def configure_buttons(button,list):
        for i in list:
            if i != button:
                i.configure(state= NORMAL,fg_color="#510723")
            
    def configure_frames(frame,list):
        for i in list:
            if i != frame:
                i.place_forget()
                
    def back(frame,button):
        frame.place_forget()
        button.configure(state= NORMAL,fg_color="#510723")
