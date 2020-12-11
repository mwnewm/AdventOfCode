def problem_1(nums):
    curr_jolt = min(nums)
    nums.remove(curr_jolt)
    diff1 = diff2 = diff3 = 0
    while nums:
        min_val = min(nums)
        if min_val-curr_jolt == 3:
            diff3 += 1
        elif min_val-curr_jolt == 2:
            diff2 += 1
        elif min_val-curr_jolt == 1:
            diff1 += 1
        else:
            return None
        curr_jolt = min_val
        nums.remove(min_val)
    return diff3*diff1

# Solution implemented using memoization
def problem_2(nums):
    paths = dict()
    for i in nums:
        paths[i] = 0
    paths[0] = 1
    for item in nums:
        if item+1 in nums:
            paths[item+1] += paths[item]
        if item+2 in nums:
            paths[item+2] += paths[item]
        if item+3 in nums:
            paths[item+3] += paths[item]
    return paths[nums[len(nums)-1]]

with open('2020/dec_10/input.txt', 'r') as file:
    nums = file.readlines()
    nums_set = set()
    for num in nums:
        nums_set.add(int(num.strip('\n')))
    nums_set.add(0)
    nums_set.add(max(nums_set)+3)

    print('Problem 1: ', problem_1(nums_set.copy()))
    print('Problem 2: ', problem_2(list(nums_set)))