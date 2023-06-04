from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 1
    # short_break_sec = 1
    # long_break_sec = 3
    reps += 1
    #print(reps)
    if reps % 8 == 0:
        # If it's the 8th rep:
        count_down(long_break_sec)
        #reps = 0
        #print("Long break")
        # timer_label['text'] = 'Long Break'
        # timer_label['fg'] = RED
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        # If it's the 2st/4rd/6th rep:
        count_down(short_break_sec)
        #print("Short break")
        # timer_label['text'] = 'Short Break'
        # timer_label['fg'] = PINK
        timer_label.config(text='Break', fg=PINK)
    elif reps % 2 != 0:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        #print("Work")
        # timer_label['text'] = 'Work'
        # timer_label['fg'] = GREEN
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer, check_mark_s
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        # count_sec = str(count_sec)
        # count_sec = "0" + count_sec
        count_sec = f"0{count_sec}"   # python can do it as its Dynamic Typing.
        # Dynamic Typing: allow you to change the type of variable by assigning different type of value.
    if count_min < 10:
        # count_min = str(count_min)
        # count_min = "0" + count_min
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_button()
        check_mark_s = ''
        completed_work_section = math.floor(reps/2)
        for _ in range(completed_work_section):
            check_mark_s += "✔"
        check_mark.config(text=check_mark_s)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# count_down(5)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(row=0, column=1)

button_left = Button(text="Start", highlightbackground=YELLOW, command=start_button)
button_left.grid(row=2, column=0)

button_right = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_right.grid(row=2, column=2)

# check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()