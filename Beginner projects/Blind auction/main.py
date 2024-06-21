from art import logo

from replit import clear

print(logo)

print("Welcome to the secret auction program. ")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
bidders = {}
bidding = False
while not bidding:
  bidders[name] = bid
  other_bidders = input(
      "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if other_bidders == "yes":
    clear()
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
  elif other_bidders == "no":
    bidding = True

highest_bid = 0
for bid in bidders:
  
  bid_amount = bidders[bid]
  if bid_amount > highest_bid:
    highest_bid = bidders[bid]
    winner = bid

print(f"The winner is {winner} with a bid of {highest_bid}$")
