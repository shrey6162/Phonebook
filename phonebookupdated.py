import sqlite3
from tkinter import *
from tkinter.messagebox import *

root1=Tk()
root1.geometry('750x400')

Label(root1,text='Project Title:Phone Book',font='Verdana 18 bold').grid(row=0,column=0)
Label(root1,text='Project of python and database',font='Verdana 15 bold').grid(row=1,column=2)
Label(root1,text='Developed By: Shrey Nigam',fg='blue',font='Verdana 15 bold').grid(row=2,column=2)
Label(root1,text='--------------------------------',fg='blue',font='Verdana 12 bold').grid(row=3,column=2)
Label(root1,text='make mouse movement over this screen to close',fg='red',font='Verdana 10 bold').grid(row=4,column=2)
def close(e=1):
    root1.destroy()
root1.bind('<Motion>',close)    
    
root1.mainloop()

root=Tk()
root.geometry('450x400')
con=sqlite3.Connection('Phonebook.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Phonebook(contact_id INTEGER PRIMARY KEY AUTOINCREMENT, fname varchar(10), mname varchar(10), lname varchar(10), company TEXT, address TEXT, city TEXT, pin INTEGER, website_url TEXT, birth_date DATE)")
cur.execute("CREATE TABLE IF NOT EXISTS Phoneno(contact_id INTEGER, phone_type INTEGER, phone_no INTEGER, phone_no1 INTEGER, FOREIGN KEY (contact_id) references Phonebook (contact_id))")
cur.execute("CREATE TABLE IF NOT EXISTS Emailid(contact_id INTEGER, email_type INTEGER, email_id TEXT, email_id1 TEXT, FOREIGN KEY (contact_id) references Phonebook (contact_id))")
con.commit()

def insert():
    a=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
    cur.execute("INSERT INTO Phonebook (fname,mname,lname,company,address,city,pin,website_url,birth_date) VALUES (?,?,?,?,?,?,?,?,?)",a)
    cur.execute("SELECT contact_id from Phonebook")
    tup1=cur.fetchall()
    if v1.get()==1:
        b="Office"
    elif v1.get()==2:
        b="Home"
    elif v1.get()==3:
        b="Mobile"
    elif v1.get()==0:
        b=''
    c=(tup1[len(tup1)-1][0],b,e11.get())
    cur.execute("INSERT INTO Phoneno (contact_id,phone_type,phone_no) values (?,?,?)",c)
    if v2.get()==1:
        f="Office"
    elif v2.get()==2:
        f="Personal"
    elif v2.get()==0:
        f=''
    g=(tup1[len(tup1)-1][0],f,e13.get())
    cur.execute("INSERT INTO Emailid (contact_id,email_type,email_id) values (?,?,?)",g)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)
    e13.delete(0,END)
    v1.set(0)
    v2.set(0)
    con.commit()
    showinfo("response","record succesfully saved")

Label(root,text='PHONEBOOK',fg='blue',font='Verdana 22 bold').grid(row=0,columnspan=3)

Label(root,text='First Name').grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)

Label(root,text='Middle Name').grid(row=2,column=0)
e2=Entry(root)
e2.grid(row=2,column=1)

Label(root,text='Last Name').grid(row=3,column=0)
e3=Entry(root)
e3.grid(row=3,column=1)

Label(root,text='Company Name').grid(row=4,column=0)
e4=Entry(root)
e4.grid(row=4,column=1)

Label(root,text='Address').grid(row=5,column=0)
e5=Entry(root)
e5.grid(row=5,column=1)

Label(root,text='City').grid(row=6,column=0)
e6=Entry(root)
e6.grid(row=6,column=1)

Label(root,text='Pin Code').grid(row=7,column=0)
e7=Entry(root)
e7.grid(row=7,column=1)

Label(root,text='Website URL').grid(row=8,column=0)
e8=Entry(root)
e8.grid(row=8,column=1)

Label(root,text='Date of Birth').grid(row=9,column=0)
e9=Entry(root)
e9.grid(row=9,column=1)

Label(root,text='Select Phone Type:',fg='blue',font='Times 12').grid(row=10,column=0)
v1=IntVar()
r=Radiobutton(root,text='Office',variable=v1,value=1)
r.grid(row=10,column=1)
r1=Radiobutton(root,text='Home',variable=v1,value=2)
r1.grid(row=10,column=2)
r2=Radiobutton(root,text='Mobile',variable=v1,value=3)
r2.grid(row=10,column=3)

Label(root,text='Phone Number').grid(row=11,column=0)
e11=Entry(root)
e11.grid(row=11,column=1)
def choice():
    e111=Entry(root)
    e111.grid(row=11,column=3)
Button(root,text='+',command=choice).grid(row=11,column=2)

Label(root,text='Select Email Type:',fg='blue',font='Times 12').grid(row=12,column=0)
v2=IntVar()
r3=Radiobutton(root,text='Office',variable=v2,value=1)
r3.grid(row=12,column=1)
r4=Radiobutton(root,text='Personal',variable=v2,value=2)
r4.grid(row=12,column=2)

Label(root,text='Email Id').grid(row=13,column=0)
e13=Entry(root)
e13.grid(row=13,column=1)
def choice():
    e131=Entry(root)
    e131.grid(row=13,column=3)
Button(root,text='+',command=choice).grid(row=13,column=2)
    
Button(root,text='Save',command=insert).grid(row=14,column=0)

def search():
    root2=Tk()
    root2.geometry('400x400')
    Label(root2,text='Searching Phone Book',bg='blue',font='Times 15 bold').grid(row=0,columnspan=3)
    Label(root2,text='Enter name:').grid(row=1,column=0)
    z=Entry(root2)
    z.grid(row=1,column=1)
    z1=Listbox(root2,width=80,height=20)
    z1.grid(row=2,columnspan=4)
    cur.execute("SELECT contact_id, fname, mname,lname from Phonebook order by fname")
    index=[]
    global r1
    r1=cur.fetchall()
    for i in range(len(r1)):
        z1.insert(END,str(r1[i][1])+" "+str(r1[i][2])+" "+str(r1[i][3]))
    def info(e=1):
        index=int(z1.curselection()[0])
        name=str(z1.get(ANCHOR))
        cur.execute("SELECT * FROM Phonebook WHERE contact_id=?",(str(r1[index][0]),))
        row1=cur.fetchall()
        cur.execute("SELECT * FROM Phoneno WHERE contact_id=?",(str(r1[index][0]),))
        row2=cur.fetchall()
        cur.execute("SELECT * FROM Emailid WHERE contact_id=?",(str(r1[index][0]),))
        row3=cur.fetchall()
        z2=Listbox(root2,width=80,height=20)
        z2.grid(row=2,columnspan=4)

        fname=str(row1[0][1])
        mname=str(row1[0][2])
        lname=str(row1[0][3])
        company=str(row1[0][4])
        address=str(row1[0][5])
        city=str(row1[0][6])
        pin=str(row1[0][7])
        website_url=str(row1[0][8])
        birth_date=str(row1[0][9])
        phone_type=str(row2[0][1])
        phone_no=str(row2[0][2])
        email_type=str(row3[0][1])
        email_id=str(row3[0][2])

        z2.insert(END,"Name= "+fname+" "+mname+" "+lname)
        z2.insert(1,"Comapny= "+company)
        z2.insert(2,"Address= "+address)
        z2.insert(3,"City= "+city)
        z2.insert(4,"Pin= "+pin)
        z2.insert(5,"Website= "+website_url)
        z2.insert(6,"Dob= "+birth_date)
        z2.insert(7,"phone type="+phone_type)
        z2.insert(8,"phone number= "+phone_no)
        z2.insert(9,"email type= "+email_type)
        z2.insert(10,"email= "+email_id)

        def delete():
            
            cur.execute("delete from Phonebook where contact_id=?",(str(r1[index][0]),))
            cur.fetchall()
            cur.execute("delete from Phoneno where contact_id=?",(str(r1[index][0]),))
            cur.fetchall()
            cur.execute("delete from Emailid where contact_id=?",(str(r1[index][0]),))
            cur.fetchall()
            con.commit()
            showinfo("response","Record Deleted From Phonebook")
            z2.delete(0,10)

        Button(root2,text="Delete",command=delete).grid(row=3,column=2)
        

        def update():
            index=int(z1.curselection()[0])
            cur.execute("delete from Phonebook where contact_id=?",(str(r1[index][0]),))
            cur.execute("delete from Phoneno where contact_id=?",(str(r1[index][0]),))
            cur.execute("delete from Emailid where contact_id=?",(str(r1[index][0]),))
            e1.insert(0,str(row1[0][1]))
            e2.insert(0,str(row1[0][2]))
            e3.insert(0,str(row1[0][3]))
            e4.insert(0,str(row1[0][4]))
            e5.insert(0,str(row1[0][5]))
            e6.insert(0,str(row1[0][6]))
            e7.insert(0,str(row1[0][7]))
            e8.insert(0,str(row1[0][8]))
            e9.insert(0,str(row1[0][9]))
            e11.insert(0,str(row2[0][1]))
            e13.insert(0,str(row3[0][1]))
            root2.destroy()

        Button(root2,text="Update",command=update).grid(row=3,column=0)

    def search1(e=1):
        item=z.get()
        cur.execute("SELECT fname,mname,lname from Phonebook WHERE (fname LIKE (?)) or (fname LIKE (?)) or (fname LIKE (?))",(item+"%","%"+item+"%","%"+item))
        r2=cur.fetchall()
        print (r2)
        z1.delete(0,END)
        for i in range(len(r2)):
            z1.insert(END,str(r2[i][0])+" "+str(r2[i][1])+" "+str(r2[i][2]))
    root2.bind("<KeyPress>",search1)
    z1.bind("<Double-Button-1>",info)
    def close(e=1):
        root2.destroy()

    Button(root2,text='Close',command=close).grid(row=3,columnspan=3)
    root2.mainloop()
    
Button(root,text='Search',command=search).grid(row=14,column=1)

def edit():
    search()
    cur.execute("delete from Phonebook where contact_id=?",(str(r1[index][0]),))
    cur.execute("delete from Phoneno where contact_id=?",(str(r1[index][0]),))
    cur.execute("delete from Emailid where contact_id=?",(str(r1[index][0]),))
    e1.insert(0,str(row1[0][1]))
    e2.insert(0,str(row1[0][2]))
    e3.insert(0,str(row1[0][3]))
    e4.insert(0,str(row1[0][4]))
    e5.insert(0,str(row1[0][5]))
    e6.insert(0,str(row1[0][6]))
    e7.insert(0,str(row1[0][7]))
    e8.insert(0,str(row1[0][8]))
    e9.insert(0,str(row1[0][9]))
    e11.insert(0,str(row2[0][1]))
    e13.insert(0,str(row3[0][1]))
    root.destroy()
    def update():
        info()
        Button(root,text="Update",command=update).grid(row=3,columnspan=1)
Button(root,text="Edit",command=edit).grid(row=14,column=3)

def close(e=1):
    root.destroy()

Button(root,text='Close',command=close).grid(row=14,column=2)



root.mainloop()
