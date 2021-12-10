def reader(filename):
    data = []
    with open(filename,"r") as file:
        for line in file:
            line = line.strip()
            data.append(line)
    
    return data


def splits(lines : list):
    corrupt_lines = []
    ok_lines = []
    symbol = []    
    grammar = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}
    for line in lines:
        out_stack = []
        line_ok = True
        for ch in line:
            if ch in [")","]","}",">"]:
                while(True):
                    c = out_stack.pop()
                    if c == grammar[ch]:
                        break
                    else:
                        corrupt_lines.append(line)
                        line_ok = False
                        symbol.append(ch)
                        break
            else:
                out_stack.append(ch)
            
            if line_ok !=  True:
                break
        if line_ok:
            ok_lines.append(line)
        
    return symbol,corrupt_lines,ok_lines

lines = reader("10_input.txt")

symbol,corrupt_lines,ok_lines = splits(lines)

error_score = { ")": 3, "]" : 57, "}" : 1197, ">" : 25137}

result = sum([ error_score[x] for x in symbol])
print(result)

def completion(lines : list):

    out_scores = []
    grammar = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}
    scores_dict = {"(": 1, "[" : 2, "{" : 3, "<" : 4} 
    for line in lines:
        out_stack = []
        score = 0
        for ch in line:
            if ch in [")","]","}",">"]:
                while(True):
                    c = out_stack.pop()
                    if c == grammar[ch]:
                        break
            else:
                out_stack.append(ch)

        for ch in reversed(out_stack):
            score *= 5
            score += scores_dict[ch]
        out_scores.append(score)
    return(out_scores)

scores = completion(ok_lines)
scores.sort()

print(scores[len(scores)//2])


