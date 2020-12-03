def problem_1(num_list, total = 2020):
    for num in num_list:
        if (total-num) in num_list:
            return num * (total-num)
    return None

def problem_2(num_list):
    for num1 in num_list:
        for num2 in num_list:
            if (2020-num1-num2) in num_list:
                return num1 * num2 * (2020-num1-num2)
    return None

def recursive(num_list, rounds, total = 2020):
    if rounds == 1:
        if total in num_list:
            return total
        else:
            return None
    start = -1
    end = len(num_list)
    for num in num_list:
        start += 1
        solution = recursive(num_list[start:end], rounds-1, total-num)
        if solution:
            return num * solution
    return None


with open('input.txt') as file:
    index = 0
    lines = file.readlines()
    nums = lines
    for line in nums:
        nums[index] = int(lines[index])
        index += 1

    print('Problem 1: ', problem_1(nums))
    print('Problem 2: ', problem_2(nums))

    print('Problem 1 recursive: ', recursive(nums, 2))
    print('Problem 2 recursive: ', recursive(nums, 3))
