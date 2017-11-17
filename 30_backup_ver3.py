import os
import time
# 1.需要备份的目录被指定于一个列表
# 如果路径中有空格，需要用双引号
source = [r"D:\Code\LearningPython\HelloWorld", r"D:\Code\SunBath"]

# 2.非分文件存储于一个目录中
target_dir = r"D:\Code\Backup"

# 3.备份需要打包成zip
# 4.zip的文件名为时间，文件夹为日期
today = time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
dir_today = target_dir + os.sep + today


# 键入注释以补充命名
comment = input('Enter a comment--->')
# 检查是否录入注释
if len(comment) == 0:
    target = dir_today + os.sep + now + '.zip'
else:
    target = dir_today + os.sep + now + '_' + comment.replace(' ', '_')+'.zip'
# 检查用于存放的目录是否存在 创建
if not os.path.exists(dir_today):
    os.mkdir(dir_today)
    print('directory created', dir_today)

# 使用zip命令打包
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份程序
print('zip command is:')
print(zip_command)
print('running')
if os.system(zip_command) == 0:
    print('back up to', target)
else:
    print('failed')
