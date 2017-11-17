shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# 索引运算符
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item -1 is', shoplist[-1])
print('Character 0 is', name[0])

# 对list切片
print('item 1 to 3 is', shoplist[1:3])
print('item start to end is', shoplist[:])
print('item 2 to -1 is', shoplist[2:-1])

# 对string切片
print('character 1 to 3 is', name[1:3])

# 可以引入步长
print(shoplist[::3])
print(shoplist[::-1])
