
from os import read
import numpy as np


def reader(filename):

    with open(filename,"r") as file:
        fold = []
        coor = []
        for line in file:

            if line == "\n":
                continue
            if "fold" in line:
                line = line.strip().split(" ")
                fold.append(line[-1].split("="))
                fold[-1][1] = int(fold[-1][1])
            
            else:
                xy = line.strip().split(",")
                coor.append((int(xy[0]),int(xy[1])))
    
    return coor,fold

coor, fold_ins = reader("13_input.txt")

board = np.zeros((895,1311))

for x,y in coor:
    board[y,x] = 1



def fold(instruction : list, board : np):

    if instruction[0] == "x":
        axis = instruction[1] 

        lower_half = np.fliplr((board[:,:axis]))
        length = board.shape[1]
        padd = length - axis 
        n_padd = ((0,0),(0,padd))
        lower_half = np.pad(lower_half,pad_width=n_padd, constant_values=(0,))
            
        result = board+lower_half
        result = result[:,:axis-1]
        return result


overlap = fold(fold_ins[0], board)
total = 0
print(np.count_nonzero(overlap))
