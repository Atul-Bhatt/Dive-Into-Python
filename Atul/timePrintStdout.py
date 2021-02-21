import time
import sys


def time_print():
    print('This is print...')
    start = time.time()
    for i in range(1000000):
        print('', end='')
    end = time.time()
    print('{:.10f}'.format(end - start))


def time_stdout():
    sys.stdout.write('This is stdout...')
    start = time.time()
    for i in range(1000000):
        sys.stdout.write('')
    end = time.time()
    sys.stdout.write('\n{:.10f}'.format(end - start))


time_print()
time_stdout()
