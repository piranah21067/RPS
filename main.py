from tkinter import *
from random import *

root=Tk()
root.title("RPS Game")
root.geometry("900x500")

titleLabel=Label(text="Rock,Paper,Scissors",bg="black",fg="white",font=("arial",45))
titleLabel.place(x=200,y=50)

def option1():
    nameLabel = Label(text="Rock",bg="blue",fg="white",font=("arial" , 25),width=6)
    nameLabel.place(x=400 , y =250)
    computerMove = compMove()
    winLose(computerMove , "Rock")

def option2():
    nameLabel2 = Label(text="Paper",bg="blue",fg="white",font=("arial" , 25),width=6)
    nameLabel2.place(x=400 , y =250)
    computerMove = compMove()
    winLose(computerMove , "Paper")

def option3():
    nameLabel3 = Label(text="Scissors",bg="blue",fg="white",font=("arial" , 25),width=6)
    nameLabel3.place(x=400 , y =250)
    computerMove = compMove()
    winLose(computerMove , "Scissors")

def compMove():
    randRps=choice(["Rock","Paper","Scissors"])
    rpsLabel=Label(text=randRps,bg="purple",fg="white",font=("arial" , 25),width=6)
    rpsLabel.place(x=400 , y =350)
    return randRps

def winLose(compMove,playerMove):
    if compMove==playerMove:
        drawLabel=Label(text="draw",bg="grey",fg="pink",font=("arial",50),width=7)
        drawLabel.place(x=600,y=250)
    elif compMove == "Rock":
        if playerMove == "Paper":
            winLabel=Label(text="you win",bg="green",fg="black",font=("arial",50),width=7)
            winLabel.place(x=600,y=250)
        else:
            loseLabel=Label(text="you lose",bg="red",fg="white",font=("arial",50),width=7)
            loseLabel.place(x=600,y=250)
    elif compMove == "Paper":
        if playerMove == "Scissors":
            winLabel=Label(text="you win",bg="green",fg="black",font=("arial",50),width=7)
            winLabel.place(x=600,y=250)
        else:
            loseLabel=Label(text="you lose",bg="red",fg="white",font=("arial",50),width=7)
            loseLabel.place(x=600,y=250)
    elif compMove == "Scissors":
        if playerMove == "Rock":
            winLabel=Label(text="you win",bg="green",fg="black",font=("arial",50),width=7)
            winLabel.place(x=600,y=250)
        else:
            loseLabel=Label(text="you lose",bg="red",fg="white",font=("arial",50),width=7)
            loseLabel.place(x=600,y=250)


rockButton=Button(text="Rock",bg="orange",fg="white",font=("arial",25),width=8,command=option1)
rockButton.place(x=200,y=150)
    
paperButton=Button(text="Paper",bg="orange",fg="white",font=("arial",25),width=8,command=option2)
paperButton.place(x=400,y=150)

scissorsButton=Button(text="Scissors",bg="orange",fg="white",font=("arial",25),width=8,command=option3)
scissorsButton.place(x=600,y=150)


root.mainloop()
