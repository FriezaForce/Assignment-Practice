lst=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    lst.append(b)
lst.sort(key=len)
print(lst)