def PatternCount(text, pattern):
    result = 0
    for i in range(0, len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)] == pattern):
            result += 1
    return result
def FrequentWords(text, k=4):
    #Return a list of the most frequent substrings in a given text.
    # import previosly written programs to get SymbolToNumber, PatternToNumber, NumberToSymbol and NumberToPattern
    import ba1m
    import ba1l
    
    # Create an array for all patterns, initialize by size 4^k  
    allPatternsWithCount = [0]*(4**k)
    # A list to store the final result
    result = []
    # Loop over the whole text moving forward one letter at a time
    for i in range(0, len(text)-k):
        # pattern is a small part of the text (with length k)
        pattern = text[i:i+k]        
        # Add one to the counter of this pattern
        allPatternsWithCount[ba1l.PatternToNumber(pattern)] += 1
         
    # After counting everything, find the maximum value
    maximum = max(allPatternsWithCount)
    #Print count of most frequent patterns
    print(maximum)
    # Loop over all patters that have been found (evtl geht das nicht bei array)
    for number, count in enumerate (allPatternsWithCount):
        # If the count for this pattern is the maximum ...
        if count == maximum:
            # Add it to the result
            result.append((number, count))
            print(ba1m.NumberToPattern(number, k),end=' ')    
    return result
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()    
# For testing
text = data[0]
#print(FrequentWords(text, int(data[1])))
FrequentWords(text, int(data[1]))



