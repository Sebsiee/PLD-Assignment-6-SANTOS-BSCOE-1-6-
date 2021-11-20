def introduction():
    print("Welcome to my Program 1 - Highest to Lowest!")

def highestToLowest(): 
    while True:
            try:
                firstNo = float(input("Enter 1st number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break

    while True:
            try:
                secondNo = float(input("Enter 2nd number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break

    while True:
            try:
                thirdNo = float(input("Enter 3rd number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break

    while True:
            try:
                fourthNo = float(input("Enter 4th number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break

    allNumbers = [firstNo, secondNo, thirdNo, fourthNo]
    highestNumber = allNumbers[0] 
    lowestNumber = allNumbers[0] 
    secondHighest = None
    thirdHighest = None
    for item in allNumbers[1:]:     
        if item > highestNumber: 
            secondHighest = highestNumber
            highestNumber = item 
        elif secondHighest == None or secondHighest < item: 
            secondHighest = item 
        if item < lowestNumber: 
            thirdHighest = lowestNumber
            lowestNumber = item 
        elif thirdHighest == None or thirdHighest > item: 
            thirdHighest = item 
    first = "%.0f" % highestNumber
    second = "%.0f" % secondHighest
    third = "%.0f" % thirdHighest
    fourth = "%.0f" % lowestNumber
    print(f"Highest to Lowest: {first}, {second}, {third}, {fourth}")

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
highestToLowest()
goodbye()