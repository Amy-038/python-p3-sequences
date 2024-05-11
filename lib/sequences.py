#!/usr/bin/env python3

def print_fibonacci(length):
    list = []

    for n in range(length):
        if n == 0:
            list.append(0)
        elif n == 1:
            list.append(1)
        else:
            f = list[-1] + list[-2]
            list.append(f)
    
    print(list)

print_fibonacci(9)