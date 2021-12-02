
with open("2_input.txt",'r') as file:
    
    data = [line.strip() for line in file]
    depth = 0
    hori = 0
    # part a
    for movement in data:
        movement_split = movement.split(" ")
        if movement_split[0] == "forward":
            hori += int(movement_split[1])
        else:
            if movement_split[0] == "up":
                depth -= int(movement_split[1])
            else:
                depth += int(movement_split[1])

    print(depth*hori)
    file.close()

    #part b 
  

    aim = 0
    depth = 0
    hori = 0
    for movement in data:
            movement_split = movement.split(" ")
            if movement_split[0] == "forward":
                value = int(movement_split[1])
                hori += value
                depth += value*aim
            else:
                if movement_split[0] == "up":
                    aim -= int(movement_split[1])
                else:
                    aim += int(movement_split[1])
    
    print(depth*hori)
