import numpy as np

data = np.genfromtxt("11_input.txt", delimiter=1,dtype=int)

def sim(octo : np,all_flash = False):
    octo = np.pad(octo, 1 ,mode= "constant", constant_values =1000)
    total_flashes = 0
    all_flash_iter = 0
    while(all_flash_iter <100 or all_flash):
        octo +=1
        nines = []
        done = []
        for i in range(1,11):
            for j in range(1,11):
               if octo[i,j] > 9:
                   nines.append((i,j))
                   octo[i,j] = -999
                   
        
        while(nines):
            i,j = nines.pop()
            done.append((i,j))
            octo[i-1:i+2,j-1:j+2] +=1
            for x in range(i-1,i+2):
                if x == 0 or x == 11:
                    continue
                for y in range(j-1,j+2):
                    if y == 0 or y ==11:
                        continue
                    if octo[x,y] > 9:
                        nines.append((x,y))
                        octo[x,y] = -999
                        
        if all_flash:
            if len(done) == 100:
                return all_flash_iter
        while(done):
            i,j = done.pop()
            octo[i,j] = 0
            total_flashes += 1

        all_flash_iter += 1





    return total_flashes


total = sim(data)
print(total)

print(sim(data,True))