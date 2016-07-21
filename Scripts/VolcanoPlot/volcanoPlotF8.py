'''
Given a file representing the x-axis values and another representing the y-axis values
this script will create a Volcano Plot of the the data. Where the x-values is the log of
the data and the y-values are the -log10 of our data.

See volcano plot for more infromation. Assumes the significance values of p-values to
be 0.05.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import sys

plotTitle = "F84E Indel Model"
xLabel = "log2(scalingParameter)"
yLabel = "-log10(pValue)"


def main():
    args = parseArgs(sys.argv)
    if args == ():
        return

    fin1, fin2, saveFile = args

    #Float type data, read whole file, delmited by newlines.
    x = np.fromfile(fin1,float,-1,'\n')
    y = np.fromfile(fin2,float,-1,'\n')
    fileFormat = "png"

    #Better looking graphs.
    pd.options.display.mpl_style = "default"

    #Set Labels
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(plotTitle)
    plt.xlim(-10, 10)
    plt.ylim(0, 10)

    #Log data as neeed for both axis.

    #Filter out all the funny values.
    #tupleList = filter(lambda (a,b): b != 0.0, zip(x,y))
    #x, y = zip(* filter(lambda (a,b): a != 0.000001, tupleList))

    y = map(f, y)
    xValues = map((lambda z: m.log(z, 2)), x)
    yValues = map((lambda z: -m.log10(z)), y)

    #Actual printing, with set color and marker type.
    plt.scatter(xValues, yValues, c="red", edgecolor='', s=0.8)
    line = -m.log10(0.05)
    plt.plot([-10, 10], [line, line], linewidth=0.5)

    print "Saving file in high quality..."
    plt.savefig(saveFile + '.' + fileFormat, dpi=800, format=fileFormat)

    fin1.close()
    fin2.close()
    return
#==========================================================================================
#Given the sys.argv it will fetch the file handles and open files for reading and writing.
#Returns: returns a tuple if successful, else the empty tuple.
def parseArgs(arguments):
    if len(arguments) != 4:
        print "Usage: <scales> <pValues> <saveFileName>"
        return ()

    inputFile1 = arguments[1]
    inputFile2 = arguments[2]
    saveFile = arguments[3]
    try:
        fin1 = open(inputFile1,'r')
        fin2 = open(inputFile2,'r')
    except IOError:
        print "Cannot open some input file..."
        return ()

    return fin1,fin2,saveFile
#==========================================================================================
#Converts all zeros to 1e-20
def f(x):
    myVal = x
    if x == 0:
        myVal = 1e-20

    return myVal
#==========================================================================================
main()
