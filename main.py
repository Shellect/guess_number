import tkinter as tk
from tkinter import messagebox
from random import randint
from time import time

HEIGHT = 300
WIDTH = 400
secret_number = randint(1, 500)
begin_timestamp = time()
total_count = 0

root = tk.Tk()
root.title = "Угадай число"
screen_x = int(root.winfo_screenwidth() / 2 - WIDTH / 2)
screen_y = int(root.winfo_screenheight() / 2 - HEIGHT / 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")

lbl = tk.Label(root, text="Угадай число от 1 до 500")
lbl.pack()

sub_lbl = tk.Label(root, text=" ")
sub_lbl.pack()

fr = tk.Frame(root, pady=15)
fr.pack()

user_answer = tk.Entry(fr)
user_answer.pack(side="left")

def guess_number(e):
    global total_count
    user_number = user_answer.get()
    if user_number.isalnum():
        user_number = int(user_number)
    else:
        return
    if user_number > secret_number:
        sub_lbl["text"] = "Не угадал, загаданное число меньше!"
        total_count = total_count + 1
    elif user_number < secret_number:
        sub_lbl["text"] = "Не угадал, загаданное число больше!"
        total_count = total_count + 1
    else:
        delta = time() - begin_timestamp
        seconds = round(delta % 60)
        minutes = delta // 60
        sub_lbl["text"] = "Угадал!"
        messagebox.showinfo("Игра окончена!", f"""
Вы потратили {minutes} минут, {seconds} секунд
и сделали {total_count} попыток
""")

btn = tk.Button(fr, text="Отгадать", command=guess_number)
btn.pack()
user_answer.bind('<Return>', guess_number)
root.mainloop()