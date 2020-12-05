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
    
    while valid:
        # Parse fields
        byr = int(passportDict['byr'])
        iyr = int(passportDict['iyr'])
        eyr = int(passportDict['eyr'])
        hgt = passportDict['hgt']
        hcl = passportDict['hcl']
        ecl = passportDict['ecl']
        pid = passportDict['pid']
    
        # Check year fields
        if byr < 1920 or byr > 2002:
            valid = False
        if iyr < 2010 or iyr > 2020:
            valid = False
        if eyr < 2020 or eyr > 2030:
            valid = False

        # Check height
        if len(hgt) > 2:
            hgt_unit = hgt[-2:]
            hgt_num = int(hgt[:-2])
            if hgt_unit == 'cm':
                if hgt_num < 150 or hgt_num > 193:
                    valid = False
            
            if hgt_unit == 'in':
                if hgt_num < 59 or hgt_num > 76:
                    valid = False
            
            if hgt_unit != 'in' and hgt_unit != 'cm':
                valid = False
        else:
            valid = False
    
        # Check hair color     
        if hcl[0] == '#':
            for char in hcl[1:7]:
                if not ord(char) in range(97, 103) and not ord(char) in range (48, 58):
                    valid = False
        else:
            valid = False

        # Check eye color
        if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

        # Check pid
        if len(pid) == 9:
            for char in pid:
                if not ord(char) in range (48, 58):
                    valid = False
        else:
            valid = False
        
        # Made it through checks!
        break

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

with open('input.txt', 'r') as file:
    input = file.readlines()
    line = 0
    passports = []
    entry = dict()
    while line < len(input):
        if input[line] != '\n':
            entry.update(makeDict(input[line]))
        else:
            passports.append(entry)
            entry = dict()
        if line == len(input)-1:
            passports.append(entry)
        line += 1

    print('Problem 1: ', problem_1(passports))
    print('Problem 2: ', problem_2(passports))