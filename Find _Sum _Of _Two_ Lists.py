# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# result = []

# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])

# print(result)
import numpy as np
list1 = np.array([1, 2, 3])
list2 = np.array([4, 5, 6])
result = list1 + list2
print(result)