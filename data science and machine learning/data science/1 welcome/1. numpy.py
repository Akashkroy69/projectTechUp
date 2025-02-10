import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype='S')

print(arr)
print(type(arr))
# accessing
print(arr[0])
# SLICING
print(arr[1:3])
# negative indexing
print(arr[-1])
# checking data type
print("data type: ",arr.dtype)

np.zeros((3, 3))   # 3x3 matrix of zeros
np.ones((2, 4))    # 2x4 matrix of ones
np.eye(3)          # Identity matrix of size 3x3
np.full((2, 3), 7) # 2x3 matrix filled with 7


# shape
print("shape: ",arr.shape)
# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])