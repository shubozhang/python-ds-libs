import numpy as np

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1)

print(arr1 * arr1)

print(arr1 - arr1)

print(1 / arr1)

print(arr1 ** 3)


############# Index
arange = np.arange(0, 11)
print(arange)

slice_arr = arange[1:5]
print(slice_arr)
slice_arr[:] = 99
print(slice_arr)

arange[0: 5] = 100
print(arange)


############### Copy
print(arange)
arr_copy = arange.copy()
arr_copy[:] = 1
print(arr_copy)
print(arange)



############### 2-D
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print(arr_2d)
print(arr_2d[1])


############ Array Tansposition
arr = np.arange(50).reshape((10, 5))
print(arr)
print(arr.T)
print(np.dot(arr.T, arr))

arr3d = np.arange(50).reshape((5, 5, 2))
print(arr3d)
print(arr3d.transpose((1, 0, 2)))

arr = np.array([[1, 2, 3]])
print(arr)
print(arr.swapaxes(0, 1))



############# Universal array function
arr = np.arange(11)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))


### Binary function
A = np.random.randn(10)
print(A)
B = np.random.randn(10)
print(B)

print(np.add(A, B))
print(np.maximum(A, B))