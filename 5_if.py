number = 23
guess = int(input('input an integer'))

if guess == number:
    # 新块
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 块结束
elif guess < number:
    print('小了')
else:
    print('大了')
print('结束')
# 最后一句将在if结束后执行
