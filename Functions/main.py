import time


def speed_calc_decorator(function):
    def wrapper_function():
        time_before = time.time()
        function()
        time_after = time.time()
        return time_after-time_before
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_speed = fast_function()
print("Speed of Fast Function ", fast_speed)
slow_speed = slow_function()
print("Speed of Slow Function ", slow_speed)

speed_difference = slow_speed - fast_speed
print("Speed Difference =", speed_difference)
