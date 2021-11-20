def highestToLowest(allNumbers): 
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
    print(f"Order of Highest to Lowest: {first}, {second}, {third}, {fourth}")

firstNo = float(input("Enter 1st number: "))
secondNo = float(input("Enter 2nd number: "))
thirdNo = float(input("Enter 3rd number: "))
fourthNo = float(input("Enter 4th number: "))
allNumbers = [firstNo, secondNo, thirdNo, fourthNo]


highestToLowest(allNumbers)