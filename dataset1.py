# Dataplot for dataset_1

# INSTRUCTIONS: Build and run to obtain the graph for dataset_1


import matplotlib.pyplot as plt
import numpy as np 

# Read the file. 
f2 = open('dataset_1.txt', 'r')

# read the whole file into a single variable, which is a list of every row of the file.
lines = f2.readlines()
f2.close()

# initialize some variable to be lists
x1 = []
y1 = []

# scan the rows of the file stored in lines, and put the values into some variables
for line in lines:
    p = line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))
    
xv = np.array(x1)
yv = np.array(y1)


# plotting the data
plt.plot(xv, yv)
plt.title('Single Orbit Example Light Curve')
plt.xlabel('Decimal Phase')
plt.ylabel('Relative Flux')
plt.show()