import time


def times(function):
    def time_time(*args):
        start = time.time()
        function(*args)
        return str(time.time() - start) + " seconds"

    return time_time


@times
def func(a, b):
    return a + b


print(func(10, 5))

