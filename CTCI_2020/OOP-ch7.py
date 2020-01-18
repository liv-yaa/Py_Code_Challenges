# OOP-ch7.py

""" 
Good Design Patterns - APPROACH:

	1. Imagine real-life problems

	2. Handle Ambiguity: Ask questions! what, where, how, why

	3. Define Core objects
		- ex. User, Photos

	4. Define one-to-one or many-to-many relationships
		- ex. User-User, User-Photos

	5. Define inheritance
		- ex. Admin inherits from User

	6. Define 
		- ex. a Family is made up of many People

	7. Investigate actions
		- these will be the methods
		- might depend on relationships
		- Other actions might depend on other objects' actions (wait...)

	8. Define 'singleton' globals: 
		those objects which only have one global instance

		- ex. one and only one Restaurant made from the class blueprint

	9. Define 'factory method' classes:
		When you want to create many instances of one class

		Here, subclasses decide which class to instantiate

			def create_game(GameType: type -> CardGame):
				if type == GameType.Poker:
					return PokerGame() 
				elif type == GameType.Blackjack:
					return BlackjackGame()

		- ex. many Tables made from the class blueprint


"""

import random

# 7.1
class Card:
	""" Singleton class for a Card """

	def __init__(self, value, suit):
		""" Has attributes value and suit, when we instantiate a new card. """
		self.value = value
		self.suit = suit

	def __repr__(self):
		""" String representation of Card """
		return f'{self.suit} of {self.value}'

class DeckOfCards:
	""" Singleton class for a Deck of Cards: Design the data structures for a generic deck of cards
	>>> doc = DeckOfCards()
	[1 of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, 11 of Spades, 12 of Spades, 13 of Spades, 1 of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, 11 of Clubs, 12 of Clubs, 13 of Clubs, 1 of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, 11 of Diamonds, 12 of Diamonds, 13 of Diamonds, 1 of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, 11 of Hearts, 12 of Hearts, 13 of Hearts]

	"""

	def __init__(self):
		self.deck = []
		self.build()
		print(self.deck)

	def __repr__(self):
		""" String representation of DeckOfCards """
		for c in self.deck:
			print(c)

	def build(self):
		""" Builds up the deck """
		for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
			for v in range(1, 14):
				self.deck.append(Card(s, v))

	def shuffle(self):
		""" Shuffles the cards randomly """
		for i in range(len(self.deck)):
			o = random.randint(i)
			self.deck[i], self.deck[o] = self.deck[o], self.deck[i]

	def draw_card(self):		
		""" Pops off the top card """
		return self.deck.pop()


class Blackjack(DeckOfCards):
	""" For a game of Blackjack, subclass the data structure of Deck of Cards to implement blackjack. 
	copied https://github.com/w-hat/ctci-solutions/blob/master/ch-07-object-oriented-design/01-deck-of-cards.py
	>>> bj = Blackjack()
	[1 of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, 11 of Spades, 12 of Spades, 13 of Spades, 1 of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, 11 of Clubs, 12 of Clubs, 13 of Clubs, 1 of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, 11 of Diamonds, 12 of Diamonds, 13 of Diamonds, 1 of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, 11 of Hearts, 12 of Hearts, 13 of Hearts]
	>>> bj.give_value()
	"""
	trans = {''}
	def give_value(self):
		""" Gives cards a respective value for this game """
		v, aces = 0, 0
		for card in self.deck:
			print(card.value)
			v += min(card.value, 10) # Doesnt work cuz we have a dict instead of vals
			aces += 1
			print(v, aces)

		while v <= 11:
			if aces:
				v += 10
				aces -= 1
		return v





if __name__ == "__main__":
	import doctest
	doctest.testmod()












	









	









	









	









	









	









	









	









	









	









	









	




