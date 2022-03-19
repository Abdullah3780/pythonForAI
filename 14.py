# Write a function, which takes 5 arguments and print the larges and smallest
from turtle import st


def largeset_smallest(num1, num2, num3, num4, num5):
    smallest = 0
    largest = 0
    if (num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5):
        smallest = num1
    if (num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5):
        psmallest = num2
    if (num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5):
        smallest = num3
    if (num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5):
        smallest = num4
    if (num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4):
        smallest = num5
    # Largest
    if (num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5):
        largest = num1
    if (num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5):
        largest = num2
    if (num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5):
        largest = num3
    if (num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5):
        largest = num4
    if (num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4):
        largest = num5
    print(str(smallest)+" is Smallest and "+str(largest)+" is largest")


largeset_smallest(4, 3, 5, 6, 3)
