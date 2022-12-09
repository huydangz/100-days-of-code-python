student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for thing in student_scores:
    score = student_scores[thing]
    if score in range(91, 101):
        student_grades[thing] = "Outstanding"
    if score in range(81, 91):
        student_grades[thing] = "Exceeds Expectations"
    if score in range(71, 81):
        student_grades[thing] = "Acceptable"
    if score <= 70:
        student_grades[thing] = "Fail"
print(student_grades)
====================================================
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


====================================================
from auction_reference import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")

def find_max_bidders(dict_bids):
  max_bid = 0
  list_winners = ""
  for bidder in dict_bids:
    if max_bid < dict_bids[bidder]:
      max_bid = dict_bids[bidder]
  for bidder in dict_bids:
    if dict_bids[bidder] == max_bid:
      if list_winners == "":
        list_winners += bidder
      else:
        list_winners += ", " + bidder
  if "," not in list_winners:
    print(f"The winner is {list_winners} with a bid of ${max_bid}")
  else:
    print(f"The winners are {list_winners} with a bid of ${max_bid}")    

dict_bids = {}
yes = "yes"
while yes == "yes":
  name = input("What is your name? ")
  bid = int(input("What's your bid: $"))
  dict_bids[name] = bid
  yes = input("Are ther any other bidders?. Type 'yes' or 'no'.\n")
  clear()

find_max_bidders(dict_bids)
===================auction_reference.py =================================
logo = '''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''