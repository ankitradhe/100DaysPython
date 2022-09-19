print("Welcome to love calculator")
name1 = input("Please enter first name? \n").lower()
name2 = input("Please enter second name? \n").lower()


unit = 0
ten = 0
word = "love"

for i in word:
    unit += name1.count(i)
    unit += name2.count(i)

word = "true"

for i in word:
    ten += name1.count(i)
    ten += name2.count(i)

sum = ten*10 + unit


if sum < 10 or sum > 90:
    print(f"Your score is {sum}, you got together like coke and mentos")
elif sum >= 40 and sum <= 50:
    print(f"Your score is {sum}, you are alright together")
else:
    print(f"Your score is {sum}")

