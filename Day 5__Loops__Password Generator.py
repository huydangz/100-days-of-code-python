student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num = 0
sum = 0
for height in student_heights:
    num += 1
    sum += height

average = round(sum / num)
print(f"{average}")
===================================================================
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = student_scores[0]
for score in student_scores:
    if score > max:
        max = score
print(f"The highest score in the class is: {max}")
===================================================================
res = 0
for n in range(1,101):
    if n % 2 == 0:
        res += n
print(f"{res}")
===================================================================
for n in range(1, 101):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(f"{n}")

===================================================================        
import string
import random

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# ## Easy level print sequencely

password = ""
for l in range(0, nr_letters):
	password += random.choice(letters)
for s in range(0, nr_symbols):
	password += random.choice(symbols)
for n in range(0, nr_numbers):
	password += random.choice(numbers)

print("Here is your password: " + password)

### Hard level print completely random order

password = []

for n in range(nr_letters):
  password.append(random.choice(letters))
for n in range(nr_symbols):
  password.append(random.choice(symbols))
for n in range(nr_numbers):
  password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
print("Here is your password:" + ''.join(password))        