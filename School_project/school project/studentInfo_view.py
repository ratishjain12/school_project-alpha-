from tkinter import *
from database import db, cursor
from tkinter import ttk
from tkinter import messagebox

def viewGuiRun():
    #----- GUI -----
    viewGui = Toplevel()
    viewGui.title('View')
    viewGui.geometry('700x700')
    viewGui.resizable(0, 0)


    #----- FUNCTIONS -----
    def search():
        if searchEntry.get().strip() == '':
            messagebox.showerror('Student Info', 'Please enter a search parameter!')

        else:
            query = searchEntry.get().strip()
            display.delete(*display.get_children())
            if searchParameter.get().strip() == 'Student ID':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where studentId = %s'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid Student ID')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')

            elif searchParameter.get().strip() == 'Roll No':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where rollno = %s'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid Roll No')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')

            elif searchParameter.get().strip() == 'Firstname':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where firstname = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid name')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')


            elif searchParameter.get().strip() == 'Lastname':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where lastname = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a valid name')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')


            elif searchParameter.get().strip() == 'Class':
                cursor.execute('use school')
                try:
                    cursor.execute('select * from studentdata where std = "%s"'%(query))
                except:
                    messagebox.showerror('Student Info', 'Please enter a class')

                data = cursor.fetchall()
                if len(data) != 0:
                    for entry in data:
                        studentId = entry[0]
                        name = entry[1] + ' ' + entry[2]
                        rollno = entry[3]
                        std = entry[4]
                        gender = entry[6]
                        display.insert('', 'end', values = (studentId, name, std, rollno, gender))
                else:
                    messagebox.showerror('Student Info', 'No data found')





    def delete():
        display.selection_clear()


    #----- WIDGETS -----
    viewByLabel = Label(viewGui, text = "View By", font = 'Helvetica 16 bold')
    searchParameter = StringVar()
    searchParameter.set("Student ID")
    searchBy = OptionMenu(viewGui, searchParameter, "Student ID", "Roll No", "Firstname", "Lastname", "Class")
    searchBy.config(width = 10)
    searchLabel = Label(viewGui, text = "Search Here:")
    searchEntry = Entry(viewGui, width = 30)
    searchButton = Button(viewGui, text = "Search", width = 10, command  = search)
    deleteButton = Button(viewGui, text = "Delete", height = 2, width = 15, command = delete)
    updateButton = Button(viewGui, text = 'Update', height = 2, width = 15)
    openButton = Button(viewGui, text  = 'Open', height = 2, width = 15)

    display = ttk.Treeview(viewGui, selectmode = "browse", height = 25)
    scrlbar = ttk.Scrollbar(viewGui, orient = 'vertical', command = display.yview)
    display.configure(xscrollcommand = scrlbar.set)

    display['columns'] = ('studentId', 'name', 'class', 'rollno', 'gender')
    display['show'] = 'headings'
    display.heading('studentId', text = 'Student ID')
    display.heading('name', text = 'Name')
    display.heading('class', text = 'Class')
    display.heading('rollno', text = 'Roll no.')
    display.heading('gender', text = 'Gender')

    display.column('studentId', anchor = 'c', width = 100 )
    display.column('name', anchor = 'c', width = 200 )
    display.column('class', anchor = 'c', width = 100)
    display.column('rollno', anchor = 'c', width = 100)
    display.column('gender', anchor = 'c', width = 100)


    #----- PLACING WIDGETS -----

    viewByLabel.place(relx = 0.13, rely = 0.095)
    searchBy.place(relx  = 0.26, rely = 0.095)
    searchEntry.place(relx = 0.44, rely = 0.1)
    searchButton.place(relx = 0.73, rely = 0.1)
    display.place(relx = 0.0715, rely = 0.2)
    scrlbar.pack(side = 'right', fill = 'x')
    openButton.place(relx = 0.1, rely = 0.9)
    updateButton.place(relx = 0.425, rely = 0.9)
    deleteButton.place(relx = 0.745, rely = 0.9)





    #----- MAINLOOP -----
    viewGui.mainloop()
