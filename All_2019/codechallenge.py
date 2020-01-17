def plagiarismCheck(code1, code2):

    # All occurrences of a are replaced with summand_1, and all occurrences of b are replaced with summand_2. 
    # It is possible first to replace all occurrences of b to c, then to replace all as to b, and then all occurrences of c to a.
    
    # Check code for logic
    
    # print(exec(code1))
    
#     c1 = ''.join(code1)
    
#     print(exec(c1))

    x = replaceAll('a', 'b', code1)
    
    if code2 == x:
        return True
    
    return False


        
    
def replaceAll(a, b, code1):
    # a = 'a'
    # b = 'bingo'
    newCode = []
    for item in code1:
        new = item.replace(a, b)
        print(new)
        newCode.append(new)
    return newCode








    def nearestGreater(a):
    b = [-1] * len(a)
    print(b)
    
    for i in range(len(a) - 1):
        # print(a[i])
        
        j = i
        
        # Find the nearest a[j] that is greater than a[i] such that abs(i - j) is minimizied
        v = 1
        while True:
            print('v', v)
            
            try:
                v1 = v 
                
                print(i, a[i], a[i + v])

                if a[i + 1] > a[i]:
                        b[i] = i + v
                        break
                        
                if i - v >= 0:
                    print(i, a[i], a[i - v])
                    if a[i - v] > a[i]:
                        b[i] = i - v
                        break
                    else:
                        v += 1
                        print('b', b)
            except:
                print('did not work, next v')
                v += 1
                
        print(b)
        
        
        
        
        