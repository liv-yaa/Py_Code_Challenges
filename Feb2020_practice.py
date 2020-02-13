# Feb2020_practice.py

def matchingStrings(strings, queries):
	""" """
    results = [None] * len(queries)
    for i, q in enumerate(queries):
        results[i] = strings.count(q)
    return results

import textwrap

def wrap(s, w):
    return textwrap.fill(s,w)

def swap_case(s):
    out = ''
    for c in s:
        if c.isupper():
            out += c.lower()
        elif c.islower():
            out += c.upper()
        else:
            out += c

    return out

# if __name__ == '__main__':
#     s = 'HackerRank.com presents "Pythonist 2".'
#     result = swap_case(s)
#     print(result)


def text_align(thickness):
	# thickness = int(input()) #This must be an odd number
	c = 'H'

	#Top Cone
	for i in range(thickness):
	    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

	#Top Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

	#Middle Belt
	for i in range((thickness+1)//2):
	    print((c*thickness*5).center(thickness*6))    

	#Bottom Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

	#Bottom Cone
	for i in range(thickness):
	    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


def is_leap(year):    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False



if __name__ == '__main__':
    text_align(9)
	print(is_leap(2100))
