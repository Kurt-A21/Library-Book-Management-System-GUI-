import sqlite3
from tkinter import *
from tkinter import messagebox

#Connect to database
con = sqlite3.connect("library book management.db")
cur = con.cursor()

#Table Names
issueTable = "books_issued" 
bookTable = "books"

#Store book id
all_bookID = [] 

def issue():
    
    global issueBtn
    global labelFrame
    global lb1
    global inf1
    global inf2
    global exitBtn
    global window
    global Canvas1
    global status
    
    bookID = inf1.get()
    issueto = inf2.get()
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extract_bookID = "SELECT bid FROM "+bookTable
    try:
        cur.execute(extract_bookID)
        con.commit()
        for i in cur:
            all_bookID.append(i[0])
        
        if bookID in all_bookID:
            checkAvail = "SELECT status FROM "+bookTable+" WHERE bid = '"+bookID+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not in Database")
    except:
        messagebox.showinfo("Error","Can't fetch Book ID")
    
    issueSql = "INSERT INTO "+issueTable+" VALUES ('"+bookID+"','"+issueto+"')"
    show = "SELECT * FROM "+issueTable
    
    updateStatus = "UPDATE "+bookTable+" SET status = 'issued' WHERE bid = '"+bookID+"'"
    try:
        if bookID in all_bookID and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            window.destroy()
        else:
            all_bookID.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            window.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is incorret\nTry again")
        
    print(bookID)
    print(issueto)
    
    all_bookID.clear()
    
def issueBook(): 
    
    global issueBtn
    global labelFrame
    global lb1
    global inf1
    global inf2
    global exitBtn
    global window
    global Canvas1
    global status
    
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
    headingLabel = Label(headingFrame1, text="Issue Book", bg='pink', fg='black', font=('Arial',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Frame
    labelFrame = Frame(window)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    #Book ID
    lb1 = Label(labelFrame,text="Book ID", fg='black')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #Issue book to
    lb2 = Label(labelFrame,text="Issued To", fg='black')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    #Issue Button
    issueBtn = Button(window,text="Issue",bg='white', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    exitBtn = Button(window,text="Exit",bg='white', fg='black', command=window.destroy)
    exitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()   