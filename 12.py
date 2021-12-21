
def reader(filename :str):
    data = []
    with open(filename,"r") as file:
        for line in file:
            data.append(line.strip().split("-"))

    return data

links = reader("12_input.txt")

def valid_paths(links)
