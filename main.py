import numpy as np

def mostCommonBit(array, column):
    l = len(array)
    if np.sum(array, axis=0)[column] >= l/2:
        return 1
    else:
        return 0
    
# get input
chars = open("input.txt").read().splitlines()
for i in range (len(chars)):
    chars[i] = list(chars[i])

# convert 2d list of chars to 2d numpy array
a = np.array(chars, dtype=int)
b = a
colnum = 0
w = len(a[0])
# loop through each column of the array
while colnum < w: 
    mostCommon = mostCommonBit(a, colnum)
    indexes = []
    # for each bit in the given column, if the bit is the 
    # most common one, store it's index
    for i in range(len(a)):
        if a[i][colnum] != mostCommon:
            indexes.append(i)
    # delete rows with those indexes
    a = np.delete(a, indexes, axis=0)
    # if only one value remains that is the result
    # otherwise proceed to the next column
    if len(a) == 1:
        o2str = ''.join(map(str, a[0]))
        O2 = int(o2str, 2)
        break
    else:
        colnum += 1
colnum = 0
while colnum < w: 
    leastCommon = 1 - mostCommonBit(b, colnum)
    indexes = []
    # for each bit in the given column, if the bit is the 
    # most common one, store it's index
    for i in range(len(b)):
        if b[i][colnum] != leastCommon:
            indexes.append(i)
    # delete rows with those indexes
    b = np.delete(b, indexes, axis=0)
    # if only one value remains that is the result
    # otherwise proceed to the next column
    if len(b) == 1:
        co2str = ''.join(map(str, b[0]))
        CO2 = int(co2str, 2)
        break
    else:
        colnum += 1
print("Life support rating:", O2 * CO2 )
