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

import random
import sys
print("Let\'s play rock, paper or scissors game!!!")
choice=input("what do you want to choose?\n1. Rock \n2. Paper \n3. Scissors\n")
if choice=="1":
  print(rock)
elif choice=="2":
  print(paper)
elif choice=="3":
  print(scissors)
else:
  sys.exit("Not an option!")
  
print("Computer Chooses:\n")
computer_choice=str(random.randint(1,4))
if computer_choice=="1":
  print(rock)
elif computer_choice=="2":
  print(paper)
elif computer_choice=="3":
  print(scissors)

if (choice=="1" and computer_choice=="3") or (choice=="2" and computer_choice=="1") or (choice=="3" and computer_choice=="2"):
  print("You wins!")
elif (choice=="1" and computer_choice=="2") or (choice=="2" and computer_choice=="3") or (choice=="3" and computer_choice=="1"):
  print("You loses!")
else:
  print("Draw!!")

