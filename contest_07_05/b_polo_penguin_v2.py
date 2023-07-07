import numpy as np

# 0. Function that finds the closes number to A in a matrix
def find_closest_number(matrix, A):
    flattened_matrix = matrix.flatten() 
    absolute_diff = np.abs(flattened_matrix - A)  
    closest_index = np.argmin(absolute_diff)  
    closest_number = flattened_matrix[closest_index]  
    return closest_number, flattened_matrix

# 1. Read the inputs
n, m, k = map(int, input().split())

# 2. Initialize the matrix
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 3. Find the mean
total_sum = 0
for row in matrix:
    total_sum += sum(row)
mean = total_sum / (n * m)

# 4. Evaluate
if mean % 1 != 0:
    # If the mean is not an integer, then it is not possible to, print -1
    print(-1)
else:
    # Find the closest number
    closest_number, flattened_matrix = find_closest_number(np.array(matrix), mean)
    # Subtract the closest number from the matrix and divide by k, then sum to find the number of operations
    subtracts = np.abs(flattened_matrix - closest_number)
    number_of_operations = int(np.sum(subtracts / k))
    print(number_of_operations)
