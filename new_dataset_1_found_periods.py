import matplotlib.pyplot as plt
import numpy as np 

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