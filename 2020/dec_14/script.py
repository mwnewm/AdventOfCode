from itertools import product

def problem_1(input):
    memory = {}
    for entry in input:
        # Parse mask
        mask = entry['mask']
        replace = []
        for x, c in enumerate(mask):
            if c != 'X':
                replace.append((x, c))
        for mem, val in entry['entries']:
            # Read in original as binary, and cast as list
            binVal = list("{0:b}".format(int(val)).zfill(36))
            for i, c in replace:
                # Replace values in original according to current mask
                binVal[i] = c
            # Join list, convert to base 2, add to return val
            memory[mem] = int(''.join(binVal), 2)
    return sum(memory.values())

def problem_2(input):
    memory = {}
    for entry in input:
        # Parse mask
        mask = entry['mask']
        replace = []
        floats = []
        for x, c in enumerate(mask):
            if c == '1':
                replace.append(x)
            elif c == 'X':
                floats.append(x)
        # Get values to be written
        for mem, val in entry['entries']:
            # Read in address as binary
            binVal = list("{0:b}".format(mem).zfill(36))
            # Overwrite 1s according to mask
            for i in replace:
                binVal[i] = '1'
            # Generate possible addresses according to floats in mask
            for address in product([0, 1], repeat=len(floats)):
                for i, x in enumerate(floats):
                    binVal[x] = str(address[i])
                addr = int(''.join(binVal), 2)
                # Write to memory
                memory[addr] = int(val)
    return sum(memory.values())

with open('2020/dec_14/input.txt') as file:
    line = file.readline()
    input = []
    while line:
        if line.startswith('mask'):
            mask = line[6:].strip(' \n')
            # Read memory lines
            entries = []
            line = file.readline()
            while line.startswith('mem'):
                val = line.split(' = ')
                entries.append(
                    (int(val[0].strip('mem[] ')), val[1].strip('\n ')))
                line = file.readline()
            # Add to input
            input.append({
                'mask': mask,
                'entries': entries
            })
        else:
            line = file.readline()

    print('Problem 1: ', problem_1(input))
    print('Problem 2: ', problem_2(input))
