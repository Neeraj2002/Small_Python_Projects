words = ["mango","computer", "banana", "water", "bottle", "garden", "apple", "chair", "router","strawberry",
         "pencil", "eraser", "papaya", "sharpener", "notebook", "grapes", "mobile", "headset", "photo", ]

def time():
    global time_left, score, miss
    if time_left > 10:
        pass
    else:
        time_label_count.configure(fg='red')

    if time_left > 0:
        time_left -= 1
        time_label_count.configure(text=time_left)
        time_label_count.after(1000, time)
    else:
        game_play_label.configure(text="Miss = {} | Total Score = {} | Words per min ={}".format(miss, score-miss, score))

        retry = messagebox.askretrycancel('Notification', 'To RETRY press ENTER')
        if retry == True:
            score = 0
            time_left = 60
            miss = 0
            time_label_count.configure(text=time_left)
            word_label.configure(text=words[0])
            score_label_count.configure(text=score)


def start_game(event):
    global score, miss
    if time_left == 60:
        time()
    game_play_label.configure(text="")
    if word_entry.get() == word_label['text']:
        score += 1
        score_label_count.configure(text=score)
    else:
        miss += 1

    random.shuffle(words)
    word_label.configure(text=words[0])
    word_entry.delete(0,END)

from tkinter import *
from tkinter import messagebox
import random

# Creating a space to work in

root = Tk()
root.geometry('800x500+250+100')
root.configure(bg='light blue')
root.title('TypingSpeedGame')
root.iconbitmap('online_learning_icon_182955.ico')

# Variables

score = 0
time_left = 60
miss = 0

# Labelling the space

font_label = Label(root, text='Welcome to typing speed game', font=('arial', 15, 'bold', ), bg='light blue', fg='blue')
font_label.place(x=260, y=30)

random.shuffle(words)
word_label = Label(root, text=words[0],font=('Times', 30, 'bold italic', ), bg='light blue')
word_label.place(x=335, y=200)

score_label = Label(root, text='Your Score:', font=('arial', 15, 'bold', ), bg='light blue', fg='red')
score_label.place(x=200, y=90)

score_label_count = Label(root, text= score, font=('arial', 15, 'bold', ), bg='light blue', fg='red')
score_label_count.place(x=250, y=130)

time_label = Label(root, text='Time Left: ', font=('arial', 15, 'bold', ), bg='light blue', fg='red')
time_label.place(x=525, y=90)

time_label_count = Label(root, text= time_left, font=('arial', 15, 'bold', ), bg='light blue', fg='red')
time_label_count.place(x=570, y=130)

game_play_label = Label(root, text='Enter the word correctly and hit enter', font=('arial', 15, 'bold', ), bg='light'
                                                                                                             ' blue'
                        , fg='grey')
game_play_label.place(x=225, y=350)

# Labelling the entry space by the user

word_entry = Entry(root, font=('Times', 20), bd=3, justify='center')
word_entry.place(x=250, y=250)
word_entry.focus_set()

root.bind('<Return>', start_game)
root.mainloop()