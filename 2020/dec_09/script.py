# Adapted from day 1 recursive solution
def check(num_list, total, rounds = 2):
    if rounds == 1:
        return total if total in num_list else None
    start = -1
    end = len(num_list)
    for num in num_list:
        start += 1
        if check(num_list[start:end], total-num, 1):
            return True
    return None

def check_contiguous(num_list, goal, contig):
    if not num_list or goal < 0:
        contig.clear()
        return False
    elif goal == 0:
        return True
    else:
        contig.append(num_list[0])
        return check_contiguous(num_list[1:], goal-num_list[0], contig)

def problem_1(nums, period):
    for i in range(period, len(nums)):
        if not check(nums[i-period:i], nums[i]):
            return nums[i]
    return None

def problem_2(num_list, period, sum):
    for i in range(len(num_list)):
        for n in num_list[i-period:i]:
            contig = []
            if check_contiguous(num_list[i-period:i], sum, contig):
                return max(contig) + min(contig)
    return None

with open('2020/dec_09/input.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip('\n')) 

    # print('Practice 1: ', problem_1(lines, 5))
    # print('Practice 2: ', problem_2(lines, 5, 127))
    
    p1 = problem_1(lines, 25)
    print('Problem 1: ', p1)
    print('Practice 2: ', problem_2(lines, 25, p1))