two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum = first_digit + second_digit
print(sum)
====================================================================
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
float_height = float(height)
float_weight = float(weight)
bmi = float_weight/(float_height**2)
print(int(bmi))
====================================================================
age = input("What is your current age?")
int_age = int(age)
days = (90 - int_age) * 365
weeks = (90 - int_age) * 52
months = (90 - int_age) * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

================================================================================
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What is the percentage tip would you like to give? 10, 12 or 15? "))
num = int(input("How many people to split the bill? "))

bill += bill * tip / 100
each_paid = round(bill/num, 2)

print(f"Each person should pay: ${each_paid}")
print("Each person should pay: $" + "{:.2f}".format(each_paid))