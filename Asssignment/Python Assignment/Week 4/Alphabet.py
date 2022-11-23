char = input("Please Enter Any Character : ")

if((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')): 
    print("The Given Character ", char, "is an Alphabet") 
else:
    print("The Given Character ", char, "is a Not an Alphabet")