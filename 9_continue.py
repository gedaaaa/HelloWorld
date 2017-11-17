while True:
    s = input('enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('太少了')
        continue
    print('字数差不多')
