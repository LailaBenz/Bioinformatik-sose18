# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:16:48 2018

@author: User
"""

#translate genetic code into quatary numbers, else as safety
def SymbolToNumber(x):
    if x == 'A':
        return 0
    elif x == 'C':
        return 1
    elif x == 'G':
        return 2
    elif x == 'T':
        return 3
    else:
        return " "

#define function
def PatternToNumber(pattern):
    #when no input, return 0
    if pattern=="":
        return 0
    #symbol is last character of pattern       
    symbol = pattern[-1]    
    #remaining part of pattern (pattern without symbol)   
    prefix = pattern[0:-1]
     #recursive function, multiply remaining part of pattern by 4 for the the position (4^0, 4^1, 4^2, etc) 
     #add quatary number of last symbol of pattern
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)
"""
pattern = "CTTCTCACGTACAACAAAATC"
print(PatternToNumber(pattern))
"""