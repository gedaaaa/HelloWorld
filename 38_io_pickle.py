import pickle

# 存储所用的文件的名称
shoplistfile = 'shoplist.data'
# 清单内容
shoplist = ['apple', 'mango', 'carrot']

# 准备写入
f = open(shoplistfile, 'wb')
# 转储
pickle.dump(shoplist, f)
f.close()

# 删除shoplist
del shoplist

# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 载入
storedlist = pickle.load(f)
print(storedlist)
