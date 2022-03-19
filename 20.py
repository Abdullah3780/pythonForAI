index = int(input("Enter the index : "))
listofValue = [1, 1]


def fact(number, count):
    if(count <= number-2):  # as first 2 no.s are already added
        ser = listofValue[count] + listofValue[count+1]
        listofValue.append(ser)
        fact(number, count+1)
        return ser


fact(index, 0)
if(index == 0):
    print(0)
print(listofValue)
