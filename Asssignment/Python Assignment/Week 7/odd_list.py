odlist = []
odListTot = int(input("Total List Items to enter = "))

for i in range(1, odListTot + 1):
    odListvalue = int(input("Please enter the %d List Item = "  %i))
    odlist.append(odListvalue)


print('\nPrinting the List Items at Odd Position')
for i in range(0, len(odlist), 2):
    print(odlist[i], end = '  ')