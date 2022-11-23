def display(num1, num2):
    results = []
    for i in range(1000, 2000+1):
        if (i%7==0) and (i%5!=0):
            results.append(i)
    return results
num1 = 1000
num2 = 2000
print(display(num1,num2))