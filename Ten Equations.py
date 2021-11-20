import random

def introduction():
    print("Welcome to my Program 2 - Ten Equations!")

def equation():
    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq1 = int(input(f"1st Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol1 = firstNumber + secondNumber
        if int(eq1) == sol1:
            print("Correct.")
            cp1 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol1}")
            cp1 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq2 = int(input(f"2nd Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol2 = firstNumber + secondNumber
        if int(eq2) == sol2:
            print("Correct.")
            cp2 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol2}")
            cp2 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq3 = int(input(f"3rd Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol3 = firstNumber + secondNumber
        if int(eq3) == sol3:
            print("Correct.")
            cp3 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol3}")
            cp3 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq4 = int(input(f"4th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol4 = firstNumber + secondNumber
        if int(eq4) == sol4:
            print("Correct.")
            cp4 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol4}")
            cp4 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq5 = int(input(f"5th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol5 = firstNumber + secondNumber
        if int(eq5) == sol5:
            print("Correct.")
            cp5 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol5}")
            cp5 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq6 = int(input(f"6th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol6 = firstNumber + secondNumber
        if int(eq6) == sol6:
            print("Correct.")
            cp6 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol6}")
            cp6 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq7 = int(input(f"7th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol7 = firstNumber + secondNumber
        if int(eq7) == sol7:
            print("Correct.")
            cp7 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol7}")
            cp7 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq8 = int(input(f"8th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol8 = firstNumber + secondNumber
        if int(eq8) == sol8:
            print("Correct.")
            cp8 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol8}")
            cp8 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq9 = int(input(f"9th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol9 = firstNumber + secondNumber
        if int(eq9) == sol9:
            print("Correct.")
            cp9 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol9}")
            cp9 = 0
        break

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    while True:
        try:
            eq10 = int(input(f"10th Equation: {firstNumber} + {secondNumber} = "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        sol10 = firstNumber + secondNumber
        if int(eq10) == sol10:
            print("Correct.")
            cp10 = 1
        else:
            print("Wrong.")
            print(f"Correct Answer is: {sol10}")
            cp10 = 0
        break
        
    points = cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7 + cp8 + cp9 + cp10
    print("")
    print(f"Total Points: {points}/10")
    
def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
equation()
goodbye()