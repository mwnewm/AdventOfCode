def problem_1(groups):
    total_qs = 0
    for group in groups:
        group_qs = set()
        for person in group:
            group_qs = group_qs.union(set(person))
        total_qs += len(group_qs)
    return total_qs

def problem_2(lines):
    total_qs = 0
    for group in groups:
        common_qs = set()
        for i, person in enumerate(group):
            if i == 0:
                common_qs.update(set(person))
            else:
                common_qs = common_qs & set(person)
        total_qs += len(common_qs)
    
    return total_qs


with open('2020/dec_06/input.txt') as file:
    lines = file.readlines()

    groups = list()
    curr_group = list()
    for line in lines:
        if line == '\n':
            groups.append(curr_group)
            curr_group = list()
        else:
            line = line.strip('\n')
            curr_group.append(line)
    groups.append(curr_group)
    
    print('Problem 1: ', problem_1(groups))
    print('Problem 2: ', problem_2(groups))