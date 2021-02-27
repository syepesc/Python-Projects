numbers = input("Please enter a series of numbers, using any separators you like, can include letters: ")

separators = ""  # separators array

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else " " for char in numbers).split()
print("Numbers:\t", list(values))
print("Sum:\t\t", sum([int(val) for val in values]))
