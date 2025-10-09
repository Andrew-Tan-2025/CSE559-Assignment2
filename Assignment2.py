import os
import numpy as np
from pathlib import Path

def PatternMatch(fileName):
    retList = []
    numComparisons = 0
    numMatches = 0
    numMismatches = 0

    # read both strings from file
    sourceString = ""
    patternString = ""
    # fileDir = "samples\\"+fileName
    if os.path.exists(fileName):
        f = open(fileName, "r")
        sourceString = f.readline()[0: len(sourceString)-1]
        patternString = f.readline()[0: len(patternString)-1]
        f.close()
    else:
        print(f"Error: The file was not found.")

    # Z algorithm implementation
    sourceString = patternString + "$" + sourceString
    Z = [0] * len(sourceString)
    index = 0 #placeholder for template matching index
    i = 1
    
    while i < len(sourceString):
        # print(i)
        while ( (i+index)<len(sourceString)):
            numComparisons += 1
            if ( sourceString[index]==sourceString[i + index] ):
                index += 1
                numMatches += 1
            else:
                break
            # print(i-index)
        
        # reset and increment
        Z[i] = index
        if index == len(patternString):
            retList.append(i - index)
            # print(i-index)
        
        if index > 1:
            for j in range(i+1, i+index):
                Z[j] = Z[j-i]
            i += index
        else:
            i += 1
        index = 0

    numMismatches = numComparisons - numMatches

    # Store solution into file
    # '''
    outFile = "solutions\\sol_"+fileName.split("_", 1)[1]
    if os.path.exists(outFile):
        os.remove(outFile)
    with open(outFile, "x") as f:
        # write data into file
        for i in retList:
            f.write(str(i) + "\n")
        f.write("Number of Comparisons: " + str(numComparisons) + "\n")
        f.write("Number of matches: " + str(numMatches) + "\n")
        f.write("Number of mismatches: " + str(numMismatches) + "\n")
    
    
    '''
    print("\n")
    print("Number of Comparisons: ", numComparisons)
    print("Number of matches: ",numMatches)
    print("Number of mismatches: ", numMismatches) 
    # '''
    
    return 0

def main():
    print("Please enter the name of the file to test (ex: sample_0, sample_1, etc.): ")
    # Take input from user, after asking what file to use
    fileName = "samples\\" + input()
    #fileTest = "examples\\ex_0" # name for examples test files
    #test = "test.txt" # name for test file
    result = PatternMatch(fileName)
    return 0

if __name__ == "__main__":
    main()