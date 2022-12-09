"""
main.py BLACKJACK
"""
import random
import time
import os
from hand import Hand
from load import loading

# pylint ignore constants
# pylint: disable=C0103

card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
clear = lambda: os.system('cls')
# shuffle card_deck
random.shuffle(card_deck)
i = 0
clear()
loading(0.1, 2, "loading")
clear()
print("\tThe game Blackjack" , end="\n"*3)
time.sleep(1)
clear()
user_won_in_start = False
banker_think_time = 1 #in seconds
init_card_1 = card_deck.pop()
init_card_2 = card_deck.pop()

hand1 = Hand(init_card_1, init_card_2)
print(f"you took two cards: {init_card_1} and {init_card_2}")
while True:
    if hand1.is_bust():
        #no potential winning options
        break
    elif hand1.is_win():
        if i == 0:
            user_won_in_start = True
        break
    else:
        hand1.options_print()
        time.sleep(0.5)
        while True:
            inp = input("do you want take a card from the card deck? (y/n): ")
            if inp.lower() == "y":
                take_card = True
                break
            elif inp.lower() == "n":
                take_card = False
                break
            else:
                print("the input wasn\'t valid, please try again...")
        if take_card:
            card_taken = card_deck.pop()
            hand1.add(card_taken)
            clear()
            print(f"you took {card_taken} from the card deck")
        else:
            clear()
            break
    i += 1

# player ended the game
if hand1.is_win():
    if user_won_in_start:
        print("congratulations, you won just by picking two cards!")
    else:
        print("congratulations, you won!")
elif hand1.is_bust():
    print("you lost")
else:
    # it is dealer's turn when user doesn't want to take any more cards
    init_card_1 = card_deck.pop()
    init_card_2 = card_deck.pop()

    hand2 = Hand(init_card_1, init_card_2)
    print("dealer\'s turn:", end="\n"*3)
    time.sleep(0.5)
    print(f"dealer took {init_card_1} and {init_card_2}")
    while True:
        options = hand2.options()
        if hand2.is_bust():
            #no potential winning options
            break
        elif hand2.is_win():
            break
        if max(options) < 17:
            take_card = True
        else:
            take_card = False
        #thinking delay to banker
        time.sleep(banker_think_time)
        if take_card:
            card_taken = card_deck.pop()
            hand2.add(card_taken)
            print(f"banker took {card_taken} from the card deck")
        else:
            break
    time.sleep(0.5)

    if hand2.is_bust():
        print("dealer busted, which means that you won! Congratulations!")
    else:
        if hand1.total() > hand2.total():
            print(f"you won! Your score: {hand1.total()}, and dealer\'s score: {hand2.total()}")
        elif hand1.total() < hand2.total():
            print(f"you lost! Your score: {hand1.total()}, and dealer\'s score: {hand2.total()}")
        elif hand1.total() == hand2.total():
            print(f"no one won, it\'s a tie! Your score: {hand1.total()}, and dealer\'s score: {hand2.total()}")
