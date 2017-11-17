def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组
    for num in numbers:
        print('元组记录了', num)
    # 遍历字典
    for a, b in phonebook.items():
        print(a, b)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
