# 04.02.21
# Timer decorator function

import time

def Timer(function):
    def clock(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        runtime = end - start
        time.sleep(0.5)
        print(f"Time-displacement took {runtime} seconds to compute.")
        return result
    return clock

@Timer
def TimeThis(function, *args):
    return function(*args)