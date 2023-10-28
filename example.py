from tkinter import *
from random import randint


window= Tk() # it creates a gui ( Graphical user interface ) window
window.title("Dice")
window.geometry("700x500")

first = randint(1,6)
second = randint(1,6)
total = Label(text=first+second,bg="black",fg="white", font=("arial",60))
total.place(x=400,y=400)
nameLabel = Label(text=first,bg="black",fg="white",font=("arial" , 60))
nameLabel.place(x=randint(1,300) , y =randint(1,300))
nameLabel2 = Label(text=second,bg="black",fg="white",font=("arial" , 60))
nameLabel2.place(x=randint(1,300) , y = randint(1,300))

def roll():
    global total , nameLabel , nameLabel2
    first = randint(1,6)
    second = randint(1,6)
    total.destroy()
    nameLabel.destroy()
    nameLabel2.destroy()
    total = Label(text=first+second,bg="black",fg="white", font=("arial",60))
    total.place(x=400,y=400)
    nameLabel = Label(text=first,bg="black",fg="white",font=("arial" , 60))
    nameLabel.place(x=randint(1,300) , y =randint(1,300))
    nameLabel2 = Label(text=second,bg="black",fg="white",font=("arial" , 60))
    nameLabel2.place(x=randint(1,300) , y = randint(1,300))
    if first+second==12:
        win=Label(text="you win",bg="green",fg="white", font=("arial",60))
        win.place(x=250,y=250)

rollButton = Button(text="Roll",bg="black" , fg="white" , font=("arial" , 40) , command=roll )
rollButton.place(x =160, y = 400)

window.mainloop()