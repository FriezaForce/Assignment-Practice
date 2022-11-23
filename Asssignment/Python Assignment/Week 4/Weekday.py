weekday = int(input("Enter weekday number (1-7) : "))

def week(weekday):
    if weekday == 1 :
        return("\nMonday")
    elif weekday == 2 :
        return("\nTuesday")
    elif(weekday == 3) :
        return("\nWednesday")
    elif(weekday == 4) :
        return("\nThursday")
    elif(weekday == 5) :
        return("\nFriday")
    elif(weekday == 6) :
        return("\nSaturday")
    elif (weekday == 7) :
        return("\nSunday")
    else :
        return("\nEnnter correct Number")

print(week(weekday))