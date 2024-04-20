from customtkinter import CTkImage
from PIL import Image

class Control():
    def __init__(self):
        pass
        
    img1 = CTkImage(Image.open("Icons\hearta.png"),size=(24,24))
    img2 = CTkImage(Image.open("Icons\heartb.png"),size=(24,24))
    img3 = CTkImage(Image.open("Icons\\volume.png"),size=(26,26))
    img4 = CTkImage(Image.open("Icons\\volume-mute.png"),size=(26,26))
    img5 = CTkImage(Image.open("Icons\music.png"),size=(24,24))
    img6a = CTkImage(Image.open("Icons\previous-button.png"),size=(32,32))
    img6b = CTkImage(Image.open("Icons\previous-button2.png"),size=(32,32))
    img7a = CTkImage(Image.open("Icons\play.png"),size=(60,60))
    img7b = CTkImage(Image.open("Icons\play2.png"),size=(60,60))
    img8a = CTkImage(Image.open("Icons\pause.png"),size=(60,60))
    img8b = CTkImage(Image.open("Icons\pause2.png"),size=(60,60))
    img9a = CTkImage(Image.open("Icons\\next-button.png"),size=(32,32))
    img9b = CTkImage(Image.open("Icons\\next-button2.png"),size=(32,32))
    img10 = CTkImage(Image.open("Icons\\fastbackward.png"),size=(25,25))
    img11 = CTkImage(Image.open("Icons\\fastforward.png"),size=(25,25))
    img12 = CTkImage(Image.open("Icons\play.png"),size=(52,52))
    img13 = CTkImage(Image.open("Icons\pause.png"),size=(50,50))
    img14 = CTkImage(Image.open("Icons\\up.png"),size=(25,25))
    img15 = CTkImage(Image.open("Icons\down.png"),size=(25,25))
    img16a = CTkImage(Image.open("Icons\\shuffle.png"),size=(20,20))
    img16b = CTkImage(Image.open("Icons\\shuffle2.png"),size=(20,20))
    img17a = CTkImage(Image.open("Icons\\loop.png"),size=(16,16))
    img17b = CTkImage(Image.open("Icons\\loop2.png"),size=(20,20))

    def audio_duration(self,length):
        hours = int(length // 3600)  
        length %= 3600
        mins = int(length // 60)  
        length %= 60
        seconds = int(length)  

        if hours == 0:
            return(f"{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")
        else:
            return(f"{str(hours).rjust(2,'0')}:{str(mins).rjust(2,'0')}:{str(seconds).rjust(2,'0')}")



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