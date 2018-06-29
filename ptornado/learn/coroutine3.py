#! /usr/bin/python
import random
from time import sleep

def stu_fib(n):
    index=0
    a,b=0,1
    while index < n:
        sleep_cnt  = yield b
        print("I will sleep %s seconds." % sleep_cnt)
        sleep(sleep_cnt)
        a, b = b, a + b
        index = index + 1


def copy_fib(n):
    print('i am a copy.')
    yield from stu_fib(n)




sfib = copy_fib(20)
ret = next(sfib)

while True:
    print(ret)
    try:
        ret = sfib.send(random.uniform(0, 2))
    except StopIteration:
        break


