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
game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice>=3 or user_choice<0:
    print("you entered the ivalid number! you loose")
else:
   print(game_images[user_choice])



computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])


if computer_choice==0 and user_choice==1:
    print("you loose")
elif computer_choice==1 and user_choice==2:
    print("you win")
elif computer_choice==3 and user_choice==1:
    print("you win")
elif computer_choice==user_choice:
    print("its draw")
elif computer_choice==1 and user_choice==0:
    print("you win")
elif computer_choice==2 and user_choice==1:
    print("you loose")
elif computer_choice==1 and user_choice==3:
    print("you loose")