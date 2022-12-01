numlist = []
even = []
odd = []

num = int(input("Enter how many number you want to enter:"))

for n in range(1, num+1):
    number = int(input("Enter any value:"))
    numlist.append(number)

for x in range(num):
    if(numlist[x]%2 == 0):
        even.append(numlist[x])
    else:
        odd.append(numlist[x])

print("values that are even", even)
print("Values that are odd", odd)