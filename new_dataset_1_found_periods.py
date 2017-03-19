import matplotlib.pyplot as plt
import numpy as np 
from scipy.signal import argrelextrema

# Read the file. 
f2 = open('new_dataset_1.txt', 'r')

# read the whole file into a single variable, which is a list of every row of the file.
lines = f2.readlines()
f2.close()

# initialize some variable to be lists
x1 = []
y1 = []
phaselist=[]

# scan the rows of the file stored in lines, and put the values into some variables
for line in lines:
    p = line.split(",")
    if(float(p[1])<0.9990):
        phaselist.append(float(p[0]))
    x1.append(float(p[0]))
    y1.append(float(p[1]))
xv = np.array(x1)
yv = np.array(y1)
# plotting the data
plt.plot(xv, yv)
plt.title('Single Orbit Example Light Curve')
plt.xlabel('Phase')
plt.ylabel('Relative Flux')
plt.show()
periodpoints=[]
periodnoorbit=[]
periodorbit=[]
for i in range(0,len(phaselist)-1):
    if(phaselist[i+1]-phaselist[i]>1):
        periodpoints.append(phaselist[i])
        periodpoints.append(phaselist[i+1])
for i in range(0,len(periodpoints)-1):
    if(i%2==0):
        periodnoorbit.append(periodpoints[i+1]-periodpoints[i])
    else:
        periodorbit.append(periodpoints[i+1]-periodpoints[i])
print "no orbit:",np.mean(periodnoorbit)
print "orbit:",np.mean(periodorbit)
print "change in flux:",1-np.min(y1)
minmy=[]
minmx=[]
findminx=[]
findminy=[]
minmpointx=[]
minmpointy=[]
for i in range(1,len(y1)-1):
    if ( (y1[i-1]>y1[i]) and  (y1[i]<y1[i+1]) ):
        if(y1[i]<0.990):
                minmy.append(y1[i])
                minmx.append(x1[i])
for i in range(1,len(minmy)-1):
    
    if(minmx[i]-minmx[i-1]<1):
        findminx.append(minmx[i-1])
        findminy.append(minmy[i-1])
    else:
        findminx.append(minmx[i-1])
        findminy.append(minmy[i-1])
        minpoint=np.min(findminy)
        index=findminy.index(minpoint)
        minmpointx.append(findminx[index])
        minmpointy.append(findminy[index])
        findminx=[]
        findminy=[]
for i in range(0,len(minmpointx)):
    print "phase:",minmpointx[i],"flux",minmpointy[i]
