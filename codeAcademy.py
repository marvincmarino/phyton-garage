# coding=utf-8
import math

# test if a number is prime
# in code academy breaks for x = -10, error:
# Oops, try again. Your function fails on is_prime(-10). It returns True when it should return False.

def is_prime(x):
    for i in range(2, x-1):
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