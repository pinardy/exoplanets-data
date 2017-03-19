# Dataplot for dataset_2

# INSTRUCTIONS: Build and run to obtain the set of graphs saved in your 
# directory under "\graphs\dataset2\"

import matplotlib.pyplot as plt
import numpy as np
import os

class DataStruct:
    def __init__(self, index):
        self.index = str(index)
        self.Xarray = []
        self.Yarray = []
    def appendX(self, x):
        self.Xarray.append(x)

    def appendY(self, y):
        self.Yarray.append(y)

    def plot(self):
        xv = np.array(self.Xarray)
        yv = np.array(self.Yarray)
        plt.figure(self.index)
        plt.plot(xv, yv)
        title = "multiple Orbit Example Light Curve for " + self.index
        plt.title(title)
        plt.xlabel('Decimal Phase')
        plt.ylabel('Relative Flux')
        plt.savefig(dirPath+self.index+".png")

# Read the file.
f2 = open('datasets\\dataset_2.txt', 'r')

# read the whole file into a single variable, which is a list of every row of the file.
lines = f2.readlines()
f2.close()

# initialize some variable to be lists
dataStructDict = {}
dirPath = os.path.dirname(os.path.realpath(__file__)) + "\\graphs\\dataset2\\"

# initialize directory
if not os.path.exists(dirPath):
    os.makedirs(dirPath)

# scan the rows of the file stored in lines, and put the values into some variables
for line in lines:
    p = line.split()
    if (dataStructDict.get(p[0], None) == None):
        dataStructDict[p[0]] = DataStruct(p[0])
    dataStructDict[p[0]].appendX(float(p[1]))
    dataStructDict[p[0]].appendY(float(p[2]))

# iterate through the dictionary to print each orbit results
for notImportant, dataStruct in dataStructDict.items():
    dataStruct.plot()

# plotting the data
# plt.show()
