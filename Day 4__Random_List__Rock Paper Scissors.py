import random
seed = int(input("Create a seed number: "))
random.seed(seed)
result = random.randint(0,1)
if result == 1:
    print("Heads")
elif result == 0:
    print("Tails")
====================================================================
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_people = len(names)
print(names[random.randint(0, number_people - 1)] + " is going to buy the meal today!")
print(random.choice(names) + " is going to buy the meal today!")
====================================================================
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
first_digit = int(position[0])
second_digit = int(position[1])
map[second_digit - 1][first_digit - 1] = 'X'
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


====================================================================
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_choices = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if your_choice < 0 or your_choice > 2:
  print("You type an invalid number! You lose.")
else:
  print(game_choices[your_choice])

  # now computer's turn
  print("Computer choose:")
  computer_choice = random.randint(0, 2)
  print(f"{computer_choice}")
  print(game_choices[computer_choice])
  
  # now apply rock-paper-scissors rule here 0>2>1>0
  tmp = your_choice - computer_choice
  if tmp == 0:
    print("Draw")
  elif tmp == 1 or tmp == -2:
    print("You win")
  elif tmp == -1 or tmp == 2:
    print("You lose")
