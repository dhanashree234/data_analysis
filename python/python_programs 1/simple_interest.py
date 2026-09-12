# 11)Write a Python program to store principal amount, rate of interest, and time using variables and calculate the simple interest.
# Input principal amount, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("\nPrincipal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)