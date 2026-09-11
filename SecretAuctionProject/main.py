import logo
import os

print(logo.auction_logo)
print("Welcome to the secret auction program.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

bid_dict = {}

bid_over = False

while not bid_over:
    name = input("Enter your name? \n")
    amount = int(input("Enter the bid amount:\n$"))
    
    bid_dict [name] = amount
    res = input("Are there any other bidders. Type 'yes' or 'no' \n").lower()
    if res == "yes":
        clear_screen()
    else:
        bid_over = True

greater_key = ""   
greater_value = 0  
for key, value in bid_dict.items():
   if value > greater_value:
       greater_value = value
       greater_key = key
       
print(f"Auction winner is {greater_key} {greater_value}")
