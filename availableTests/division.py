import random
def Division():
    rand1 = random.randint(1, 15)
    rand2 = random.randint(1, 15)
    # Ensure the division is a whole number
    product = rand1 * rand2
    print(f"What is {product} ÷ {rand1}?")
    res = int(input("Your Answer: "))
    ans = rand2
    return res, ans

__all__ = ['Division']