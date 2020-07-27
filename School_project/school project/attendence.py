from tkinter import *

attendenceGui = Tk()
attendenceGui.geometry('500x500')
attendenceGui.title('Attendence Report')
attendenceGui.resizable(0,0)



#----- FUNCTIONS -----
def submit():
    pass






defaultDate = StringVar(attendenceGui)
defaultDate.set('1')
defaultMonth = StringVar(attendenceGui)
defaultMonth.set('January')
var = IntVar()
labelDate = Label(text = 'Select Date')
labelMonth = Label(text = 'Select Month')
dateMenu = OptionMenu(attendenceGui, defaultDate, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
monthMenu = OptionMenu(attendenceGui, defaultMonth, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
presentButton = Radiobutton(attendenceGui, text = 'Present', variable = var, value = 'present')
absentButton = Radiobutton(attendenceGui, text = 'Absent', variable = var, value = 'absent')
submitButton = Button(attendenceGui, text = 'Submit', command = submit)
studentIdEntry = Entry(attendenceGui)
studentIdLabel = Label(attendenceGui, text = 'Enter Student ID')
studentNameEntry = Entry(attendenceGui, state = 'disabled')
studentNameLabel = Label(attendenceGui, text = 'Student Name')


labelDate.place(rely = 0.3, relx = 0.35)
dateMenu.place(rely = 0.29, relx = 0.51)
labelMonth.place(rely = 0.4, relx = 0.35)
monthMenu.place(rely = 0.39, relx = 0.51)
presentButton.place(rely = 0.53, relx = 0.3, anchor = W)
absentButton.place(rely = 0.53, relx = 0.5, anchor = W)
submitButton.place(rely = 0.6, relx = 0.43)
studentIdEntry.place(rely = 0.1, relx = 0.45)
studentIdLabel.place(rely = 0.1, relx = 0.25)
studentNameEntry.place(rely = 0.19, relx = 0.45)
studentNameLabel.place(rely = 0.19, relx = 0.25)


attendenceGui.mainloop()
