import mysql.connector
import matplotlib as plt
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
root  = Tk()
root.geometry("800x600")
root.title("Student Admin")
root.resizable(0,0)


#-----Data-Base-Integration----#
db = mysql.connector.connect(user='root', password='1234')
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
cursor.execute("USE school")
cursor.execute("""CREATE TABLE IF NOT EXISTS stdata(
        id int primary key,
        firstname text,
        lastname text,
        rollno int,
        class text)""")


db.commit()
#conn.close()
#------Functions-----#

def home():
    c.withdraw()
    root.deiconify()


def add():
    global db, b, cursor
    ids = int(stid_ent.get())
    firstname  = name_ent.get()
    lastname = name2_ent.get()
    rollno = int(rno_ent.get())
    sclass = clicked.get()
    command = "INSERT INTO stdata VALUES(%s, '%s', '%s', %s, '%s')"%(ids, firstname, lastname, rollno, sclass)
    cursor.execute(command)
    ids = stid_ent.delete(0,END)
    firstname  = name_ent.delete(0,END)
    lastname = name2_ent.delete(0,END)
    rollno = rno_ent.delete(0,END)
    lst.delete(0,END)
    cursor.execute("SELECT * FROM stdata")
    b = cursor.fetchall()

    for i in b:
        lst.insert(END,i)

    db.commit()
    db.close()

def delete():
    global db
    clicked_items = lst.curselection()
    for i in clicked_items:
        print(i)
        lst.delete(i)
    cursor = db.commit()
    db.commit()

def search():
    global db, cursor
    try:
        if searches.get() == "Id":
            lst.delete(0,END)
            cs = search_ent.get()
            "SELECT *  FROM stdata where id = Id"
            cursor.execute("SELECT *  FROM stdata where id = ?",(cs,))
            data = cursor.fetchall()

            for i in data:
                lst.insert(END,i)

            db.commit()

        if searches.get() == "Roll No":
            lst.delete(0,END)
            cs = search_ent.get()
            "SELECT *  FROM stdata where id = Id"
            cursor.execute("SELECT *  FROM stdata where rollno = ?",(cs,))
            data = cursor.fetchall()

            for i in data:
                lst.insert(END,i)

            db.commit()

        if searches.get() == "class":
            lst.delete(0,END)
            cs = search_ent.get()
            "SELECT *  FROM stdata where id = Id"
            cursor.execute("SELECT *  FROM stdata where class = ?",(cs,))
            data = cursor.fetchall()

            for i in data:
                lst.insert(END,i)

            db.commit()

        if searches.get() == "firstname":
            lst.delete(0,END)
            cs = search_ent.get()
            "SELECT *  FROM stdata where id = Id"
            cursor.execute("SELECT *  FROM stdata where firstname = ?",(cs,))
            data = cursor.fetchall()

            for i in data:
                lst.insert(END,i)

        if searches.get() == "all":
            lst.delete(0,END)
            cursor.execute("SELECT *  FROM stdata")
            d = cursor.fetchall()

            for i in d:
                lst.insert(END,i)


            db.commit()

    except:
        print("Invalid Search!")

def Home():
    pass

def Attendance():
    pass
def Parents_info():
    pass


def login():
    global db, cursor, searches, search, lst, clicked, rno_ent, name_ent, name2_ent, stid_ent, c
    u = user_ent.get()
    p = user_pass.get()
    if u == "admin" and p == "1234":

        messagebox.showinfo("Student Admin","YOU SUCCESSFULLY LOGGED IN!!")
        root.withdraw()
        #---New-Window------#
        c = Toplevel(root)
        c.geometry("1310x700")
        c.configure(bg="blue")
        c.resizable(0,0)
        title_f1 = Frame(c)
        title_f1.place(relx=0.4)
        title = Label(title_f1,text="STUDENT PANEL",font = "Helvetic 25 bold",bg="blue")
        title.grid()
        #designing#
        back_btn = Button(c,text = "Back to Home",width=12,height= 3,font = "Helvetica 10 bold",command = home)
        back_btn.grid(row=0,column=0)
        admin_f1 = Frame(c,highlightbackground="black",highlightthickness=1)
        admin_f1.place(relx=0.04,rely=0.1)

        stid_lbl = Label(admin_f1,text = "Enter Student Id:",font = "Helvetica 20 bold")
        stid_lbl.grid(pady = 5)

        stid_ent = Entry(admin_f1)
        stid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

        name_lbl = Label(admin_f1,text = "Enter Student FirstName:",font = "Helvetica 20 bold")
        name_lbl.grid(pady = 30)

        name_ent = Entry(admin_f1)
        name_ent.grid(row = 1,column = 1,padx = 3,pady = 30)

        name2_lbl = Label(admin_f1,text = "Enter Student LastName:",font = "Helvetica 20 bold")
        name2_lbl.grid(pady = 30)

        name2_ent = Entry(admin_f1)
        name2_ent.grid(row = 2,column = 1,padx = 3,pady = 30)

        rno_label = Label(admin_f1,text = "Enter Roll Number:",font = "Helvetica 20 bold")
        rno_label.grid(pady = 30)

        rno_ent = Entry(admin_f1)
        rno_ent.grid(row = 3,column = 1,padx = 3,pady = 30)

        sc_label = Label(admin_f1,text = "Enter Student class:",font = "Helvetica 20 bold")
        sc_label.grid(pady = 30)

        clicked = StringVar(admin_f1)
        clicked.set("1st-standard")

        sc_ent = OptionMenu(admin_f1,clicked,"1st-standard","2nd-standard","3rd-standard","4th-standard","5th-standard","6th-standard","7th-standard","8th-standard","9th-standard","10th-standard","11th-standard","12th-standard")
        sc_ent.grid(padx = 2,row = 4,column=1,pady = 30)

        add_btn = Button(admin_f1,text = "ADD",font = "Helvetica 20 bold",command = add)
        add_btn.grid(row = 5 , column = 1,pady=20)

        #displaying data#
        admin_f2 = Frame(c)
        admin_f2.place(relx = 0.51,rely = 0.1)

        branched_f1 = Frame(admin_f2)
        branched_f1.grid()

        searchby_lbl = Label(branched_f1,text = "Search By",font = "Helvetica 20 bold")
        searchby_lbl.grid()

        searches = StringVar()
        searches.set("Id")

        opt_ent = OptionMenu(branched_f1,searches,"all","Id","Roll No","firstname","class")
        opt_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

        search_lbl = Label(branched_f1,text = "Search Here:",font = "Helvetica 20 bold")
        search_lbl.grid(row=0,column = 2)



        search_ent = Entry(branched_f1)
        search_ent.grid(row = 0, column = 3)

        search_btn = Button(branched_f1,text = "Search",font = "Helvetica 14 bold",command = search)
        search_btn.grid(row = 0,column = 4)

        delete_btn = Button(branched_f1,text = "Delete",font = "Helvetica 14 bold",command = delete)
        delete_btn.grid(row = 0,column = 5)


        branched_f2 = Frame(admin_f2)
        branched_f2.grid()

        lst = Listbox(branched_f2,width  = 70,height = 28)
        lst.grid(row = 3)


        cursor.execute("SELECT * FROM stdata")
        b = cursor.fetchall()

        for i in b:
            lst.insert(END,i)




        db.commit()
        #menu
        menu = Menu(c)
        file_menu = Menu(menu)
        menu.add_cascade(label = "Home",menu = file_menu)
        file_menu.add_command(label = "Home",command = Home)
        file_menu.add_separator()
        ###############
        attendance_menu = Menu(menu)
        menu.add_cascade(label = "Attendance",menu = attendance_menu)
        attendance_menu.add_command(label = "Attendance",command = Attendance)
        attendance_menu.add_separator()
        ##############
        parents_info = Menu(menu)
        menu.add_cascade(label = "parents_info",menu = parents_info)
        parents_info.add_command(label = "Parent Info",command = Parents_info)
        parents_info.add_separator()
        ##############
        Quit = Menu(menu)
        menu.add_cascade(label = "quit",menu = Quit)
        Quit.add_command(label = "quit",command = quit)
        c.config(menu = menu)
        c.mainloop()
    #designing endede#
    else:
        messagebox.showinfo("Student Admin","Alert: Invalid Username or Password")



#----Functions-End--#

main_f1 = Frame(root)
main_f1.place(relx = 0.3,rely = 0.5)

img = PhotoImage(file = "logo.png")
logo = Label(image = img)
logo.grid(padx = 240,pady = 50)

user_label = Label(main_f1,text = "Enter Username:",font = "Helvetica 20 bold")
user_label.grid(pady = 5)

user_ent = Entry(main_f1)
user_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

pass_label = Label(main_f1,text = "Enter Password:",font = "Helvetica 20 bold")
pass_label.grid(pady = 5)

user_pass = Entry(main_f1,show = "*")
user_pass.grid(row = 1,column = 1,padx = 3,pady = 5)

log_btn = Button(main_f1,width = 10,height = 2,text = "login",font = "Helvetica 15 bold",command = login)
log_btn.grid(row = 2,column=1)

root.mainloop()
