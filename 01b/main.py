#open file
readings = open("input.txt").read().splitlines()
#convert str list to int list
ints = [int(x) for x in readings]
count = 0
for i in range (len(ints)-3):
    sum1 = ints[i] + ints[i+1] + ints[i+2]
    sum2 = ints[i+1] + ints[i+2] + ints[i+3]
    if sum2 > sum1:
        count=count+1
print(count)

