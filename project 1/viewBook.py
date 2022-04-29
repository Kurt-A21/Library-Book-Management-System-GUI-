import sqlite3
from tkinter import *
from tkinter import messagebox

#Connect to database
con = sqlite3.connect("library book management.db")
cur = con.cursor()

#Table Names
bookTable = "books" 

def viewBookList(): 
    
    window = Tk()
    window.title("Library Book Management System ")
    window.iconbitmap("Images/contents.ico")
    window.state("normal")
    window.geometry("460x450")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    
    #Background Colour
    Canvas1 = Canvas(window) 
    Canvas1.config(bg="#AA336A")
    Canvas1.pack(expand=True,fill=BOTH)
    
    #Label
    headingFrame1 = Frame(window,bg="pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Book List", bg='pink', fg='black', font = ('Arial',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Frame
    labelFrame = Frame(window, bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "SELECT * FROM "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch items from database")
    
    exitBtn = Button(window,text="Exit",bg='white', fg='black', command=window.destroy)
    exitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
    
