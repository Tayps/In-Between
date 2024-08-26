import random as rand
import numpy as np
import inquirer
from collections import Counter

# Create deck and assign card Values
deck = []
cardValue = {}

evStats = {'winOdds':0, 
           'dblOdds':0,
           'lssOdds':0,
           'ev':0,
           'winningOuts':0,
           'doubleOuts':0}

for i in range(1,14):
    val = i
    i = str(i)
    if i == '1':
        i = 'Ace'
    elif i == '11':
        i = 'Jack'
    elif i == '12':
        i = 'Queen'
    elif i == '13':
        i = 'King'
    else:
        i=i
    for j in ['\U00002665', '\U00002663', '\U00002666', '\U00002660']:
        deck.append(i + ' ' + j)
        cardValue[i + ' ' + j] = val

gameDeck = []

# Create function to shuffle a set number of decks and create game deck.
def shuffle(deckCount):
    global gameDeck
    gameDeck.clear()
    gameDeck = list(np.repeat(deck,deckCount))
    rand.shuffle(gameDeck)

# Function to deal Outer Cards
def dealOuter():
    tableCards = []
    tableCards.append(gameDeck.pop())
    tableCards.append(gameDeck.pop())
    tableCards.sort()
    return tableCards

# Function to deal Inner Card
def dealInner():
    innerCard = []
    innerCard.append(gameDeck.pop())
    return innerCard


# Function to check AutoTiang
def checkAutoTiang(table):
    if cardValue[table[0]] == cardValue[table[1]]:
        return True
    else:
        pass

# Function to check if Win
def compareValue(table, player):
    if cardValue[player[0]] < max(cardValue[table[0]],cardValue[table[1]]) and cardValue[player[0]] > min(cardValue[table[0]],cardValue[table[1]]):
        return 'Win'
    elif cardValue[player[0]] == cardValue[table[0]] or cardValue[player[0]] == cardValue[table[1]]:
        return 'Pay Double'
    else: 
        return 'Lose'

# Function to calculate expected value given outer cards
def calEV(outer):

    # global winOdds
    # global dblOdds
    # global lssOdds
    # global ev
    
    global evStats
    
    winningCards = []

    doubleCards = []

    currentDeck = gameDeck.copy()
    totalCardsRemaining = len(currentDeck)
    for i in range(totalCardsRemaining):
        currentDeck[i] = cardValue[currentDeck[i]] #replace deck elements with their value
        total = dict(Counter(currentDeck)) #  dic with count of cards left for each value

    smallCard = min(cardValue[outer[0]],cardValue[outer[1]])
    bigCard = max(cardValue[outer[0]],cardValue[outer[1]])
    for i in range(smallCard+1, bigCard ):
        winningCards.append(i) # gives list of value that will win

    for j in winningCards:      # For each winning value,
        try:
            evStats['winningOuts'] += total[j] # retrieve the number of cards left and sum up.
        except:
            evStats['winningOuts'] += 0 
    doubleCards.extend([cardValue[outer[0]], cardValue[outer[1]]]) #gives list of value that dbl
    for k in doubleCards:      #for each double value
        try:
            evStats['doubleOuts'] += total[k] # retrieve the number of cards left and sum up 
        except:
            evStats['doubleOuts'] += 0
    evStats['winOdds'] = round(evStats['winningOuts']/totalCardsRemaining,2)
    evStats['dblOdds'] = round(evStats['doubleOuts']/totalCardsRemaining,2)
    evStats['lssOdds'] = round(1 - (evStats['winOdds'] + evStats['dblOdds']),2)

    evStats['ev'] = round((1*evStats['winOdds']) + (-1*evStats['lssOdds']) + (-2*evStats['dblOdds']),2)
    
    # return winOdds, dblOdds, lssOdds, ev


# print("How many decks?", end="\n\n")
# deckCount = input("How many decks? \n\n")
# print("\n")
# shuffle(deckCount)
# endGame = False

while True:
    if len(gameDeck) < 3:
        deckCount = input("How many decks? \n\n")
        print("\n")
        shuffle(deckCount)
    else:
        pass
    print("New Hand? [y/n]", end="\n\n")
    start = input()
    print("\n")
    if start == 'y':
        for keys in evStats:
            evStats[keys] = 0
        outer = []
        outer.extend(dealOuter())
        if checkAutoTiang(outer):
            print(outer[0],outer[1])
            print("Auto Tiang Bitch!", end="\n\n")
            continue
        else:
            calEV(outer)
            print("Cards are " + str(outer[0]) + " and " + str(outer[1]))
            print("EV = " + str(evStats['ev']) + " (Play on higher EV)", end="\n\n")
            print("Player's move")
            print("1) Hit")
            print("2) Pass", end="\n\n")
            move = input()
            print("\n")
            if move == '2':
                continue
            else:
                inner = []
                inner.extend(dealInner())
                print("You drew " + str(inner[0]), end="\n\n")
                print(compareValue(outer,inner))
                print("cards left: " + str(len(gameDeck)))
                continue
    else:
        break
        
            