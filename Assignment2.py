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
    Z = np.zeros(len(sourceString))
    index = 0 #placeholder for template matching index

    for i in range(1, len(sourceString)-1):
        #numComparisons += 1
        while ( (i+index)<len(sourceString) ) and ( sourceString[index]==sourceString[i + index] ):
            index += 1
            numMatches += 1

        if index == len(patternString):
            numComparisons += index
            retList.append(i - index)
            # print(i-index)
        else:
            numMismatches += 1
            numComparisons += (index+1)
        
        Z[i] = index
        index = 0

    # Store solution into file
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
    #print("Number of Comparisons: ", numComparisons)
    #print("Number of matches: ",numMatches)
    #print("Number of mismatches: ", numMismatches) 
    
    return 0

def main():
    fileName = 'samples\\sample_14' # name for samples test files
    # fileTest = 'examples\\ex_1' # name for examples test files
    result = PatternMatch(fileName)
    return 0

if __name__ == "__main__":
    main()