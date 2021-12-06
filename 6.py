


from os import read


def reader(filename):

    data = []
    to_int  = lambda x : int(x)
    with open(filename,"r") as file:
        for line in file:

            data.extend([to_int(x) for x in line.strip().split(",")])
    return data


fish = reader("6_input.txt")

# this works for part 1 and is good eneough for part tw othis will explode in memory so we change tactics

# for i in range(1,81):
#     new_fish = []
#     for idx, age in enumerate(fish):
#         if age == 0:
#             fish[idx] = 6
#             new_fish.append(8)
#         else:
#             fish[idx] -= 1
#     fish.extend(new_fish)

# print(len(fish))

# part b now we just store the 8 spots and move the populations between them. to test the previous ans is 372984

population = [0,0,0,0,0,0,0,0,0]
for age in fish:
    population[age] += 1

for i in range(1,257):
    new_fish = 0
    reset_fish = 0
    for idx, pop in enumerate(population):
        if idx == 0:
            new_fish = pop
            reset_fish = pop
        #swap populations
        else:
            population[idx-1] = population[idx] 
    population[6] += reset_fish
    #because all the fish would move to number 7 and the new fish do not count in this.
    population[8] = new_fish

print(sum(population))