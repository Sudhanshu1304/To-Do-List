from DataBase import Read, Write2, Write3
from tkinter import *
from tkinter import ttk
import PIL  as Im
from PIL import ImageTk
import time
import random

################################################                            ############################################


'''

@ Global Function and Variables : 

It Contains Functions Common to Various Windows 
Features:
1. Display Content Method


@ Window 1:

Features:
1. Create New List
2. Names of Old Lists

'''


def Getinput():
    global t, s, count2, list1, win1

    win = Tk()
    win.title("Create New List")
    c = Canvas(win, height=500, width=400, bg='#232778')  # '#db5864')
    c.pack(pady=30, padx=10)

    entry = Entry(c, font=(10))
    c.create_window(120, 20, window=entry)
    t = 1
    s = 90

    list1 = []
    import random

    tt = 90

    def creat_label3(A):
        global tt
        d.create_text(160, 30, text='Follow This Sequence'.upper(), font=('bold'))

        l1 = Label(d, text=A, font=('bold'), width=20)
        d.create_window(200, tt, window=l1)

        c = Checkbutton(d, font=('bold'))
        d.create_window(340, tt, window=c)

        tt = tt + 60

    def first_window():
        win3 = Tk()
        win3.title("NEW LIST")

    def Done():
        global d

        win.destroy()
        win2 = Tk()
        win2.title('SUDHANSHU')

        d = Canvas(win2, height=500, width=400, bg='dark blue')
        d.pack(pady=30, padx=10)

        b = Button(d, text=' THANKS ', command=lambda: win2.destroy(), bg='red', font=(30))
        d.create_window(320, 460, window=b)

        global list1

        data = Read()
        list1 = list(data["Sudhanshu"].values())
        random.shuffle(list1)

        for i in range(len(list1)):
            if list1[i] == '':
                pass
            else:
                creat_label3(list1[i])

        mainloop()

    def create_label1(task):

        global list1
        list1.append(str(e1.get()).upper())
        d = {str(entry.get()): {"Task-{}".format(task): str(e1.get()).upper()}}

        Write2(d)
        create_label()
        c.update()

    count2 = 0

    def Done1():
        global win1
        win1.update()
        win1.destroy()
        win.update()
        win.destroy()

        __init__()

    def create_label():

        global e1, t, s, count2
        l1 = Label(c, text=t, font=(10), fg='red')
        e1 = Entry(c, font=(10))

        c.create_window(30, s, window=l1)
        c.create_window(200, s, window=e1)
        t = t + 1
        s = s + 60

        if count2 < 25:
            b = Button(c, text=' ADD ', command=lambda: create_label1(t), font=(30))

        else:
            b = Button(c, text=' ADD ', font=(30))
        c.create_window(360, 470, window=b)
        count2 = count2 + 1

        d = Button(c, text=' DONE ', command=lambda: Done1(), font=(30))
        c.create_window(270, 470, window=d)

        return t, s

    create_label()
    mainloop()


###################                               Global Functions and Variables

def __init__():
    global e, win1
    Data = Read()

    e = 0

    def Delete_List(list_name):
        data = Read()

        del data[list_name]

        Write3(data)
        win1.update()
        win1.destroy()
        __init__()

    def Delete_Task(task):

        global game, name
        var = random.randint(100, 5000)
        d = {"Completed": {"Task-{}".format(var): task}}
        Write2(d)
        data = Read()
        Task = data[name]

        values = list(Task.values())
        key = list(Task.keys())
        flag = 0
        for i in range(len(Task)):
            if values[i] == task:
                flag = 1
                break

        if flag == 1:
            Task.pop(key[i])
            flag = 0
        data[name] = Task
        Write3(data)
        win1.update()
        win1.destroy()
        __init__()

    def ENTER(win):

        global LENGTH, d, name, e
        dd = {}

        val = {'TASK-{}'.format(LENGTH): str(e.get())}

        dd[name] = val
        Write2(dd)

        e = Entry(win, font='bold', width=25)
        e.grid(row=LENGTH + 4, column=0, padx=10, pady=10)
        for _ in range(10):
            win.update()

        LENGTH = LENGTH + 1

    def Done1(win):

        global win1, win2

        win.update()
        win.destroy()

        win1.update()
        win1.destroy()

        __init__()

    def Display(Window, list, widget, function=None, costum_win_1=False, command=None, display=True, window3=None):

        global e, LENGTH, d, name
        Window.geometry("453x520+600+100")

        pos = [150, 100]

        main_frame = Frame(Window, bd=5)
        main_frame.pack(expand=1, fill=BOTH)

        c = '#232778'  # '#db5864'
        list_color = 'white'
        relif = 'ridge'
        border_color = 'green'
        boder_width = 5

        canvas = Canvas(main_frame, bg=c)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scroll_y = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        secounf_frame = Frame(canvas, bg=c, bd=5)

        canvas.create_window((0, 0), window=secounf_frame, anchor='nw')

        if display == True:

            if costum_win_1 == True:
                c = Label(secounf_frame, bg=c, fg='white', width=22, text='WELCOME'.upper(),
                          font=("Times", "16", "bold italic"))
                c.grid(column=0, row=0, padx=5)
                b = Button(secounf_frame, text="New List", font=('bold', 15), command=lambda: Window_3(),
                           bd=boder_width)
                b.grid(column=1, row=0, padx=0, pady=20)

            else:
                e = Entry(secounf_frame, font='bold', width=25)
                e.grid(row=LENGTH + 4, column=0, padx=10, pady=10)
                LENGTH = LENGTH + 1

                b = Button(secounf_frame, text="Create Task", font=('bold'), command=lambda: ENTER(secounf_frame),
                           bd=boder_width)
                b.grid(column=0, row=0, padx=0, pady=20)
                b1 = Button(secounf_frame, text="SAVE", font=('bold'), command=lambda: Done1(Window), bd=boder_width)

                b1.grid(column=1, row=0, padx=0, pady=20)

            for i in range(len(list)):

                if widget == Button:
                    command = lambda name=list[i]: function(name)
                    command2 = lambda name=list[i]: Delete_List(name)

                    text = 'DELETE'
                else:
                    command2 = lambda name=list[i]: Delete_Task(name)
                    text = 'DONE'

                if len(list[i]) != 0 and list[i] != '\n' and list[i] != '\n\n':
                    l = widget(secounf_frame, text=list[i], bg=list_color, font=("Arial", "14", "bold italic"),
                               width=22, command=command, bd=boder_width + 2, highlightbackground=border_color)
                    l.grid(column=0, row=i + 2, padx=15, pady=10)  # pack(fill=BOTH, expand=True)
                    l1 = Button(secounf_frame, text=text, font=('bold'), width=8, relief=relif, command=command2,
                                bd=boder_width)
                    l1.grid(column=1, row=i + 2, padx=0, pady=20)  # pack(fill=BOTH, expand=True)

        main_frame.config(bg='white')

    def Window_3():

        Getinput()
        win1.update()

    def Window2(ID):

        global LENGTH, add, d, name, win2
        d = {}
        win2 = Tk()
        win2.title(str(ID))
        win2.geometry("444x520+600+100")

        List = Data[ID].values()
        lis = []

        for i in List:
            lis.append(i)
        LENGTH = len(lis)
        name = ID
        Display(win2, lis, Label, LENGTH)

        win2.mainloop()

    win1 = Tk()
    win1.title("LISTS")
    win1.geometry("450x520+600+100")

    list1 = list(Data.keys())

    Display(win1, list1, Button, costum_win_1=True, function=Window2)

    win1.mainloop()


__init__()

