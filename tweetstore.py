from threading import Lock

stacklock = Lock()
_stack = []

def push(tweet):
    try:
        stacklock.acquire(blocking=True)
        _stack.append(tweet)
    finally:
        stacklock.release()

def read():
    try:
        stacklock.acquire(blocking=True)
        return _stack[::-1]
    finally:
        stacklock.release()
