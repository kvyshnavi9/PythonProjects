import random

def number_guessing_game(number, retry):
    game_over = False
    print(f"you have {retry} times remaining to guess the number")
    while not game_over:
        if retry ==0:
            game_over = True
            print("You Couldn't guess the number. You lost the game!")
        n = int(input("Make a guess:"))
        if n > number:
           print("Too high \nGuess again")
           retry-= 1
           print(f"You have {retry} times remaining")
        elif n < number:
            print("Too low \nGuess again")
            retry-= 1
            print(f"You have {retry} times remaining")
        elif n == number:
            print(f"You guessed correctly {number}. You Won!")
            
print("Welcome to the Number Guessing game!\n")
print("I'm thinking of a number between 1 and 100")
number = random.choice(range(1,101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
retry =0

if difficulty == 'easy':
   retry =10
else:
    retry = 5
    
number_guessing_game(number,retry)      
           