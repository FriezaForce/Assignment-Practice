lst  = []

num = int(input("Enter how many number you want to enter:"))

for n in range(num):
    numbers = int(input("Enter a number:"))
    lst.append(numbers)

print("Maximum number in given list is ", max(lst))

