def reader(filename):

    data = []
    to_int  = lambda x : int(x)
    with open(filename,"r") as file:
        for line in file:

            data.extend([to_int(x) for x in line.strip().split(",")])
    return data


positions = reader("7_input.txt")
# median is the most central value so we use that.and least distance from every other. 
positions.sort()
median = len(positions)//2 

fuel_used = 0
for pos in positions:
    fuel_used += abs(positions[median]-pos)

print(fuel_used)

#part b so the fuel is exponentially geowing.
# for this we can use average. because the average is the closest from every point. 

avg = sum(positions)//len(positions)

fuel_used = 0
for pos in positions:
    dist = abs(pos-avg)
    fuel_used += dist*(dist+1)//2

print(fuel_used)
