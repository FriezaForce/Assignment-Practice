lst = []

num = int(input("Enter how many numbers you want to enter:"))

for n in range(1, num+1):
    numbers = int(input("Enter a number:"))
    lst.append(numbers)

lst.sort()

print("second largest number in a list is ", lst[-2])