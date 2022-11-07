from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

FontType = "Calibri Light"
global Folderdir
global Imagedir
Folderdir = ""
Imagedir = ""

def setClick():
    folder_path = filedialog.askdirectory()
    global testImg
    global resultImg
    global Folderdir
    global Imagedir
    global bgcanvas
    if folder_path != "":
        bgcanvas.itemconfig(set_label, text=folder_path)
        Folderdir = folder_path
    if Imagedir == "":
        pass
    else:
        execute()
    return

def fileClick():
    image_path = filedialog.askopenfilename()
    global testImg
    global resultImg
    global Folderdir
    global Imagedir
    global bgcanvas
    if image_path != "":
        testImg = ImageTk.PhotoImage(Image.open(image_path).resize((350,350)))
        bgcanvas.itemconfig(test_image, image=testImg)
        bgcanvas.itemconfig(file_label, text=image_path)
        Imagedir = image_path
    if Folderdir == "":
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((350,350)))
        bgcanvas.itemconfig(result_image, image=noImg)
    else:
        execute()
    return

def execute():
    return


root = Tk()
root.title("GUI")
root.iconbitmap("gui/icon.ico")
root.geometry("1280x720")
root.resizable(0, 0)

bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png"))
buttonImage = PhotoImage(file='gui/buttons.png',width=80,height=30)
noImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((350,350)))
testImg = noImg
resultImg = noImg

bgcanvas = Canvas(root, width=1280, height=720)
bgcanvas.create_image(0,0,image=bgImage,anchor="nw")
bgcanvas.place(x=0,y=0)

#Header
title_text = bgcanvas.create_text(640, 10, anchor = N, text="Face Recognition", font=(FontType, 36))
title_line = bgcanvas.create_line(50,80,1230,80, width=2)
#Left Inset
set_text = bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
SetBut = Button(root, image=buttonImage, borderwidth=0, command=setClick)
set_button = bgcanvas.create_window(100, 220, anchor = W, window=SetBut)
set_label = bgcanvas.create_text(200, 210, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

file_text = bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
FileBut = Button(root, image=buttonImage, borderwidth=0, command=fileClick)
file_button = bgcanvas.create_window(100, 350, anchor = W, window=FileBut)
file_label = bgcanvas.create_text(200, 340, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

result_label = bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
output_label = bgcanvas.create_text(130, 475, anchor = NW, text="None", font=(FontType, 18), fill="#01D901")
#Main viewfinder
test_image_label = bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
test_image = bgcanvas.create_image(400,350, anchor=W, image=testImg)
result_image_label = bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
result_image = bgcanvas.create_image(800,350, anchor=W, image=testImg)
#timer
timer_title = bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
timer_label = bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")

root.mainloop()

