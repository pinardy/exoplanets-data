# Dataplot for new_dataset_1

import matplotlib.pyplot as plt
import numpy as np 

# Read the file. 
# f2 = open('new_dataset_1.txt', 'r')

with open('dataset_2.txt') as f:
    f=[x.strip() for x in f if x.strip()]
    data=[tuple(map(float,x.split())) for x in f[2:]]
    phase=[x[1] for x in data]
    flux=[x[2] for x in data]
    cycle=[x[0] for x in data]
    print('cycle',cycle)
    print('flux',flux)
    print('phase',phase)

# read the whole file into a single variable, which is a list of every row of the file.
# lines = f2.readlines()
# f2.close()

# initialize some variable to be lists
x1 = []
y1 = []

# scan the rows of the file stored in lines, and put the values into some variables
# for line in lines:
#     p = line.split()
#     x1.append(float(p[0]))
#     y1.append(float(p[1]))
    
# xv = np.array(x1)
# yv = np.array(y1)


# plotting the data
# plt.plot(xv, yv)
# plt.title('Single Orbit Example Light Curve')
# plt.xlabel('Phase')
# plt.ylabel('Relative Flux')
# plt.show()