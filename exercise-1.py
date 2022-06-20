"""
💡Objective:
To improve your arithmetic algorithm and problem solving skills.
Write a Python code on your Playground/IDE and submit your code (answer) as a plain text.
Problem : If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?
"""

money = 1000
rate_per_day = 0.07
day_number = input('Enter day number: ')
result_money = (money * ((1 + rate_per_day)) ** float(day_number))
print(result_money)
