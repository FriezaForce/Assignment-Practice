char = input("Please Enter Your Own Character : ")

if(char.isupper()):
    print("The Given Character ", char, "is an Uppercase Alphabet")
elif(char.islower()):
    print("The Given Character ", char, "is a Lowercase Alphabet")
else:
    print("The Given Character ", char, "is Not a Lower or Uppercase Alphabet")