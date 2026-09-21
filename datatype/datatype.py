#2. Data Types

#1. Demonstrate int, float, str, bool, and complex.
a = 10
b = 10.5
c = "Hello"
d = True
e = 2 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#2. Accept two numbers and display their data types.
a = int(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Type of a =", type(a))
print("Type of b =", type(b))
#3. Convert a string number into an integer and float.
x = "25"

a = int(x)
b = float(x)

print("Integer =", a)
print("Float =", b)
#4. Find the length of a string.
name = input("Enter a string: ")

print("Length =", len(name))
#5. Create a list, tuple, set, and dictionary and displaytheir types.

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = {"name": "john", "age": 20}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
