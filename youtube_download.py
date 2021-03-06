from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DHIWAHAR_K_ADHITHYA")


Label(root,text = 'YOUTUBE VIDEO DOWNLOADER', font ='calibri 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'PASTE LINK HERE', font = 'calibri 20 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'calibri 20').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'calibri 20 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()
