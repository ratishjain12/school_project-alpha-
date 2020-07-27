from tkinter import *
from tkinter import messagebox
import csv
import shutil
from tkinter import filedialog

main_window = Toplevel()
main_window.geometry("800x600")
main_window.resizable(0,0)
main_window.title("Reportcard - generator")
main_window.config(bg = "grey")
#####Functions########
def back0():
    main_window.withdraw()
    from menu import root
    
def quit_function():
    repsonse = messagebox.askquestion("Confirmation","Are you sure you want to quit?",icon = "warning")
    if repsonse == "yes":
        main_window.destroy()
def back():
    c_first_fourth.withdraw()
    main_window.deiconify()
def back2():
    c_fifth_tenth.withdraw()
    main_window.deiconify()

def back3():
    c_eleventh_twelfth.withdraw()
    main_window.deiconify()

def back4():
    c_eleventh_twelfth_science.withdraw()
    main_window.deiconify()

def open_file():
    main_window.filename = filedialog.askopenfile(initialdir = '/Users/ratish/Desktop/school project/generated-report')



def subject_choice():
    global choice_subject
    global subject_mark
    choice_subject = subject4_var.get()
    if choice_subject == "Mathematics":
        subject_mark = marks4_ent.get()
        subject_label.after(1000,subject_label.destroy)
        marks_ent.after(1000,marks_ent.destroy)
    else:
        subject_mark = marks_ent.get()
        subject4_label.after(1000,subject4_label.destroy)
        marks4_ent.after(1000,marks4_ent.destroy)
        

def save():
    if choice_subject == 'Mathematics':
        subject_mark = marks4_ent.get()
    elif choice_subject == 'Biology':
        subject_mark = marks_ent.get()
    elif choice_subject == None:
        subject_mark = marks4_en
    f = open(student_ent.get()+'.csv','w')
    w = csv.writer(f,delimiter = ',')
    exam_type = Exam_var.get()
    w.writerow(['Name - '+student_ent.get()+"  "+'Class -'+class_var.get()+'  '+'Section -'+section_var.get(),'Marks'])
    w.writerow(['                                        EXAM -                                              ',Exam_var.get()])
    l = [[subject1_var.get(),marks1_ent.get()],
         [subject2_var.get(),marks2_ent.get()],
         [subject3_var.get(),marks3_ent.get()],
         [subject4_var.get(),subject_mark],
         [subject5_var.get(),marks5_ent.get()],
        ]
    w.writerows(l)
    f.close()
    shutil.move(student_ent.get()+'.csv','generated-report')

    


def class_section1():
    global c_first_fourth
    global frame2
    global student_ent
    global studentid_ent
    global class_var
    global section_var
    global Exam_var
    global subject1_var
    global marks1_ent
    global subject2_var
    global marks2_ent
    global subject3_var
    global marks3_ent
    global subject4_var
    global marks4_ent
    global subject5_var
    global marks5_ent
    
    main_window.withdraw()
    c_first_fourth = Toplevel(main_window)
    c_first_fourth.title("Class  1st - 4th")
    c_first_fourth.resizable(0,0)
    c_first_fourth.geometry("1310x700")
    c_first_fourth.config(bg = "#bbf1c8")

    frame = Frame(c_first_fourth,bg = "#bbf1c8")
    frame.place(relx = 0.35,rely = 0.1)
    studentid_label = Label(frame,text = "Student - Id:",bg = "#bbf1c8",font = "Helvetica 20 bold")
    studentid_label.grid(pady = 5)

    studentid_ent = Entry(frame,width = 30)
    studentid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    student_label = Label(frame,text = "Student - Name:",bg = "#bbf1c8",font = "Helvetica 20 bold")
    student_label.grid(pady = 5)

    student_ent = Entry(frame,width = 30)
    student_ent.grid(row = 1,column = 1,padx = 3,pady = 5)

    class_label = Label(frame,text = "Choose class:",bg = "#bbf1c8",font = "Helvetica 20 bold")
    class_label.grid(pady = 5)

    class_var = StringVar()
    class_var.set("1st-standard")
    class_menu = OptionMenu(frame,class_var,"1st-standard","2nd-standard","3rd-standard","4th-standard","5th-standard")
    class_menu.grid(row = 2,column = 1,padx = 3,pady = 5) 

    section_label = Label(frame,text = "Section",font = "Helvetica 20 bold",bg = "#bbf1c8")
    section_label.grid(pady = 5,row = 3 ,column = 0)   

    section_var = StringVar()
    section_var.set("A")
    section_menu = OptionMenu(frame,section_var,"A","B","C","D")
    section_menu.grid(row = 3,column = 1,padx = 3,pady = 5)

    exam_label = Label(frame,text = "Exam:",font = "Helvetica 20 bold",bg = "#bbf1c8")
    exam_label.grid(pady = 5,row = 4 ,column = 0)   

    Exam_var = StringVar()
    Exam_var.set("periodic-test 1")
    Exam_menu = OptionMenu(frame,Exam_var,"periodic-test 1","periodic-test 2","Mid-term","periodic-test 3","periodic-test 4","Final-Exam")
    Exam_menu.grid(row = 4,column = 1,padx = 3,pady = 5) 
 
    frame2 = Frame(c_first_fourth)
    frame2.place(relx = 0.35,rely = 0.43)

    subject1_var = StringVar()
    subject1_var.set("English:")
    subject1_label = Label(frame2,textvariable = subject1_var,font = "Helvetica 20 bold")
    subject1_label.grid(pady = 5)

    marks1_ent = Entry(frame2,width = 30)
    marks1_ent.grid(row = 0,column = 1,padx = 3,pady = 5)


    subject2_var = StringVar()
    subject2_var.set("G.K")
    subject2_label = Label(frame2,textvariable = subject2_var,font = "Helvetica 20 bold")
    subject2_label.grid(pady = 5)

    marks2_ent = Entry(frame2,width = 30)
    marks2_ent.grid(row = 1,column = 1,padx = 3,pady = 5)


    subject3_var = StringVar()
    subject3_var.set("Maths")
    subject3_label = Label(frame2,textvariable = subject3_var,font = "Helvetica 20 bold")
    subject3_label.grid(pady = 5)

    marks3_ent = Entry(frame2,width = 30)
    marks3_ent.grid(row = 2,column = 1,padx = 3,pady = 5)

    subject4_var = StringVar()
    subject4_var.set("Evs")
    subject4_label = Label(frame2,textvariable = subject4_var,font = "Helvetica 20 bold")
    subject4_label.grid(pady = 5)

    marks4_ent = Entry(frame2,width = 30)
    marks4_ent.grid(row = 3,column = 1,padx = 3,pady = 5)


    subject5_var = StringVar()
    subject5_var.set("Hindi")
    subject5_label = Label(frame2,textvariable = subject5_var,font = "Helvetica 20 bold")
    subject5_label.grid(pady = 5)

    marks5_ent = Entry(frame2,width = 30)
    marks5_ent.grid(row = 4,column = 1,padx = 3,pady = 5)

    button_frame = Frame(c_first_fourth)
    button_frame.place(relx = 0.35,rely = 0.80)

    Save_button = Button(button_frame,text = "Export/Save",font = "Helvetica 20 bold",width=40,command=save)
    Save_button.grid(pady = 5)

    Open_button = Button(button_frame,text = "Open Report-Card",font = "Helvetica 20 bold",width = 40)
    Open_button.grid(pady = 5)



    back_button = Button(c_first_fourth,text = "Back",command = back,font = "Helvetica 20 bold")
    back_button.grid()

    

def class_section2():
    global c_fifth_tenth
    global student_ent
    global frame2
    global studentid_ent
    global class_var
    global section_var
    global Exam_var
    global subject1_var
    global marks1_ent
    global subject2_var
    global marks2_ent
    global subject3_var
    global marks3_ent
    global subject4_var
    global marks4_ent
    global subject5_var
    global marks5_ent

    main_window.withdraw()
    c_fifth_tenth = Toplevel(main_window)
    c_fifth_tenth.title("Class  1st - 4th")
    c_fifth_tenth.resizable(0,0)
    c_fifth_tenth.geometry("1310x700")
    c_fifth_tenth.config(bg = "#fb7813")
    
    

    frame = Frame(c_fifth_tenth,bg = "#fb7813")
    frame.place(relx = 0.35,rely = 0.1)

    studentid_label = Label(frame,text = "Student - Id:",bg = "#fb7813",font = "Helvetica 20 bold")
    studentid_label.grid(pady = 5)

    studentid_ent = Entry(frame,width = 30)
    studentid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    student_label = Label(frame,text = "Student - Name:",bg = "#fb7813",font = "Helvetica 20 bold")
    student_label.grid(pady = 5)

    student_ent = Entry(frame,width = 30)
    student_ent.grid(row = 1,column = 1,padx = 3,pady = 5)

    class_label = Label(frame,text = "Choose class:",bg = "#fb7813",font = "Helvetica 20 bold")
    class_label.grid(pady = 5)

    class_var = StringVar()
    class_var.set("5th-standard")
    class_menu = OptionMenu(frame,class_var,"5th-standard","6th-standard","7th-standard","8th-standard","9th-standard","10th-standard")
    class_menu.grid(row = 2,column = 1,padx = 3,pady = 5) 

    section_label = Label(frame,text = "Section",font = "Helvetica 20 bold",bg = "#fb7813")
    section_label.grid(pady = 5,row = 3 ,column = 0)   

    section_var = StringVar()
    section_var.set("A")
    section_menu = OptionMenu(frame,section_var,"A","B","C","D")
    section_menu.grid(row = 3,column = 1,padx = 3,pady = 5)

    exam_label = Label(frame,text = "Exam:",font = "Helvetica 20 bold",bg = "#fb7813")
    exam_label.grid(pady = 5,row = 4 ,column = 0)   

    Exam_var = StringVar()
    Exam_var.set("periodic-test 1")
    Exam_menu = OptionMenu(frame,Exam_var,"periodic-test 1","periodic-test 2","Mid-term","periodic-test 3","periodic-test 4","Final-Exam")
    Exam_menu.grid(row = 4,column = 1,padx = 3,pady = 5) 
 
    frame2 = Frame(c_fifth_tenth)
    frame2.place(relx = 0.35,rely = 0.43)

    subject1_var = StringVar()
    subject1_var.set("English:")
    subject1_label = Label(frame2,textvariable = subject1_var,font = "Helvetica 20 bold")
    subject1_label.grid(pady = 5)

    marks1_ent = Entry(frame2,width = 30)
    marks1_ent.grid(row = 0,column = 1,padx = 3,pady = 5)


    subject2_var = StringVar()
    subject2_var.set("Science:")
    subject2_label = Label(frame2,textvariable = subject2_var,font = "Helvetica 20 bold")
    subject2_label.grid(pady = 5)

    marks2_ent = Entry(frame2,width = 30)
    marks2_ent.grid(row = 1,column = 1,padx = 3,pady = 5)


    subject3_var = StringVar()
    subject3_var.set("Maths:")
    subject3_label = Label(frame2,textvariable = subject3_var,font = "Helvetica 20 bold")
    subject3_label.grid(pady = 5)

    marks3_ent = Entry(frame2,width = 30)
    marks3_ent.grid(row = 2,column = 1,padx = 3,pady = 5)

    subject4_var = StringVar()
    subject4_var.set("Social-Studies:")
    subject4_label = Label(frame2,textvariable = subject4_var,font = "Helvetica 20 bold")
    subject4_label.grid(pady = 5)

    marks4_ent = Entry(frame2,width = 30)
    marks4_ent.grid(row = 3,column = 1,padx = 3,pady = 5)


    subject5_var = StringVar()
    subject5_var.set("Hindi:")
    subject5_label = Label(frame2,textvariable = subject5_var,font = "Helvetica 20 bold")
    subject5_label.grid(pady = 5)

    marks5_ent = Entry(frame2,width = 30)
    marks5_ent.grid(row = 4,column = 1,padx = 3,pady = 5)

    button_frame = Frame(c_fifth_tenth)
    button_frame.place(relx = 0.34,rely = 0.80)

    Save_button = Button(button_frame,text = "Export/Save",font = "Helvetica 20 bold",width=40,command=save)
    Save_button.grid(pady = 5)

    Open_button = Button(button_frame,text = "Open Report-Card",font = "Helvetica 20 bold",width = 40)
    Open_button.grid(pady = 5)



    back_button = Button(c_fifth_tenth,text = "Back",command = back2,font = "Helvetica 20 bold")
    back_button.grid()
    

def class_section3():
    global c_eleventh_twelfth
    global subject4_var
    global subject4_label
    global marks4_ent
    global subject_label
    global marks_ent
    global subject5_label
    global frame2
    global student_ent
    global studentid_ent
    global class_var
    global section_var
    global Exam_var
    global subject1_var
    global marks1_ent
    global subject2_var
    global marks2_ent
    global subject3_var
    global marks3_ent
    global subject4_var
    global marks4_ent
    global subject5_var
    global marks5_ent
    
    main_window.withdraw()
    c_eleventh_twelfth = Toplevel(main_window)
    c_eleventh_twelfth.title("Class  1st - 4th")
    c_eleventh_twelfth.resizable(0,0)
    c_eleventh_twelfth.geometry("1310x700")
    c_eleventh_twelfth.config(bg = "#726a95")

    frame = Frame(c_eleventh_twelfth,bg = "#726a95")
    frame.place(relx = 0.35,rely = 0.1)

    studentid_label = Label(frame,text = "Student - Id:",bg = "#726a95",font = "Helvetica 20 bold")
    studentid_label.grid(pady = 5)

    studentid_ent = Entry(frame,width = 30)
    studentid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    student_label = Label(frame,text = "Student - Name:",bg = "#726a95",font = "Helvetica 20 bold")
    student_label.grid(pady = 5)

    student_ent = Entry(frame,width = 30)
    student_ent.grid(row = 1,column = 1,padx = 3,pady = 5)

    class_label = Label(frame,text = "Choose class:",bg = "#726a95",font = "Helvetica 20 bold")
    class_label.grid(pady = 5)

    class_var = StringVar()
    class_var.set("11th")
    class_menu = OptionMenu(frame,class_var,"11th-standard","12th-standard")
    class_menu.grid(row = 2,column = 1,padx = 3,pady = 5) 

    section_label = Label(frame,text = "Section",font = "Helvetica 20 bold",bg = "#726a95")
    section_label.grid(pady = 5,row = 3 ,column = 0)   

    section_var = StringVar()
    section_var.set("A")
    section_menu = OptionMenu(frame,section_var,"A","B","C","D")
    section_menu.grid(row = 3,column = 1,padx = 3,pady = 5)

    exam_label = Label(frame,text = "Exam:",font = "Helvetica 20 bold",bg = "#726a95")
    exam_label.grid(pady = 5,row = 4 ,column = 0)   

    Exam_var = StringVar()
    Exam_var.set("periodic-test 1")
    Exam_menu = OptionMenu(frame,Exam_var,"periodic-test 1","periodic-test 2","Mid-term","periodic-test 3","periodic-test 4","Final-Exam")
    Exam_menu.grid(row = 4,column = 1,padx = 3,pady = 5) 
 
    frame2 = Frame(c_eleventh_twelfth)
    frame2.place(relx = 0.35,rely = 0.43)

    subject1_var = StringVar()
    subject1_var.set("B.S.T")
    subject1_label = Label(frame2,textvariable = subject1_var,font = "Helvetica 20 bold")
    subject1_label.grid(pady = 5)

    marks1_ent = Entry(frame2,width = 30)
    marks1_ent.grid(row = 0,column = 1,padx = 3,pady = 5)


    subject2_var = StringVar()
    subject2_var.set("Accounts")
    subject2_label = Label(frame2,textvariable = subject2_var,font = "Helvetica 20 bold")
    subject2_label.grid(pady = 5)

    marks2_ent = Entry(frame2,width = 30)
    marks2_ent.grid(row = 1,column = 1,padx = 3,pady = 5)


    subject3_var = StringVar()
    subject3_var.set("Statistics")
    subject3_label = Label(frame2,textvariable = subject3_var,font = "Helvetica 20 bold")
    subject3_label.grid(pady = 5)

    marks3_ent = Entry(frame2,width = 30)
    marks3_ent.grid(row = 2,column = 1,padx = 3,pady = 5)

    subject4_var = StringVar()
    subject4_label = Radiobutton(frame2,text = "Mathematics",variable = subject4_var,font = "Helvetica 20 bold",command = subject_choice,value = "Mathematics")
    subject4_label.grid(pady = 5)

    marks4_ent = Entry(frame2,width = 30)
    marks4_ent.grid(row = 3,column = 1,padx = 3,pady = 5)

    subject_label = Radiobutton(frame2,text = "Entrepreneurship",variable = subject4_var,font = "Helvetica 20 bold",command = subject_choice,value = "Entrepreneur")
    subject_label.grid(pady = 5)
    
    marks_ent = Entry(frame2,width = 30)
    marks_ent.grid(row = 4,column = 1,padx = 3,pady = 5)

    subject5_var = StringVar()
    subject5_var.set("English")
    subject5_label = Label(frame2,textvariable = subject5_var,font = "Helvetica 20 bold")
    subject5_label.grid(pady = 5)

    marks5_ent = Entry(frame2,width = 30)
    marks5_ent.grid(row = 5,column = 1,padx = 3,pady = 5)

    button_frame = Frame(c_eleventh_twelfth)
    button_frame.place(relx = 0.35,rely = 0.80)

    Save_button = Button(button_frame,text = "Export/Save",font = "Helvetica 20 bold",width=40,command=save)
    Save_button.grid(pady = 5)

    Open_button = Button(button_frame,text = "Open Report-Card",font = "Helvetica 20 bold",width = 40)
    Open_button.grid(pady = 5)



    back_button = Button(c_eleventh_twelfth,text = "Back",command = back3,font = "Helvetica 20 bold")
    back_button.grid()

def class_section4():
    global c_eleventh_twelfth_science
    global subject4_var
    global subject4_label
    global marks4_ent
    global subject_label
    global marks_ent
    global subject5_label
    global frame2
    global student_ent
    global studentid_ent
    global class_var
    global section_var
    global Exam_var
    global subject1_var
    global marks1_ent
    global subject2_var
    global marks2_ent
    global subject3_var
    global marks3_ent
    global subject4_var
    global marks4_ent
    global subject5_var
    global marks5_ent
    main_window.withdraw()
    c_eleventh_twelfth_science = Toplevel(main_window)
    c_eleventh_twelfth_science.title("Class  11th-12th(Science)")
    c_eleventh_twelfth_science.resizable(0,0)
    c_eleventh_twelfth_science.geometry("1310x700")
    c_eleventh_twelfth_science.config(bg = "#74d4c0")

    frame = Frame(c_eleventh_twelfth_science,bg = "#74d4c0")
    frame.place(relx = 0.35,rely = 0.1)

    studentid_label = Label(frame,text = "Student - Id:",bg = "#74d4c0",font = "Helvetica 20 bold")
    studentid_label.grid(pady = 5)

    studentid_ent = Entry(frame,width = 30)
    studentid_ent.grid(row = 0,column = 1,padx = 3,pady = 5)

    student_label = Label(frame,text = "Student - Name:",bg = "#74d4c0",font = "Helvetica 20 bold")
    student_label.grid(pady = 5)

    student_ent = Entry(frame,width = 30)
    student_ent.grid(row = 1,column = 1,padx = 3,pady = 5)

    class_label = Label(frame,text = "Choose class:",bg = "#74d4c0",font = "Helvetica 20 bold")
    class_label.grid(pady = 5)

    class_var = StringVar()
    class_var.set("11th")
    class_menu = OptionMenu(frame,class_var,"11th-standard","12th-standard")
    class_menu.grid(row = 2,column = 1,padx = 3,pady = 5) 

    section_label = Label(frame,text = "Section",font = "Helvetica 20 bold",bg = "#74d4c0")
    section_label.grid(pady = 5,row = 3 ,column = 0)   

    section_var = StringVar()
    section_var.set("A")
    section_menu = OptionMenu(frame,section_var,"A","B","C","D")
    section_menu.grid(row = 3,column = 1,padx = 3,pady = 5)

    exam_label = Label(frame,text = "Exam:",font = "Helvetica 20 bold",bg = "#74d4c0")
    exam_label.grid(pady = 5,row = 4 ,column = 0)   

    Exam_var = StringVar()
    Exam_var.set("periodic-test 1")
    Exam_menu = OptionMenu(frame,Exam_var,"periodic-test 1","periodic-test 2","Mid-term","periodic-test 3","periodic-test 4","Final-Exam")
    Exam_menu.grid(row = 4,column = 1,padx = 3,pady = 5) 
 
    frame2 = Frame(c_eleventh_twelfth_science)
    frame2.place(relx = 0.35,rely = 0.43)

    subject1_var = StringVar()
    subject1_var.set("Computer-Science")
    subject1_label = Label(frame2,textvariable = subject1_var,font = "Helvetica 20 bold")
    subject1_label.grid(pady = 5)

    marks1_ent = Entry(frame2,width = 30)
    marks1_ent.grid(row = 0,column = 1,padx = 3,pady = 5)


    subject2_var = StringVar()
    subject2_var.set("Physics")
    subject2_label = Label(frame2,textvariable = subject2_var,font = "Helvetica 20 bold")
    subject2_label.grid(pady = 5)

    marks2_ent = Entry(frame2,width = 30)
    marks2_ent.grid(row = 1,column = 1,padx = 3,pady = 5)


    subject3_var = StringVar()
    subject3_var.set("Chemistry")
    subject3_label = Label(frame2,textvariable = subject3_var,font = "Helvetica 20 bold")
    subject3_label.grid(pady = 5)

    marks3_ent = Entry(frame2,width = 30)
    marks3_ent.grid(row = 2,column = 1,padx = 3,pady = 5)

    subject4_var = StringVar()
    subject4_label = Radiobutton(frame2,text = "Mathematics",variable = subject4_var,font = "Helvetica 20 bold",command = subject_choice,value = "Mathematics")
    subject4_label.grid(pady = 5)
    


    marks4_ent = Entry(frame2,width = 30)
    marks4_ent.grid(row = 3,column = 1,padx = 3,pady = 5)

    subject_label = Radiobutton(frame2,text = "Biology",variable = subject4_var,font = "Helvetica 20 bold",command = subject_choice,value = "Biology")
    subject_label.grid(pady = 5)
    
    marks_ent = Entry(frame2,width = 30)
    marks_ent.grid(row = 4,column = 1,padx = 3,pady = 5)

    subject5_var = StringVar()
    subject5_var.set("English")
    subject5_label = Label(frame2,textvariable = subject5_var,font = "Helvetica 20 bold")
    subject5_label.grid(pady = 5)

    marks5_ent = Entry(frame2,width = 30)
    marks5_ent.grid(row = 5,column = 1,padx = 3,pady = 5)

    button_frame = Frame(c_eleventh_twelfth_science)
    button_frame.place(relx = 0.35,rely = 0.80)

    Save_button = Button(button_frame,text = "Export/Save",font = "Helvetica 20 bold",width=40,command=save)
    Save_button.grid(pady = 5)

    Open_button = Button(button_frame,text = "Open Report-Card",font = "Helvetica 20 bold",width = 40,command = open_file)
    Open_button.grid(pady = 5)



    back_button = Button(c_eleventh_twelfth_science,text = "Back",command = back4,font = "Helvetica 20 bold")
    back_button.grid()

    
frame = Frame(main_window,bg = "grey")
frame.place(relx = 0.20,rely = 0.32)

classes = Button(frame,text = "Class 1st- 4th",font = "Helvetica 20 bold",width=40,command = class_section1)
classes.grid(pady = 5)

classes = Button(frame,text = "Class 5th - 10th",font = "Helvetica 20 bold",width = 40,command = class_section2)
classes.grid(pady = 5)

classes = Button(frame,text = "Class 11th - 12th(Commerce)",font = "Helvetica 20 bold",width = 40,command = class_section3)
classes.grid(pady = 5)

classes = Button(frame,text = "Class 11th - 12th(Science)",font = "Helvetica 20 bold",width = 40,command = class_section4)
classes.grid(pady = 5)


window_quit = Button(frame,text = "Quit",font = "Helvetica 20 bold",width = 40 ,command = quit_function)
window_quit.grid(pady = 5)

Back = Button(main_window   ,text = "Back",font = "Helvetica 20 bold",width = 20 ,command = back0)
Back.grid(pady = 5)

##########################################
main_window.mainloop()
