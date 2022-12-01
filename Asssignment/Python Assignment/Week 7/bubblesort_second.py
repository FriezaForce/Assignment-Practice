lst=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    lst.append(b)
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp 
print('Second largest number is:',lst[n-2])