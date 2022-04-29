import sqlite3
from tkinter import *
from tkinter import messagebox

#Connect to database
con = sqlite3.connect("library book management.db")
cur = con.cursor()

#Table Names
issueTable = "books_issued" 
bookTable = "books"

def deleteBook():
    
    bookID = bookInfo1.get()
    
    deleteSql = "DELETE FROM "+bookTable+" WHERE bid = '"+bookID+"'"
    deleteIssue = "DELETE FROM "+issueTable+" WHERE bid = '"+bookID+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    
    print(bookID)
    bookInfo1.delete(0, END)
    window.destroy()
    
def delete(): 
    
    global bookInfo1
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
    
    #Background Colour
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#AA336A")
    Canvas1.pack(expand=True,fill=BOTH)
        
    #Label
    headingFrame1 = Frame(window,bg="pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Book", bg='pink', fg='black', font=('Arial',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Frame
    labelFrame = Frame(window)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    #Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID",fg='black')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='white', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    exitBtn = Button(window,text="Exit",bg='white', fg='black', command=window.destroy)
    exitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()