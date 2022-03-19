# Input a number and Print numbers up to that number in reverse
from itertools import count
from tokenize import Number


num = int(input("Enter the no. : "))


def pr(number, count):
    if(count < number):
        pr(number, count+1)
    print(number)


pr(num, 1)
