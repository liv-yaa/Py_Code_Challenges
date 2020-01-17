def customSort(arr):
    # Write your code here
    dic = {a: arr.count(a) for a in arr}

    print(dic)


out = []
    for i in range(1, len(arr)):
        c = [j for j in arr if arr.count(j) == i]
        c.sort()
        out.extend(c)
    
    for o in out:
        print(o)
