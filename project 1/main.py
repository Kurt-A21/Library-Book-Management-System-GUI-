import sqlite3
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from addBook import *
from delBook import *
from viewBook import *
from issueBook import *
from returnBook import *

def show_frame(frame):
    frame.tkraise()

#SQL connect
con = sqlite3.connect("library book management.db")
cur = con.cursor()

#Table names
issueTable = "desc books_issued"
bookTable = "desc books"


#Store book ids
all_bookID = []

#Main window   
window = tk.Tk()
window.title("Library Book Management System ")
window.iconbitmap("Images/contents.ico")
window.state("normal")
window.geometry("460x450")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#Top created space
frame1_title = tk.Label(window)
frame1_title.pack(fill="x")
sp = tk.Label(window)
sp.pack(fill="x")

#Background image
bg1=PhotoImage(file="Images/bg_wallpaper1_600x500.png")
my_wallpaper = tk.Label(window, image=bg1)
my_wallpaper.place(x=0, y=0, relheight=1, relwidth=1)

#Main Menu Background Frame
bg_frame = LabelFrame(window, padx="5", pady="10", bg="white")
bg_frame.pack()

#Title image in background frame
title_img = ImageTk.PhotoImage(Image.open("Images/logo1_2_32.jpg"))
my_label = Label(bg_frame,image=title_img)
my_label.pack()


#Main menu buttons
#Add Book
btn_addB = tk.Button(bg_frame, text="Add Book", pady="10", fg="white", bg="#1735B6", command=addBook)
btn_addB.pack(fill="x")

#Issue Book
btn_issueB = tk.Button(bg_frame, text="Issue Book", pady="10", fg="white", bg="#1735B6",command=issueBook)
btn_issueB.pack(fill="x")

#Return Book
btn_returnB = tk.Button(bg_frame, text="Return Book", pady="10", fg="white", bg="#1735B6", command=reBook)
btn_returnB.pack(fill="x")

#Delete Book
btn_delB = tk.Button(bg_frame, text="Delete Book", pady="10",  fg="white", bg="#1735B6", command=delete)
btn_delB.pack(fill="x")

#View Book List
btn_viewBL = tk.Button(bg_frame, text="View Book List", pady="10", fg="white", bg="#1735B6", command=viewBookList)
btn_viewBL.pack(fill="x")

window.mainloop()