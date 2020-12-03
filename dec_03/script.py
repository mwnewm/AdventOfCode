def problem_1(map, right = 3, down = 1):
    count = 0
    col = 0
    modVal = len(map[0])-1
    for row in range(1, len(map)):
        if row % down == 0:
            col += right
            if map[row][col % modVal] == '#':
                count += 1
    return count

def problem_2(map):
    product = problem_1(map, 1, 1)*problem_1(map, 3, 1)*problem_1(map, 5, 1)*problem_1(map, 7, 1)*problem_1(map, 1, 2)
    return product


with open('input.txt', 'r') as file:
    map = file.readlines()

    print('Problem 1: ', problem_1(map))
    print('Problem 2: ', problem_2(map))

