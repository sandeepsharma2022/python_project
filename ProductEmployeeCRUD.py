# Product Employee CRUD app 

from tkinter import*
from tkinter import messagebox
import mysql.connector

# creating window object , geometry and set title................
window=Tk()
window.geometry("800x350")
window.title("Employee CRUD app--(Made by SK SHARMA)")

# creating Methods................................................
def show():
    
    myDB=mysql.connector.connect(host="localhost", username="root", password="2002",database="employee")
    mycur=myDB.cursor()
    mycur.execute("select * from empDetails")

    rows=mycur.fetchall()
    list.delete(0,list.size())

    for row in rows:
        addData=str(row[0])+"  "+row[1]+"  "+row[2]

        list.insert(list.size()+1,addData)
    myDB.close()


# creating Methods................................................
# creating inserData Methods......................................
def insertData():
    # getching data.....
    id=enterID.get()
    name=enterName.get()
    dept=enterDept.get()

    if(id=="" or name=="" or dept==""):
        messagebox.showwarning("Error in data insertion", "please fill all the fiels to insert data")

    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="2002", database="employee")
       # myDB = mysql.connector.connect(host="localhost", user="<new_user>", passwd="<new_password>", database="employee")

        mycur=myDB.cursor()
        mycur.execute("insert into empdetails values('"+id+"','"+name+"','"+dept+"')")
        myDB.commit()

        enterID.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()
        messagebox.showinfo("Insert Status","Data inserted Successfully! ")
        myDB.close()

# creating updateData Methods................................................
def updateData():
    # getching data.....
    id=enterID.get()
    name=enterName.get()
    dept=enterDept.get()

    if(id=="" or name=="" or dept==""):
        messagebox.showwarning("Error in data filling", "please fill all the fiels:")

    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="2002", database="employee")
       # myDB = mysql.connector.connect(host="localhost", user="<new_user>", passwd="<new_password>", database="employee")

        mycur=myDB.cursor()
        mycur.execute("update empdetails set empName='"+name+"',empDept='"+dept+"' where empID='"+id+"'")
        myDB.commit()

        enterID.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()
        messagebox.showinfo("update Status","Data updated Successfully! ")
        myDB.close()

# creating getData Methods................................................
def getData():
    if(enterID.get()==""):
        messagebox.showwarning("fill id","please provide id:")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="2002",database="employee")
        mycur=myDB.cursor()
        mycur.execute("select * from empdetails where empID='"+enterID.get()+"'")
        rows=mycur.fetchall()
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])

        myDB.close()

# creating deleteData Methods................................................
def deleteData():
    if(enterID.get()==""):
        messagebox.showwarning("fill id","please provide id:")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="2002",database="employee")
        mycur=myDB.cursor()
        mycur.execute("delete from empdetails where empID='"+enterID.get()+"'")
        myDB.commit()

        enterID.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("delete status:"," data successfully deleted!")
        myDB.close()
# creating resetData Methods................................................
def resetData():
        enterID.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        list.delete(0,list.size())



# creating Text or Label........................................
empID=Label(window,text="Employee ID",font=("Serif",12))
empID.place(x=20,y=30)

empName=Label(window,text="Employee Name",font=("Serif",12))
empName.place(x=20,y=60)

empDept=Label(window,text="Employee Dept",font=("Serif",12))
empDept.place(x=20,y=90)

# creating Entry Field...........................................
enterID=Entry(window)
enterID.place(x=150,y=30)

enterName=Entry(window)
enterName.place(x=150,y=60)

enterDept=Entry(window)
enterDept.place(x=150,y=90)

# creating Buttons................................................
insertBtn=Button(window,text="Insert",font=("Serif",12),bg="blue",fg="white", command=insertData)
insertBtn.place(x=20,y=120)

updateBtn=Button(window,text="Update",font=("Serif",12),bg="blue",fg="white", command=updateData)
updateBtn.place(x=90,y=120)

fetchBtn=Button(window,text="Fetch",font=("Serif",12),bg="blue",fg="white", command=getData)
fetchBtn.place(x=175,y=120)

deleteBtn=Button(window,text="Delete",font=("Serif",12),bg="blue",fg="white", command=deleteData)
deleteBtn.place(x=20,y=180)

resetBtn=Button(window,text="Reset",font=("Serif",12),bg="blue",fg="white", command=resetData)
resetBtn.place(x=90,y=180)

# creating ListBox
list=Listbox(window)
list.place(x=300,y=30)



window.mainloop()

# this is the our GUI based small software which is developed by sksharma.