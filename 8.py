
import difflib
def reader(filename):
    data = []
    with open(filename,"r") as file:
        for line in file:
            temp = line.strip().split(" | ")
            a = temp[0].split(" ")
            b = temp[1].split(" ")
            data.append((a,b))
    return data

data = reader("8_input.txt")
unique_digits = 0
# 2, 4, 3, 7
for _,output in data:
    value = []
    value = [len(x) for x in output if len(x) in [2,3,4,7]]
    unique_digits += len(value)

print(unique_digits)


def patterns(raw : list):

    raw = ["".join(sorted(x)) for x in raw]
    raw.sort(key=lambda val: len(val) )
    two,seven,four,eight = raw[0],raw[1],raw[2],raw[9]
    a = list(difflib.ndiff(two,seven))[0][-1]
    
# digit : segments
# by convnetion my segments are:
#   aaaa    
#  b    c  
#  b    c 
#   dddd    
#  e    f  
#  e    f  
#   gggg   
#
# 1 : 2 c f 
# 7 : 3 a c f
# 4 : 4 b c d f
# 8 : 7 a b c d e f g
# 2 : 5 a c d f g 
# 3 : 5 a c d f g 
# 5 : 5 a b d f g
# 6 : 6 a b d e f g 
# 9 : 6 a b c d f g
# 0 : 6 a b c e f g
    return

for wires,output in data:
    patterns(wires)
    unique_digits += len(value)


