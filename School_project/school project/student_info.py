from tkinter import *


#----- GUI -----
studentInfoGui = Tk()
studentInfoGui.geometry('500x500')
studentInfoGui.resizable(0,0)
studentInfoGui.title('Student Information')


#----- FUNCTIONS -----
def register():
    from studentInfo_register import registerGuiRun
    registerGuiRun()


def view():
    from studentInfo_view import viewGuiRun
    viewGuiRun()


#---- WIDGETS -----
registerButton = Button(studentInfoGui, text = 'Register', width = 10, height = 2, command = register)
viewButton = Button(studentInfoGui, text = 'View', width = 10, height = 2, command = view)
registerPhoto = PhotoImage(file = 'images/registerIcon.png')
registerLabel = Label(image = registerPhoto)
viewPhoto = PhotoImage(file = 'images/viewIcon.png')
viewLabel = Label(image = viewPhoto)


#----- PLACING WIDGETS -----
registerButton.place(relx = 0.25, rely = 0.5)
viewButton.place(relx = 0.6, rely = 0.5)
registerLabel.place(relx = 0.25, rely = 0.3)
viewLabel.place(relx = 0.6, rely = 0.3)


#----- MAINLOOP -----
studentInfoGui.mainloop()
