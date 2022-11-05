from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("GUI")
root.geometry("1280x720")
root.resizable(0, 0)

global dir
dir = " "

def setClick():
    folder_path = filedialog.askdirectory()
    setLabel.config(text=folder_path)
    global dir
    dir = folder_path
    print(dir)
    return

def fileClick():
    folder_path = filedialog.askopenfilename()
    FileLabel.config(text=folder_path)
    global testImg
    global resultImg
    testImg = ImageTk.PhotoImage(Image.open(folder_path).resize((350,350)))
    testImgDis = Label(image=testImg)

    if dir == " ":
        resultImg = ImageTk.PhotoImage(Image.open("noimage.jpg").resize((350,350)))
        resultImgDis = Label(image=resultImg)
        resultImgDis.grid(row=3, column=4, rowspan=10, sticky=W, pady=(0, 0))
    else:
        execute()
    
    testImgDis.grid(row=3, column=1, rowspan=10, sticky=W, pady=(0, 0))
    return

def execute():
    return

#label test
titleLabel = Label(root, text="Face Recognition", font=("Calibri Light", 36))
titleUnderScore =Canvas(root, height=15, width=1280)
titleUnderScore.create_line(50,0,1230,0, width=15)


setTitle = Label(root, text="Insert Your Dataset", font=("Calibri Light", 18))
SetBut = Button(root, text="Choose File", command=setClick)
setLabel = Label(root, text="No File Chosen", font=("Calibri Light", 10), width=30, anchor='w')
FileTitle = Label(root, text="Insert Your Image", font=("Calibri Light", 18))
FileBut = Button(root, text="Choose File", command=fileClick)
FileLabel = Label(root, text="No File Chosen", font=("Calibri Light", 10), width=30, anchor='w')
resultLabel = Label(root, text="Result", font=("Calibri Light", 18))
outputLabel = Label(root, text="None", fg="#77D977", font=("Calibri Light", 18))

testImgLabel = Label(root, text="Test Image", font=("Calibri Light", 10))
testImg = ImageTk.PhotoImage(Image.open("noimage.jpg").resize((350,350)))
testImgDis = Label(image=testImg)
resultImgLabel = Label(root, text="Closest Result", font=("Calibri Light", 10))
resultImg = ImageTk.PhotoImage(Image.open("noimage.jpg").resize((350,350)))
resultImgDis = Label(image=testImg)


timerTitle = Label(root, text="Execution Time: ", font=("Calibri Light", 14))
timerLabel = Label(root, text="00.00", fg="#77D977", font=("Calibri Light", 14))



titleLabel.grid(row=0, column=0, columnspan=7, sticky=N)
titleUnderScore.grid(row=1, column=0, columnspan=7, sticky=N)

setTitle.grid(row=2, column=0, sticky=NW, padx=(100, 0), pady=(50, 0))
SetBut.grid(row=3, column=0, sticky=W, padx=(100, 0), pady=(10, 0))
setLabel.grid(row=3, column=0, sticky=W, padx=(200, 0), pady=(10, 0))

FileTitle.grid(row=4, column=0, sticky=W, padx=(100, 0), pady=(20, 0))
FileBut.grid(row=5, column=0, sticky=W, padx=(100, 0), pady=(10, 0))
FileLabel.grid(row=5, column=0, sticky=W, padx=(200, 0), pady=(10, 0))

resultLabel.grid(row=6, column=0, sticky=W, padx=(100, 0), pady=(50, 0))
outputLabel.grid(row=7, column=0, sticky=W, padx=(120, 0), pady=(0, 0))

testImgLabel.grid(row=2, column=1, columnspan=3, sticky=W, pady=(50, 0))
testImgDis.grid(row=3, column=1, rowspan=10, sticky=W, pady=(0, 0))
resultImgLabel.grid(row=2, column=4, columnspan=3, sticky=W, pady=(50, 0))
resultImgDis.grid(row=3, column=4, rowspan=10, sticky=W, pady=(0, 0))

timerTitle.grid(row=13, column=1, columnspan=3, sticky=W, pady=(50, 0))
timerLabel.grid(row=13, column=1, columnspan=3, sticky=W, pady=(52, 0), padx=(130,0))

root.mainloop()

