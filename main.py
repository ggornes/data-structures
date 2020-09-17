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
    print("1. Add nodes to the list")
    for s in valid_suit:
        for r in valid_rank:
            card_deck.insert_at_start(Card(r, s))


    """ 2. Delete a node (a card) from the list (deck) """
    print("2. Delete a selected card from the list")
    print("Selected Card: ")
    selected_card = Card('A', 'D')
    selected_card.pprint()

    card_deck.delete_element(selected_card)

    """ 3. Display all data in the list backwards """
    print("3. Display the list backwards")
    # card_deck.reverse_list()
    for c in card_deck:
        c.data.pprint()

    """ 4. Find a node (card) on the list (deck) """
    print("4. Find a card on the list")
    card = Card('5', 'D')
    print("Searching: ")
    card.pprint()
    search = card_deck.search(card)

