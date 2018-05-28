#function to write DNA-String into Numbers
def PatternToNumber(pattern):
    if pattern=="":
        return 0
    #symbol is last character of pattern     
    symbol = pattern[-1]    
    #remaining part of pattern  
    prefix = pattern[0:-1]
    #recursive function  
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

#translate genetic code into quatary numbers, else as safety
def SymbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

#for testing
text = "ACGCGGCTCTGAAA"
k = 2

#initialize an array with the length of 4^k
patternFrequencies = [0] * 4**k

#loop over the text to find pattern, write into array
for i in range(len(text)-k+1):
	pattern = text[i:i+k]
	j = PatternToNumber(pattern)
	patternFrequencies[j] = patternFrequencies[j] + 1

#
p = ""
for i in patternFrequencies:
	p += str(i) + " "

print(p)
