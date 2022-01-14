
# list comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Jojo"
new_list = [letter for letter in name]
print(new_list)

new_list = [num*2 for num in range(1,5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
caps_long = [name.upper() for name in names if len(name) > 5]
print(caps_long)

# dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score >= 65}
print(passed_students)

# looping through pandas

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
# pandas loop through rows
for (index, row) in student_df.iterrows():
    print(row.score)
    