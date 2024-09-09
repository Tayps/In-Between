# In-Between

In this python project, we will build an In-between game simulator with features to calculate the relevant statistics of each hand.
We will then run simulations of multiple hands to study and develop an optimal strategy in playing this game.

---
## Document Contents

* [Game Rules & How to play](#gameRules)
* [Code Walk Through](#codeWalkThrough) 

---
## Game rules & How to play <a name = "gameRules"></a>

In Between is a popular card game played in Singapore and Malaysia among friends and families during the lunar new year festivities.

The game is played with one or more deck(s) of standard 52-card poker cards. The card values range from Ace (smallest) to King (largest).
The goal is to draw a card that is in-between (exclusive) the 2 face-up cards.

**Game Start:**  
> At the start of the game, each player contributes in a pre-determined amount of money(the blinds) into a pot .
> 
> The amount of money in the pot at the start of each player's hand, is the maximum amount of money that player can win in that hand.
> 
> One (or more) deck(s) of cards is then shuffled.  

**Player's Turn:**
> At the beginning of a turn, 2 cards are dealt face up from the deck.
> 
> The player decides if he would like to play the hand.  

**Player decides to play:**   
>Step 1: If the player decides to play, he can bet any amount smaller than or equals to the pot value.
>
>Step 2: A card is then dealt face up.
>
>>**Winning:** If the card dealt is in between the 2 face up cards (exclusive), the player wins his bet amount from the pot.
>
>>**Losing:** If the card dealt is out of of the 2 face up cards, the player loses the wager amount and contributes it into the pot.
>
>>**Losing Double:** If the dealt card is the same as either of the 2 face up cards, the player loses double the wager amount and contributes it into the pot.  
>
>The player collects his winning from the pot or pays his losses into the pot and his turn ends.  

**Player decides not to play:**  
>If the player decides not to play, no wagers are made and his turn ends.  

**End of turn:**  
>All face up cards are burnt and the round repeats with the next player (Step 2)  
>

**2 identical face up cards:**  
>If 2 identical face-up cards are dealt at the start of a player's turn, he automatically loses and pays double the blinds into the pot.  

**Empty pot:**
>When the pot is empty (player wagers the pot amount and wins). All player contributes another round of blinds into the pot and the game continues with the next player.  

---
## Code Walk-Through <a name = "codeWalkThrough"></a>

**ibBetween.ipynb** : python notebook for experiementing and code testing in blocks.  
**inBetween.py**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: python script for playing the game.  
**ibSim.py**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: python script for simulating a set number of hands.  
