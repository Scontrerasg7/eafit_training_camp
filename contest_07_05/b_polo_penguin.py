import numpy as np

def find_closest_number(matrix, A):
    flattened_matrix = matrix.flatten() 
    absolute_diff = np.abs(flattened_matrix - A)  
    closest_index = np.argmin(absolute_diff)  
    closest_number = flattened_matrix[closest_index]  
    return closest_number, flattened_matrix

# 1. Read the inputs
n, m, k = input().split(' ')
n = int(n)
m = int(m)
k = int(k)

# 2. Initialize the matrix
matrix = np.zeros((n,m))
for i in range(n):
    row = input().split(' ')
    matrix[i,:] = [int(x) for x in row]

# 3. Find the mean
mean = np.mean(matrix)

# 4. Evaluate
if mean % 1 != 0:
    print(-1)
else:
    closest_number, flattened_matrix = find_closest_number(matrix, mean)
    subtracts = np.abs(flattened_matrix - closest_number)
    number_of_operations = int(np.sum(subtracts / k))
    print(number_of_operations)