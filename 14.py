

def reader(filename):


    with open(filename,"r") as file:
        lines = file.readlines()
        sequence = lines[0].strip()
        seq_dict = {}
        for line in lines[2:]:
            two = line.split("->")
            key,value = two[0].strip(),two[1].strip()
            seq_dict[key] = value
    
    return seq_dict,sequence


seq_dict, sequence = reader("14_input.txt")

def sequence_split(sequence):

    pairs = []
    for i in range(len(sequence)-1):
        pairs.append(sequence[i]+sequence[i+1])
    
    return pairs

for step in range(0,40):

    pairs = sequence_split(sequence)
    new_str = []
    for i in range(0,len(pairs)):
        new_str.append(sequence[i])
        new_str.append(seq_dict[pairs[i]])
    
    new_str.append(sequence[-1])
    sequence = "".join(new_str)

alpha = [0]*25
for c in sequence:
    idx = ord(c) -ord("A")
    alpha[idx] += 1
imlazy = []
for i in alpha:
    if i == 0:
        continue
    else:
        imlazy.append(i)

print(max(imlazy)-min(imlazy))
