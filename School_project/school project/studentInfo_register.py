from tkinter import *
from tkinter import messagebox
from database import db, cursor
import datetime

def registerGuiRun():
    #----- GUI -----
    registerGui = Toplevel()
    registerGui.title('Register')
    registerGui.geometry('600x600')
    registerGui.resizable(0,0)


    #----- FUNCTIONS -----
    def check():
        firstname = firstnameEntry.get().strip()
        lastname = lastnameEntry.get().strip()
        address = addressEntry.get().strip()
        fatherName = fatherNameEntry.get().strip()
        fatherNo = fatherNoEntry.get().strip()
        fatherProfession = fatherProfessionEntry.get().strip()
        motherName = motherNameEntry.get().strip()
        motherNo = motherNoEntry.get().strip()
        motherProfession = motherProfessionEntry.get().strip()
        studentId = studentIdEntry.get().strip()
        std = stdEntry.get().strip()
        rollno = rollnoEntry.get().strip()
        dobDate= dobDateVar.get()
        dobMonth = dobMonthVar.get()
        dobYear = dobYearVar.get()
        gender = genderVar.get().strip()
        section = sectionVar.get()
        
        issue_counter = 0
        details = ['firstname', 'lastname', 'address',
                   'fatherName', 'fatherNo', 'fatherProfession',
                   'motherName', 'motherNo', 'motherProfession',
                   'studentId', 'std', 'rollno', 'gender']

        for detail in details:
            if vars()[detail] == '':
                messagebox.showerror('Student Registration', 'Please fill all the details')
                print(detail)
                issue_counter += 1
                break
        if issue_counter == 0:
            cursor.execute('select studentId from studentdata')
            ids = cursor.fetchall()

            for i in range(len(ids)):
                if (studentId,) in ids:
                    messagebox.showerror('Student Registration', 'Student ID already exists. Please use a unique Student ID')
                    issue_counter += 1

            cursor.execute('select std, section, rollno from studentdata')
            data = cursor.fetchall()
            for i in range(len(data)):
                if (std, section, int(rollno)) in data:
                    messagebox.showerror('Student Registration', 'Roll no. already exists in the class')
                    issue_counter += 1



        if issue_counter == 0:
            submit()



    def submit():
        firstname = firstnameEntry.get().strip()
        lastname = lastnameEntry.get().strip()
        address = addressEntry.get().strip()
        fatherName = fatherNameEntry.get().strip()
        fatherNo = fatherNoEntry.get().strip()
        fatherProfession = fatherProfessionEntry.get().strip()
        motherName = motherNameEntry.get().strip()
        motherNo = motherNoEntry.get().strip()
        motherProfession = motherProfessionEntry.get().strip()
        studentId = studentIdEntry.get().strip()
        std = stdEntry.get().strip()
        rollno = rollnoEntry.get().strip()
        dobDate= dobDateVar.get()
        dobMonth = dobMonthVar.get()
        dobYear = dobYearVar.get()
        gender = genderVar.get().strip()
        section = sectionVar.get()

        dob = dobDate + '-' + dobMonth + '-' + dobYear
        dob = datetime.datetime.strptime(dob, '%d-%B-%Y')
        '''
        cursor.execute('use school')
        cursor.execute("insert into studentdata values(%s, '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s')"%(studentId, firstname, lastname, rollno, std, section, gender, address, dob))
        cursor.execute("insert into parentinfo values(%s, '%s', %s, '%s', '%s', %s, '%s')"%(studentId, fatherName, fatherNo, fatherProfession, motherName, motherNo, motherProfession))
        db.commit()
        '''
        messagebox.showinfo('Student Registration', 'Data successfully registered!')

        firstnameEntry.delete(0, END)
        lastnameEntry.delete(0, END)
        addressEntry.delete(0, END)
        fatherNameEntry.delete(0, END)
        fatherNoEntry.delete(0, END)
        fatherProfessionEntry.delete(0, END)
        motherNameEntry.delete(0, END)
        motherNoEntry.delete(0, END)
        motherProfessionEntry.delete(0, END)
        studentIdEntry.delete(0, END)
        stdEntry.delete(0, END)
        rollnoEntry.delete(0, END)
        dobDateVar.set('1')
        dobMonthVar.set('January')
        dobYearVar.set('2000')
        sectionVar.set('A')
        


    #----- WIDGETS -----
    mainLabel = Label(registerGui, text = 'Student Registration')
    studentIdEntry = Entry(registerGui)
    studentIdLabel = Label(registerGui, text = 'Student ID')
    firstnameEntry = Entry(registerGui)
    firstnameLabel = Label(registerGui, text = 'First Name')
    lastnameEntry = Entry(registerGui)
    lastnameLabel = Label(registerGui, text = 'Last Name')
    stdEntry = Entry(registerGui)
    stdLabel = Label(registerGui, text = 'Standard')
    sectionVar = StringVar(registerGui)
    sectionLabel = Label(registerGui, text = 'Section')
    sectionVar.set('A')
    sectionMenu = OptionMenu(registerGui, sectionVar, 'A', 'B', 'C', 'D')
    sectionMenu.config(width = 2)
    rollnoEntry = Entry(registerGui)
    rollnoLabel = Label(registerGui, text = 'Roll No.')
    dobDateVar = StringVar(registerGui)
    dobDateVar.set('1')
    dobMonthVar = StringVar(registerGui)
    dobMonthVar.set('January')
    dobYearVar = StringVar(registerGui)
    dobYearVar.set('2000')
    dobLabel = Label(registerGui, text = 'DOB')
    dobDateMenu = OptionMenu(registerGui, dobDateVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    dobMonthMenu = OptionMenu(registerGui, dobMonthVar, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    dobYearMenu = OptionMenu(registerGui, dobYearVar, '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
    dobDateMenu.config(width = 2)
    dobMonthMenu.config(width = 10)
    dobYearMenu.config(width = 5)
    genderVar = StringVar(registerGui)
    genderMenu = OptionMenu(registerGui, genderVar, 'M', 'F', 'Other')
    genderMenu.config(width = 5)
    genderLabel = Label(registerGui, text = 'Gender')
    addressEntry = Entry(registerGui, width = 50)
    addressLabel = Label(registerGui, text = 'Address')
    fatherNameEntry = Entry(registerGui)
    fatherNameLabel = Label(registerGui, text = 'Father\'s Name')
    fatherNoEntry = Entry(registerGui)
    fatherNoLabel = Label(registerGui, text = 'Father\'s No.')
    fatherProfessionEntry = Entry(registerGui)
    fatherProfessionLabel = Label(registerGui, text = 'Father\'s Profession')
    motherNameEntry = Entry(registerGui)
    motherNameLabel = Label(registerGui, text = 'Mother\'s Name')
    motherNoEntry = Entry(registerGui)
    motherNoLabel = Label(registerGui, text = 'Mother\'s No.')
    motherProfessionEntry = Entry(registerGui)
    motherProfessionLabel = Label(registerGui, text = 'Mother\'s Profession')
    submitButton = Button(registerGui, text = 'Submit', command = check, height = 2, width = 15)


    #----- PLACING WIDGETS -----
    mainLabel.place(relx = 0.4, rely = 0.005)
    firstnameLabel.place(relx = 0.1, rely = 0.05)
    firstnameEntry.place(relx = 0.23, rely = 0.05)
    lastnameLabel.place(relx = 0.1, rely = 0.1)
    lastnameEntry.place(relx = 0.23, rely = 0.1)
    addressLabel.place(relx = 0.1, rely = 0.15)
    addressEntry.place(relx = 0.23, rely = 0.15)
    dobLabel.place(relx = 0.1, rely = 0.21)
    dobDateMenu.place(relx = 0.219, rely = 0.2)
    dobMonthMenu.place(relx = 0.325, rely = 0.2)
    dobYearMenu.place(relx = 0.501, rely = 0.2)
    genderLabel.place(relx = 0.1, rely = 0.275)
    genderMenu.place(relx = 0.219, rely = 0.265)

    fatherNameLabel.place(relx = 0.1, rely = 0.35)
    fatherNameEntry.place(relx = 0.3215, rely = 0.35)
    fatherNoLabel.place(relx = 0.1,rely = 0.4)
    fatherNoEntry.place(relx = 0.3215, rely = 0.4)
    fatherProfessionLabel.place(relx = 0.1, rely = 0.45)
    fatherProfessionEntry.place(relx = 0.3215, rely = 0.45)
    motherNameLabel.place(relx = 0.1, rely = 0.5)
    motherNameEntry.place(relx = 0.3215, rely = 0.5)
    motherNoLabel.place(relx = 0.1,rely = 0.55)
    motherNoEntry.place(relx = 0.3215, rely = 0.55)
    motherProfessionLabel.place(relx = 0.1, rely = 0.6)
    motherProfessionEntry.place(relx = 0.3215, rely = 0.6)

    studentIdLabel.place(relx = 0.1, rely = 0.67)
    studentIdEntry.place(relx = 0.23, rely= 0.67)
    stdLabel.place(relx = 0.1, rely = 0.72)
    stdEntry.place(relx = 0.23, rely = 0.72)
    sectionLabel.place(relx = 0.1, rely = 0.78)
    sectionMenu.place(relx = 0.225, rely = 0.77)
    rollnoLabel.place(relx = 0.1, rely = 0.845)
    rollnoEntry.place(relx = 0.23, rely = 0.845)

    submitButton.place(relx = 0.38, rely = 0.9)


    #----- MAINLOOP -----
    registerGui.mainloop()
