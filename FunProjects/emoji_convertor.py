user_input = input("Enter your message: ");

words = user_input.split(" ")  # split user input by espaces

emojis = {
    ":)": "😃",
    ":(": "😞",
    ":|": "😑"
}

output = ""
for word in words:
    output = output + emojis.get(word, word) + " "
print(output)
