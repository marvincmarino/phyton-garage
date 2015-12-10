# coding=utf-8
import math

# test if a number is prime
# in code academy breaks for x = -10, error:
# Oops, try again. Your function fails on is_prime(-10). It returns True when it should return False.

import math

# test if a number is prime

def is_prime(x):
    exceptions = [0,1]
    if x in exceptions:
        return False
    for i in range(x, x-1):
        result = x / float(i) # trick to get result as float
        check = result - math.floor(result)
        if check == 0:
            print("Is not prime.")
            return False
            break
        else:
            i += 1
    print("Is prime.")
    return True

number = int(raw_input("Enter a number:"))
is_prime(number)