from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
from art import logo
print(logo)
#Empty dictionary
bids = {}
bidding_finished = False
#Function to find the highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
#Main program
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  #Adding a key and value to the dictionary
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()