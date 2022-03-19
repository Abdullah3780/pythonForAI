# Write a function with the name of fact, which calculate factorial of a value that is sent as an argument
num = int(input("Enter the number : "))


def fact(number):
    if(number == 1):
        return 1
    else:
        factorial = number * fact(number-1)
        return factorial


print(fact(num))
