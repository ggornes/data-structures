from d_linked_list import DLinkedList
from card import Card

players = []

# def deal_cards(deck, players):


if __name__ =='__main__':

    card_deck = DLinkedList()

    valid_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # valid_rank = ['A']
    # valid_suit = ['D', 'C', 'H', 'S']
    valid_suit = ['D']



    """ 1. Add node to the list, in this case, all cards """
    for s in valid_suit:
        for r in valid_rank:
            card_deck.insert_at_start(Card(r, s))


    """ 2. Delete a node (a card) from the list (deck) """
    selected_card = Card('A', 'D')

    card_deck.delete_element(selected_card)

    """ 3. Display all data in the list backwards """
    # card_deck.reverse_list()
    for c in card_deck:
        c.data.pprint()

    """ 4. Find a node (card) on the list (deck) """