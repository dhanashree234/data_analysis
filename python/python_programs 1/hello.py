print("hello")
print("text1")
print("text2")
print("text3")


# python variables and datatypes

# print employee details
name = "John"
age = 20
salary = float(50000)

print("Name :", name)
print("Age :", age)
print("Salary :", salary)

formatString = f"|=================================================|"
print(formatString)
print(f"|Emp name \t |\tage  \t |\tsalary    |")
print(formatString)
print(f"|{name} \t\t |\t{age} \t |\t{salary}  |")
print(formatString)

# Python Variables - Assign Multiple Values
# print cities
city1, city2, city3 = "city1", "city2", "city3"
print("\n\n")
print(formatString)
print(f"|  {city1}\t |\t{city2}\t |\t{city3} \t  |")
print(formatString)

# datatypes
# integer 
marks = 30
price = 30.0
print(type(marks))
print(type(age))
print(type(name))
print(type(price))

# lists are mutable - we can add new elements, elements can be repeated
list1 = [10,10,20,30]
print(list1)

# tuple are immutable - we cannot add or modify new elements, same element can occur multiple times
tuple1 = (10,20,30)
print(tuple1)

# dictionary - key value pair
dict1 = {"name":"John"}
print(dict1)