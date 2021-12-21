import numpy as np

cave = np.genfromtxt("15_input.txt" , dtype=int, delimiter=1)

def min_route(map : np):
    last_x,last_y = 0,0
    # map = np.pad(map,pad_width=(1,),constant_values=99)

    i,j = map.shape
    i -= 1
    j -= 1
    score = map[i,j] - map[last_x,last_y] 

    while( i != last_x or  j != last_y):

        if i != 0:
            min_x = map[i-1,j]
        else:
            min_x = 99
        if j != 0:
            min_y = map[i,j-1]
        else:
            min_y = 99

        if min_x < min_y:
            i = i-1
        else:
            j = j-1
        score += map[i,j]
        print(i,j)
    return score


min_faf = min_route(cave)

print(min_faf)