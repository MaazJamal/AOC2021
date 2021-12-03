from collections import defaultdict
from os import truncate


with open("3_input.txt",'r') as file:
    
    data = [line.strip() for line in file]
    raw_dict = {}
    raw_dict = defaultdict(lambda:[0,0], raw_dict)
    # part a
    for bytes in data:
        for idx,bit in enumerate(bytes):

            if bit == "0":
                raw_dict[idx][0] += 1
            else:
                raw_dict[idx][1] += 1

    #since python 3.7 all dics are orederd so we start with 0 

    gamma = 0
    epsilon = 0 

    ideal_oxygen = "" # for part b this number matches the criteria completeley 
    ideal_co2 = "" # for part b

    # value[0] is the number of 0 bits and value[1] is the number of 1 bits 
    for key,value in raw_dict.items():

        #if less 0's than 1's

        if value[0] < value[1]:
            gamma |= 1
            ideal_oxygen += "1"
            ideal_co2 += "0"

        #if more 0's than 1's
        else:
            epsilon |= 1 
            ideal_oxygen += "0"
            ideal_co2 += "1"
        
        epsilon <<= 1
        gamma <<= 1
    
    epsilon >>= 1
    gamma >>= 1
    
    print(gamma*epsilon)
    file.close()

    #part b 

    max_bits_matched_oxygen = 0
    max_bits_matched_co2 = 0
    most_matched_oxygen = ""
    most_matched_co2 = ""

    for byte in data:
        cur_bits_matched_oxygen = 0
        cur_bits_matched_co2 = 0
        conseucutive_bit_oxy = True
        conseucutive_bit_co2 = True
        for idx,bit in enumerate(byte):

            if ideal_oxygen[idx] == bit and conseucutive_bit_oxy:
                cur_bits_matched_oxygen +=1
            else:
                conseucutive_bit_oxy = False
            
            if ideal_co2[idx] == bit and conseucutive_bit_co2:
                cur_bits_matched_co2 +=1
            else:
                conseucutive_bit_co2 = False
            
            if conseucutive_bit_co2 == False and conseucutive_bit_oxy == False:
                break
        
        if max_bits_matched_co2 < cur_bits_matched_co2:
            most_matched_co2 = byte
            max_bits_matched_co2 = cur_bits_matched_co2

        if max_bits_matched_oxygen < cur_bits_matched_oxygen:
            most_matched_oxygen = byte
            max_bits_matched_oxygen = cur_bits_matched_oxygen
    
    oxygen = 0
    co2 = 0
    for idx, bit in enumerate(most_matched_oxygen):
        oxygen |= int(bit)
        co2 |= int(most_matched_co2[idx])
        oxygen <<=1
        co2 <<=1
    
    oxygen >>=1
    co2 >>=1

    print(oxygen*co2)




  

