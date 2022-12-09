def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month == 2 and is_leap(year):
      return 29
  else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
===============================================================

from replit import clear
from art import logo

def calculator_result(num1, opt, num2):
  """Return result with operation opt between num1 and num2"""
  result = 0
  if opt == '+':
      result = num1 + num2
  elif opt == '-':
      result = num1 - num2
  elif opt == '*':
      result = num1 * num2
  elif opt == '/':
      result = num1 / num2
  return result

y = "n"
while y == "n":
  print(logo)
  num1 = float(input("What's the first number?: "))
  print("+\n-\n*\n/")

  y = "y"
  while y == "y":
    opt = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = calculator_result(num1, opt, num2)
    print(f"{num1} {opt} {num2} = {result}")
    num1 = result
    y = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation, or type 'e' to exit: ")
  clear()

==================== art.py =========================================
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""