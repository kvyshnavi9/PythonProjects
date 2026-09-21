import random
import data
import art

game_over = False
sum =0

def random_value():
    return random.choice(data.data)

def compare(person):
    return person["followers_million"]
        
print(art.logo)
while not game_over:
    value1 = random_value()
    value2 = random_value()

    # Make sure A and B aren't the same person
    while value2 == value1:
        value2 = random_value()
    print(f"Compare A: {value1['name']}, {value1['profession']}, {value1['country']}")
    print(art.vs)
    print(f"Against B: {value2['name']}, {value2['profession']}, {value2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B':")
    if choice == "A":
        if compare(value1)> compare(value2):
            sum+= 1
        else:
            print(f"You won {sum} times")
            game_over = True  
    elif choice == "B":
        if compare(value2)> compare(value1):
            sum+= 1
        else:
            print(f"You won {sum} times")
            game_over = True  
    else:
        print("Invalid choice. Please type 'A' or 'B'.")
        
    
    
        
        
        
        
        