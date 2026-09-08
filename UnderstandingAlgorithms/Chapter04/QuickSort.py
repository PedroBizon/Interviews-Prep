from random import randint

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)

    ordered = []
    for i in left:
        ordered.append(i)

    ordered.append(pivot)

    for i in right:
        ordered.append(i)

    return ordered

def tests():
    arr = []
    for i in range(10):
        arr.append(randint(0,10))

    print("Unordered Array:")
    print(arr)

    arr = quick_sort(arr)

    print("Ordered array: ")
    print (arr)

tests()