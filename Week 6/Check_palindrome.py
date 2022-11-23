
num = input("Enter any number : ")

reverse = str(num)[::-1]

print()

if reverse == num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")