country_map = [
    [0, 0, 0],
    [1, 0, 1], 
    [0, 1, 0]
] # there are 3 countries

import numpy as np

def solver(m):
    counts=0
    _copy =  np.copy(country_map)
    for y in enumerate(_copy):
        for x in enumerate(y):
            if _copy[x][y] ==1:
                counts+=1
                DFS(x,y)

    
    def DFS(x,y):
        if country_map[x+1][y] == 1:
            _copy[x+1][y]=0
            DFS(x+1,y)
        else:
            return
        if country_map[x][y+1] == 1:
            _copy[x][y+1]=0
            DFS(x,y+1)
        else:
            return
        if country_map[x-1][y] == 1:
            _copy[x-1][y]=0
            DFS(x-1,y)
        else:
            return
        if country_map[x][y-1] == 1:
            _copy[x][y-1]=0
            DFS(x,y-1)
        else:
            return
    
    return counts

print(solver(country_map))