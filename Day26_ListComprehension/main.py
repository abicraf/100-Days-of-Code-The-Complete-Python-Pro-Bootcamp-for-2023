#
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers,
# each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
with open("file1.txt", "r") as file_1:
    file1_content = file_1.readlines()
with open("file2.txt", "r") as file_2:
    file2_content = file_2.readlines()


result = [int(number) for number in file1_content if number in file2_content]


# Write your code above 👆

print(result)


