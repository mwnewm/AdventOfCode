def findSeat(bp):
    row_start, row_end = 0, 127
    for flag in bp[:7]:
        shift = (row_end + row_start) // 2
        if flag == 'F':
            row_end = shift
        elif flag == 'B':
            row_start = shift + 1
    
    col_start, col_end = 0, 7
    for flag in bp[7:]:
        shift = (col_end + col_start) // 2
        if flag == 'L':
            col_end = shift
        elif flag == 'R':
            col_start = shift + 1

    seat = {
        'row': row_start,
        'column': col_start
    }
    
    return seat['row']*8 + seat['column']



with open('2020/dec_05/input.txt') as file:
    seats = file.readlines()
    ids = list()

    for bp in seats:
        ids.append(findSeat(bp.strip()))

    print("Problem 1: ", max(ids))