num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

def sum_thrice(num1, num2, num3):

    sum = num1 + num2 + num3

    if num1 == num3 == num3:
      sum = sum * 3
    return sum

print(sum_thrice(num1, num2, num3))
