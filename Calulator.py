n1 = float(input("First number: "))
n2 = float(input("Second number: "))
operation = input("+ - * / ")

if operation == "+":
    maths = n1 + n2
elif operation == "-":
    maths = n1 - n2
elif operation == "*":
    maths = n1 * n2
elif operation == "/":
    maths = n1 / n2

print("The answer is " + str(maths))
print("Computing Done")
