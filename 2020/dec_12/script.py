import math

def rotate(point, angle):
    tx = point[0]*math.cos(angle) - point[1]*math.sin(angle)
    ty = point[0]*math.sin(angle) + point[1]*math.cos(angle)
    return (round(tx), round(ty))

def problem_1(directions):
    east, north = 0, 0
    comp = ['E', 'N', 'W', 'S']
    facing = 0
    for cmd, num in directions:
        if cmd == 'N':
            north += num
        elif cmd == 'S':
            north -= num
        elif cmd == 'E':
            east += num
        elif cmd == 'W':
            east -= num
        elif cmd == 'L':
            facing = (facing + 1*(num//90)) % 4
        elif cmd == 'R':
            facing = (facing + 3*(num//90)) % 4
        elif cmd == 'F':
            if comp[facing] == 'E':
                east += num
            elif comp[facing] == 'N':
                north += num
            elif comp[facing] == 'W':
                east -= num
            elif comp[facing] == 'S':
                north -= num
        else:
            print('ERROR')
    return abs(east)+abs(north)

def problem_2(directions):
    east, north = 10, 1
    east_s, north_s = 0, 0
    for cmd, num in directions:
        if cmd == 'N':
            north += num
        elif cmd == 'S':
            north -= num
        elif cmd == 'E':
            east += num
        elif cmd == 'W':
            east -= num
        elif cmd == 'L' or cmd == 'R':
            east, north = rotate((east, north), math.radians(num) if cmd == 'L' else -1*math.radians(num))
        elif cmd == 'F':
            east_s += num*east
            north_s += num*north
        else:
            print('ERROR')
    return abs(east_s)+abs(north_s)

with open('2020/dec_12/input.txt', 'r') as file:
    input = file.readlines()
    directions = [(x[0], int(x[1:].strip('\n'))) for x in input]

    print('Problem 1: ', problem_1(directions))
    print('Problem 2: ', problem_2(directions))