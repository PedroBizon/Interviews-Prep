from random import randint

def fill_hash(hash, n):
    for _ in range(n//2):
        key = randint(0, n)
        value = randint(0, n)

        hash[key] = value  

    return hash

def search(hash: dict, num):
    if num in hash.keys():
        return True

    return False

def tests():
    # Test 1
    hash1 = {}
    hash1 = fill_hash(hash1, 10)
    if search(hash1, 5):
        print(hash1[5])
    else: 
        print(f'Number not found')

    hash2 = {}
    hash2 = fill_hash(hash2, 10000)
    if search(hash2, 10):
        print(hash2[10])
    else:
        print(f'Number not found')

tests()