graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
#print(graph)
#undirected graph

from collections import deque

#search_queue += graph["bob"]
#print(search_queue)
#while queue isn't empty
def person_is_seller(name):
    return name[-1] == 'm'
def queue():
    search_queue = deque()
    search_queue += graph["you"] 
    ive_searched = []
    while search_queue:
        person = search_queue.popleft() #grabs first person off queue
        if not person in ive_searched:
            if person_is_seller(person):
                print   (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
    return False
# Basically O(V+E) or O(n) in array terms
print(queue())