"""
Task : Print the Fizz Buzz numbers.

        -Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.

-Print numbers from 1 to 100 inclusively following these instructions:
        
        1- if a number is multiple of 3, print "Fizz" instead of this number,
        2- if a number is multiple of 5, print "Buzz" instead of this number,
        3- for numbers that are multiples of both 3 and 5, print "FizzBuzz",
        4- print the rest of the numbers unchanged.
        
Output each value on a separate line.
"""
num = list(range(1, 101))
    
for i in num:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=' ')
            
    elif i % 5 == 0 :
        print("Buzz", end=" ")
            
    elif i % 3 == 0:
        print("Fizz", end=" ")
            
    else:
        print(str(i), end=" ")
