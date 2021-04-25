# 04.02.21
# Timer decorator function

import time

def Timer(function):
    def clock(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"The function {function.__name__} took {runtime} seconds to complete")
        return result
    return clock

@Timer
def TimeThis(function, *args):
    return function(*args)