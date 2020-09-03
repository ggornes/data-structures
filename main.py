from linked_lists import SLinkedList
from d_linked_list import DLinkedList
from card import Card

players = []

# def deal_cards(deck, players):






if __name__ =='__main__':
    card_deck = SLinkedList()

    card_deck2 = DLinkedList()

    p1_hand = DLinkedList()
    p2_hand = DLinkedList()

    valid_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # valid_suit = ['D', 'C', 'H', 'S']
    valid_suit = ['D']

    for s in valid_suit:
        for r in valid_rank:
            card_deck.add(Card(r, s))

            card_deck2.add(Card(r, s))

    """ print all deck """
    card_deck.display()

    """ pretty print """
    # card_deck.pdisplay()

    """ print by groups """
    card_deck.gdisplay()

    print("Card deck size: ")
    print(card_deck.size())


    selected_card = Card('8', 'D')
    selected_card.pprint()

    card_deck.search(selected_card)

    card_deck.delete(selected_card)

    card_deck.gdisplay()




    # card_deck2.display()


