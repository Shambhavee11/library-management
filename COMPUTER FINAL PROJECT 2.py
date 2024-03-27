from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_db():


    global id
    global title
    global author

    bid=id.get()
    btitle=title.get()
    bauthor=author.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
    cursor = db.cursor()
    
    print(bid,end='--')
    print(btitle,end='--')
    print(bauthor,end='--')
    print("add")

    sqlquery= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES');"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book added Successfully")
    except:
        messagebox.showinfo("Error","Cannot add given book data into Database")
    
    window.destroy()

def addBooks():

    global id
    global title
    global author

    window=Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Add Books")
    greet.grid(row = 0,columnspan = 3)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    #----------title-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Title: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    title=Entry(window,width=5,font =('arial', 15, 'bold'))
    title.grid(row=4,column=3)

    #----------author-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Author: ")
    L.grid(row = 6, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)

    author=Entry(window,width=5,font =('arial', 15, 'bold'))
    author.grid(row=6,column=3)
    
    submitbtn=Button(window,text="Submit",command=add_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("add")
    pass

def delete_db():

    global id

    bid=id.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
    cursor = db.cursor()
    
    print(bid,end='--')
    print("delete")

    sqlquery= "delete from books where bid='"+bid+"';"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book deleted Successfully")
    except:
        messagebox.showinfo("Error","Book with given id does not exist")
    
    window.destroy()

def deleteBooks():

    global id

    window=Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Delete Books")
    greet.grid(row = 0,columnspan = 3)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    submitbtn=Button(window,text="Submit",command=delete_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("delete")
    pass

def viewBooks():

    global id

    window=Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "View Books")
    greet.grid(row = 0,columnspan = 3)

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
    cursor = db.cursor()

    sqlquery= "select * from books ;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        # db.commit()
        L = Label(window, font = ('arial', 20), text = "%-10s%-20s%-20s%-20s"%('BID','Title','Author','Available'))
        L.grid(row = 1,columnspan = 4)

        L = Label(window, font = ('arial', 20), text = "----------------------------------------------------------------")
        L.grid(row = 2,columnspan = 4)

        x=4
        for i in cursor:
            L = Label(window, font = ('arial', 15), text = "%-10s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3]))
            L.grid(row = x,columnspan = 4)
            x+=1   

    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass

def issue_db():

    global id
    global StudentName

    bid=id.get()
    bStudentName=StudentName.get()

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
    cursor = db.cursor()
    
    print(bid,end='--')
    print(bStudentName,end='--')
    print("issue")

    try:
        checkavailability=" select * from books where available='YES';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag=0

        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='NO' where bid='"+bid +"';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery= "insert into issue values('" + bid +"','" +bStudentName+"' );"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success',"Book issued Successfully")
        else:
            messagebox.showinfo("Error","Required Book is not available")
    except:
        messagebox.showinfo("Error","Cannot issue given book ")
    
def issueBooks():

    global id
    global StudentName

    window=Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Issue Books")
    greet.grid(row = 0,columnspan = 3)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    #----------StudentName-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter StudentName: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    StudentName=Entry(window,width=5,font =('arial', 15, 'bold'))
    StudentName.grid(row=4,column=3)
    
    submitbtn=Button(window,text="Submit",command=issue_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("issue")
    pass

def return_db():

    global id

    bid=id.get()

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
    cursor = db.cursor()
    
    print(bid,end='--')
    print("return")

    try:
        checkavailability=" select * from books where available='NO';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag=0

        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='YES' where bid='"+bid +"';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery= "delete from issue where bid='" + bid +"';"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success',"Book returned Successfully")
        else:
            messagebox.showinfo("Error","Invalid Book id")
    except:
        messagebox.showinfo("Error","Cannot return given book ")
    
def returnBooks():

    global id

    window=Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Return Books")
    greet.grid(row = 0,columnspan = 3)

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    
    submitbtn=Button(window,text="Submit",command=return_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("return")
    pass

#----------------------------------------------------MAIN PROGRAM------------------------------------------------------

db = mysql.connector.connect(host ="localhost",user = "root",password = 'Sakurajimamai123#',database='Computer_Project')
cursor = db.cursor()

window=Tk()
window.title("ProjectGurukul Library Management System")

greet = Label(window, font = ('arial', 30, 'bold'), text = "Welcome to ProjectGurukul!")
greet.grid(row = 0,columnspan = 3)

addbtn=Button(window,text="Add Books",command=addBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
addbtn.grid(row=3,columnspan=3)

deletebtn=Button(window,text="Delete Books",command=deleteBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
deletebtn.grid(row=5,columnspan=3)

issuebtn=Button(window,text="Issue Books",command=issueBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
issuebtn.grid(row=7,columnspan=3)

returnbtn=Button(window,text="Return Books",command=returnBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
returnbtn.grid(row=9,columnspan=3)

viewbtn=Button(window,text="View Books",command=viewBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
viewbtn.grid(row=11,columnspan=3)

greet = Label(window, font = ('arial', 15, 'bold'), text = "Thank you")
greet.grid(row = 13,columnspan = 3)

window.mainloop()
