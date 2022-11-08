from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from time import sleep
from os import _exit

#globar var
FontType = "Calibri Light"
Folderdir = ""
Imagedir = ""
Fullscreen = False
viewfinderRes = 350

#keperluan backend
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
        testImg = ImageTk.PhotoImage(Image.open(image_path).resize((viewfinderRes,viewfinderRes)))
        bgcanvas.itemconfig(test_image, image=testImg)
        bgcanvas.itemconfig(file_label, text=image_path)
        Imagedir = image_path
    else:
        testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))

    if Folderdir == "":
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
        bgcanvas.itemconfig(result_image, image=noImg)
    else:
        execute()
    return

def execute():
    return


#setup
windowrt = Tk()
windowrt.title("GUI")
windowrt.iconbitmap("gui/icon.ico")
windowrt.geometry("1280x720")
windowrt.overrideredirect(True)

#assets
bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((1280,720)))
buttonImage = PhotoImage(file='gui/buttons.png',width=80,height=30)
minimImage = PhotoImage(file='gui/customminimize.png',width=20,height=20)
closeImage = PhotoImage(file='gui/customclose.png',width=20,height=20)
closeImageHl = PhotoImage(file='gui/customclosehl.png',width=20,height=20)
fullImage = PhotoImage(file='gui/customfull.png',width=20,height=20)
winImage = PhotoImage(file='gui/customwindow.png',width=20,height=20)
nullImg = PhotoImage(file='gui/nullImg.png',width=1,height=1)
noImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
testImg = noImg
resultImg = noImg

bgcanvas = Canvas(windowrt)

#custom handle
handle = Label(windowrt,height=28,width=1280,image=nullImg, bg="#AADDFF")
handle.pack_propagate(0)
def start_move(event):
    if Fullscreen == False:
        windowrt.x = event.x
        windowrt.y = event.y
def stop_move(event):
    if Fullscreen == False:
        windowrt.x = None
        windowrt.y = None
def do_move(event):
    if Fullscreen == False:
        deltax = event.x - windowrt.x
        deltay = event.y - windowrt.y
        x = windowrt.winfo_x() + deltax
        y = windowrt.winfo_y() + deltay
        windowrt.geometry(f"+{x}+{y}")
def minimize():
    windowrt.update_idletasks()
    windowrt.overrideredirect(False)
    windowrt.state('withdrawn')
    windowrt.state('iconic')
def frame_mapped(event):
    windowrt.update_idletasks()
    windowrt.overrideredirect(True)
    windowrt.state('normal')
def close():
    _exit(0)
def highlight(event):
    event.widget['background'] = '#99CCEE'
def highlightClose(event):
    event.widget['image'] = closeImageHl
    event.widget['background'] = '#FF7799'
def unhighlight(event):
    event.widget['background'] = '#AADDFF'
def unhighlightClose(event):
    event.widget['image'] = closeImage
    event.widget['background'] = '#AADDFF'

#fitur fullscreen
def fullify():
    global Fullscreen
    Fullscreen = True

    widthval = windowrt.winfo_screenwidth()
    heightval = windowrt.winfo_screenheight()
    windowrt.geometry("%dx%d+0+0"%(widthval,heightval))
    full_button.config(image=winImage,command=winify)
    handle.config(width=widthval)
    minimize_button.place(x=widthval-150,y=0)
    full_button.place(x=widthval-100,y=0)
    close_button.place(x=widthval-50,y=0)

    global viewfinderRes
    viewfinderRes = heightval*350//720

    global Imagedir
    global Folderdir
    global testImg
    global resultImg
    if Imagedir != "":
        testImg = ImageTk.PhotoImage(Image.open(Imagedir).resize((viewfinderRes,viewfinderRes)))
    else:
        testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
    bgcanvas.itemconfig(test_image, image=testImg)

    if Folderdir == "":
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
        bgcanvas.itemconfig(result_image, image=noImg)
    else:
        execute()
    bgcanvas.itemconfig(result_image, image=resultImg)

    global bgImage
    bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((widthval,heightval)))
    bgcanvas.itemconfig(background,image=bgImage)

    newdst1 = heightval*60//720
    newdst2 = heightval*80//720
    newdst3 = heightval*100//720
    
    newdst4 = widthval*300/1280
    newdst5 = widthval*400/1280

    newdst6 = heightval*50/720
    newdst7 = heightval*420/720

    bgcanvas.coords(title_text, widthval/2, 40)#bgcanvas.create_text(640, 40, anchor = N, text="Face Recognition", font=(FontType, 36))
    bgcanvas.coords(title_line, 50, 110, widthval-50, 110)#bgcanvas.create_line(50,110,1230,110, width=2)
    #Left Inset
    bgcanvas.coords(set_text, 100, 110+newdst1)#bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
    bgcanvas.coords(set_button, 100, 160+newdst1)#bgcanvas.create_window(100, 220, anchor = W, window=SetBut)
    bgcanvas.coords(set_label, 200, 160+newdst1)#bgcanvas.create_text(200, 220, anchor = W, text="No File Chosen", font=(FontType, 12),width=170)

    bgcanvas.coords(file_text, 100, 160+newdst1+newdst2)#bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
    bgcanvas.coords(file_button, 100, 210+newdst1+newdst2)#bgcanvas.create_window(100, 350, anchor = W, window=FileBut)
    bgcanvas.coords(file_label, 200, 210+newdst1+newdst2)#bgcanvas.create_text(200, 350, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

    bgcanvas.coords(result_label, 100, 210+newdst1+newdst2+newdst3)#bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
    bgcanvas.coords(output_label, 130, 250+newdst1+newdst2+newdst3)#bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01D901")
    
    #Main viewfinder
    bgcanvas.coords(test_image_label, 100+newdst4, 110+newdst6)#bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
    bgcanvas.coords(test_image, 100+newdst4, 120+newdst6)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
    bgcanvas.coords(result_image_label, 100+newdst4+newdst5, 110+newdst6)#bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
    bgcanvas.coords(result_image, 100+newdst4+newdst5, 120+newdst6)#bgcanvas.create_image(800,160, anchor=NW, image=testImg)
    
    #timer
    bgcanvas.coords(timer_title, 100+newdst4, 120+newdst6+newdst7)#bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
    bgcanvas.coords(timer_label, 230+newdst4, 121+newdst6+newdst7)#bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")
    
    

def winify():
    global Fullscreen
    Fullscreen = False

    widthval = 1280
    heightval = 720
    windowrt.geometry("%dx%d"%(widthval,heightval))
    full_button.config(image=fullImage,command=fullify)
    handle.config(width=1280)
    minimize_button.place(x=1130,y=0)
    full_button.place(x=1180,y=0)
    close_button.place(x=1230,y=0)

    global viewfinderRes
    viewfinderRes = 350

    global Imagedir
    global Folderdir
    global testImg
    global resultImg
    if Imagedir != "":
        testImg = ImageTk.PhotoImage(Image.open(Imagedir).resize((viewfinderRes,viewfinderRes)))
    else:
        testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
    bgcanvas.itemconfig(test_image, image=testImg)

    if Folderdir == "":
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewfinderRes,viewfinderRes)))
        bgcanvas.itemconfig(result_image, image=noImg)
    else:
        execute()
    bgcanvas.itemconfig(result_image, image=resultImg)

    global bgImage
    bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((1280,720)))
    bgcanvas.itemconfig(background,image=bgImage)

    bgcanvas.coords(title_text, 630, 40)#bgcanvas.create_text(640, 40, anchor = N, text="Face Recognition", font=(FontType, 36))
    bgcanvas.coords(title_line, 50, 110, 1230, 110)#bgcanvas.create_line(50,110,1230,110, width=2)
    #Left Inset
    bgcanvas.coords(set_text, 100, 170)#bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
    bgcanvas.coords(set_button, 100, 220)#bgcanvas.create_window(100, 220, anchor = W, window=SetBut)
    bgcanvas.coords(set_label, 200, 220)#bgcanvas.create_text(200, 220, anchor = W, text="No File Chosen", font=(FontType, 12),width=170)

    bgcanvas.coords(file_text, 100, 300)#bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
    bgcanvas.coords(file_button, 100, 350)#bgcanvas.create_window(100, 350, anchor = W, window=FileBut)
    bgcanvas.coords(file_label, 200, 350)#bgcanvas.create_text(200, 350, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

    bgcanvas.coords(result_label, 100, 450)#bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
    bgcanvas.coords(output_label, 130, 490)#bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01D901")
    
    #Main viewfinder
    bgcanvas.coords(test_image_label, 400, 150)#bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
    bgcanvas.coords(test_image, 400, 160)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
    bgcanvas.coords(result_image_label, 800, 150)#bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
    bgcanvas.coords(result_image, 800, 160)#bgcanvas.create_image(800,160, anchor=NW, image=testImg)
    
    #timer
    bgcanvas.coords(timer_title, 400, 580)#bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
    bgcanvas.coords(timer_label, 531, 581)#bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")
    

handle.bind("<ButtonPress-1>", start_move)
handle.bind("<ButtonRelease-1>", stop_move)
handle.bind("<B1-Motion>", do_move)
handle.bind("<Map>",frame_mapped)

minimize_button = Button(windowrt, image=minimImage, borderwidth=0, command=minimize, bg="#AADDFF",width=50,height=30)
close_button = Button(windowrt, image=closeImage, borderwidth=0, command=close, bg="#AADDFF",width=50,height=30)
full_button = Button(windowrt, image=fullImage, borderwidth=0, command=fullify, bg="#AADDFF",width=50,height=30)

minimize_button.bind("<Enter>", highlight)
minimize_button.bind("<Leave>", unhighlight)
close_button.bind("<Enter>", highlightClose)
close_button.bind("<Leave>", unhighlightClose)
full_button.bind("<Enter>", highlight)
full_button.bind("<Leave>", unhighlight)

handle.place(x=0,y=0)
minimize_button.place(x=1130,y=0)
full_button.place(x=1180,y=0)
close_button.place(x=1230,y=0)



#background
background = bgcanvas.create_image(0,0,image=bgImage,anchor="nw")
#Header
title_text = bgcanvas.create_text(640, 40, anchor = N, text="Face Recognition", font=(FontType, 36))
title_line = bgcanvas.create_line(50,110,1230,110, width=2)
#Left Inset
set_text = bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
SetBut = Button(windowrt, image=buttonImage, borderwidth=0, command=setClick)
set_label = bgcanvas.create_text(200, 220, anchor = W, text="No File Chosen", font=(FontType, 12),width=170)

file_text = bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
FileBut = Button(windowrt, image=buttonImage, borderwidth=0, command=fileClick)
file_label = bgcanvas.create_text(200, 350, anchor = W, text="No File Chosen", font=(FontType, 12),width=170)

result_label = bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
output_label = bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01D901")
#Main viewfinder
test_image_label = bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
test_image = bgcanvas.create_image(400,160, anchor=NW, image=testImg)
result_image_label = bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
result_image = bgcanvas.create_image(800,160, anchor=NW, image=testImg)
#timer
timer_title = bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
timer_label = bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")

bgcanvas.pack(fill="both", expand=True)
#splash screen
def opening():
    images = []
    def editalpha(x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = windowrt.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            images.append(ImageTk.PhotoImage(image))
            img = bgcanvas.create_image(x1, y1, image=images[-1], anchor='nw')
        return img

    bushImage = ImageTk.PhotoImage(Image.open("gui/bush.png"))
    logoImage = ImageTk.PhotoImage(Image.open("gui/icon.ico"))

    alp = 1
    img = editalpha(0,0,1280,720,fill="white",alpha=alp)
    bush1 = bgcanvas.create_image(80,30, anchor=W, image=bushImage)
    bush2 = bgcanvas.create_image(-3000,0, anchor=W, image=bushImage)
    logo = bgcanvas.create_image(640,360, image=logoImage)
    logodim = 256
    angle = 0
    bgcanvas.update()
    for i in range(40):
        sleep(0.001)
        bgcanvas.move(bush1, 40, 0)
        bgcanvas.delete(logo)
        if i > 20:
            bgcanvas.move(bush2, -40, 0)
            logodim -= 5
        else:
            logodim += 5
        
        if i > 0 and i <=10:
            angle += 1
        elif i > 10 and i <=20:
            angle -= 1
        elif i > 20 and i <=30:
            angle += 1
        elif i > 30 and i <40:
            angle -= 1
        
        logoImage = ImageTk.PhotoImage(Image.open("gui/icon.ico").resize((logodim,logodim)).rotate(angle))
        logo = bgcanvas.create_image(640,360, image=logoImage)
        bgcanvas.update()
    bgcanvas.delete(bush1)
    bgcanvas.delete(bush2)
    bgcanvas.delete(logo)

    counter = 0
    while alp > 0:
        counter += 1
        alp -= 0.05
        sleep(0.001)
        bgcanvas.delete(img)
        img = editalpha(0,0,1280,720,fill="white",alpha=alp)
        bgcanvas.update()
        if counter == 3:
            global set_button
            global file_button
            set_button = bgcanvas.create_window(100, 220, anchor = W, window=SetBut)
            file_button = bgcanvas.create_window(100, 350, anchor = W, window=FileBut)
    images = []

#main
opening()
mainloop()


