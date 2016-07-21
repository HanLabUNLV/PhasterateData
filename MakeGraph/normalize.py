'''
Given a file of floats, one per line, it will create a file of the same size with the
values normalized between -50.0 and 50.0.

python normalize.py <inputFile> <outputFile>
'''
#==========================================================================================
import sys
#==========================================================================================
def main():
    #Check argumments.
    args = parseArgs(sys.argv)
    if args == ():
        return
    inputFile,outputFile = args

    fin = openFileReading(inputFile)
    if fin == ():
        return()

    fout = openFileWriting(outputFile)
    if fout == ():
        return()

    #Create list of number:
    myNumbers = [float(number) for number in fin]
    myMax = max(map(abs,myNumbers))
    myMin = -myMax
    divisor = myMax - myMin

    for number in myNumbers:
        normalizedNumber = (number - myMin) / divisor
        fout.write(str(round(normalizedNumber * 100 - 50, 4)) + '\n')

    fout.close()
    fin.close()

    print("Done!")
    return
#==========================================================================================
'''
Given a file name as a string will attempt to open it for reading.
'''
def openFileWriting(outputFile):
    try:
        fout = open(outputFile,'w')
    except IOError:
        print("Cannot open file to write to: ", outputFile)
        return ()

    return fout
#==========================================================================================
'''
Given a file name as a string will attempt to open it for reading.
'''
def openFileReading(outputFile):
    try:
        fout = open(outputFile,'r')
    except IOError:
        print("Cannot open file to read from..")
        return ()

    return fout
#==========================================================================================
'''
Given the sys.argv it will fetch the file handles and open files for reading and writing.
Returns: returns ppa tuple if successful, else the empty tuple.
'''
def parseArgs(args):
    if len(args) != 3:
        print("Usage: <inpuntFile> <outputFile>")
        return ()

    inputFile = args[1]
    outputFile = args[2]

    return inputFile, outputFile
#==========================================================================================
if __name__ == "__main__":
    main()
