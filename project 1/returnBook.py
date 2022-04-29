from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

#Connect to database
con = sqlite3.connect("library book management.db")
cur = con.cursor()

#Table Names
issueTable = "books_issued" 
bookTable = "books"

#Store book id
all_bookID = [] 


def returnB():
    
    global SubmitBtn
    global labelFrame
    global lb1
    global bookInfo1
    global exitBtn
    global window
    global Canvas1
    global status
    
    bid = bookInfo1.get()
    extractBid = "SELECT bid FROM "+issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            all_bookID.append(i[0])
        
        if bid in all_bookID:
            checkAvail = "SELECT status FROM "+bookTable+" WHERE bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not in Database")
    except:
        messagebox.showinfo("Error","Can't fetch Book ID")
    
    
    issueSql = "DELETE FROM "+issueTable+" WHERE bid = '"+bid+"'"
    
    print(bid in all_bookID)
    print(status)
    updateStatus = "UPDATE "+bookTable+" SET status = 'avail' WHERE bid = '"+bid+"'"
    try:
        if bid in all_bookID and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            all_bookID.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            window.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is incorret\nTry again")
    
    
    all_bookID.clear()
    window.destroy()
    
def reBook(): 
        
    global bookInfo1
    global SubmitBtn
    global exitBtn
    global Canvas1
    global con
    global cur
    global window
    global labelFrame
    global lb1
    
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
    
    
    #Lable  
    headingFrame1 = Frame(window,bg="pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='pink', fg='black', font=('Arial',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Frame
    labelFrame = Frame(window)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    #Book ID to Return
    lb1 = Label(labelFrame,text="Book ID", fg='black')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(window,text="Return",bg='white', fg='black',command=returnB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    exitBtn = Button(window,text="Exit",bg='white', fg='black', command=window.destroy)
    exitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
