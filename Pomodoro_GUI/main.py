from tkinter import *
import math
#  CONSTANTS 
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


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00" )
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
    
    

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label = Label(text="Long Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
        label.place(x=120,y=10)
    elif reps% 2 == 0:
        label = Label(text="Short Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
        label.place(x=120,y=10)
        countdown(short_break_sec)
    else:
        countdown(work_sec)


def countdown (count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.minsize(width=800, height=500)
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=324, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Pomodoro_GUI/tomato.png")
canvas.create_image(100,200, image=tomato_img)
timer_text = canvas.create_text(105,225, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.place(x=200,y=5)


label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.place(x=200,y=10)

button_start = Button(text="Start", bg = RED, fg="white" ,command=start_timer, width=10,height=2, font=(FONT_NAME, 10, "bold"))
button_start.place(x=120,y=320)

button_reset = Button(text="Reset", bg=RED,fg="white", width=10,height=2, font=(FONT_NAME, 10, "bold"), command=reset_timer)
button_reset.place(x=400,y=320)

check_mark = Label(font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg=GREEN)
check_mark.place(x=250,y=350)


window.mainloop()


















