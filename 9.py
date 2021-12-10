import numpy as np

# so many 2d arrays. i should have ussed np before

def reader(filename):
    data = []
    to_int  = lambda x : int(x)
    with open(filename,"r") as file:
        for line in file:
            line = line.strip()
            data.append([to_int(x) for x in line])
    
    return data

def low_points(array : np):

    low_point = []
    idx = []
    for i in range(0,100):
        for j in range(0,100):
            num = array[i,j] 
            if array[i,j] == 9:
                continue
            one = 12 if j == 0 else array[i,j-1]
            four = 12 if i == 0 else array[i-1,j]
            two = 12 if j == 99 else array[i,j+1]
            three = 12 if i == 99 else array[i+1,j]
            if num in [one,two,three,four]:
                continue
            if num == min([num,one,two,three,four]):
                low_point.append(num)
                idx.append[(i,j)]
    
    return low_point,idx




a,loc = np.array(reader("9_input.txt"))

points = low_points(a)
risk = [p+1 for p in points]
print(sum(risk))

def basin(array : np, loc : list):
    return

    