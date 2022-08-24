# open the input file and split into a list of strings
readings = open("input.txt").read().splitlines()
# convert list[str] to list[int]
ints = [int(x) for x in readings]
n = 0
# count how many times the next item is larger than the current item
for i in range (len(ints)-1):
    if ints[i+1] > ints[i]:
        n=n+1
print(n)
