PLACEHOLDER = "[name]"
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
#print(letter_content)

# The readlines() method returns a list containing each line in the file as a list item.
#
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# strip() Method: Remove spaces at the beginning and at the end of the string.
# e.g.
#    txt = "     banana     "
#    x = txt.strip()
#    print("of all fruits", x, "is my favorite")



