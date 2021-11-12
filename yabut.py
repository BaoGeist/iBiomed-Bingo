import tkinter as tk
import random

cardsString =[]
f = open('cards.txt', 'rt')
for line in f:
    cardsString.append(line)

random.shuffle(cardsString)

window = tk.Tk()
window.title('YABUT - BINGO')
lbl1 = tk.Label(master = window, text = cardsString[0], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl2 = tk.Label(master = window, text = cardsString[1], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl3 = tk.Label(master = window, text = cardsString[2], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl4 = tk.Label(master = window, text = cardsString[3], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl5 = tk.Label(master = window, text = cardsString[4], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl6 = tk.Label(master = window, text = cardsString[5], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl7 = tk.Label(master = window, text = cardsString[6], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl8 = tk.Label(master = window, text = cardsString[7], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl9 = tk.Label(master = window, text = cardsString[8], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl10 = tk.Label(master = window, text = cardsString[9], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl11 = tk.Label(master = window, text = cardsString[10], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl12 = tk.Label(master = window, text = cardsString[11], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl13 = tk.Label(master = window, text = cardsString[12], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl14 = tk.Label(master = window, text = cardsString[13], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl15 = tk.Label(master = window, text = cardsString[14], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl16 = tk.Label(master = window, text = cardsString[15], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl17 = tk.Label(master = window, text = cardsString[16], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl18 = tk.Label(master = window, text = cardsString[17], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl19 = tk.Label(master = window, text = cardsString[18], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl20 = tk.Label(master = window, text = cardsString[19], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl21 = tk.Label(master = window, text = cardsString[20], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl22 = tk.Label(master = window, text = cardsString[21], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl23 = tk.Label(master = window, text = cardsString[22], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl24 = tk.Label(master = window, text = cardsString[23], borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")
lbl25 = tk.Label(master = window, text = 'Free Space', borderwidth=2, relief="groove", width=20, height=5, wraplength=125, justify="center", font="helvetica 11")

lbl1.grid(row=0, column=0, pady = 10, sticky = tk.NSEW)
lbl2.grid(row=0, column=1, pady = 10, sticky = tk.NSEW)
lbl3.grid(row=0, column=2, pady = 10, sticky = tk.NSEW)
lbl4.grid(row=0, column=3, pady = 10, sticky = tk.NSEW)
lbl5.grid(row=0, column=4, pady = 10, sticky = tk.NSEW)
lbl6.grid(row=1, column = 0, pady = 10, sticky = tk.NSEW)
lbl7.grid(row=1, column=1, pady = 10, sticky = tk.NSEW)
lbl8.grid(row=1, column =2, pady = 10, sticky = tk.NSEW)
lbl9.grid(row=1, column =3, pady = 10, sticky = tk.NSEW)
lbl10.grid(row=1, column =4, pady = 10, sticky = tk.NSEW)
lbl11.grid(row=2, column =0, pady = 10, sticky = tk.NSEW)
lbl12.grid(row=2, column =1, pady = 10, sticky = tk.NSEW)
lbl25.grid(row=2, column =2, pady = 10, sticky = tk.NSEW)
lbl14.grid(row=2, column =3, pady = 10, sticky = tk.NSEW)
lbl15.grid(row=2, column =4, pady = 10, sticky = tk.NSEW)
lbl16.grid(row=3, column =0, pady = 10, sticky = tk.NSEW)
lbl17.grid(row=3, column =1, pady = 10, sticky = tk.NSEW)
lbl18.grid(row=3, column =2, pady = 10, sticky = tk.NSEW)
lbl19.grid(row=3, column =3, pady = 10, sticky = tk.NSEW)
lbl20.grid(row=3, column =4, pady = 10, sticky = tk.NSEW)
lbl21.grid(row=4, column =0, pady = 10, sticky = tk.NSEW)
lbl22.grid(row=4, column =1, pady = 10, sticky = tk.NSEW)
lbl23.grid(row=4, column =2, pady = 10, sticky = tk.NSEW)
lbl24.grid(row=4, column =3, pady = 10, sticky = tk.NSEW)
lbl13.grid(row=4, column =4, pady = 10, sticky = tk.NSEW)

window.mainloop()