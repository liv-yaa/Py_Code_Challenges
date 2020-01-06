# Following this! https://codechalleng.es/bites/paths


# DATA FORMATS https://codechalleng.es/bites/paths/data-formats

# Bite 38. Using ElementTree to parse XML: *NOT DONE* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import xml.etree.ElementTree as ET
class XMLParser:
	"""
	Parses XML using `ElementTree`:
		The Element type is a flexible container object, designed to store hierarchical data structures in memory. 
		The type can be described as a cross between a list and a dictionary.
		https://docs.python.org/2/library/xml.etree.elementtree.html

	"""
	# from OMDB
	xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
		<root response="True">
		  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
		  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
		  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
		  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
		  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
		</root>'''  # noqa E501

	def get_tree(self):
	    """ Use ET.fromstring - this reads data from the string 
    	    
    	    print(root, root.tag, root.attrib) # <Element 'root' at 0x107a3f910>, 'root', {'response': 'True'}
			Children are nested, and we can access specific child nodes by index:
				root[0][1].text

			Methods for finding elements:
				Element.iter()
		"""
	    print('get_tree root')
	    root = ET.fromstring(self.xmlstring)
	    return root
	    



	def get_movies(self):
	    """Call get_tree and retrieve all movie titles, return a list or generator"""
	    print('get_movies')
	    root = self.get_tree()
	    print(root)

	    r = []
	    for c in root:
	    	r.append(c.attrib)
    	# return r



	def get_movie_longest_runtime(self):
	    """Call get_tree again and return the movie title for the movie with the longest
	       runtime in minutes, for latter consider adding a _get_runtime helper"""
	    print('get_lrt')
	    r = self.get_tree()
	    m = self.get_movies()
	    print('r', r, 'm', m)
# if __name__ == "__main__":
	# STUCK - need to look up answers
	# x = XMLParser()
	# x.get_tree()
	# x.get_movies()
	# x.get_movie_longest_runtime()




# Bite 130. Analyzing basic JSON Car Data: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from collections import Counter
import requests
class JSONParser:
	""" Data analysis with basic car data """

	CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'
	with requests.Session() as s:
	    data = s.get(CAR_DATA).json() # A list of dicts


	# your turn:
	def most_prolific_automaker(self, year):
		# print(year)

		c = Counter()

		for d in self.data:
			if d['year'] == year:
				# print(d['year'])
				# for k, v in d.items():
				# 	print('k,v', k, v)
				c.update([d['automaker']])
		# print(c)
		std = [str(k) for k, v in sorted(c.items(), key=lambda item:item[1])[::-1]]
		# print('std', std)
		return std[0]


	def get_models(self, automaker, year):
	    """Filter cars 'data' by 'automaker' and 'year',
	       return a set of models (a 'set' to avoid duplicate models)"""
	    # print('get_models!!!')
	    # return {'tests'}

	    s = set()
	    for m in self.data:
	    	if m['automaker'] == automaker and m['year'] == year:
	    		s.add(str(m['model']))

	    return s 
if __name__ == "__main__":
	# See testCars.py for full test suite
	j = JSONParser()
	# print(j.get_models('Nissan', 2000))

	models = j.get_models('Volkswagen', 2008)
	# print(models, len(models))


# Bite 1105. Slice and dice ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text):
	"""Get a list of words from the passed in text.
	Instructions:
	1. Take the block of text provided and strip off the whitespace at both ends. 
	2. Split the text by newline (\n).
	3. Loop through lines, for each line:
	strip off any leading spaces,
	check if the first character is lowercase,
	if so, split the line into words and get the last word,
	strip the trailing dot (.) and exclamation mark (!) from this last word,
	and finally add it to the results list.
	Return the results list.

	"""
	results = []
	for line in text.strip().splitlines():
		line = line.lstrip()

		if line[0] not in ascii_lowercase:
			continue

		words = line.split()
		last_word_stripped = words[-1].rstrip('!.')
		results.append(last_word_stripped)

	return results


if __name__ == '__main__':
	r = slice_and_dice(text)
	print(r)























