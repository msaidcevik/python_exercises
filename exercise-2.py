"""
💡Objective:
To improve your arithmetic algorithm and knowledge of several functions skills.
Task-1:

Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.
Task-2:
Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.
"""
Celsius = float(input('Please enter Celsius degree: '))
Fahrenheit = (Celsius * 1.8) + 32
print(f"{Celsius} degree is: {Fahrenheit} fahrenheits.")

# TASK 2
Kilometer = float(input('Please enter Kilometer: '))
Mile = Kilometer * 0.6214
print(f"{Kilometer} km is: {Mile} miles.")

