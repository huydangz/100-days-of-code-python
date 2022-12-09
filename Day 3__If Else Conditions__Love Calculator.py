number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
====================================================================
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height**2)
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweigh.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")	
====================================================================
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap year.")
        else:
             print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
====================================================================
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
====================================================================
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()

word_true = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
word_love = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') + name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')
love_score = int(str(word_true) + str(word_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")