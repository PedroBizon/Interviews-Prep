def iterative_binary_search(ordered_list, target):
    start = 0
    finish = len(ordered_list) - 1

    while start < finish:
        middle = (start+finish) // 2
        
        if ordered_list[middle] == target:
            return middle

        if ordered_list[middle] > target:
            finish = middle

        else:
            start = middle + 1

    if(start == finish):
        if ordered_list[start] == target:
            return start

    return None

def recursive_binary_search(ordered_list, start, finish, target):
    if(start == finish and ordered_list[start] != target):
        return None
    
    middle = (start + finish) // 2

    if (ordered_list[middle] == target):
        return middle
    elif (ordered_list[middle] > target):
        return recursive_binary_search(ordered_list, start, middle, target)
    else:
        return recursive_binary_search(ordered_list, middle+1, finish, target)

def testes():
    arr1 = range(0, 100, 2)
    arr2 = range(0,100)
    arr3 = range(0, 10000)
    arr4 = range(0, 100000, 10)


    print("Iterative tests:")
    print(iterative_binary_search(arr1, 12))
    print(iterative_binary_search(arr2, 50))
    print(iterative_binary_search(arr3, 9000))
    print(iterative_binary_search(arr4, 12345))
    
    print("Recusive tests:")
    print(recursive_binary_search(arr1, 0, len(arr1)-1, 12))
    print(recursive_binary_search(arr2, 0, len(arr2)-1, 50))
    print(recursive_binary_search(arr3, 0, len(arr3)-1, 9000))
    print(recursive_binary_search(arr4, 0, len(arr4)-1, 12345))

testes()