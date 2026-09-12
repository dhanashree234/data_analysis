# 12)Write a Python program to swap the values of two variables using a third variable.
# Input two variables
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display values before swapping
print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swap using a third variable
temp = a
a = b
b = temp

# Display values after swapping
print("\nAfter swapping:")
print("a =", a)
print("b =", b)