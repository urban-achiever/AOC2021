lines = open("input.txt").read().splitlines()
f = 0
d = 0
for i in range (len(lines)-1):
    lines[i] = lines[i].split()
    if lines[i][0] == 'forward':
        f = f + int(lines[i][1])
    if lines[i][0] == 'up':
        d = d - int(lines[i][1])
    if lines[i][0] == 'down':
        d = d + int(lines[i][1])
print(d*f)
