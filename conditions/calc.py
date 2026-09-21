#7. Create a simple calculator using if-elif-else.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Answer =", a + b)
elif op == "-":
    print("Answer =", a - b)
elif op == "*":
    print("Answer =", a * b)
elif op == "/":
    print("Answer =", a / b)
else:
    print("Invalid operator")
