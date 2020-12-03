def problem_1(pw_list):
    total = 0
    for pw in pw_list:
        min, max, char, text = pw['num1'], pw['num2'], pw['char'], pw['pass']
        count = text.count(char)
        if min <= count and max >= count:
            total += 1
    return total

def problem_2(pw_list):
    total = 0
    for pw in pw_list:
        index1, index2, char, text = pw['num1'], pw['num2'], pw['char'], pw['pass']
        condition = False
        if text[index1-1] == char:
            condition = not condition
        if text[index2-1] == char:
            condition = not condition
        if condition:
            total += 1
    return total

with open('input.txt', 'r') as file:
    lines = file.readlines()
    passwords = []
    for line in lines:
        line = line.split()
        nums = line[0].split('-')
        pw_dict = {
            'num1': int(nums[0]),
            'num2': int(nums[1]),
            'char': line[1].strip(':'),
            'pass': line[2]
        }
        passwords.append(pw_dict)

    print('Problem 1: ', problem_1(passwords))
    print('Problem 2: ', problem_2(passwords))
