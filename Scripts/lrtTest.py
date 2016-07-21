'''
Given two files containing the log likelihood scores. It will perform a likelihood
ratio test. The files must contain a single column of floats separated by newlines.

LRT: -2 (valueOne[i] - valueTwo[i])
'''
#==========================================================================================
import sys
import numpy as np
#==========================================================================================
def main():
    #Check argumments.
    args = parseArgs(sys.argv)
    if args == ():
        return
    firstModel, secondModel, outputFile = args
    firstValues = np.fromfile(firstModel, float, -1, sep="\n")
    secondValues = np.fromfile(secondModel, float, -1, sep="\n")

    pValues = 2 * np.subtract(firstValues, secondValues)

    #Print array to file
    np.savetxt(outputFile, pValues, fmt='%1.6f')

    return
#==========================================================================================
'''
Given the sys.argv it will fetch the file handles and open files for reading and writing.
Returns: returns ppa tuple if successful, else the empty tuple.
'''
def parseArgs(args):
    if len(args) != 4:
        print "Usage: <altModel> <nullModel> <outputFile>"
        return ()

    firstModel = args[1]
    secondModel = args[2]
    outputFile = args[3]

    return firstModel, secondModel, outputFile
#==========================================================================================
if __name__ == "__main__":
    main()
