def problem_1(input):
    memory = {}
    for entry in input:
        mask = entry['mask']
        for mem, val in entry['entries']:
            binVal = list("{0:b}".format(val).zfill(36)) # Read in original as binary, and cast as list
            for i, c in mask:
                binVal[i] = c # Replace values in original according to current mask
            memory[mem] = int(''.join(binVal), 2) # Join list, convert to base 2, add to return val
    return sum(memory.values())

def problem_2(input):
    pass

with open('2020/dec_14/input.txt') as file:
    line = file.readline()
    input = []
    while line:
        if line.startswith('mask'):
            # Parse mask
            mask = line[6:].strip(' \n')
            replace = []
            for x, c in enumerate(mask):
                if c != 'X':
                    replace.append((x, c))
            # Read memory lines
            entries = []
            line = file.readline()
            while line.startswith('mem'):
                val = line.split(' = ')
                entries.append(
                    (int(val[0].strip('mem[] ')), int(val[1].strip('\n '))))
                line = file.readline()
            # Add to input
            input.append({
                'mask': replace,
                'entries': entries
            })
        else:
            line = file.readline()

    print('Problem 1: ', problem_1(input))
    print('Problem 2: ', problem_2(input))
