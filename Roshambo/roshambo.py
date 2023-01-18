## Roshambo / Rock Paper Scissors Game

## Import tkinter and random

import random
import tkinter as tk

## Create a window

window = tk.Tk()
window.geometry("400x300")
window.title("Roshambo")

## Create global variables for scores and choices

USER_SCORE = 0
COMP_SCORE = 0
USER_CHIOCE = ""
COMP_CHOICE = ""

## Convert and store choices as a number

def choice_to_number(choice):
    rps = {'rock':0, 'paper':1, 'scissor':2}
    return rps[choice]

def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]

## Create a function for computers hand, use random library to choose between rock, paper, or scissors

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

## Create result function to determine winner. Update scores based on wins.
## Create a text area to display current scores

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("This round is a tie!")
    elif((user-comp)%3==1):
        print("You won this round!")
        USER_SCORE+=1
    else:
        print("Comp winds")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)

    text_area.insert(tk.END,answer)

## Define 3 functions for possible user choices, when selected will generate comp choice as well and pass to result function

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE  
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE  
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

## Create buttons so the user can play the game

button1 = tk.Button(text="      Rock        ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)

button2 = tk.Button(text="      Paper        ",bg="pink",command=paper)
button2.grid(column=0,row=2)

button3 = tk.Button(text="      Scissor        ",bg="green",command=scissor)
button3.grid(column=0,row=3)

## generate mainloop to run program in
window.mainloop()
