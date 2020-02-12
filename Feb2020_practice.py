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
	print(textwrap.fill(S,w))


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

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)


