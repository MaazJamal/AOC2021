
import re

def reader(filename):
    with open(filename,"r") as file:
        line = file.readlines()
        data = [re.split(r'[[\]]',l.strip()) for l in line]
    return data
        

number = reader("18_input.txt")
a = 0


