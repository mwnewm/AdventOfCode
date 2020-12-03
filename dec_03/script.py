def problem_1(map):
    count = 0
    col = 0
    modVal = len(map[0])-1
    for row in range(1, len(map)):
        col += 3
        #print(map[row][col % modVal])
        #print('Row: ', row, 'Col: ', col % modVal, ' (', col, ')')
        if map[row][col % modVal] == '#':
            count += 1
            #print('count')

    return count


with open('input.txt', 'r') as file:
    map = file.readlines()

    print('Problem 1: ', problem_1(map))
