# Modify the two-number calculator problem and solve it using functions for add, sub etc. Return the results from
# these functions and display them in main.

def sub(num1, num2):
    return num1-num2


def add(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


n1 = float(input("Enter the first No. : "))
n2 = float(input("Enter the Second No. : "))
op = input("Enter the operator +/-* : ")
if op == '*':
    print(mul(n1, n2))
elif op == '-':
    print(sub(n1, n2))
elif op == '/':
    print(div(n1, n2))
elif op == '+':
    print(add(n1, n2))
