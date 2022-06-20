"""
Task : Find out the most frequent number and its frequency.

Write a program that;

-Finds out the most frequent number in the given list.
-Calculates its frequency.
-Prints out the result such as :

Given list numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3] 
Desired output the most frequent number is 3 and it was 4 times repeated
"""
numbers =[1, 3, 7, 4, 3, 0, 3, 6, 3]
print(f"The most frequent number {max(numbers, key = numbers.count)} and it was {numbers.count(max(numbers, key = numbers.count))} times repeated.)
