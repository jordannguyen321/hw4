import time

def timestamp(func):
    def inside(*args, **kwargs):
        newTime = time.ctime()
        print(newTime)
        final = func(*args, **kwargs)
        return final
    return inside
