import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_alphabets[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()

