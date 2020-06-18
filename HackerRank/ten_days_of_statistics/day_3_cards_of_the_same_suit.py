# Task
# You draw 2 cards from a standard 52 -card deck without replacing them.
# What is the probability that both cards are of the same suit?

if __name__ == '__main__':
    cards = 52
    suits = 4
    cards_per_suits = 52/4

    print(cards_per_suits)

    #first draw

    cards_after_first_draw = 51
    cards_of_suit_of_draw_chosen = (52/4) - 1

    print(cards_per_suits)

    #second draw - probability of a card will be of the same suit -

    p_two_same_suit = cards_of_suit_of_draw_chosen / cards_after_first_draw

    print(p_two_same_suit)