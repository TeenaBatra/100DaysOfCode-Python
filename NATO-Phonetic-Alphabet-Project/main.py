import pandas

# Create a dictionary with the NATO phonetic alphabet
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of phonetic codes for a word input by the user
is_game_on = True
while is_game_on:
    user_input = input("Enter a word:").upper()
    try:
        # Create a list of tuples with the letter and its corresponding phonetic code
        phonetic_list = [(ltr, nato_dict[ltr]) for ltr in user_input]
    except KeyError:
        # Handle non-alphabetic characters
        print("Sorry, only alphabets are allowed.")
    else:
        print(phonetic_list)
        is_game_on = False
