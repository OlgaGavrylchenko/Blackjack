'''
    CIT 287 - Final Examination
    Write a program that allows a user to,
    a very limited extend, to play the game of blackjack.

    @Created by Olga Gavrylchenko, 04/25/2017
'''

from tkinter import *
from tkinter import messagebox as messageBox

import game_data
import startGame
import global_data

listOfWinLoseBox = []

##create a window
window = Tk()

##create title
window.title("Blackjack")

##set a window size
window.geometry("800x650")
window.resizable(0, 0)
        

##create frame to display result
frameTotal = Frame(window, width=800, height=50, bg="white")
frameTotal.pack_forget()
##frameTotal.pack(side=TOP)
        
##create mainFrame
frameMain = Frame(window, width=800, height=570, bg="light green")
frameMain.pack_forget()
##frameMain.pack()

label_title = Label(frameTotal, anchor=CENTER, text="Available Funds: ",
                            bg="white", font="Times 14 bold")
label_title.place(x=50, y=15, width=150)
label_totalFunds = Label(frameTotal, text="$ "+str(global_data.USER_BALANCE),
                                 font="Times 14 bold", bg="white", anchor=CENTER)
label_totalFunds.place(x=200, y=15, width=100)

def removeWinLoseBox():
    for labelItem in listOfWinLoseBox:
        labelItem.destroy()
    listOfWinLoseBox[:] = []
    
        
def createGameBoard():
    removeWinLoseBox()

    if global_data.USER_BALANCE != -1000:
        frameTotal.pack(side=TOP)
        frameMain.pack()
        updateLabelTotalFunds()
        ##start game
        startGame.startGame(frameMain)
        
    else:
        gameOverMessageBox()


def exitGame():
    result = messageBox.askyesno("Confirmation", "Are you sure, you would like to QUIT a game?")
    if result == 1:
        messageBox.showinfo("Confirmation", "See you later")
        window.destroy()

def displayAvailableFunds():
    updateLabelTotalFunds()
    result = messageBox.showinfo("Information",
                                 "Your Available Funds is $ "+str(global_data.USER_BALANCE))


def resetFundsToZero():
    result = messageBox.askyesno("Confirmation", "Are you sure, you would like to RESET all your winnings to zero?")
    if result == 1:
        global_data.USER_BALANCE = 0.00
        updateLabelTotalFunds()


def gameOverMessageBox():
    updateLabelTotalFunds()
    photo = PhotoImage(file='Cards/gameoverIcon.gif')
    label = Label(window, image=photo)
    label.image = photo
    listOfWinLoseBox.append(label)
    label.place(x=200, y=200, width=400, height=200)
        

def updateLabelTotalFunds():
    label_totalFunds['text'] = "$ "+str(global_data.USER_BALANCE)



##create menu
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Game Options", menu = filemenu)
filemenu.add_command(label="Play the Game", command=createGameBoard)
filemenu.add_command(label="Display Available Funds", command=displayAvailableFunds)
filemenu.add_command(label="Reset Funds to Zero", command=resetFundsToZero)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=exitGame)


#create frame to display copyright
frameBottom = Frame(window, bg="light grey", width=800, height=30)
frameBottom.pack(side=BOTTOM)


##create label and add to frame2
label_copyright = Label(frameBottom, text="Created by Olga Gavrylchenko, 04/25/2018",
                        justify=CENTER, fg="black", font="Times 10 bold")
label_copyright.place(x=0, y=0, width=800, height=30)


##start the program
window.mainloop()
