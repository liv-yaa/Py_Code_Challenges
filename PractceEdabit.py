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

def robotPath(instructions, bound):
    #Given a sequence of instructions and a restricting square, output an array of two integers representing the final position of the robot after executing all the instructions.
   # 'L', 'R', 'U', 'D'

    # return bound
    
    loc = [0, 0]
    i = 0 # get the first instruction
    
    while True:
        # Square is centered at 0,0 and `bound` is equal to the half-length of the restricting square's side.
        if i == len(instructions):
            return loc
            
        if instructions[i] == 'L' and -(bound) <= loc[0] - 1 <= bound:
            loc[0] = loc[0] - 1

        elif instructions[i] == 'R' and -(bound) <= loc[0] + 1 <= bound:
            loc[0] = loc[0] + 1
                
        elif instructions[i] == 'U' and -(bound) <= loc[1] + 1 <= bound:
            loc[1] = loc[1] + 1
                
        elif instructions[i] == 'D' and -(bound) <= loc[1] - 1 <= bound:
            loc[1] = loc[1] - 1
                
        i += 1
        
def knapsackLight2(weight1, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return "both"
    
    elif weight1 <= maxW and weight2 <= maxW: # and weight1 + weight2 > maxW:
        return "either"
    
    elif weight1 <= maxW and weight2 > maxW:
        return "first"
    
    elif weight2 <= maxW and weight1 > maxW:
        return "second"
    
    else:
        return "none"


def squarePerimeter(n):

    return n*4

def isLuckyNumber(n):
    
    return all([d not in '01235689' for d in str(n)])

def sumOfDivisorsBAD):
    
    return sum([d for d in range(1, n+1) if n % d == 0])

import math
def sumOfDivisorsANS(n):
        res = 1
        for i in range(2, int(math.sqrt(n) + 1)):
                curr_sum = 1
                curr_term = 1
        
                while n % i == 0:
                        n = n / i
                        curr_term = curr_term * i
                        curr_sum += curr_term
                res = res * curr_sum
        if n > 2:
                res = res * (1 + n)
        return res


def firstReverseTry(arr):

    if len(arr) > 1:
        temp = arr[0]
        arr[0] = arr[-1]
        arr[-1] = temp
        
    return arr


def rightTriangle(sides):

    s = sorted(sides)
    return (s[2] ** 2 == s[0] ** 2 + s[1] ** 2)


def sameElementsNaive(a, b):

    return len(list(set(a) & set(b)))

def isDigit(symbol):

    try:
        int(symbol)
        return True
    except:
        return False

def isUppercase(symbol):
    
    return (65 <= ord(symbol) <= 90)

def arrayReplace(inputArray, elemToReplace, substitutionElem):
        
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
        
    return inputArray

# arrayReplaceBetterANS = lambda i, e, s: [s if x == e else x for x in i] 

def arithmeticProgressionANS(e, f, n):
        return e+(f-e)*(n-1)

def waterTubes(w, f):
    # 1 x 2 x 5 = 10 L^3
    # // 
    # 1 x 1 x 2 = 2 L^3 / min
    # = 
    # 10 // 2 = 
    
    m = 0
    while any(x > 0 for x in w):
        for i, x in enumerate(w):
            w[i] -= f[i]
        m += 1
    return m

# def waterTubes2 = lambda w, f: max((x + y - 1) // y for x, y in zip(w, f))

def reversedSumOfDigitsBAD(p, n):
    # Time exceeded on bigger tests :(
    # n = 1
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # n = 2
    # 10, 11, 12, 13, 14, 15, ... 
    # n = 3
    # 100, 101, 102, 103
    
    # Initialize the smallest number of that length:
    out = "1" + ('0' * (n - 1))
    print(out)
    
    while True:
        l = sum([int(i) for i in out])
        print(l)
        
        if p == 0 and n == 1:
            return '0'
        elif p == 0:
            return '-1'
        
        elif l == p:
            return out
        
        elif len(out) > n:
            return '-1'
        
        else:
            out = str(int(out) + 1)
            print(out)


def reversedSumOfDigitsANS(p, n):
    r = "-1"
    if p == 0:
        if n == 1:
            r = "0"
        return r

    if n*9 >= p:      
        s = [0]*(n-1) + [1]
        S = ""
        for i in s:
            while i < 9 and p>1:
                i += 1
                p -= 1
            S += str(i)
        r = S[::-1]
    return r

# wowe
imageTrunc = lambda i, t: [[[x, t][x > t] for x in y] for y in i]

# my ans
def imageTruncation(image, threshold):
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] > threshold:
                image[i][j] = threshold
                
    return image


def leastFactorial(n):

    f = 1
    z = 1
    if n == 1:
        return 1
    while True:
        print('f', f, 'z', z)
        z += 1
        f = f * z
        
        if f >= n:
            return f


def leastFacANS(n):
    i = k = 1
    while k < n:
        i += 1
        k *= i
    return k


import math
def insideCircle(point, center, radius):    
    return radius >= math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)


def seatsInTheater(nCols, nRows, col, row):
    # return number of people who sit strictly behind you and in your column or to the left.
    # A1 is at the origin; the screen is along the x-axis
    return (nCols - col + 1) * (nRows - row)
    

def integerToStringOfFixedWidth(n, w):
    
    if len(str(n)) > w:
        n = str(n)[-w:]
        
    elif len(str(n)) < w:
        n = str('0' * -(len(str(n)) - w)) + str(n)
        
    return str(n)


def integerToStringOfFixedWidth(number, width):
    return ('0' * width + str(number))[-width:]


def fromDecimal(b, n):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

def fromDecimal(b, n):

    r = ''
    
    while n:
        r = str(n % b) + r
        print('r', r)
        print('n', n)
        n //= b
        
    return r

import math
def reverseOnDiagonals(matrix):
     # reverse the order of elements on both of its longest diagonals.
     
     def switch(c1, c2): # takes (x, y) tuples of coordinates and switches them in the matrix
          temp = matrix[c1[0]][c1[1]]
          matrix[c1[0]][c1[1]] = matrix[c2[0]][c2[1]]
          matrix[c2[0]][c2[1]] = temp          
     
     
     l = len(matrix[0])     # length     
     m = math.ceil(l / 2)   # mid mark     
     i = 0                  
     
     while i < m:
          x1, y1 = (i, i), (l - i - 1, l - i - 1)
          switch(x1, y1)

          x2, y2 = (i, l - i - 1), (l - i - 1, i)
          switch(x2, y2)
          
          i += 1
          
     return matrix
          
          
def candles(candlesNumber, makeNew):
        
    stubs = total = 0
    
    while candlesNumber > 0:
        
        candlesNumber -= 1
        stubs += 1
        total += 1
            
        if stubs == makeNew:
            candlesNumber += 1
            stubs -= makeNew
        
    return total

            
def maxSumSegments(iA):
    # Pick the length subarray that has the maxiumum sum

    out = []
    
    for k in range(len(iA)):
        
        s = [sum(iA[j:j+k+1]) for j in range(len(iA) - k)]
        out.append(s.index(max(s)))

    return out
     

def maxSumSegments(iA):
    # Pick the length subarray that has the maxiumum sum
    
    return [[sum(iA[j:j+k+1]) for j in range(len(iA) - k)].index(max([sum(iA[j:j+k+1]) for j in range(len(iA) - k)])) for k in range(len(iA))]


def leapYear(y):
    return y % 400 == 0 or not (y % 100 == 0) and y % 4 == 0


def appleBoxes(k):
    
    r = sum([i**2 for i in range(1, k+1) if i % 2 == 0])
    y = sum([i**2 for i in range(1, k+1) if i % 2 == 1])
    
    return r - y

# Alt ans - wow
appleBoxesLabda = lambda k: -k*k%(k*=%2 - 5)

def arrayMinimumAboveBound(inputArray, bound):
    inputArray.sort()
    
    for i in range(len(inputArray) - 1):
        if bound < inputArray[i + 1]:
            return inputArray[i + 1]
        

def electionsWinners(v, k):
    M = max(v)
    a = b = 0
    for i in v:
        a += i + k > M
        b ^= i == M
    return a or b


def removeDuplicateCharacters(str):
    for ch in set(str):
        if str.count(ch) > 1:
            str = str.replace(ch, '')
                      
    return str


def regularBracketSequence1(sequence):
    
    while True:
        x = sequence.find('(')
        y = sequence.find(')')
        if x > y: # Wrong order 
            return False
        elif x > -1 and y > -1: # Continue           
            sequence = sequence.replace('(', 'L', 1)
            sequence = sequence.replace(')', 'R', 1)
        elif x == -1 and y == -1: # Success! Even number in proper order - return True
            return True
        elif x == -1 or y == -1: # Uneven number - return False
            return False


def parallelLines(l1, l2):
    
    return l1[0] * l2[1] == l2[0] * l1[1]


def companyBotStrategy(trainingData):
    # https://app.codesignal.com/company-challenges/codesignal/gJMBmTwHHMF8mbQvH
    div = 0
    n = sum([1 for d in trainingData if d[1] == 1])
    
    if n != 0:
        div = sum([d[0] for d in trainingData if d[1] == 1]) / n
    return div



def evenNumbersBeforeFixed(sequence, fixedElement):
    
    try:
        pos = sequence.index(fixedElement)
        return len([i for i in range(pos) if sequence[i] % 2 == 0])
    except:
        return -1


from itertools import combinations 
def countIncreasingSequences(n, k):
    
    return len([c for c in list(combinations(range(1, k + 1), n)) if list(c) == sorted(c)])


def decipher(cipher):

    out = ""
    i = 0
    
    while True:
        if i < len(cipher) - 1:
            n = int(cipher[i:i+2])
            
            if n in [n for n in range(97, 123)]:
                i += 2
            else:
                if i < len(cipher) - 2:
                    n = int(cipher[i:i+3])
                    i += 3            
            out += chr(n)
        else:
            break
    return out
            
        
def fullName(first, last):

    return first + ' ' + last


def shapeAreaRecursive(n):
    
    if n == 1:
        return 1
    
    else:
        return shapeArea(n - 1) + (4 * (n - 1))


def shapeAreaIter(n):
    area = 1
    for i in range(1, n + 1):
        area += 4*(i - 1)
        
    return area


def properOrImproper(a):
    #if the absolute value of the fraction is strictly less than one.
    
    if abs(a[0] / a[1]) >= 1:
        return "Improper"
    return "Proper"


def findTheRemainder(a, b):

    return a % b


def hailstoneSequence(n):
    steps = 0
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
            
    return steps


def isDiagonalMatrix(matrix):
    #In linear algebra, a square matrix is called a diagonal matrix if all entries outside the main diagonal are zero.

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0 and (i, j) not in mainDiag(matrix):
                return False
    return True
        
    
def mainDiag(m):
    # helper function - Takes a matrix m and returns the `main diagonal` - goes from the upper left corner of a matrix to its lower right corner.
    return [(i, i) for i in range(len(m))]
    
#numpy solution
    p = numpy
    i, j = p.nonzero(*eval(dir()[0]))
    return p.any(i - j) ^ 1


def kthDivisor(n, k):
    try:
        return [i for i in range(1, n + 1) if n % i == 0][k - 1]
    except:
        return -1

# concise solution ^^
    n, k = eval(dir()[0])
    t = -1,
    i = n
    while n:
      if i % n < 1:
        t += n,
      n -= 1
    return t[-k]


def eulersTotientFunction(n):
    #Given an integer n, find the value of phi(n), where phi is Euler's totient function.
    #Euler’s totient or phi function is an arithmetic function that counts the positive integers less than or equal to n that are relatively prime to n.
    return len([i for i in range(1, n+1) if relPrime(i, n)]) 
    
def relPrime(p, q):
    #Two integers are said to be relatively prime (or coprime) if the only positive integer that evenly divides both of them is 1.
    return [i for i in range(1, min(p, q) + 1) if p % i == 0 and q % i == 0] == [1]    
    
# Concise solution ^^
    n, = eval(dir()[0])
    return sum(numpy.gcd(range(n), n) < 2)


from itertools import permutations
def equationTemplate(values):
    #try fill the template that will result in a correct equation. - return boolean if possible
    
    for p in permutations(values):  
        if bool(p[0] == p[1] * p[2] * p[3]) == True or bool(p[0] * p[1] == p[2] * p[3]) == True:
            return True
          
    return False

#Super concise:
    a, b, c, d = sorted(*eval(dir()[0]), key=abs)
    return a*b*c == d or a*d == b*c

def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray) - 1)])
    # return max([b*c for (b,c) in zip(a,a[1:])])

def isInfiniteProcess(a, b):
    #Given integers a and b, determine whether the following pseudocode results in an infinite loop

    # while a is not equal to b do
    #   increase a by 1
    #   decrease b by 1

def isInfiniteProcess(a, b):
    #Given integers a and b, determine whether the following pseudocode results in an infinite loop

    # while a is not equal to b do
    #   increase a by 1
    #   decrease b by 1

def isInfiniteProcess(a, b):
    #Given integers a and b, determine whether the following pseudocode results in an infinite loop

    # while a is not equal to b do
    #   increase a by 1
    #   decrease b by 1

    return (a != b) and (a >= b or ((a % 2 == 0 or b % 2 == 0) and (a % 2 == 1 or b % 2 == 1)))


def divisorsPairs(sequence):
    # Find num of unique pairs such that second elem is divis by first one and they are !=
    # for each, use number as many times as you wish
    
    return len([(n, m) for n in sequence for m in sequence if n != m and m % n == 0])

def applesDistribution(apples, boxCapacity, maxResidue):
    #distribute them between some gift boxes in such a way that all the boxes will contain an equal number of apples. 
    #maxResidue is max leftover
    #number of left out apples should be less than x apples in each box
    #infinite number of boxes . with boxCapacity
    # How mnay ways to distribute the apples? maximum is boxCapacity ways because they're all the same
     
    return len([i for i in range(1, boxCapacity + 1) if apples % i <= maxResidue])


def higherVersion(ver1, ver2):

    # `semver` - semantic versioning
    # Each point compared with its respective point, independently and in order of operations
    # return bool if first is greater than second
    
    v1, v2 = ver1.split("."), ver2.split(".")
            
    for i in range(len(v1)):
        if int(v1[i]) > int(v2[i]):
            return True
        if int(v1[i]) < int(v2[i]):
            return False
        
    return False
        

def parabole(a, b, c, x):
    #A parabole is a curve defined by the equation y = ax2 + bx + c where a, b, c are given integer parameters a, b, and c
    #Given the x-coordinate of a point on the parabole with specified coefficients, find the y-coordinate of that point.
    
    return a * x ** 2 + b * x + c

def differentSubstringsTrie(iS):
    #Given a string, find the number of different non-empty *substrings* in it.
     
    ol = []
    for i in range(0, len(iS)):
        ol.extend([iS[i:i + j + 1] for j in range(0, len(iS) - i)])
            
    return len(set(ol))


def josephusProblem(n, k):
    # Start at person 1 through n in clockwise direction circle. In each step, k-1 people are skipped and the person you land on is removed from the circle. Who is last remaining person
    people = [n for n in range(1, n + 1)]
    i = 0

    while True:
        # Skip k-1 people after curr and delete the person at the index. 
        i = (i + k - 1) % len(people)
        del people[i]
        
        if len(people) == 1:
            return people[0]


def digitsProduct(product):

    #find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product
    
    under10 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    primes = []
    
    nums = [] #all nums that * digits = product
    
    p = dpRecurse(product)

    
    if nums:
        return min(nums)
    else:
        return -1
            
        
    
def dpRecurse(num):
    # Splits up num into prime factors, then sort it! 
    
    facs = [i for i in range(1, num + 1) if num % i == 0]
    
    print(facs)
    
    try:
        x = facs[len(facs) // 2]
        y = int(num / x)
        
        m = []

        while True:
            if x < 10:
                if y < 10:
                    m.append(int(str(x) + str(y)))
        print


def minimalMultiple(n, l):
    #Find the smallest multiple of the given number n that's not less (>=) than a specified lower bound l
    if n > l:
        return n
    m = n
    while True:
        m += n 
        
        if m >= l:
            return m


# def minimalMultipleANS
    n, l, r = eval(dir()[0])
    return max(0, 1 + n//2 - max(l, n-r))

    n, l, r = eval(dir()[0])

    a, c = l, 0
    while l <= a <= r:
        if a <= n - a <= r:
            c += 1
        a += 1
        
    return c


def countSumOfTwoRepresentations2(n, l, r):

    # find num of ways n = A + B such that l <= A <= B <= r    
    
    a, c = l, 0
    
    while l <= a <= r:
        if a <= n-a <= r:
            c += 1
            
        a += 1
        
    return c


def pointInLine(p, l):
    #line : a set of such points (x, y) that A * x + B * y + C = 0 for specified A, B and C.
    
    return l[0] * p[0] + l[1] * p[1] + l[2] == 0
    

def comfortableNumbers(l, r):
    # Got help
    # Define s(x)
    def s(x):
        # sum of x's digits
        s = sum([int(d) for d in str(x)])

        return range(x - s, x + s + 1)
 
    t = 0
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            t += i in s(j) and j in s(i)
                
    
    return t


def lastDigit(a, b):
    return pow(a,b,10)


def matrixTransposition(matrix):
    # from m x n get transpose, n x m
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def firstDigit(inputString):
    
    return re.findall('\d', inputString)[0]


def strangeCode(s, e):
    out = ''
    while True:
        if s < e - 1:
            s += 1
            e -= 1

            if len(out) > 0 and out[-1] == 'a':
                out += 'b'
            else:
                out += 'a'
        else:
            return out

def dfsComponentSize(matrix, vertex):
    # matrix[i][j] = true if there is an edge from the ith to the jth vertex, and false otherwise. 
    # Graph given is 'undirected'-- it is guaranteed that for each i and j matrix[i][j] = matrix[j][i]. Visually, this looks like Symmetry on the Diagonal.
    
    # Given Adjacency matrix of undirected graph & a vertex in it,
    ### Return the size of the 'connected component'
    ### -- a set of all nodes which can be reached from each other and cannot be reached from any other node of this graph.
    
    cc = dict() # connected components
    print(cc)
    
    for i in range(len(matrix[vertex])):
        # if matrix[vertex][i] == True:
        cc[i] = matrix[vertex][i]

    print(cc)
    
    # return len(cc)


def graphEdges(matrix):
    #Count the number of different edges in a given undirected graph with no loops and multiple edges.
    
    # Cut graph in half diagonally
    return sum([1 for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == True ])//2


























import copy
def volleyballPositions(formation, k):
    forms = {
        0: (0, 1), # Player5
        1: (1, 0), # Player4
        2: (3, 0), # Player6
        3: (2, 1), # Player3
        4: (3, 2), # Player1
        5: (1, 2), # Player2
    }

    out = copy.deepcopy(formation)
    
    for i, f in forms.items():
        o = forms.get((i + k) % 6) # Get original position
        out[o[0]][o[1]] = formation[f[0]][f[1]] # Put player name at orig position

    return out


def whoseMove(lastPlayer, win):

    if win == True:
        return lastPlayer
    if lastPlayer == "white":
        return "black"
    return "white"
















def differentDigitsNumberSearch(inputArray):
    
    for item in inputArray:
        if len(set(str(item))) == len(str(item)):
            return item
    
    return -1


import copy
def primeFactors2(n):
    def isPrime(m):
        f = [i for i in range(1, m + 1) if m % i == 0]
        return m == 1 or m == 2 or len(f) == 2 and f[0] == 1 and f[1] == m

    def getFacs(k):
        # provide list of k's factors
        return [i for i in range(1, k + 1) if k % i == 0]
    
    if n == 1:
        return []
    
    facs = [n]
    
    # create a list, dividing continuously until all are prime (check isPrime)
    while True:
        if all([isPrime(i) for i in facs]):
            return facs
        else:        
            newFacs = []
            for fac in facs:
                if isPrime(fac):
                    newFacs.append(fac)
                else:
                    f = getFacs(fac)
                    newFacs.extend([f[1], fac//f[1]])
            facs = sorted(set(newFacs))


def domainType(domains):
    tps = {
        '.com': "commercial",
        '.org': "organization",
        '.net': "network",
        '.info': "information"  
    }
    
    out = []
    for d in domains:
        try:
            end = '.' + d.split('.')[-1]
            out.append(tps[end])
            
        except:
            print("error")
            
    return out

def digitSum(n):
    s = 0
    for dig in str(n):
        s += int(dig)
    return s
    

def coolString(ss):
    
    ss = ''.join([i for i in ss if i != ' '])

    
    if len(ss) < 2:
        if not ss[0].isalpha():
            return False 
        if ss[0].isalpha():
            return True 
    
    for i in range(len(ss) - 1):
        
        if ss[i].isdigit():
            return False
        
        if ss[i + 1].isdigit():
            return False
        
        if ord('a') <= ord(ss[i]) <= ord('z'):
            # if ord('A') <= ord(ss[i + 1]) <= ord('Z'):
            #     print('True')
            if ord('a') <= ord(ss[i + 1]) <= ord('z'):
                print('False')
                return False
            
        if ord('A') <= ord(ss[i]) <= ord('Z'):
            # if ord('a') <= ord(ss[i + 1]) <= ord('z'):
            #     print('True')
            if ord('A') <= ord(ss[i + 1]) <= ord('Z'):
                print('False')
                return False
            
    return True

coolString = lambda i: not re.search('[A-Z]{2}|[a-z]{2}|[\W\d_]', i)


def longestString(iA):
    return [j for j in iA if len(j) == max([len(i) for i in iA])][0]


def stringsCrossover(inputArray, result):
    #result = string of same length as A, B, such that result[i] = A[i] or B[i]
    #how man ypairs of strings could potentially give you result?
    
    def possible(a, b):
        x = []
        for i in range(len(result)):
            if a[i] == result[i] or b[i] == result[i]:
                x.append(True)
            else:
                x.append(False)
        return all(x)
            
    return sum([1 for com in combinations(inputArray, 2) if possible(com[0], com[1])]) 


def reduceString(iS):
    while True:

        if len(iS) == 0 or len(iS) == 1:
            return ""
        if len(iS) >= 2:
            if (iS[-1] == iS[0]):
                iS = iS[1:-1]
            else:
                return iS

    # Solution
    # while s and s[0] == s[-1]:
    #     s = s[1:-1]
    # return s


def minimalNumberOfCoins(coins, price):
    #go backward through array and count coins used

    count = 0
    
    while price > 0:
        for i in range(len(coins) - 1, -1, -1):
            p = price // coins[i]
            count += p
            price = price - p * coins[i]

    return count


def sumOfMultiples(n, k):
    #For given n and k find the sum of all multiples of k that are not greater than n.
    return sum([k*i for i in range(1, n + 1) if k*i <= n])

# Prime factors - mine worked, but this solution was faster for 1/29 test cases.
# I buess its faster to use eval(dir()[0])
n, = eval(dir()[0])
i = 2
r = []

while i * i < n:
    j = 1
    while n % i < 1:
        r += [i] * j
        j = 0
        n /= i
    i += i % 2 + 1

return r + [n] * (n > 1)


def neighbouringElements(a):
    # Not working yet
    #Two elements of a matrix are considered neighboring if their indices are equal on one axis and DIFFER BY ONE on the other axis.
    
    # set of sets unordered
    s = {}
    print(s)
    
    count = 0
    
    # count row elems that are same
    for i in range(len(a)):
        for j in range(len(a[i])):
            try:
                print(i, j, 'and', i, j+1, 'have valueS:', a[i][j], a[i][j+1])
                if a[i][j] == a[i][j+1]:
                    print('are equal')
                    count += 1
            except:
                print('error')
            try:
                print(j, i, 'and', j+1, i, 'have valueS:', a[j][i], a[j+1][i])
                if a[j][i] == a[j+1][i]:
                    print('are equal')
                    count += 1
            except:
                print('error')
                
    return count
                
def extractEachKth(inputArray, k):
    if k < 2:
        return []
    i = k - 1
    while i < len(inputArray):
        inputArray.pop(i)
        i += k - 1
        
    return inputArray

#looked up answer for this
    s=eval(dir()[0])[0]
    q=1
    while s >= q:
        s-=q
        q+=1
    return q-1


def sumOfSquares(n):
    
    return sum([i**2 for i in range(1, n+1)])

def add(param1, param2):
    return param1 + param2

def countWaysToChangeDigit(v):
            
    return sum([9 - int(str(v)[i]) for i in range(len(str(v))) if int(str(v)[:i] + str((9 - int(str(v)[i])) + int(str(v)[i])) + str(v)[i+1:]) > v ])


def lateRide(n):
    
    ans = [0, 0, 0, 0]
    
    hr = int(n) // 60
    mn = int(n) % 60
    
    if hr > 9:
        ans[0] = hr // 10
    ans[1] = hr % 10
    
    if mn > 9:
        ans[2] = mn // 10
    ans[3] = mn % 10
    
    return sum(ans)


def splitAddress(address):
    s = address.split('://')    
    w1, w2 = None, None
    w0 = s[0]
    
    if len(s) > 1:
        s2 = s[1].split('.com')        
        w1 = s2[0]
        
        if len(s2) > 1:
            w2 = s2[1][1:]
            if w2 != "":
                return [w0, w1, w2]
    return [w0, w1]  


def circleOfNumbers(n, firstNumber):
    
    return (firstNumber + (n // 2)) % n







def areSimilarNumbers(a, b, d):

    return (a % d == 0 and b % d == 0) or (a % d != 0 and b % d != 0)


def isSumOfConsecutive(n):
    ## THis was hard!!!
    # False - 1, 8, 128, 256 
    # True - 9, 42, 45, 55, 400
    # 2*i + 1      # 1
    # 3*i + 3      # 1 + 2
    # 4*i + 5      # 1 + 2 + 3
    # 5*i + 10     # 1 + 2 + 3 + 4
    # 6*i + 15     # 1 + 2 + 3 + 4 + 5

    for i in range(1, n // 2 + 1): 
        j, m, b = 2, 2, 1
        while j < n // 2:            
            if m * i + b == n:
                return True
            b += j
            m += 1
            j += 1

    return False
























