import numpy as np


my_list1 = [1, 2, 3, 4]
my_array1 = np.array(my_list1)
print(my_array1)

my_list2 = [5, 6, 7, 8]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)
print(my_array2)
print(my_array2.dtype)


my_zeros_array = np.zeros(5)
print(my_zeros_array)
print(my_zeros_array.dtype)


my_ones = np.ones([5, 5])
print(my_ones)

my_empty = np.empty(5, float)
print(my_empty)

my_eye = np.eye(5)
print(my_eye)

my_arange = np.arange(5)
print(my_arange)
my_arange2 = np.arange(5, 50, 3)
print(my_arange2)