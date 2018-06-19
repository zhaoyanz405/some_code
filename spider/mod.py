# -*- coding: utf-8 -*-

import sys
import signal
import functools


class TimeoutError(Exception): pass


def timeout(seconds, error_msg="TimeoutError: the function has not finished in NNNN seconds"):
    def decorated(func):
        result = ""

        def _handle_timeout(signum, frame):
            global result
            result = error_msg  
            raise TimeoutError(error_msg)

        def wrapper(*args, **kwargs):
            global result
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                return result

            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(5)
def slowfunc(sleep_time):
    a = 1
    import time
    time.sleep(sleep_time)
    return a

if __name__ == "__main__":
    print(slowfunc(11))