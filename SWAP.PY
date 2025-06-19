# Swapping two numbers using a temporary variable

# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Display before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

# Display after swapping
print(f"After swapping: a = {a}, b = {b}")
