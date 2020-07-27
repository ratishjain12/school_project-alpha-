from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Menu")
root.geometry("800x600")
root.config(bg = "yellow")
root.resizable(0,0)



#####Functions########
def quit_function():
    repsonse = messagebox.askquestion("Confirmation","Are you sure you want to quit?",icon = "warning")
    if repsonse == "yes":
        root.destroy()

def Reportcard():
    root.withdraw()
    from reportcard import main_window
    
def Fee_status():
    root.withdraw()
    from fee_status import fee_window
    
def Student_info():
    root.withdraw()
    from student_info import studentInfoGui

def attendance():
    root.withdraw()
    from attendence import attendenceGui


frame = Frame(root,bg = "yellow")
frame.place(relx = 0.35,rely = 0.32)

Student_info = Button(frame,text = "Student-Info",font = "Helvetica 20 bold",width=20)
Student_info.grid(pady = 5)

Fee_status = Button(frame,text = "Fee - Status",font = "Helvetica 20 bold",width =20,command=Fee_status)
Fee_status.grid(pady = 5)

Gradebook = Button(frame,text = "Grade-book",font = "Helvetica 20 bold",width = 20)
Gradebook.grid(pady = 5)

reportcard = Button(frame,text = "Report-Card Generator",font = "Helvetica 20 bold",width = 20,command  = Reportcard)
reportcard.grid(pady = 5)

Attendance = Button(frame,text = "Attendance",font = "Helvetica 20 bold",width = 20)
Attendance.grid(pady = 5)


quit = Button(frame,text = "Quit",font = "Helvetica 20 bold",width = 20 ,command = quit_function)
quit.grid(pady = 5)

root.mainloop()
