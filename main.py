from availableTests.addition import *
from availableTests.subtraction import *
from availableTests.multiplication import *
from availableTests.division import *

import math
import random

availableTests = ['Addition', 'Subtraction', 'Multiplication', 'Division']
result = 0

def ask():
    print("Choose a Test Simulation:")
    for test in availableTests:
        print(test)

def conclude():
    print(f"You got {result}% correct")

def menu():
    global result
    ask()
    choice = input("Your Choice: ")
    
    if choice == 'Addition':
        for _ in range(10):
            res, ans = Addition()
            if res == ans:
                result += 10

    elif choice == 'Subtraction':
        for _ in range(10):
            res, ans = Subtraction()
            if res == ans:
                result += 10

    elif choice == 'Multiplication':
        for _ in range(10):
            res, ans = Multiplication()
            if res == ans:
                result += 10

    elif choice == 'Division':
        for _ in range(10):
            res, ans = Division()
            if res == ans:
                result += 10
    
    conclude()

menu()




