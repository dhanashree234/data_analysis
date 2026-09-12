# 4)Write a Python program to store marks of three subjects and calculate the total and average.

marks1 = 9
marks2 = 10
marks3 = 8

total = marks1.__add__(marks2).__add__(marks3)
average = total/3

print(f"Total = {total} \nAverage = {average}")

# using list
marks = [10, 9, 8]

total = 0

for m in marks:
    total += m

average = total / len(marks)

print(f"Marks : {marks}\t Total = {total}\t Average = {average}")

# using tuple
marks = (10, 9, 8)

total = 0

for m in marks:
    total += m

average = total / len(marks)

print(f"Marks : {marks}\t Total = {total}\t Average = {average}")

# using dictionary

marks_dict = {"marks1": 10, "marks2": 9, "marks3": 8}

print(type(marks_dict["marks1"]))

total = 0

for subject in marks_dict:
    total += marks_dict[subject]

average = total / len(marks_dict)

print(f"Total = {total} \nAverage = {average}")


    