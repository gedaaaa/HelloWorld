age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 对于浮点数保留小数点后三位
print('{0:.3f}'.format(1.0 / 3))

# 使用下划线填充文本，并居中
print('{0:_^11}'.format('hello'))

# 基于关键词输出
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 指定以空白结尾，不换行
print('a', end='')
print('b', end='')

# 指定以空格结尾
print('a', end=' ')
print('b', end=' ')
print('c', end=' ')
