# 8)Write a Python program to create a list containing five fruits and print the complete list, first fruit, and last fruit.
fruits = ["fruit1", "fruit2", "fruit3", "fruit4", "fruit5"]

print(fruits)
print(f"First item - {fruits[0]} \t last item - {fruits[-1]}")
      
# 9)Write a Python program to create a tuple containing five numbers and print the second and fourth numbers.
num_tuple = (1, 2, 3, 4, 5)

length = len(num_tuple)

print(f"Second tuple element : {num_tuple[length - 4]}\t fourth element : {num_tuple[length - 2]}")

print(f"Second tuple element : {num_tuple[1]}\t fourth element : {num_tuple[3]}")

# 10)Write a Python program to create a dictionary containing a student's name, age, and mark. Print each value separately
# Create a dictionary containing student's details
student = {
    "name": input("Enter student name: "),
    "age": int(input("Enter student age: ")),
    "mark": float(input("Enter overall mark: "))
}

# Print each value separately
print("\nStudent Details")
print("Name:", student["name"])
print("Age:", student["age"])
print("Overall Mark:", student["mark"])

# List of subjects
subjects = ["Math", "Science", "English"]

# Dictionary to store subject names and marks
marks = {}

# Input marks using for loop and range
for i in range(len(subjects)):
    marks[subjects[i]] = int(input(f"Enter marks for {subjects[i]}: "))

# Print subject marks
print("\nSubject Marks")
for subject, mark in marks.items():
    print(subject + ":", mark)