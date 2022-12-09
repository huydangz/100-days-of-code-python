import random
from replit import clear
from art import logo
print(logo)
print("Welcome to the Number Guessing Name!")
print("I'm thinking of a number between 1 and 100.")
keep_playing = True
while keep_playing:
  result = random.randint(1, 100)
  print(result)
  attemps = 10
  if input("Choose a difficult lever, type 'ease' or 'hard': ") == "hard":
    attemps = 5
  while attemps > 0:
    print(f"You have {attemps} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == result:
      print(f"You got it! The answer was {result}")
      attemps = 0
    else:
      if guess < result:
        print("Too low")
      elif guess > result:
        print("Too high")
      #both cases
      attemps -= 1
      if attemps == 0:
        print("You run out of guesses. You lose!")
      else:
        print("Guess again")
  if input("Run again? 'y' or 'n': ") != "y":
    keep_playing = False
  clear()
  
========================== art.py ===============================
logo = '''

                             _   _                                  _               
  __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/                                                                              
'''  