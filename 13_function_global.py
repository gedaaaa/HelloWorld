x = 50


def func():
    global x
    print('x is', x)
    x = 2
    print('change global x to', x)


func()
print('x now is', x)
