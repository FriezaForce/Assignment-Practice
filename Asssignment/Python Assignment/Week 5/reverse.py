
given_num = int(input("Enter any number:"))

reverse_number = 0



while (given_num > 0):

    remainder = given_num % 10
    reverse_number = (reverse_number * 10) + remainder
    given_num = given_num // 10


print("The reversed number =", reverse_number)