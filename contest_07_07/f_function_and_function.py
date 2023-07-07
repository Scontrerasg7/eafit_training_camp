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

def recursive_function(x, k):
    if k == 0:
        return x
    
    elif x == 0:
        if k % 2 == 0:
            return 0
        else:
            return 1
        
    elif x == 1 or x == 2:
        if k % 2 == 0:
            return 1
        else:
            return 0
        
    else:
        return recursive_function(real_g_4_life(x), k - 1)

for _ in range(test_cases):
    x, k = map(int, input().split())
    print(recursive_function(x, k))