from customtkinter import CTkImage
from PIL import Image
from Extra import*

class Control():
    img1 = CTkImage(Image.open("Icons\hearta.png"),size=(24,24))
    img2 = CTkImage(Image.open("Icons\heartb.png"),size=(24,24))
    img3 = CTkImage(Image.open("Icons\\volume.png"),size=(26,26))
    img4 = CTkImage(Image.open("Icons\\volume-mute.png"),size=(26,26))
    img5 = CTkImage(Image.open("Icons\music.png"),size=(24,24))
    img6 = CTkImage(Image.open("Icons\previous-button.png"),size=(32,32))
    img7 = CTkImage(Image.open("Icons\play.png"),size=(64,64))
    img8 = CTkImage(Image.open("Icons\pause.png"),size=(62,62))
    img9 = CTkImage(Image.open("Icons\\next-button.png"),size=(32,32))
    img10 = CTkImage(Image.open("Icons\\fastbackward.png"),size=(25,25))
    img11 = CTkImage(Image.open("Icons\\fastforward.png"),size=(25,25))
    img12 = CTkImage(Image.open("Icons\play.png"),size=(52,52))
    img13 = CTkImage(Image.open("Icons\pause.png"),size=(50,50))
    img14 = CTkImage(Image.open("Icons\\up.png"),size=(25,25))
    img15 = CTkImage(Image.open("Icons\down.png"),size=(25,25))

    def audio_duration(length):
        hours = int(length // 3600)  
        length %= 3600
        mins = int(length // 60)  
        length %= 60
        seconds = int(length)  

        if hours == 0:
            return(f"{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")
        else:
            return(f"{str(hours).rjust(2,'0')}:{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")

