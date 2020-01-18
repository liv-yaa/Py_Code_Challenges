
	
""" 
Factory Method Design Pattern!

	- Used to create implementations of a common interface
	- Separated the process of creating an object 

	- The application allows the subclass to decide what it will be? 


	How:
	- Start with a parent class, 
	- create child classes


	- Take `cls`
	- Replace complex if/elif/else code
	- 

	When to use:
	- When refactoring code 

"""

import json
import xml.etree.ElementTree as et

class Song:
	""" Class representing a Song """
	def __init__(self, song_id, title, artist):
		self.song_id = song_id
		self.title = title
		self.artist = artist

class SongSerializer:
	""" Class contains set of methods that serialize the Song 

	>>> ss = SongSerializer()
	>>> print(ss)
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
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        
        else:
            raise ValueError(format)





if __name__ == "__main__":
	import doctest
	doctest.testmod()




























































