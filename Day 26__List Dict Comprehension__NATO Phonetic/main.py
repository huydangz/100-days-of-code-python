import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}

word = input("Enter a name: ")
answer = [dict_alphabet[letter.title()] for letter in word]
print(answer)