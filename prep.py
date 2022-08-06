from collections import defaultdict
from collections import deque as que
f = dict(five=5,three=3,one=1,two=2,z=4)
e = dict ([('string',['two',2])])
#print(e)
print(max(f))
print(f)
x = defaultdict(list)
x['two'].append('hwo')
print(x['apple'])
print(x)
maker = que([])
maker.append(('a',0))
print(maker.popleft)
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
def BFS(self, s):
    visited = [False] * (max(self.graph) + 1)
    queue = que([])
    queue.append(s)
    visited[s] = True
    while queue:
        #dequeue a vertex from queue and print it
        s = queue.pop(0) 
        #removes first element, all items get shifted up making it O(n)
        print(s)
        # this loops one time and goes back to the while loop
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

