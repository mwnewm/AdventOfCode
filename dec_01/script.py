def problem_1(num_list, total = 2020):
    for num in num_list:
        if (total-num) in num_list:
            return num * (total-num)
    return None

def problem_2(num_list):
    start = 0
    end = len(num_list)
    for num in num_list:
        solution = problem_1(num_list[start:end], 2020-num)
        if solution:
            return num * solution
        start += 1
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
