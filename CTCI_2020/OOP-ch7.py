# OOP-ch7.py

""" key terms review:
"""
class ThreeMethodTypes:
	""" 1. INSTANCE , CLASS, and STATIC METHODS

	>>> tmt = ThreeMethodTypes()
	
	>>> print('class name', tmt.name)
	class name Raggety

	>>> tmt.instance_method()
	>>> print('instance name', tmt.lastname)
	instance name LastInTheClass

	>>> print(tmt.factorial(4))
	24

	"""
	# Define a class attribute:
	name = 'Raggety'

	def instance_method(self):
		# Creates an instance attriute through keyword 'self'
		self.lastname = 'LastInTheClass'
		# print(self.lastname)

	@classmethod
	def class_method(cls):
		# Accesses a class attribute through keyword cls
		cls.name = 'Classy'
		print(cls.name)

	@staticmethod # * Does not take 'cls' or 'self'!
	def factorial(number):
		if number == 0:
			return 1
		else:
			return number * ThreeMethodTypes.factorial(number - 1)



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
	# >>> bj = Blackjack()
	[1 of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, 11 of Spades, 12 of Spades, 13 of Spades, 1 of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, 11 of Clubs, 12 of Clubs, 13 of Clubs, 1 of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, 11 of Diamonds, 12 of Diamonds, 13 of Diamonds, 1 of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, 11 of Hearts, 12 of Hearts, 13 of Hearts]
	# >>> bj.give_value()
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


# 7.2 Design a Call Center
class Employee:
	""" 
	Base class representing one employee
	>>> e = Employee('respondent', 1)
	>>> e = Employee('manager', 2)
	>>> e = Employee('director', 3)
	"""

	def __init__(self, empType, empNumber):
		self.empType = empType
		self.empNumber = empNumber

	def __repr__(self):
		return str(self.empType) + str(self.empNumber)

class Company:
	""" Assigns a call to the first available employee (there are 3 types)
		# >>> c = Company(10) 
		# >>> c.dispatchCall()
	"""
	ETYPES = ['respondent', 'manager', 'director']

	def __init__(self, size):
		self.all_employees = {t : [] for t in self.ETYPES}
		self.size = size
		self.build(size=self.size)

	def build(self, size):
		# Randomly build up a dict of employees, given company size
		for i in range(size):
			# Get a random type of employee
			rand_type = self.ETYPES[random.randint(0, 2)]

			if rand_type != -1:
				# Create an employee and add it to the company dictionary
				self.all_employees.get(rand_type, []).append(Employee(rand_type, i))

	def dispatchCall(self):
		""" Assigns a call to the first available employee (there are 3 types) 		
		"""
		# self.all_employees['respondent'] = []
		e = self.all_employees.get('respondent')
		m = self.all_employees.get('manager')
		r = self.all_employees.get('director')

		if e != [] and e != -1:
			# First, get the respondents
			return e[0]

		elif m != [] and m != -1:
			# If respondent does not exist, get the managers
			return m[0]
		elif r != [] and r != -1:
			# If neither respondents nor managers exist, get the directors
			return r[0]
		else:
			return 'No one exists'


# Note, this solution uses a Queue of Employee objects, who each have a manager.
# The call goes up the chain of command! https://github.com/w-hat/ctci-solutions/blob/master/ch-07-object-oriented-design/02-call-center.py

class CallCenter2:
	def __init__(self, respondents, managers, director):
		self.respondents = respondents
		self.managers = managers
		self.director = director
		
		self.respondent_queue = []
		self.call_queue = []

		for respondent in respondents:
			respondent.callcenter = self
			if not respondent.call:
				self.respondent_queue.append(respondent)

	def __repr__(self):
		r = '\n'.join([str(x) for x in self.respondents])
		m = '\n'.join([str(x) for x in self.managers])
		d = str(self.director)
		return 
		f"""
			{r}

			{m}

			{d}

			{self.respondent_queue}
		"""
	def route_respondent(self, respondent):
		if len(self.call_queue):
			respondent.take_call(self.call_queue.pop(0))
		else:
			self.respondent_queue.append(respondent)

	def route_call(self, call):
		if len(self.respondent_queue):
			self.respondent_queue.pop(0).take_call(call)

		else:
			self.call_queue.append(call)

class Call2:
	def __init__(self, issue):
		self.issue = issue
		self.employee = None

	def resolve(self, handled):
		if handled:
			self.issue = None
		self.employee.finish_call(handled)

	def apologize(self):
		self.employee = None

class Employee2:
	def __init__(self, name, manager):
		self.name, self.manager = name, manager
		self.call = None

	def __repr__(self):
		return 'Employee name: ' + str(self.name)

	def take_call(self, call):
		if self.call:
			self.escalate(call)
		else:
			self.call = call
			self.call.employee = self

	def escalate(self, call):
		if self.manager:
			self.manager.take_call(call)
		else:
			call.apologize()

	def finish_call(self, handled=True):
		if not handled:
			if self.manager:
				self.manager.take_call(self.call)
			else:
				call.apologize()
		self.call = None

class Respondent2(Employee2):
	def __repr__(self):
		return 'ERespondent: ' + str(self.name) + ' (m: ' + str(self.manager.name) + ') '

	def finish_call(self, handled=True):
		super(Respondent2, self).finish_call(handled)
		self.callcenter.route_respondent(self)

class Manager2(Employee2):
	def __repr__(self):
		return 'EManager: ' + str(self.name) + ' (man: ' + str(self.manager.name) + ') '


class Director2(Employee2):
	def __repr__(self):
		return 'EDirector: ' + str(self.name)

	def __init__(self, name):
		super(Director2, self).__init__(name, None)


# import unittest
# class Test(unittest.TestCase):
#   def test_call_center(self):
#     lashaun = Director2("Lashaun")
#     juan = Manager2("Juan", lashaun)
#     sally = Manager2("Sally", lashaun)
#     boris = Respondent2("Boris", juan)
#     sam = Respondent2("Sam", juan)
#     jordan = Respondent2("Jordan", sally)
#     casey = Respondent2("Casey", sally)
#     center = CallCenter2([boris, sam, jordan, casey], [juan, sally], lashaun)
#     print(center)
#     # print(center.director) # Lashaun

#     # Take some calls:
#     call1 = Call2("The toilet")
#     call2 = Call2("The webpage")
#     call3 = Call2("The email")
#     call4 = Call2("The lizard")
#     call5 = Call2("The cloudy weather")
#     call6 = Call2("The noise")
#     self.assertEqual(len(center.respondent_queue), 4)
#     # print(center.respondent_queue)
#     center.route_call(call1)
#     center.route_call(call2)
#     self.assertEqual(len(center.respondent_queue), 2)
#     center.route_call(call3)
#     center.route_call(call4)
#     center.route_call(call5)
#     center.route_call(call6)
#     print(center.respondent_queue)

#     self.assertEqual(center.call_queue, [call5, call6])
#     # call1.resolve(True)
#     # self.assertEqual(call1.issue, None)
#     # self.assertEqual(center.call_queue, [call6])
#     # self.assertEqual(sally.call, None)
#     # self.assertEqual(lashaun.call, None)
#     # call4.resolve(False)
#     # self.assertEqual(sally.call, call4)
#     # call4.resolve(False)
#     # self.assertEqual(sally.call, None)
#     # self.assertEqual(lashaun.call, call4)
#     # call4.resolve(True)
#     # self.assertEqual(lashaun.call, None)
#     # call6.resolve(True)
#     # self.assertEqual(center.respondent_queue, [casey])




class Jukebox:
	""" 
	Class represenging a Jukebox. Stores a queue of songs. Takes titles to play and plays them.
	>>> song1 = Song("Just Dance", "8598742398723498")
	>>> song2 = Song("When You Wish Upon a Beard", "9879834759827209384")
	>>> j = Jukebox([song1, song2])
	>>> print(j)
	{'Just Dance': Song Object Just Dance{ by: 8598742398723498 } played: False, 'When You Wish Upon a Beard': Song Object When You Wish Upon a Beard{ by: 9879834759827209384 } played: False}
	>>> song3 = Song('Pepperoni', '35')
	>>> j.add_to_dict(song3)
	>>> print(j)
	{'Just Dance': Song Object Just Dance{ by: 8598742398723498 } played: False, 'When You Wish Upon a Beard': Song Object When You Wish Upon a Beard{ by: 9879834759827209384 } played: False, 'Pepperoni': Song Object Pepperoni{ by: 35 } played: False}
	
	"""
	def __init__(self, songs):
		# Initialize a song dictionary to store all songs in the jukebox
		self.songs = {}
		for song in songs:
			# Set the key as the title and value as song object
			self.songs[song.title] = song
		# Initialize this flag
		self.playing = None

	def __repr__(self):
		# String rep
		return str(self.songs)

	def add_to_dict(self, song):
		# Adds a Song object to the queue
		# print('Adding Song to queue')
		self.songs[song.title] = song

	def play_song(self, title):
		if self.playing:
			self.stop_song()
		self.playing = self.songs[title]
		self.playing.play()

class Song:	
	""" 
	>>> son = Song('baby', 'elvis', 'dataa')
	>>> print(son)
	Song Object baby{ by: elvis } data: dataa
	>>> son.play()
	>>> print(son.is_playing)
	True
	"""
	def __init__(self, title, artist, data):
		self.title = title
		self.artist = Artist(artist)
		self.data = data
		self.play_count = 0

	def __repr__(self):
		# String rep of a Song
		return 'Song Object' + ' ' + str(self.title) + str(self.artist) + ' data: ' + str(self.data)

	def play(self):
		""" Plays the song """
		self.is_playing = True
		self.play_count += 1

	def stop(self):
		self.is_playing = False

class Artist:
	""" Artist object 
	>>> a = Artist('Picasso')
	>>> print(a)
	{ by: Picasso }
	>>> sl = [Song('SongTitle1', 'Picasso'), Song('SongTitle2', 'Picasso'), Song('SongTitle1', 'Not Picasso')]
	>>> a.add_song_list_to_artist(sl)
	
	>>> a.change_artist_genre('Pop')
	>>> print(a.artist_genre)
	Pop

	>>> a.list_all_genres()
	['Pop', 'Hip Hop', 'Rock', 'Folk']
	"""
	artist_genre = None

	def __init__(self, artist_name):
		self.artist_name = artist_name
		self.songs = set()
	
	def __repr__(self):
		# String rep of a Artist
		return '{ by: ' + str(self.artist_name) + ' }'

	@staticmethod
	def list_all_genres():
		return ['Pop', 'Hip Hop', 'Rock', 'Folk']


	@classmethod
	def change_artist_genre(cls, newGenre):
		cls.artist_genre = newGenre

	def add_song_list_to_artist(self, song_list):
		for s in song_list:
			# print(s)
			self.songs.add(s)

	def get_artist_songs(self):
		# Returns the set of songs!
		return self.songs




if __name__ == "__main__":
	import doctest
	doctest.testmod()
	# unittest.main()













	









	









	









	









	









	









	









	









	









	









	









	




