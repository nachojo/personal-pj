from tkinter import*
from tkinter import ttk
import time
from datetime import datetime, timedelta
import webbrowser


def web():
    #
    time_del()


def time_del():
    time1 = datetime.now()
    while True:
        time2 = datetime.now()
        if time2 == time1 + timedelta(seconds=5):
            #
            pr_time.config(text="~~")
            break


def alarm():
    set_t = set_time.get()
    global dt_cur
    dt_cur = datetime.now()
    while True:
        now_time = time.strftime('%X', time.localtime(time.time()))
        if now_time == set_t:
            web()
            break


window = Tk()
window.geometry('410x210+500+300')
set_time = StringVar()
window.title("program")
title_label = Label(window, text="제목입니다").grid(row=0, column=0)
input_exam = Label(window, text="시간을 00:00:00으로 입력해주세요.").grid(
    row=1, columnspan=2)

mac_entry = Entry(window, textvariable=set_time).grid(row=2, column=0)
pr_time = Label(window)
act_btn = Button(window, text=" 설정 ", width=20,
                 command=alarm).grid(row=2, column=1)
pr_time.grid(row=3, column=0)
window.mainloop()
