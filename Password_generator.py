#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# #easy version
# for num in range(0, nr_letters):
#   length = len(letters)
#   print(letters[random.randint(0, length-1)], end='')

# for num in range(0, nr_symbols):
#   length = len(symbols)
#   print(symbols[random.randint(0, length-1)], end='')

# for num in range(0, nr_numbers):
#   length = len(numbers)
#   print(numbers[random.randint(0, length-1)], end='')

# print('')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
# Use for loop to get letters, sympbols, numbers in the "password" string.
for num in range(0, nr_letters):
  # length = len(letters)
  # password.append(letters[random.randint(0, length-1)])
  password.append(random.choice(letters))

for num in range(0, nr_symbols):
  # length = len(symbols)
  # password.append(symbols[random.randint(0, length-1)])
  password.append(random.choice(symbols))

for num in range(0, nr_numbers):
  # length = len(numbers)
  # password.append(numbers[random.randint(0, length-1)])
  password.append(random.choice(numbers))

# # Print Password out and Use ''.join to skip brackets
# print(f"\nEasy Level Password: "+''.join(password))

# # Use random.sample(string, count) to randomly get each characters in the string and Use ''.join to skip brackets
# n = len(password)
# print("Hard Level Password: "+''.join(random.sample(password,n)))

# print password without any module
# use random.shuffle()
print("")
print(f"Easy level Password: {password}")
random.shuffle(password)
print(f"Hard level Password: {password}")

# copy strings from the "List type" to another "String type"
password_string = ''
for char in password:
  password_string += char

print(f"\nAfter transfering from List to String type: {password_string}")
