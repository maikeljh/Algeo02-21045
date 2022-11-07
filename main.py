from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import time

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


windowrt = Tk()
windowrt.title("GUI")
windowrt.iconbitmap("gui/icon.ico")
windowrt.geometry("1280x720")



bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png"))
buttonImage = PhotoImage(file='gui/buttons.png',width=80,height=30)
noImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((350,350)))
testImg = noImg
resultImg = noImg

bgcanvas = Canvas(windowrt)

bgcanvas.create_image(0,0,image=bgImage,anchor="nw")
bgcanvas.pack(fill="both", expand=True)
#Header
title_text = bgcanvas.create_text(640, 10, anchor = N, text="Face Recognition", font=(FontType, 36))
title_line = bgcanvas.create_line(50,80,1230,80, width=2)
#Left Inset
set_text = bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
SetBut = Button(windowrt, image=buttonImage, borderwidth=0, command=setClick)
set_label = bgcanvas.create_text(200, 210, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

file_text = bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
FileBut = Button(windowrt, image=buttonImage, borderwidth=0, command=fileClick)
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

def opening():
    images = []
    def create_rectangle(x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = windowrt.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            images.append(ImageTk.PhotoImage(image))
            img = bgcanvas.create_image(x1, y1, image=images[-1], anchor='nw')
        rect = bgcanvas.create_rectangle(x1, y1, x2, y2, **kwargs)
        return (img,rect)

    bushImage = ImageTk.PhotoImage(Image.open("gui/bush.png"))
    logoImage = ImageTk.PhotoImage(Image.open("gui/icon.ico"))

    alp = 1
    img = create_rectangle(0,0,1280,720,fill="white",alpha=alp)
    bush1 = bgcanvas.create_image(80,30, anchor=W, image=bushImage)
    bush2 = bgcanvas.create_image(-3000,0, anchor=W, image=bushImage)
    logo = bgcanvas.create_image(640,360, image=logoImage)
    logodim = 256
    bgcanvas.update()
    for i in range(40):
        time.sleep(0.001)
        bgcanvas.move(bush1, 40, 0)
        bgcanvas.delete(logo)
        if i > 20:
            bgcanvas.move(bush2, -40, 0)
            logodim -= 5
        else:
            logodim += 5
        logoImage = ImageTk.PhotoImage(Image.open("gui/icon.ico").resize((logodim,logodim)))
        logo = bgcanvas.create_image(640,360, image=logoImage)
        bgcanvas.update()
    bgcanvas.delete(bush1)
    bgcanvas.delete(bush2)
    bgcanvas.delete(logo)

    counter = 0
    while alp > 0:
        counter += 1
        alp -= 0.05
        time.sleep(0.001)
        bgcanvas.delete(img[0])
        bgcanvas.delete(img[1])
        img = create_rectangle(0,0,1280,720,fill="white",alpha=alp)
        bgcanvas.update()
        if counter == 3:
            global set_button
            global file_button
            set_button = bgcanvas.create_window(100, 220, anchor = W, window=SetBut)
            file_button = bgcanvas.create_window(100, 350, anchor = W, window=FileBut)
    images = []

opening()
mainloop()


