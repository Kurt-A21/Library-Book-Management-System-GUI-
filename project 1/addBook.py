import sqlite3
from tkinter import *
from tkinter import messagebox

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "INSERT INTO "+bookTable+" VALUES ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)
    window.destroy()
    
def addBook(): 
    
    global bookInfo1
    global bookInfo2
    global bookInfo3
    global bookInfo4
    global Canvas1
    global con
    global cur
    global bookTable
    global window
    
    window = Tk()
    window.title("Library Book Management System ")
    window.iconbitmap("Images/contents.ico")
    window.state("normal")
    window.geometry("460x450")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    
    #Connect to database
    con = sqlite3.connect("library book management.db")
    cur = con.cursor()
    
    #Table Names
    bookTable = "books"
    
    #Background Colour
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#AA336A")
    Canvas1.pack(expand=True,fill=BOTH)
        
    #Label
    headingFrame1 = Frame(window,bg="pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='pink', fg='black', font=('Arial',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Frame
    labelFrame = Frame(window)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #Book ID
    lb1 = Label(labelFrame,text="Book ID", fg='black')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title", fg='black')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author", fg='black')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued)", fg='black')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.4,rely=0.65, relwidth=0.52, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(window,text="SUBMIT",fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    exitBtn = Button(window,text="Exit",fg='black', command=window.destroy)
    exitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
