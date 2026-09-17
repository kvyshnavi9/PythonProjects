import logo
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    """
    return a random card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    #easiest way - sum fn takes a lit and sum the values form left to right
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "User Lost!"
    elif user_score == 0:
        return "User Won!"
    elif user_score > 21 :
        return "User Lost!"
    elif computer_score > 21:
        return "Computer Lost!"
    else:
        if user_score > computer_score:
            return "User Won!"
        else:
            return "Computer Won!"
        
        
def play_game():
    is_game_over = False   
    print(logo.jackman_logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score= calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User Cards: {user_cards} - user score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")  
    
        if user_score>21 or computer_score== 0 or user_score == 0 :
            is_game_over = True
        else:
            proceed= input("Type 'y' to get another card, type 'n' to pass \n")
            if proceed == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
            
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card)     

    print(f"User Final Cards and Scrore : {user_cards} - {user_score}") 
    print(f"Computer Final Cards and Scrore : {computer_cards} - {computer_score}") 
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    clear_screen()
    play_game()