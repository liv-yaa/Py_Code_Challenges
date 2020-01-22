""" 
REFACTORING PRACTICE!

Note: This was my technical idea for the Plenty interview 1-2020
I did not whiteboard it correctly but tried :(


Factory Method Design Pattern!

	What is a Factory method?
		- To provide a separate component w/ responsibility to decide 
		which concrete implementation should be used
		- Makes this decision based on some specified parameter (here, 'format')
		- 

	When:
		- Used to create implementations of a common interface
		- Separated the process of creating an object 
		- The application allows the subclass to decide what it will be? 


	How:
		Look for a common interface **
		- do the if/elif/else 
			start with a common 'start' and
			end at a common 'final destination'??

			ex. here, the SongSerializer takes a Song and returns a string.


	Refactoring code **
		" the process of changing a software system in such a way that 
		does not alter the external behavior of the code yet improves 
		its internal structure "


		1. Define the Desired Interface
			Here, it is an object or a function that takes a Song object and returns a string representation.

		2. Refactor just one of the logical paths in this interface
			Start with ._serialize_to_json()

		3. Then, do the other parts

		4. Monitor that behavior has not changed

		5. Add a new method ._get_serializer() that takes the desired `format`
		   This is the * Factory Method *
		   It evaluates `format` and returns the matching serialization function.
		   							 ``````` 							`````````

		6. Delete the block in original serialize() method.
		   Now, have it use the new _get_serializer(format) method
		   and return serializer(song)

"""

import json
import xml.etree.ElementTree as et

class Song:
	""" Class representing a Song 
	# >>> s = Song(44, 'tt', 'aa')
	# >>> print(s)
	# 44 tt aa
	"""
	className = 'Song'
	
	def __init__(self, song_id, title, artist):
		self.song_id = song_id
		self.title = title
		self.artist = artist

	# def __repr__(self):
	# 	return str(self.song_id) + ' ' + str(self.title) + ' ' + str(self.artist)

class BadSongSerializer:
	""" 
	** HARD AND BAD TO USE ***

		Can convert a Song object into its string representation,
		depending on what the 'format' is
		Class contains set of methods that serialize the Song 

		>>> ss = BadSongSerializer()
		>>> mySong = Song(33, 'mySongTitle', 'mySongArtist')
		>>> ss.serialize(mySong, 'JSON')
		'{"id": 33, "title": "mySongTitle", "artist": "mySongArtist"}'

		>>> ss.serialize(mySong, 'XML')
		'++++ XML SONG ++++++'

		>>> ss.serialize(mySong, "YAML")
		ValueError
	"""
	def serialize(self, song, format):
		""" Uses spagetti if/elif/else block to determine how to parse the song """

		if format == 'JSON':
			song_info = {
				'id': song.song_id,
				'title': song.title,
				'artist': song.artist
			}
			return json.dumps(song_info)

		elif format == 'XML':
			return '++++ XML SONG ++++++'
			# song_info = et.Element('song', attrib={'id': song.song_id})
			# title = et.SubElement(song_info, 'title')
			# title.text = song.title
			# artist = et.SubElement(song_info, 'artist')
			# artist.text = song.artist
			# return et.tostring(song_info, encoding='unicode')

		else:
			print('ValueError')
			# raise ValueError(format)

class BetterSongSerializer:
	""" 
	** Better TO USE ! ***

		Can convert a Song object into its string representation,
		depending on what the 'format' is

		>>> ss = BetterSongSerializer()
		>>> mySong = Song(33, 'mySongTitle', 'mySongArtist')
		>>> ss.serialize(mySong, 'JSON')
		'{"id": 33, "title": "mySongTitle", "artist": "mySongArtist"}'
		>>> ss.serialize(mySong, 'XML')
		'++++ XML SONG ++++++'
		>>> ss.serialize(mySong, "YAML")
		'ValueError'
	"""
	def serialize(self, song, format):
		"""  Depends on a factory function to tell it how to behave! 
		"""
		serializer = self._get_serializer(format) # Get method name
		return serializer(song) # Call method on our argument

	def _get_serializer(self, format):
		""" A factory function
			Determines how to serialize the song using factory methods
			Takes the string format,
			Returns a * function * 
			Because that is what we want to 'overwrite' the serialize method with!
		"""
		if format == 'JSON':
			return self._serialize_to_json # Returns function name not a call
		elif format == 'XML':
			return self._serialize_to_xml # Returns function name not a call
		else:
			return 'ValueError'
			# raise ValueError(format)


	def _serialize_to_json(self, song):
		payload = {
			'id': song.song_id,
			'title': song.title,
			'artist': song.artist
		}
		return json.dumps(payload)


	def _serialize_to_xml(self, song):

		return '++++ XML SONG ++++++'
		# song_info = et.Element('song', attrib={'id': song.song_id})
		# title = et.SubElement(song_info, 'title')
		# title.text = song.title
		# artist = et.SubElement(song_info, 'artist')
		# artist.text = song.artist
		# return et.tostring(song_info, encoding='unicode')







if __name__ == "__main__":
	import doctest
	doctest.testmod()




























































