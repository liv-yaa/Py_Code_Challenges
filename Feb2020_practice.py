# Feb2020_practice.py

def matchingStrings(strings, queries):
	""" """
    results = [None] * len(queries)
    for i, q in enumerate(queries):
        results[i] = strings.count(q)
    return results


import textwrap
def textWrap():
	S = raw_input()
	w = input()
	print textwrap.fill(S,w)