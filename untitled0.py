from tkinter import *
from PIL import ImageTK,Image
from datetime import datetime
import pytz
import time


root = Tk()
root.geometry("600x600")
clockImage = ImageTK.Photoimage(Image.open("download.png"))

labelIndia = label(root, text = "India")
labelIndia.place(relx =0.2, rely = 0.5, anchor = Center)


labelIndiaImg = Label(root)
labelIndiaImg["image"] = clockImage
labelIndiaImg.place(relx =0.2, rely = 0.35, anchor = Center)

labelIndiaTime = Label(root, text = "Time:")
labelIndiaTime.place(relx = 0.2, rely = 0.65)



labelUSA = Label(root, text = "USA")
labelUSA.place(relx =0.7, rely = 0.5, anchor = Center)


LabelUsaImage = Label(root)
LabelUsaImage["image"] = clockImage
LabelUsaImage.place(relx =0.7, rely = 0.35, anchor = Center)

labelUsaTime = Label(root, text = "Time:")
labelUsaTime.place(relx = 0.7, rely = 0.65)


class India():
    def time(self):
        home = pytz.timezone("Asia/Kolkota")
        localTime = datatime.now(home)
        currentTime = localTime.strftime("%H:%M:%S")
        labelUsaTime["text"] = "Time:"+currentTime
        labelUsaTime.after(200,self.times)
        
class Usa():
    def time(self):
        home = pytz.timezone("US/Central")
        localTime = datatime.now(home)
        currentTime = localTime.strftime("%H:%M:%S")
        labelIndiaTime["text"] = "Time:"+currentTime
        labelIndiaTime.after(200,self.times)
        
objIndia = India()
objUsa = Usa()
indiaBtn = Button(root,text = "Show Time", command = objIndia.time)
india.place(relx = 0.2, rely = 0.8, anchor = CENTER)
usaBtn = Button(root,text = "Show Time", command = objUsa.time)
usaBtn.place(relx = 0.7, rely = 0.8, anchor = CENTER)
root.mainloop()
