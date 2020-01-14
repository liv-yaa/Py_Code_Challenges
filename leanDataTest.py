# leanDataTest.py
# https://www.hackerrank.com/tests/890mt9pn1qj/login?b=eyJ1c2VybmFtZSI6Im9saXZpYS5mLnNtaXRoQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiOGU3YzU0MDMiLCJoaWRlIjp0cnVlLCJhY2NvbW1vZGF0aW9ucyI6bnVsbH0=


def calculateMostImprovement(students, scores):
    # Write your code here
    # del = 0
    dic = dict()
    if len(students) == len(scores):
        for i in range(len(scores)):
            # print(students[i], scores[i])
            
            if students[i] not in dic:
                dic[student[i]] = [scores[i]]
                
    print(dic)



print(calculateMostImprovement(['Mary', 'Steve', 'Steve', 'Mary', 'Steve'], [19, 70, 99, 80, 100])





def calculateMostImprovement(students, scores):
    dic = dict()
    d = defaultdict(list)
    print('d', d)
    max_improvement = 0
    if len(students) == len(scores):
        for i in range(len(scores)):
            d[students[i]].append(scores[i])
            # if students[i] not in dic:
            #     dic[students[i]] = [scores[i]]
            # else:
            #     v = dic[students[i]].append(scores[i])
    
    # for k, v in dic.items():
    #     max_delt = 0
    #     for i in range(len(v)):
    #         for j in range(i + 1, len(v)):
    #             d = v[j] - v[i]
    #             if d > max_delt:
    #                 max_delt = d 
    #     if max_delt > max_improvement:
    #         max_improvement = max_delt
    return d








































































































































































































