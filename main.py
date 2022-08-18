import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# ---------FUNCTIONS-------------
def right_answer():
    pass


# ----------READING DATA ---------
data = pandas.read_csv("./data/french_words.csv")
new_dictionary = pandas.DataFrame.todict(orient="records")



# ---------UI-------------------
# ------WINDOW
window = tkinter.Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----CARDS
front_card = tkinter.PhotoImage(file="./images/card_front.png")
back_card = tkinter.PhotoImage(file="./images/card_back.png")

# -----CANVAS
canvas = tkinter.Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 262, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 265, text="Pomme", font=("Arial", 60, "bold"))




#----BUTTONS
right_image = tkinter.PhotoImage(file="./images/right.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
window.mainloop()
