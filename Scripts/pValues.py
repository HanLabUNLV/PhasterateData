'''
Given a file it will compute the p-values based on the passed degrees of freedom
using a chi-squared distribution. Assumes data has headers.

Requires numpy and scipy to work.
'''
# ==========================================================================================
import sys
import numpy as np
import scipy.stats as stats
# ==========================================================================================
def main():
    # Check argumments.
    args = parseArgs(sys.argv)
    if args == ():
        return
    inputFile, degreesOfFreedom, outputFile = args

    with open(inputFile) as fin:
        # Assume and skip headers.
        fin.readline()
        fin.readline()
        values = [(l.split()[0], l.split()[1]) for l in fin]

    # Unzip data.
    values = map(lambda t: 2 * (float(t[1]) - float(t[0])), values)
    pValues = 1 - stats.chi2.cdf(list(values), int(degreesOfFreedom))

    # Print array to file
    np.savetxt(outputFile, pValues, fmt='%1.8f')

    return
# ==========================================================================================
'''
Given the sys.argv it will fetch the file handles and open files for reading and writing.
Returns: returns ppa tuple if successful, else the empty tuple.
'''
def parseArgs(args):
    if len(args) != 4:
        print("Usage: <inputFile> <degreesOfFreedom> <outputFile>")
        return ()

    inputFile = args[1]
    degreesOfFreedom = args[2]
    outputFile = args[3]

    return inputFile, degreesOfFreedom, outputFile
# ==========================================================================================
if __name__ == "__main__":
    main()
