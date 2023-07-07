class RecursiveExit(Exception):
    pass

# 1. Read the inputs
# 1.1 Read the number of test cases
test_cases = int(input())

# 2. Create the recursive function that returns
# the number of enclosed areas in a number
enclosed_areas = {
    0: 1,
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7: 0,
    8: 2,
    9: 1
}

def real_g_4_life(x):
    digits = [int(digit) for digit in str(x)]
    return sum([enclosed_areas[digit] for digit in digits])

# Memoization cache
memo = {}

def recursive_function(x, k):
    if k == 0:
        return x
    
    elif x == 0 or x == 4 or x == 6 or x == 9:
        if k % 2 == 0:
            raise RecursiveExit(0)
        else:
            return RecursiveExit(1)
        
    elif x == 1 or x == 2 or x == 3 or x == 5 or x == 7:
        if k % 2 == 0:
            return RecursiveExit(1)
        else:
            return RecursiveExit(0)
        
    else:
        result = recursive_function(real_g_4_life(x), k - 1)
        memo[(x, k)] = result
        return result


for _ in range(test_cases):
    x, k = map(int, input().split())
    try:
        print(recursive_function(x, k))
    except RecursiveExit as e:
        print(e)
