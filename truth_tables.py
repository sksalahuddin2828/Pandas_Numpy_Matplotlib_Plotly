import numpy as np
import pandas as pd

# Helper function to create truth tables
def create_truth_table(propositions, operation):
    n = len(propositions)
    m = 2 ** n
    truth_table = np.zeros((m, n + 1), dtype=int)
    for i in range(n):
        truth_table[:, i] = (np.arange(m) // (2 ** i)) % 2
    truth_table[:, n] = operation(*[truth_table[:, i] for i in range(n)]).astype(int)
    return truth_table

# 1. Prove that X ⨁ Y ≅ (X ∧ ∼Y) ∨ (∼X ∧ Y).
X = np.array([True, True, False, False])
Y = np.array([True, False, True, False])

result_XOR = X ^ Y
result_AND_OR = (X & ~Y) | (~X & Y)

are_equivalent = np.array_equal(result_XOR, result_AND_OR)

print("Truth Table for X ⨁ Y:")
print(pd.DataFrame({"X": X, "Y": Y, "X ⨁ Y": result_XOR}))

print("\nTruth Table for (X ∧ ∼Y) ∨ (∼X ∧ Y):")
print(pd.DataFrame({"X": X, "Y": Y, "(X ∧ ∼Y) ∨ (∼X ∧ Y)": result_AND_OR}))

print("\nAre the expressions equivalent?", are_equivalent)

# 2. Show that (p ⨁ q) ∨ (p ↓ q) is equivalent to p ↑ q.
p = np.array([True, True, False, False])
q = np.array([True, False, True, False])

result_XOR_NOR = (p ^ q) | ~(p | q)
result_NAND = ~(p & q)

are_equivalent = np.array_equal(result_XOR_NOR, result_NAND)

print("\nTruth Table for (p ⨁ q) ∨ (p ↓ q):")
print(pd.DataFrame({"p": p, "q": q, "(p ⨁ q) ∨ (p ↓ q)": result_XOR_NOR}))

print("\nTruth Table for p ↑ q:")
print(pd.DataFrame({"p": p, "q": q, "p ↑ q": result_NAND}))

print("\nAre the expressions equivalent?", are_equivalent)


# Answer: Truth Table for X ⨁ Y:
#         X      Y  X ⨁ Y
#         0   True   True  False
#         1   True  False   True
#         2  False   True   True
#         3  False  False  False

#         Truth Table for (X ∧ ∼Y) ∨ (∼X ∧ Y):
#               X      Y  (X ∧ ∼Y) ∨ (∼X ∧ Y)
#         0   True   True                False
#         1   True  False                 True
#         2  False   True                 True
#         3  False  False                False

#         Are the expressions equivalent? True

#         Truth Table for (p ⨁ q) ∨ (p ↓ q):
#               p      q  (p ⨁ q) ∨ (p ↓ q)
#         0   True   True              False
#         1   True  False               True
#         2  False   True               True
#         3  False  False               True

#         Truth Table for p ↑ q:
#               p      q  p ↑ q
#         0   True   True  False
#         1   True  False   True
#         2  False   True   True
#         3  False  False   True

#         Are the expressions equivalent? True
