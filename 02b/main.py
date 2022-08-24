lines = open("input.txt").read().splitlines()
f = 0
d = 0
aim = 0
for i in range (len(lines)-1):
    lines[i] = lines[i].split()
    v = int(lines[i][1])
    if lines[i][0] == 'forward':
        f = f + v
        d = d + aim*v
    if lines[i][0] == 'up':
        aim = aim - v
    if lines[i][0] == 'down':
        aim = aim + v
print(d*f)
