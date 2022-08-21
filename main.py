import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#p190file = r"c:\Users\pxgeo2.geo\PycharmProjects\P190_visualization\RS2201522P110077.WGS84.p190"
p190file = r"c:\Users\pxgeo2.geo\PycharmProjects\P190_visualization\RS2201630P210100.WGS84.p190"
s=[]
x=[]
y=[]
xnf=[]
ynf=[]
with open(p190file, 'r') as p190:
    for line in p190:
        if line.startswith("S"):
#            print(line[20:25])
            s += [int(line[20:25])]
            x += [float(line[47:55])]
            y += [float(line[55:65])]
            #print (x,y)
        if line.startswith("H2600 ") and "NF " in line:
            xnf += [float(line[20:29])] + [float(line[52:61])]
            ynf += [float(line[29:39])] + [float(line[61:71])]
plt.scatter(x, y, marker='s',s=2, c='b')
plt.scatter(xnf, ynf, marker='.',s=1, c='r')
#print (" ------------------- COS ----------------------")
#plt.scatter(x, y, marker='s',s=1)
plt.xticks(np.arange(min(x), max(x)+1, 1000.0))
plt.yticks(np.arange(min(y), max(y)+1, 1000.0))
for i, label in enumerate(s):
    plt.annotate(label, (x[i], y[i]))
plt.show()
# with open(p190file, 'r') as p190:
#     for line in p190:
#         if line.startswith("H2600  ") and " NF " in line:
#             xnf += [float(line[47:56])]
#             ynf += [float(line[47:56])]
# print (" ------------------- COS ----------------------")
#plt.scatter(xnf, ynf, marker='s',s=1)
#plt.xticks(np.arange(min(x), max(x)+1, 1000.0))
#plt.yticks(np.arange(min(y), max(x)+1, 1000.0))
#plt.show()

#print (" ------------------- NFH ----------------------")
#print(p190nfh)
#print (" ------------------- GUN ----------------------")
#print(p190gun)