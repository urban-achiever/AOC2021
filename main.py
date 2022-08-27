import numpy as np
# get input
chars = open("input.txt").read().splitlines()
for i in range (len(chars)):
    chars[i] = list(chars[i])
# convert 2d list of chars to 2d numpy array
a = np.array(chars, dtype=int)
l = len(a)
# Sum the 0 and 1 values in the columns and rows
colsums = np.sum(a, axis=0)
rowsums = np.sum(a, axis=1)
#print("rowsums before", rowsums)
# Check if more than half the values in a row or col are 1
rowstr = ""
colstr = ""
for i in range (len(colsums)):
    if colsums[i] > l/2:
        colstr = colstr + "1"
        rowstr = rowstr + "0"
    else:
        colstr = colstr + "0"
        rowstr = rowstr + "1"
gam = int(rowstr, 2)
eps = int(colstr, 2)
power = gam*eps
print(power)
