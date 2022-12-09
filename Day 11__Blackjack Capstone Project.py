from art import logo, colors
from replit import clear
import random

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def deal():
  deal = []
  deal.append(random.choice(cards))
  deal.append(random.choice(cards))
  return deal
  
def is_blackjack(your_cards):
  if len(your_cards) == 2 and your_cards.count("A") == 1 and (your_cards.count("10") == 1 or your_cards.count("J") == 1 or your_cards.count("Q") == 1 or your_cards.count("K") == 1):
    return True
  else:
    return False
    
def score(cards):
  score = 0
  for card in cards:
    if card == "A":
      if score <= 10:
        score += 11
      else:
        score += 1
    elif card == "J" or card == "Q" or card == "K":
      score += 10
    else:
      score += int(card)
  return score

def is_bust(cards):
  if score(cards) > 21:
    return True
  else:
    return False


def you_play(your_cards, dealer_cards):
  if is_blackjack(your_cards):
    print(f'{colors["blue"]}  Your final hand: {your_cards}, final score: Blackjack{colors["reset"]}')
  else:
    keep_get_card = True
    if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
      keep_get_card = False
    while keep_get_card:
      your_cards.append(random.choice(cards))
      print(f"  Your cards: {your_cards}, current score: {score(your_cards)}")
      print(f"  Computer's first card: ['{dealer_cards[0]}']")
    
      #Conditions for player finish get card
      if is_bust(your_cards) or input("Type 'y' to get another card, type 'n' to pass: ") == "n":
          keep_get_card = False

    #Player finalize and stop
    print(f'{colors["blue"]}  Your final hand: {your_cards}, final score: {score(your_cards)}{colors["reset"]}')


def dealer_play(your_cards, dealer_cards):
  #Case 1: Dealer blackjack -> no need get card
  if is_blackjack(dealer_cards):
    print(f'''{colors["red"]}  Computer's final hand: {dealer_cards}, final score: Blackjack{colors["reset"]}''')
    #Check player:
    if is_bust(your_cards):
      print("You went over. You LOSE.")
    elif is_blackjack(your_cards):
      print("DRAW.")
    else:
      print("You LOSE.")

  #Case 2: Dealer not blackjack (2 cases)
  else:
    #Case 2.1: player bust or blackjack  -> no need get card
    if is_bust(your_cards):
      print(f'''{colors["red"]}  Computer's final hand: {dealer_cards}, final score: {score(dealer_cards)}{colors["reset"]}''')
      print("You went over. You LOSE.")
    elif is_blackjack(your_cards):
      print(f'''{colors["red"]}  Computer's final hand: {dealer_cards}, final score: {score(dealer_cards)}{colors["reset"]}''')
      print("You WIN.")
    #Case 2.2: player normal --> must get card 
    else:
      while score(dealer_cards) <= 16:
        dealer_cards.append(random.choice(cards))
      #Finished getting cards
      print(f'''{colors["red"]}  Computer's final hand: {dealer_cards}, final score: {score(dealer_cards)}{colors["reset"]}''')
      y = score(your_cards)
      d = score(dealer_cards)
      if d > 21: #dealer bust
        print("Dealer went over. You WIN.")
      else:
        if y == d:
          print("DRAW.")
        elif y < d:
          print("You LOSE.")
        else:
          print("You WIN.")

#Start to playing with cards
keep_playing = True
while keep_playing:
  clear()
  print(logo)
  your_cards = deal()
  dealer_cards = deal()
  print(f"  Your cards: {your_cards}, current score: {score(your_cards)}")
  print(f"  Computer's first card: ['{dealer_cards[0]}']")
  
  #Turn of Player:
  you_play(your_cards, dealer_cards)
    
  #Turn of Dealer:
  dealer_play(your_cards, dealer_cards)
  
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
    keep_playing = False
  

========================== art.py =================================
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# colors
colors = {
  'reset': '\x1b[0m',
  'bold': '\x1b[1m',
  'italic': '\x1b[3m',
  'underline': '\x1b[4m',
  'inverse': '\x1b[7m',

  'black': '\x1b[30m',
  'red': '\x1b[31m',
  'green': '\x1b[32m',
  'yellow': '\x1b[33m',
  'blue': '\x1b[34m',
  'magenta': '\x1b[35m',
  'cyan': '\x1b[36m',
  'white': '\x1b[37m',
  'gray': '\x1b[90m',
  'bright_red': '\x1b[91m',
  'bright_green': '\x1b[92m',
  'bright_yellow': '\x1b[93m',
  'bright_blue': '\x1b[94m',
  'bright_magenta': '\x1b[95m',
  'bright_cyan': '\x1b[96m',
  'bright_white': '\x1b[97m',

  'bg_black': '\x1b[40m',
  'bg_red': '\x1b[41m',
  'bg_green': '\x1b[42m',
  'bg_yellow': '\x1b[43m',
  'bg_blue': '\x1b[44m',
  'bg_magenta': '\x1b[45m',
  'bg_cyan': '\x1b[46m',
  'bg_white': '\x1b[47m',
  'bg_gray': '\x1b[100m',
  'bg_bright_red': '\x1b[101m',
  'bg_bright_green': '\x1b[102m',
  'bg_bright_yellow': '\x1b[103m',
  'bg_bright_blue': '\x1b[104m',
  'bg_bright_magenta': '\x1b[105m',
  'bg_bright_cyan': '\x1b[106m',
  'bg_bright_white': '\x1b[107m'
}