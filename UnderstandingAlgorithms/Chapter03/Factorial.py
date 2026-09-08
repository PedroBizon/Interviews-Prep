def factorial(num):
    if num == 1:
        return num

    return num * factorial(num - 1)

def tests():
    print("5 factorial: ")
    print(factorial(5))

    print("3 factorial: ")
    print(factorial(3))

    print("10 factorial: ")
    print(factorial(10))

tests()