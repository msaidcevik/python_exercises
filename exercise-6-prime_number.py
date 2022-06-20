"""
To improve your control flow statement skills and to raise your awareness of some algebraic knowledge.

    **Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

    The examples of the desired output are as follows :

    input →  19 ⇉ output : 19 is a prime number
    input →  10 ⇉ output : 10 is not a prime number
"""
# Solution-1
number = int(input("Enter a number: "))
count = 0

for i in range(2,number):
    if number % i == 0:
        count += 1
        break

if count == 0:
    print(f" {number} is a prime number.")

else:
    print(f" {number} is not a prime number.") 

# Solution-2
number = int(input("Enter a number: "))
x = number - 1
while x > 1:
    if number % x == 0:
        print(f" {number} is not a prime number.")
        break
    else:
        x -= 1
else:
    print(f" {number} is a prime number.") 
