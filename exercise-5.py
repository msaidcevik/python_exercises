"""
-An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number.
-Write a Python program that;
1-takes a positive integer number from the user,
2-checks the entered number if it is Armstrong,
3-consider the negative, float and any entries other than numeric values then display a warning message to the user.
"""
# Solution-1
number = input("Enter a number: ") # Please enter an integer number.
if float(number) < 0: # To show that the float input is invalid. 
    print("It is an invalid entry.")
elif float(number) > 0:
    digit = len(str(number))
    if digit == 3: # To see if 3-digit numbers are Armstong or not. 
        if int(number) == (int(number[0])**3)+(int(number[1])**3)+(int(number[2])**3):
# (int(number[0])**3) Especially the integer expression was made to get the power of the value in each digit. 
            print(f"{number} is an Armstrong number. ")
        else:
            print(f"{number} is not an Armstrong number. ")
    elif digit == 4: # To see if 4-digit numbers are Armstong or not.
        if int(number) == (int(number[0])**4)+(int(number[1])**4)+(int(number[2])**4)+(int(number[3])**4):
            print(f"{number} is an Armstrong number. ")
        else:
            print(f"{number} is not an Armstrong number. ")        
    else:
        print("It is an invalid entry.")

# Solution-2

while True:
    number = input("Enter a posotive number : ")
    digits = len(number)
    summ = 0
    
    if not number.isdigit():
        print(number, " is invalid entry. Please enter valid input.")
    elif int(number) >= 0:
        for i in range(digits):
            summ = summ + int(number[i]) ** digits    
        if summ == int(number):
            print(number, "is an Armstong Number.")
            break
        else:
            print(number, "is not an Armstrong Number.")
            break 
