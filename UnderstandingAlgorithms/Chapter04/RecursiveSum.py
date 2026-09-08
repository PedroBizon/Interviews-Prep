def recursive_sum(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + recursive_sum(arr[1:])

def tests():
    arr = []

    for i in range(1, 10):
        arr.append(i)

    print(arr)
    print(recursive_sum(arr))

    arr = []

    for i in range(0, 10, 2):
        arr.append(i)

    print(arr)
    print(recursive_sum(arr))

tests()