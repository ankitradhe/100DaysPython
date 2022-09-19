import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = [ rock, paper, scissor ]
com_choise = random.randint(1,3)

choice = int(input("Welcome to RPS game, please type '1' for Rock, '2' for Paper and '3' for Scissors\n"))

if (choice < 1) or (choice > 2):
    print("Invalid choice, should be in a range of 1-3")
else:
    print('You chosse' + art[choice - 1])
    print('Computer chosse' + art[com_choise-1])
    if com_choise == choice:
        print("Its a Draw!!!")
    elif 1 == com_choise and 3 == choice:
        print("YOU LOSSE, Rock beats Scissor, better luck next time")
    elif 2 == com_choise and 1 == choice:
        print("YOU LOSSE, Paper beats Rock, better luck next time")
    elif 3 == com_choise and 2 == choice:
        print("YOU LOSSE, Scissor beats Paper, better luck next time")
    else :
        print("You win!!!")


