def reader(filename):

    lines = []
    with open(filename,"r") as file:
        data = [line.strip() for line in file]
        mid_break = lambda x: x.split(" -> ")
        raw_coordinate = [mid_break(x) for x in data]
        processed_coordinate = []
        for coordinate in raw_coordinate:
            x,y = coordinate[0].split(","),coordinate[1].split(",")
            processed_coordinate.append(([int(x[0]),int(x[1])],[int(y[0]),int(y[1])]))
        return processed_coordinate
    
# y1 x1,x2,x3,x4
# y2
# y3   
# y4 
# part a 
def get_line(coordinate):
    x1,y1 = coordinate[0]
    x2,y2 = coordinate[1]
    idx = []
    line_found = False
    if x1 == x2 :
        line_found = True
        if y1 < y2:
            small = y1
            large = y2
        else:
            small = y2
            large = y1
        
        for i in range(small,large+1):
            idx.append((1000*i)+x1)

    elif y1 == y2:
        line_found = True
        if x1 < x2:
            small = x1
            large = x2
        else:
            small = x2
            large = x1
        for i in range(small,large+1):
            idx.append((1000*y1)+i)

    if line_found:
        return idx
    else:
        return False

board = {}.fromkeys(list(range(0,1000000)))
lines = reader("5_input.txt")

for line in lines:
    idx = get_line(line)
    if idx:
        for id in idx:
            if board[id] == None:
                board[id] = 1
            else:
                board[id] += 1

overlap_points = 0
for key,value in board.items():
    if value != None:
        if value > 1:
            overlap_points += 1

print(overlap_points)

#maths 45 degree diagnals have sides equal to each other. if you draw a trianglw.
def diagnals(coordinate):


    x1,y1 = coordinate[0]
    x2,y2 = coordinate[1]
    idx = []
    line_found = False
    if x1 != x2 and y1 != y2 :
        
        line_found = True
        # This isnt 
        # if y1 < y2:
        #     y_small = y1
        #     y_large = y2
        # else:
        #     y_small = y2
        #     y_large = y1

        # if x1 < x2:
        #     x_small = x1
        #     x_large = x2
        # else:
        #     x_small = x2
        #     x_large = x1
        
        direction = 1
        # multiplied later to change the step direction
        if x1 < x2:
            direction = 1
        else:
            direction = -1
     # every other point on the line is one down and left or right from previous point depending on direction. because 45 degrees.
        if y1 < y2:
            for i,j in enumerate(range(y1,y2+1)):
                idx.append((1000*j)+(i*direction))
        else:
            for i,j in enumerate(range(y2,y1+1)):
                idx.append((1000*j)+(i*direction))            

    if line_found:
        return idx
    else:
        return False

for line in lines:
    idx = diagnals(line)
    if idx:
        for id in idx:
            if board[id] == None:
                board[id] = 1
            else:
                board[id] += 1

overlap_points = 0
for key,value in board.items():
    if value != None:
        if value > 1:
            overlap_points += 1

print(overlap_points)