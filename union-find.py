"""There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces."""
# from collections import defaultdict
# #cities = [[1,1,0,0],[1,1,1,1],[0,1,1,0],[0,1,0,1]]
# cities = [[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = defaultdict(list)
#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#     def find_parent(self,connected,i):
#         #print(connected)
#         if connected[i] == -1:
#             return i
#         if connected[i] != -1:
#             return self.find_parent(connected,i)
#     def union(self,parent,x,y):
#         parent[x] = y
# g = Graph(len(cities))
# b = [list(enumerate(i)) for i in cities]
# print(b)
# arr = []
# for row in range(0,len(b)):
#     for col in range(0,len(b[0])):
#         if b[row][col][1] == 1:
#             arr.append(b[row][col][0])
#     arr.append('break')
# print(arr)
# for i in range(len(arr)-1):
#     ##rint(type(arr[0]), "hellooo", arr[1], g.graph[0])
#     if arr[i] == int and arr[i+1] == 'break' and g.graph[i] != None:
#         g.addEdge(arr[i],None)
#     print(type(arr[i]),type(arr[i+1]),g.graph[i],arr[i+1], g.graph[i] != arr[i+1])
#     if arr[i] == int and arr[i+1] == int and g.graph[i] != arr[i+1]:
#         print('HELLOO')
#         g.addEdge(arr[i],arr[i+1])

# print(g.graph)
# # count = 0
# # for i in range(0,g.V):
# #     if g.graph[i] == []:
# #         count+=1
# #print(count)



    
class UnionFind(object):
    def __init__(self,n):
        self.V = list(range(n))
    def union(self, a, b):
        tempa,tempb = self.find(a), self.find(b) #compare ends of graphs
        if tempa != tempb:               #if ends are different, set one end to the next end.
            self.V[tempa] = tempb
    def find(self, a): #update a to current stored value at index a
        while self.V[a] != a:
            a = self.V[a]
        return a
class Solution(object):
    def findCircleNum(self,M):
        if not M:
            return 0
        n = len(M)
        obj = UnionFind(n)
        print(obj.V)
        for r in range(n):
            for c in range(r,n):
                if M[r][c] == 1: # 0000 0123 | 111 123 | 22 23 | 3 3
                    obj.union(r,c)
                    print(obj.V)
        print([obj.find(i) for i in range(n)])
        return len(set([obj.find(i) for i in range(n)]))
        
#[[1,1,0,0],[1,1,1,1],[0,1,1,0],[0,1,0,1]]
# #[[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# a = []
# b = []
# s = [[1,1,0,0],[1,1,1,1],[0,1,1,0],[0,1,0,1]]
# for r in range(len(s)):
#     for c in range(r,len(s)):
#         print(r,c)
#         a.append(s[r][c])
# print("end")
# for row in range(len(s)):
#     for col in range(len(s[0])):
#         print(row,col)
#         b.append(s[row][col])
        
# print(a)
# print(b)


# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 2, 2, 3]
# [0, 2, 2, 3]
# [0, 2, 2, 3]
# [0, 2, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [1, 1, 2, 3]
# [1, 1, 2, 3]
# [1, 2, 2, 3]
# [1, 2, 3, 3]
# [1, 2, 3, 3]
# [1, 2, 3, 3]
# [3, 3, 3, 3]
# 3
# 1        
