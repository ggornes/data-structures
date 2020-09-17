import unittest
from card import Card

class TestCardComparison(unittest.TestCase):

    def test_card_comparison(self):
        self.assertEqual(Card('A', 'C'), Card('A', 'C'))
        self.assertNotEqual(Card('A', 'C'), Card('A', 'H'))
