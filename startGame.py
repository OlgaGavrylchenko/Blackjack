'''
    CIT 287 - Final Examination
    Write a program that allows a user to,
    a very limited extend, to play the game of blackjack.

    @Created by Olga Gavrylchenko, 04/25/2017
'''
from tkinter import *
from tkinter import messagebox as messageBox

import game_data
import global_data

##const values
L_WIDTH=170
L_HEIGHT=240

L_PADX = 10
L_PADY = 10


##list of used cards
listOfCards = []
listValueOfCards = []
listOfLabels = []
listOfWinLoseBox = []

def winMessageBox(frameMain):
    photo = PhotoImage(file='Cards/congratulationsIcon.gif')
    label = Label(frameMain, image=photo)
    listOfWinLoseBox.append(label)
    label.image = photo
    label.place(x=200, y=200, width=400, height=150)

def loseMessageBox(frameMain):
    photo = PhotoImage(file='Cards/loseIcon.gif')
    label = Label(frameMain, image=photo)
    listOfWinLoseBox.append(label)
    label.image = photo
    label.place(x=200, y=200, width=400, height=150)

def gameOverMessageBox(frameMain):
    photo = PhotoImage(file='Cards/gameoverIcon.gif')
    label = Label(frameMain, image=photo)
    listOfWinLoseBox.append(label)
    label.image = photo
    label.place(x=200, y=200, width=400, height=200)
    

def displayRandomCards(frameMain):
    
    if len(listOfCards) == 2:
        coordX = 200
        coordY = 10
        for card in listOfCards:
            for key in card.keys():
                photo = PhotoImage(file=key)
                label = Label(frameMain, image=photo, relief=RAISED)
                ##hold reference to an image
                label.image = photo
                label.place(x=coordX, y=coordY, width=L_WIDTH, height=L_HEIGHT)
                listOfLabels.append(label)
                coordX += 200

    elif len(listOfCards) >= 3 and len(listOfCards) <= 4:
        coordX = 200
        coordY = 10
        for card in listOfCards:
            for key in card.keys():
                photo = PhotoImage(file=key)
                label = Label(frameMain, image=photo, relief=RAISED)
                ##hold reference to an image
                label.image = photo
                label.place(x=coordX, y=coordY, width=L_WIDTH, height=L_HEIGHT)
                listOfLabels.append(label)
                coordX += 200
                if coordX > 400:
                    coordX = 200
                    coordY = 260
                
    elif len(listOfCards) > 4 and len(listOfCards) <= 8:
        coordX = 10
        coordY = 10
        for card in listOfCards:
            for key in card.keys():
                photo = PhotoImage(file=key)
                label = Label(frameMain, image=photo, relief=RAISED)
                ##hold reference to an image
                label.image = photo
                label.place(x=coordX, y=coordY, width=L_WIDTH, height=L_HEIGHT)
                listOfLabels.append(label)
                coordX += 200
                if coordX > 700:
                    coordX = 10
                    coordY = 260
                    
    else:
        coordX = 10
        coordY = 10
        for card in listOfCards:
            for key in card.keys():
                photo = PhotoImage(file=key)
                label = Label(frameMain, image=photo, relief=RAISED)
                ##hold reference to an image
                label.image = photo
                label.place(x=coordX, y=coordY, width=L_WIDTH, height=L_HEIGHT)
                listOfLabels.append(label)
                coordX += 150
                if coordX > 700:
                    coordX = 10
                    coordY = 260


def removeAllCardsDataFromFrame():
    for labelItem in listOfLabels:
        labelItem.destroy()
    ##destroy all element
    ##empty lists
    listOfLabels[:] = []

def removeWinLoseBox():
    for labelItem in listOfWinLoseBox:
        labelItem.destroy()
    listOfWinLoseBox[:] = []


def getNextCard():
    isExist = True;
    while isExist == True:
        #generate number
        num1 = game_data.getRandomNum()
        cardData = game_data.deckOfCards[num1]
        if game_data.isCardExist(cardData, listOfCards) == True:
            num1 = game_data.getRandomNum()
            cardData = game_data.deckOfCards[num1]
        else:
            isExit = False
            break
    return cardData


def setCardValue(cardData):
    for card in cardData.values():
        listValueOfCards.append(int(card))


def calculateCardsTotal():
    total = 0
    newList = sorted(listValueOfCards, reverse=True)
    for value in newList:
        if value == 0:
            if total == 10 or total == 0:
                total += 11
            elif total > 10:
                total += 1
        else:
            total += value

    return total
                
        
def cleanGameBoard():
    removeAllCardsDataFromFrame()
    removeWinLoseBox()
    listValueOfCards[:] = []
    listOfCards[:] = []
    

def showCards(frameMain, button):
    card1 = getNextCard()
    ##append card key and value
    listOfCards.append(card1)
    ##append card value
    setCardValue(card1)
    ##clean a screen
    removeAllCardsDataFromFrame()
    ##display cards
    displayRandomCards(frameMain)

    ##get total points
    if calculateCardsTotal() == 21:
        button.config(state=DISABLED)
        global_data.USER_BALANCE += global_data.WIN_PRIZE_AMOUNT
        winMessageBox(frameMain)

    elif (calculateCardsTotal() > 21):
        button.config(state=DISABLED)
        global_data.USER_BALANCE -= global_data.LOSE_PRIZE_AMOUNT
        loseMessageBox(frameMain)

    

def startGame(frameMain):

    ##clean game board
    cleanGameBoard()

    ##print shuffled list
    game_data.shuffleDeck()

    ##get random two cards and display them on a game board
    card1 = getNextCard()
    listOfCards.append(card1)
    setCardValue(card1)
    
    card2 = getNextCard()
    listOfCards.append(card2)
    setCardValue(card2)
    displayRandomCards(frameMain)
    
    ##create button
    buttonMain = Button(frameMain, bg="light grey", font="Times 10 bold", text="GET NEXT CARD",
                        command=lambda: showCards(frameMain, buttonMain))
    buttonMain.place(x=600, y=530, width=170, height=30)


    if calculateCardsTotal() == 21:
        buttonMain.config(state=DISABLED)
        global_data.USER_BALANCE += global_data.WIN_PRIZE_AMOUNT
        winMessageBox(frameMain)

    elif (calculateCardsTotal() > 21):
        buttonMain.config(state=DISABLED)
        global_data.USER_BALANCE -= global_data.LOSE_PRIZE_AMOUNT
        loseMessageBox(frameMain)


    



















    

    
