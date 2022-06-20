"""
Task : Print the prime numbers which are between 1 to entered limit number (n).

        1-You can use a nested for loop.
        2-Collect all these numbers into a list
        3-The desired output for n=100 :

This is the desired output.
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
m = 1 
n = 100 
prime_numbers = []  
for num in range(m, n + 1):  
   if num > 1:  
       for i in range(2, num):  
           if (num % i) == 0:  
               break  
       else:  
           prime_numbers.append(num)
print(prime_numbers)

