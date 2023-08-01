import numpy as np

# Example multisets
set_A = [1, 1, 2, 3, 3, 3, 4]
set_B = [3, 3, 4, 4, 5]

# Union of multisets
union_result = np.union1d(set_A, set_B)
print("Union of sets A and B:", union_result)

# Intersection of multisets
intersection_result = np.intersect1d(set_A, set_B)
print("Intersection of sets A and B:", intersection_result)

# Difference of multisets
difference_result = np.setdiff1d(set_A, set_B)
print("Difference of sets A and B:", difference_result)

# Sum of multisets
sum_result = np.concatenate((set_A, set_B))
print("Sum of sets A and B:", sum_result)


# Answer: Union of sets A and B: [1 2 3 4 5]
#         Intersection of sets A and B: [3 4]
#         Difference of sets A and B: [1 2]
#         Sum of sets A and B: [1 1 2 3 3 3 4 3 3 4 4 5]
