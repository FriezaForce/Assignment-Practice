#prime Number

import math 

num = int(input("Enter a number to check its type: "))
flag = False


if num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break


if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


#Armstrong Number

Sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    Sum += digit ** 3
    temp //= 10

# display the result
if num == Sum:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")

#=================================================================================================
#Strong Number Check

Sum = 0
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    Sum=Sum+f
    num=num//10
if(Sum==temp):
    print("Given number is a strong number")
else:
    print("Given number is not a strong number")

#======================================================================================================
#Magic Number Check

def Magic(num):
    Sum = 0
    
    while (num > 0 or Sum > 9):
        if (num == 0):
            num = Sum
        Sum = 0
    Sum = Sum + num % 10
    num = int(num / 10)
    return True if (Sum == 1) else False


if (Magic(num)):
    print("Given number is a Magic Number.")
else:
    print("Given number is not a Magic Number.")

#=================================================================================================
#Perect Number Check
Sum = 0
for i in range(1, num):
    if(num % i == 0):
        Sum = Sum + i
if (Sum == num):
    print("Given  number is a Perfect number!")
else:
    print("Given number is not a Perfect number!")
    
#===============================================================================

