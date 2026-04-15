#(3×3) Array → Row sum, Column sum, 2nd Maximum 
import numpy as np

arr = np.array([[3, 8, 1],
                [5, 7, 9],
                [2, 6, 4]])

print("Array:\n", arr)

# Row-wise sum
row_sum = np.sum(arr, axis=1)
print("Row-wise sum:", row_sum)

# Column-wise sum
col_sum = np.sum(arr, axis=0)
print("Column-wise sum:", col_sum)

# 2nd maximum element
flat = arr.flatten()
second_max = np.sort(flat)[-2]

print("Second maximum element:", second_max)