import random
from availableTests.addition import Addition
from availableTests.subtraction import Subtraction
from availableTests.multiplication import Multiplication
from availableTests.division import Division
result = 0
wrong = []
availableTests = {
    'Addition': Addition,
    'Subtraction': Subtraction,
    'Multiplication': Multiplication,
    'Division': Division
}

def ask():
    print("Choose A Test Simulation:")
    for test in availableTests.keys():
        print(test)

def conclude():
    print(f"You got {result}% correct!")
    if wrong:
        print("Incorrect answers:")
        for wrong_answer in wrong:
            print(wrong_answer)

def menu():
    global result, wrong
    ask()
    choice = input("Your Choice: ")

    test_function = availableTests.get(choice)
    if test_function:
        for _ in range(10):
            res, ans = test_function()
            result += 10
            if res == ans:
                print("Correct!")
            else:
                format = f"question { _ + 1} is wrong. Your answer was {res}. The correct answer was {ans}. Failure."
                wrong.append(format)
                result -= 10
                
    else:
        print("Invalid choice.")
        return

    conclude()

menu()






