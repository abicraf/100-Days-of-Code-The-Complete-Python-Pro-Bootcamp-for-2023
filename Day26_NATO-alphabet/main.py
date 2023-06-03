import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    #print(key)
    pass


student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato)
nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")
user_input_char = [char.upper() for char in user_input]
#print(user_input_char)

# Solution A:
#
# phaonetic = []
# for char in user_input_char:
#     for nato_key in nato_dict.keys():
#         if char == nato_key:
#             phaonetic.append(nato_dict[char])
#
#
# Rephrase it by List comprehension:
#
#phaonetic = [nato_dict[char] for char in user_input_char for nato_key in nato_dict.keys() if char == nato_key]


# Solution B:
phaonetic = [nato_dict[char] for char in user_input_char]
print(phaonetic)

