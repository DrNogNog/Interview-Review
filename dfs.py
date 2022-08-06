country_map = [
    [0, 1, 0],
    [1, 1, 1], 
    [0, 1, 0]
] # there are 3 countries

def get_num_country(map_grid) -> int:
    queue = []
    out_of_bounds_row = len(map_grid)
    out_of_bounds_col = len(map_grid[0])
    for row in range(len(map_grid)):
        for col in range(len(map_grid[0])):
            # if (row-1 < 0) or (col-1 < 0) or (row+1 >= out_of_bounds_row) or ((col+1 >= out_of_bounds_col)):
            #     continue
            # if map_grid[row][col] == 1:
            #     elif map_grid[row][col-1] == 1:
                
            #     elif map_grid[row][col-1] == 1:
                        
            #     elif map_grid[row][col-1] == 1:
                
            #     elif map_grid[row][col-1] == 1:
            # check top valid
            queue.append(# top indices)
            # check bottom valid
            queue.append(# bottom indices)
            # check left valid
            queue.append(# left indices)
            # check right valid
            queue.append(# right indices)
            get_num_country()
            
            queue.pop(# top indices)
            # check bottom valid
            queue.pop(# bottom indices)
            # check left valid
            queue.pop(# left indices)
            # check right valid
            queue.pop(# right indices)
            
    
    