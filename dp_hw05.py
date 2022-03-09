#!/usr/bin/env python3
# above: Fixed shebang to be more portable.
import random

# below: Fixed long lines in comment blocks. (multiple)
# War, the card game of chance where 26 battles take place between rival
# armies. The higher card wins each battle. Ties accumulate a bonus to
# be won at the next battle. For each battle, output the number of
# cards left, the two cards drawn, and the win totals. If a battle is a
# tie, its value is accrued towards the next battle that is won.

# Build deck list, containing tuples of the names and values of each
# card. The order of the names list determines the cards' values.
# The deck is 52 tuples like this: ('Jack of Diamonds', 11).
# below: Broke long statements into separate lines per PEP8. (multiple)
names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
# below: Fixed index to use name not suit, added 2 so values match card.
deck = [(name + ' of ' + suit, names.index(name) + 2)
        for name in names for suit in suits]
# below: Fixed variable names to use snake_case.(multiple)
bonus, score_a, score_b = 0, 0, 0

# below: Added random to shuffle deck so each game is unique.
deck = (random.sample(deck, len(deck)))

# As long as there are cards left in the deck, draw pairs for each
# battle. While loop is safe as long as the only thing that happens
# to deck is .pop().
# below: Fixed indent to 4 spaces, as per PEP8. (multiple)
while deck:

    # Compare a pair of cards' values, tally scores and adjust bonus.
    # There are three possible cases; in case of a win the bonus is
    # paid out, otherwise it rises.
    card_a, card_b = deck.pop(), deck.pop()

    if card_a[1] == card_b[1]:
        # below: Fixed by adding 1 to bonus, not score_a.
        bonus += 1
        outcome = 'ties'
    elif card_a[1] > card_b[1]:
        score_a += 1 + bonus
        bonus = 0
        outcome = 'beats'
    else:
        score_b += 1 + bonus
        bonus = 0
        # below: Fixed line that wasn't indented as part of else clause.
        outcome = 'is beaten by'

    # display the outcome of each battle, current winnings,
    # and how much is left to be won.
    event = "The {} {} the {}!".format(card_a[0], outcome, card_b[0])
    print('{:55.55}  ${} to ${}, ${} left.'.format(
        event, score_a, score_b, int(len(deck)/2)))
