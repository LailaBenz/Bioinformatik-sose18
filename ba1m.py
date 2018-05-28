# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:17:23 2018

@author: User
"""
#translate numbers back into genetic code, else as safety
def NumberToSymbol(index):
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
    else:
        return ' '

#define function
def NumberToPattern(index, k):
    if k==1:
        return NumberToSymbol(index)
    
    #recursive function, devide index with integer division, add NumberToSymbol from the remainder of the quotient
    return NumberToPattern(index // 4, k-1) + NumberToSymbol(index % 4)

"""
#for testing
index = 5353
k = 7

print(NumberToPattern(index, k))
"""

