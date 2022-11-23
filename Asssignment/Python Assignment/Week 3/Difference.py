n = int(input("Enter any number:"))

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
        


print(difference(n))
