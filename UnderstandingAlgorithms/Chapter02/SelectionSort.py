from random import randint

def selection_sort(arr:list)-> list:
    ordered_arr = []
    arr_size = len(arr)
    
    for i in range(arr_size):
        smallest = arr[0]

        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]

        ordered_arr.append(smallest)
        arr.remove(smallest)

    return ordered_arr


def test():
    arr = []

    for i in range(10):
        arr.append(randint(1, 1000))

    print("Unordered Array:")
    print(arr)

    arr = selection_sort(arr)

    print("Ordered Array:")
    print(arr)

test()