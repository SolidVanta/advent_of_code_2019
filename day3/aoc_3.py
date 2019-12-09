import numpy as np
dim = 25000
wires = list()
grid = np.zeros((2*dim,1.2*dim))
x = 10000
y = 2000
pos = [x,y]

with open("input","r") as file:
    for line in file:
        wires.append(line.strip().split(","))

def isIntersection(val, pos):
    if val == 2 and grid[pos[1], pos[0]] == 1.0:
        return True
    
def decode_command(command, val):
    if command[0] == "R":
        for incr in range(int(command[1:])):
            prev = pos
            pos[0]= pos[0] + 1
            if isIntersection(val, prev):
                grid[pos[1] , pos[0]] = 3
                continue
            else:
                grid[pos[1] , pos[0]] = val
            grid[pos[1] , pos[0]] = val
            print pos
                
    if command[0] == "L":
        for incr in range(int(command[1:])):
            prev = pos
            pos[0]= pos[0] - 1
            if isIntersection(val,prev):
                grid[pos[1] , pos[0]] = 3
                continue
            else:
                grid[pos[1] , pos[0]] = val
            grid[pos[1] , pos[0]] = val
            print pos

    if command[0] == "U":
        for incr in range(int(command[1:])):
            prev = pos
            pos[1]= pos[1] + 1
            if isIntersection(val,prev):
                grid[pos[1] , pos[0]] = 3
                continue
            else:
                grid[pos[1] , pos[0]] = val
            grid[pos[1] , pos[0]] = val
            print pos

    if command[0] == "D":
        for incr in range(int(command[1:])):
            prev = pos
            pos[1] = pos[1] - 1
            if isIntersection(val, prev):
                grid[pos[1] , pos[0]] = 3
                continue
            else:
                grid[pos[1] , pos[0]] = val
            grid[pos[1] , pos[0]] = val
            print(pos)

'''
def move_right(matrix, steps):
def move_left(matrix, steps):
def move_up(matrix, steps):
def move_down(matrix, steps):
'''
#w2 = ["U7","R6","D4","L4"]
#w1 = ["R8","U5","L5","D3"]
#w1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
#w2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
w1 = wires[0]
w2 = wires[1]

for command in w1:
    decode_command(command, 1)
    #print np.flipud(grid)
print("W I R E 2 MAAAAAAAAAAAAAAAAAAAAN")
pos = [x,y]
for command in w2:
    decode_command(command, 2)
    #print np.flipud(grid)

results = np.where(grid==3, )
print(results)
print(len(results))
distances = list()
for i in range(len(results[0])):
    distances.append(abs(results[0][i]-y) + abs(results[1][i]-x))
print(min(distances))
    #print(results[0][i],results[1][i])

