import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# ----------READING DATA ---------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

new_dictionary = data.to_dict(orient="records")



# ---------FUNCTIONS-------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_dictionary)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def right_answer():
    new_dictionary.remove(current_card)
    print(len(new_dictionary))
    data = pandas.DataFrame(new_dictionary)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------UI-------------------
# ------WINDOW
window = tkinter.Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
# ----CARDS
front_card = tkinter.PhotoImage(file="./images/card_front.png")
back_card = tkinter.PhotoImage(file="./images/card_back.png")

# -----CANVAS
canvas = tkinter.Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# ----BUTTONS
right_image = tkinter.PhotoImage(file="./images/right.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

