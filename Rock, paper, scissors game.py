import random

user_choice = input("Choose rock, paper, or scissors:").lower()

computer_choice = random.choice(['rock','paper','scissors'])

print("You choose:", user_choice)
print("computer choose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win") 
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win")
else:
    print("You lose")               