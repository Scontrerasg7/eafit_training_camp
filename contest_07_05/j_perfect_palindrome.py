from collections import Counter
# 0. Function that returns the number of characters that are different
#    to the one that repeats the most

def number_of_diferents(string):
    char_counts = Counter(string)
    # 0.1. Get the most common character and its count
    most_common_char, most_common_count = char_counts.most_common(1)[0] 
    
    # 0.2. Get the number of different characters
    different_chars_count = len(string) - most_common_count
    return different_chars_count


# 1. Read the input, first line: number of test cases
test_cases = int(input())

for test in range(test_cases):
    # 2. Read the input, second line: string
    string = input()
    # 3. Get the number of different characters
    print(number_of_diferents(string))
