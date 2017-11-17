def print_max(x, y):
    '''Prints the maximum of two numbers.

    They must be integers'''
    # 如果可能，则转变为整型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, '更大')

    else:
        print(y, '更大')


print_max(3, 5)
print(print_max.__doc__)
