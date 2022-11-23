amount = int(input("Enter Amount to be paid : "))

def Currency(amount):
    notes = [2000,500,200,100,50,20,10,5,2,1]
    notesCount = {}

    for note in notes:
        if amount >=note:
            notesCount[note] = amount//note
            amount = amount%note

    print("currency count:")
    for key, val in notesCount.items():
        print(f"{key} : {val}")

Currency(amount)

