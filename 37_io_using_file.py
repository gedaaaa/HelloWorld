poem = '''\
Programming is fun
When the work is done

if you wanna make your work also fun:
    use Python!
'''

# 打开文件来编辑 w stands for write
f = open('poem.txt', 'w')
# 项文件中写入
f.write(poem)
# 关闭文件
f.close()

# 没有附加参数时默认使用读操作 r stands for read
f = open('poem.txt')
while True:
    line = f.readline()
    # 通过零长度指示EOF
    if len(line) == 0:
        break
    print(line, end='')
f.close()
