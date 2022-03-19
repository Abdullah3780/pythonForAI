# Input a number and print even numbers up to that number
num = int(input("Enter the NO. : "))


def evenNos(number, count):
    if (count < number):
        evenNos(number, count+1)
    if(count % 2 == 0):
        print(count)


evenNos(num, 0)
