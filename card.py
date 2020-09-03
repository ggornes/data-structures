class Card:

    # self.suit = '♥♦♣♠'[suit_dict.get(suit)]  # 1,2,3,4 = ♥♦♣♠

    def __init__(self, rank=None, suit=None):
        valid_ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        valid_suits = ('D', 'C', 'H', 'S')
        # suit_dict = {'H': 0, 'D': 1, 'C': 2, 'S': 3}

        if rank in valid_ranks and suit in valid_suits:
            # print("Valid card")
            self.rank = rank
            self.suit = suit
        else:
            # print("Invalid card")
            # Joker ?
            # self.rank = None
            # self.suit = None
            raise Exception("Card does not exists")

    def print(self):
        suit_dict = {'H': 0, 'D': 1, 'C': 2, 'S': 3}
        print(str(self.rank) + '♥♦♣♠'[suit_dict.get(self.suit)])

    def pprint(self):
        suit_dict = {'H': 0, 'D': 1, 'C': 2, 'S': 3}
        print('┌───────┐')
        print(f'| {self.rank:<2}    |')
        print('|       |')
        print(f'|   '+'♥♦♣♠'[suit_dict.get(self.suit)]+'   |')
        print('|       |')
        print(f'|    {self.rank:>2} |')
        print('└───────┘')

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
