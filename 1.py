
with open("input.txt",'r') as file:
    
    data = [int(line.strip()) for line in file]
    
    # part a
    prev = sum(data[0:3])
    total = 0
    for depth in data[1:]:
        if depth>prev:
            total +=1
        prev = depth
    print(total)
    file.close()

    #part b sum of threes this can probably be turned into a function but ¯\_(ツ)_/¯
    prev = sum(data[0:3])
    limit = len(data)
    total = 0
    for idx,_ in enumerate(data[1:limit-1]):
        average = sum(data[idx:idx+3])
        if average>prev:
            total +=1
        prev = average
    print(total)
    


