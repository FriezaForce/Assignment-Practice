n=int(input("Enter number"))
def Sum(n):    
    sum = 0
    while (n != 0): 
        sum = sum + (n % 10)
        n = n//10
    return sum    

print("Sum of digits",Sum(n))