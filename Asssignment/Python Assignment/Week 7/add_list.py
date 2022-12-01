list1 = []
list2 = []

num1 = int(input("Enter how many number to add in list 1:"))
for i in range(1, num1+1):
    number1 = int(input("Enter values for list 1:"))
    list1.append(number1)

num2 = int(input("Enter how many number to add in list 2:"))
for x in range(1,num2+1):
    number2 = int(input("Enter values for list 2:"))
    list2.append(number2)

list3=list1+list2
print("The merged list is ", list3)
list3.sort()
print("The sorted list is ", list3)