import copy

def process_part1(input_chart):
    new_chart = copy.deepcopy(input_chart)
    for i, row in enumerate(input_chart):
        for j, seat in enumerate(row):
            adjacent = []
            if seat != '.':
                up = None if i == 0 else input_chart[i-1][j]
                down = None if i == len(input_chart)-1 else input_chart[i+1][j]
                right = None if j == len(row)-1 else input_chart[i][j+1]
                left = None if j == 0 else input_chart[i][j-1]
                diag_downL = None if not (down and left) else input_chart[i+1][j-1]
                diag_downR = None if not (down and right) else input_chart[i+1][j+1]
                diag_upL = None if not (up and left) else input_chart[i-1][j-1]
                diag_upR = None if not (up and right) else input_chart[i-1][j+1]
                adjacent = [up, down, right, left, diag_downL, diag_downR, diag_upL, diag_upR]
                if seat == 'L' and '#' not in adjacent:
                    new_chart[i][j] = '#'
                elif seat == '#' and adjacent.count('#')>3:
                    new_chart[i][j] = 'L'
    return new_chart

def look(i, j, input_chart, direction):
    vision = 1
    if direction == 'up':
        while i-vision > -1 and input_chart[i-vision][j] == '.':
            vision += 1
        return '.' if i-vision < 0 else input_chart[i-vision][j]
    
    elif direction == 'down':
        while i+vision < len(input_chart) and input_chart[i+vision][j] == '.':
            vision += 1
        return '.' if i+vision > len(input_chart)-1 else input_chart[i+vision][j]
    
    elif direction == 'left':
        while j-vision > -1 and input_chart[i][j-vision] == '.':
            vision += 1
        return '.' if j-vision < 0 else input_chart[i][j-vision]
    
    elif direction == 'right':
        while j+vision < len(input_chart[i]) and input_chart[i][j+vision] == '.':
            vision += 1
        return '.' if j+vision > len(input_chart[i])-1 else input_chart[i][j+vision]
    
    # Diagionals
    elif direction == 'diag_downL':
        while i+vision < len(input_chart) and j-vision > -1 and input_chart[i+vision][j-vision] == '.':
            vision += 1
        return '.' if (i+vision > len(input_chart)-1 or j-vision < 0) else input_chart[i+vision][j-vision]
    
    elif direction == 'diag_downR':
        while i+vision < len(input_chart) and j+vision < len(input_chart[i]) and input_chart[i+vision][j+vision] == '.':
            vision += 1
        return '.' if (i+vision > len(input_chart)-1 or j+vision > len(input_chart[i])-1) else input_chart[i+vision][j+vision]
    
    elif direction == 'diag_upR':
        while i-vision > -1 and j+vision < len(input_chart[i]) and input_chart[i-vision][j+vision] == '.':
            vision += 1
        return '.' if (i-vision < 0 or j+vision > len(input_chart[i])-1) else input_chart[i-vision][j+vision]
    
    elif direction == 'diag_upL':
        while i-vision > -1 and j-vision > -1 and input_chart[i-vision][j-vision] == '.':
            vision += 1
        return '.' if (i-vision < 0 or j-vision < 0) else input_chart[i-vision][j-vision]
    else:
        return None

def process_part2(input_chart):
    new_chart = copy.deepcopy(input_chart)
    for i, row in enumerate(input_chart):
        for j, seat in enumerate(row):
            adjacent = []
            if seat != '.':
                up = None if i == 0 else look(i, j, input_chart, 'up')
                down = None if i == len(input_chart)-1 else look(i, j, input_chart, 'down')
                right = None if j == len(row)-1 else look(i, j, input_chart, 'right')
                left = None if j == 0 else look(i, j, input_chart, 'left')
                diag_downL = None if not (down and left) else look(i, j, input_chart, 'diag_downL')
                diag_downR = None if not (down and right) else look(i, j, input_chart, 'diag_downR')
                diag_upL = None if not (up and left) else look(i, j, input_chart, 'diag_upL')
                diag_upR = None if not (up and right) else look(i, j, input_chart, 'diag_upR')
                adjacent = [up, down, right, left, diag_downL, diag_downR, diag_upL, diag_upR]
                if seat == 'L' and '#' not in adjacent:
                    new_chart[i][j] = '#'
                elif seat == '#' and adjacent.count('#')>4:
                    new_chart[i][j] = 'L'
    return new_chart

# for debugging
def printChart(chart):
    for line in chart:
        print(line)
    print('---------------------------------------------------')

def get_solution(chart, part2 = False):
    # Pick process function
    if part2:
        process = process_part2
    else:
        process = process_part1

    # While the state is changing, apply function
    last_result = chart
    new_result = process(chart)
    while last_result != new_result:
        last_result = new_result
        new_result = process(last_result)
    
    # Count unoccupied seats for solution
    num_taken = 0
    for row in new_result:
        num_taken += row.count('#')
    return num_taken

with open('2020/dec_11/input.txt', 'r') as file:
    line = file.readline()
    input = []
    while line:
        row = line.strip('\n')
        input.append([x for x in row])
        line = file.readline()

    print('Problem 1: ', get_solution(input))
    print('Problem 2: ', get_solution(input, True))