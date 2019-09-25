import itertools

def stringsRearrangement(inputArray):

    def f(x,y):
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        if c == 1:
            return True
        return False
    
    
    for k in itertools.permutations(inputArray, len(inputArray)):
        r = True
        for i in range(len(k)-1):
            if not f(k[i], k[i+1]):
                r = False
        if r: 
            return True
        
    return False


def extractEachKth(x, k):
    del x[k-1::k]
    return x


def extractEachKth(inputArray, k):

    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]


def firstDigit(inputString):
    
    answer = None
    for n in inputString:
        try:
            return str(int(n))
        except:
            # print('Could not convert')
            pass


def differentSymbolsNaive(s):

    return len(set(s))


def arrayMaxConsecutiveSum(a, k):
    #LUA
    c = m = sum(a[:k])
    
    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)
        
    return m


def growingPlant(upSpeed, downSpeed, desiredHeight):

    d = 1 # Starting day
    h = 0 # starting height
    
    while h < desiredHeight:
        h += upSpeed
        
        if h >= desiredHeight:
            return d
        
        #else
        h -= downSpeed
        
        #increment day
        d += 1
        
        
    


def longestDigitsPrefix(inputString):
    pre = []
        
    for k in range(len(inputString)):
        
        try:
            pre.append(str(int(inputString[k])))
        except:
            return ''.join(pre)

        
    return ''.join(pre)
            


def digitDegree(n):
    # "digit degree": the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
    
    t = 0 # times
    
    while True:
        if len(str(n)) == 1:
            return t
                
        n = sum([int(i) for i in str(n)])
        
        t += 1
        
        if len(str(n)) == 1:
            return t


def digitDegree2(n):
    d = 0

    while n >= 10:
        n = sum([int(i)

         for i in str(n)])
        d += 1
    return d


def bishopAndPawn(bishop, pawn):
    
    bx, by = bishop[0], int(bishop[1])
    px, py = pawn[0], int(pawn[1])
    
    l = 'abcdefgh'

    x = l.index(bx) - l.index(px)
    y = by - py
    
    return abs(x) == abs(y)       


def BAD1isBeautifulString(inputString):
    # True if each letter of the alphabet appears at most as many times as than the previous letter; ie: b occurs no more times than a; c occurs no more times than b; etc.
    
    # a >= b >= c >= ... 
       
    d = {c : inputString.count(c) for c in set(inputString) }
    
    print(d)
    
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    std = sorted(d.keys())
    
    print(alpha[:len(std)], std)
    
    a0 = d.get(std[0])
    b1 = d.get(std[1])
    
    print(std[0], a0)
    print(std[1], b1)
    

def BAD2isBeautifulString(inputString):
    # True if :
        # all letters from a to whatever exist
        # a >= b >= c >= ... 
       
    d = {c : inputString.count(c) for c in sorted(set(inputString)) }
    
    print(d)
    
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    std = sorted(d.keys())
    
    print(alpha[:len(std)], std)
    
    if (alpha[:len(std)] == std):
        
        l0, v0 = 'a', d.get('a')
        l1, v1 = 'b', d.get('b')
        
        print('0', l0, v0)
        print('1', l1, v1)
        
        while v0 >= v1:
            
            l0, v0 = l1, v1
            print('0', l0, v0)
            
            nextLetter = chr(ord(l1) + 1)
            print(nextLetter)
            l1, v1 = nextLetter, d.get(nextLetter)
            
            if v1 == 0:
                break
            elif v0 < v1:
                break
        
        
        
        
            
            
        
        
        
    return False
        
 

def LU1isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)  
        
def findEmailDomain(address):
    a = address.split('@')
    return a[-1] # domain
    

def buildPalindromeLU1(st):
    for i in range(0,len(st)):
        if(st[i:len(st)] == st[i:len(st)][::-1]):
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]


def buildPalindromeLU2(st):
    n = len(st)
    a = ""
    if st == st[::-1]:
        return st
    a = st + st[::-1][1:]
    counter = len(a)
    while counter > n:
        if a[n:counter] == st[n-counter+n:n]:
            return a[0:n] + a[counter:]
        counter -= 1
    return a 

def BADelectionsWinners(votes, k):
    # find the number of candidates who still have a chance to win the election.

    print(votes, k)
    if k == 0:
        if len([x for x in votes if x == max(votes)]) == 1:
            return 1
        else:
            return 0
    
    winnable = []
    for i in range(len(votes)):

        if votes[i] + k > max(votes):
            winnable.append(i)
            
        elif votes[i] == max(votes):
            # Try distributing the votes evenly and see if they are still the max
            avail = k
            for j in range(len(votes)):
                if j != i:
                    votes[j] + 1
                    k -= 1
                    print('avail', avail, 'k', k, 'votes', votes)
                    
     
    
    
    print('winnable', winnable)
    return len(winnable)

        
 
def LU1electionsWinners(v, k):
    c, mv = 0, max(v)
    if k==0 and v.count(mv)==1: c=1
    for i in v: 
        if i+k>mv: c+=1
    return c

def LU2electionsWinners(votes, k):
    votes_req = max(votes)
    if not k:
        front_runners = votes.count(votes_req)
        if front_runners >= 2:
            return 0
        return 1
    return sum(1 for v in votes if v+k > votes_req)

def BAD1isMAC48Address(inputString):

    l = inputString.split('-')

    print(l)
    
    if len(l) != 6:
        return False
    
    for sub in l:
        try:
            hexa = int(sub, 16)
            print('sub', sub, 'hexa', hexa)
        except:
            print('Cant convert to integer')
            return False
        
    return True
        
def LUisMAC48Address(inputString):
    try:
        l = inputString.split('-')

        if len(l) != 6:
            return False

        for sub in l:
            if len(sub) != 2:
                return False
            
            hexa = int(sub, 16)        


        return True
    except:
        return False
   



def isDigit(symbol):
    return symbol in '0123456789'



def lineEncodingSOLVED(s):

    # First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
    lst = []
    i = 0
    j = 1
    while True:
        x = s[i:i + j]
        print(x)
        print('i, j', i, j)
        
        if i+j == len(s):
            if len(set(x)) != 1:
                lst.append(s[i:i+j - 1])
                lst.append(s[i+j - 1:])
                print('break2')
                break
            else:
                lst.append(s[i:i+j])
                print('break2')
                break

        if len(set(x)) != 1:    # nonhomogenous list found
            lst.append(s[i:i+j - 1])  # append the one before
            i += j - 1            # increment i by len of newly added sublist 
            print('lst',lst)
            
            
            j = 1               # Reset j
        else:                   # homogenous list
            j += 1
        
        
        
    print(lst)
    
   

    # Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
    for i in range(len(lst)):
        if len(lst[i]) > 1:
            lst[i] = str(len(lst[i])) + lst[i][0]
        
    print(lst)
    
    return ''.join(lst)
    
    
from itertools import groupby
def lineEncodingLU(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x        
        
def lineEncodingLU2(s):
    counted = re.findall(r'((\w)\2*)', s)
    return "".join([ str(len(count[0])) + count[1] if len(count[0]) > 1 else str(count[0]) for count in counted])

def chessKnightSOLVED(cell):
    # check how many valid L-shpaed moves a knight can perform
    # In the center it is 8, but on the edge it might be 2 or 3 or 4 or 6
    
    # First convert the letters to numbers - both x and y now from int 1-8, inclusive
    cx = ord(cell[0]) - 96 # X-axis is letters 'abcdefgh'
    cy = int(cell[1])
    
    def mv1(x, y):
        # x: Right 2; y: Up 1
        return (x + 2, y + 1)
    def mv2(x, y):
        # x: Right 1; y: Up 2
        return (x + 1, y + 2)
    def mv3(x, y):
        # x: Left 2; y: Up 1
        return (x - 2, y + 1)
    def mv4(x, y):
        # x: Left 1; y: Up 2
        return (x - 1, y + 2)
    def mv5(x, y):
        # x: Right 2; y: Down 1
        return (x + 2, y - 1)
    def mv6(x, y):
        # x: Right 1; y: Down 2
        return (x + 1, y - 2)
    def mv7(x, y):
        # x: Left 2; y: Down 1
        return (x - 2, y - 1)
    def mv8(x, y):
        # x: Left 1; y: Down 2
        return (x - 1, y - 2)
        
    ans1 = mv1(cx, cy)
    ans2 = mv2(cx, cy)
    ans3 = mv3(cx, cy)
    ans4 = mv4(cx, cy)
    ans5 = mv5(cx, cy)
    ans6 = mv6(cx, cy)
    ans7 = mv7(cx, cy)
    ans8 = mv8(cx, cy)
    
    answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    ok = [a for a in answers if a[0] in nums and a[1] in nums]
    
    return len(ok)


def chessKnightANS(c):

    x , y = ord(c[0]) - 96, int(c[i])

    l = []
    for i in [-2, -1, 1, 2]:
        for j in [-2, -1, 1, 2]:
            if 1 <= x + i <= 8 and 1 <= y + j <= 8:
                l.append(x, y)

    return len(l) // 2 # to account for double counting

    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    






    
    
    
    
    
    







