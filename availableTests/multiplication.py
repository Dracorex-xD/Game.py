import random

def Multiplication():
    rand1 = random.randint(0, 15)
    rand2 = random.randint(0, 15)
    print(f"What is {rand1} x {rand2}?")
    res = int(input("Your Answer: "))
    ans = rand1 * rand2
    return res, ans

__all__ = ['Multiplication']