import random

print("Create a program which takes name as input and randomly tell who is going to pay the bill")

attendy = input("Please enter the list of attende comma separated \n")

names = attendy.split(',')

chossen_one = names[random.randint(0, len(names)-1)]

#Below is simplar code for the same problem
#chossen_one = random.choice(names)

print(f"{chossen_one} will pay the bill")

