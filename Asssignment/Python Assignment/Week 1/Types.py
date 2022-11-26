user_input = input("Enter something ")

try:
    val = int(user_input)
    print("Input is an integer")
except ValueError:
    try:
        val = float(user_input)
        print("Input is a float")
    except ValueError:
        print("It's a string")