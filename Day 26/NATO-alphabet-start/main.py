import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets = {row.letter: row.code for (index, row) in nato_df.iterrows()}

word = input("Enter a word: ")

result = [alphabets[letter.upper()] for letter in word]
print(result)
