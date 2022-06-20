"""
To improve your defining function skills and get familiar with the recursion concept.

        -Define a function named my_fact to calculate factorial of the given number. Given a non-negative integer return the factorial of the integer.

(Example: The factorial of 5 is: 5*4*3*2*1 = 120 and factorial of 0 is: 1)
"""

def my_fact(n):
    multip = 1
    for i in range(1, n+1):
        if n == 0:
            return 1
        else:
            multip *= i
    return multip
    
