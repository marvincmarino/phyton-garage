# coding=utf-8

# test if a number is prime

import math

def is_prime(x):
    if x <= 1:  # exceptions 1 and negative integers are not prime
        print("Is not prime.")
        return False
    for i in range(2, x):
        result = x / float(i)  # trick to get result as float
        check = result - math.floor(result)
        if check == 0:
            print("Is not prime.")
            return False
            break
        else:
            i += 1
    print("Is prime.")
    return True

# user input
number = int(raw_input("Enter a number:"))
is_prime(number)
