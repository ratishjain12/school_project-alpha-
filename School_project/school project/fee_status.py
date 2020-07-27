from tkinter import * 

fee_window = Toplevel()
fee_window.geometry('500x400')
fee_window.title('Fee-Status')
fee_window.resizable(0,0)

def check_individual():
    fee_window.withdraw()
    check_individual_window = Toplevel(fee_window)
    check_individual_window.geometry('600x700')
    check_individual_window.title('Fee - Status')

frame = Frame(fee_window)
frame.place(relx = 0.25, rely = 0.3)


#--------Buttons---------#
check_individual = Button(frame,text = 'Check for a student',width=20, font = 'Helvetica 20 bold',command = check_individual)
check_individual.grid(pady=4)

Pending_Paid= Button(frame,text = 'pending / paid',width=20, font = 'Helvetica 20 bold')
Pending_Paid.grid(pady=4)




fee_window.mainloop()

