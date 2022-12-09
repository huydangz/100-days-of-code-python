import math
def paint_calc(height, width, cover):
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
=======================================================
def prime_checker(number):
    count = 0
    for n in range(1, number + 1):
        if number % n == 0:
            count += 1
    if count > 2:
        print("It's not a prime number.")
    elif count == 2:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


=======================================================
from replit import clear
from caesar_reference import logo, alphabet

def caesar(choice, message, shift):
  result = ""
  for letter in message.lower():
    if letter in alphabet:
      i = alphabet.index(letter)
      if choice == "encode":
        i += shift
      elif choice == "decode":
        i -= shift
      if i >= len(message) or i < -len(message):
          i = i % 26
      result += alphabet[i]
    else:
      result += letter
  print(f"Here's the {choice}d result: {result}")
    
yes = "yes"
while yes == "yes":
  clear()
  print(logo)
  choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  message = input("Type your message:\n")
  shift = int(input("Type your shift number:\n"))
      
  caesar(choice, message, shift)

  yes = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if yes !="yes":
    print("Goodbye and see you later.")
    
=================== caesar_reference.py ====================================
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
