import random

def Subtraction():
    rand1 = random.randint(0, 10000)
    rand2 = random.randint(0, 10000)
    print(f"What is {rand1} - {rand2}?")
    res = int(input("Your Answer: "))
    ans = rand1 - rand2
    return res, ans

__all__ = ['Subtraction']
