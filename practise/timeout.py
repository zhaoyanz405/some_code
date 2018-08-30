import signal
import time


def t(x, y):
    raise RuntimeError


def test(timeout):
    try:
        signal.signal(signal.SIGALRM, t)
        signal.alarm(timeout)
        time.sleep(10)
        signal.alarm(0)
        print('i am awake in 10 s')
    except RuntimeError:
        print('time out .')
