

p1_pos = 3
p2_pos = 5

def die_roll(i):
    sum = i*3 + 3
    if (i == 100):
        sum -= 200
    if (i == 99):
        sum -= 100
    return sum

def update_pos(pos,die_Sum):
    new_pos = (pos+die_Sum)%10 
    if new_pos == 0:
        new_pos = 10
    return new_pos

win = False
p1_score = 0
p2_score = 0
turn = 0
p1_turn = True
j = 1
while(not win):
    for i in range(j,101,3):
        die_sum = die_roll(i)
        turn +=3
        if p1_turn:
            p1_turn = False
            p1_pos = update_pos(p1_pos,die_sum)
            print("{},{}".format(p1_pos,die_sum))
            p1_score += p1_pos
        else:
            p1_turn = True
            p2_pos = update_pos(p2_pos,die_sum)
            p2_score += p2_pos
        if p1_score > 999 or p2_score > 999:
            win = True
            break
        j = (i+3)-100

result = (p1_score*turn) if p1_score<p2_score else (p2_score*turn) 
print(result)

