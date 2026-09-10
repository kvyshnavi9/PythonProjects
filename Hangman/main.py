import random
import hangman_art
import  hangman_words

#Step1: Generate a random word
 
chosen_word = random.choice(hangman_words.word_list)

print(chosen_word)

#step2 - create blank ex: hi then 2 blanks( __ )
placeholder = ""
for n in chosen_word:
    placeholder+= "_"
    
print(placeholder)

#step3: Ask user to guess the letter
game_over = False
lives = 6
print(lives)

while not game_over:
    guess = input("Guess the letter \n").lower()
    newdisplay = ""
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            lives+= 1
            newdisplay+= letter
        else:
            newdisplay+= placeholder[position]
    
    placeholder = newdisplay       
    print(placeholder)
    
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print(hangman_art.HANGMANPICS[lives])
            print("You Lose!")
        else:
            print(hangman_art.HANGMANPICS[lives])
        
    if not "_" in newdisplay:
        game_over = True
        print("You Win!")
            