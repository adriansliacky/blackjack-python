"""
The class Hand
"""
from resolver import resolve

class Hand:
    """
    Hand methods and operations
    """
    def __init__(self, card1, card2):
        self.cards = [card1, card2]

    def options(self):
        """
        which possible moves can i make?
        """
        options_lst = []
        sum_cards = sum(map(resolve, self.cards)) # with ACE
        options_lst.append(sum_cards)
        # no need to worry about 2 or more occurences of Ace in hand - sum of both two will be
        # more than 22, and it gets out of the way by the final filtration anyway

        if 1 in self.cards:
            options_lst.append(sum_cards+10)

        #final filter
        filtered = filter(lambda score: score <= 21, options_lst)
        return list(filtered)


    def options_print(self):
        """
        print possible moves
        """

        str_card_deck = [str(int) for int in self.cards]
        card_deck = " | ".join(str_card_deck)
        possible_options = [str(int) for int in self.options()]
        possible_options_filtered = []
        for i in possible_options:
            if i not in possible_options_filtered:
                possible_options_filtered.append(i)
        str_possible_options_filtered = " or ".join(possible_options_filtered)


        print(f"Your cards on hand are:\n{card_deck} \nand hand total(s): \n{str_possible_options_filtered}")


    def add(self, card):
        """
        adds a card to the hand
        """
        self.cards.append(card)

    def is_win(self):
        """
        returns T/F
        returns True if user won
        returns False if user did not win
        """
        return 21 in self.options()

    def is_bust(self):
        """
        did user bust?
        """
        return not self.options()

    def total(self):
        """
        what is the highest option in your hand?
        """
        options = self.options()
        if not options:
            return options
        else:
            return max(options)
