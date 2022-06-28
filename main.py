import tkinter as tk
from tkinter import *
import random, time









x = 0

num = 0

my_var = 0

remarks = 0

total_ques_in_quiz = 5

question_per_marks = 5

question_per_time = 10

total_time = total_ques_in_quiz * question_per_time




right_answer1 = open("system/do_not_open.txt", "r")
right_answer = right_answer1.read().split(" ")

right_answer1.close()
total_ques_quiz = total_ques_in_quiz - 1

question = open("system/dont.txt","r")
ques = question.read().split("\n")
question.close()


total_ques = int(len(ques)/5)


def times_up():

    global my_var,total_ques_quiz
    my_var = total_ques_quiz

    submit()


def timer():

    global now_second,total_time

    if(total_time == 0):
        times_up()

    else:

        timer_hour = int(total_time/3600)

        timer_min = int((total_time - (timer_hour * 3600))/60)

        timer_sec = int(total_time - ((timer_hour*3600)+(timer_min*60)))

        try:

            time_hour_for = "{0:0=2d}".format(timer_hour)
            time_min_for = "{0:0=2d}".format(timer_min)
            time_sec_for = "{0:0=2d}".format(timer_sec)

        except:
            #this is for python 2 and lower versions of python 3
            time_hour_for = "%02d"%timer_hour
            time_min_for = "%02d"%timer_min
            time_sec_for = "%02d"%timer_sec

        time_string = str(time_hour_for) + ":" + str(time_min_for) +  ":" + str(time_sec_for)
        clock_label.config(text = time_string)

        total_time = total_time - 1
        clock_label.after(1000, timer)

def time_management():

    global now_second
    recent_time = time.strftime("%H:%M:%S").split(":")
    now_minute = (int(recent_time[0]) * 60) + int(recent_time[1])
    now_second = (now_minute * 60) + int(recent_time[2])


def restart_quiz():
    global result_label,result_label_image,Start_new_quiz_btn,label_score,x,num,my_var,remarks,total_time,total_ques_quiz,question_per_time

    result_label.destroy()
    result_label_image.destroy()
    Start_new_quiz_btn.destroy()
    label_score.destroy()

    x = 0
    num = 0
    my_var = 0
    remarks = 0
    total_time = total_ques_in_quiz * question_per_time

    start_page_create()


def start_page_create():
    global Logo_image,logo_label, head_label,Quiz_startbtn,term_label,total_ques_in_quiz,question_per_marks
    m.config(
        background="#ffffff"
    )
    Logo_image = PhotoImage(file="images/logo.png")
    logo_label = Label(
        m,
        image=Logo_image,
        border=0,
        justify="center",
    )
    logo_label.pack(pady=(30, 10))#pack logo label
    head_label = Label(
        m,
        text="Quiz Game",
        font=("Comic sans MS", 24, "bold"),
        background="#ffffff",
        justify="center",
    )
    head_label.pack(pady=(0, 10))

    quiz_start_logo = PhotoImage(file="images/start_quiz.png")
    Quiz_startbtn = Button(
        m,
        image=quiz_start_logo,
        border=0,
        background="#ffffff",
        command=start_btnpress
    )
    Quiz_startbtn.pack(pady=30)

    Quiz_startbtn.image = quiz_start_logo

    term_label = Label(
        m,
        text="Rules for this Quiz Game\n"
             "*This game have " + str(total_ques_in_quiz) + " questions and each question have " + str(question_per_marks) + " marks\n"
             "You have " + str(total_time/60) + " minute to answer this questions\n"
             "*Cheak before submiting your answer\n"
             "*Answer's are not changeable after submiting.\n"
             "*After submiting answers result will be shown in main window",
        background="blue",
        width=580,
        justify="center",
    ) #tearms and condition label create
    term_label.pack(padx=10)


def save_question():
    global qtn_enty,qtn_enty_op2,qtn_enty_op1,qtn_enty_op3,qtn_enty_op,answer_var

    save_string = "\n" + qtn_enty.get() + "\n" + qtn_enty_op.get() + "\n" + qtn_enty_op1.get() + "\n" + qtn_enty_op2.get() +"\n" + qtn_enty_op3.get()
    save_to_file = open("system/dont.txt", "a")
    save_to_file.write(save_string)
    save_to_file.close()

    answer_file = open("system/do_not_open.txt", "a")
    answer_file.write(" " + str(answer_var.get()))
    answer_file.close()

def question_entry():
    global qtn_enty,qtn_enty_op2,qtn_enty_op1,qtn_enty_op3,qtn_enty_op,answer_var
    n = Tk()
    n.geometry("600x700")
    n.resizable(0,0)
    n.wm_iconbitmap("images/logo_official.ico")
    n.title("New question entry point")
    answer_var = IntVar()
    answer_var = (-1)

    question_entry_label = Label(
        n,
        text = "question entry point",
        font = ("bold",30)
    )

    question_entry_label.pack()

    question_entry_label_small = Label(
        n,
        text= "Enter Question",
        font = ("bold",16)
    )
    question_entry_label_small.place(x=50,y=70)

    qtn_enty = Entry(
        n,
        width =30,
        font = (16)

    )
    qtn_enty.pack(padx=220,pady=(22,39))

    question_entry_label_small_0 = Label(
        n,
        text="Enter Option 1",
        font=("bold", 16)
    )
    question_entry_label_small_0.place(x=50, y=170)

    save_answer1 = Radiobutton(
        n,
        value=0,
        variable=answer_var,
    )
    save_answer1.place(x=200, y=173)

    qtn_enty_op = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op.pack(padx=220, pady=34)

    question_entry_label_small_1 = Label(
        n,
        text="Enter Option 2",
        font=("bold", 16)
    )
    question_entry_label_small_1.place(x=50, y=270)

    save_answer2 = Radiobutton(
        n,
        value=1,
        variable=answer_var,
    )
    save_answer2.place(x=200, y=273)

    qtn_enty_op1 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op1.pack(padx=220, pady=37)

    question_entry_label_small_2= Label(
        n,
        text="Enter Option 3",
        font=("bold", 16)
    )
    question_entry_label_small_2.place(x=50, y=370)

    save_answer3 = Radiobutton(
        n,
        value=2,
        variable=answer_var,
    )
    save_answer3.place(x=200, y=373)

    qtn_enty_op2 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op2.pack(padx=220, pady=37)

    question_entry_label_small_3 = Label(
        n,
        text="Enter option 4",
        font=("bold", 16)
    )
    question_entry_label_small_3.place(x=50, y=470)

    save_answer4 = Radiobutton(
        n,
        value=3,
        variable=answer_var,
    )
    save_answer4.place(x=200, y=473)

    qtn_enty_op3 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op3.pack(padx=220, pady=37)

    question_entry_btn = Button(
        n,
        text = "save",
        command = save_question

    )
    question_entry_btn.place(x = 400,y=570)
    n.mainloop()


def reviewer():
    global num, answerss,my_var,remarks,ques_set,right_answer

    if(answerss.get() == int(right_answer[ques_set[my_var]])):

        remarks = remarks + 1

def result():
    global remarks,question_per_marks,total_ques_in_quiz,question_per_marks,result_label,result_label_image,Start_new_quiz_btn,label_score

    marks = remarks * question_per_marks

    excelent_image = PhotoImage(file="images/excelent.png")
    ordinary_image = PhotoImage(file="images/ordinary.png")
    fail_image = PhotoImage(file="images/fail.png")

    m.config(
        background = "#8BE2FF"
    )

    result_label = Label(
        m,
        text= "you got " + str(question_per_marks * remarks),
        background = "#8BE2FF",
        font = ("bold",30)
    )
    result_label.pack()

    result_label_image = Label(
        m,
        border=0
    )
    result_label_image.pack()


    total_marks = total_ques_in_quiz*question_per_marks
    remark_percent_st1 = 100/total_marks
    remark_percent = remark_percent_st1 * marks

    if (remark_percent >= 80.0):

        result_label_image.config(image=excelent_image)
        result_label_image.image = excelent_image
        label_score = Label(
            m,
            text="Wow carry on",
            background="#8BE2FF",
            font=('bold', 30)
        )
        label_score.pack()

    elif(remark_percent > 50.0):

        result_label_image.config(image=ordinary_image)
        result_label_image.image = ordinary_image
        label_score = Label(
            m,
            text = "you need to do better",
            background = "#8BE2FF",
            font = ('bold', 30)
        )
        label_score.pack()
    else:
        result_label_image.config(image=fail_image)
        result_label_image.image = fail_image
        label_score = Label(
            m,
            text="Dont sad, next time you do better",
            background="#8BE2FF",
            font=('bold', 26)
        )
        label_score.pack()

    new_quiz_logo = PhotoImage(file="images/start_new_quiz.png")
    Start_new_quiz_btn = Button(
        m,
        image = new_quiz_logo,
        command = restart_quiz
    )
    Start_new_quiz_btn.place(x=530,y=520)
    Start_new_quiz_btn.image = new_quiz_logo


def question_no_genarator():
    global ques_set,ques,x,total_ques,total_ques_quiz

    ques_set = [0]

    while(len(ques_set)<=total_ques_quiz):
        value = random.randint(0,total_ques-1)

        if(value in ques_set):
            continue

        else:
            ques_set.append(value)
            x += 1


def submit():
    global answerss,ques_set,num,question_label,radiobtn,radiobtn3,radiobtn1,radiobtn2,submit_btn,total_ques_in_quiz,my_var,remarks,clock_label

    question_label.destroy()
    radiobtn.destroy()
    radiobtn1.destroy()
    radiobtn2.destroy()
    radiobtn3.destroy()
    submit_btn.destroy()


    if(my_var == total_ques_quiz):

        if (answerss.get() == right_answer[ques_set[my_var-1]]):
            remarks = remarks + 1
        reviewer()

        result()

        clock_label.destroy()

    else:
        reviewer()
        my_var = my_var + 1

        start_quiz()


def start_quiz():
    global  answerss,num,question_label,radiobtn,radiobtn3,radiobtn1,radiobtn2,submit_btn,my_var,clock_label,now_second
    num = ques_set[my_var] * 5

    m.config(
        bg = "#43d4d9"
    )

    question_label = Label(
        m,
        text = ques[num],
        bg = "#43d4d9",
        font = ("bold",24)
    )
    question_label.pack(pady = 50)
    answerss = IntVar()   #create variable to get answer from user


    radiobtn = Radiobutton(
        m,
        text = ques[num+1],
        value = 0,
        variable = answerss,
        bg="#addcde",
        width = 50,
        height = 2,
        font = (20)
    )
    radiobtn.pack(pady = 10)

    radiobtn1 = Radiobutton(
        m,
        text=ques[num+2],
        value = 1,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn1.pack(pady = 10)

    radiobtn2 = Radiobutton(
        m,
        text=ques[num+3],
        value = 2,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn2.pack(pady = 10)

    radiobtn3 = Radiobutton(
        m,
        text=ques[num+4],
        value = 3,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn3.pack(pady = 20)

    Submit_logo = PhotoImage(file="images/submit.png")
    submit_btn = Button(
        m,
        image=Submit_logo,
        command = submit
    )
    submit_btn.pack()

    submit_btn.image = Submit_logo


def start_btnpress():
    global logo_label,head_label,Quiz_startbtn,term_label,clock_label

    logo_label.destroy()
    head_label.destroy()
    Quiz_startbtn.destroy()
    term_label.destroy()

    clock_label = Label(
        m,
        bg="#000000",
        fg="#ffffff",
        font = ("bold",30)
    )
    clock_label.place(x=540,y=0)
    timer()

    start_quiz()




m = tk.Tk()

m.title("Quiz game project by Samia & Aminul")

m.geometry("700x600")
m.wm_iconbitmap("images/logo_official.ico")

m.resizable(0,0)

menu = Menu(
    m
)
m.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="question_entry",menu = sub_menu)
sub_menu.add_cascade(label="question_entry",command= question_entry)
start_page_create()
question_no_genarator()

m.mainloop()