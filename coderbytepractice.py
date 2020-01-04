# coderbyte practice

def LetterChanges(str):
	""" Have the function LetterChanges(str) take the str parameter being passed and modify it using 
	the following algorithm. Replace every letter in the string with the letter following it in the alphabet 
	(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and 
	finally return this modified string.Have the function LetterChanges(str) take the str parameter being 
	passed and modify it using the following algorithm. Replace every letter in the string with the letter 
	following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
	 (a, e, i, o, u) and finally return this modified string. """
	out = ''
	for let in str:
		if ord(let) == 90:
			out += 'A'
		elif ord(let) == 122:
			out += 'a'
		elif (64 < ord(let) and ord(let) < 90) or (96 < ord(let) and ord(let) < 122) :
			out += chr(ord(let) + 1)
		else:
			out += let

	out = out.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
	return out

print(LetterChanges(input()))