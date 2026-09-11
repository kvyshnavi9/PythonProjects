import logo
import os

print(logo.auction_logo)
print("Welcome to the secret auction program.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


bid_dict = {}

name = input("Enter your name? \n")
amount = int(input("Enter the bid amount:\n$"))

bid_dict [name] = amount

should_cont = False

while not should_cont:
    res = input("Are there any other bidders. Type 'yes' or 'no' \n").lower()
    if res == "yes":
        clear_screen()
        name = input("Enter your name? \n")
        amount = int(input("Enter the bid amount:\n$"))

        bid_dict [name] = amount
    else:
        should_cont = True

greater_key = ""   
greater_value = 0  
for key, value in bid_dict.items():
   if value > greater_value:
       greater_value = value
       greater_key = key
       
print(f"Auction winner is {greater_key} {greater_value}")
