number = input('Enter numbers, using any separator: ')
separators = ''
numbers = ''

for character in number:
    if not character.isnumeric():
        separators = separators + character
    else:
        numbers = numbers + character

print(f'Separators = {separators}')
print(f'Numbers = {numbers}')
