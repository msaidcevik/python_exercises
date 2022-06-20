"""
Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

        **The desired output is like this:
        fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""
# Solution-1

def fib(n):  # The desired output is found for n=9.
    fib_list =[0, 1]
    for x in range(n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    fib_list.remove(0) # I removed 0 because 0 in fib_list.
    print(fib_list)

# Solution-2
fibo=[1,1]
for i in range(8):
  fibo.append(fibo[i]+fibo[i+1])
fibo
