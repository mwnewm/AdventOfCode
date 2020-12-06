def findSeat(bp):
    # Find row
    row_start, row_end = 0, 127
    for flag in bp[:7]:
        shift = (row_end + row_start) // 2
        if flag == 'F':
            row_end = shift
        elif flag == 'B':
            row_start = shift + 1
    
    # Find column
    col_start, col_end = 0, 7
    for flag in bp[7:]:
        shift = (col_end + col_start) // 2
        if flag == 'L':
            col_end = shift
        elif flag == 'R':
            col_start = shift + 1
    
    return row_start*8 + col_start

def findEmpty(ids):
    for id in range(127*8+7):
        if id not in ids and id-1 in ids and id+1 in ids:
            return id

with open('2020/dec_05/input.txt') as file:
    passes = file.readlines()
    ids = list()

    for bp in passes:
        ids.append(findSeat(bp.strip()))

    print('Problem 1: ', max(ids))
    print('Problem 2: ', findEmpty(ids))

