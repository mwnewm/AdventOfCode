def getCmds(input):
    cmds = []
    for line in input:
        item = line.strip('\n').split(' ')
        if item[1][0] == '+':
            item[1] = int(item[1][1:])
        elif item[1][0] == '-':
            item[1] = -1*int(item[1][1:])
        item.append(False)
        cmds.append(item)
    return cmds

def resetFlags(cmds):
    for line in cmds:
        line[2] = False
    return cmds

def problem_1(cmds):
    accum = i = 0
    curr = cmds[0]
    while i < len(cmds) and not cmds[i][2] :
        curr = cmds[i]
        if curr[0] == 'nop':
            i += 1
        elif curr[0] == 'acc':
            accum += curr[1]
            i += 1
        elif curr[0] == 'jmp':
            i += curr[1]
        else:
            print('ERR')
        curr[2] = True
    resetFlags(cmds)
    return (accum, True if i >= len(cmds)-1 else False)

def problem_2(cmds):
    for line in cmds:
        if line[0] == 'nop':
            line[0] = 'jmp'
            response = problem_1(cmds)
            if response[1]:
                return response[0]
            else:
                line[0] = 'nop'
        elif line[0] == 'jmp':
            line[0] = 'nop'
            response = problem_1(cmds)
            if response[1]:
                return response[0]
            else:
                line[0] = 'jmp'
    return 'No solution'

with open('2020/dec_08/input.txt', 'r') as file:
    input = file.readlines()
    cmds = getCmds(input)

    print('Problem 1: ', problem_1(cmds)[0])
    print('Problem 2: ', problem_2(cmds))