number = 23
running = True

while running:
    guess = int(input('enter an integer:'))

    if guess == number:
        print('对了')
        # 把running设为False结束while
        running = False
    elif guess < number:
        print('小了')
    else:
        print('大了')
else:
    print('循环完毕')
print('结束')
