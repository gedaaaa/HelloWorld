print('Simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist只是指向同一对象的另外一个名称
mylist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
print('两个列表一样')

print('通过切片制作副本')
mylist = shoplist[:]
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
print('两个列表不一样')
