import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# print(rock)
choices = ["rock", "paper", "scissors"]

user_choice = int(input('what do you choose? type 0 for Rock 1 for Paper or 2 for Scissors. '))


def check_choice(user_choice):
    if user_choice < 0 or user_choice > 2:
        print("Please type a valid value")
        exit()
    

print(check_choice(user_choice))

computer_choice = random.randint(0, 2)
     

# user_choice_means = ''
# computer_choice_means = ''

user_choice_means = choices[user_choice]
computer_choice_means = choices[computer_choice]

who_is_winner = ''

if computer_choice == 0 and user_choice == 1:
    who_is_winner = 'winner: YOU'
elif computer_choice == 1 and user_choice == 2:
    who_is_winner = 'winner: YOU'
elif computer_choice == 2 and user_choice == 0:
    who_is_winner = 'winner: YOU'
elif computer_choice == user_choice:
    who_is_winner = 'DRAW'
else:
    who_is_winner = 'winner: COMPUTER'        
    

print(f' you choise {user_choice} means: {user_choice_means} and computer choise {computer_choice} means: {computer_choice_means} then {who_is_winner} ')

