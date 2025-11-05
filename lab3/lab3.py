import tkinter as tk
import random


def main():
    global label
    root = tk.Tk()
    root.title("keygen")
    root.geometry("1600x900")
    canvas = tk.Canvas(root, height=900, width=1600)
    canvas.pack(fill="both", expand=True)

    img = tk.PhotoImage(file="lab3/re7.png")
    img = img.subsample(2, 2)

    but = tk.Button(root, text="get key", font=('Arial', 30), command=key)
    label = tk.Label(root, bg='White', text="", font=("Arial", 30))

    canvas.create_image(0, 0,image=img, anchor='nw')
    canvas.create_window(800, 300, window=but)
    canvas.create_window(800, 540, window=label)

    root.mainloop()


def key():
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    
    key1 = "".join(random.sample("".join(random.sample(alf, 3)) + "".join(random.sample(num, 1)), 4))
    key2 = "".join(random.sample("".join(random.sample(alf, 3)) + "".join(random.sample(num, 1)), 4))
    key3 = "".join(random.sample("".join(random.sample(alf, 3)) + "".join(random.sample(num, 1)), 4))
    key4 = "".join(random.sample("".join(random.sample(alf, 3)) + "".join(random.sample(num, 1)), 4))
    key = f"{key1}-{key2}-{key3}-{key4}"
    label.config(text=key)

main()