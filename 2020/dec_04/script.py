def makeDict(entry):
    passport = entry.split(' ')
    passportDict = dict()
    for item in passport:
        pair = item.split(':')
        passportDict[pair[0].strip()] = pair[1].strip()
    return passportDict

def checkFields(passportDict):
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        try:
            passportDict[key]
        except KeyError:
            return False
    return True

def validate(passportDict):
    # Check that fields exist
    valid = checkFields(passportDict)
    
    # Parse fields
    if valid:
        byr = int(passportDict['byr'])
        iyr = int(passportDict['iyr'])
        eyr = int(passportDict['eyr'])
        hgt = passportDict['hgt']
        hcl = passportDict['hcl']
        ecl = passportDict['ecl']
        pid = passportDict['pid']
    
    # Check year fields
    if valid:
        valid = byr in range(1920, 2003) and iyr in range(2010, 2021) and eyr in range(2020, 2031)

    # Check height
    if valid:
        if len(hgt)>2:         
            hgt_unit = hgt[-2:]
            hgt_num = int(hgt[:-2])
            valid = (hgt_unit == 'cm' and hgt_num in range(150,194)) or (hgt_unit == 'in' and hgt_num in range(59, 77))
        else:
            valid = False
    
    # Check hair color  
    if valid:
        valid = hcl[0] == '#' and (ord(char) in range(97, 103) and not ord(char) in range (48, 58) for char in hcl[1:7])

    # Check eye color
    if valid:
        valid = ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # Check pid
    if valid:
        valid = len(pid) == 9 and (ord(char) in range (48, 58) for char in pid)
        
    return valid

def problem_1(passports):
    count = 0
    for entry in passports:
        if checkFields(entry):
            count += 1
    return count

def problem_2(passports):
    count = 0
    for entry in passports:
        if validate(entry):
            count += 1
    return count

with open('2020/dec_04/input.txt', 'r') as file:
    line = file.readline()
    passports = []
    entry = dict()
    while line:
        if line == '\n':
            passports.append(entry)
            entry = dict()  
        else:
            entry.update(makeDict(line))
        line = file.readline()
    passports.append(entry)

    print('Problem 1: ', problem_1(passports))
    print('Problem 2: ', problem_2(passports))