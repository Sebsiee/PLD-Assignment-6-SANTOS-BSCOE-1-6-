import random

def equation():
    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq1 = input(str(f"1st Equation: {firstNumber} + {secondNumber} = "))
    sol1 = firstNumber + secondNumber
    if int(eq1) == sol1:
        print("Correct.")
        cp1 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol1}")
        cp1 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq2 = input(str(f"2nd Equation: {firstNumber} + {secondNumber} = "))
    sol2 = firstNumber + secondNumber
    if int(eq2) == sol2:
        print("Correct.")
        cp2 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol2}")
        cp2 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq3 = input(str(f"3rd Equation: {firstNumber} + {secondNumber} = "))
    sol3 = firstNumber + secondNumber
    if int(eq3) == sol3:
        print("Correct.")
        cp3 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol3}")
        cp3 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq4 = input(str(f"4th Equation: {firstNumber} + {secondNumber} = "))
    sol4 = firstNumber + secondNumber
    if int(eq4) == sol4:
        print("Correct.")
        cp4 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol4}")
        cp4 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq5 = input(str(f"5th Equation: {firstNumber} + {secondNumber} = "))
    sol5 = firstNumber + secondNumber
    if int(eq5) == sol5:
        print("Correct.")
        cp5 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol5}")
        cp5 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq6 = input(str(f"6th Equation: {firstNumber} + {secondNumber} = "))
    sol6 = firstNumber + secondNumber
    if int(eq6) == sol6:
        print("Correct.")
        cp6 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol6}")
        cp6 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq7 = input(str(f"7th Equation: {firstNumber} + {secondNumber} = "))
    sol7 = firstNumber + secondNumber
    if int(eq7) == sol7:
        print("Correct.")
        cp7 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol7}")
        cp7 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq8 = input(str(f"8th Equation: {firstNumber} + {secondNumber} = "))
    sol8 = firstNumber + secondNumber
    if int(eq8) == sol8:
        print("Correct.")
        cp8 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol8}")
        cp8 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq9 = input(str(f"9th Equation: {firstNumber} + {secondNumber} = "))
    sol9 = firstNumber + secondNumber
    if int(eq9) == sol9:
        print("Correct.")
        cp9 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol9}")
        cp9 = 0

    firstNumber = random.randint(0,99)
    secondNumber = random.randint(0,99)
    eq10 = input(str(f"10th Equation: {firstNumber} + {secondNumber} = "))
    sol10 = firstNumber + secondNumber
    if int(eq10) == sol10:
        print("Correct.")
        cp10 = 1
    else:
        print("Wrong.")
        print(f"Correct Answer is: {sol10}")
        cp10 = 0
    
    points = cp1 + cp2 + cp3 + cp4 + cp5 + cp6 + cp7 + cp8 + cp9 + cp10
    print("")
    print(f"Total Points: {points}/10")


equation()
