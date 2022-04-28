"""
placeholder name include in the letter template
a list of names in a separate txt file
generate a bunch of letters for each name in the list, ready to be printed
"""

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt, Replace the [name] placeholder with the actual name.
# return the content inside invited_names.txt file as a list
# remove the some characters from string
# replace a specific text inside a string
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.readlines()

for name in invited_names:
    edited_name = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_for_{edited_name}.txt", mode="w") as letter:
        letter.write(letter_template.replace(PLACEHOLDER, edited_name))


