alist=[]
blist=[]
n1=int(input("Enter number of elements for list1:"))
for x in range(0,n1):
    element=int(input("Enter element" + str(x+1) + ":"))
    alist.append(element)
n2=int(input("Enter number of elements for list2:"))
for x in range(0,n2):
    element=int(input("Enter element" + str(x+1) + ":"))
    blist.append(element)

intersection = [value for value in alist if value in blist]

print(intersection)