import copy
from time import perf_counter

def count_neighbors(row, col, input_chart, limit=8, part2=False):
    num_occupied = 0
    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        neighbor_row, neighbor_col = i + row, j + col
        while neighbor_row > -1 and neighbor_row < NUM_ROWS and neighbor_col > -1 and neighbor_col < NUM_COLUMNS:
            if input_chart[neighbor_row][neighbor_col] != '.':
                num_occupied += 1 if input_chart[neighbor_row][neighbor_col] == '#' else 0
                if num_occupied == limit:
                    return num_occupied
                break
            if not part2:
                break
            else:
                neighbor_row += i
                neighbor_col += j
    return num_occupied

def process_part1(input_chart):
    new_chart = copy.deepcopy(input_chart)
    for row in range(len(input_chart)):
        for col in range(len(input_chart[row])):
            if input_chart[row][col] == 'L' and count_neighbors(row, col, input_chart) == 0:
                new_chart[row][col] = '#'
            elif input_chart[row][col] == '#' and count_neighbors(row, col, input_chart, 4) >= 4:
                new_chart[row][col] = 'L'
    return new_chart

def process_part2(input_chart):
    new_chart = copy.deepcopy(input_chart)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            if input_chart[row][col] == 'L' and count_neighbors(row, col, input_chart, part2=True) == 0:
                new_chart[row][col] = '#'
            elif input_chart[row][col] == '#' and count_neighbors(row, col, input_chart, 5, part2=True) == 5:
                new_chart[row][col] = 'L'
    return new_chart

def printChart(chart):
    # for debugging
    if chart:
        for line in chart:
            print(line)
        print('---------------------------------------------------')

def get_solution(chart, part2=False):
    # Pick process function
    process = process_part2 if part2 else process_part1

    # While the state is changing, apply function
    last_result = None
    while last_result != chart:
        last_result = chart
        chart = process(last_result)

    # Count occupied seats for solution
    return sum(row.count('#') for row in chart)

with open('2020/dec_11/input.txt', 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]
    input = [list(line) for line in lines]

    NUM_ROWS = len(input)
    NUM_COLUMNS = len(input[0])

    start = perf_counter()
    print('Problem 1: ', get_solution(input),
          '  (Calculated in', perf_counter() - start, 'seconds.)')
    start = perf_counter()
    print('Problem 2: ', get_solution(input, part2=True),
          '  (Calculated in', perf_counter() - start, 'seconds.)')