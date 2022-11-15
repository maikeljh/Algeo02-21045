from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from os import _exit
from time import time, sleep
from datetime import timedelta
from numpy import asarray
import cv2

import main_algo as algo

#globar var
FontType = "Calibri Light"
Folderdir = ""
Imagedir = ""
Fullscreen = False
viewFinderRes = 350
cameraStandbytime = 15
cameraCapturetime = 10

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
            execute(0)
    else:
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
        bgcanvas.itemconfig(result_image, image=resultImg)
        bgcanvas.itemconfig(set_label, text="No Folder Chosen") 
        bgcanvas.itemconfig(output_label, text="None")
        bgcanvas.itemconfig(timer_label, text="00.00")
        Folderdir = folder_path
    return

def fileClick():
    image_path = filedialog.askopenfilename()
    global testImg
    global resultImg
    global Folderdir
    global Imagedir
    global bgcanvas
    if image_path != "":
        testImg = ImageTk.PhotoImage(Image.open(image_path).resize((viewFinderRes,viewFinderRes)))
        bgcanvas.itemconfig(file_label, text=image_path)
        bgcanvas.itemconfig(test_image, image=testImg)
        Imagedir = image_path
        if Folderdir == "":
            resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(output_label, text="None")
            bgcanvas.itemconfig(result_image, image=resultImg)
            bgcanvas.itemconfig(timer_label, text="00.00")
        else:
            execute(0)
    else:
        testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
        bgcanvas.itemconfig(file_label, text="No File Chosen")
        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
        
        bgcanvas.itemconfig(result_image, image=resultImg)
        bgcanvas.itemconfig(test_image, image=testImg)
        bgcanvas.itemconfig(output_label, text="None")
        bgcanvas.itemconfig(timer_label, text="00.00")
        Imagedir = image_path
    return

def execute(feed):
    global resultImg
    global Folderdir
    global Imagedir
    global resultFace

    global videostart
    if not videostart:
        resultArray, time_elapsed, filename = algo.main_algo(Folderdir, Imagedir)
        resultArray = asarray(resultArray)
        resultFace = Image.fromarray(resultArray).resize((viewFinderRes,viewFinderRes))
        resultImg = ImageTk.PhotoImage(image=resultFace)

        timerResult = str(timedelta(milliseconds=time_elapsed*1000))

        bgcanvas.itemconfig(result_image, image=resultImg)
        bgcanvas.itemconfig(timer_label, text=timerResult)
        bgcanvas.itemconfig(output_label, text=filename)
    else:
        resultArray, time_elapsed, filename = algo.camera_algo(Folderdir, feed)
        resultArray = asarray(resultArray)
        resultFace = Image.fromarray(resultArray).resize((viewFinderRes,viewFinderRes))
        resultImg = ImageTk.PhotoImage(image=resultFace)

        timerResult = str(timedelta(milliseconds=time_elapsed*1000))

        bgcanvas.itemconfig(result_image, image=resultImg)
        bgcanvas.itemconfig(timer_label, text=timerResult)
        bgcanvas.itemconfig(output_label, text=filename)


#setup
overlay = Tk()
overlay.attributes("-alpha",0.0)
windowrt = Toplevel(overlay)
windowrt.title("GUI")
windowrt.geometry("1280x720")
windowrt.overrideredirect(1)
bgcanvas = Canvas(windowrt)

def onRootIconify(event):
    windowrt.withdraw()
overlay.bind("<Unmap>", onRootIconify)
def onRootDeiconify(event):
    windowrt.deiconify()
overlay.bind("<Map>", onRootDeiconify)

#assets
bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((1280,720)))
buttonImage = PhotoImage(file='gui/buttonshl.png',width=80,height=30)
buttonImageHl = PhotoImage(file='gui/buttons.png',width=80,height=30)
buttonImageOff = PhotoImage(file='gui/buttonsoff.png',width=80,height=30)
minimImage = PhotoImage(file='gui/customminimize.png',width=20,height=20)
closeImage = PhotoImage(file='gui/customclose.png',width=20,height=20)
closeImageHl = PhotoImage(file='gui/customclosehl.png',width=20,height=20)
fullImage = PhotoImage(file='gui/customfull.png',width=20,height=20)
winImage = PhotoImage(file='gui/customwindow.png',width=20,height=20)
nullImg = PhotoImage(file='gui/nullImg.png',width=1,height=1)
noImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
logoImg = ImageTk.PhotoImage(Image.open("gui/icon.ico").resize((50,50)))
logoImgHl = ImageTk.PhotoImage(Image.open("gui/iconhl.ico").resize((50,50)))
handleMark = ImageTk.PhotoImage(Image.open("gui/nullImg.png").resize((1280,30)))


camera = ImageTk.PhotoImage(Image.open("gui/camera.png").resize((30,30)))
cameraHl = ImageTk.PhotoImage(Image.open("gui/camerahl.png").resize((30,30)))
cameraClose = ImageTk.PhotoImage(Image.open("gui/cameraclose.png").resize((30,30)))
cameraCloseHl = ImageTk.PhotoImage(Image.open("gui/cameraclosehl.png").resize((30,30)))


testImg = noImg
resultImg = noImg

#custom handle
handle = Label(windowrt,height=28,width=1280,image=nullImg, bg="#AADDFF")

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
    overlay.iconify()
def close():
    closing()
    _exit(0)

handle.bind("<ButtonPress-1>", start_move)
handle.bind("<ButtonRelease-1>", stop_move)
handle.bind("<B1-Motion>", do_move)

#fitur fullscreen
def fullify():
    global Fullscreen
    if Fullscreen == False:
        Fullscreen = True
        formervid = videostart
        if formervid:
            stopVideo()

        widthval = windowrt.winfo_screenwidth()
        heightval = windowrt.winfo_screenheight()
        windowrt.geometry("%dx%d+0+0"%(widthval,heightval))
        full_button.config(image=winImage,command=winify)
        handle.config(width=widthval)
        minimize_button.place(x=widthval-150,y=0)
        full_button.place(x=widthval-100,y=0)
        close_button.place(x=widthval-50,y=0)

        global viewFinderRes
        viewFinderRes = widthval*350//1280

        global Imagedir
        global Folderdir
        global testImg
        global resultImg
        global testImg
        global resultImg
        global resultFace
        
        
        global bgImage
        bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((widthval,heightval)))
        bgcanvas.itemconfig(background,image=bgImage)

        newdst1 = heightval*60//720
        newdst2 = heightval*50//720
        newdst3 = widthval*300//1280
        newdst4 = widthval*400//1280
        newdst5 = widthval*170//1280

        bgcanvas.coords(title_text, widthval/2, 40)#bgcanvas.create_text(640, 40, anchor = N, text="Face Recognition", font=(FontType, 36))
        bgcanvas.coords(title_line, 50, 110, widthval-50, 110)#bgcanvas.create_line(50,110,1230,110, width=2)
        #Left Inset
        bgcanvas.coords(set_text, 100, 110+newdst1)#bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
        bgcanvas.coords(set_button, 100, 160+newdst1)#bgcanvas.create_window(100, 220, anchor = W, window=set_button)
        bgcanvas.coords(set_label, 200, 150+newdst1)#bgcanvas.create_text(200, 220, anchor = W, text="No File Chosen", font=(FontType, 12),width=170)
        bgcanvas.itemconfig(set_label, width=newdst5)

        bgcanvas.coords(file_text, 100, 240+newdst1)#bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
        bgcanvas.coords(file_button, 100, 290+newdst1)#bgcanvas.create_window(100, 350, anchor = W, window=file_button)
        bgcanvas.coords(file_label, 200, 280+newdst1)#bgcanvas.create_text(200, 350, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)
        bgcanvas.itemconfig(file_label, width=newdst5)

        bgcanvas.coords(result_label, 100, 390+newdst1)#bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
        bgcanvas.coords(output_label, 130, 440+newdst1)#bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01D901")
        
        #Main viewfinder
        bgcanvas.coords(test_image_label, 100+newdst3, 110+newdst2)#bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
        bgcanvas.coords(test_image, 100+newdst3, 120+newdst2)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
        bgcanvas.coords(result_image_label, 100+newdst3+newdst4, 110+newdst2)#bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
        bgcanvas.coords(result_image, 100+newdst3+newdst4, 120+newdst2)#bgcanvas.create_image(800,160, anchor=NW, image=testImg)
        
        bgcanvas.coords(capture_image_label, 100+newdst3, 130+newdst2+viewFinderRes)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
        #timer
        bgcanvas.coords(timer_title, 100+newdst3, 190+newdst2+viewFinderRes)#bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
        bgcanvas.coords(timer_label, 230+newdst3, 191+newdst2+viewFinderRes)#bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")

        bgcanvas.coords(logo_credits, widthval-80, heightval-80)
        bgcanvas.coords(camera_button, 285, 240+newdst1)#camera_button = bgcanvas.create_image(275, 300, anchor=W, image=camera)

        global handleMark
        handleMark = ImageTk.PhotoImage(Image.open("gui/nullImg.png").resize((widthval,30)))
        bgcanvas.itemconfig(handle_location, image=handleMark)

        global creditsRolled
        if creditsRolled:
            global bushImage
            global mascotImage
            global text1
            global text2
            global text3
            global text4

            newdst6 = heightval*100//720

            if heightval/720 > widthval/1280:
                fontsz1 = 48*widthval//1280
                fontsz2 = 28*widthval//1280
            else:
                fontsz1 = 48*heightval//720
                fontsz2 = 28*heightval//720
            
            bushImage = ImageTk.PhotoImage(Image.open("gui/bushalt.png"))
            bgcanvas.itemconfig(bush_bg, image = bushImage)
            bgcanvas.coords(bush_bg, -475, -600)

            bgcanvas.coords(text1, 40, 50)
            bgcanvas.coords(text2, 40, 50+1*newdst6)
            bgcanvas.coords(text3, 40, 50+2*newdst6)
            bgcanvas.coords(text4, 40, 50+3*newdst6)
            bgcanvas.itemconfig(text1, font=("Kristen ITC", fontsz1))
            bgcanvas.itemconfig(text2, font=("Kristen ITC", fontsz2))
            bgcanvas.itemconfig(text3, font=("Kristen ITC", fontsz2))
            bgcanvas.itemconfig(text4, font=("Kristen ITC", fontsz2))

            mascotImage = ImageTk.PhotoImage(Image.open("gui/mascot.png").resize((widthval*428//1280, heightval*1218//720)))
            bgcanvas.coords(mascot_img, widthval-(29*(widthval*10//1280)), 100)
            bgcanvas.itemconfig(mascot_img, image=mascotImage)

        if Imagedir != "" and Folderdir != "":
            resultFace = resultFace.resize((viewFinderRes,viewFinderRes))
            resultImg = ImageTk.PhotoImage(image=resultFace)
            bgcanvas.itemconfig(result_image, image=resultImg)
        else:
            resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(result_image, image=resultImg)

        if Imagedir == "":
            testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(test_image, image=testImg)
        else:
            testImg = ImageTk.PhotoImage(Image.open(Imagedir).resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(test_image, image=testImg)

        if formervid:
            startVideo()

def winify():
    global Fullscreen
    if Fullscreen == True:
        Fullscreen = False
        formervid = videostart
        if formervid:
            stopVideo()

        widthval = 1280
        heightval = 720
        windowrt.geometry("%dx%d"%(widthval,heightval))
        full_button.config(image=fullImage,command=fullify)
        handle.config(width=1280)
        minimize_button.place(x=1130,y=0)
        full_button.place(x=1180,y=0)
        close_button.place(x=1230,y=0)

        global viewFinderRes
        viewFinderRes = 350

        global Imagedir
        global Folderdir
        global testImg
        global resultImg
        global testImg
        global resultImg
        global resultFace
        
        

        global bgImage
        bgImage = ImageTk.PhotoImage(Image.open("gui/bg.png").resize((1280,720)))
        bgcanvas.itemconfig(background,image=bgImage)

        bgcanvas.coords(title_text, 630, 40)#bgcanvas.create_text(640, 40, anchor = N, text="Face Recognition", font=(FontType, 36))
        bgcanvas.coords(title_line, 50, 110, 1230, 110)#bgcanvas.create_line(50,110,1230,110, width=2)
        #Left Inset
        bgcanvas.coords(set_text, 100, 170)#bgcanvas.create_text(100, 170, anchor = W, text="Insert Your Dataset", font=(FontType, 18))
        bgcanvas.coords(set_button, 100, 220)#bgcanvas.create_window(100, 220, anchor = W, window=set_button)
        bgcanvas.coords(set_label, 200, 210)#bgcanvas.create_text(200, 210, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)
        bgcanvas.itemconfig(set_label, width=170)

        bgcanvas.coords(file_text, 100, 300)#bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
        bgcanvas.coords(file_button, 100, 350)#bgcanvas.create_window(100, 350, anchor = W, window=file_button)
        bgcanvas.coords(file_label, 200, 340)#bgcanvas.create_text(200, 340, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)
        bgcanvas.itemconfig(file_label, width=170)

        bgcanvas.coords(result_label, 100, 450)#bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
        bgcanvas.coords(output_label, 130, 490)#bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01D901")
        
        #Main viewfinder
        bgcanvas.coords(test_image_label, 400, 150)#bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
        bgcanvas.coords(test_image, 400, 160)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
        bgcanvas.coords(result_image_label, 800, 150)#bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
        bgcanvas.coords(result_image, 800, 160)#bgcanvas.create_image(800,160, anchor=NW, image=testImg)

        bgcanvas.coords(capture_image_label, 400, 520)#bgcanvas.create_image(400,160, anchor=NW, image=testImg)
        #timer
        bgcanvas.coords(timer_title, 400, 580)#bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
        bgcanvas.coords(timer_label, 531, 581)#bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01E901")

        bgcanvas.coords(logo_credits, 1200, 640)
        bgcanvas.coords(camera_button, 285, 300)

        global handleMark
        handleMark = ImageTk.PhotoImage(Image.open("gui/nullImg.png").resize((1280,30)))
        bgcanvas.itemconfig(handle_location, image=handleMark)

        global creditsRolled
        if creditsRolled:
            global bushImage
            global mascotImage
            global text1
            global text2
            global text3
            global text4
            
            bushImage = ImageTk.PhotoImage(Image.open("gui/bushalt.png").resize((2011,1000)))
            bgcanvas.itemconfig(bush_bg, image = bushImage)
            bgcanvas.coords(bush_bg, -340, -200)

            bgcanvas.coords(text1, 40, 50)
            bgcanvas.coords(text2, 40, 150)
            bgcanvas.coords(text3, 40, 250)
            bgcanvas.coords(text4, 40, 350)
            bgcanvas.itemconfig(text1, font=("Kristen ITC", 48))
            bgcanvas.itemconfig(text2, font=("Kristen ITC", 28))
            bgcanvas.itemconfig(text3, font=("Kristen ITC", 28))
            bgcanvas.itemconfig(text4, font=("Kristen ITC", 28))

            mascotImage = ImageTk.PhotoImage(Image.open("gui/mascot.png"))
            bgcanvas.coords(mascot_img, widthval-300, 100)
            bgcanvas.itemconfig(mascot_img, image=mascotImage)

        if Imagedir != "" and Folderdir != "":
            resultFace = resultFace.resize((viewFinderRes,viewFinderRes))
            resultImg = ImageTk.PhotoImage(image=resultFace)
            bgcanvas.itemconfig(result_image, image=resultImg)
        else:
            resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(result_image, image=resultImg)

        if Imagedir == "":
            testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(test_image, image=testImg)
        else:
            testImg = ImageTk.PhotoImage(Image.open(Imagedir).resize((viewFinderRes,viewFinderRes)))
            bgcanvas.itemconfig(test_image, image=testImg)

        if formervid:
            startVideo()


#custom window buttons
def highlight(event):
    event.widget['background'] = '#99CCEE'
    showHandle(event)
def highlightClose(event):
    event.widget['image'] = closeImageHl
    event.widget['background'] = '#FF7799'
    showHandle(event)
def unhighlight(event):
    event.widget['background'] = '#AADDFF'
    hideHandle(event)
def unhighlightClose(event):
    event.widget['image'] = closeImage
    event.widget['background'] = '#AADDFF'
    hideHandle(event)

minimize_button = Button(windowrt, image=minimImage, borderwidth=0, command=minimize, bg="#AADDFF",width=50,height=30)
close_button = Button(windowrt, image=closeImage, borderwidth=0, command=close, bg="#AADDFF",width=50,height=30)
full_button = Button(windowrt, image=fullImage, borderwidth=0, command=fullify, bg="#AADDFF",width=50,height=30)

minimize_button.bind("<Enter>", highlight)
minimize_button.bind("<Leave>", unhighlight)
close_button.bind("<Enter>", highlightClose)
close_button.bind("<Leave>", unhighlightClose)
full_button.bind("<Enter>", highlight)
full_button.bind("<Leave>", unhighlight)


#MAIN
#taskbar
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
set_button = bgcanvas.create_image(100, 220, anchor=W, image=buttonImage)
set_label = bgcanvas.create_text(200, 210, anchor = NW, text="No Folder Chosen", font=(FontType, 12),width=170)

file_text = bgcanvas.create_text(100, 300, anchor = W, text="Insert Your Image", font=(FontType, 18))
file_button = bgcanvas.create_image(100, 350, anchor=W, image=buttonImage)
file_label = bgcanvas.create_text(200, 340, anchor = NW, text="No File Chosen", font=(FontType, 12),width=170)

result_label = bgcanvas.create_text(100, 450, anchor = W, text="Result", font=(FontType, 18))
output_label = bgcanvas.create_text(130, 490, anchor = W, text="None", font=(FontType, 18), fill="#01DA01")
#Main viewfinder
test_image_label = bgcanvas.create_text(400, 150, anchor = W, text="Test Image", font=(FontType, 14))
test_image = bgcanvas.create_image(400,160, anchor=NW, image=testImg)
result_image_label = bgcanvas.create_text(800, 150, anchor = W, text="Result Image", font=(FontType, 14))
result_image = bgcanvas.create_image(800,160, anchor=NW, image=testImg)

capture_image_label = bgcanvas.create_text(400, 520, anchor = W, text="", font=(FontType, 14))
#timer
timer_title = bgcanvas.create_text(400, 580, anchor = W, text="Execution Time:", font=(FontType, 14))
timer_label = bgcanvas.create_text(530, 581, anchor = W, text="00.00", font=(FontType, 15), fill="#01FA01")

#logo credits
logo_credits = bgcanvas.create_image(1200,640,anchor=NW,image=logoImg)
camera_button = bgcanvas.create_image(285, 300, anchor=W, image=camera)

handle_location = bgcanvas.create_image(0,0,anchor=NW,image=handleMark)

#Custom Buttons
def highlightSetbtn(event):
    bgcanvas.itemconfig(set_button, image=buttonImageHl)
def unhighlightSetbtn(event):
    bgcanvas.itemconfig(set_button, image=buttonImage)
def buttonclickSet(event):
    bgcanvas.move(set_button, -2, 2)
    windowrt.update()
    sleep(0.01)
    bgcanvas.move(set_button, 2, -2)
    setClick()
def highlightFilebtn(event):
    if not videostart:
        bgcanvas.itemconfig(file_button, image=buttonImageHl)
def unhighlightFilebtn(event):
    if not videostart:
        bgcanvas.itemconfig(file_button, image=buttonImage)
def buttonclickFile(event):
    if not videostart:
        bgcanvas.move(file_button, -5, 5)
        windowrt.update()
        sleep(0.01)
        bgcanvas.move(file_button, 5, -5)
        fileClick()

bgcanvas.tag_bind(set_button, '<Enter>', highlightSetbtn)     
bgcanvas.tag_bind(set_button, '<Leave>', unhighlightSetbtn)
bgcanvas.tag_bind(set_button, '<ButtonPress-1>', buttonclickSet)

bgcanvas.tag_bind(file_button, '<Enter>', highlightFilebtn)     
bgcanvas.tag_bind(file_button, '<Leave>', unhighlightFilebtn)
bgcanvas.tag_bind(file_button, '<ButtonPress-1>', buttonclickFile)

#Hide taskbar
def showHandle(event):
    handle.place(y=0)
    minimize_button.place(y=0)
    full_button.place(y=0)
    close_button.place(y=0)
def hideHandle(event):
    global Fullscreen
    if Fullscreen == True:
        handle.place(y=-30)
        minimize_button.place(y=-30)
        full_button.place(y=-30)
        close_button.place(y=-30)

bgcanvas.tag_bind(handle_location, '<Enter>', showHandle)
handle.bind('<Leave>', hideHandle)

#buatvideo
creditsRolled = False
def highlightCred(event):
    bgcanvas.itemconfig(logo_credits, image=logoImgHl)
def unhighlightCred(event):
    bgcanvas.itemconfig(logo_credits, image=logoImg)
def rollcred(event):
    bgcanvas.move(logo_credits, -2, 2)
    windowrt.update()
    sleep(0.01)
    bgcanvas.move(logo_credits, 2, -2)

    global creditsRolled
    global bush_bg
    global text1
    global text2
    global text3
    global text4

    global mascot_img
    
    if not creditsRolled:
        creditsRolled = True
        if not Fullscreen:
            bushImage = ImageTk.PhotoImage(Image.open("gui/bushalt.png").resize((2011,1000)))
            mascotImage = ImageTk.PhotoImage(Image.open("gui/mascot.png"))
            bush_bg = bgcanvas.create_image(1280,-200, image=bushImage, anchor=NW)
            mascot_img = bgcanvas.create_image(1250,100, image=mascotImage, anchor=NW)

            bgcanvas.tag_raise(handle_location)
            

            for i in range(27):
                bgcanvas.move(bush_bg, -60, 0)
                bgcanvas.move(mascot_img, -10, 0)
                windowrt.update()
            #target mascot = 980, 100

            text1 = bgcanvas.create_text(-500, 50, anchor = NW, text="#TeamOnodera", font=("Kristen ITC", 48))
            text2 = bgcanvas.create_text(-500, 150, anchor = NW, text="Fakhri Muhammad Mahendra      13521045", font=("Kristen ITC", 28))
            text3 = bgcanvas.create_text(-500, 250, anchor = NW, text="Muhamad Aji Wibisono          13521095", font=("Kristen ITC", 28))
            text4 = bgcanvas.create_text(-500, 350, anchor = NW, text="Michael Jonathan Halim        13521124", font=("Kristen ITC", 28))

            for i in range(20):
                bgcanvas.move(text1, 27, 0)
                bgcanvas.move(text2, 27, 0)
                bgcanvas.move(text3, 27, 0)
                bgcanvas.move(text4, 27, 0)
                windowrt.update()

        
        else:
            heightval = windowrt.winfo_screenheight()
            widthval = windowrt.winfo_screenwidth()
            newdist1 = heightval*100//720
            newspd1 = widthval*10//1280

            if heightval/720 > widthval/1280:
                fontsz1 = 48*widthval//1280
                fontsz2 = 28*widthval//1280
            else:
                fontsz1 = 48*heightval//720
                fontsz2 = 28*heightval//720

            bushImage = ImageTk.PhotoImage(Image.open("gui/bushalt.png"))
            mascotImage = ImageTk.PhotoImage(Image.open("gui/mascot.png").resize((widthval*428//1280, heightval*1218//720)))
            bush_bg = bgcanvas.create_image(1280,-600, image=bushImage, anchor=NW)
            mascot_img = bgcanvas.create_image(widthval-30, 100, image=mascotImage, anchor=NW)

            bgcanvas.tag_raise(handle_location)
            bgcanvas.tag_raise(logo_credits)

            for i in range(27):
                bgcanvas.move(bush_bg, -65, 0)
                bgcanvas.move(mascot_img, -newspd1, 0)
                windowrt.update()
            #target mascot = widthval-300, 100

            text1 = bgcanvas.create_text(-1040, 50, anchor = NW, text="#TeamOnodera", font=("Kristen ITC", fontsz1))
            text2 = bgcanvas.create_text(-1040, 50+newdist1, anchor = NW, text="Fakhri Muhammad Mahendra      13521045", font=("Kristen ITC", fontsz2))
            text3 = bgcanvas.create_text(-1040, 50+2*newdist1, anchor = NW, text="Muhamad Aji Wibisono          13521095", font=("Kristen ITC", fontsz2))
            text4 = bgcanvas.create_text(-1040, 50+3*newdist1, anchor = NW, text="Michael Jonathan Halim        13521124", font=("Kristen ITC", fontsz2))
            
            for i in range(20):
                bgcanvas.move(text1, 54, 0)
                bgcanvas.move(text2, 54, 0)
                bgcanvas.move(text3, 54, 0)
                bgcanvas.move(text4, 54, 0)
                windowrt.update()
            #target = -475,-600

        bgcanvas.tag_raise(logo_credits)
        while creditsRolled:
            windowrt.update()

    else:
        bgcanvas.tag_lower(logo_credits)
        creditsRolled = False
        if not Fullscreen:
            for i in range(20):
                bgcanvas.move(text1, -27, 0)
                bgcanvas.move(text2, -27, 0)
                bgcanvas.move(text3, -27, 0)
                bgcanvas.move(text4, -27, 0)
                windowrt.update()
            bgcanvas.delete(text1)
            bgcanvas.delete(text2)
            bgcanvas.delete(text3)
            bgcanvas.delete(text4)
            for i in range(27):
                bgcanvas.move(bush_bg, 60, 0)
                windowrt.update()
            bgcanvas.delete(bush_bg)
            bgcanvas.delete(mascot_img)
        
        else:
            for i in range(20):
                bgcanvas.move(text1, -54, 0)
                bgcanvas.move(text2, -54, 0)
                bgcanvas.move(text3, -54, 0)
                bgcanvas.move(text4, -54, 0)
                windowrt.update()
            bgcanvas.delete(text1)
            bgcanvas.delete(text2)
            bgcanvas.delete(text3)
            bgcanvas.delete(text4)
            for i in range(27):
                bgcanvas.move(bush_bg, 120, 0)
                windowrt.update()
            bgcanvas.delete(bush_bg)
            bgcanvas.delete(mascot_img)
        bgcanvas.tag_raise(logo_credits)

bgcanvas.tag_bind(logo_credits, '<Enter>', highlightCred)
bgcanvas.tag_bind(logo_credits, '<Leave>', unhighlightCred)
bgcanvas.tag_bind(logo_credits, '<ButtonPress-1>', rollcred)

#Bonus Video feed
videofeed = "none"
videostart = False
def startVideo():    
    try:
        global Imagedir
        global Folderdir
        global videostart
        global videofeed
        global testImg
        videostart = True
        Imagedir = ""

        resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
        bgcanvas.itemconfig(result_image, image=resultImg)
        
        videoCap = cv2.VideoCapture(0)
        approxstartW = videoCap.get(cv2.CAP_PROP_FRAME_WIDTH) // 2 - viewFinderRes // 2
        approxstartH =  videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2 - viewFinderRes // 2
        if viewFinderRes <= videoCap.get(cv2.CAP_PROP_FRAME_WIDTH) and viewFinderRes <= videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT):
            approxstartW = videoCap.get(cv2.CAP_PROP_FRAME_WIDTH) // 2 - viewFinderRes // 2
            approxstartH =  videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2 - viewFinderRes // 2
            plusval = viewFinderRes
        else:
            if approxstartH < 0:
                approxstartH = 0
            if approxstartW < 0:
                approxstartW = 0
            plusval = min(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH), videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        bgcanvas.itemconfig(file_label, text="Camera Feed")
        bgcanvas.itemconfig(file_button, image=buttonImageOff)
        bgcanvas.itemconfig(camera_button, image=cameraClose)

        cachedTime = time()
        captured = False
        while videostart:
            cachedTime2 = time()
            _,frame = videoCap.read()
            frame = cv2.flip(frame,1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            testImg = Image.fromarray(cv2image).crop([approxstartW,approxstartH,approxstartW+plusval,approxstartH+plusval]).resize([viewFinderRes,viewFinderRes])

            videofeed = ImageTk.PhotoImage(image=testImg)
            bgcanvas.itemconfig(test_image, image=videofeed)
            windowrt.update()

            if Folderdir != "":
                if (cachedTime2 - cachedTime > cameraCapturetime + cameraStandbytime):
                    cachedTime = cachedTime2
                    captured = False
                elif (cachedTime2 - cachedTime > cameraCapturetime):
                    if not captured:
                        captured = True
                        bgcanvas.itemconfig(capture_image_label, text="Captured")
                        feedArray = asarray(testImg)
                        feed = algo.cb.videoToMatrix(feedArray)
                        execute(feed)
                        
                elif(cachedTime2 - cachedTime > 9 and cachedTime2 - cachedTime < 10):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 1")
                elif(cachedTime2 - cachedTime > 8 and cachedTime2 - cachedTime < 9):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 2")
                elif(cachedTime2 - cachedTime > 7 and cachedTime2 - cachedTime < 8):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 3")
                elif(cachedTime2 - cachedTime > 6 and cachedTime2 - cachedTime < 7):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 4")
                elif(cachedTime2 - cachedTime > 5 and cachedTime2 - cachedTime < 6):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 5")
                elif(cachedTime2 - cachedTime > 4 and cachedTime2 - cachedTime < 5):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 6")
                elif(cachedTime2 - cachedTime > 3 and cachedTime2 - cachedTime < 4):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 7")
                elif(cachedTime2 - cachedTime > 2 and cachedTime2 - cachedTime < 3):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 8")
                elif(cachedTime2 - cachedTime > 1 and cachedTime2 - cachedTime < 2):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 9")
                elif(cachedTime2 - cachedTime > 0 and cachedTime2 - cachedTime < 1):
                    bgcanvas.itemconfig(capture_image_label, text="Capturing: 10")
            else:
                cachedTime = time()
                bgcanvas.itemconfig(capture_image_label, text="")
    except:
        bgcanvas.itemconfig(capture_image_label, text="")
        print(Exception)
        stopVideo()
        videofeed = "fail"

    bgcanvas.itemconfig(capture_image_label, text="")

def stopVideo():
    global videostart
    global testImg
    global resultImg
    videostart = False
    bgcanvas.itemconfig(file_label, text="No File Chosen")
    testImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))
    resultImg = ImageTk.PhotoImage(Image.open("gui/noimage.jpg").resize((viewFinderRes,viewFinderRes)))

    bgcanvas.itemconfig(output_label, text="None")
    bgcanvas.itemconfig(timer_label, text="00.00")
    bgcanvas.itemconfig(test_image, image=testImg)
    bgcanvas.itemconfig(result_image, image=resultImg)
    bgcanvas.itemconfig(file_button, image=buttonImage)
    bgcanvas.itemconfig(camera_button, image=camera)

    bgcanvas.itemconfig(capture_image_label, text="")

def highlightCam(event):
    global videostart
    if videostart:
        bgcanvas.itemconfig(camera_button, image=cameraCloseHl)
    else:
        bgcanvas.itemconfig(camera_button, image=cameraHl)
def unhighlightCam(event):
    global videostart
    if videostart:
        bgcanvas.itemconfig(camera_button, image=cameraClose)
    else:
        bgcanvas.itemconfig(camera_button, image=camera)
def cameraPress(event):
    bgcanvas.move(camera_button, -2, 2)
    windowrt.update()
    sleep(0.01)
    bgcanvas.move(camera_button, 2, -2)
    if not videostart:
        startVideo()
    else:
        stopVideo()
    
bgcanvas.tag_bind(camera_button, '<Enter>', highlightCam)
bgcanvas.tag_bind(camera_button, '<Leave>', unhighlightCam)
bgcanvas.tag_bind(camera_button, '<ButtonPress-1>', cameraPress)

#pack
bgcanvas.pack(fill="both", expand=True)


#splash screen
def opening():
    global Fullscreen
    Fullscreen = True
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
    windowrt.update()
    for i in range(40):
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
        windowrt.update()
    bgcanvas.delete(bush1)
    bgcanvas.delete(bush2)
    bgcanvas.delete(logo)

    while alp > 0:
        alp -= 0.05
        bgcanvas.delete(img)
        img = editalpha(0,0,1280,720,fill="white",alpha=alp)
        windowrt.update()
    bgcanvas.delete(img)
    images.clear()
    Fullscreen = False

#closing screen
def closing():
    global Fullscreen
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

    if Fullscreen == False:
        Fullscreen = True

        alp = 0
        img = editalpha(0,0,1280,720,fill="white",alpha=alp)
        windowrt.update()

        while alp < 1:
            alp += 0.15
            bgcanvas.delete(img)
            img = editalpha(0,0,1280,720,fill="white",alpha=alp)
            windowrt.update()
        
        bgcanvas.delete(img)
        images.clear()

    else:
        Fullscreen = False

        alp = 0
        img = editalpha(0,0,windowrt.winfo_screenwidth(),windowrt.winfo_screenheight(),fill="white",alpha=alp)
        windowrt.update()

        while alp < 1:
            alp += 0.15
            bgcanvas.delete(img)
            img = editalpha(0,0,windowrt.winfo_screenwidth(),windowrt.winfo_screenheight(),fill="white",alpha=alp)
            windowrt.update()
        
        bgcanvas.delete(img)
        images.clear()

#main
opening()
window = Frame(master=overlay)
window.mainloop()

