weight = float(input("Please enter the weight "))
height = float(input("Please enter the height "))

bmi = round((weight/(height ** 2)), 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi} and you are perfectly normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi} and you are slightly overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi} and you are obse")
else:
    print(f"Your bmi is {bmi} and you are clinically obse")
