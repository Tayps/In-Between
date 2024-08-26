import random as rand
import numpy as np
import inquirer
from collections import Counter
import pandas as pd

# Create deck and assign card Values
deck = []
cardValue = {}
gameDeck = []

handData = {'simID':0,
            'handID':0,
            'deckUsed':0,
            'shuffleCount':0,
            'topCard':0,
            'bottomCard':0,
            'drawCard':0,
            'spread':0,
            'winOdds':0,
            'loseOdds':0,
            'dblOdds':0,
            'ev':0,
            'outcome':0,
            'winningOuts':0,
            'doubleOuts':0,
            'cardsRemaining':0}

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

# Create function to shuffle a set number of decks and create game deck.
def shuffle(deckCount):
    global gameDeck
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
    
    global handData
    
    winningCards = []

    doubleCards = []

    currentDeck = gameDeck.copy()
    totalCardsRemaining = len(currentDeck)
    handData['cardsRemaining'] = totalCardsRemaining
    for i in range(totalCardsRemaining):
        currentDeck[i] = cardValue[currentDeck[i]] #replace deck elements with their value
        total = dict(Counter(currentDeck)) #  dic with count of cards left for each value

    smallCard = min(cardValue[outer[0]],cardValue[outer[1]])
    bigCard = max(cardValue[outer[0]],cardValue[outer[1]])
    handData['spread'] = bigCard - smallCard - 1
    for i in range(smallCard+1, bigCard ):
        winningCards.append(i) # gives list of value that will win

    for j in winningCards:      # For each winning value,
        try:
            handData['winningOuts'] += total[j] # retrieve the number of cards left and sum up.
        except:
            handData['winningOuts'] += 0 
    doubleCards.extend([cardValue[outer[0]], cardValue[outer[1]]]) #gives list of value that dbl
    for k in doubleCards:      #for each double value
        try:
            handData['doubleOuts'] += total[k] # retrieve the number of cards left and sum up 
        except:
            handData['doubleOuts'] += 0
    handData['winOdds'] = round(handData['winningOuts']/totalCardsRemaining,2)
    handData['dblOdds'] = round(handData['doubleOuts']/totalCardsRemaining,2)
    handData['loseOdds'] = round(1 - (handData['winOdds'] + handData['dblOdds']),2)

    handData['ev'] = round((1*handData['winOdds']) + (-1*handData['loseOdds']) + (-2*handData['dblOdds']),2)


# Simulation Inputs

simID = input('Enter Simulation number \n')
print('\n')
deckCount = input('How many decks in to be used in simulation? \n')
print('\n')
handCount = input('How many hands to simulate? \n')
print('\n')

# Run Simulation

log = []
shuffleCount = 0

for hands in range(1,int(handCount)+1):
    if len(gameDeck) <3:
        shuffle(deckCount)
        shuffleCount += 1
    else:
        pass
    # Log Metadata
    handData['simID'] = simID
    handData['handID'] = hands
    handData['deckUsed'] = deckCount
    handData['shuffleCount'] = shuffleCount
    
    # Deal Outer Cards
    outer = []
    outer.extend(dealOuter())
    outer.sort()
    handData['topCard'] = outer[0]
    handData['bottomCard'] = outer[1]
    
    # If Auto Tiang
    if checkAutoTiang(outer):
        handData['outcome'] = 'Auto Tiang'
        handData['drawCard'] = ''
        log.append(list(handData.values()))
        # print(outer[0],outer[1])
        # print("Auto Tiang Bitch!", end="\n\n")
        continue
        
    # No Auto Tiang, Continue to draw
    else:
        calEV(outer)
        
        # print("Cards are " + str(outer[0]) + " and " + str(outer[1]))
        # print("EV = " + str(ev) + " (Play on higher EV)", end="\n\n")
        # print("Player's move")
        # print("1) Hit")
        # print("2) Pass", end="\n\n")
        # move = input()
        # print("\n")
        # if move == '2':
        #     continue
        # else:
        inner = []
        inner.extend(dealInner())
        # print("You drew " + str(inner[0]), end="\n\n")
        handData['drawCard'] = inner[0]
        handData['outcome'] = compareValue(outer,inner)
        # print("cards left: " + str(len(gameDeck)))
        # continue

        print(handData)
        
        # Log the outputs of the hand to Log list.
        log.append(list(handData.values()))
        # print(handData)
        
        #Rest the handData
        for keys in handData:
            handData[keys] = 0

        
# End of Simulation
df = pd.DataFrame(log,columns = handData.keys())
print('End of Simulation')
print(df)


# tlist = []
# hand = {}

# def oneHand():
#     global hand
#     hand["run"] = rand.randint(1,9)
#     hand["EV"] = rand.randint(1,9) 
#     return hand

# for i in range(1,1000):
#     tlist.append(list(oneHand().values()))

# df = pd.DataFrame(tlist,columns= hand.keys())
# print(df)