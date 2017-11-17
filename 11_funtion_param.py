def print_max(a, b):
    if a > b:
        print(a, '比较大')
    elif a == b:
        print(a, '等于', b)
    else:
        print(b, '比较大')


# 可以直接用字面值
print_max(3, 4)

# 可以利用参数传递变量

x = 5
y = 7

print_max(x, y)
