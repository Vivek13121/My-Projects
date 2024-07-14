BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random
current_card = {}

try:
    data = pandas.read_csv("./Flashcard/data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("./Flashcard/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text= current_card["French"],fill = "black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text= current_card["English"],fill= "white")
    canvas.itemconfig(card_background, image= card_back)
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Flashcard/data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashcard")
window.minsize(width=1000, height=726)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

correct_img = PhotoImage(file="./Flashcard/images/right.png")
button1 = Button(image=correct_img, highlightthickness=0,command=is_known)
button1.place(x=600,y=550)

wrong_img = PhotoImage(file="./Flashcard/images/wrong.png")
button2 = Button(image=wrong_img, highlightthickness=0,command=next_card)
button2.place(x=200, y=550)


canvas = Canvas(height=526, width=800, highlightthickness=0)
card_front = PhotoImage(file="./Flashcard/images/card_front.png")
card_back = PhotoImage(file="./Flashcard/images/card_back.png")
card_background = canvas.create_image(400,263, image = card_front)
canvas.place(x=70,y=20)
canvas.config(bg=BACKGROUND_COLOR)

card_word = canvas.create_text(400, 263, text="Work", font=("Arial", 60, "bold"))
card_title = canvas.create_text(400, 150, text="French", font=("Arial" ,40, "italic" ))



next_card()












window.mainloop()