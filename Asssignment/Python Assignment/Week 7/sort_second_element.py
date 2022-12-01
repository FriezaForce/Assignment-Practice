lst = [["Python", 4],["tiger",2],["Dog",6],["elephant",8]]
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if(lst[j][1]>lst[j+1][1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
 
print(lst)