
row1 = [ "😀", "😄", "😆" ]
row2 = [ "😀", "😄", "😆" ]
row3 = [ "😀", "😄", "😆" ]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
pos = int(input("Where do you want to put the treasure? (type 12 for column 1 and row 2)\n"))

unit = int(pos % 10)
ten = int(pos / 10)

if (unit < 1) or (unit > 3):
    print("Invalid row value, should be in the range of 1-3\n")
elif (ten < 1) or (ten > 3):
    print("Invalid column value, should be in the range of 1-3\n")
else:
    map[unit-1][ten-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
