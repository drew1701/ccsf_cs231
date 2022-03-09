#!/usr/local/bin/python3
import random

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
deck = [ (name + ' of ' + suit, suits.index(suit) ) for name in names for suit in suits ]
bonus, scoreA, scoreB = 0, 0, 0

# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:

 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 cardA, cardB = deck.pop(), deck.pop()
 if cardA[1] == cardB[1]:
  bonus += scoreA
  outcome = 'ties'
 elif cardA[1] > cardB[1]:
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
  scoreA += 1 + bonus
  bonus = 0
 outcome = 'is beaten by'

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
 print ( '{:55.55}  ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )

