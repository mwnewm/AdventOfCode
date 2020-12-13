# Chinese Remainder Theorem Starter Code
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i  # modified to round to the nearest integer
        sum += a_i * mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def problem_1(timestamp, ids):
    times = dict()
    for id in ids:
        if id != 'x':
            wait_time = (((timestamp // id)+1)*id) % timestamp
            times[wait_time] = id
    min_wait = min(times.keys())
    return times[min_wait]*min_wait

def problem_2(ids):
    a = []
    n = []
    for i, bus in enumerate(ids):
        if bus != 'x':
            a.append((-i) % bus)
            n.append(bus)
            # print('x = ', bus, '(mod ', (-i) % bus, ')')
    return chinese_remainder(n, a)

with open('2020/dec_13/input.txt') as file:
    timestamp = int(file.readline())
    ids_list = file.readline()
    ids = ['x' if x == 'x' else int(x) for x in ids_list.split(',')]

    print('Problem 1: ', problem_1(timestamp, ids))
    print('Problem 2: ', problem_2(ids))