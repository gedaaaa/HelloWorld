# 尽量使用括号标记元祖的起始与结束
# 显式优于隐式
zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('number of cages in the new zoo is ', len(new_zoo))
print('all animals in new zoo are', new_zoo)
print('animals brought from the old zoo are', new_zoo[2])
print('last animal brought from old zoo is', new_zoo[2][2])
print('number of animals in new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))
