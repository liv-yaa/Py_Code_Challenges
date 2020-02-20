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

def fams(k, elems):
	# Bad answer!
	k = input()
    elems = [int(x) for x in input().strip().split(' ')]
    print(fams(k, elems))
    # Create a counts dictionary
    cts = {}
    for e in elems:
        cts[e] = cts.get(e, 0) + 1

    # Get the one item in dictionary that has value != 0
    ans = [None, None]
    for e, v in cts.items():
        if v != k:
            ans = (e, v)
    return ans[0]


def captain_room_ans():
	# Answer from https://www.hackerrank.com/challenges/py-the-captains-room/editorial
	K = int(raw_input())

	#Step 1: Gets the input
	roomList = map(int, raw_input().split())

	#Step 2: create a set from input list
	roomSet = set(roomList) 

	#Step 3: Add up all items in the list and set respectively
	sumRoomSet = sum(roomSet) 
	sumRoomList = sum(roomList) 

	# Step 4: 
	temp = sumRoomSet * K - sumRoomList 

	# Step 5
	answer = temp / (K - 1) 

	# Step 6
	print answer
	K = int(input())
	set_S = set()
	sumlist_S = 0
	for i in input().split():
	    I = int(i)
	    set_S.add(I)
	    sumlist_S += I

	print((sum(set_S)*K - sumlist_S)//(K-1)) 


def captain_room():
	rooms = "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 "
	k = 5 # actually input()
	roomList = rooms.strip().split(' ') # actually input()
	print(roomList)






# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

def dayOnDate(gd):
    # Given a date `gd`, find which day is on that date.
    DZ = [
        'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'
    ]
    gd = gd.split(' ')
    mo, da, yr = int(gd[0]), int(gd[1]), int(gd[2])
    # print(mo, da, yr)

    c = calendar.TextCalendar(firstweekday=6).formatmonth(yr, mo, w=4).split('\n')
    # print(c)

    # look for the day in the month
    da = ' ' + str(da) + ' '
    print('da', da)
    for row in c:
        row = '  ' + row + '  '
        print('row', row)
        
        # look for our day in it.
        if da in row:
            print('found da')





            
if __name__ == '__main__':
    # givenDate = input()
    givenDate = "04 30 2000"
    dayOnDate(givenDate)

















































if __name__ == '__main__':
	# text_align(9)
	# print(is_leap(2100))


	print(captain_room())
