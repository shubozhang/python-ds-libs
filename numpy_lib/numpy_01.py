import numpy as np


my_list1 = [1, 2, 3, 4]
my_array1 = np.array(my_list1)
print(my_array1)

my_list2 = [5, 6, 7, 8]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)
print(my_array2)

print(np.zeros(5))