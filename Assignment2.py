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
    
    n = len(sourceString)
    Z = [0] * n
    index = 0
    l,r= 0,0
    i = 1 #index for sourceString

    while i < n:
        if i > r: # Case 1
            l=i
            r=i

            while ( (i+index) < n ):
                numComparisons += 1
                if ( (sourceString[index] == sourceString[i + index]) ):
                    r += 1
                    index += 1
                    Z[i] += 1
                    numMatches += 1
                else:
                    numMismatches += 1
                    break
            r-=1
        else: # Case 2
            if Z[i-l] == r-l: # Case 2-C
                index = len(patternString)
                while ( (i+index) < n ):
                    numComparisons += 1
                    if ( (sourceString[index] == sourceString[l + index]) ):
                        index += 1
                        numMatches += 1
                    else:
                        numMismatches += 1
                        break
                Z[i] = Z[i-l]
            else: # Case 2-a, 2-b
                while ( (i+index) < n ):
                    if ( (sourceString[index] == sourceString[i + index]) ):
                        index += 1
                    else:
                        Z[i] = index
                        break
                            
        # print(numComparisons," ",numMatches," ",numMismatches)
        if index == len(patternString):
                retList.append(i-index)
        index=0
        i += 1
    
    # Store solution into file
    #'''
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
    for i in retList:
        print(i)
    print("Number of Comparisons: ", numComparisons)
    print("Number of matches: ",numMatches)
    print("Number of mismatches: ", numMismatches) 
    # '''
    
    return 0

def main():
    print("Please enter the name of the file to test (ex: sample_0, sample_1, etc.): ")
    # Take input from user, after asking what file to use
    fileName = "samples\\" + input()
    fileTest = "examples\\ex_1" # name for examples test files
    test = "test.txt" # name for test file
    result = PatternMatch(fileName)
    return 0

if __name__ == "__main__":
    main()