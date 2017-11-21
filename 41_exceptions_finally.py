import sys
import time
f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("press keyboardinterrupt now")
        time.sleep(2)

except IOError:
    print("not found")
except KeyboardInterrupt:
    print('reading cancelled')
finally:
    if f:
        f.close()
    print('file closed')
