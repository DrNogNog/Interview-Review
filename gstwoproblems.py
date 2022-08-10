import re
'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor. 

Sample input and output:

hasCommonAncestor(pairs, 3, 8)   => false
hasCommonAncestor(pairs, 5, 8)   => true
hasCommonAncestor(pairs, 6, 8)   => true
hasCommonAncestor(pairs, 6, 9)   => true
hasCommonAncestor(pairs, 1, 3)   => false
hasCommonAncestor(pairs, 3, 1)   => false
hasCommonAncestor(pairs, 7, 11)  => true
hasCommonAncestor(pairs, 6, 5)   => true
hasCommonAncestor(pairs, 5, 6)   => true
hasCommonAncestor(pairs, 3, 6)   => true
hasCommonAncestor(pairs, 21, 11) => true

n: number of pairs in the input

'''
import time
pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]
from collections import defaultdict
def hasCommonAncestor(pairs,a,b):
    dictionary = defaultdict(set)
    for i in pairs:
        dictionary[i[1]].add(i[0])
    print(dictionary)
    stacka = []
    visiteda = set()
    stackb = []
    visitedb = set()
    stacka.append(a)
    #print(stacka,"start")
    #print(dictionary[stacka[0]])
    while stacka:
        a = stacka[-1]
        #print(a,"stack top")
        stacka.pop()
        #time.sleep(2)
        visiteda.add(a)
        for i in dictionary[a]:
            stacka.append(i)
        #visiteda.pop()
    stackb.append(b)
    while stackb:
        b = stackb[-1]
        stackb.pop()
        visitedb.add(b)
        for i in dictionary[b]:
            stackb.append(i)
    visiteda.remove(a)
    visitedb.remove(b)
    x = visiteda.intersection(visitedb)

    print(visiteda,visitedb)
        #print(stacka,"hell")
    #print(visiteda)
    # for i in dictionary[a]:
    #     visiteda.append(i)
    # while visiteda:
    #     visiteda.extend(dictionary[])
    #     time.sleep(2)
    #     print(visiteda)
    return bool(x)
#hasCommonAncestor(pairs,6,8)    
print(hasCommonAncestor(pairs, 1, 3))
bing = """
hasCommonAncestor(pairs, 3, 8)   => false
hasCommonAncestor(pairs, 5, 8)   => true
hasCommonAncestor(pairs, 6, 8)   => true
hasCommonAncestor(pairs, 6, 9)   => true
hasCommonAncestor(pairs, 1, 3)   => false
hasCommonAncestor(pairs, 3, 1)   => false
hasCommonAncestor(pairs, 7, 11)  => true
hasCommonAncestor(pairs, 6, 5)   => true
hasCommonAncestor(pairs, 5, 6)   => true
hasCommonAncestor(pairs, 3, 6)   => true
hasCommonAncestor(pairs, 21, 11) => true"""

# arr = re.split(' => true\n| => false\n|\n| => true',bing)
# arr = arr[1:]
# arr = arr[0:len(arr)-1]
# [i.strip() for i in arr]
# ans = [eval(arr[i]) for i in range(len(arr))]
# #print(eval(arr[2]))
# print(ans)



# # child, parents
# from collections import defaultdict
# def solution(pairs):
#     dictionary = defaultdict(list)
#     zero_p = []
#     one_p = []
#     for i in pairs:
#         lst = i[0]
#         dictionary[i[1]].append(lst)
#     for i in pairs:
#         #print(i)
#         if i[0] not in dictionary:
#             zero_p.append(i[0])
#     #print(set(zero_p))
#     for i in dictionary.keys():
#         #print(i)
#         if len(dictionary[i]) == 1:
#             one_p.append(i)
#         #print(one_p)
#     return(set(zero_p),set(one_p))

import re
import pprint
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if not M: return 0
        s = len(M)
        print(s,"s: len(n)")
        seen = set()
        print(seen)
        
        def dfs(p):
            print(f"start dfs{p}")
            for q, adj in enumerate(M[p]):
                print(f"q:{q}, adj: {adj}, e: {M[p]}")
                if (q not in seen) and (adj == 1):
                    print(f"{q} not in set {seen} and {adj} == 1")
                    seen.add(q)
                    print(f"added number to {seen} in dfs")
                    dfs(q)
        
        cnt = 0
        for i in range(s):
            print(f"for {i} in range({s})")
            if i not in seen: 
                print(f"if {i} not in set: {seen}" )
                dfs(i)
                print("end dfs")
                cnt += 1
                print(f"{cnt} after + = 1")
        return cnt
