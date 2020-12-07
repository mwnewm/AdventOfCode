def readRules(rules):
    tree = {}
    for rule in rules:
        bag = rule.split(' contain ')
        contains = bag[1].strip('.\n').replace(' bags', '').replace(' bag', '').split(', ')
        bagName = bag[0].replace(' bags', '').replace(' bag', '')
        child_tree = {}
        for item in contains:
            words = item.split(' ')
            if words[0].isdigit():
                child_tree[' '.join(words[1:])] = int(words[0])
            else:
                child_tree[item] = 0
        tree[bagName] = child_tree
    return tree

def traverse(tree, children, goal):
    if 'no other' in children:
        return False
    elif goal in children:
        return True
    else:
        return any(traverse(tree, tree[i].keys(), goal) for i in children)

def problem_1(tree, goal):
    sum = 0
    for key in tree.keys():
        if traverse(tree, tree[key].keys(), goal):
            sum += 1
    return sum

def problem_2(tree, curr):
    if curr == 'no other':
        return 0
    children = tree[curr]
    return sum(tree[curr].values()) + sum(tree[curr][i]*problem_2(tree, i) for i in children.keys())

with open('2020/dec_07/input.txt', 'r') as file:
    rules = file.readlines()
    tree = readRules(rules)

    print('Problem 1: ', problem_1(tree, 'shiny gold'))
    print('Problem 2: ', problem_2(tree, 'shiny gold'))