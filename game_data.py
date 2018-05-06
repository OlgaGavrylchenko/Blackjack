'''
    CIT 287 - Final Examination
    Write a program that allows a user to,
    a very limited extend, to play the game of blackjack.

    @Created by Olga Gavrylchenko, 04/25/2017
'''

import random

deckOfCards = [{'Cards/twoOfClubs.gif' : '2'},
            {'Cards/threeOfClubs.gif': '3'},
            {'Cards/fourOfClubs.gif' : '4'},
            {'Cards/fiveOfClubs.gif' : '5'},
            {'Cards/sixOfClubs.gif' : '6'},
            {'Cards/sevenOfClubs.gif' : '7'},
            {'Cards/eightOfClubs.gif' : '8'},
            {'Cards/nineOfClubs.gif' : '9'},
            {'Cards/tenOfClubs.gif' : '10'},
            {'Cards/jackOfClubs.gif' : '10'},
            {'Cards/queenOfClubs.gif' : '10'},
            {'Cards/kingOfClubs.gif' : '10'},
            {'Cards/aceOfClubs.gif' : '0'},
            {'Cards/twoOfDiamonds.gif' : '2'},
            {'Cards/threeOfDiamonds.gif': '3'},
            {'Cards/fourOfDiamonds.gif' : '4'},
            {'Cards/fiveOfDiamonds.gif' : '5'},
            {'Cards/sixOfDiamonds.gif' : '6'},
            {'Cards/sevenOfDiamonds.gif' : '7'},
            {'Cards/eightOfDiamonds.gif' : '8'},
            {'Cards/nineOfDiamonds.gif' : '9'},
            {'Cards/tenOfDiamonds.gif' : '10'},
            {'Cards/jackOfDiamonds.gif' : '10'},
            {'Cards/queenOfDiamonds.gif' : '10'},
            {'Cards/kingOfDiamonds.gif' : '10'},
            {'Cards/aceOfDiamonds.gif' : '0'},
            {'Cards/twoOfHearts.gif' : '2'},
            {'Cards/threeOfHearts.gif': '3'},
            {'Cards/fourOfHearts.gif' : '4'},
            {'Cards/fiveOfHearts.gif' : '5'},
            {'Cards/sixOfHearts.gif' : '6'},
            {'Cards/sevenOfHearts.gif' : '7'},
            {'Cards/eightOfHearts.gif' : '8'},
            {'Cards/nineOfHearts.gif' : '9'},
            {'Cards/tenOfHearts.gif' : '10'},
            {'Cards/jackOfHearts.gif' : '10'},
            {'Cards/queenOfHearts.gif' : '10'},
            {'Cards/kingOfHearts.gif' : '10'},
            {'Cards/aceOfHearts.gif' : '0'},
            {'Cards/twoOfSpades.gif' : '2'},
            {'Cards/threeOfSpades.gif': '3'},
            {'Cards/fourOfSpades.gif' : '4'},
            {'Cards/fiveOfSpades.gif' : '5'},
            {'Cards/sixOfSpades.gif' : '6'},
            {'Cards/sevenOfSpades.gif' : '7'},
            {'Cards/eightOfSpades.gif' : '8'},
            {'Cards/nineOfSpades.gif' : '9'},
            {'Cards/tenOfSpades.gif' : '10'},
            {'Cards/jackOfSpades.gif' : '10'},
            {'Cards/queenOfSpades.gif' : '10'},
            {'Cards/kingOfSpades.gif' : '10'},
            {'Cards/aceOfSpades.gif' : '0'}]



def shuffleDeck():
    random.shuffle(deckOfCards)


def getRandomNum():
    return random.randint(0, 51)

##compare two dicnionaries
def isCardExist(newCard, usedDeckOfCards):
    isExist = False
    if newCard in usedDeckOfCards:
        isExist = True

    return isExist


















