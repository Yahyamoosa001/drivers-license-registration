from tkinter import *
import datetime
import mysql.connector 
from tkinter import messagebox as MessageBox
import tkinter



##Window creation and rules png
window= Tk()
window.title("Driver's License Registration")
window.geometry("1920x1080")
window.configure(background="black")

canvas= Canvas(width=1920, height=1080)
canvas.pack()
photo=PhotoImage(file='C:\\Users\\yahya\\OneDrive\\Desktop\\Apex training centre\\bk6_copyii.png')
canvas.create_image(0, 0, image=photo, anchor=NW)
photo1=PhotoImage(file='C:\\Users\\yahya\\OneDrive\\Desktop\\Apex training centre\\rules 11.png')
canvas.create_image(1090,190, image=photo1, anchor=NW)



##def 
def register():
      try:
            age = int(t_age.get())
            cid=int(t_cid.get())
      except ValueError:
            MessageBox.showinfo("Driver's License Registration","Invalid input has been entered")

      try:
            dob=str(t_dob.get())
            format="%Y-%m-%d"
            datetime.datetime.strptime(dob,format)
      except ValueError:
            MessageBox.showinfo("driver's License Registration","Invalid date")

      name = t_name.get()
      age = t_age.get()
      dob= t_dob.get()
      nat = clicked.get()
      cid=t_cid.get()

      check=name.split(" ")
      for x in check:
          if not x.isalpha():
              MessageBox.showinfo("Driver's License Registration","Invalid name")
          else:
              if(name=="" or age=="" or dob=="" or nat=="" or cid==""):
                  MessageBox.showinfo("Driver's License Registration","All fields are required")
              elif(age<='17'):
                  MessageBox.showinfo("Driver's License Registration","Your age must be 18 or above")
              else:
                  con = mysql.connector.connect(host="localhost",user="root", password="root", database="tc2")
                  cursor = con.cursor()
                  cursor.execute("insert into list values('"+ name +"' , '"+ age +"' , '"+ dob +"' , '"+ nat +"' , '"+ cid +"')")
                  con.commit()

                  t_name.delete(0, len(name))
                  t_age.delete(0, len(age))
                  t_dob.delete(0, len(dob))
                  t_cid.delete(0, len(cid))
                  MessageBox.showinfo("Driver's License Registration", "Registration Succesful")
                  con.close();


def unregister():
      try:
            cid=int(t_cid.get())
      except ValueError:
            MessageBox.showinfo("Driver's License Registration","Invalid input has been entered")

      name = t_name.get()
      age = t_age.get()
      dob= t_dob.get()
      nat = clicked.get()
      cid=t_cid.get()
      
      if(name=="" and cid==""):
            MessageBox.showinfo("Driver's License Registration","Name and Civil ID is required for unregistration")
      else:
            con=mysql.connector.connect(host="localhost",user="root",password="root",database="tc2")
            cursor = con.cursor()
            cursor.execute("delete from list where name='"+ t_name.get() +"' or cid='"+ t_cid.get() +"' ")
            con.commit()
            

            t_name.delete(0, len(name))
            t_age.delete(0, len(age))
            t_dob.delete(0, len(dob))
            t_cid.delete(0, len(cid))
            MessageBox.showinfo("Driver's License Registration","Unregistered")
            con.close();
      



def update():
      try:
            age = int(t_age.get())
            cid=int(t_cid.get())
      except ValueError:
            MessageBox.showinfo("Driver's License Registration","Invalid input has been entered")
      
      name = t_name.get()
      age = t_age.get()
      dob= t_dob.get()
      nat = clicked.get()
      cid=t_cid.get()

      try:
          dob=str(t_dob.get())
          format="%Y-%m-%d"
          datetime.datetime.strptime(dob,format)
      except ValueError:
          MessageBox.showinfo("driver's License Registration","Invalid date format")

      

      if(cid==""):
            MessageBox.showinfo("Driver's License Registration","Civil ID must be entered to update any infomation")

      elif(age<='17'):
            MessageBox.showinfo("Driver's License Registration ","Age cannot be updated to less than 18")
      else:
          check=name.split(" ")
          for x in check:
              if not x.isalpha():
                  MessageBox.showinfo("Driver's License Registration","Invalid name")
              else:
                  con=mysql.connector.connect(host="localhost", user="root",password="root",database="tc2")
                  cursor=con.cursor()
                  cursor.execute("update list set name='"+ name +"' where cid='"+ cid +"'")
                  cursor.execute("update list set age='"+ age +"' where cid='"+ cid +"'")
                  cursor.execute("update list set dob='"+ dob +"' where cid='"+ cid +"'")
                  cursor.execute("update list set nat='"+ nat +"' where cid='"+ cid +"'")
                  con.commit()

                  t_name.delete(0, len(name))
                  t_age.delete(0, len(age))
                  t_dob.delete(0, len(dob))
                  t_cid.delete(0, len(cid))
                  MessageBox.showinfo("Driver's License Registration","Information updated successfully")
                  con.close();


def get():
      root=tkinter.Tk()
      root.title("Info")
      root.geometry("200x200")

      cid=t_cid.get()

      try:
            cid=int(t_cid.get())
      except ValueError:
            MessageBox.showinfo("Driver's License Registration","Invalid input has been entered")
      
      if(cid==""):
            MessageBox.showinfo("Driver's License Registration","Civil ID must be entered to obtained the registered details")
      else:
            listbox = tkinter.Listbox(root)
            con=mysql.connector.connect(host="localhost",user="root",password="root",database="tc2")
            cursor=con.cursor()
            cursor.execute("select * from list where cid='"+ t_cid.get() +"'")
            rows=cursor.fetchall()
            
            for x in rows:
                  listbox.insert(0,"Nationality:" ,x[3])
                  listbox.insert(0,"Date Of Birth:", x[2])
                  listbox.insert(0,"Age:",x[1])
                  listbox.insert(0,"Name:", x[0])
                  listbox.pack()
                  t_cid.delete(0, 'end')  
            
            con.close()
      root.mainloop()



      
##labels!!
heading = Label(window, text="Driver's License Registration", font=("times",35,"bold") ,bg="black" ,fg="maroon")
heading.place(x=490,y=30)

name=Label(window,text="Enter your name:",font=("times",25,"bold"),bg="black", fg="white")
name.place(x=60,y=300)

age=Label(window,text="Age:",font=("times",25,"bold"), bg="black",fg="white")
age.place(x=60,y=350)

dob=Label(window,text="Date Of Birth:",font=("times",25,"bold"),bg="black",fg="White")
dob.place(x=60,y=400)

nat=Label(window,text="Nationality:",font=("times",25,"bold"),bg="black",fg="white")
nat.place(x=60,y=450)

cid=Label(window,text="Civil ID", font=("times",25,"bold"), bg="black",fg="white")
cid.place(x=60,y=500)


##textboxes
t_name= Entry(window,font=("times",16))
t_name.place(x=400,y=310,width=350,height=30)

t_age= Entry(window,font=("times",16))
t_age.place(x=400,y=360,width=350,height=30)

t_dob= Entry(window,font=("times",16))
t_dob.place(x=400,y=410,width=350,height=30)

clicked=StringVar()
clicked.set("India")
t_nat= OptionMenu(window,clicked,"India","Oman")
t_nat.place(x=400,y=460,width=350,height=30)

t_cid= Entry(window,font=("times",16))
t_cid.place(x=400,y=510,width=350,height=30)


##buttons
register=Button(window,text="Register",font=("times",20,"bold"),bg="DeepSkyBlue",width=9, command=register)
register.place(x=60,y=600)

unregister=Button(window,text="Unregister",font=("times",20,"bold"),bg="OrangeRed2",width=9, command=unregister)
unregister.place(x=240,y=600)

update=Button(window,text="Update",font=("times",20,"bold"),bg="gold",width=9, command=update)
update.place(x=420,y=600)

get=Button(window,text="Get",font=("times",20,"bold"),bg="maroon2",width=9, command=get)
get.place(x=600,y=600)

window.mainloop()









