import random

#
# numbers = [1, 2, 3]
#
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
#
# name = 'Angela'
#
# new_list = [letter for letter in name]
# print(new_list)
#
# # a_range = [1,2,3,4]
# # new_range = [num*2 for num in a_range]
# new_range = [num*2 for num in range(1,5)]
# print(new_range)
#
# names = ['Alex', 'Beth', 'Caroline', 'Elanor', 'Freddie']
# upper_case_long_name = [name.upper() for name in names if len(name)>5]
# print(upper_case_long_name)

#
# Practice Dict Comprehension:
#
# students_list = ['Alex', 'Beth', 'Caroline', 'Elanor', 'Freddie']
# student_score = {student:random.randint(1, 100) for student in students_list}
# print(student_score)
# #passed_student = {student:student_score[student] for student in student_score if student_score[student] >= 60}
#
# print(student_score.items())
# passed_student = {student:score for (student,score) in student_score.items() if score >=60}
#
# print(passed_student)

#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# result = {char:len(char) for char in sentence.split()}
#
# # Write your code below:
#
#
# print(result)


# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f:
#
# (temp_c * 9/5) + 32 = temp_f
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# Don't change code above
# Write your code 👇 below:
weather_f = {date: (temp_c * 9 / 5) + 32 for (date, temp_c) in weather_c.items()}
print(weather_f)
